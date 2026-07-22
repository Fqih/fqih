# Bio README Redesign — Gateway to Portfolio

**Date:** 2026-07-22 (revised nine times — v1 cream, v2 camo + horizontal CTA, v3 chrome + shorter role, v4 chrome bar + IPK + big role, v5 SVG circle + name + 6 stats + brand icons, v5.1 cyan + 2+ years + 19 certs + hyphen, **v5.2 inline brand-colored icons (no boxes) + responsive stats (2 rows on small screens)**, **v5.3 tighten stats→strip gap + 2 prominent CTA buttons (Portfolio, Connect) below icon row + cleaner HuggingFace icon**, **v5.4 drop wide stats (2-row layout only) + redesign Portfolio/Connect buttons as 4-color Google strip with centered arrow (no text label)**)
**Status:** Draft
**Repo:** `fqih` (GitHub profile bio at `github.com/Fqih/fqih`)
**Companion repo:** `porto` (`faqihhakim.tech`)
**Sub-domain:** `connect.faqihhakim.tech` (contact hub)

## Goal

Make the GitHub profile README a **lightweight gateway** to the portfolio. It should:

1. Identify who the person is (one glance).
2. Surface the **hero facts that aren't easily visible on the portfolio** (current role, location) — but **omit GPA** to keep the bio low-surface-area for personal data.
3. Push visitors to `faqihhakim.tech` for full case studies, experience, and tech stack.
4. Show **GitHub stats** (stars, streak, repos, followers) as a **single compact inline SVG**, one row, modest height.

It must **not** duplicate content that already lives on the portfolio (projects, achievements, experience details, full tech stack, current focus bullets).

## Non-goals

- Do not redesign the portfolio (`../porto`).
- Do not maintain multi-file SVG assets in a `svg/` folder — the inline SVG lives inside `README.md` as embedded markup.
- Do not write a long-form README.

## Final README structure (≤ 25 rendered lines)

