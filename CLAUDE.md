# Stephanie Vargas Aguilar — website (Quarto + GitHub Pages)

Personal academic site for Stephanie Vargas Aguilar (postdoctoral fellow,
Olson lab, Department of Molecular Biology, UT Southwestern Medical Center).
Migrated from a Google Site in August 2026. **Manually deployed**: no CI, no
GitHub Actions, no `gh-pages` branch. Every change is rendered locally and
pushed.

Maintained by Elías Cisneros; Stephanie supplies content. All biographical
and research prose on the site is a draft pending her sign-off.

## Local design reference

Elías's reference website, <https://elias-cisneros.com/>, has its source at
`/Users/eliascis/Dropbox/omagua/web/eliascis.github.io`. Inspect that checkout
directly when comparing its infrastructure or design. Its Jekyll/Minimal
Mistakes sidebar uses `author.links` in `_config.yml` and
`_includes/author-profile.html`. Treat it as a visual reference and adapt
the pattern to this site's Quarto structure; its implementation and build
instructions do not apply here.

## Deploy workflow (do not deviate)

```
1. Edit .qmd / _quarto.yml / styles.scss / images/   (sources)
2. quarto render                                     (rebuilds all of docs/)
3. git status   # sanity check — see guardrails
4. git add <changed files>
5. git commit -m "..."
6. git push                                          (this is what deploys)
```

## Guardrails

1. **Never run `quarto publish`.** This site is served from `docs/` on
   `master`, not from a `gh-pages` branch. Always plain `quarto render`.
2. **Never hand-edit anything in `docs/`.** It is fully render-owned.
   `docs/site_libs/` holds Bootstrap CSS/JS and Bootstrap Icons; every page
   references them by relative path. If it goes missing the site loses all
   styling.
3. **After rendering, check `git status`.** If `docs/site_libs/` loses a
   file the rendered pages still reference (`bootstrap.min.js`,
   `bootstrap-icons.css`, or the single hashed `bootstrap-<hash>.min.css`
   named in `docs/*.html`), the render did not complete — recover with
   `git checkout -- docs/site_libs/` and re-render; do not commit that
   state. Deletion of *stale* hashed `bootstrap-<hash>.min.css` copies that
   no page references is normal: Quarto renames the hash whenever
   `styles.scss` changes and may remove the old copies (observed
   2026-10-02 with Quarto 1.9.36). Check with
   `grep -oh 'bootstrap-[0-9a-f]*\.min\.css' docs/*.html | sort -u`.
4. **Verify the rendered HTML contains your change** before committing, e.g.
   after editing `research.qmd`, grep `docs/research.html` for new text.
5. **LF line endings**, not CRLF.

## How the pieces fit

- `index.qmd` — a full-viewport hero: name, role, research question, subtitle,
  and Stephanie's heart microscopy image. The accepted version centers
  the text over the enlarged image, with a dark gradient for contrast.
  Portrait screens crop more of the image's sides. Elías approved this
  version and its merge into `master` for publication on 2026-09-28.
  It was developed on `experiment/centered-heart-hero`.
  The previously approved version placed the text and complete section
  side by side, stacking on phones. It remains preserved in commit
  `8564a22`. Elías approved the original treatment and enlarged
  name/affiliation earlier on 2026-09-28 (see `TODO.md` item 3).
  It must not contain a markdown heading: Quarto's section wrapper absorbs
  the enclosing div's classes and the heading colour then leaks onto every
  paragraph inside, and a leading `h1` is hoisted into Quarto's title-block
  header, out of the layout. Use spans with classes, as it does now.
- `about.qmd` — a six-paragraph first-person bio beside Stephanie's portrait,
  supplied on 2026-10-02 (opening question, the regenerative-window framing,
  current research in the Olson lab, training, methods and funding, and
  international outlook). It replaced the "In Progress" placeholder; the
  earlier draft bio remains in Git history. `contact.qmd` holds the email
  address; the CV remains available from the navbar.
