# PachaLab → Quarto migration: design

Date: 2026-08-27. Status: draft for review.

## Goal

Replace the Google Site at `www.stephanie-vargas.com` (Stephanie Vargas Aguilar,
postdoc, Olson lab, UT Southwestern) with a git-managed Quarto site on GitHub
Pages, maintained by Elías, deployed with the same manual `quarto render` →
`docs/` → push loop as `prise-lab.github.io`.

## Findings that shape the design

- The *published* Google Site is a single page: banner with her name and one
  field photo. No navigation, no text.
- The *draft* (unpublished, "editors must review" is on) has three pages:
  Home (portrait, placeholder bio "I am .... at UT Southwestern", an unfilled
  two-icon row, "References: Eric Olson, Michael Sieweke"), CV (a bare link),
  Research (Google Scholar link, "Ongoing research projects — Tu grant",
  "Working papers — Published working papers / Bio archives...", and a
  formatted 7-item publication list that matches `stefi.bib` minus the 2023
  Circulation Research abstract).
- So there is no prose to port. Text is authored from the CV
  (`Vargas_CV_July2025.pdf`) and `stefi.bib`.
- Domain `stephanie-vargas.com`: Namecheap, BasicDNS, `www` CNAME →
  `ghs.googlehosted.com`, no apex record, **expires 2026-10-05**.
- Both reference sites are Elías's; PRISE (Quarto 1.9.36, `output-dir: docs`,
  `post-render.sh`, no CI) is the operational template.

## Decisions taken

| Decision | Choice |
|---|---|
| Engine | Quarto website, rendered locally, served from `docs/` on `master` |
| Repo | `eliascis/stephanie-vargas.com`, public (Pages on private repos needs GitHub Pro) |
| Domain | `www.stephanie-vargas.com` canonical; apex A-records redirect to www |
| Maintainer | Elías; Stephanie sends content |
| Look | Standalone identity, not PRISE-branded |
| Spec location | `_notes/specs/` — **not** `docs/`, which Quarto overwrites |

## Site map

```
index.qmd      Home     portrait · 3-paragraph bio · contact/icon row
research.qmd   Research current projects · publications (from stefi.bib)
CV             navbar link → files/vargas-aguilar_cv.pdf (no page)
```

Navbar: left = name/logo → Home, Research; right = CV (external PDF link).
Footer: "© 2026 Stephanie Vargas Aguilar · UT Southwestern Medical Center".
No News, no Working papers page: the draft contains only placeholders; add
pages when there is content (YAGNI).

### Home (`index.qmd`)

- Portrait `images/portrait.jpg` (from `figures/stefi.jpg`), left column;
  text right, stacking on mobile.
- Bio, ~120 words, drafted from the CV: postdoctoral fellow with Eric Olson
  (immunology and heart regeneration, UT Southwestern, 2020–); PhD Humboldt
  University Berlin 2018 with Michael Sieweke (macrophage self-renewal, CIML
  Marseille / MDC Berlin); Diploma Molecular Medicine, Freiburg 2012; AHA
  Career Development Award 2025. Stephanie reviews wording before launch.
- Icon row: email (`stephanie.vargasaguilar@utsouthwestern.edu`), Google
  Scholar, LinkedIn, CV. Icons via Bootstrap Icons (bundled with Quarto), not
  the PNGs in `figures/` — sharper, theme-colourable, no licence question
  (`PikPng.com_google-logo-white-png_*.png` is of unknown provenance).
- No "References" block: referee names belong in applications, not a public
  page. Flag to Stephanie; drop unless she wants it.

### Research (`research.qmd`)

- Intro line with Google Scholar link.
- "Current research": one paragraph each on (a) PD-1/PD-L1 immunosuppression
  in neonatal heart regeneration (Nat Cardiovasc Res 2024; AHA CDA 2025–),
  (b) macrophage self-renewal and ageing (PIWI/Piwil2 line of work from the
  Sieweke lab, presentations 2015–2020). Drafted from CV; Stephanie reviews.
- "Publications": generated from `stefi.bib`.
  - `bibliography: stefi.bib`, `csl: csl/apa-cv.csl` (vendored from the CSL
    repository; sorts by year descending, no in-text numbering).
  - `nocite:` lists the 7 peer-reviewed keys explicitly; the abstract
    `vargasaguilar.etal2023.cr` stays in the bib but is not listed, matching
    the CV.
  - Author bolding is a `perl` substitution in `post-render.sh`, not a Lua
    filter: Quarto rejects `citeproc` as a filter name, and `at: post-render`
    runs before citeproc emits the reference list. Verified 2026-08-27 on
    Quarto 1.9.36 — the substitution matches both "Vargas Aguilar, S." and
    "Aguilar, S. V.", bolds 6 occurrences, and is idempotent (negative
    lookarounds prevent double-wrapping on re-render).
  - DOIs render as links (CSL handles this).

## Repository layout