```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 28" width="100%" height="28" role="img" aria-label="macOS-style window controls, name, and Open to Work"><title>top bar</title><circle cx="12" cy="14" r="6" fill="#FF5F57"/><circle cx="36" cy="14" r="6" fill="#FEBC2E"/><circle cx="60" cy="14" r="6" fill="#28C840"/><text x="400" y="19" text-anchor="middle" font-family="Poppins, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" letter-spacing=".05em" fill="#1E1C19">Faqih Hakim</text><circle cx="608" cy="14" r="6" fill="#01d5ff"/><text x="790" y="19" text-anchor="end" font-family="Poppins, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#1E1C19">Open to Work - Q4 2026</text></svg>

`Final-year Informatics · Jakarta, Indonesia`

# AI & Data Engineer

LLM, data, and graph-based intelligence

<a href="https://faqihhakim.tech/" aria-label="Portfolio"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="#4285F4" role="img"><title>Portfolio</title><path d="M14.5 2 L9.5 2 L9.5 7 L7 11 L7 17 L10 17 L10 22 L14 22 L14 17 L17 17 L17 11 L14.5 7 Z"/></svg></a> <a href="https://www.linkedin.com/in/faqih-hakim/" aria-label="LinkedIn"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="#0A66C2" role="img"><title>LinkedIn</title><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a> <a href="https://connect.faqihhakim.tech/" aria-label="Connect"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="#2D2D2B" role="img"><title>Connect</title><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></a> <a href="mailto:mhmdfkih21@gmail.com" aria-label="Email"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="#EA4335" role="img"><title>Email</title><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg></a> <a href="https://huggingface.co/faqihhakim" aria-label="Hugging Face"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" role="img"><title>Hugging Face</title><circle cx="12" cy="12" r="10" fill="#FFB000"/><circle cx="9" cy="10" r="1.4" fill="#1E1C19"/><circle cx="15" cy="10" r="1.4" fill="#1E1C19"/><path d="M8 14 Q12 17.5 16 14" stroke="#1E1C19" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg></a>

<a href="https://faqihhakim.tech/" aria-label="Portfolio"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 48" width="100%" height="48" role="img"><title>Portfolio</title><defs><clipPath id="btn-portfolio"><rect width="220" height="48" rx="10"/></clipPath></defs><g clip-path="url(#btn-portfolio)"><rect x="0" y="0" width="55" height="48" fill="#EA4335"/><rect x="55" y="0" width="55" height="48" fill="#FBBC05"/><rect x="110" y="0" width="55" height="48" fill="#34A853"/><rect x="165" y="0" width="55" height="48" fill="#4285F4"/></g><path d="M 100 24 L 120 24 M 110 18 L 120 24 L 110 30" stroke="#ffffff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></a> <a href="https://connect.faqihhakim.tech/" aria-label="Connect"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 48" width="100%" height="48" role="img"><title>Connect</title><defs><clipPath id="btn-connect"><rect width="220" height="48" rx="10"/></clipPath></defs><g clip-path="url(#btn-connect)"><rect x="0" y="0" width="55" height="48" fill="#EA4335"/><rect x="55" y="0" width="55" height="48" fill="#FBBC05"/><rect x="110" y="0" width="55" height="48" fill="#34A853"/><rect x="165" y="0" width="55" height="48" fill="#4285F4"/></g><path d="M 100 34 L 120 14 M 108 14 L 120 14 L 120 26" stroke="#ffffff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></a>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 112" width="100%" style="display:block;margin:0" role="img" aria-label="Faqih stats: 840 contributions, 33 Stars, 3.87 GPA, 2+ years experience, 18+ projects, 19 certifications" font-family="Poppins, 'Segoe UI', Roboto, sans-serif"><title>Faqih Stats</title><style>.num{fill:#4C5D3A;font-size:20px;font-weight:700;letter-spacing:-.02em;}.label{fill:#6B5D3F;font-size:9px;font-weight:700;letter-spacing:.14em;}.div{stroke:#8A8265;stroke-width:1;}</style><text x="90"  y="26" text-anchor="middle" class="num">840</text><text x="90"  y="44" text-anchor="middle" class="label">CONTRIBUTION</text><line x1="180" y1="14" x2="180" y2="42" class="div"/><text x="270" y="26" text-anchor="middle" class="num">33</text><text x="270" y="44" text-anchor="middle" class="label">STARS</text><line x1="360" y1="14" x2="360" y2="42" class="div"/><text x="450" y="26" text-anchor="middle" class="num">3.87</text><text x="450" y="44" text-anchor="middle" class="label">GPA</text><line x1="180" y1="70" x2="180" y2="98" class="div"/><text x="90"  y="82" text-anchor="middle" class="num">2+</text><text x="90"  y="100" text-anchor="middle" class="label">YEARS</text><text x="270" y="82" text-anchor="middle" class="num">18+</text><text x="270" y="100" text-anchor="middle" class="label">PROJECTS</text><line x1="360" y1="70" x2="360" y2="98" class="div"/><text x="450" y="82" text-anchor="middle" class="num">19</text><text x="450" y="100" text-anchor="middle" class="label">CERTIFICATIONS</text></svg>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 8" width="100%" height="8" style="display:block;margin:0" preserveAspectRatio="none" role="img" aria-label="Google brand colors"><title>Google colors</title><rect x="0" y="0" width="200" height="8" fill="#EA4335"/><rect x="200" y="0" width="200" height="8" fill="#FBBC05"/><rect x="400" y="0" width="200" height="8" fill="#34A853"/><rect x="600" y="0" width="200" height="8" fill="#4285F4"/></svg>
```

### Block-by-block rationale

