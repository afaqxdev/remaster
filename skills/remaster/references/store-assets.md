# Store assets — screenshots & feature graphic (`/remaster-store-assets`)

Store screenshots are an ad, not a gallery. A visitor decides in about three seconds from the first two frames. Design them as a **short story built from the approved UI Kit**, not raw captures with text on top.

Prerequisite: the approved Figma design (Gate 1 at minimum; ideally Phase 5–7 done) so every frame shows the real redesigned UI. Never show screens, features or results the app doesn't have.

## 1. Specs (verified Oct 2026 from multiple guides — re-check Play Console / App Store Connect before upload)
| Store | Asset | Size | Rules |
|---|---|---|---|
| Google Play | Phone screenshots | 1080 × 1920 (9:16) recommended; 2–8 per device type | JPEG or 24-bit PNG, **no alpha**; longest side ≤ 2× shortest |
| Google Play | 7"/10" tablet (if supported) | 1920 × 1200 / 1200 × 1920 | same |
| Google Play | **Feature graphic** (required) | **1024 × 500** | JPEG or 24-bit PNG, no alpha; also the cover of the promo video |
| App Store | iPhone 6.9" (main set) | 1320 × 2868 (or 1290 × 2796) | PNG/JPEG flat, no transparency; up to 10; smaller sizes scale from it |
| App Store | iPad 13" (if the app runs on iPad) | 2064 × 2752 (or 2048 × 2732) | required when iPad is supported |
Build each size as its own Figma frame — never stretch one export to another ratio.

## 2. Pick a visual concept (show the user 3, they choose)
Render frame 1 + 2 in each concept, light theme, then ask which to develop:
- **A · Hero caption** — big 2–5-word headline on top, one device (or frameless UI) below, bleeding off the bottom edge; brand background from the kit. Clean, safest for conversion.
- **B · Panorama** — one continuous background/illustration flowing across all frames so the row reads as one image while scrolling; devices tilted ±4–8°; motif shapes from the brand cross frame edges.
- **C · Spotlight** — a zoomed crop of one UI element (the key interaction) floating large, with a smaller full screen behind and 1–2 callout labels; best for showing a unique feature.
All three use the kit's colours, fonts, radii, shadows and motif — screenshots must look like the same brand as the app icon and splash.

## 3. Storyboard (6 frames for phones; adapt to the app)
1. **Value proposition** — the single strongest reason to install + the hero screen. No feature lists.
2. **Core action** — the main thing users do, mid-action (e.g., a reveal or a completed task).
3. **Differentiator** — what competitors lack (from `app-dossier.md` → missing features / pain points fixed).
4. **Progress / reward** — stats, streaks, results, the "feel good" moment.
5. **Personal / social / daily** — daily content, sharing, friends, personalization.
6. **Trust & polish** — dark mode, accessibility, offline, privacy — or a strong closing line.
Order frames 1–3 for people who never swipe further.

## 4. Caption rules
- Headline **2–5 words**, benefit-first, verb-led ("Guess smarter every day"), set in the kit's display font, ≥ 6% of frame height; optional one-line subhead.
- One idea per frame; ≤ 2 lines; never cover essential UI.
- Contrast ≥ 4.5:1 against its background; readable at thumbnail size (check at 25% zoom).
- No rankings, "#1", "best", prices, discounts, "free"/"download now" calls to action, award claims, or other apps' names/marks — store policies reject or penalise these.
- Write captions in a separate text layer per locale; keep room for ~30% longer languages; mirror layout for RTL.

## 5. Device & UI presentation
- Use the **real Figma screens** at full fidelity with realistic, honest content (no lorem ipsum, no fake reviews or numbers presented as real users).
- Device frame optional: a simple, current, generic frame or frameless rounded screen with the kit's shadow — never another manufacturer's trademarked hardware render you don't have rights to.
- Hide/clean the status bar (full battery, neutral time like 9:41).
- Provide **light and dark** sets when the app supports both; choose the stronger one as the default listing.

## 6. Feature graphic (1024 × 500)
- Brand-led, not a screenshot collage: app mark + a 2–5-word tagline + one hero UI fragment or illustration from the kit.
- Keep text and the logo inside the central ~80% (cropping and the video play button can cover edges/centre — keep the exact centre clear of text if a promo video is attached).
- Bold, simple, readable at 50% size; same palette and motif as the icon and screenshots.

## 7. Build in Figma
- New page **"Store assets"**: one frame per size and locale, named `play/phone/01-value` … `appstore/iphone69/01-value`, `play/feature-graphic`.
- Captions as text styles from the kit; backgrounds and motif as components so changes propagate to every frame.
- Self-review with screenshots: thumbnail test (25%), contrast, policy list above, story order, consistency with icon/splash.

## 8. Export & hand-off
- Export each frame at exact pixel size, flattened (**no alpha**) as PNG or JPEG; put them in `redesign/<app-slug>/store-assets/{play,appstore}/<locale>/`.
- Write `store-assets.md`: frame order, caption text per locale, which concept was chosen, specs used, and anything the user must still check in the console.
- Suggest A/B testing variants (Play Store listing experiments, App Store product page optimization) instead of guessing.
