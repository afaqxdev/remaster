# Phases 3–5: Direction, sample, full design

## Phase 3 — Visual direction (`design-direction.md`)

Load `ui-ux-pro-max` for style, palette, font pairing and UX rules matched to the app's category and audience; then `emil-design-eng` to sharpen polish and interaction decisions. Reconcile where they disagree and say why.

Decide and justify, against the dossier (audience, pain points, competitors):
- Primary/secondary palette, semantic colors, light/dark plan
- Typography (brand font + fallback; must support the app's languages/scripts) and hierarchy
- Density and whitespace, grid
- Surface treatment: cards vs flat sections vs lists, borders, depth, shadows, gradients
- Imagery: illustration / photography / iconography style (one icon set)
- Primary navigation pattern (bottom bar, rail, tabs, single-stack — whatever fits)
- Motion language in one sentence (e.g. "quick, springy, spatial — motion explains where things came from")
- **Graphic inventory and graphic language** (icons, illustrations, empty/success states, app icon) — see `visual-quality.md`

Optionally present 2 contrasting directions in one line each and let the user pick before building the sample.

### Ideas, not copies (strict)
- Work only from the **text** feature/screen inventory in `app-dossier.md`. Do **not** open the original's screenshots, binary resources or store graphics in Phases 3–10.
- Turn every finding into a **need**, then design the answer from scratch: "home has Play / Challenge / Pass buttons" → need: "start a game fast, invite a friend" → new composition.
- Not allowed from the original: layouts, screen structure, content design and copy, colors, fonts, icons, illustrations, component shapes, spacing, design tokens, motion.
- Check against the dossier's **do-not-copy list** (text only): if any color, font or pattern you chose is on it, replace it.
- Only **genre-wide conventions** users rely on (e.g., green = right spot / yellow = wrong spot in word games, standard gestures) may carry over — in your own shades, listed by name in `design-direction.md` as conventions, never as copied styling.

### Color composition check (must pass before the sample)
- **Brand hue:** one confident, ownable primary chosen for the audience and mood — not grey-on-beige by default, not the original app's color, not the category cliché unless it's a convention users rely on (e.g. Wordle green/yellow for tile feedback).
- **Structure:** ~60% neutrals (background/surfaces) · ~30% brand/support · ~10% accent for the few moments that matter. Neutrals are tinted toward the brand hue, never dead grey.
- **Harmony:** accent and semantic colors (success/warning/error/info, or game states) are picked as a set — analogous or complementary to the brand hue, similar saturation and lightness so nothing looks muddy, neon or out of family.
- **Contrast:** text ≥ 4.5:1 (≥ 3:1 for large text and UI shapes), measured, in both themes; never rely on color alone (add icons/labels; offer a color-blind palette when color carries meaning).
- **Dark theme** is designed, not inverted: lifted surfaces, slightly desaturated brand, same hierarchy.
- **Show it:** build a **Palette** board on the Figma Foundations page — swatches with names, hex, light/dark, contrast ratios, and a 60-30-10 strip — and get it approved with the sample.

### App-aware direction — no default style
Every app gets its own design system. Derive each decision from this app's problem, audience, features, differentiators, desired emotion, category conventions, existing brand assets and competitor research — never from a previous project or a house template.
- **Answer first (in `design-direction.md`):** what problem it solves · who it's for · core features & differentiators · the emotions it should carry · which category conventions help users · which existing brand elements are requirements vs. mere current implementation · what competitors do (to stand apart, not copy).
- **Then decide:** palette & semantic tokens · typography & hierarchy · layout & composition · imagery (illustration, photography, 3D, data viz, editorial type…) · iconography · spacing, shapes, surfaces · motion principles · onboarding narrative · accessibility & platform behaviour. Write one line of *why* for each.
- **Two directions that genuinely differ** (not two palettes on one layout) are presented when the right answer is unclear.
- **Existing designs:** keep required functionality, established brand assets and explicit constraints; improve weak decisions; don't reproduce an old design just because it exists, and don't discard established branding without a reason.
- Research (competitors, category patterns, current trends) when it changes a decision; skip it when it wouldn't.

### Modern-UI vocabulary (options, not defaults)
Use what serves *this* app; none of these is mandatory and none should become a habit across projects:
floating or standard navigation bars, rails, tabs or single-stack navigation · tonal surfaces vs. outlined vs. flat editorial sections · bento grids vs. lists vs. full-bleed media · big display type vs. quiet, content-first type · generous vs. tight radii · bold brand moments vs. restrained colour · photography, illustration, 3D or data visualisation as the main imagery · data shown as charts, rings, chips or tables.

### Quality red flags (any one = rework that element)
Defaults left unstyled (stock Material/Cupertino look with only a colour swap) · flat hierarchy where everything has equal weight · inconsistent spacing or radii · outlines and shadows piled on every element · colour with no clear brand role, or contrast failures · decorative graphics with no purpose · clutter on small screens · dated effects (glossy bevels, heavy drop shadows, clip-art) · a layout that could belong to any app in any category.

### Onboarding — every screen intentional
Decide the story first (what the user must understand, feel and do by the end), then the purpose of each screen, then a composition chosen for that message: device-focused, immersive illustration, contextual photography, diagram, interactive preview, editorial typography, or something new. Never stamp one layout and swap text/art. Vary compositions when it helps the story; repeat one when repetition genuinely serves the flow. Skip onboarding entirely if the app is self-explanatory.

### Consistency ≠ sameness
Keep typography, colour tokens, component behaviour, spacing logic, iconography and accessibility consistent. Let composition, artwork, hierarchy, background treatment and focal points change when the content and journey justify it.

### Adaptive design review (before presenting)
- Does the direction fit this product and audience — would it look wrong on a different app?
- Does each screen have one clear purpose?
- Are repeated compositions there on purpose, and do variations feel intentional rather than random?
- Distinctive without hurting usability, platform conventions or feasibility in Flutter?
If it feels generic or like a template unrelated to the app, go back to the direction.

### Self-review loop (mandatory before showing anything)
After building each component and each screen, answer the 5-question professional review in `visual-quality.md`, then: screenshot it, check it against the app-aware direction, the quality red flags, the adaptive design review, the color composition check and the dossier's do-not-copy list (text only — never the original's screenshots), and fix what fails. Only then present it.