| Block | Content | Why |
|---|---|---|
| 1. Top chrome bar | Single full-width inline SVG: 3 macOS circles on left (`#FF5F57`, `#FEBC2E`, `#28C840`), `Faqih Hakim` centered wordmark, cyan SVG circle (`#01d5ff`) marker + `Open to Work - Q4 2026` text right-aligned | Three-zone layout in one element: window-control signal left, name center, availability signal right. The availability circle is drawn in SVG (not an emoji) so the visual marker stays consistent across renderers. |
| 2. Location/status chip | Inline code: `` `Final-year Informatics · Jakarta, Indonesia` `` | Identity + city + country. |
| 3. Role (H1) | `# AI & Data Engineer` | Markdown H1 — the bio's primary heading. |
| 4. Role explanation | Plain text: `LLM, data, and graph-based intelligence` | Small caption below the H1 — what Faqih builds. |
| 5. CTA bar (one row, brand-colored icons, no background boxes) | 5 inline `<svg>` icons on one markdown line, each wrapped in an `<a>` link, icon fill = brand color, **no background rectangle**. Order: Portfolio (`rocket`, `#4285F4`) → LinkedIn (`linkedin`, `#0A66C2`) → Connect (`link`, `#2D2D2B`) → Email (`gmail`, `#EA4335`) → HuggingFace (`huggingface`, `#FFB000`). | Brand-colored icons sit directly on the README canvas — no chip background, no shields.io box. Each icon is a real link to the destination (not a static image). |
| 5b. Prominent CTA buttons (one row, two arrow buttons, 4-color Google strip background) | Two `<a>` tags on one markdown line, each wrapping an inline `<svg>` button. Each button SVG is `viewBox="0 0 220 48"` with a `<defs><clipPath id="btn-N"><rect width="220" height="48" rx="10"/></clipPath></defs>` and a `<g clip-path="url(#btn-N)">` containing **4 equal-width `<rect>` strips** (each 55 wide × 48 tall) in canonical Google brand order: red `#EA4335` · yellow `#FBBC05` · green `#34A853` · blue `#4285F4`. A single white-stroke `<path>` arrow is centered on the button: **right-arrow `→`** for Portfolio (`M 100 24 L 120 24 M 110 18 L 120 24 L 110 30`), **up-right external-link arrow `↗`** for Connect (`M 100 34 L 120 14 M 108 14 L 120 14 L 120 26`). Arrow stroke `#ffffff`, `stroke-width="3"`, `stroke-linecap="round"`, `stroke-linejoin="round"`. **No text label inside the button.** The whole SVG renders as a single clickable element via the parent `<a>` wrapper. | Portfolio and Connect are the two destinations users land on most — making them visually prominent (4-color Google brand strip + arrow) signals where to go and ties them visually to the Google strip footer. Arrow direction differentiates the buttons: → for going forward into Faqih's work, ↗ for going off-site to a contact hub. |
| 6. Stats inline (2-row layout only, no responsive toggle) | **One** inline SVG: a 3-cell × 2-row layout (viewBox `0 0 540 112`). Same stats values/labels as before (`840 / CONTRIBUTION`, `33 / STARS`, `3.87 / GPA`, `2+ / YEARS`, `18+ / PROJECTS`, `19 / CERTIFICATIONS`). The stats SVG carries inline `style="display:block;margin:0"` and is immediately followed (no blank line) by the Google strip SVG, which also carries `style="display:block;margin:0"`. | Mobile-style 3×2 layout reads well on both desktop and mobile — desktop doesn't need a wider 6-cell layout because the 3×2 grid is more scannable. Single SVG simplifies the file and removes the responsive `@media` toggle. The stats→strip join stays tightened. |
| 7. Google strip (bottom chrome) | 4-segment Google brand-color bar inline SVG: red `#EA4335` · yellow `#FBBC05` · green `#34A853` · blue `#4285F4` | Visual frame bottom. |

### Inline SVG stats design (v5.4 — 2-row layout only, no responsive toggle)

