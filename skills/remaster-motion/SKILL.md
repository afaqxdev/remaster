---
name: remaster-motion
description: Remaster command — design the key-moment animations (success, level/task complete, errors, splash, onboarding) as Figma Motion timelines with springs that map 1:1 to Flutter, plus motion-system.md. Use when the user wants animations or motion designed in Figma, or runs /remaster-motion.
---

# /remaster-motion

Run **Phase 7** of the `remaster` workflow.

0. Run the **Update check** in the `remaster` skill's `SKILL.md` (once per session).
1. Read `status.md`; Gate 1 must be approved.
2. Read the `remaster` skill's `references/motion-research.md` and `references/motion-flutter.md`; load Figma's `figma-use` + `figma-use-motion` skills.
3. Build one Figma Motion timeline per key moment (fallback: Smart Animate keyframes), modern vocabulary, `CUSTOM_SPRING` bounce values, reduced-motion notes.
4. Verify with `get_motion_context`; write `motion-system.md` with the Flutter mapping per beat. Update `status.md`.
