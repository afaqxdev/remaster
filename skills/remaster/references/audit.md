# Phase 8: Completeness audit (with the development spec) (`completeness-checklist.md`)

Walk `app-dossier.md` line by line against the deliverables. Don't declare done until every row is ✅ or has a written reason.

## Traceability table
| Dossier item (feature / screen / flow / state) | Covered in (file § section) | Status ✅ / ⚠️ / ❌ | Note |

## Checks
- [ ] Every feature has a flow; every screen has a spec
- [ ] Every route in `ux-flows.md` exists in `screen-specifications.md` and the build prompt
- [ ] Splash, onboarding, home and primary navigation designed and animated
- [ ] Loading / empty / error / success / disabled states covered where applicable
- [ ] All screens and components use tokens only
- [ ] UI Kit complete and validated; every screen built only from it; per-screen check shows changes beyond colour (layout, components, type, spacing, navigation, icons)
- [ ] Every transition follows `motion-system.md`; reduced-motion alternatives exist
- [ ] Accessibility: contrast, semantics, text scaling, touch targets, focus order
- [ ] Responsive: small/large phones, safe areas, keyboard, tablet/landscape if supported
- [ ] Platform specifics respected for the chosen platform(s)
- [ ] Unknowns documented as open questions, not guessed
- [ ] Figma: real file verified, or spec clearly labeled as such
- [ ] Nothing reused from the original app's brand assets
- [ ] App icon: static, distinctive at 48/29px, adaptive + monochrome (Android) and 1024 + dark/tinted (iOS) exports ready
- [ ] Icon, splash, onboarding illustrations and in-app icons share one style; every graphic/animation has a purpose; all assets original or licensed

## Handoff message
Deliverables with paths · verified vs inferred · open questions · what the user must decide or provide next.
