"""The source registry: nothing enters a served chunk without its licence terms.

AI4BCM guidance improvements ticket 05 (2026-09-10). The audit's R10 table classifies every
candidate source A (open licence, may be included with attribution), B (free to read and
quotable), C (citation only) or D (unverified). Only class A may become chunks; the build
refuses everything else, and refuses a source it has never heard of, so that ticket 08 can
load literature by adding a row rather than by editing the builder.

Runs against temporary directories only — no guidance submodule needed, so it ships public.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import build_chunks as bc


UNIT = """# Test unit

## Method

A body so the section is not empty.
"""

ROW = {
    "id": "test-source",
    "title": "A test source",
    "publisher": "Nobody",
    "edition": "1.0",
    "licence": "CC BY 4.0",
    "licence_class": "A",
    "citation": "Nobody (2026). A test source, {edition}, {source_file}. CC BY 4.0.",
    "paths": ["units/*"],
}


def write_registry(tmp_path: Path, rows: list[dict]) -> Path:
    path = tmp_path / "sources.json"
    path.write_text(json.dumps({"schema": 1, "sources": rows}), encoding="utf-8")
    return path


def write_units(tmp_path: Path, names=("principles.md",)) -> Path:
    units = tmp_path / "units"
    (units / "stages").mkdir(parents=True, exist_ok=True)
    for name in names:
        (units / name).write_text(UNIT, encoding="utf-8")
    return units


def test_a_source_row_missing_a_field_is_refused(tmp_path):
    row = {k: v for k, v in ROW.items() if k != "licence"}
    with pytest.raises(SystemExit) as exc:
        bc.load_sources(write_registry(tmp_path, [row]))
    assert "licence" in str(exc.value)


def test_an_unknown_licence_class_is_refused(tmp_path):
    with pytest.raises(SystemExit) as exc:
        bc.load_sources(write_registry(tmp_path, [{**ROW, "licence_class": "open-ish"}]))
    assert "licence_class" in str(exc.value)


def test_a_file_no_source_claims_cannot_become_a_chunk(tmp_path):
    units = write_units(tmp_path, ("principles.md",))
    registry = bc.load_sources(write_registry(tmp_path, [{**ROW, "paths": ["units/nothing/*"]}]))
    with pytest.raises(SystemExit) as exc:
        bc.build_all(units, "2026.09", registry)
    assert "no registered source" in str(exc.value)
    assert "units/principles.md" in str(exc.value)


@pytest.mark.parametrize("cls", ["A-share-alike", "B", "C", "D"])
def test_a_source_that_is_not_class_a_cannot_become_a_chunk(tmp_path, cls):
    units = write_units(tmp_path)
    registry = bc.load_sources(write_registry(tmp_path, [{**ROW, "licence_class": cls}]))
    with pytest.raises(SystemExit) as exc:
        bc.build_all(units, "2026.09", registry)
    assert "licence class" in str(exc.value)


def test_a_class_a_source_stamps_every_chunk_with_its_terms(tmp_path):
    units = write_units(tmp_path)
    registry = bc.load_sources(write_registry(tmp_path, [ROW]))
    chunks = bc.build_all(units, "2026.09", registry)
    assert chunks
    for chunk in chunks:
        assert chunk.source_id == "test-source"
        assert chunk.source_edition == "1.0"
        assert chunk.licence == "CC BY 4.0"
        assert chunk.citation == (
            "Nobody (2026). A test source, 1.0, units/principles.md. CC BY 4.0."
        )


def test_the_release_sentinel_fills_the_edition_from_the_release_tag(tmp_path):
    units = write_units(tmp_path)
    registry = bc.load_sources(write_registry(tmp_path, [{**ROW, "edition": "@release"}]))
    chunks = bc.build_all(units, "2026.09", registry)
    assert {c.source_edition for c in chunks} == {"2026.09"}


def test_validate_refuses_a_chunk_with_no_licence(tmp_path):
    units = write_units(tmp_path)
    registry = bc.load_sources(write_registry(tmp_path, [ROW]))
    chunks = bc.build_all(units, "2026.09", registry)
    chunks[0].licence = ""
    with pytest.raises(SystemExit) as exc:
        bc.validate(chunks, "2026.09")
    assert "without source terms" in str(exc.value)


def test_the_shipped_registry_covers_the_guidance_units():
    """The registry that ships is loadable and claims the units the server builds from."""
    registry = bc.load_sources(bc.DEFAULT_SOURCES_FILE)
    source = bc.source_for("units/stages/analysis.md", registry)
    assert source.id == "ai4bcm-guidance"
    assert source.licence_class == "A"
    assert source.licence == "CC BY 4.0"


def test_the_corpus_may_hold_more_chunks_than_the_units_alone(tmp_path):
    """Literature is chunked beside the units, so the count bound is not a unit count.

    Improvements ticket 08: DORA alone is 65 chunks. A build that validated only up to 300
    would refuse the corpus the registry exists to carry.
    """
    units = write_units(tmp_path)
    registry = bc.load_sources(write_registry(tmp_path, [ROW]))
    chunks = bc.build_all(units, "2026.09", registry)
    # Derived from the reserved set rather than restated, so ticket 07 adding an id to
    # CITATION-CONTRACT.md does not silently turn this fixture into a false failure.
    stage_fillers = [
        bc.Chunk(id=cid, unit=cid.rsplit("-", 1)[0], section_type="section",
                 title=cid, breadcrumb=cid, text="body", char_count=4,
                 url=bc.citation_url("units/filler.md", "2026.09", "filler"),
                 source_file="units/filler.md",
                 release_tag="2026.09", source_id="test-source", source_edition="1.0",
                 licence="CC BY 4.0", citation="c")
        for cid in sorted(bc.RESERVED_CHUNK_IDS)
    ]
    filler = [
        bc.Chunk(id=f"literature-filler-{n}", unit="literature", section_type="section",
                 title="t", breadcrumb="t", text="body", char_count=4,
                 url=bc.citation_url("literature/filler.md", "2026.09", "filler"),
                 source_file="literature/filler.md",
                 release_tag="2026.09", source_id="test-source", source_edition="1.0",
                 licence="CC BY 4.0", citation="c")
        for n in range(400)
    ]
    bc.validate(chunks + stage_fillers + filler, "2026.09")  # no SystemExit
