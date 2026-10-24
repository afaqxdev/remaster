# Phase 7: Motion system (`motion-system.md`)

Motion must explain navigation, give feedback, preserve continuity and express the brand. No motion just to look animated. Load `emil-design-eng` (and `animate` for decision order) before writing this. Note: store and launcher icons are static — motion lives in the splash, onboarding and in-app experience.

## Key-moment animations in Figma (required)
Read `motion-research.md` first. Every moment that rewards or informs the user — the core success action (e.g., a correct guess), task/level complete, errors/invalid input, splash, onboarding — gets a **designed, playable animation in Figma**, not just a note.
- **Primary: Figma Motion timeline** (load the Figma `figma-use-motion` skill). One top-level frame per moment whose *resting state is the final state*; keyframe tracks on its children (transform, opacity, size, colour, blur/glow, path trim), `CUSTOM_SPRING` easing with explicit bounce, `setTimelineDuration`. Hide mid-animation-only layers at rest (opacity 0).
- **Fallback (Motion not enabled):** Smart Animate keyframe frames — one frame per keyframe, identical layer names, `AFTER_TIMEOUT` reactions with spring easing, flow starting point.
- Use the **modern motion vocabulary** in `motion-research.md` (springs, staggered waves, card flips, depth, circular reveal, shared-element flight, light sweep, rolling counters, rings, confetti, island morph, haptics).
- Write a timing note under each moment (offset, duration, easing/bounce, haptic) and the reduced-motion alternative.
- **Verify** with `get_motion_context` (keyframes + spring curves) and, when ffmpeg is available, `export_video` frame samples; the moment must finish fast (≤ ~1.5 s before the user can act).
These timelines are the source of truth for Phase 9d (`get_motion_context` → Flutter via the mapping table) and the Phase 10 visual check.

## Tokens (adapt values to the direction)

| Token | Duration | Curve (Flutter) | Use |
|---|---|---|---|
| `instant` | 100ms | `Curves.easeOut` | press feedback, toggles |
| `quick` | 200ms | `Curves.easeOutCubic` | small state changes, tab icon/label |
| `standard` | 300ms | `Easing.emphasizedDecelerate` | route transitions, sheets |
| `emphasized` | 450ms | `Easing.emphasizedDecelerate` / spring | hero, container transform, splash |

Exits ~20–30% shorter than entrances. Nothing a user waits on regularly exceeds ~400ms. Define all of these once in `theme/tokens.dart` (`AppMotion`).

## Splash
Native splash (`flutter_native_splash` or platform launch screen) shows the brand instantly; the Flutter splash continues it seamlessly: logo fade + subtle scale (0.92→1), staggered wordmark, optional slow background movement, then transition into onboarding/home. Total ≲ 1s after first frame, and it ends as soon as init is done — never used to hide slow startup.

## Onboarding
Use animated illustrations that demonstrate the features (see `visual-quality.md` → splash/onboarding motion; Rive or Lottie only when Flutter animations can't reach the quality).
`PageView` driven: staggered text/illustration reveals per page (`Interval`s on one controller), light parallax tied to `PageController.page`, animated progress indicator, responsive next/back/skip/done. Motion must never block reading or tapping.

## Route transitions — choose by relationship
| Relationship | Transition | Flutter |
|---|---|---|
| Unrelated content, tab switches | Fade-through | `animations`: `FadeThroughTransition` / `PageTransitionSwitcher` |
| Hierarchy or sequential flow | Shared axis (X for steps, Y for depth, Z for parent/child) | `SharedAxisTransition` |
| Element continues to next screen | Hero / shared element | `Hero` |
| Card/list item expands into detail | Container transform | `OpenContainer` |
| Temporary tasks | Modal / bottom sheet | `showModalBottomSheet`, `DraggableScrollableSheet`, Cupertino sheet on iOS |

Configure via `PageTransitionsTheme` / route `pageBuilder` centrally; on iOS keep the swipe-back gesture working (Cupertino-style route or a custom one that supports it). Don't stack your own transition on top of one the router already plays.

## Navigation
Active/inactive items: icon swap or fill + label/indicator change in `quick`. Tab content: fade-through. Preserve each tab's state and scroll (`StatefulShellRoute.indexedStack` in go_router or `IndexedStack`). Re-tapping the active tab scrolls to top / pops to root. Badges animate count changes subtly. Never animate the whole bar.

## Micro-interactions
Button press (scale 0.97 + `instant`), card selection, toggles, form validation (gentle shake only for errors, inline message fade-in), loading → success morph, favorite/bookmark (small pop + haptic), counter tweens, snackbars, pull-to-refresh. Each must communicate a result. Pair key ones with `HapticFeedback` (selection/light impact).

## Implementation rules
- Prefer implicit animations (`AnimatedContainer`, `AnimatedOpacity`, `AnimatedSwitcher`, `TweenAnimationBuilder`) for simple effects; `AnimationController` + `AnimatedBuilder` for choreography; `Hero`, `animations` package for transitions. Add a dependency only when it clearly beats native code.
- Dispose controllers; use `SingleTickerProviderStateMixin`/`TickerProviderStateMixin`; stop repeating animations when off-screen.
- Keep rebuilds small: pass `child` to `AnimatedBuilder`, animate transform/opacity, wrap busy animated regions in `RepaintBoundary`; avoid animating layout or blur on large areas.
- Target 60/120 Hz smoothness; profile with `flutter run --profile` and DevTools when in doubt.
- **Safe motion fallback (required, every animation):** respect the device's accessibility setting. Read `MediaQuery.disableAnimationsOf(context)` (same value as `MediaQuery.of(context).disableAnimations`, but rebuilds only when it changes). When it is `true`: skip movement, scale, rotation, parallax, particles, blur and springs; jump to the final state or use a ≤ 150–250 ms crossfade; keep state changes and haptics that convey meaning. Centralise it once (e.g., `AppMotion.reduced(context)` returning zero/short durations) so every widget and timeline obeys it, and cover it with a widget test that sets `disableAnimations: true`.

## `motion-system.md` sections
Principles · Tokens · Splash · Onboarding · Route transition table (per route from `ux-flows.md`) · Navigation · Micro-interactions · Reduced-motion alternatives · Flutter implementation guidance · Performance.
