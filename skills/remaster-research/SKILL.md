---
name: remaster-research
description: Remaster command — run only the research phases (Step 0 discovery + Phases 1–2) for an app redesign: store listing, reviews, competitor teardown, feature and screen inventory, do-not-copy list. Produces app-dossier.md and status.md. Use when the user wants to research or analyze an existing app before redesigning it, or runs /remaster-research.
---

# /remaster-research

Run **Step 0 and Phases 1–2 only** of the `remaster` workflow.

1. Read the `remaster` skill's `SKILL.md` (rules, Step 0, skills-per-phase table) and `references/research.md`.
2. Ask the Step 0 questions in one message (app/link, platform, APK/IPA with the supply guide, project, assets, deliverables).
3. Do the research exactly as `research.md` describes; label every claim `[verified]`, `[inferred]` or `[assumption]`.
4. Write `redesign/<app-slug>/app-dossier.md` and `status.md`.
5. Stop. Tell the user the next command is `/remaster-sample` (or `/remaster` to continue the whole flow).

Never open the original's screenshots again after writing the inventory.