### Component freshness check (every component)
- Built for this product's personality, not a stock widget with a color swap.
- Current design language: clear hierarchy through type and space, crisp radii matched to the brand (not max-rounded everywhere), soft tonal depth instead of heavy shadows, purposeful use of fills vs outlines.
- Has every state designed (default, pressed, focused, selected, disabled, loading, error, success) and its micro-interaction noted.
- Looks intentional next to the other components — one family, not a mix of styles.
- Nothing that dates it: glossy/3D bevels, clip-art, default Material ripple look, gradients for decoration only, outlined-everything.

### Avoid the generic look
Do not default to: dashboard templates; maximum radius on everything; grids of identical cards; flat hierarchy; gradients or glassmorphism without reason; stock-looking bottom nav; floating decorative blobs; generic illustrations; heavy shadows/borders; every screen built from the same three components. Every visual choice must serve usability, clarity, brand or quality. Use platform conventions where they help usability, styled for this product.

## Phase 4 — Figma prototype (4–5 screens only)

**First build and validate the UI Kit (`ui-kit.md`)** — kit board with every component and state in light and dark — then compose the screens only from it.

### Pick screens from the dossier
Typical: splash, onboarding (or auth), **home with primary navigation**, the core feature, one secondary (detail / profile / library / settings). Replace any that don't apply; don't pad to five.

### The sample must establish
Visual identity, palette (light **and** dark), typography, spacing/layout approach, representative buttons/cards/fields/nav, interaction states, motion direction, responsiveness on the selected platforms. Content must be realistic and grounded in the dossier — no lorem ipsum. The home screen sets the quality bar for the whole app: spend the most effort there. The navigation must feel integrated, with clear active state and restrained transitions.

### Design tooling (explicit)
- **Primary:** Figma MCP — `use_figma` (Plugin API: variables, text styles, components, frames) and `get_screenshot` for every self-review. Build in the real file; never describe frames you didn't create.
- **Machine-readable output:** at the end of Phase 5, export the variables and text styles to `redesign/<app-slug>/design-tokens.json` (W3C design-tokens format: color per mode, typography, spacing, radius, motion). Phase 9a builds the Flutter theme from this file.
- **Fallback (no Figma MCP):** `figma-spec.md` + `design-tokens.json` + one SVG wireframe per screen in `redesign/<app-slug>/wireframes/`, clearly labeled as not a Figma file.

### Format: Figma frames — never app code
The sample is a **design** in Figma. Do **not** write Flutter or any app code before Gate 2 (Phases 1–8). Review the screens critically (self-review loop) and refine weak layouts before showing them.