- **One SVG** (v5.4): the 3-cell × 2-row layout (viewBox `0 0 540 112`) is the only stats SVG. The wide 6-cell × 1-row layout is dropped. Total file SVG count is now **5** (top chrome + 2 buttons + narrow stats + bottom chrome).
- **Narrow layout (used on ALL viewports, both desktop and mobile):** viewBox `0 0 540 112`, 3 cells × 2 rows. Row 1 cells at `x=90 / 270 / 450` carry `840 / CONTRIBUTION`, `33 / STARS`, `3.87 / GPA`. Row 2 cells at `x=90 / 270 / 450`, `y=82` for numbers and `y=100` for labels, carry `2+ / YEARS`, `18+ / PROJECTS`, `19 / CERTIFICATIONS`. Dividers at `x=180 / 360` for both rows (y range `14-42` for row 1, `70-98` for row 2).
- **No responsive toggle.** The wide 6-cell × 1-row SVG and its `@media (max-width: 600px)` CSS are gone. The 3×2 grid reads cleanly at every viewport width.
- **Typography:** Poppins; number `20px / 700`, label `9px / 700 / .14em tracking` (uppercase).
- **Color palette (woodland camo):** numbers `#4C5D3A`, labels `#6B5D3F`, dividers `#8A8265`.
- **Label language:** English. `CONTRIBUTION`, `STARS`, `GPA`, `YEARS`, `PROJECTS`, `CERTIFICATIONS`.
- **Numbers are static for v1** (`840` / `33` / `3.87` / `2+` / `18+` / `19`). Dynamic update is a future concern.
- **v5 swap:** `IPK` → `GPA` (English label, matches international audience). Projects (`18+`) and Certifications (`19`) added to match portfolio's published counts and LinkedIn profile.
- **v5.3 join:** the stats SVG and the Google-strip SVG are placed on **consecutive physical lines (no blank markdown line between them)**, and the strip SVG carries `style="display:block;margin:0"` so default browser block margins don't add vertical whitespace. The stats SVG also carries `style="display:block;margin:0"` for symmetry.
- **v5.4 simplification:** only the 2-row layout exists. No `@media` toggle, no wide 6-cell SVG. The 3×2 grid reads cleanly on both desktop and mobile.

### Top chrome bar (v5 — name + SVG green circle)

- **Inline SVG**, full width, 28 px tall, viewBox `0 0 800 28`, attribute `width="100%"`.
- **Three zones** in a single horizontal strip:
  - **Left** (window controls): 3 macOS Big Sur+ circles — close `#FF5F57`, minimize `#FEBC2E`, maximize `#28C840`. Centers at `cx="12"`, `cx="36"`, `cx="60"`; radius 6; baseline `cy="14"`.
  - **Center** (name wordmark): `Faqih Hakim` text at `x="400"` `text-anchor="middle"`, font Poppins 13px/700, letter-spacing `.05em`, fill `#1E1C19`. Letter-spacing is `.05em` (not `.18em`) because the longer name reads better with subtle tracking than heavy letterform expansion.
  - **Right** (availability, no emoji): cyan SVG `<circle>` at `cx="608"`, `cy="14"`, `r="6"`, fill `#01d5ff`, followed by `Open to Work - Q4 2026` text at `x="790"` `text-anchor="end"`, font Poppins 13px/600, fill `#1E1C19`. The cyan circle replaces the v4 `🟢` emoji so the marker is rendered identically across all clients.
- Single physical line.

### Google brand strip (bottom chrome)

- **Inline SVG**, full width, 8 px tall, viewBox `0 0 800 8`, `preserveAspectRatio="none"` so segments scale to README column width.
- **4 equal segments**, 200 px wide in viewBox, colors in canonical Google brand order: red `#EA4335` · yellow `#FBBC05` · green `#34A853` · blue `#4285F4`.

### Inline brand-colored icons (v5.2 — no shields.io boxes)

