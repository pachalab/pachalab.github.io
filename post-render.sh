#!/bin/bash
set -euo pipefail
# Bold the site owner in citeproc reference lists. Quarto cannot do this with a
# Lua filter (citeproc is not addressable as a filter, and `at: post-render`
# runs before the reference list exists), so patch the rendered HTML. The
# negative lookarounds make repeated renders idempotent.
if [ -f docs/research.html ]; then
  perl -pi -e 's{(?<!<strong>)(Vargas Aguilar, S\.(?! V\.)|Aguilar, S\. V\.)(?!</strong>)}{<strong>$1</strong>}g' docs/research.html
fi
