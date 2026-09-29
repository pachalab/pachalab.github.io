#!/bin/bash
set -euo pipefail
# The former citeproc list was patched here to bold Stephanie's name. The
# BibTeX-based publication card generator now marks it up after rendering.
# Quarto cannot do this with a Lua filter (citeproc is not addressable as a
# filter, and `at: post-render` runs before the reference list exists).
# Custom domain. DNS points at GitHub Pages; ship the CNAME on every render
# so GitHub Pages keeps www.stephanie-vargas.com as the canonical address.
DEPLOY_CNAME="${DEPLOY_CNAME:-1}"
python3 scripts/build_publications.py
if [ "$DEPLOY_CNAME" = "1" ]; then
  cp _CNAME docs/CNAME
fi

# Former citeproc repair, retained for reference:
# perl -pi -e 's{(?<!<strong>)(Vargas Aguilar, S\.(?! V\.)|Aguilar, S\. V\.)(?!</strong>)}{<strong>$1</strong>}g' docs/research.html
