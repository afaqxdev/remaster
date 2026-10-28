# Phase 8: Development spec (`build-prompt.md`)

After Phase 4, write a short version that covers only the approved sample. In Phase 8, rewrite it as the full prompt that maps **every Figma screen, component, asset, interaction and animation** to its implementation, and documents dependencies, project conventions, localization, accessibility and acceptance criteria. It must let Claude implement the design without guessing: link to the other deliverables for detail, but put every decision that affects code in the prompt itself.

## Template

```markdown
# Build: <App> (Flutter)

You are implementing an approved redesign. Source of truth, in order: this prompt,
design-system.md, screen-specifications.md, ux-flows.md, motion-system.md, app-dossier.md.
Do not invent features, APIs, data or backend services. Use placeholders only where marked
APPROVED-PLACEHOLDER. If something is ambiguous, ask.

## 1. Product
Purpose, audience, target platform(s): <Android | iOS | Both>. Verified features vs assumptions.

## 2. Architecture & data contract (required before Phase 9)
- **Folder structure:** `lib/{app, core/theme, core/widgets, core/routing, features/<feature>/{data,domain,presentation}, l10n}` — or the existing project's structure.
- **State management:** the project's existing choice; for a new app the one the user confirmed at Gate 2 (default Riverpod). Never `setState` sprawl across large screens.
- **Navigation:** GoRouter route table — name, path, params, transition, guards, deep links (e.g., `/c/:code` for challenges), `StatefulShellRoute` for tabs.
- **Data contract:** every model (fields, types, nullability, JSON keys) and every repository interface (methods, errors) per feature.
- **Dependency injection & mock data layer:** every repository/service is an interface injected via DI (Riverpod providers / `get_it` / constructors). Mock implementations + fixtures cover every state in `screen-specifications.md` (empty, loading, error, offline, success) and are selected by DI overrides, so 9b–9c run without a backend and 9d swaps to real implementations with zero UI changes.
- **Persistence & services:** local storage choice, analytics/ads/billing boundaries behind interfaces.

## 2b. Project
- New app: `flutter create --org <org> --platforms=<...> <name>`; build from the approved Figma frames.
- Existing app: audit first; keep its architecture, state management and business logic;
  restyle without replacing working logic.
- Stack (unless the project already uses something else): go_router (StatefulShellRoute for tabs),
  <state mgmt: Riverpod by default>, `animations` package, <fonts via google_fonts or bundled>.
- Folder structure: lib/{app, theme, widgets, features/<feature>/{data,ui}, routing, l10n}.

## 3. Design tokens
Paste final tokens: colors (light/dark), text styles, spacing, radii, elevation, motion.
Implement in theme/tokens.dart + ThemeData + ThemeExtension. No hardcoded values in screens.

## 4. Components
List each reusable widget, its variants, states and tokens.

## 5. Navigation & routes
Route table: name | path | params | transition | back behavior | state preservation. Deep links.

## 6. Screens (MVP order)
For each: purpose, layout, components, copy, actions, validation, all states, responsive, a11y, motion.

## 7. Motion
Transition rules per route, splash, onboarding, nav, micro-interactions, reduced motion.

## 8. Data & backend boundaries
Repositories/interfaces per feature; which are real (with known endpoints) vs approved placeholders.
Services from `app-dossier.md` → Services & cost, within the user's budget: the chosen provider/package per need, its free-tier limits, and the upgrade path behind the same interface. With budget 0, no paid-only package or service appears in the spec — but every feature, screen and state still does; only the provider behind each interface changes.

## 9. Localization & accessibility
ARB-based l10n, RTL if relevant, semantics labels, text scaling, contrast, 48dp targets.

## 10. Priorities
MVP: <screens/features>. Then: <...>. Then: <...>.

## 11. Quality, testing, performance
- `flutter analyze` clean; widget tests for key components; navigation tests for critical journeys;
  golden tests for the main screens if practical.
- Verify on small/large phones (and tablet if relevant) for each target platform.
- No jank in profile mode on key transitions; controllers disposed; no needless rebuilds.

## 12. Acceptance criteria
Checklist per screen and flow — observable and testable.
```
