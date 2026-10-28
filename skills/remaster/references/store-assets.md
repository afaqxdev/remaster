# Store assets — screenshots & feature graphic (`/remaster-store-assets`)

Store screenshots are an ad, not a gallery. A visitor decides in about three seconds from the first two frames. Design them as a **short story built from the approved UI Kit and real redesigned screens** — never features, results or reviews the app doesn't have.

Prerequisite: the approved Figma design (Gate 1 at minimum; ideally Phases 5–7 done).

## 1. Brief (ask in one message before designing)
- Stores and devices (Play phone/tablet, iPhone, iPad), number of screenshots (default 6), locales.
- Target audience in one line (who, context, what they want).
- Preferred style (offer the three below with the recommendation for this app's category) and tone.
- Brand constraints: logo placement, mandatory tagline/keywords, photos vs. graphics allowed.
- Promo video planned? (affects the feature graphic).
Don't ask what `app-dossier.md`, `design-direction.md` or the UI Kit already answers.

## 2. Pick one of three styles (render frames 1–2 in the recommended style + one alternative, user chooses)

### Style 1 · Device-Hero (UI-centric)
- **Layout:** one large portrait device or frameless screen fills most of the frame (often bleeding off the bottom); short headline in the clear top area. The UI carries the message.
- **Type:** the kit's display font for the headline, UI font for the subhead; headline over empty background, never over UI.
- **Colour & imagery:** brand background or soft gradient from kit tokens; no stock photos; accents only from the UI.
- **Extras:** at most one floating element (a zoomed UI fragment or a chip) — no fake ratings or badges.
- **Best for:** apps with a distinctive UI — creative, social, games, productivity with a strong look.
- **Pros / cons:** fastest, most honest, modern · can feel flat if the UI isn't striking.

### Style 2 · Lifestyle / Contextual
- **Layout:** the device in a scene — hand-held, on a desk, in the moment of use — tilted or partly out of frame; headline in the photo's calm area, on a brand-coloured scrim if needed for contrast. Keep the UI clearly readable (it should still be the largest single element).
- **Type & colour:** bold, high-contrast headline; brand gradient overlay to unify photo colours with the kit.
- **Imagery:** relatable people/environments for the target user. Use **only licensed or original** photos or renders (record source/license); AI-generated people must not imply real customers. No other brands' hardware renders without rights.
- **Best for:** fitness, wellness, travel, food, dating, family apps.
- **Pros / cons:** emotional, aspirational · needs photography/licensing, can hide UI detail, slower to make.

### Style 3 · Feature-Grid / Iconic
- **Layout:** no device; 2×2 or 3×2 rounded cards (kit radii/shadows), each with a custom icon or mini UI snippet and a 1–3 word label; headline above. Use for 1–2 frames inside a set, not the whole set.
- **Type & colour:** strong bold headline; flat card fills from kit tokens; icons from the kit's icon family (same stroke, radius).
- **Best for:** utility, finance, productivity, security, B2B apps with many benefits.
- **Pros / cons:** many benefits at a glance · cluttered or "salesy" if overused; less product feel.

| Style | Ideal for | Effort (6-frame set) |
|---|---|---|
| Device-Hero | distinctive UI, games, social, creative | fast |
| Lifestyle | wellness, fitness, travel, food, dating | slow (photos + licensing) |
| Feature-Grid | utility, finance, productivity, B2B | medium |
Mixing is fine: e.g. Device-Hero frames 1–4 + one Feature-Grid frame for "everything else" — but one palette, one type system, one motif across the set.

## 3. Storyboard (6 frames for phones; adapt)
1. **Value proposition / core job** — what the user gets, shown on the hero screen (never login or onboarding).
2. **Core action** — the main task mid-action.
3. **Differentiator** — what competitors lack (from `app-dossier.md`).
4. **Progress / reward** — results, stats, streaks.
5. **Personal / social / daily** — sharing, daily content, personalization.
6. **Trust & polish** — dark mode, offline, privacy, accessibility; or a Feature-Grid summary.

## 4. Copy
| Element | Length | Rule |
|---|---|---|
| Headline | 3–6 words (≤ 7 for Lifestyle) | benefit-first, verb-led, enhances the visual instead of describing it |
| Subhead (optional) | 8–12 words | one sentence |
| Grid labels | 1–3 words | nouns or short verb phrases |
| Closing line (optional, last frame) | 1–3 words | benefit CTA ("Start your streak") — avoid store-action CTAs like "Download now"/"Install" and "free" claims |
- Headline ≥ 6% of frame height; contrast ≥ 4.5:1; readable when the frame is ~200 px wide.
- Never: rankings, "#1"/"best", prices or discounts, award claims, star ratings or review quotes, other apps' names/marks.
- Per-locale text layers, ~30% room for longer languages, mirrored layout for RTL.

## 5. Specs (re-check Play Console / App Store Connect before upload)
| Store | Asset | Size | Rules |
|---|---|---|---|
| Google Play | Phone screenshots | 1080 × 1920 portrait (9:16) recommended; landscape 1920 × 1080 allowed | 2–8 per device type; each side 320–3840 px; longest side ≤ 2× shortest; JPEG or 24-bit PNG, **no alpha** |
| Google Play | Tablet (if supported) | 1920 × 1200 / 1200 × 1920 | same rules |
| Google Play | **Feature graphic** (required) | **1024 × 500** | JPEG / 24-bit PNG, no alpha |
| App Store | iPhone 6.9" (main set) | 1320 × 2868 (1290 × 2796 also accepted) | up to 10; flat PNG/JPEG, no transparency; smaller iPhones scale from it |
| App Store | iPad 13" (if the app runs on iPad) | 2064 × 2752 (2048 × 2732 also accepted) | required when iPad is supported |
- Keep text and key UI inside the centre ~80% of each frame.
- Portrait first; add landscape only when the content is wide (games, maps, video) — keep one orientation per set where possible.
- Build every size as its own frame; never stretch an export to another ratio.

## 6. Feature graphic (1024 × 500)
Brand-led, not a screenshot collage: app mark + 2–5-word tagline + one hero UI fragment or illustration from the kit. Text and logo inside the centre ~80%; keep the exact centre clear when a promo video is attached (play button). Readable at 50% size; same palette and motif as the icon and screenshots.

## 7. Workflow
Brief → pick style (2 frames × 2 styles) → full storyboard → self-review → user review → export all sizes and locales.
- Figma page **"Store assets"**: frames named `play/phone/01-value`, `appstore/iphone69/01-value`, `play/feature-graphic`; captions as kit text styles; backgrounds/motif as components.
- Self-review each frame: thumbnail test (~200 px wide), contrast, copy lengths, policy list, story order, consistency with icon and splash, safe area.

## 8. Export & hand-off
Export at exact pixel sizes, flattened (**no alpha**), PNG or JPEG, to `redesign/<app-slug>/store-assets/{play,appstore}/<locale>/`. Write `store-assets.md` (chosen style, frame order, captions per locale, asset sources/licenses, specs used, items to re-check in the console) and suggest A/B tests (Play store listing experiments, App Store product page optimization).
