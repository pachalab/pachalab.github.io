#!/bin/bash
set -euo pipefail
# Bold the site owner in citeproc reference lists. Quarto cannot do this with a
# Lua filter (citeproc is not addressable as a filter, and `at: post-render`
# runs before the reference list exists), so patch the rendered HTML. The
# negative lookarounds make repeated renders idempotent.
# Custom domain. The domain still points at Google Sites, so deploying a
# CNAME would set the Pages custom domain and break the
# pachalab.github.io preview. At DNS cut-over, set DEPLOY_CNAME=1
# here (or export it) and the domain file ships with the next render.
DEPLOY_CNAME="${DEPLOY_CNAME:-0}"
if [ "$DEPLOY_CNAME" = "1" ]; then
  cp _CNAME docs/CNAME
fi

if [ -f docs/research.html ]; then
  perl -pi -e 's{(?<!<strong>)(Vargas Aguilar, S\.(?! V\.)|Aguilar, S\. V\.)(?!</strong>)}{<strong>$1</strong>}g' docs/research.html
fi
