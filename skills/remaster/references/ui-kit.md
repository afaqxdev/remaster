# UI Kit first (mandatory)

No screen is designed or coded until a complete, original UI Kit exists and has been checked. A redesign that only changes colours or backgrounds is a failure — redo it.

## 1. Build the kit (Figma *Foundations* + *Components* pages, exported to `design-tokens.json`)
| Area | Must define |
|---|---|
| Colours | primary, secondary, accent, background, surface levels, text (primary/secondary), border, success, warning, error, disabled, scrim — light **and** dark |
| Typography | families, sizes, weights, line heights, letter spacing; styles for display, heading, subtitle, body, label, caption, button |
| Spacing & layout | spacing scale, screen padding, gaps, grid, safe areas, breakpoints (phone / tablet) |
| Shape & elevation | radii, borders, shadows, surface hierarchy |
| Components | buttons, icon buttons, cards, text fields, dropdowns, checkboxes, switches, chips, tabs, dialogs, bottom sheets, navigation bars, banners/toasts, list rows, progress/loading — only those the product needs, plus product-specific ones |
| States | default, hover (where applicable), focused, pressed, selected, disabled, loading, error, success — for every interactive component |
| Icons & illustration | one icon family + custom key icons; illustration direction (see `visual-quality.md`) |
| Motion | durations, easing/springs, transitions, reusable patterns (see `motion-research.md`) |
| Responsive | how components and layouts adapt across phone and tablet widths |

Everything is a token or a component; screens never carry one-off values.

## 2. Validate the kit before any screen
- Build a **kit board** (all components × all states, light + dark) and screenshot it.
- Check: contrast measured, every state present, components look like one family, nothing on the do-not-copy list, modern-UI rules and colour check pass.
- For an **existing app**: list its UI weaknesses first (hierarchy, typography, components, spacing, navigation, iconography) and show how the kit fixes each.

## 3. Apply it everywhere
Every screen in the inventory uses only kit tokens and components — splash, onboarding, home/dashboard, history, data entry/forms, reports/analytics, export/preview (e.g. PDF), settings, dialogs, sheets, navigation, and every state. Never redesign only the home screen.

## 4. Prove it's a real redesign
Before Gate 1 and again in Phase 10:
- Compare original vs redesigned **per screen** — side by side when the user supplied the original (their own app or project), otherwise against the text inventory and do-not-copy list (never by opening store screenshots).
- For each screen confirm changes beyond colour: layout & hierarchy, components, typography, spacing, navigation/IA, icons & graphics.
- Any screen that reads as "same layout, new colours" is redesigned again.

## 5. In code (Phase 9)
Kit → `ThemeData`/`ThemeExtension` + shared widgets first (9a), with a widget gallery and golden tests per component/state. Screens consume only those. Existing projects keep their architecture, business logic, navigation, data, integrations and localization.