- **Inline `<svg>` icons** on the README canvas, each wrapped in an `<a>` link tag. No background rectangle, no shields.io, no chip.
- **Icon dimensions:** each SVG is `width="28" height="28"` with `viewBox="0 0 24 24"`. Icons sit directly on the README with only the spacing between them.
- **Color:** each `<svg>` has `fill="<brand-color>"` on the root element, and the `<path>` inherits the fill (no per-path color).
- **Icon paths (simple-icons + feathericons):**
  | Channel | Destination | Brand color | SVG path source |
  |---|---|---|---|
  | Portfolio | `https://faqihhakim.tech/` | `#4285F4` Google blue | hand-crafted rocket path on 24×24 |
  | LinkedIn | `https://www.linkedin.com/in/faqih-hakim/` | `#0A66C2` LI blue | simple-icons `linkedin` |
  | Connect | `https://connect.faqihhakim.tech/` | `#2D2D2B` charcoal | feathericons `link` |
  | Email | `mailto:mhmdfkih21@gmail.com` | `#EA4335` Gmail red | simple-icons `gmail` |
  | HuggingFace | `https://huggingface.co/faqihhakim` | `#FFB000` HF yellow | simple-icons `huggingface` (**v5.3 — use the latest simple-icons canonical path**, which renders cleanly at 24×24; if the canonical path still looks like a face emoji, fall back to a hand-crafted clean HF face — yellow circle with two black dot eyes and a small smile arc — sized for the 24×24 canvas) |
- All 5 on **one** markdown line, single spaces between, separated by spaces (no blank lines).
- Accessibility: each `<a>` carries `aria-label="<channel name>"` so the link has a name.

### Prominent CTA buttons (v5.4 — 4-color Google strip + centered arrow, no label)

- **Two `<a>` tags** on **one** markdown line (no blank line), each wrapping an inline `<svg>` button.
- **Each button SVG:** `viewBox="0 0 220 48"`, `width="100%"`, `height="48"`, `role="img"`, `<title>` element with the channel name for accessibility.
- **4-color Google strip background:** inside a `<defs><clipPath id="btn-N"><rect width="220" height="48" rx="10"/></clipPath></defs>`, a `<g clip-path="url(#btn-N)">` contains **4 equal-width `<rect>` strips** (each 55 wide × 48 tall) in canonical Google brand order: red `#EA4335` · yellow `#FBBC05` · green `#34A853` · blue `#4285F4`. The clip-path gives the button rounded corners (`rx="10"`).
- **Centered white-stroke arrow `<path>`** (no `<rect>` background, no `<text>` label inside the button):
  - **Portfolio:** right-arrow `→`. Path data: `M 100 24 L 120 24 M 110 18 L 120 24 L 110 30` (horizontal line at y=24 from x=100 to x=120, then arrowhead from x=110 to x=120 at y=18/24/30).
  - **Connect:** up-right external-link arrow `↗`. Path data: `M 100 34 L 120 14 M 108 14 L 120 14 L 120 26` (diagonal from x=100 y=34 to x=120 y=14, then corner at x=108 y=14 / x=120 y=14 / x=120 y=26).
  - Arrow stroke `stroke="#ffffff"`, `stroke-width="3"`, `fill="none"`, `stroke-linecap="round"`, `stroke-linejoin="round"`.
- **No text label inside the button.** Channel identity comes from the `<a>`'s `aria-label` attribute (`aria-label="Portfolio"` and `aria-label="Connect"`).
- **The two `<a>` tags are separated by a single space** on the markdown line, so GitHub renders them side by side.
- **Visual rationale:** the 4-color Google strip ties the buttons visually to the bottom Google strip footer. Arrow direction differentiates the buttons: `→` for going forward into Faqih's work, `↗` for going off-site to a contact hub.

## Style rules

