"""The chunk-id citation contract: the reserved ids, the document, and the real corpus.

kb-move ticket 07 (2026-09-10). `KoGerner/workflow-design`'s `run-bia.yaml` cites chunk ids
minted here. The two used to share a working tree; they no longer do, so the guarantee has to
be a build-time refusal instead of a coincidence. `CITATION-CONTRACT.md` states it in prose and
`build_chunks.RESERVED_CHUNK_IDS` states it in code — these tests fail when they disagree, and
when a real build stops producing one of the reserved ids.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

import build_chunks as bc


REPO = Path(__file__).resolve().parent.parent
CONTRACT = REPO / "CITATION-CONTRACT.md"

# The citations in run-bia.yaml at 26880b5, read out of that file on 2026-09-10. Copied rather
# than imported: the citing file is in another repository and is not on this box's test path.
# If it grows a citation, this list and RESERVED_CHUNK_IDS both have to move — which is the
# contract's "open an issue naming the citing file" step, done deliberately.
RUN_BIA_CITES = frozenset({
    "prompts-bia",
    "prompts-review",
    "stages-analysis-level",
    "stages-analysis-method",
    "stages-analysis-minimum-controls",
    "stages-analysis-typical-ai-uses",
    "stages-design-method",
    "stages-design-minimum-controls",
    "stages-design-typical-ai-uses",
})


def test_the_reserved_set_is_the_documented_one():
    """The prose and the constant are the same fact twice; neither may drift alone."""
    text = CONTRACT.read_text(encoding="utf-8")
    stages = re.search(r"For each of (.+?):", text, re.S).group(1)
    stage_names = re.findall(r"`(\w+)`", stages)
    sections = re.findall(r"^stages-<stage>-(\S+)$", text, re.M)
    prompts = set(re.findall(r"`(prompts-[a-z-]+)`", text.split("**Two prompt units")[1]))

    documented = {f"stages-{s}-{sec}" for s in stage_names for sec in sections} | prompts
    assert documented == set(bc.RESERVED_CHUNK_IDS)
    assert len(documented) == 26, documented


def test_every_run_bia_citation_is_reserved():
    """The gap ticket 07 found: 7 of the 9 cited ids were guaranteed, 2 were not."""
    assert RUN_BIA_CITES <= bc.RESERVED_CHUNK_IDS


def _tag() -> str:
    return bc.release_tag_from(bc.DEFAULT_RELEASES_DIR)


def _units_build() -> list:
    """The units-only build — the one that mints every reserved id. No literature needed."""
    return bc.build_all(bc.DEFAULT_UNITS_DIR, _tag())


def test_a_real_build_produces_every_reserved_id():
    built = {c.id for c in _units_build()}
    assert bc.RESERVED_CHUNK_IDS <= built, sorted(bc.RESERVED_CHUNK_IDS - built)


def test_a_missing_reserved_id_fails_the_build_and_says_why():
    """A heading reword must stop the corpus being published, not reach the public silently."""
    chunks = [c for c in _units_build() if c.id != "prompts-bia"]
    with pytest.raises(SystemExit) as exc:
        bc.validate(chunks, _tag())
    assert "prompts-bia" in str(exc.value)
    assert "CITATION-CONTRACT.md" in str(exc.value)


def test_reserved_ids_carry_a_public_url_in_the_index():
    """What the contract promises a consumer: a page URL per reserved id, from the index."""
    urls = {t["id"]: t["url"] for t in bc.build_index(_units_build(), _tag())["topics"]}
    for cid in sorted(bc.RESERVED_CHUNK_IDS):
        assert urls[cid] == f"{bc.PUBLIC_BASE_URL}/{cid}/"
