# Premium visual quality bar (applies to every phase that produces visuals)

The target is a **premium app in today's market** — not a basic layout of simple cards, default buttons and standard widgets. Never trade visual quality for speed.

## Skills to use (check they're installed; use the closest alternative if not)
| Area | Skills |
|---|---|
| Mobile UI/UX patterns, palettes, type, UX rules | `ui-ux-pro-max`, `typeui-fundamentals`, `design-skills:interaction-design` |
| Visual polish, motion taste | `emil-design-eng`, `apple-design`, `animate` |
| Design system & elevation | `design-system`, `design-skills:design-elevation`, `design-skills:design-systems` |
| Graphics: icons, illustration, brand | `design` (icon design, SVG), `brand`, `banner-design` (store graphics) |
| Critique & accessibility | `design:design-critique`, `design:accessibility-review`, `break-ui` |
| Figma build | Figma MCP: `figma-use`, `figma-generate-design`, `figma-generate-library` |
| Flutter fidelity | flutter.dev / pub.dev docs; local `flutter` CLI (Phases 9–10 only) |

## Principles
- **Modern visual identity:** one design system — palette, typography, spacing, icons, shapes, hierarchy — used everywhere.
- **Premium UI:** clean layouts, balanced whitespace, beautiful type, subtle soft shadows, gradients only when they add meaning, refined components.
- **Modern components:** navigation, buttons, cards, inputs, bottom sheets, dialogs — each deliberately designed designed for this app (see `design.md` → "App-aware direction" and "Modern-UI vocabulary").
- **Consistency:** every screen speaks the same visual language; it must feel like one product.
- **UX first:** intuitive, accessible, responsive; usability beats decoration.
- **Avoid outdated design:** clutter, excessive gradients, unnecessary borders, inconsistent spacing, generic templates, repetitive cards without purpose.
- **Inspiration, not imitation:** study principles from polished products (Linear's restraint and type, Notion's calm hierarchy, Airbnb's imagery and cards, Things, Arc, Duolingo's character for games) — adapt the *principle* to this app's identity and audience, never their look.

## Graphics the app ships with (inventory in Phase 3, built in Phase 6)
Plan graphics as part of the design system, not as decoration added at the end.

