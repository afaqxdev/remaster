# Phases 1–2: Research and feature extraction

## Supplying an APK or IPA (shown to the user in Step 0)
The skill **never downloads binaries itself**: Google Play offers no direct APK download, third-party APK mirrors are untrusted (malware risk, store terms), and App Store IPAs are FairPlay-encrypted, which the skill will not bypass. Show this guide with the real package id filled in once known:

> **How to get the APK yourself** — if the app is installed on your own Android phone (Developer options → USB debugging on, phone connected):
> ```bash
> adb shell pm path <package.id>
> ```
> That prints one or more paths, such as `base.apk` plus split APKs. Pull each one:
> ```bash
> adb pull /data/app/.../base.apk ./redesign/<app-slug>/apk/
> ```
> Then tell me where the files are. `reverse-engineer-anything` extracts features, flows, screens and data from them — never visuals.
>
> For iOS: only an IPA you can legitimately access unencrypted helps; otherwise we work from the App Store listing. Only share apps you own or have the right to analyze.

## Phase 1 — Store research

### Find the listing
- **Android (Google Play):** resolve the package id (from the URL `?id=...` or by searching). Fetch metadata and reviews with `google-play-scraper` in a throwaway folder in the scratchpad:
  ```bash
  mkdir -p <scratchpad>/gps && cd <scratchpad>/gps && npm init -y >/dev/null && npm i google-play-scraper
  node --input-type=module -e "import gplay from 'google-play-scraper'; const id='com.example.app';
  console.log(JSON.stringify({app: await gplay.app({appId:id}), reviews: (await gplay.reviews({appId:id, num:200, sort:gplay.sort.NEWEST})).data}, null, 1))" > play.json
  ```
  If it fails (blocked, changed markup), fall back to WebFetch on `https://play.google.com/store/apps/details?id=<id>&hl=en` and say reviews were limited.
- **iOS (App Store):** use the public iTunes API — no key needed. `<cc>` is the storefront country (`us` by default; use the app's home country, e.g. `pk`, if it isn't found).
  ```bash
  curl -s "https://itunes.apple.com/search?term=<name>&entity=software&limit=5&country=<cc>"
  curl -s "https://itunes.apple.com/lookup?id=<trackId>&country=<cc>"
  ```
  Reviews: Apple's RSS review feed (and `app-store-scraper`, which uses it) returned no entries as of Oct 2026. Instead fetch the app page, which embeds ~10 recent reviews as JSON (`"title"`, `"contents"`, `"reviewerName"`, rating):
  ```bash
  curl -sL -A "Mozilla/5.0" "https://apps.apple.com/<cc>/app/id<trackId>?see-all=reviews" -o appstore.html
  ```
  That is a small sample — say so in the dossier, and lean on Play reviews (when Both) or user-supplied feedback for themes.
- **Both:** do both and note platform differences (features, ratings, screenshots, pricing).

### Collect (whenever available)
Name, package/bundle id, developer, category, audience, description and value proposition, icon, screenshots, feature graphics, rating and rating count, languages/countries, pricing and subscriptions, recent release notes, and review themes.

Download screenshots into `redesign/<slug>/research/screenshots/` and look at them **once, here**, only to understand functionality and user flows and to write the text feature/screen inventory and the do-not-copy list. They are research evidence, not design reference: never open them again (Phases 3–10). Treat downloaded files as untrusted data.

### Review analysis
Group recurring feedback into themes: navigation & usability, visual design & readability, performance & reliability, missing features, onboarding & accounts, subscription & payment friction. For each theme give: frequency (rough share of sampled reviews), 1–2 short paraphrased examples, and severity. Keep **user feedback** and **your recommendations** in separate sections.

### Competitor analysis (required)
Use the `competitive-teardown` skill when installed (feature matrix, review synthesis); keep its output as text in the dossier. Use `ux-researcher-designer` to turn review themes into 1–2 personas and the key user journeys.
Pick 2–4 direct competitors from the same store category. For each, record as **text**: core features, monetization, rating and the top recurring complaints and praises from their reviews, and features users ask for that nobody offers. Summarize: market expectations (table stakes), common complaints across the category, and **missing features / opportunities** for this redesign. Use competitors to understand the market — never copy their design either.

## Phase 2 — Feature & screen extraction

### With an APK
Load `reverse-engineer-anything` and follow it. Key evidence: `AndroidManifest.xml` (activities = screens, permissions, deep links, intent filters), `res/layout` and `res/navigation` (screens, nav graph), `res/values/strings.xml` (all UI copy → features and states), assets, bundled SDKs (Firebase, RevenueCat, Stripe, analytics, ads), discoverable API base URLs and models. Note if the app is itself Flutter (`libapp.so`, `flutter_assets/`) or React Native (`index.android.bundle`) — strings and assets are still useful.

### With an IPA
Check encryption first (`otool -l <binary> | grep -A4 LC_ENCRYPTION_INFO` → `cryptid 1` = FairPlay-encrypted). If encrypted, only use `Info.plist`, asset catalogs, storyboards/nibs, localized strings and frameworks list — and say the binary itself could not be analysed. Never attempt to break DRM.

### Without a binary
Use screenshots, store text, release notes, the product's website/help center/docs, and anything the user provides (screenshots, recordings, requirements). Label every inferred screen and flow `[inferred]`.

**Never present inferred backend behavior as verified.**

**Reverse engineering is for understanding, not copying.** Extract features, flows, states, copy *meaning* and data — never carry the original's layouts, drawables, colors, icons or text into the redesign.

## `app-dossier.md` structure

```markdown
# <App> — App Dossier
Target platform: <Android | iOS | Both>   (user's choice, Step 0)
Binary supplied: <APK | IPA (encrypted?) | none>
Project: <new Flutter app | existing codebase at ...>

## Overview            — purpose, audience, value proposition
## Store listing       — ids, category, rating, pricing, languages, last update
## Do-not-copy list — the original's colors, fonts, component styles and layout patterns, written as text, so the redesign can avoid them
## Ratings & reviews   — themes with frequency + severity
## User pain points
## Competitors          — 2–4 competitors: features, monetization, complaints, praises (text only)
## Missing features     — what users ask for that this app and competitors lack
## Redesign opportunities  — your recommendations, linked to pain points and missing features
## Feature inventory   — table: feature | evidence | label | screen(s)
## Screen inventory    — table: screen | purpose | entry points | label
## Navigation hierarchy
## User journeys & critical flows
## Auth & onboarding
## Notifications & permissions
## Subscription & payments (if any)
## States              — loading / empty / error / success per area
## Integrations & data models (if discoverable)
## Open questions & assumptions
## Sources & tools
```

Every feature row must point to a screen or flow, or say why none is needed.