- **Language:** English, short sentences. Match the portfolio's tone (calm, structured, practical).
- **Length target:** ≤ 25 lines.
- **No `##` headings deeper than H1:** the bio uses exactly one H1 (`# AI & Data Engineer`). No H2/H3/etc.
- **No name H1:** the bio's H1 is the role, not the name. Porto carries the name.
- **Single-line rule:** every SVG element (top chrome, stats, Google strip) and the CTA badge row each occupy **one** physical markdown line. No internal newlines, no blank lines between adjacent badges.
- **CTA layout (v5.2):** all 5 icon badges on **one** markdown line (separated by single spaces, no blank lines between). GitHub renders adjacent markdown image links on the same line as a horizontal row.
- **CTA layout (v5.4):** the two prominent CTA buttons (Portfolio + Connect) sit on **one** markdown line directly below the icon row, also separated by a single space. Both `<a>` wrappers sit on that line; the SVG button content is inline. The button row is separated from the icon row above and the stats row below by single blank markdown lines (matching the rest of the vertical rhythm).
- **Tight join (v5.3):** between the narrow stats SVG and the Google strip SVG, **no blank markdown line** — they sit on adjacent lines. All three SVGs in that block (wide stats, narrow stats, Google strip) carry inline `style="display:block;margin:0"` to eliminate default browser block margins.
- **No footer redirect line:** v3 had `Full case studies, experience, and tech stack → faqihhakim.tech`. v4 removes it — porto is already one tap away via the Portfolio CTA icon, and the explicit text pointer was duplicative.
- **No shields.io / badge background:** CTA icons render directly on the README canvas in their brand color. No `img.shields.io` URLs, no `for-the-badge` chips, no colored box behind the icon.
- **Color palette (v4):**
  - Woodland camo (stats SVG only): numbers `#4C5D3A`, labels `#6B5D3F`, dividers `#8A8265`.
  - macOS chrome (top): `#FF5F57` / `#FEBC2E` / `#28C840` (Big Sur+).
  - Google chrome (bottom): `#EA4335` / `#FBBC05` / `#34A853` / `#4285F4`.
  - CTA icon chips: brand colors (Google blue, LinkedIn blue, charcoal, Gmail red, HuggingFace yellow).
  - Top chrome text (FQIH wordmark + Open to Work): `#1E1C19` (zen-900). Ties the chrome bar to the rest of the type stack.
- **Emoji:** allowed only in the Open to Work text (inside the top chrome SVG). No decorative emoji elsewhere.
- **Icons:** inline brand-colored SVG icons for CTAs. No shields.io. No badge backgrounds.
- **No tables.** No multi-column layouts. Single-column flow only.
- **No images / hero photos.** Porto owns the visual identity; bio stays text-first.

## What gets removed from the current README

| Section / Asset | Action |
|---|---|
| 4 SVG cards in `svg/` (`custom-stats-{dark,light,base}.svg`, `streak-{dark,light,base}.svg`, `top-langs-{dark,light,base}.svg`, `trophy-{dark,light,base}.svg`) | Delete all 12 files in `svg/` folder |
| `## GitHub Overview` 2×2 table | Remove |
| `## Selected Work` (AI Fraud, LLM Workflow, Amazon Sentiment) | Remove — lives on porto |
| `## Experience` (PT Tunas Ridean, Gunadarma, GDGoC, PowerNET) | Remove — lives on porto |
| `## Achievements` (Grand Champion, 3rd Place, Finalist) | Remove — lives on porto |
| `## Tech Stack` (Core Tools + Data/ML + Infrastructure) | Remove — lives on porto |
| `## Current Focus` bullets | Remove — lives on porto |
| Long intro paragraph (lines 9–18) | Compress to single tagline |
| `Connect` row (LinkedIn, Discord, HuggingFace, Kaggle, ORCID) | Reduce to 4 CTAs (Portfolio, LinkedIn, Email, HuggingFace); keep the most-used |

## What stays

| Asset / Section | Reason |
|---|---|
| `Image/` folder | Historical assets; do not touch in this design. Future cleanup is a separate task. |
| `.github/scripts/` and `.github/workflows/` | May be reused later for badge automation, but no required changes for this design. |
| Identity line (Name, role) | The minimum the README must carry. |

