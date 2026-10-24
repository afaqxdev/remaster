# Contributing to Remaster

Thanks for helping make app redesigns better and more original.

## Good contributions
- **Rules & checklists** that make output more modern, accessible or honest (`skills/remaster/references/design.md`, `visual-quality.md`).
- **Motion research** updates when Figma Motion or Flutter animation APIs change (`motion-research.md`).
- **Platform coverage** — iOS/Apple HIG details, tablets, foldables.
- **Fallbacks** for when a recommended skill or tool isn't installed.
- **Test prompts** in `evals/prompts.md` that catch regressions.

## Ground rules
- Keep `SKILL.md` short: workflow, gates and routing only. Put detail in a reference file loaded in its phase.
- Never add guidance that copies an existing app's design, downloads app binaries, or bypasses DRM.
- Don't duplicate another skill — route to it and give a fallback.
- Cite sources for factual claims about Figma, Flutter or store APIs.

## Before opening a PR
```bash
python3 scripts/validate.py
```
Describe what changed, why, and which eval prompts you ran.
