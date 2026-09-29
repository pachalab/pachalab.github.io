#!/usr/bin/env python3
"""Build compact publication entries from the site's BibTeX source."""

import html
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "stefi.bib"
OUTPUT = ROOT / "docs" / "publications.html"
PLACEHOLDER = re.compile(r'<div id="publication-list-placeholder">\s*</div>')

# Peer-reviewed publications in newest-first order. The 2023 Circulation
# Research conference abstract is deliberately excluded, as on the CV.
PUBLICATION_KEYS = (
    "vargasaguilar.etal.inpress.cr",
    "vargasaguilar.etal2024.ncr",
    "gainullina.etal2023.cr",
    "subramanian.etal2022.ni",
    "aguilar.etal2020.ni",
    "imperatore.etal2017.tej",
    "matcovitchnatan.etal2016.s",
    "dennemaerker.etal2010.bc",
)


def author_name(author):
    family = author.get("family", "")
    given = author.get("given", "")
    initials = " ".join(
        "-".join(f"{name[0]}." for name in part.split("-") if name)
        for part in given.split()
    )
    name = html.escape(f"{family}, {initials}" if initials else family)
    if family == "Vargas Aguilar" or (family == "Aguilar" and given.startswith("Stephanie Vargas")):
        return f"<strong>{name}</strong>"
    return name


def card(item):
    title = html.escape(item["title"])
    doi = item.get("DOI")
    if doi:
        url = "https://doi.org/" + quote(doi, safe="/")
        title = (
            f'<a href="{html.escape(url, quote=True)}" target="_blank" '
            f'rel="noopener noreferrer">{title}</a>'
        )

    authors = item.get("author", [])
    shown = ", ".join(author_name(author) for author in authors[:7])
    if len(authors) > 7:
        shown += ", et al."

    year = item["issued"]["date-parts"][0][0]
    journal = html.escape(item["container-title"])
    status = item.get("status")
    volume = html.escape(item.get("volume", ""))
    issue = html.escape(item.get("issue", ""))
    pages = html.escape(item.get("page", "")).replace("-", "–")
    detail = f"{journal}, {html.escape(status)}" if status else journal
    if volume:
        detail += f", {volume}"
        if issue:
            detail += f"({issue})"
    if pages:
        detail += f": {pages}"

    return (
        f'<li class="publication-card" id="ref-{html.escape(item["id"], quote=True)}">\n'
        f'  <h2 class="publication-title">{title}</h2>\n'
        f'  <p class="publication-authors">{shown}</p>\n'
        f'  <p class="publication-meta">{year} <span aria-hidden="true">·</span> {detail}</p>\n'
        "</li>"
    )


def main():
    result = subprocess.run(
        ["quarto", "pandoc", str(BIB), "-f", "bibtex", "-t", "csljson"],
        check=True,
        capture_output=True,
        text=True,
    )
    entries = {item["id"]: item for item in json.loads(result.stdout)}
    missing = set(PUBLICATION_KEYS) - entries.keys()
    if missing:
        raise ValueError(f"Publication keys missing from {BIB}: {sorted(missing)}")

    markup = '<ol class="publication-list">\n'
    markup += "\n".join(card(entries[key]) for key in PUBLICATION_KEYS)
    markup += "\n</ol>\n"
    page = OUTPUT.read_text(encoding="utf-8")
    page, count = PLACEHOLDER.subn(lambda _: markup, page)
    if count != 1:
        raise ValueError(f"Expected one publication placeholder in {OUTPUT}")
    OUTPUT.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main()
