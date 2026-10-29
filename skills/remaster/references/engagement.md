# Phase 2b: Engagement, retention & habit design (`engagement-retention.md`)

Goal: an app people **choose** to come back to because it keeps giving them value — not one that manufactures activity. Adapt proven patterns from successful apps, games and marketplaces to *this* app's purpose, audience and business model.

Inputs: `app-dossier.md` (purpose, audience, reviews, competitors, monetization, budget). Runs after research and **before** Phase 3, so the approved mechanics shape the UI Kit and prototype.

## 1. Research retention patterns (only as deep as decisions need)
- Study 2–4 successful apps in the same category plus 1–2 relevant games or marketplaces (reuse the Phase 1 competitor list; research more only when it changes a decision).
- For each, record as text: engagement loop, progression, rewards, discovery, personalization, feedback, re-engagement (notifications, emails, widgets), and **why users return and where they drop off** — from reviews ("I stopped because…", "I open it every day to…").
- Take mechanics as ideas only; the no-copy rule applies to their UI too.

## 2. Core engagement loop
Define one repeatable loop that serves the app's core job:

**Trigger → Action → Immediate reward → Progress → Reason to return**

| Step | Must be |
|---|---|
| Trigger | relevant: a goal the user set, fresh content, a useful reminder |
| Action | the app's real value task, not busywork |
| Immediate reward | satisfying feedback or a useful result within seconds |
| Progress | visible movement toward something the user cares about |
| Reason to return | a next milestone, ongoing project, new content or personal recommendation |

If a step only exists to raise session time, cut it.

## 3. Select mechanics — the smallest set that clearly helps
Evaluate each; pick only those that fit the purpose, audience and business model, and justify each with research evidence:

| Family | Examples |
|---|---|
| Progression | milestones, levels, achievements, completion indicators |
| Rewards | unlocks, meaningful benefits, earned badges, useful bonuses |
| Discovery | personalized recommendations, new content, useful surprises |
| Personalization | adaptive home, remembered preferences, relevant suggestions |
| Collection | saved items, finished projects, curated libraries |
| Social (optional) | sharing, collaboration, friendly challenges, community |
| Habit | helpful routines, **optional** streaks, consistent progress feedback |
| Re-engagement | relevant notifications and contextual reminders with user control |
| Delight | polished motion, satisfying transitions, haptics/sound where fitting |

Prioritize as **Must / Should / Later**. Never add a mechanic because a competitor has it. Mechanics follow the budget rule (provider only; e.g. local notifications and on-device personalization on a 0 budget) — see `research.md` → Services & cost.

## 4. Retention UX
Specify:
- **First session:** time to first meaningful value (target: the first minute where possible), what the user achieves, the first reason to return.
- **Recurring journey** and progression model.
- **States:** empty, in-progress, completion, reward, milestone, and recovery after inactivity.
- **Return after 1 day / 1 week / 1 month+:** what changed, a welcoming summary, an easy restart — never a wall of losses.
- **Notifications:** ask for permission only after the user has seen value and in context; default frequency, per-type controls, quiet hours, and the value each notification delivers.
- **Progress visibility** that never crowds the core task.

## 5. Ethical engagement (non-negotiable)
- No deceptive countdowns, fabricated scarcity, misleading rewards or fake social proof.
- No punishment for breaks (streak freezes/repair or no streak at all); never make leaving, cancelling or deleting an account hard.
- Streaks, reminders and social features are optional and can be turned off.
- Respect notification preferences, privacy, accessibility and reduced motion.
- No artificial waits or meaningless tasks to stretch sessions.
- Optimize for user value, satisfaction and voluntary return — not compulsive use.

## 6. Deliverable — `engagement-retention.md`
1. Competitor and reference-app findings (text only, labeled `[verified]`/`[inferred]`).
2. Users' reasons to return and reasons to abandon.
3. The core engagement loop.
4. Selected mechanics: justification, expected user benefit, priority (Must/Should/Later); rejected mechanics with one-line reasons.
5. Journeys: first use, repeat use, return after inactivity.
6. Required screens, components, interaction states, animations and notifications.
7. Ethical checklist (section 5) with each item ticked or explained.
8. Measurement plan: activation (first value reached), meaningful repeat use (core action, not opens), D1/D7/D30 retention cohorts, feature adoption, completion/conversion outcomes, notification opt-in and opt-out — event names, properties and success thresholds.

## Engagement approval (before Phase 3)
Present the loop, chosen mechanics with their expected user benefit, and the ethical checklist. Retention-specific UI and functionality are added **only after the user approves**; record the approval in `status.md`. Revise as often as needed.

## Integration after approval
- **Phase 3–4:** UI Kit gets the components the mechanics need (progress, reward, milestone, streak/recap, recommendation, notification-settings); the representative screen set includes the first-value moment and one return or progress screen.
- **Phase 5:** every engagement state in `screen-specifications.md` (empty, progress, completion, reward, comeback, notification settings).
- **Phase 7:** reward, milestone and comeback moments become key-moment animations with reduced-motion fallbacks.
- **Phase 8:** `build-prompt.md` lists engagement logic, notification schedule and controls, and the analytics events from the measurement plan behind DI interfaces.
- **Phase 10:** audit checks the ethical checklist in the built app, that every event fires, and that streaks/notifications can be turned off.
