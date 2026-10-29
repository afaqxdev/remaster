# Phases 9–10: Figma → Flutter, then visual & technical audit (only after Gate 2)

Follow `build-prompt.md` as the source of truth; read the approved Figma frames (`get_design_context` / `get_screenshot` / `get_variable_defs`) for exact values.

## Phase 9 — Implementation

### Before writing code
- **Existing project:** read its rules (CLAUDE.md, README, `analysis_options.yaml`, folder conventions, state management, routing, DI) and follow them. Preserve working business logic, dependencies, architecture and configuration; any change to them needs a reason and the user's approval.
- **Faithfulness:** if any part of the design can't be built faithfully in Flutter (performance, platform limits, package gaps), stop and explain the limitation with a proposed solution before substituting a different design.

### Ponytail (code simplicity — used alongside the Flutter and design skills, not instead of them)
Before coding, check that the `ponytail:ponytail` skill is installed and load it; if it isn't, tell the user and don't claim to follow it. Apply it like this:
1. **Inspect before changing:** read the project structure, rules, related files and existing implementations first.
2. **Reuse:** existing widgets, utilities, theme tokens, dependencies and architectural patterns before new ones.
3. **YAGNI:** no unnecessary abstractions, files, packages, layers or clever solutions.
4. **Preserve project rules:** existing architecture, state management, localization, responsive patterns and conventions.
5. **Focused changes:** the smallest complete solution that satisfies the approved Figma design and the functional requirements.
6. **Keep quality:** never drop validation, error handling, accessibility, security or tests to write less code.
7. **Verify:** run tests, static analysis and visual comparison; review affected and dependent code (`ponytail:ponytail-review`) before calling anything done.

**Ponytail simplifies the implementation, never the design.** Custom graphics, approved animations, responsive layouts and every UI detail in the Figma design are requirements, not code to skip.

### Build order — one sub-step at a time, verify before moving on
- **9a · Design system & tokens:** generate `ThemeData` / `ColorScheme` / `ThemeExtension` (every mode), text styles, spacing/radius constants and `AppMotion` from `design-tokens.json`; build the core primitives (Button, IconButton, Tile, Key, TextField, Toggle, Banner, SettingsRow, Floating Nav, Sheet) with all states; a widget-gallery screen + golden tests for each primitive.
- **9b · Screens & routing:** scaffold every screen from `screen-specifications.md` with the GoRouter table from the spec; static layouts at all breakpoints; navigation, back behavior and deep links working.
- **9c · Interactive states & mock data — via dependency injection:** UI widgets depend only on **repository/service interfaces** provided through the project's DI (Riverpod providers, `get_it`, or constructor injection) — never on concrete classes, HTTP clients or fixtures. Register **mock implementations** of those interfaces for 9c and implement every state (loading, empty, error, offline, success, validation) and interaction against them. Rule: switching 9c → 9d must change only the DI registration (provider overrides / bindings), with **zero edits to UI widgets** — verify by diffing `presentation/` before and after 9d.
- **9d · Graphics, motion & real data:** app icon (`flutter_launcher_icons`), native splash (`flutter_native_splash`), SVG graphics (`flutter_svg`, theme-colored), animations from the Figma Motion timelines (`get_motion_context` → Flutter via the mapping table in `motion-research.md`: one `AnimationController` per moment, `Interval` per track, `SpringDescription.withDurationAndBounce` for springs) and `motion-system.md`, then swap mocks for real repositories behind the same interfaces.

### Quality while building
- `flutter analyze` clean; unit tests for logic, widget tests for components, integration tests for critical journeys.
- Security (OWASP Mobile Top 10): validate all external/deep-link input, no hard-coded secrets, sensitive data in secure storage, HTTPS only, minimal permissions.
- Version control: small logical commits per feature; PR with a review checklist (lint, tests, screenshots). Commit/push only when the user asks.

## Phase 10 — Visual & technical audit (scripted; repeat until acceptance criteria pass)
Claude Code can view images (Read a PNG) and the Figma MCP exports frames, so the visual check is real — but script it so it's repeatable:
1. **Static:** `flutter analyze` (zero issues) and `dart format --set-exit-if-changed .`.
2. **Tests:** `flutter test` (unit + widget) and golden tests (`matchesGoldenFile`) for primitives and key screens in light/dark and small/large sizes; `flutter test integration_test` (or Patrol / Maestro flows) for critical journeys.
3. **Screenshots:** drive each screen/state on an emulator per target platform (integration test or Maestro flow) and capture (`adb exec-out screencap -p > shots/<screen>.png`, or the iOS simulator tool); export the matching Figma frames with `get_screenshot` into `figma/<screen>.png`.
4. **Diff:** compare each pair with a small script (ImageMagick `compare -metric AE -fuzz 5%` or a pixel-diff script) and also open both images to judge spacing, type, color and graphics; list every discrepancy, fix, re-run.
5. **Performance & accessibility:** profile mode (no jank on key transitions), startup time, asset size; TalkBack/VoiceOver labels, contrast, touch targets, text scaling, reduced motion; platform behavior (back gesture, system bars, haptics).
   **Engagement:** every measurement-plan event fires once with the right properties; streaks, reminders and notifications can be turned off; no dark pattern from the ethical checklist slipped in.
6. **Report honestly:** what passed, what was fixed, what wasn't verified. Add a `code-reviewer` report and `ponytail:ponytail-review` on the changes.