```
stephanie-vargas.com/
├── _quarto.yml
├── index.qmd  research.qmd  404.qmd
├── stefi.bib
├── csl/apa-cv.csl
├── styles.scss                # theme vars + custom rules
├── images/  portrait.jpg  fieldwork.jpg  favicon.png
├── files/   vargas-aguilar_cv.pdf
├── post-render.sh             # CNAME, .nojekyll, author bolding
├── docs/                      # RENDER OUTPUT — never hand-edit
├── _notes/specs/              # this file; ignored by Quarto (leading _)
├── .gitignore  CLAUDE.md  README.md
```

Migration of existing files: `pachalab/figures/stefi.jpg` → `images/portrait.jpg`;
`Foto_SV.jpg` (719 KB) → resized to ≤1600 px → `images/fieldwork.jpg`;
`files/Vargas_CV_July2025.pdf` → `files/vargas-aguilar_cv.pdf` (stable URL,
mirrors `cisneros_cv.pdf` convention); `stefi.bib` → root. The icon PNGs and
`PachaLab.gsite` are not needed by the new site — **deletion requires
Elías's explicit OK** (his rule); until then they are moved to
`_notes/legacy/` so Quarto ignores them.

## Visual design

- `format.html.theme: [cosmo, styles.scss]`. SCSS variables set the palette;
  custom rules below them.
- Palette derived from the current site's headings: primary teal-blue
  `#2b7a9e`, dark text `#1f2933`, light background, accent for links only.
  Not PRISE's `#0e5c5c`.
- Type: Lato (Google Fonts) for headings — the Google Site's face — system
  sans for body. Fallback stacks specified.
- Home hero: name as `h1` in the primary colour, no full-bleed banner (the
  current banner is a Google Sites default and adds nothing).
- `toc: false` site-wide; `page-layout: article`.

## Deploy and DNS

Loop, verbatim from PRISE: edit → `quarto render` → `git status` (check no
`docs/site_libs/` deletions) → `git add` → commit → push. Never
`quarto publish`.

GitHub: repo → Settings → Pages → Source "Deploy from a branch",
`master` / `/docs`; custom domain `www.stephanie-vargas.com`; enforce HTTPS
once the certificate is issued (minutes to an hour after DNS resolves).

Namecheap Advanced DNS, `stephanie-vargas.com` (Elías performs after the
domain push; each record change is confirmed with him first):

| Type | Host | Value | Action |
|---|---|---|---|
| CNAME | `www` | `ghs.googlehosted.com` | **remove** |
| CNAME | `www` | `eliascis.github.io` | add |
| A | `@` | `185.199.108.153` | add |
| A | `@` | `185.199.109.153` | add |
| A | `@` | `185.199.110.153` | add |
| A | `@` | `185.199.111.153` | add |

Leave any Google-Sites verification TXT records; they are harmless.

Cut-over order: (1) repo live at `eliascis.github.io/stephanie-vargas.com`
and checked; (2) DNS switched; (3) verify `https://www.stephanie-vargas.com`
and `https://stephanie-vargas.com` both serve the new site; (4) leave the
Google Site published for 7 days as fallback, then unpublish.

## Error handling / guardrails

Carried over from PRISE `CLAUDE.md`: `docs/` is render-owned; after render
verify `git status` shows no `site_libs` deletions and that the changed
`docs/*.html` actually contains the edit; LF line endings; `.gitignore`
covers `/.quarto/`, `/_site/`, `.DS_Store`.

Failure modes specific to this site: a broken `stefi.bib` entry aborts the
whole render with a citeproc error — fix the bib, don't work around it in
the qmd. If the CSL is missing, Quarto silently falls back to Chicago
(alphabetical, wrong order): the verification step below catches this.

## Verification (before every "done" claim)

1. `quarto render` exits 0.
2. `docs/index.html`, `docs/research.html`, `docs/404.html`, `docs/CNAME`
   (content `www.stephanie-vargas.com`), `docs/.nojekyll` exist.
3. `grep -c 'class="csl-entry"' docs/research.html` = 7 (the 2023 abstract is
   excluded); the first `doi.org` occurrence is `10.1038/s44161-024-00447-7`
   (2024 entry first ⇒ CSL sort is in effect); `grep -o '<strong>' ` count = 6.
4. `docs/files/vargas-aguilar_cv.pdf` present; PDF link on the page is
   relative and resolves.
5. `quarto preview` visual check at desktop and 390 px width.
6. After DNS: `curl -sI https://www.stephanie-vargas.com | head -1` → 200;
   apex → 301 to www; certificate valid.

## Inputs still needed

- Google Scholar profile URL (the editor hides hrefs).
- LinkedIn URL.
- Stephanie's sign-off on the bio and research paragraphs, and on dropping
  the "References" block.
- Domain push from Stephanie's Namecheap account to Elías's; auto-renew on.
- Whether to rename the local folder `patchalab/` → `stephanie-vargas.com/`
  to match the repo (recommended; the current name is also misspelled).

## Out of scope

News/blog, working-papers page, Stephanie editing the site herself, CI
builds, analytics, comments.
