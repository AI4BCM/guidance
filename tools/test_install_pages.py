"""The install pages reach the question box and stay out of the print.

Plug-in answers, 2026-11-01. The owner: "we must ... answer it correctly ONLY on github, so the
chatbox can reach the answers, but keep them out of the pdf". So `install/*.md` is chunked as the
guidance's own text (`source_id` `ai4bcm-guidance`, cited on GitHub), while the PDF and the .md
download, which are both made from `units/` alone, never carry it.

Three things have to hold for that, and each fails here rather than in front of a reader:

1. the build turns every install page into chunks with the guidance's terms and a GitHub citation;
2. the publish round passes `install/` to the build, or the live corpus never sees the pages;
3. no install page sits under `units/` or in the release manifest's unit list (what the .md
   download is assembled from), and no install sentence is in the PDF's text.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

import pytest

import build_chunks as bc

REPO = bc._REPO
INSTALL_DIR = REPO / bc.INSTALL_DIR_NAME
PRINT_PDFS = sorted((REPO / "print").glob("*.pdf"))

# A sentence the PDF does carry, so an empty or garbled text extraction cannot pass check 3.
PRINTED_SENTENCE = "Free public tools never get BCM data."


def install_chunks() -> list[bc.Chunk]:
    tag = bc.release_tag_from(bc.DEFAULT_RELEASES_DIR)
    chunks = bc.build_all(bc.DEFAULT_UNITS_DIR, tag, extra_dirs=(INSTALL_DIR,))
    bc.validate(chunks, tag)
    return [c for c in chunks if c.source_file.startswith("install/")]


def flat(text: str) -> str:
    """Whitespace and line-end hyphenation out, so a wrapped PDF line still matches."""
    text = text.replace("­", "").replace("’", "'")
    text = re.sub(r"-\s*\n\s*", "-", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def sentences(chunk: bc.Chunk) -> list[str]:
    """The chunk's prose sentences of eight words or more: long enough that a match in the PDF
    would mean the page was printed, not that two texts share a phrase."""
    body = chunk.text.partition("\n\n")[2]
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    body = re.sub(r"[`*_|>\[\]]", " ", body)
    out = []
    for s in re.split(r"(?<=[.!?])\s+", body):
        s = s.strip()
        if len(s.split()) >= 8 and not s.lower().startswith(("sources:", "source:")):
            out.append(flat(s))
    return out


def test_every_install_page_is_chunked_as_the_guidance_with_a_github_citation():
    pages = sorted(p.name for p in INSTALL_DIR.glob("*.md"))
    chunks = install_chunks()
    assert sorted({Path(c.source_file).name for c in chunks}) == pages
    tag = bc.release_tag_from(bc.DEFAULT_RELEASES_DIR)
    for c in chunks:
        assert c.source_id == "ai4bcm-guidance", c.id
        assert c.id.startswith("install-"), c.id
        assert c.url.startswith(f"{bc.CITATION_BASE_URL}/{tag}/install/"), c.url


def test_the_publish_round_builds_the_install_pages():
    script = (REPO / "tools" / "publish_knowledge.sh").read_text(encoding="utf-8")
    assert '--source-dir "$APP_ROOT/install"' in script


def test_no_install_page_is_a_unit_or_in_the_release_unit_list():
    import json

    manifest = json.loads(next(bc.DEFAULT_RELEASES_DIR.glob("*.json")).read_text(encoding="utf-8"))
    assert not any(f.startswith("install/") for f in manifest["files"])
    assert not list(bc.DEFAULT_UNITS_DIR.rglob("install*"))


@pytest.mark.skipif(not shutil.which("pdftotext"), reason="pdftotext (poppler-utils) not installed")
@pytest.mark.skipif(not PRINT_PDFS, reason="no PDF under print/")
@pytest.mark.parametrize("pdf", PRINT_PDFS, ids=lambda p: p.name)
def test_the_pdf_carries_no_install_sentence(pdf: Path):
    text = flat(subprocess.run(["pdftotext", str(pdf), "-"], check=True,
                               capture_output=True, text=True).stdout)
    assert flat(PRINTED_SENTENCE) in text, "PDF text extraction failed; the check would prove nothing"
    checked = [(c.id, s) for c in install_chunks() for s in sentences(c)]
    assert len(checked) > 50, f"only {len(checked)} sentences to check"
    printed = [(cid, s) for cid, s in checked if s in text]
    assert printed == [], f"install text found in {pdf.name}: {printed[:5]}"
