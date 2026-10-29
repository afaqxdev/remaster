---
name: remaster-audit
description: Remaster command — run the scripted visual and technical audit of a Flutter redesign: flutter analyze, unit/widget/golden/integration tests, emulator screenshots compared with Figma exports, performance, accessibility and reduced motion. Use when the user wants to verify or QA the built app, or runs /remaster-audit.
---

# /remaster-audit

Run **Phase 10** of the `remaster` workflow.

0. Run the **Update check** in the `remaster` skill's `SKILL.md` (once per session).
1. Read the `remaster` skill's `references/implementation.md` → "Phase 10".
2. Run every step (static analysis, tests, goldens, emulator screenshots vs Figma via `get_screenshot`, diff, performance, accessibility, reduced motion).
3. Fix what fails and repeat until the acceptance criteria in `build-prompt.md` pass.
4. Report honestly: passed, fixed, not verified.
