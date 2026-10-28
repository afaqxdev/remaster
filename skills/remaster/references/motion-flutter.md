# Phase 7: Motion system (`motion-system.md`)

Motion must explain navigation, give feedback, preserve continuity and express the brand. No motion just to look animated. Load `emil-design-eng` (and `animate` for decision order) before writing this. Note: store and launcher icons are static — motion lives in the splash, onboarding and in-app experience.

## Key-moment animations in Figma (required)
Read `motion-research.md` first. Every moment that rewards or informs the user — the core success action (e.g., a correct guess), task/level complete, errors/invalid input, splash, onboarding — gets a **designed, playable animation in Figma**, not just a note.
- **Primary: Figma Motion timeline** (load the Figma `figma-use-motion` skill). One top-level frame per moment whose *resting state is the final state*; keyframe tracks on its children (transform, opacity, size, colour, blur/glow, path trim), `CUSTOM_SPRING` easing with explicit bounce, `setTimelineDuration`. Hide mid-animation-only layers at rest (opacity 0).
- **Fallback (Motion not enabled):** Smart Animate keyframe frames — one frame per keyframe, identical layer names, `AFTER_TIMEOUT` reactions with spring easing, flow starting point.
- Pick techniques for *this* moment from the motion vocabulary in `motion-research.md` — it's a menu of options, not a checklist; use only what the moment needs.
- Write a timing note under each moment (offset, duration, easing/bounce, haptic) and the reduced-motion alternative.
- **Verify** with `get_motion_context` (keyframes + spring curves) and, when ffmpeg is available, `export_video` frame samples; the user must be able to act again quickly — length set by the moment's purpose (a rare celebration can be longer than routine feedback), never padded to feel special.
These timelines are the source of truth for Phase 9d (`get_motion_context` → Flutter via the mapping table) and the Phase 10 visual check.

## Tokens — derived per app
First define the app's **motion character** in one line (e.g., calm and precise · brisk and utilitarian · playful and bouncy), from its personality, audience, platform conventions, accessibility needs and performance budget. Then set timing and easing **per interaction type** — feedback, navigation, content change, onboarding, expressive/celebration — and record a one-line reason for each in `motion-system.md`. Don't make motion slower, faster or more elaborate just to look distinctive.

**Fallback starting points** (use only when there's no better evidence; mark as assumptions and revise):

| Token | Duration | Curve (Flutter) | Use |
|---|---|---|---|
| `instant` | 100ms | `Curves.easeOut` | press feedback, toggles |
| `quick` | 200ms | `Curves.easeOutCubic` | small state changes, tab icon/label |
| `standard` | 300ms | `Easing.emphasizedDecelerate` | route transitions, sheets |
| `emphasized` | 450ms | `Easing.emphasizedDecelerate` / spring | hero, container transform, splash |

Common guidance worth checking against the app: exits a little shorter than entrances; things users wait on often stay short. Define the chosen tokens once in `theme/tokens.dart` (`AppMotion`).

## Splash
Native splash (`flutter_native_splash` or platform launch screen) shows the brand instantly; the Flutter splash continues it seamlessly: a brand reveal suited to the app's motion character (e.g., fade + subtle scale, a mark assembling, a reveal of the key visual), then a transition into onboarding/home. Keep it brief and end it as soon as init is done — never used to hide slow startup.

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
Active/inactive items: icon swap or fill + label/indicator change using the app's feedback timing. Tab content: fade-through. Preserve each tab's state and scroll (`StatefulShellRoute.indexedStack` in go_router or `IndexedStack`). Re-tapping the active tab scrolls to top / pops to root. Badges animate count changes subtly. Never animate the whole bar.

## Micro-interactions
Button press (a subtle press response such as a small scale or tonal change, at feedback timing), card selection, toggles, form validation (gentle shake only for errors, inline message fade-in), loading → success morph, favorite/bookmark (small pop + haptic), counter tweens, snackbars, pull-to-refresh. Each must communicate a result. Pair key ones with `HapticFeedback` (selection/light impact).

## Implementation rules
- Prefer implicit animations (`AnimatedContainer`, `AnimatedOpacity`, `AnimatedSwitcher`, `TweenAnimationBuilder`) for simple effects; `AnimationController` + `AnimatedBuilder` for choreography; `Hero`, `animations` package for transitions. Add a dependency only when it clearly beats native code.
- Dispose controllers; use `SingleTickerProviderStateMixin`/`TickerProviderStateMixin`; stop repeating animations when off-screen.
- Keep rebuilds small: pass `child` to `AnimatedBuilder`, animate transform/opacity, wrap busy animated regions in `RepaintBoundary`; avoid animating layout or blur on large areas.
- Target 60/120 Hz smoothness; profile with `flutter run --profile` and DevTools when in doubt.
- **Safe motion fallback (required, every animation):** respect the device's accessibility setting. Read `MediaQuery.disableAnimationsOf(context)` (same value as `MediaQuery.of(context).disableAnimations`, but rebuilds only when it changes). When it is `true`: skip movement, scale, rotation, parallax, particles, blur and springs; jump to the final state or use a ≤ 150–250 ms crossfade; keep state changes and haptics that convey meaning. Centralise it once (e.g., `AppMotion.reduced(context)` returning zero/short durations) so every widget and timeline obeys it, and cover it with a widget test that sets `disableAnimations: true`.

## `motion-system.md` sections
Principles · Tokens · Splash · Onboarding · Route transition table (per route from `ux-flows.md`) · Navigation · Micro-interactions · Reduced-motion alternatives · Flutter implementation guidance · Performance.
