# TODO

Open items after the Google Sites → Quarto migration (2026-08-27).
Live preview: <https://pachalab.github.io/>

## 1. Domain account access and renewal — expiry 2027-10-05

The [registry](https://rdap.verisign.com/com/v1/domain/stephanie-vargas.com)
reports that `stephanie-vargas.com` expires **2027-10-05** (checked
2026-09-28). It is registered at Namecheap (BasicDNS) on Stephanie's account.
If it lapses, the public custom-domain site goes dark.

- [x] Accept domain-manager access in Elías's Namecheap account; auto-renew is on
- [ ] Optional: Stephanie pushes the domain to Elías's Namecheap account
      (Domain List → Manage → Sharing & Transfer → Change Ownership).
      Free, immediate, keeps the expiry date; no auth code, no 60-day wait
      because the domain stays inside Namecheap. Changing the registrant can
      set a 60-day *outbound* transfer lock — irrelevant unless moving
      registrars soon.

## 2. DNS cut-over and HTTPS

Namecheap → `stephanie-vargas.com` → Advanced DNS:

| Type | Host | Value | Action |
|---|---|---|---|
| CNAME | `www` | `ghs.googlehosted.com` | remove |
| CNAME | `www` | `pachalab.github.io` | add |
| A | `@` | `185.199.108.153` | add |
| A | `@` | `185.199.109.153` | add |
| A | `@` | `185.199.110.153` | add |
| A | `@` | `185.199.111.153` | add |

Leave any Google-Sites verification TXT records; they are harmless.

- [x] Apply the DNS records above (2026-09-29)
- [x] Set `DEPLOY_CNAME=1` in `post-render.sh`, `quarto render`, commit, push
      (this ships `docs/CNAME` and makes GitHub adopt the custom domain)
- [x] Enable "Enforce HTTPS" in repo settings after certificate approval
- [x] Verify `https://www.stephanie-vargas.com` serves the site and the bare
      apex redirects to it
- [x] Unpublish the Google Site (2026-09-29); the direct URL now requires
      sign-in for unauthenticated visitors.
- [ ] Confirm removal of the owner-owned `PachaLab` Google Sites file; it still
      opens in Elías's editor account after unpublishing.

## 3. Hero image — approved for publication

The home page is a full-viewport hero. The original teal gradient and heart
outline were placeholders; the design was modelled on
<https://www.alaingdlb.com/>, where the hero carries a striking scientific
image. On 2026-09-28 Elías supplied `images/Heart.jpg` (1884 × 1516).

- [x] Heart microscopy image supplied for use on the homepage.
- [x] Build a local preview: black background, question left, full heart
      section right; stack image above text on phones. Add a Research link.
      Responsive WebP derivatives retain the original JPEG as fallback.
- [x] Elías approved the visual direction and enlarged name/affiliation
      for publication (2026-09-28).
- [ ] Add an image credit or scientific caption if supplied by Stephanie;
      species and stain identities are currently unspecified.
- [x] Hero question confirmed by Elías (2026-08-28): "How does the immune
      system heal the heart?" Still worth Stephanie's eye when she reviews
      the prose, since it appears under her name.

### Centered background version — accepted (2026-09-28)

- [x] Preserve the previous published design in commit `8564a22` before editing.
- [x] Build a local alternative on `experiment/centered-heart-hero`:
      centered text over an enlarged heart image, with shading for contrast.
- [x] Elías accepted this version and authorized merging into `master` and
      pushing for publication (2026-09-28).

## 4. Content still missing

- [ ] Google Scholar profile URL → add to `contact.qmd`
- [ ] LinkedIn URL → same
- [ ] Decide whether an ORCID link belongs there too
- [ ] When the new *Cell Reports* article is published, replace its in-press
      status with the final DOI, volume and article number in `stefi.bib`, and
      confirm whether 2026 remains the publication year

Icons use Bootstrap Icons, e.g.
`<a href="URL"><i class="bi bi-google"></i> Scholar</a>`.

## 5. Stephanie's review

The site's draft prose was based on `Vargas_CV_July2025.pdf` and checked
against `Vargas_CV_2026.pdf`. Elías supplied the current Research-page text on
2026-09-29. Nothing should be treated as final until Stephanie has read it.

- [x] About-page text supplied on 2026-10-02 and published in place of the
      "In Progress" placeholder; it opens with the regenerative-window
      question formerly at the top of the research page.
- [ ] The remaining "Current work" paragraph on the research page (the
      opening paragraph moved to About on 2026-10-02; Elías plans to add
      more research text)
- [ ] The October 2026 CV lists Stephanie as Instructor (2025–present), but
      the site still says "Postdoctoral fellow" in the `index.qmd` hero role,
      the `_quarto.yml` site description, and the `CLAUDE.md` header. Confirm
      the title and update all three together.
- [ ] Decide whether the Freire-Fierro et al. 2026 perspective in *Frontiers
      in Research Metrics and Analytics* (PMID 42528971), listed in the CV
      under "Other scholarly publications", belongs on the publications page
      (`stefi.bib` + key list in `scripts/build_publications.py`).
- [ ] Confirm the omission of the "References: Eric Olson, Michael Sieweke"
      block that was in the Google Sites draft (referee names do not belong
      on a public page)
- [ ] Confirm the 2023 Circulation Research abstract stays off the
      publication list (matches the CV)

## 6. Organization

- [ ] Get Stephanie's GitHub username
- [ ] Invite her as an Owner of the `pachalab` org (free; lets ownership
      pass to her later without touching Elías's account)

## 7. Site metadata

- [x] Quarto's `site-url`, `docs/sitemap.xml`, and `docs/robots.txt` use
      `https://www.stephanie-vargas.com` after the DNS cut-over.

## 8. Design and search visibility

- [ ] Harmonize font sizes across all pages, including headings, body text,
      navigation, and the sidebar on desktop and mobile screens.
- [ ] Add banners to the content tabs (About, Research, Publications, and
      Contact); select images and crops from `_notes/banner-options/`, confirm
      credits and reuse rights, and check desktop and mobile layouts.
- [ ] Optimize the site for Google Search: review page titles and descriptions,
      heading structure, internal links, image alt text, canonical URLs, and
      sitemap indexing in Google Search Console.

## 9. Web-filter categorization (UTSW block, 2026-09-30)

On 2026-09-30 UTSW's campus network blocked the site as an "uncategorized"
website; UTSW IT suggested the categories Professional Networking and Job
Search, and Stephanie filed a UTSW service incident. Each filter vendor keeps
its own database, so a UTSW-local fix does not propagate; strict policies of
this kind are typical of hospital and medical-center networks. Nothing on the
site or GitHub side assigns a category. Requests submitted 2026-10-01 by Elías
(contact: his UT Dallas address; requested Education or Reference/Research,
Personal Sites as fallback). Expected turnaround one to seven days.

| Vendor | Status 2026-10-01 | Action |
|---|---|---|
| Skyhigh/Trellix (ex-McAfee) | Job Search + Professional Networking, Minimal Risk, DB dated 2026-10-01 | None; matches UTSW IT's wording, so UTSW's own ticket applied |
| FortiGuard | Not Rated | Submitted (Education) |
| Broadcom/Symantec WebPulse | Not rated | Submitted (Education, Personal Sites) |
| Trend Micro | Untested, Newly Observed Domain | Submitted (Safe, Education); needs e-mail confirmation click |
| BrightCloud/OpenText | Entertainment and Arts (allowed, but wrong) | Submitted (Reference and Research, Educational Institutions) |
| Cloudflare Radar/Gateway | Uncategorized | Submitted (Education, Science) |
| Palo Alto PAN-DB | Parked (stale; strict policies block parked domains) | Open: change requests need a Palo Alto account since 2026-03-15 |
| Cisco Talos (Umbrella, Firepower) | No category, reputation Unknown | Open: needs a Cisco account |
| Zscaler / Check Point / Forcepoint | not checkable | Customer-only lookup / User Center login / lookup host defunct |

- [ ] Click the Trend Micro confirmation link sent to Elías's UT Dallas inbox
- [ ] Create a Palo Alto Networks account and file the PAN-DB change request
      at <https://urlfiltering.paloaltonetworks.com/> (highest priority:
      Palo Alto is the most common hospital firewall)
- [ ] Optionally file the Cisco Talos content-categorization ticket
      (<https://talosintelligence.com/reputation_center/lookup?search=stephanie-vargas.com>)
- [ ] Re-check the vendor lookups about one week after 2026-10-01
- [ ] Tell Stephanie that the UTSW fix does not propagate to other
      institutions and that the remaining vendors are being handled

## Not planned

News/blog page, working-papers page, analytics, comments, CI builds.
Add them when there is content that needs them, not before.
