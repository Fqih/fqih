# Bio README Gateway Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite the GitHub profile README at `Fqih/fqih` into a ≤ 25-line gateway that points visitors to `faqihhakim.tech`, and delete all 12 SVG assets in `svg/`.

**Architecture:** Pure documentation change. One markdown file is fully rewritten with five blocks (header, hero facts, CTA, inline stats, footer redirect). All visual assets are removed so the portfolio owns visual identity. Verification is by content inspection against the acceptance criteria.

**Tech Stack:** GitHub-flavored Markdown, shields.io badge endpoints.

## Global Constraints

- README rendered line count must be ≤ 25 (acceptance criterion #1).
- No `##` or deeper heading levels; the only heading is `# Muhammad Faqih Hakim` (acceptance criterion #2).
- No HTML `<img>`, no `<table>`, no multi-column layout. **Inline `<svg>` is allowed** — the new stats card is embedded as `<svg>...</svg>` markup inside `README.md`, not as a file reference (acceptance criterion #3).
- Portfolio CTA must use `for-the-badge` style with `#1E1C19` fill so it reads as the dominant action (acceptance criterion #4).
- Exactly one inline `<svg>` element on a single line in the README, height ≤ 64 px, containing all five stats: Kontribusi / Stars / Streak / Repos / Followers (Kontribusi leads), with numbers `840 / 33 / 1d / 27 / 61` (acceptance criterion #5).
- The final line must be a one-sentence redirect to `faqihhakim.tech` (acceptance criterion #6).
- No content from the old `Selected Work`, `Experience`, `Achievements`, `Tech Stack`, or `Current Focus` sections may remain (acceptance criterion #7).
- No mention of "GPA" or "IPK" anywhere in the README (acceptance criterion #8).
- The `svg/` folder must be empty after execution (acceptance criterion #9).
- Commit messages end with `Co-Authored-By: Claude <noreply@anthropic.com>` per repo convention.

---

## File Structure

| File | Action | Responsibility |
|---|---|---|
| `README.md` | Modify (full rewrite) | The only user-facing deliverable: the gateway README |
| `svg/custom-stats-dark.svg` | Delete | Replaced by inline shields.io stats |
| `svg/custom-stats-light.svg` | Delete | Same |
| `svg/custom-stats.svg` | Delete | Same |
| `svg/streak-dark.svg` | Delete | Replaced by inline shields.io streak badge |
| `svg/streak-light.svg` | Delete | Same |
| `svg/streak.svg` | Delete | Same |
| `svg/top-langs-dark.svg` | Delete | Languages live on portfolio; not duplicated in bio |
| `svg/top-langs-light.svg` | Delete | Same |
| `svg/top-langs.svg` | Delete | Same |
| `svg/trophy-dark.svg` | Delete | Achievements live on portfolio; not duplicated in bio |
| `svg/trophy-light.svg` | Delete | Same |
| `svg/trophy.svg` | Delete | Same |
| `svg/` (folder) | Remove after files are gone | Acceptance criterion #8 |

No other files are touched in this plan. `Image/`, `.github/scripts/`, and `.github/workflows/` are explicitly out of scope.

---

### Task 1: Rewrite README.md to the gateway structure

**Files:**
- Modify: `README.md` (full rewrite — replace all existing content)

**Produces:** The new `README.md` matching the spec's "Final README structure" block exactly.

- [ ] **Step 1: Confirm the working tree is at the right baseline**

The controller has already restored the original long-form `README.md` from commit `d928f0e` into the working tree (staged). Run:

```bash
wc -l /home/faqihhakim/dataDiri/web/fqih/README.md
git status --short
```

Expected: `wc -l` returns ~189 (the long-form original). `git status --short` shows `M  README.md` (modified, staged). If either is wrong, stop and report — do not run `git reset` or any other history-rewriting command.

- [ ] **Step 2: Replace `README.md` with the new gateway content (no GPA, inline SVG stats)**

The current staged content is the obsolete state. Overwrite `README.md` in full with the new content below. The `git add` at the end of this step re-stages your work; the staged long-form content from Step 1 is replaced.

Write the following content to `/home/faqihhakim/dataDiri/web/fqih/README.md` (overwriting the existing file in full):

```markdown
# Muhammad Faqih Hakim

**AI & Data Engineer** — Final-year Informatics student building practical
LLM workflows, data products, and graph-based intelligence systems.

`Final-year Informatics · Indonesia`

[![Portfolio](https://img.shields.io/badge/Portfolio-1E1C19?style=for-the-badge&logo=googlechrome&logoColor=white)](https://faqihhakim.tech/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/faqih-hakim/)
[![Email](https://img.shields.io/badge/Email-1E1C19?style=flat-square&logo=gmail&logoColor=white)](mailto:mhmdfkih21@gmail.com)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-FFB000?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/faqihhakim)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 56" width="100%" height="56" role="img" aria-label="GitHub stats: 840 contributions this year, 33 Stars, 1 day Streak, 27 Repos, 61 Followers" font-family="Poppins, 'Segoe UI', Roboto, sans-serif">
  <title>GitHub Stats</title>
  <style>.num{fill:#1E1C19;font-size:20px;font-weight:700;letter-spacing:-.02em;}.label{fill:#5F5142;font-size:9px;font-weight:700;letter-spacing:.14em;}.div{stroke:#ded8ca;stroke-width:1;}</style>
  <text x="90"  y="26" text-anchor="middle" class="num">840</text><text x="90"  y="44" text-anchor="middle" class="label">KONTRIBUSI</text>
  <line x1="180" y1="14" x2="180" y2="42" class="div"/>
  <text x="270" y="26" text-anchor="middle" class="num">33</text> <text x="270" y="44" text-anchor="middle" class="label">STARS</text>
  <line x1="360" y1="14" x2="360" y2="42" class="div"/>
  <text x="450" y="26" text-anchor="middle" class="num">1d</text> <text x="450" y="44" text-anchor="middle" class="label">STREAK</text>
  <line x1="540" y1="14" x2="540" y2="42" class="div"/>
  <text x="630" y="26" text-anchor="middle" class="num">27</text> <text x="630" y="44" text-anchor="middle" class="label">REPOS</text>
  <line x1="720" y1="14" x2="720" y2="42" class="div"/>
  <text x="810" y="26" text-anchor="middle" class="num">61</text> <text x="810" y="44" text-anchor="middle" class="label">FOLLOWERS</text>
</svg>

Full case studies, experience, and tech stack → **[faqihhakim.tech](https://faqihhakim.tech)**
```

The SVG must be on a single physical line in the file (no internal newlines). The four badge links above stay as they are.

- [ ] **Step 3: Verify line count is ≤ 25**

Run:
```bash
wc -l /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: 25 or fewer. Acceptance criterion #1 is satisfied when the count is ≤ 25.

- [ ] **Step 4: Verify no deep heading levels**

Run:
```bash
grep -nE '^##' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: no output. Acceptance criterion #2 is satisfied.

- [ ] **Step 5: Verify no `<img>`, no `<table>`, no multi-column layout (inline `<svg>` is allowed)**

Run:
```bash
grep -nE '<img|<table|srcset' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: no output. Note the grep intentionally omits `<svg` — the spec allows the inline SVG stats card. Acceptance criterion #3 is satisfied when this command produces zero matches.

- [ ] **Step 6: Verify the Portfolio CTA uses `for-the-badge` and `#1E1C19`**

The shields.io URL places the color token before the style token (`badge-Portfolio-1E1C19?style=for-the-badge`), so the grep must accept either order:

Run:
```bash
grep -nE 'for-the-badge.*1E1C19|1E1C19.*for-the-badge' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: one matching line containing the Portfolio badge. Acceptance criterion #4 is satisfied.

- [ ] **Step 7: Verify exactly one inline SVG with height ≤ 64 px on a single line**

Run each of these — the first must match the stats SVG line; the second must produce zero matches (no extra SVGs):

```bash
grep -nE '<svg[^>]*height="(32|40|48|56|64)"' /home/faqihhakim/dataDiri/web/fqih/README.md
grep -cE '<svg' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: the first grep prints exactly one line (the stats SVG with `height="56"`); the second prints `1`. Acceptance criterion #5 is satisfied.

- [ ] **Step 8: Verify all five stat labels appear inside the SVG**

Run:
```bash
grep -oE '>(KONTRIBUSI|STARS|STREAK|REPOS|FOLLOWERS)<' /home/faqihhakim/dataDiri/web/fqih/README.md | sort -u
```

Expected: five lines, one per label in alphabetical order: `FOLLOWERS`, `KONTRIBUSI`, `REPOS`, `STARS`, `STREAK`. Acceptance criterion #5 is fully satisfied when all five labels are present.

- [ ] **Step 8b: Verify the five stat numbers appear inside the SVG, in order**

Run:
```bash
grep -oE 'class="num">[0-9a-z]+<' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: five matches in this exact order — `840`, `33`, `1d`, `27`, `61`. Acceptance criterion #5's "Kontribusi leads" ordering is satisfied when this sequence matches.

- [ ] **Step 9: Verify no leftover content from removed sections**

Run:
```bash
grep -nE 'Selected Work|## Experience|## Achievements|## Tech Stack|Current Focus' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: no output. Acceptance criterion #7 is satisfied.

- [ ] **Step 10: Verify GPA / IPK is absent**

Run:
```bash
grep -niE 'GPA|IPK' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: no output. Acceptance criterion #8 is satisfied.

- [ ] **Step 11: Verify the final line redirects to faqihhakim.tech**

Run:
```bash
tail -1 /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: the line is `Full case studies, experience, and tech stack → **[faqihhakim.tech](https://faqihhakim.tech)**`. Acceptance criterion #6 is satisfied.

- [ ] **Step 12: Commit the rewritten README**

Run:
```bash
git add README.md && git commit -m "docs: rewrite bio README as portfolio gateway

Replaces the long-form README with a short gateway whose sole job is
to point visitors to faqihhakim.tech. Removes SVG cards, table layouts,
and sections that duplicate portfolio content (Selected Work,
Experience, Achievements, Tech Stack, Current Focus). Drops GPA from
the hero facts line. Keeps a dominant Portfolio CTA, secondary
connect badges (LinkedIn, Email, Hugging Face), and one inline SVG
that shows Stars, Streak, Repos, and Followers in a single compact
row.

Co-Authored-By: Claude <noreply@anthropic.com>"
```

Expected: one new commit on the current branch, with only `README.md` in the changeset.

---

### Task 2: Delete the `svg/` folder

**Files:**
- Delete: 12 files inside `svg/` (listed in the File Structure table above)
- Remove: the `svg/` directory itself

**Consumes:** Task 1's commit (so the working tree shows only the `svg/` deletions when this task runs). The new stats SVG lives inline in `README.md`, not in this folder.

- [ ] **Step 1: List the files to delete so the deletion is auditable**

Run:
```bash
ls -1 /home/faqihhakim/dataDiri/web/fqih/svg
```

Expected: 12 `.svg` filenames (the four sets × {dark, light, base}). Record the count. If the count is not 12, stop and report — the spec assumed 12 files and a mismatch means prior drift.

- [ ] **Step 2: Delete the `svg/` directory with git**

Run:
```bash
git rm -r /home/faqihhakim/dataDiri/web/fqih/svg
```

Expected: `git rm` removes all 12 files and the directory; git's status now lists the deletions. Do not use plain `rm` — using `git rm` keeps git's index in sync so the next commit records both the file removals and the directory removal.

- [ ] **Step 3: Verify the directory is gone**

Run:
```bash
test ! -e /home/faqihhakim/dataDiri/web/fqih/svg && echo "svg/ removed"
```

Expected: `svg/ removed`. Acceptance criterion #9 is satisfied.

- [ ] **Step 4: Verify `README.md` still references no local `svg/` path**

Run:
```bash
grep -nE '\./svg/|/svg/' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: no output. If any line matches, it means the README rewrite in Task 1 accidentally left a `src="./svg/..."` reference — fix it and amend before committing.

- [ ] **Step 5: Commit the deletion**

Run:
```bash
git commit -m "chore: remove legacy SVG cards from bio repo

The bio README now hosts its stats as one inline <svg> in the
markdown itself, so the svg/ folder of 12 files (custom-stats,
streak, top-langs, trophy × dark/light/base) is unused. Removing it
keeps the repo aligned with the new design.

Co-Authored-By: Claude <noreply@anthropic.com>"
```

Expected: one new commit listing 12 file deletions plus the directory removal.

- [ ] **Step 6: Verify the full set of acceptance criteria**

Walk the spec's acceptance criteria one more time against the working tree:

1. `wc -l README.md` shows ≤ 25. *(Verified in Task 1 Step 4.)*
2. `grep -nE '^##' README.md` shows nothing. *(Verified in Task 1 Step 5.)*
3. `grep -nE '<img|<table|srcset' README.md` shows nothing. *(Verified in Task 1 Step 6.)*
4. `grep -nE 'for-the-badge.*1E1C19|1E1C19.*for-the-badge' README.md` shows the Portfolio line. *(Verified in Task 1 Step 7.)*
5. `grep -nE '<svg[^>]*height="(32|40|48|56|64)"' README.md` shows one matching line and `grep -cE '<svg' README.md` shows `1`, with all four labels `STARS|STREAK|REPOS|FOLLOWERS` present. *(Verified in Task 1 Steps 8 and 9.)*
6. `tail -1 README.md` is the redirect line. *(Verified in Task 1 Step 12.)*
7. `grep -nE 'Selected Work|## Experience|## Achievements|## Tech Stack|Current Focus' README.md` shows nothing. *(Verified in Task 1 Step 10.)*
8. `grep -niE 'GPA|IPK' README.md` shows nothing. *(Verified in Task 1 Step 11.)*
9. `test ! -e svg` prints `svg/ removed`. *(Verified in Step 3 above.)*

All nine must pass. If any fails, fix the issue (amend or follow-up commit) before declaring done.

---

### Task 3: Update inline SVG stats — add Kontribusi (5 stats total)

**Files:**
- Modify: `README.md` (replace the 4-stat SVG with the 5-stat SVG)

**Consumes:** Task 2's commit. Spec and plan were updated to require a fifth stat — `KONTRIBUSI` (840 contributions this year) — at the leading position.

- [ ] **Step 1: Confirm the working tree is at Task 2's HEAD**

Run:
```bash
git status --short
```

Expected: empty output (working tree clean). HEAD should be at `cf5fe8e` (Task 2's deletion commit).

- [ ] **Step 2: Replace the SVG block in `README.md` with the 5-stat version**

The current SVG block in `README.md` is exactly:

```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 56" width="100%" height="56" role="img" aria-label="GitHub stats: 33 Stars, 1 day Streak, 27 Repos, 61 Followers" font-family="Poppins, 'Segoe UI', Roboto, sans-serif">
  <title>GitHub Stats</title>
  <style>.num{fill:#1E1C19;font-size:20px;font-weight:700;letter-spacing:-.02em;}.label{fill:#5F5142;font-size:9px;font-weight:700;letter-spacing:.14em;}.div{stroke:#ded8ca;stroke-width:1;}</style>
  <text x="90"  y="26" text-anchor="middle" class="num">33</text>  <text x="90"  y="44" text-anchor="middle" class="label">STARS</text>
  <line x1="180" y1="14" x2="180" y2="42" class="div"/>
  <text x="270" y="26" text-anchor="middle" class="num">1d</text> <text x="270" y="44" text-anchor="middle" class="label">STREAK</text>
  <line x1="360" y1="14" x2="360" y2="42" class="div"/>
  <text x="450" y="26" text-anchor="middle" class="num">27</text> <text x="450" y="44" text-anchor="middle" class="label">REPOS</text>
  <line x1="540" y1="14" x2="540" y2="42" class="div"/>
  <text x="630" y="26" text-anchor="middle" class="num">61</text> <text x="630" y="44" text-anchor="middle" class="label">FOLLOWERS</text>
</svg>
```

Replace it **in place** (no other lines change) with the following single-line SVG block:

```
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 56" width="100%" height="56" role="img" aria-label="GitHub stats: 840 contributions this year, 33 Stars, 1 day Streak, 27 Repos, 61 Followers" font-family="Poppins, 'Segoe UI', Roboto, sans-serif"><title>GitHub Stats</title><style>.num{fill:#1E1C19;font-size:20px;font-weight:700;letter-spacing:-.02em;}.label{fill:#5F5142;font-size:9px;font-weight:700;letter-spacing:.14em;}.div{stroke:#ded8ca;stroke-width:1;}</style><text x="90"  y="26" text-anchor="middle" class="num">840</text><text x="90"  y="44" text-anchor="middle" class="label">KONTRIBUSI</text><line x1="180" y1="14" x2="180" y2="42" class="div"/><text x="270" y="26" text-anchor="middle" class="num">33</text><text x="270" y="44" text-anchor="middle" class="label">STARS</text><line x1="360" y1="14" x2="360" y2="42" class="div"/><text x="450" y="26" text-anchor="middle" class="num">1d</text><text x="450" y="44" text-anchor="middle" class="label">STREAK</text><line x1="540" y1="14" x2="540" y2="42" class="div"/><text x="630" y="26" text-anchor="middle" class="num">27</text><text x="630" y="44" text-anchor="middle" class="label">REPOS</text><line x1="720" y1="14" x2="720" y2="42" class="div"/><text x="810" y="26" text-anchor="middle" class="num">61</text><text x="810" y="44" text-anchor="middle" class="label">FOLLOWERS</text></svg>
```

Notes:
- The replacement must remain on a **single physical line** in the file (no internal newlines).
- The viewBox widens from `0 0 720 56` to `0 0 900 56` to fit the fifth cell; cell centers and divider positions are recomputed for 5 equal cells of 180px.
- The `aria-label` is updated to mention the contribution count.
- No other line in `README.md` changes.

- [ ] **Step 3: Verify the SVG still satisfies the spec's height and single-line constraints**

Run:
```bash
grep -nE '<svg[^>]*height="(32|40|48|56|64)"' /home/faqihhakim/dataDiri/web/fqih/README.md
grep -cE '<svg' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: the first grep prints exactly one line (height="56"); the second prints `1`.

- [ ] **Step 4: Verify all five labels are present**

Run:
```bash
grep -oE '>(KONTRIBUSI|STARS|STREAK|REPOS|FOLLOWERS)<' /home/faqihhakim/dataDiri/web/fqih/README.md | sort -u
```

Expected: five lines — `FOLLOWERS`, `KONTRIBUSI`, `REPOS`, `STARS`, `STREAK`.

- [ ] **Step 5: Verify the five numbers appear in the spec'd order**

Run:
```bash
grep -oE 'class="num">[0-9a-z]+<' /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: five matches in this exact order — `840`, `33`, `1d`, `27`, `61`. Any deviation means the SVG cell positions don't match the spec.

- [ ] **Step 6: Verify total line count is still ≤ 25 (the SVG stays on one line, so line count is unchanged)**

Run:
```bash
wc -l /home/faqihhakim/dataDiri/web/fqih/README.md
```

Expected: 14 (unchanged from Task 1). Acceptance criterion #1 still holds.

- [ ] **Step 7: Commit the SVG update**

Run:
```bash
git add README.md && git commit -m "docs: add Kontribusi to inline stats SVG (5 stats)

Per user feedback, the inline stats card now leads with Kontribusi
(this year's contribution count, 840) ahead of Stars, Streak, Repos,
and Followers. SVG viewBox widens from 720 to 900 to fit the fifth
cell; cell geometry recomputed for 5 equal cells. Single-line
layout and 56 px height unchanged.

Co-Authored-By: Claude <noreply@anthropic.com>"
```

Expected: one new commit on the current branch, with only `README.md` in the changeset.