1. **Graphic inventory (Phase 3):** list every graphic the app needs — app icon, splash mark, onboarding illustrations, empty / error / success states, achievements or badges, store screenshots. Each must explain something or carry the brand; drop anything decorative only.
2. **One graphic language:** derive illustrations from the brand motif (shapes, palette tokens, corner radii, stroke weight) so they look made for this app. Same light direction, same stroke, same palette in every graphic; light and dark variants.
3. **Icons:** one consistent set (e.g., a rounded 1.75–2px stroke family) tuned to the type; key product icons (the app's core actions and rewards) drawn custom in the same style. No emoji or mixed icon families.
4. **How to make them:** vector first — build in Figma from shapes/SVG (`use_figma`, `createNodeFromSvg`) or with the `design` skill's SVG icon generation. Raster hero art only if the style needs it: Figma `generate_image` (tell the user AI credits were used) or user-supplied assets. Never stock clip-art, and never the original app's graphics.
5. **In Figma:** a **Graphics** page with the icon set as components, each illustration as a component with light/dark variants, and export settings (SVG; PNG @1x/2x/3x only for raster).
6. **Animated graphics:** only when motion adds meaning (celebration, onboarding demo). Specify as Lottie or Rive with a size budget; static fallback for reduced motion.

## Phase 6 — App icon (a separate product-design deliverable, static)
- **Concept first:** one strong, simple idea that says what the app is (built from the brand motif), readable at 48px and smaller. No text, no fine detail, no generic symbol (stars, checkmarks, plain letters), no complicated compositions. Create **three distinct concepts**, compare them, recommend the strongest and confirm with the user.
- **Launcher and store icons are static.** Never promise an animated home-screen or store icon. Use motion in the splash, onboarding and in-app instead; platform-specific animated icon features are a separate, optional discussion.
- **Android (Google Play):** adaptive icon = foreground + background layers on a 108×108dp canvas, key art inside the 66dp safe zone (it gets masked to circle/squircle); add a **monochrome** layer for Android 13+ themed icons; Play Store listing icon 512×512 PNG (32-bit, ≤1 MB); legacy mipmaps 48/72/96/144/192px.
- **iOS (App Store):** single 1024×1024 PNG, no transparency, no pre-rounded corners (the system masks it); provide **dark** and **tinted** variants for iOS 18+.
- **Icon review (all must pass):** silhouette readable as a black shape; contrast between foreground and background; recognizable at 48 and 29px; survives every platform mask (circle, squircle, rounded square, iOS); export quality (crisp edges, correct sizes, no transparency on iOS, safe zone on Android).
- **Checks before finalizing:** view at 1024, 180, 48 and 29px; on light, dark and busy wallpapers; in grayscale; inside every mask shape; next to the category's top store icons (as a store-grid check — not to borrow their design). It must be distinctive and production-ready.
- **In Figma:** an **App icon** page with the concept sketches, the final layered icon, every mask preview, light/dark/tinted/monochrome variants, and export slices for every size above.
- **Flutter:** generate platform icons with `flutter_launcher_icons` from the exported layers (adaptive + monochrome for Android, 1024 master for iOS).

## Splash, onboarding and micro-interaction motion
- **Splash:** a native splash shows the static mark instantly (`flutter_native_splash`; on Android 12+ the system SplashScreen uses the icon on a solid background — keep the mark inside its safe circle), then a short Flutter reveal continues it seamlessly: logo build/reveal, elegant brand motion, ≤ ~1s, ends as soon as the app is ready. Fast, lightweight, never hiding slow startup.
- **Onboarding:** animated illustrations that *demonstrate* each key feature (e.g., the actual game mechanic playing out), coordinated with text reveals and page progress; interactive where it helps (tap to try). Built with Flutter animations, or Rive (interactive/state-driven) / Lottie (linear) when an illustrator-grade animation is needed — with a size budget and a static fallback for reduced motion.
- **Micro-interactions:** buttons, toggles, transitions, loading, navigation, success/error, rewards — subtle, fast, each communicating a result (timings in `motion-flutter.md`).
- **Every animation needs a purpose** (orientation, feedback, explanation, delight at rare moments). Decorative-only motion is removed.

## Asset quality
Original or properly licensed assets only; record the source/license of anything not made in-house. No placeholders in final screens, no generic AI visuals that don't fit the product, nothing from the original app.

## Flutter fidelity (Phases 9–10)
- Keep spacing, proportions, type, colors, graphics and motion exactly as designed; compare emulator screenshots with the Figma frames.
- Vector graphics via `flutter_svg`, colored from theme tokens (not baked-in hex) so light/dark and palettes switch; raster via resolution-aware assets (1x/2x/3x) and `precacheImage` for first-screen art.
- Lottie (`lottie`) or Rive (`rive`) only for the animated graphics specified; respect reduced motion.
- Responsive: layouts adapt to small phones, large phones and tablets (breakpoints from `design.md`).

## Professional review (before finalizing ANY screen)
Answer honestly; any "no" means refine before moving on:
1. Does this screen look modern and visually appealing?
2. Does it feel like a real, production-ready app rather than a prototype?
3. Are the graphics, icons, typography, colors and spacing cohesive?
4. Is it distinctive rather than a generic AI-generated template?
5. Does it work across small phones, large phones and tablets?

Before finalizing the whole design, also confirm: the app icon clearly represents the app, stays distinctive at small sizes and is production-ready; the icon, splash, onboarding illustrations and in-app icons share one visual style; every graphic and animation has a clear purpose.

Record the answers for each screen in `screen-specifications.md` (one line per question) so the review is visible, not assumed.
