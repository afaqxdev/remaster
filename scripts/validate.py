#!/usr/bin/env python3
"""Validate the Remaster package: skill frontmatter, local links, manifests, assets. Exit 1 on any error."""
import json
import re
import sys
import xml.dom.minidom
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


# 1. Skills
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    err("no skills/*/SKILL.md found")
for skill in skills:
    rel = skill.relative_to(ROOT)
    fm = frontmatter(skill.read_text())
    if fm is None:
        err(f"{rel}: missing YAML frontmatter")
        continue
    name, desc = fm.get("name", ""), fm.get("description", "")
    if name != skill.parent.name:
        err(f"{rel}: name '{name}' must match folder '{skill.parent.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        err(f"{rel}: name must be lowercase-hyphenated")
    if not desc or len(desc) > 1024:
        err(f"{rel}: description missing or longer than 1024 chars ({len(desc)})")

# 2. Local links and reference mentions
main = ROOT / "skills" / "remaster"
for md in list(ROOT.glob("*.md")) + list((ROOT / ".github").glob("*.md")) + list((ROOT / "skills").rglob("*.md")):
    text = md.read_text()
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if re.match(r"[a-z]+:", target):
            continue
        if not (md.parent / target).exists():
            err(f"{md.relative_to(ROOT)}: broken link -> {target}")
    for ref in set(re.findall(r"references/([a-z0-9-]+\.md)", text)):
        if not (main / "references" / ref).exists():
            err(f"{md.relative_to(ROOT)}: unknown reference file references/{ref}")
    for src in re.findall(r'(?:src|srcset)="([^"]+)"', text):
        if not re.match(r"[a-z]+:", src) and not (md.parent / src).exists():
            err(f"{md.relative_to(ROOT)}: missing image {src}")

# 3. Manifests
try:
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    if plugin.get("name") != "remaster":
        err("plugin.json: name must be 'remaster'")
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin.get("name") not in names:
        err("marketplace.json: must list the plugin")
    top = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(), re.M)
    if not top or top.group(1) != plugin.get("version"):
        err("CHANGELOG.md top version must equal plugin.json version")
except (OSError, json.JSONDecodeError) as e:
    err(f"manifest error: {e}")

# 4. Assets are well-formed SVG
for svg in (ROOT / "assets").glob("*.svg"):
    try:
        xml.dom.minidom.parse(str(svg))
    except Exception as e:  # noqa: BLE001 - report any parser failure
        err(f"{svg.relative_to(ROOT)}: invalid SVG ({e})")

if errors:
    print("Validation failed:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"OK — {len(skills)} skills, links, manifests and assets valid.")