- Hero mechanics live in `styles.scss` under `body:has(.hero)`: a flex
  layout replaces Quarto's article grid and its empty 60px bottom row;
  the empty title block and footer are suppressed. The home page fills
  one screen when the content fits, and scrolls naturally on short screens
  or with enlarged text.
- Keep the index homepage free of a contact/profile column; it uses the
  centered hero layout. Elías clarified this after the sidebar preview.
- The native Quarto sidebar `contact-profiles` is defined in `_quarto.yml`
  and enabled explicitly in About, Research, Publications, and Contact.
  The index sets `sidebar: false`. Keep sidebar destinations in sync with
  `contact.qmd`. On small screens, Quarto exposes the links through a
  collapsible navigation bar.
  Its first, unlinked text item is Stephanie's name, followed by the Olson
  Lab, email, and professional profiles. Contact is omitted from the
  top navbar; its existing page remains available directly.
- `images/Heart.jpg` is the supplied 1884 × 1516 original. The hero uses
  responsive WebP derivatives, with the JPEG as fallback. Regenerate with:
  `cwebp -q 90 -sharp_yuv -m 6 images/Heart.jpg -o images/heart.webp` and
  `cwebp -q 90 -sharp_yuv -m 6 -resize 960 0 images/Heart.jpg -o images/heart-960.webp`.
  The previous side-by-side version displayed the image intact, with no
  tint, overlay, or animation. The accepted centered layout scales it to 88%
  of the hero width on wide screens, or 88% of its height on portrait
  screens, to reduce cropping. It uses a CSS shading layer; the source
  image files remain unchanged.
  Species, stains, and a scientific caption have not been supplied.
- Layout uses two custom properties: `--measure` (940px) is the alignment
  grid that the title, headings and photo column share; `--text-measure`
  (720px) is the reading width. Prose gets `padding-right` rather than a
  narrower box, so the left edge stays in register with the headings.
  Target `section > p`, not `main > p` — Quarto wraps content in
  `<section class="level2">`.
- `research.qmd` — a one-paragraph current-work narrative (neonatal heart,
  PD-1/PD-L1, γδT17 cells, IL-17A) supplied by Elías on 2026-09-29, followed
  by research funding; separate from the publication list and still pending
  Stephanie's review. Its former opening paragraph (the regenerative-window
  question) moved to `about.qmd` on 2026-10-02 to avoid repetition; more
  research text is planned.
- `publications.qmd` — eight compact publication entries generated from
  `stefi.bib` by `scripts/build_publications.py` after rendering. The
  title is a modest linked heading, followed by an author line and a line
  for the year, journal and publication details. These headings override
  the global uppercase section-heading style in `styles.scss`. The
  explicit key list retains newest-first order and excludes the ninth bib
  entry, `vargasaguilar.etal2023.cr`, a conference abstract, matching the CV.
  List every author except on the 2023 *Cell Reports* and 2020 *Nature
  Immunology* entries, which retain seven authors followed by "et al."
  Quarto renders a placeholder, which the post-render script replaces in
  `docs/publications.html`. The in-press article's year and status come from
  the BibTeX record.
- `files/vargas-aguilar_cv.pdf` is the public copy of Stephanie's September
  2026 CV. Quarto copies it to `docs/files/` during render; keep the stable
  URL when replacing the PDF.
- `post-render.sh` — builds publication cards and handles the custom-domain
  CNAME switch. The former citeproc bolding repair is retained there as a
  comment; the publication generator now marks up Stephanie's name.
- `.nojekyll` lives at the repo root and reaches `docs/` as a site resource.
  The custom domain is held back: it lives in `_CNAME` (underscore-prefixed
  so Quarto ignores it) and is copied to `docs/CNAME` by `post-render.sh`
  **only** when `DEPLOY_CNAME=1`. Reason: GitHub reads `docs/CNAME` on every
  build and sets the Pages custom domain from it; while DNS still points at
  Google Sites that makes the pachalab.github.io preview
  301-redirect to a domain serving the old site. Resource negation
  (`"!CNAME"`) does not work for root-level files — only for directories.
