# TODO

Open items after the Google Sites → Quarto migration (2026-08-27).
Live preview: <https://pachalab.github.io/>

## 1. Domain account access and renewal — expiry 2027-10-05

The [registry](https://rdap.verisign.com/com/v1/domain/stephanie-vargas.com)
reports that `stephanie-vargas.com` expires **2027-10-05** (checked
2026-09-28). It is registered at Namecheap (BasicDNS) on Stephanie's account.
If it lapses, the current Google Site goes dark too, so this is independent
of the migration.

- [ ] Confirm access to Stephanie's Namecheap account and that auto-renew is on
- [ ] Optional: Stephanie pushes the domain to Elías's Namecheap account
      (Domain List → Manage → Sharing & Transfer → Change Ownership).
      Free, immediate, keeps the expiry date; no auth code, no 60-day wait
      because the domain stays inside Namecheap. Changing the registrant can
      set a 60-day *outbound* transfer lock — irrelevant unless moving
      registrars soon.

## 2. DNS cut-over (blocked on account access and Stephanie's content review)

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

- [ ] Apply the DNS records above
- [ ] Set `DEPLOY_CNAME=1` in `post-render.sh`, `quarto render`, commit, push
      (this ships `docs/CNAME` and makes GitHub adopt the custom domain)
- [ ] Enable "Enforce HTTPS" in repo settings once the certificate is issued
- [ ] Verify `https://www.stephanie-vargas.com` and the bare apex both serve
- [ ] After ~7 days of overlap, unpublish the Google Site

## 3. Hero image — local design ready for review

The home page is a full-viewport hero. The original teal gradient and heart
outline were placeholders; the design was modelled on
<https://www.alaingdlb.com/>, where the hero carries a striking scientific
image. On 2026-09-28 Elías supplied `images/Heart.jpg` (1884 × 1516).

- [x] Heart microscopy image supplied for use on the homepage.
- [x] Build a local preview: black background, question left, full heart
      section right; stack image above text on phones. Add a Research link.
      Responsive WebP derivatives retain the original JPEG as fallback.
- [ ] Review the visual direction with Elías before publishing.
- [ ] Add an image credit or scientific caption if supplied by Stephanie;
      species and stain identities are currently unspecified.
- [x] Hero question confirmed by Elías (2026-08-28): "How does the immune
      system heal the heart?" Still worth Stephanie's eye when she reviews
      the prose, since it appears under her name.

## 4. Content still missing

- [ ] Google Scholar profile URL → add to the contact block in `about.qmd`
- [ ] LinkedIn URL → same
- [ ] Decide whether an ORCID link belongs there too
- [ ] When the new *Cell Reports* article is published, replace its in-press
      status with the final DOI, volume and article number in `stefi.bib`, and
      confirm whether 2026 remains the publication year

Icons use Bootstrap Icons, e.g.
`<a href="URL"><i class="bi bi-google"></i> Scholar</a>`.

## 5. Stephanie's review

All prose on the site was drafted from `Vargas_CV_July2025.pdf` and checked
against `Vargas_CV_2026.pdf`; it is not her own words. Nothing should be
treated as final until she has read it.

- [ ] Bio on the About page
- [ ] The two "Current work" paragraphs on the research page
- [ ] Confirm the omission of the "References: Eric Olson, Michael Sieweke"
      block that was in the Google Sites draft (referee names do not belong
      on a public page)
- [ ] Confirm the 2023 Circulation Research abstract stays off the
      publication list (matches the CV)

## 6. Organization

- [ ] Get Stephanie's GitHub username
- [ ] Invite her as an Owner of the `pachalab` org (free; lets ownership
      pass to her later without touching Elías's account)

## 7. Preview-site metadata

- [ ] While `pachalab.github.io` is the public site, set Quarto's `site-url`
      to `https://pachalab.github.io` and re-render so `docs/sitemap.xml`
      and `docs/robots.txt` point to the live preview. Switch it to the
      custom domain when the DNS cut-over is ready.

## Not planned

News/blog page, working-papers page, analytics, comments, CI builds.
Add them when there is content that needs them, not before.
