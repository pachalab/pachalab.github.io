# PachaLab → Quarto Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace Stephanie Vargas Aguilar's Google Site with a Quarto site in git, built locally and hosted on GitHub Pages under `eliascis`.

**Architecture:** Quarto website rendered to `docs/` on `master`, served by GitHub Pages, deployed by pushing (no CI). Two content pages plus a CV PDF link. The publication list is generated from `stefi.bib` by citeproc; author bolding happens in `post-render.sh` after render.

**Tech Stack:** Quarto 1.9.36, Bootstrap/cosmo + SCSS, citeproc + APA-CV CSL, GitHub Pages, Namecheap DNS.

**Spec:** `_notes/specs/2026-08-27-quarto-migration-design.md`

## Global Constraints

- Output directory is `docs/`; it is render-owned. Never hand-edit, never `quarto publish`.
- Branch is `master`. Commit after each task. Never push without being asked.
- No AI-authorship trailers in commit messages.
- Site URL: `https://www.stephanie-vargas.com`. CNAME file content: `www.stephanie-vargas.com`.
- Contact: `stephanie.vargasaguilar@utsouthwestern.edu`.
- Primary colour `#2b7a9e`; body text `#1f2933`. Headings in Lato.
- All bio/research prose is a draft for Stephanie's sign-off; do not present it as final.
- DNS cut-over is OUT OF SCOPE for this plan — it waits on the domain push.

---

### Task 1: Quarto scaffold that renders

