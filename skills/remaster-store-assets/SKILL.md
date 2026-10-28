---
name: remaster-store-assets
description: Remaster command — design Google Play and App Store screenshots and the Play feature graphic from the approved Figma design and UI Kit: 3 styles to choose from (Device-Hero, Lifestyle, Feature-Grid), a 6-frame story, length-checked captions, light/dark sets, exact store sizes, policy-safe copy, and flattened exports. Use when the user wants store screenshots, app store images, a feature graphic or store listing graphics, or runs /remaster-store-assets.
---

# /remaster-store-assets

Design the store listing graphics. Read the `remaster` skill's `references/store-assets.md` and follow it.

1. Read `redesign/<app-slug>/status.md`. Gate 1 must be approved and the Figma design must exist; if not, say what's missing and stop.
2. Ask the brief in one message (stores, devices, count, locales, audience, style + tone, brand constraints, photos vs. graphics, promo video) — skip anything the dossier, direction or UI Kit already answers.
3. Recommend a style for the app's category; build frames 1–2 in that style and one alternative on a Figma page "Store assets"; the user picks.
4. Build the full 6-frame story + feature graphic in the chosen style, light and dark if supported, from the UI Kit and real screens only. Self-review (thumbnail test, contrast, policy list).
5. Export flattened PNG/JPEG at exact sizes to `redesign/<app-slug>/store-assets/`, write `store-assets.md`, update `status.md`.
Never show features the app doesn't have, other brands' marks, rankings, prices or fake reviews.