## Constraints & assumptions

- GitHub README renders standard markdown + inline HTML; no custom CSS, no JS.
- Inline SVG (`<svg>...</svg>`) inside the markdown is allowed by GitHub and renders in the README view.
- The Portfolio button points to `https://faqihhakim.tech/` — the same canonical URL as the `porto` site.
- The bio does **not** attempt to mirror the portfolio's `zen` theme. Visual identity lives entirely on `porto`.
- Stats numbers are static for v1 — no GitHub Action, no shields.io dependency. The plan covers re-generation as a future, separate task.

## Out of scope

- Renaming or restructuring folders other than `svg/` (which is emptied).
- Changing GitHub Actions workflows.
- Adding badge auto-update jobs (shields.io without auth is sufficient for now).
- Translating the README to Indonesian.
- Touching the `porto` repo in any way.

## Acceptance criteria

1. `README.md` is ≤ 25 rendered lines.
2. **No `##` headings deeper than H1.** The bio may have at most one `# H1`.
3. **Exactly one H1, and it is `# AI & Data Engineer`.** No `# Muhammad Faqih Hakim` (name removed in v3; role is the H1 in v4/v5).
4. No HTML `<img>`, no `<table>`, no multi-column layout. **Inline `<svg>` is allowed**.
5. **Top chrome bar:** the **first non-blank line** of the README is a single-line inline `<svg>` containing 3 macOS circles (`#FF5F57` red, `#FEBC2E` yellow, `#28C840` green) on the left, `Faqih Hakim` text centered, and a cyan SVG `<circle>` (`#01d5ff`) followed by `Open to Work - Q4 2026` text right-aligned. **No emoji** (`🟢` is replaced by an inline SVG circle).
6. **Chip:** the line `` `Final-year Informatics · Jakarta, Indonesia` `` appears (verbatim, with the comma and `Jakarta`).
7. **Role explanation:** the line `LLM, data, and graph-based intelligence` appears immediately after the H1 on its own line (plain text, no bold).
8. **Five CTA icons sit on one markdown line** in this exact order: Portfolio → LinkedIn → Connect → Email → HuggingFace. Each is an inline `<svg>` (28×28 px, viewBox `0 0 24 24`) wrapped in an `<a>` link. **No shields.io, no `img.shields.io` URL, no background box.**
9. CTA brand colors: Portfolio `#4285F4`, LinkedIn `#0A66C2`, Connect `#2D2D2B`, Email `#EA4335`, HuggingFace `#FFB000` (HF yellow appears on the inner `<circle>` face element, not the `<svg>` root — see criterion 20). For the other 4 icons, the hex appears as `fill="<HEX>"` on the `<svg>` root; for HF the `#FFB000` fill is on the inner `<circle>` only.
10. CTA logo paths come from simple-icons / feathericons; the connect link icon is the feathericons `link` path. Each `<svg>` contains exactly one `<path>` with a `d` attribute.
11. Connect link points to `https://connect.faqihhakim.tech/`.
12. **Single stats SVG, 2-row layout.** One `<svg viewBox="0 0 540 112">` (no wide companion). Three cells × two rows. Row 1: `840 / CONTRIBUTION`, `33 / STARS`, `3.87 / GPA`. Row 2: `2+ / YEARS`, `18+ / PROJECTS`, `19 / CERTIFICATIONS`. Labels: `CONTRIBUTION`, `STARS`, `GPA`, `YEARS`, `PROJECTS`, `CERTIFICATIONS` (uppercase, English). No Streak / Repos / Followers / IPK. No `@media (max-width:600px)` toggle — same SVG on all viewports. No internal `<style>` `.stats-wide` / `.stats-narrow` classes.
13. SVG stats palette is **woodland camo**: number fill `#4C5D3A`, label fill `#6B5D3F`, divider stroke `#8A8265`.
14. **Bottom chrome:** a single-line inline `<svg>` rendering 4 equal Google-color segments (`#EA4335` red, `#FBBC05` yellow, `#34A853` green, `#4285F4` blue) appears as the **last non-blank line** of the README. Each color appears exactly once as a `<rect>` fill.
15. **No footer redirect line:** the v3 line `Full case studies, experience, and tech stack → **[faqihhakim.tech](...)**` is REMOVED.
16. **Five SVG elements total** appear in the README: top chrome, Portfolio button, Connect button, narrow stats, Google strip. The 2 button SVGs share **one** markdown line (separated by a single space); the other 3 SVGs each occupy their own single physical markdown line.
17. **`Faqih Hakim` wordmark** appears in the top chrome SVG (text content `Faqih Hakim`, fill `#1E1C19`, centered at `x="400"`). The v4 `FQIH` text is replaced.
18. No content from the old README's "Selected Work", "Experience", "Achievements", "Tech Stack", or "Current Focus" sections remains.
19. **No `KONTRIBUSI` and no `IPK` labels.** The leading label is `CONTRIBUTION`; the GPA cell uses `GPA`, not `IPK`.
20. **HF icon is a hand-crafted clean face.** The HuggingFace icon on the 5-icon row is a hand-crafted clean HF face sized for the 24×24 canvas: `<circle cx="12" cy="12" r="10" fill="#FFB000"/>` (yellow face), `<circle cx="9" cy="10" r="1.4" fill="#1E1C19"/>` (left eye), `<circle cx="15" cy="10" r="1.4" fill="#1E1C19"/>` (right eye), and `<path d="M8 14 Q12 17.5 16 14" stroke="#1E1C19" stroke-width="1.4" fill="none" stroke-linecap="round"/>` (smile). The `<svg>` has **no `fill` attribute on the root** — each element carries its own fill. No simple-icons `huggingface` path. No `M23.735` legacy face path.
21. **Two prominent CTA buttons** (Portfolio + Connect) appear on **one** markdown line directly below the 5-icon row, separated by a single space. Each button is an `<a>` tag wrapping an inline `<svg viewBox="0 0 220 48">` with: (a) a `<defs><clipPath>` containing a `width="220" height="48" rx="10"` rect, (b) a `<g clip-path>` containing **4 equal-width rect strips** (each 55×48) in Google brand order `#EA4335` / `#FBBC05` / `#34A853` / `#4285F4`, (c) a single centered white-stroke `<path>` arrow (Portfolio `→` path data `M 100 24 L 120 24 M 110 18 L 120 24 L 110 30`; Connect `↗` path data `M 100 34 L 120 14 M 108 14 L 120 14 L 120 26`). **No text label inside the button.** Each `<a>` has an `aria-label`.
22. **Stats is 2-row layout only (no wide SVG, no responsive toggle).** A single stats SVG with `viewBox="0 0 540 112"` is the only stats element. There is **no `viewBox="0 0 1080 56"`** SVG (wide layout dropped). The stats SVG carries inline `style="display:block;margin:0"` and is placed on a physical line directly adjacent (no blank line) to the Google strip SVG, which also carries `style="display:block;margin:0"`.
23. Working tree clean after commit; only `README.md` changed in the commit.

## Implementation summary (high-level only — see plan)

1. Rewrite `README.md` to the structure above.
2. Delete all 12 SVG files under `svg/`.
3. Remove the empty `svg/` folder.
4. Verify by reading the new file end-to-end and counting lines.
5. (v5.3) Confirm the new 2-button row renders as `<a><svg><rect/><path/><text/></svg></a>` with rounded background + icon + label, and that the narrow-stats → Google-strip join has no blank line and `display:block;margin:0`.
6. (v5.4) Drop the wide stats SVG entirely; keep only the 2-row narrow layout. Replace the 2 button SVGs with the 4-color Google strip + centered arrow design (no text label). Confirm 5 total SVGs.