**Files:**
- Create: `_quarto.yml`, `post-render.sh`, `index.qmd`, `.gitignore` (modify)
- Move: `pachalab/stefi.bib` → `stefi.bib`; `pachalab/figures/stefi.jpg` → `images/portrait.jpg`; `pachalab/figures/Foto_SV.jpg` → `images/fieldwork.jpg` (resized to 1200 px); `pachalab/files/Vargas_CV_July2025.pdf` → `files/vargas-aguilar_cv.pdf`
- Move to legacy (no deletion without Elías's OK): remaining `pachalab/**` → `_notes/legacy/`

**Interfaces:**
- Produces: `_quarto.yml` with `output-dir: docs`, navbar entries Home/Research/CV; `post-render.sh` writing `docs/CNAME` + `docs/.nojekyll`.

- [ ] **Step 1: Create directories and move assets**

```bash
mkdir -p images files csl _notes/legacy
git mv pachalab/stefi.bib stefi.bib
cp pachalab/figures/stefi.jpg images/portrait.jpg
sips -Z 1200 pachalab/figures/Foto_SV.jpg --out images/fieldwork.jpg
cp "pachalab/files/Vargas_CV_July2025.pdf" files/vargas-aguilar_cv.pdf
mv pachalab _notes/legacy/pachalab
```

- [ ] **Step 2: Write `_quarto.yml`**

```yaml
project:
  type: website
  output-dir: docs
  post-render: post-render.sh
  resources:
    - CNAME
    - .nojekyll
    - files/

website:
  title: "Stephanie Vargas Aguilar"
  description: "Postdoctoral fellow, Department of Molecular Biology, UT Southwestern Medical Center — immunology and heart regeneration."
  site-url: https://www.stephanie-vargas.com
  favicon: images/favicon.png
  navbar:
    background: light
    foreground: "#1f2933"
    left:
      - href: index.qmd
        text: Home
      - href: research.qmd
        text: Research
    right:
      - href: files/vargas-aguilar_cv.pdf
        text: CV
        target: _blank
  page-footer:
    center: "© 2026 Stephanie Vargas Aguilar · UT Southwestern Medical Center"

format:
  html:
    theme: [cosmo, styles.scss]
    toc: false
    page-layout: article
    link-external-newwindow: true
```

- [ ] **Step 3: Write `post-render.sh` and make it executable**

```bash
#!/bin/bash
set -euo pipefail
touch docs/.nojekyll
echo www.stephanie-vargas.com > docs/CNAME
# Bold the site owner in citeproc reference lists. Quarto cannot do this with a
# Lua filter (citeproc is not addressable as a filter, and at: post-render runs
# before the reference list exists), so patch the rendered HTML. The negative
# lookarounds make repeated runs idempotent.
if [ -f docs/research.html ]; then
  perl -pi -e 's{(?<!<strong>)(Vargas Aguilar, S\.(?! V\.)|Aguilar, S\. V\.)(?!</strong>)}{<strong>$1</strong>}g' docs/research.html
fi
```

- [ ] **Step 4: Write a minimal `index.qmd` and `styles.scss` so the render has input**

```markdown
---
title: ""
---

# Stephanie Vargas Aguilar

Placeholder — replaced in Task 2.
```

```scss
/*-- scss:defaults --*/
$primary: #2b7a9e;
$body-color: #1f2933;
```

- [ ] **Step 5: Render and verify the scaffold**

Run: `quarto render`
Expected: exit 0; `docs/index.html`, `docs/CNAME` (content `www.stephanie-vargas.com`), `docs/.nojekyll` all exist.

```bash
quarto render && test -f docs/index.html && cat docs/CNAME && test -f docs/.nojekyll && echo SCAFFOLD_OK
```

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "Scaffold Quarto site; move assets out of pachalab/"
```

---

### Task 2: Home page

**Files:**
- Modify: `index.qmd`
- Uses: `images/portrait.jpg`, `files/vargas-aguilar_cv.pdf`

**Interfaces:**
- Consumes: `_quarto.yml` navbar and theme from Task 1.
- Produces: CSS classes `.profile-grid`, `.profile-photo`, `.contact-row` consumed by Task 4's SCSS.

- [ ] **Step 1: Write `index.qmd`**

Bio drafted from `_notes/legacy/pachalab/files/…cv.pdf` (education, positions, AHA award). Icon row uses Bootstrap Icons, which ship with Quarto's Bootstrap build — no external CSS.

```markdown
---
title: ""
pagetitle: "Stephanie Vargas Aguilar"
---

::: {.profile-grid}
![](images/portrait.jpg){.profile-photo fig-alt="Stephanie Vargas Aguilar"}

::: {.profile-text}
# Stephanie Vargas Aguilar {.name-heading}

Postdoctoral fellow, Department of Molecular Biology,
UT Southwestern Medical Center

I study how the immune system shapes the regenerating heart. In the
laboratory of Eric Olson I work on the PD-1/PD-L1 pathway and the
immunosuppressive environment that newborn hearts require in order to
regenerate after injury — work supported since 2025 by an American Heart
Association Career Development Award.

Before Dallas I completed my PhD with Michael Sieweke at the Centre
d'Immunologie de Marseille-Luminy and the Max Delbrück Center in Berlin,
on the molecular mechanisms that let tissue-resident macrophages renew
themselves, and a Diploma in Molecular Medicine at the University of
Freiburg.

::: {.contact-row}
[{{< bi envelope >}} Email](mailto:stephanie.vargasaguilar@utsouthwestern.edu)
[{{< bi file-earmark-person >}} CV](files/vargas-aguilar_cv.pdf)
:::
:::
:::
```

- [ ] **Step 2: Render and verify**

Run: `quarto render index.qmd`
Expected: exit 0, and the page contains the portrait, the mailto link, and the CV link.

```bash
quarto render && grep -q 'images/portrait.jpg' docs/index.html \
  && grep -q 'mailto:stephanie.vargasaguilar@utsouthwestern.edu' docs/index.html \
  && grep -q 'files/vargas-aguilar_cv.pdf' docs/index.html && echo HOME_OK
```

- [ ] **Step 3: Commit**

```bash
git add index.qmd docs
git commit -m "Add home page with bio and contact row"
```

---

### Task 3: Research page and bibliography

**Files:**
- Create: `research.qmd`, `csl/apa-cv.csl`
- Uses: `stefi.bib`

**Interfaces:**
- Consumes: `post-render.sh` bolding from Task 1.
- Produces: `docs/research.html` with exactly 7 `csl-entry` divs.

- [ ] **Step 1: Vendor the CSL style**

```bash
curl -sSf -o csl/apa-cv.csl https://raw.githubusercontent.com/citation-style-language/styles/master/apa-cv.csl
```

- [ ] **Step 2: Write `research.qmd`**

The `nocite` list names the 7 peer-reviewed keys; `vargasaguilar.etal2023.cr` (a
conference abstract) stays in the bib but off the page, matching the CV.

```markdown
---
title: "Research"
bibliography: stefi.bib
csl: csl/apa-cv.csl
nocite: |
  @vargasaguilar.etal2024.ncr, @gainullina.etal2023.cr, @subramanian.etal2022.ni,
  @aguilar.etal2020.ni, @imperatore.etal2017.tej, @matcovitchnatan.etal2016.s,
  @dennemaerker.etal2010.bc
---

## Current work

**Immune control of heart regeneration.** Newborn mammalian hearts can
regenerate after injury; adult hearts cannot. My work shows that the
PD-1/PD-L1 checkpoint pathway maintains the immunosuppressive environment
this regenerative window depends on, and asks how T cell populations are
recruited and licensed during neonatal cardiac injury.

**Self-renewal and ageing of tissue-resident macrophages.** During my PhD I
characterised a short isoform of Piwil2 required for the self-renewal of
murine macrophages, and contributed to work on how alveolar macrophages
retain their epigenetic identity through long-term expansion and how
microglia mature in the developing brain.

## Publications

::: {#refs}
:::
```

- [ ] **Step 3: Render and verify count, order, and bolding**

Run: `quarto render`
Expected: 7 entries; newest first; 6 bolded author occurrences.

```bash
quarto render
echo "entries: $(grep -c 'class="csl-entry"' docs/research.html)"   # expect 7
echo "first:   $(grep -o 'doi.org/[^\"<]*' docs/research.html | head -1)"  # expect .../s44161-024-00447-7
echo "bold:    $(grep -o '<strong>' docs/research.html | wc -l | tr -d ' ')"  # expect 6
```

- [ ] **Step 4: Verify idempotence of the bolding**

Run `quarto render` a second time and confirm the bold count is still 6, not 12.

- [ ] **Step 5: Commit**

```bash
git add research.qmd csl docs
git commit -m "Add research page with bibliography generated from stefi.bib"
```

---

### Task 4: Visual identity

**Files:**
- Modify: `styles.scss`
- Create: `images/favicon.png`

**Interfaces:**
- Consumes: classes emitted by Tasks 2–3 (`.profile-grid`, `.profile-photo`, `.profile-text`, `.contact-row`, `.name-heading`, `.csl-entry`).

- [ ] **Step 1: Generate the favicon from the heart icon**

```bash
sips -Z 180 _notes/legacy/pachalab/figures/heart-icon-01.png --out images/favicon.png
```

- [ ] **Step 2: Write `styles.scss`**

```scss
/*-- scss:defaults --*/
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

$primary:      #2b7a9e;
$body-color:   #1f2933;
$link-color:   #2b7a9e;
$headings-font-family: Lato, -apple-system, "Segoe UI", sans-serif;
$font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
$navbar-bg: #ffffff;

/*-- scss:rules --*/
.name-heading {
  color: $primary;
  font-weight: 300;
  letter-spacing: 0.5px;
  margin-top: 0;
}

.profile-grid {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 2.5rem;
  align-items: start;
  margin-top: 1.5rem;
}

.profile-photo {
  width: 100%;
  border-radius: 8px;
  display: block;
}

.profile-text p { line-height: 1.65; }

.contact-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  margin-top: 1.75rem;
}

.contact-row a {
  text-decoration: none;
  font-weight: 700;
}

.contact-row a:hover { text-decoration: underline; }

.csl-entry {
  margin-bottom: 1.1rem;
  padding-left: 1.4rem;
  text-indent: -1.4rem;
  line-height: 1.55;
}

@media (max-width: 700px) {
  .profile-grid { grid-template-columns: 1fr; gap: 1.5rem; }
  .profile-photo { max-width: 220px; }
}
```

- [ ] **Step 3: Render and inspect at both widths**

Run: `quarto render`, then open `docs/index.html`; check desktop and a 390 px viewport.

- [ ] **Step 4: Commit**

```bash
git add styles.scss images/favicon.png docs
git commit -m "Add standalone visual identity: palette, Lato headings, responsive profile layout"
```

---

### Task 5: 404 page and repository documentation

**Files:**
- Create: `404.qmd`, `README.md`
- Rewrite: `CLAUDE.md`

- [ ] **Step 1: Write `404.qmd`**

```markdown
---
title: "Page not found"
---

That page does not exist. Try the [home page](/) or [research](/research.html).
```

- [ ] **Step 2: Rewrite `CLAUDE.md`** in the PRISE style: deploy loop, `docs/` guardrails (never hand-edit, never `quarto publish`, check `git status` for `site_libs` deletions, verify the rendered HTML contains the change), the bib/CSL/bolding mechanism, and DNS facts.

- [ ] **Step 3: Write `README.md`** — one paragraph on what the repo is, the three-command deploy loop, and a pointer to `CLAUDE.md`.

- [ ] **Step 4: Render, verify, commit**

```bash
quarto render && test -f docs/404.html && echo OK
git add 404.qmd README.md CLAUDE.md docs
git commit -m "Add 404 page and repository documentation"
```

---

### Task 6: GitHub repository and Pages

**Files:** none (remote operations)

- [ ] **Step 1: Create the repository** — ask Elías to confirm before creating, since this is outward-facing.

```bash
gh repo create eliascis/stephanie-vargas.com --public \
  --description "Website of Stephanie Vargas Aguilar" --source=. --remote=origin
```

- [ ] **Step 2: Push `master`**

```bash
git push -u origin master
```

- [ ] **Step 3: Enable Pages from `master` /docs**

```bash
gh api -X POST repos/eliascis/stephanie-vargas.com/pages \
  -f 'source[branch]=master' -f 'source[path]=/docs'
```

- [ ] **Step 4: Verify the site builds on the github.io address**

```bash
curl -sI https://eliascis.github.io/stephanie-vargas.com/ | head -1   # expect 200
```

Do NOT set the custom domain yet — that belongs with the DNS cut-over, which is out of scope here.

---

## Deferred (not in this plan)

Domain push from Stephanie to Elías; Namecheap DNS records; GitHub custom-domain setting and HTTPS; unpublishing the Google Site. Also deferred: Google Scholar and LinkedIn icon links (URLs not yet supplied) and Stephanie's sign-off on the prose.
