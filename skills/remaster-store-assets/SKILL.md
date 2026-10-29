---
name: remaster-store-assets
description: Remaster command — design Google Play and App Store screenshots and the Play feature graphic from the approved Figma design and UI Kit: a narrative, screenshot count and 1–3 visual directions derived from the app, length-checked captions, light/dark sets, exact store sizes, policy-safe copy, and flattened exports. Use when the user wants store screenshots, app store images, a feature graphic or store listing graphics, or runs /remaster-store-assets.
---

# /remaster-store-assets

Design the store listing graphics. Read the `remaster` skill's `references/store-assets.md` and follow it.

0. Run the **Update check** in the `remaster` skill's `SKILL.md` (once per session).
1. Read `redesign/<app-slug>/status.md`. Gate 1 must be approved and the Figma design must exist; if not, say what's missing and stop.
2. Ask the brief in one message (stores, devices, count, locales, audience, style + tone, brand constraints, photos vs. graphics, promo video) — skip anything the dossier, direction or UI Kit already answers.
3. Derive the narrative and count; present 1–3 suitable directions (frames 1–2 each, with why they fit) on a Figma page "Store assets"; the user picks.
4. Build the full set + feature graphic in the chosen direction, light and dark if supported, from the UI Kit and real screens only. Self-review (thumbnail test, contrast, policy list).
5. Export flattened PNG/JPEG at exact sizes to `redesign/<app-slug>/store-assets/`, write `store-assets.md`, update `status.md`.
Never show features the app doesn't have, other brands' marks, rankings, prices or fake reviews.
