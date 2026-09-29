# stephanie-vargas.com

Personal academic website of Stephanie Vargas Aguilar, built with
[Quarto](https://quarto.org) and served by GitHub Pages from `docs/` on
`master`.

```bash
quarto preview     # local development
quarto render      # rebuild docs/
git add -A && git commit -m "..." && git push   # deploy
```

Publications are generated from `stefi.bib` by
`scripts/build_publications.py` during `quarto render`; do not hand-edit the
list or the rendered `docs/publications.html`.
See `CLAUDE.md` for the deploy guardrails and the non-obvious details of
the build.
