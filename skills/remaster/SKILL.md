---
name: remaster
description: Research an existing mobile app (Google Play / App Store, optional user-supplied APK or IPA), understand its features and UX, and redesign it as a modern, premium Flutter app — product designer first, Flutter developer second. Gated workflow - a 4-5 screen Figma prototype for approval, then the complete Figma design, app icon and graphics, motion system and Flutter build spec, then (only after a second approval) pixel-accurate Flutter implementation and a visual/technical audit. Use when the user wants to redesign, rebuild, modernize or "make a better version of" an existing app in Flutter, or names an app and asks for a new design for it.
---

# Remaster

Turn any existing app into a modern, premium Flutter app. Act as a **product designer first and a Flutter developer second.** Research the app, establish a distinctive visual identity, get the design approved, implement it faithfully, and verify the result. Never jump from screenshots to generic UI, and never code before the final Figma design is approved.

**Workflow:** Step 0 discovery → 1–2 research & dossier → 3 visual direction → 4 Figma prototype → **GATE 1** → 5 complete Figma design → 6 graphics & app icon → 7 motion system → 8 development spec → **GATE 2** → 9 Flutter implementation → 10 visual & technical audit.

## Non-negotiable rules

1. **No premature design or coding.** No full design before Gate 1; no app code before Gate 2. "Looks good, continue" counts as approval; silence or a revision request does not. If a design can't be implemented faithfully in Flutter, explain the limitation and propose a solution before substituting anything.
2. **No fake evidence, no fake completion.** Don't claim reviews, screenshots, binary contents, a Figma file, a URL, a prototype, an asset, an animation or a test you did not actually access, create, implement or verify. Label claims in docs `[verified]`, `[inferred]` or `[assumption]`. Never mark a screen, asset, animation or test complete without doing and checking it.
3. **Strict no-copy: take the idea, never the design.** The app the user names is only a source of *concepts* — what it does, for whom, and what users like or hate. Never copy its screens, layouts, content design (screen structure, copy, wording, information order), colors, typography, icons, illustrations, logo, name, or design system (components, tokens, spacing, shapes). Its screenshots may be viewed **once, in Phases 1–2 only**, to understand functionality and flows and write a text inventory; after that they are **never opened, attached or referenced (Phases 3–10)**. Design from the text inventory and user needs on a blank canvas; if a choice happens to match the original, change it.
4. **Don't assume the platform.** Record the user's answer in `app-dossier.md` and apply it everywhere.
5. **Ask, don't invent.** When purpose, audience, business logic, navigation or monetization is unclear and it changes the design, ask one concise question. Don't ask what you can discover.
6. **No silent omissions.** Every feature in the dossier ends up with a screen, a flow, or a written reason why it needs none.
7. **Modern, new components.** Use the modern-UI vocabulary as options for *this* app (never a fixed house style), avoid every quality red flag, and run the self-review loop (screenshot → check → fix) in `references/design.md` before showing anything.
8. **Attractive, proper color.** A confident brand hue, deliberate accent, semantic colors tuned to the palette, measured contrast, designed light and dark themes — see the color composition check in `references/design.md`.
9. **Premium quality bar, including graphics.** Modern graphics, custom icons, a distinctive app icon and purposeful motion are **required deliverables**, not extras. Follow `references/visual-quality.md` and answer its 5-question professional review for every screen.
10. **No unnecessary rewrites.** In an existing Flutter project, preserve working business logic, dependencies, architecture and configuration unless a change is justified and approved. Read the project's own rules (CLAUDE.md, README, lint config, conventions) before changing anything.
11. **UI Kit first, never a reskin.** Before any screen is designed or coded, build and validate a complete original UI Kit (tokens, components with all states, icons, motion, light/dark, responsive rules) per `references/ui-kit.md`, apply it to every screen, and prove each screen changed beyond colours.
12. **App-aware, never a template.** Understand the product first, research when it changes a decision, then derive the visual language from this app's purpose, audience, features and brand. Never carry one project's style, layouts, palette or onboarding structure into another; design every screen — especially onboarding — for its own purpose (`references/design.md` → App-aware direction).

## Step 0 — Project discovery (ask before doing anything)

