#!/bin/bash
set -euo pipefail
# The former citeproc list was patched here to bold Stephanie's name. The
# BibTeX-based publication card generator now marks it up after rendering.
# Quarto cannot do this with a Lua filter (citeproc is not addressable as a
# filter, and `at: post-render` runs before the reference list exists).
# Custom domain. The domain still points at Google Sites, so deploying a
# CNAME would set the Pages custom domain and break the
# pachalab.github.io preview. At DNS cut-over, set DEPLOY_CNAME=1
# here (or export it) and the domain file ships with the next render.
DEPLOY_CNAME="${DEPLOY_CNAME:-0}"
python3 scripts/build_publications.py
if [ "$DEPLOY_CNAME" = "1" ]; then
  cp _CNAME docs/CNAME
fi

# Former citeproc repair, retained for reference:
# perl -pi -e 's{(?<!<strong>)(Vargas Aguilar, S\.(?! V\.)|Aguilar, S\. V\.)(?!</strong>)}{<strong>$1</strong>}g' docs/research.html
