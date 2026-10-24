# Motion research — Figma (2026) → Flutter

Read in Phase 7 (designing motion) and Phase 9d (implementing it). Verified October 2026; re-check Figma release notes if a call fails.

## What Figma can do now
- **Figma Motion** (Config, June 2026): a native **timeline + keyframe** mode on the canvas. Per-layer keyframe tracks, preset styles (opacity, position, scale, rotation, size, path, text stagger), spring and cubic easing, video export, and Dev Mode / MCP hand-off of keyframes and easing. Sources: designcompass.org (Figma Motion revealed), acodez.in (Figma motion design), chatgate.ai (Figma Motion timeline).
- **Plugin API via the Figma MCP** (`use_figma` + the `figma-use-motion` skill):
  - `node.applyManualKeyframeTrack({type:'PROPERTY', name}, {keyframes})` — fields: `TRANSLATION_X/Y/XY`, `ROTATION`, `SCALE_X/Y/XY` (**vector values for SCALE_XY**), `OPACITY`, `WIDTH`, `HEIGHT`, `CORNER_RADIUS`, `STROKE_WEIGHT`, layout spacing, `PATH_TRIM_START/END`.
  - Colors: `manualKeyframeTracks.fills/strokes[index]`; effects: `{type:'INDEXED_ITEM', collection:'effects', index, field:'RADIUS'|'EFFECT_OPACITY'|…}` (blur, shadow, glow).
  - Easing: `EASE_*`, `*_BACK`, `CUSTOM_CUBIC_BEZIER`, springs `GENTLE/QUICK/BOUNCY/SLOW`, **`CUSTOM_SPRING {bounce 0–1}`**, `HOLD` (step).
  - Timeline per top-level frame: `node.setTimelineDuration(id, seconds)`; animate children, never the top-level frame.
  - Not animatable: 3D transforms, arcs/polygons, variant properties → use stacked layers + opacity/scale instead.
  - Gate: if any motion call throws "not a supported API", Motion isn't enabled → fall back to **Smart Animate keyframe frames** (one frame per keyframe, same layer names, `AFTER_TIMEOUT` reactions, spring easings).
- **Verification:** `get_screenshot` shows only the resting state. `get_motion_context` returns every animated node's keyframes + CSS (with spring curves as `linear(...)`) — use it to verify timing/values. `export_video` (MP4) + `ffmpeg` frame sampling for visual checks when ffmpeg is available.
- **Design → code:** `get_motion_context` (+ `figma-implement-motion` skill) is the source of truth for durations, easing and keyframes in Phase 9d. It emits CSS / motion.dev, not Dart — translate with the table below.

## Flutter equivalents (2026)
| Figma Motion | Flutter |
|---|---|
| One frame timeline | one `AnimationController(duration: timeline)` per moment; each track = `Interval(start/total, end/total)` |
| Multi-keyframe track | `TweenSequence` (weights = segment lengths) inside the track's `Interval` |
| `TRANSLATION_X/Y` | `Transform.translate` / `SlideTransition` (or flutter_animate `.moveX/.moveY`) |
| `SCALE_XY`, `SCALE_Y` | `ScaleTransition` / `Transform.scale(scaleY:)` — `SCALE_Y`→0 then swap layer = card-flip |
| `ROTATION` (deg, **+ = counter-clockwise**) | `Transform.rotate(angle: -deg * pi / 180)` (Flutter + = clockwise) |
| `OPACITY` | `FadeTransition` / `Opacity` (`.fade`) |
| `WIDTH/HEIGHT/CORNER_RADIUS` | `AnimatedContainer` or tweened `BoxDecoration`/`SizedBox` (prefer transforms for 60/120 fps) |
| fill/stroke color | `ColorTween` |
| effect blur `RADIUS` | `ImageFiltered(imageFilter: ImageFilter.blur(...))` — small areas only, costly |
| shadow / glow `EFFECT_OPACITY` | tweened `BoxShadow` |
| `PATH_TRIM_END` (rings, line draws) | `CustomPainter` + `PathMetric.extractPath(0, len * t)` |
| Text stagger | per-glyph/word widgets with staggered `Interval`s (flutter_animate `.animate(interval:)`) |
| `EASE_OUT/IN/IN_AND_OUT`, `*_BACK` | `Curves.easeOut/easeIn/easeInOut`, `Curves.easeOutBack` |
| `CUSTOM_CUBIC_BEZIER x1,y1,x2,y2` | `Cubic(x1, y1, x2, y2)` |
| **`CUSTOM_SPRING bounce b`** | **`SpringDescription.withDurationAndBounce(duration:, bounce: b)`** + `SpringSimulation` via `controller.animateWith(...)` — same number on both sides; author springs as `CUSTOM_SPRING` (presets have no published bounce) |
| `HOLD` | `Threshold(1.0)` curve |
| Light sweep / shimmer | `ShaderMask` + animated `LinearGradient` (or a `FragmentProgram` shader for richer effects) |
| Particles / confetti | `CustomPainter` driven by the controller (or a maintained confetti package) |
| Shared-element flight between screens | `Hero` / `animations` `OpenContainer` |
| Illustrator-grade or interactive loops | **Rive** (state machines, interactive) or **Lottie** (linear exports) with size budget |
| Haptics on keyframes | `HapticFeedback.selectionClick/lightImpact/mediumImpact` at the track times |
| Reduced motion | `MediaQuery.disableAnimationsOf(context)` → crossfade to final state |

Performance: Impeller is the default renderer; animate transform/opacity; wrap animated regions in `RepaintBoundary`; budget ~8 ms per frame on 120 Hz.

## Modern motion vocabulary (use for key moments)
Springs with a little bounce (0.15–0.35) and overshoot on landing · staggered waves (40–120 ms) · card-flip reveals (squash + layer swap) · depth: background recedes (scale 0.94 + blur + dim) · circular reveal in brand colour from the point of action · shared-element flight of the thing the user just made · light sweep / glow bloom on success · rolling counters (odometer) · activity-style rings filling · confetti tiles with gravity · Dynamic-Island-style toast morph (width/height/radius spring) · haptics synced to beats · everything interruptible, ≤ ~1.5 s before the user can act, with a reduced-motion version.