Ask in a single message:
1. App name or Google Play / App Store URL?
2. Target platform: Android, iOS, or both?
3. Can you provide the APK or IPA? (Optional. Enables deeper analysis; without it we use public listings, screenshots and reviews.)
4. New Flutter project, or an existing codebase (path)? Is source code available?
5. Any existing design assets (brand, logo, fonts, Figma) to respect, and which deliverables do you need (Figma only, or Figma + Flutter code)?

With question 3, include the **"Supplying an APK or IPA"** guide from `references/research.md` (the skill never downloads binaries itself).

If the user has no binary, continue without it and label findings `[inferred]`. **Check the design tooling now:** call the Figma MCP `whoami`; if it isn't connected, tell the user to authorize it via `/mcp`, or agree on the fallback (Figma-ready spec + `design-tokens.json` + SVG wireframes) before Phase 3. If an existing project is given, inspect its rules and structure now (read-only). Create the output folder `redesign/<app-slug>/`; all deliverables go there.

## Skills per phase (load only what the current phase needs)

Before using a skill, check it is installed and read its instructions once; if it's missing, use the closest alternative and say so. Resolve conflicting guidance and note which you followed.

| Phase | Load | Never load here |
|---|---|---|
| 0–2 Discovery & research | WebSearch/WebFetch/`curl`; `competitive-teardown` (competitor analysis); `ux-researcher-designer` (personas, journeys from reviews); `reverse-engineer-anything` only if a binary is supplied | design skills, Ponytail |
| 3–4 Direction & prototype | `ui-ux-pro-max`, `emil-design-eng`, `ui-design-system` (tokens); `apple-hig-expert` only if iOS is a target; Figma MCP (`figma-use`, `figma-generate-design`) | Ponytail, Flutter tooling |
| 5–7 Full design, graphics, motion | Figma MCP + `figma-use-motion` (timelines) — read `references/motion-research.md`; `ui-design-system` (component docs); `apple-hig-expert` (iOS only); `design` (icons/app icon) or `brand` when making graphics; `design:design-critique` / `design:accessibility-review` for reviews; `animate` for motion decisions | Ponytail, Flutter tooling |
| 8 Dev spec | flutter.dev / pub.dev docs only for package choices | design skills (decisions are already in the artifacts) |
| 9–10 Code & audit | `ponytail:ponytail` (coding), `ponytail:ponytail-review` (per change), `ponytail:ponytail-audit` (existing repo); `code-reviewer` (Dart/Flutter quality report, Phase 10); `figma-implement-motion` + `get_motion_context` for 9d animations (translate with `motion-research.md`); Flutter docs, `flutter` CLI | design skills — read the approved Figma and artifacts instead |

Alternatives when a first choice is unavailable: `design-system`, `typeui-fundamentals`, `design-skills:design-elevation` (direction); `apple-design`, `review-animations` (motion); `break-ui` (stress tests); jadx/apktool (binaries); a clearly labeled Figma-ready spec if Figma isn't authorized. Never claim a skill was used if it wasn't loaded. Don't add overlapping skills: `karpathy-coder` duplicates Ponytail, `a11y-audit` targets web frameworks (use `design:accessibility-review` for Figma), `epic-design` is for websites.

Record the tools and sources that materially shaped the result in a `## Sources & tools` section of `app-dossier.md`.

## Phases

Read each reference file when you reach its phase — not before.

