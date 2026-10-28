# Store assets — screenshots & feature graphic (`/remaster-store-assets`)

Store screenshots are an ad, not a gallery. A visitor decides in about three seconds from the first two frames. Design them as a **short story built from the approved UI Kit and real redesigned screens** — never features, results or reviews the app doesn't have.

Prerequisite: the approved Figma design (Gate 1 at minimum; ideally Phases 5–7 done).

## 1. Brief (ask in one message before designing)
- Stores and devices (Play phone/tablet, iPhone, iPad), locales, and any limit on how many screenshots they want.
- Target audience in one line (who, context, what they want).
- Any style preference or reference listings they like (as inspiration, never to copy), and tone.
- Brand constraints: logo placement, mandatory tagline/keywords, photos vs. graphics allowed.
- Promo video planned? (affects the feature graphic).
Don't ask what `app-dossier.md`, `design-direction.md` or the UI Kit already answers.

## 2. Narrative — derived from this app
- **Count:** decide from platform limits (Play 2–8 per device type, App Store up to 10), how many genuinely strong messages the app has, its complexity and the audience. Fewer strong frames beat padded ones.
- **Opening frame:** the app's primary value, shown on the screen that proves it (never login or a generic onboarding screen) — most visitors never swipe past the first two or three.
- **Sequence:** order the remaining frames by the strongest product-specific messages and the real user journey (from `app-dossier.md`: core jobs, differentiators, fixed pain points). Don't force fixed categories (value, core action, differentiator, reward, social, trust) into every set.
- Research competitor listings and category conventions when it would change the narrative — to stand apart, never to copy.

## 3. Visual direction — derived, not picked from a menu
Explore what fits this app's product, audience and brand. Device-focused, lifestyle/contextual, editorial typography, photographic, illustrative, feature-grid, panoramic, data-led and other approaches are possibilities, not an exhaustive list; mixing within a set is fine if the palette, type system and motif stay consistent.
When a style decision is needed, present **one to three genuinely suitable directions** (frames 1–2 in each), each with one line on why it fits this app and its trade-offs (e.g., lifestyle needs licensed photography; feature grids can feel salesy). Never offer the same set of styles by default.
Constraints that always apply:
- Show the real redesigned UI and honest content; keep the UI readable even in lifestyle compositions.
- Photos/renders only if licensed or original (record source); AI-generated people never presented as real customers; no other brands' hardware renders without rights.
- All colours, type, radii, icons and motif come from the UI Kit, so screenshots match the icon and splash.

## 4. Copy
| Element | Length | Rule |
|---|---|---|
| Headline | short — typically 3–7 words | benefit-first, enhances the visual instead of describing it |
| Subhead (optional) | typically one sentence of ~8–12 words | supports, never repeats, the headline |
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
Brief → narrative → 1–3 directions (frames 1–2) → user choice → full set → self-review → user review → export all sizes and locales.
- Figma page **"Store assets"**: frames named `play/phone/01-value`, `appstore/iphone69/01-value`, `play/feature-graphic`; captions as kit text styles; backgrounds/motif as components.
- Self-review each frame: thumbnail test (~200 px wide), contrast, copy lengths, policy list, story order, consistency with icon and splash, safe area.

## 8. Export & hand-off
Export at exact pixel sizes, flattened (**no alpha**), PNG or JPEG, to `redesign/<app-slug>/store-assets/{play,appstore}/<locale>/`. Write `store-assets.md` (chosen style, frame order, captions per locale, asset sources/licenses, specs used, items to re-check in the console) and suggest A/B tests (Play store listing experiments, App Store product page optimization).
