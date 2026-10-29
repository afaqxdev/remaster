# Changelog

## 1.4.0
- Update check at the start of every run (once per session): compares the installed version with the latest on GitHub and, when newer, asks *update now or continue?* Updates only on a yes; silent when up to date or offline. Every command runs it.

## 1.3.0
- New **Phase 2b — Engagement, retention & habit design** (`/remaster-engagement`): reasons users return or leave, one core loop (trigger → action → reward → progress → reason to return), the smallest set of mechanics with justification and priority, retention UX (first value, return after 1 day/week/month, notification timing and controls), an ethical checklist and a measurement plan → `engagement-retention.md`, approved by the user before any retention UI.
- Rule 13 *Ethical engagement*: no deceptive countdowns, fake scarcity or social proof, punishing streaks, artificial waits or hard-to-leave flows.
- Approved mechanics flow into the UI Kit, the prototype screen set, Phase 5 states, motion key moments, the dev spec (logic, notifications, analytics events) and both audits.

## 1.2.0
- Step 0 asks for a monthly budget for paid services; **0** means free tiers, open-source and on-device options only.
- The budget only changes which provider powers a feature — never the feature list, screens, states or design quality. When nothing free works, the feature stays and the user chooses how to power it.
- Research lists every external service the app or its competitors use (backend, maps, AI, SMS, payments…), with current pricing, free-tier limits and a budget-fitting alternative. Recorded in `app-dossier.md` → Services & cost and carried into the dev spec.

## 1.1.0
- No semi-fixed defaults: motion timings from each app's motion character (old values are fallbacks), screenshot count/narrative/style derived per app, smallest representative prototype set, colour distribution derived per app.
- Three app-specific theme concepts (palette, type, icons, components, layout, assets, motion) presented side by side before the UI Kit.
- App-aware design: no default house style; visual language, onboarding story and compositions derived per app; modern-UI patterns are options, not defaults; adaptive design review.
- New `/remaster-store-assets`: Play & App Store screenshots and the Play feature graphic — app-derived narrative, count and 1–3 directions, copy rules, brief questions, exact store sizes, policy rules, flattened exports.
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