| Phase | Reference | Output |
|---|---|---|
| 1–2. Research & app dossier (store, reviews, competitors, flows; binary if supplied) | [references/research.md](references/research.md) | `app-dossier.md` — feature inventory, user journeys, pain points, competitor notes, do-not-copy list |
| 3. Visual direction & design skills | [references/design.md](references/design.md), [references/visual-quality.md](references/visual-quality.md) | `design-direction.md` — colors, type, spacing, shapes, icon style, illustration style, motion principles, light/dark |
| 4. **UI Kit, then Figma prototype** (3 theme concepts → user pick → validated kit board → smallest representative screen set in light + dark, no code) | [references/design.md](references/design.md) | Figma Foundations + prototype screens, `sample-design.md`, draft `build-prompt.md` |
| **GATE 1** | — | User approves style, colors, type, layout, navigation, graphics, motion direction |
| 5. Complete Figma design (every screen & state, responsive, dark mode, a11y) | [references/design.md](references/design.md) | `design-system.md`, `screen-specifications.md`, `ux-flows.md` |
| 6. Graphics & app icon (3 icon concepts → final + exports; custom icons, illustrations, splash & onboarding visuals) | [references/visual-quality.md](references/visual-quality.md) | Figma *App icon* and *Graphics* pages, export-ready assets |
| 7. Motion system + **key-moment prototypes in Figma** (success/correct action, level or task complete, error, splash, onboarding) | [references/motion-flutter.md](references/motion-flutter.md) | `motion-system.md`, Figma *Motion — key moments* page |
| 8. Development spec — **architecture & data contract** (folders, state management, GoRouter routes, models, repositories, mock data layer) + completeness audit | [references/build-prompt.md](references/build-prompt.md), [references/audit.md](references/audit.md) | `build-prompt.md`, `completeness-checklist.md` |
| Store assets (any time after Gate 1) | [references/store-assets.md](references/store-assets.md) | Play/App Store screenshots + feature graphic (`/remaster-store-assets`) |
| **GATE 2** | — | Explicit "yes" to convert Figma into Flutter |
| 9. Flutter implementation — 9a design system & tokens · 9b screens & routing · 9c interactive states & mock data · 9d graphics, motion & real data | [references/implementation.md](references/implementation.md) | Flutter code, one sub-step at a time |
| 10. Visual & technical audit (scripted) | [references/implementation.md](references/implementation.md) | `flutter analyze`, unit/widget/golden/integration tests, emulator screenshots diffed against Figma exports, fixes until criteria pass |

No app code is written in Phases 1–8 — everything before Gate 2 is research, Figma and specs.

## Gate 1 (end of Phase 4)

Present the prototype (Figma link + light and dark screenshots of every screen), then ask the user to approve or revise: visual style, colors (both themes), typography, layout, navigation, graphics and animation direction. Revise and re-present as often as needed. Record the approved decisions at the top of `design-direction.md` under `## Approved` with the date. Phase 5+ builds on the approved direction, never starts over.

## Gate 2 (end of Phase 8)

Ask: **"The Figma design is complete and audited. Shall I convert it into Flutter code?"** Restate the platform and key build choices (new vs existing project, state management, architecture) so the user can correct them. Start Phase 9 only on an explicit yes; otherwise stop with the design handoff: deliverables with paths, verified vs inferred, open questions, and the verified Figma link (or a clearly labeled Figma-ready spec).

## Token efficiency

- Keep this file to workflow, gates and routing; detailed instructions live in `references/` and are read only in their phase.
- Load specialist skills only for the current phase (table above). Ponytail is for coding, refactoring and code review only — never research or Figma design.
- Never read a whole codebase when a targeted inspection is enough; don't re-read files or skill instructions already in context; avoid repeated research, unnecessary tool calls and verbose command output (filter with `head`, `grep`, `--quiet`).
- Save each phase's result in a concise Markdown artifact and reuse it as the handoff; don't repeat rules across files.
- Don't regenerate completed deliverables unless requirements change.
- Prefer the simplest solution that keeps correctness, security, accessibility and approved design quality; finish each task in as few necessary steps as possible without skipping verification.

### Handoff file and fresh sessions
Keep `redesign/<app-slug>/status.md` (≤ 20 lines): current phase, approved decisions, Figma link + key node ids, open questions, next step. Update it at the end of every phase.

Suggest a fresh session (the user runs `/clear` or opens a new one) at these points, starting with: *"Use remaster. Read `redesign/<app-slug>/status.md` and continue."*
- after **Gate 1** (research is done; Phase 5 needs only the artifacts and the Figma file),
- after **Gate 2** (coding needs only `build-prompt.md`, `status.md` and the Figma link),
- when switching to an unrelated task, or when context is mostly old tool output.

Context commands to suggest to the user in Claude Code: `/context` (see what fills the context), `/compact` (summarize while continuing a long phase), `/clear` (start fresh at the points above), `/model` (a lighter model for routine steps like exports, renames and test runs; the strongest model for direction, full design and architecture).

When a session resumes, read `status.md` first, then only the artifacts the current phase needs, and continue from the last completed phase.
