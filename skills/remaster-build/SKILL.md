---
name: remaster-build
description: Remaster command — implement the approved Figma design in Flutter (9a tokens and core widgets, 9b screens and routing, 9c states with injected mock data, 9d graphics, motion and real data). Only runs after Gate 2. Use when the user approves converting the final Figma design to Flutter code, or runs /remaster-build.
---

# /remaster-build

Run **Phase 9** of the `remaster` workflow.

1. Read `status.md` and `build-prompt.md`. If Gate 2 isn't recorded, ask: "The Figma design is complete and audited. Shall I convert it into Flutter code?" and wait for an explicit yes.
2. Read the `remaster` skill's `references/implementation.md` and `references/motion-research.md`; load `ponytail` and Figma's `figma-implement-motion`.
3. Work one sub-step at a time (9a → 9d), verifying each. UI depends only on injected interfaces; 9c → 9d changes DI bindings only.
4. Never simplify the design to write less code. Update `status.md`.
