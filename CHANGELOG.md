# Changelog

## 1.1.0
- App-aware design: no default house style; visual language, onboarding story and compositions derived per app; modern-UI patterns are options, not defaults; adaptive design review.
- New `/remaster-store-assets`: Play & App Store screenshots and the Play feature graphic — three styles (Device-Hero, Lifestyle, Feature-Grid), copy-length rules, brief questions, 6-frame story, caption & policy rules, exact sizes, flattened exports.
- UI Kit-first rule: complete validated kit before any screen; no reskins.

## 1.0.0 — first public release
- Orchestrator skill `remaster` with 10 phases and two approval gates.
- Commands: `/remaster-research`, `/remaster-sample`, `/remaster-motion`, `/remaster-build`, `/remaster-audit`, `/remaster-status`, `/remaster-help`.
- Strict no-copy rules, do-not-copy list, honest evidence labels.
- Modern UI vocabulary, old-school red flags, colour-composition check, 5-question design review.
- Light + dark prototype, full design with every state, responsive and accessible.
- App icon as its own deliverable (3 concepts, Android adaptive + iOS exports).
- Figma Motion timelines for key moments, with a Figma → Flutter motion mapping (springs 1:1 via `SpringDescription.withDurationAndBounce`).
- Architecture & data contract, dependency-injected mock layer (9c → 9d with zero UI changes), reduced-motion fallbacks.
- Scripted Phase 10 audit: analysis, golden/integration tests, emulator vs Figma comparison.
- Token-efficient: per-phase skill loading, `status.md` handoffs, fresh-session points.