Using the Figma MCP (load its `figma-use` skill / `get_figma_skill` first, then `create_new_file` → `create_session` → `use_figma`):
- Pages **"App icon"** and **"Graphics"** are built in Phase 6 (key graphic pieces may already appear in the prototype) — see `visual-quality.md`.
- Page **"Foundations"**: color variables (light + dark modes), text styles, spacing/radius variables, and the components this app's sample needs (from the UI Kit).
- Page **"Sample"**: one phone frame per screen at the target platform's size (Android 412×917, iOS 393×852), built from those components with Auto Layout and realistic content. **Deliver every sample screen in both light and dark mode** (same frames, Dark variable mode) so the user approves both themes at Gate 1.
- Motion direction as short annotation notes beside the frames (and a simple prototype link between frames if practical).
- Check every frame with `get_screenshot` and fix overlaps/clipping before showing the user.

If Figma isn't authorized, tell the user it needs authorizing via `/mcp` and stop to ask; don't substitute code.

Do not claim a prototype or Figma file exists unless it actually does.

### `sample-design.md`
For each screen: why it was chosen, layout, components used, content, states shown, motion. Plus the token draft and screenshot paths.

### Gate 1
Ask for approval on: visual style, colors, typography, layout, navigation, graphics, animation direction. Allow revisions. **Stop here until explicitly approved.**

## Phase 5 — Complete Figma design (only after Gate 1)

Design **every** required screen, component and state with realistic content — including loading, empty, error, success, permission and offline scenarios where relevant — plus responsive layouts (small phone, large phone, tablet when required) and dark mode where appropriate. Expand the approved prototype. Each screen is designed for its own purpose and journey within the shared system — not a copy of the sample's layout.

### `ux-flows.md`
Information architecture; navigation hierarchy (primary, secondary, nested); route table (name, path, params, transition type); user journeys; auth & onboarding; main task flows; forms & validation; permissions & system dialogs; payments/subscriptions; notifications & deep links; recovery and error flows. Specify back behavior, modal dismissal and state preservation per route.

### `design-system.md`
**Tokens** — all screens use these, no ad-hoc values:
- Color roles: primary, secondary, accent, background, surface levels, text primary/secondary, border/divider, success/warning/error/info, disabled, selected, overlay/scrim — light and dark where appropriate. Check contrast (WCAG AA: 4.5:1 body, 3:1 large text and UI).
- Typography: named styles (display, headline, title, body, label, button, caption…) with family, size, weight, line height, letter spacing. Must scale with system text size.
- Spacing & layout: spacing scale (e.g. 4-based), screen padding, gaps, grid, safe areas, breakpoints (compact < 600, medium 600–840, expanded > 840).
- Shape & elevation: radii, borders, shadows, surface hierarchy.
- Motion tokens: from `motion-system.md`.

**Components** — only those the product needs. For each: purpose, anatomy, sizes, variants, tokens used, interactions, accessibility, and states: default, pressed, focused, selected, disabled, loading, error, success (hover only for tablet/desktop/web).

### `screen-specifications.md`
For **every** screen in the dossier: purpose, user intent, entry/exit, layout and hierarchy, components, real copy, primary/secondary actions, interactions, validation, loading/empty/error/success/disabled states, responsive behavior, accessibility (semantic labels, focus order, 48dp touch targets), motion. Don't stop after the attractive screens.

### Figma
If the Figma MCP is authorized: load `/figma-use`, create the file and pages — Cover & direction; Foundations (variables for color/spacing/radius, text styles); Typography, colors, icons, spacing; Components & variants (Auto Layout); Navigation & UX flows; Wireframes; Motion — key moments (Smart Animate keyframe prototypes, see `motion-flutter.md`); Final screens (Android and iOS frames when both; light and dark; responsive frames for small phone / tablet where required); States (loading, empty, error, success, permission, offline); Prototype; Motion specs; Handoff notes. Verify the file exists before sharing its link.
If not authorized: tell the user it needs authorizing via `/mcp`, and write `figma-spec.md` with the same page structure — clearly labeled as a spec, no invented URL.

### Responsive & accessible
Phone sizes and aspect ratios, safe areas, text scaling to 200%, keyboard behavior in forms, Android vs iOS differences (back gesture, system UI, pickers, haptics), tablets if relevant, orientation, contrast, screen-reader labels, reduced motion, localization and RTL where relevant. No fixed layouts that break.
