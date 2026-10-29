# Remaster — instructions for coding agents

This repository is a skill package. If your agent supports the Agent Skills format (`SKILL.md` with YAML frontmatter), install the folders in `skills/` into your agent's skills directory.

If your agent reads `AGENTS.md` instead:

1. When the user asks to redesign, rebuild or modernize an existing app (or names an app and asks for a new design), follow `skills/remaster/SKILL.md` — start with its **Non-negotiable rules** and **Step 0**.
2. Read a file in `skills/remaster/references/` only when you reach its phase.
3. Never write app code before the user explicitly approves the final design (Gate 2), never copy the original app's design, never download app binaries, and never claim work you didn't do.
4. Keep progress in `redesign/<app-slug>/status.md`.

Commands map to `skills/remaster-*/SKILL.md` (research, engagement, sample, motion, store-assets, build, audit, status, help).