- Icons are Bootstrap Icons (`<i class="bi bi-envelope">`), whose CSS ships
  with Quarto's Bootstrap bundle. `{{< bi … >}}` is **not** a built-in
  shortcode and renders as literal text.
- The site icon is `images/favicon.svg`, a two-layer trace (red silhouette +
  white interior) of the anatomical-heart icon from the Google Site, with the
  original's grey blocks and white background removed. `.ico` and
  apple-touch-icon are rendered from the same vector. Source and the rejected
  candidates are in `_notes/favicon-options/`; `heart-cut.png` there is the
  cleaned raster the trace came from.
- Icon `<link>` tags live in `_includes/head-icons.html`. Quarto's `favicon:`
  key is deliberately unset — it emits a second `rel="icon"`, and two
  competing ones make the browser's choice ambiguous.
- `images/` is listed under `project.resources` because the icon files are
  referenced only from raw header HTML, which Quarto does not scan.
- `images/publication-review/` holds local figure candidates and source notes
  for review. It is ignored by Git and excluded from Quarto resources; do not
  add its contents to the site without checking figure reuse permissions.
- `project.render` is limited to `"*.qmd"`. Without it Quarto renders
  `TODO.md` into a public `docs/TODO.html`.
- `_notes/` holds the design spec and implementation plan. `z_old/pachalab/`
  holds the original Google Site assets and `.gsite` Drive pointer; it is
  excluded from the build. Keep it until Elías says it can go.
- `_notes/banner-options/` holds downloaded banner candidates, source
  credits, and an interactive `preview.html` gallery. Keep this design study
  local until an image and placement are chosen. `_notes/**` is explicitly
  excluded from `project.resources`; Quarto otherwise copies referenced
  image assets even when the folder name starts with an underscore.

## Verification before claiming a change works

```bash
quarto render
grep -c 'class="publication-entry"' docs/publications.html          # 8
grep -o 'doi.org/[^"<]*' docs/publications.html | head -1            # …s44161-024-00447-7
grep -o '<strong>\(Vargas \)\?Aguilar, S[^<]*</strong>' docs/publications.html | wc -l
cmp _CNAME docs/CNAME                                                 # after the custom-domain cut-over
```

## Hosting and DNS

- Repo: `pachalab/pachalab.github.io` (org-owned site repo, like `prise-lab`);
  GitHub Pages from `master` `/docs`. Canonical domain:
  <https://www.stephanie-vargas.com/>.
- Local checkout: `/Users/eliascis/Dropbox/omagua/web/pachalab`.
- Domain `stephanie-vargas.com` is registered at **Namecheap** (BasicDNS).
  On 2026-09-29, Stephanie granted `eliascis` domain-manager access.
  Auto-renew is on; the current registration expires **2027-10-05**.
  `www` is a CNAME to `pachalab.github.io`, and the apex has the four GitHub
  Pages A records (185.199.108–111.153). Keep the Google Sites verification
  TXT record and the existing mail settings.
- `post-render.sh` now includes `docs/CNAME` by default on each render. GitHub
  Pages adopted `www.stephanie-vargas.com` from commit `633717e`.
- GitHub approved a certificate for both `www` and the apex on 2026-09-29;
  Enforce HTTPS is on. The `www` homepage serves over HTTPS, and the apex
  redirects to it. The old Google Site remains at its Google Sites URL;
  unpublish it after about a week of overlap (its editor URL and owner account
  are recorded in the private migration notes, not here).
- Web-filter categorization: on 2026-09-30 UTSW's network blocked the site as
  "uncategorized". Vendor databases are independent, so on 2026-10-01 Elías
  submitted recategorization requests (Education / Reference) to FortiGuard,
  Broadcom/Symantec, Trend Micro, BrightCloud and Cloudflare; Skyhigh already
  carried UTSW's categories. Palo Alto (currently "Parked") and Cisco Talos
  still need a vendor-account login. Status table and open items: `TODO.md`
  item 9. No site-side setting affects this.
