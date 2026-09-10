"""Asserts the real guidance corpus builds to the chunk count the server serves.

Moved here from `bia-workflow` on 2026-09-10 (kb-move ticket 05). It was marked private-only
there because it needed the `guidance` submodule checked out, which a public contributor might
not have. **That reason is gone**: the units are in this repository, so the test simply runs.

Guards the knowledge-source home: build_chunks must read the units from this repo, never from
the vault. The vault is the units' source of record and this repository is the published mirror.

2026-09-10, publish-and-audit ticket 05: the July snapshot (addendum-clean.md +
knowledge/*.md, 146 chunks keyed `ppN-section`) was retired for the guidance units, keyed on
the unit path and its heading. The count is pinned so a unit edit that silently drops or
splits a section shows up here.
"""
import pytest

import build_chunks as bc

pytestmark = pytest.mark.skipif(
    not bc.DEFAULT_UNITS_DIR.is_dir(),
    reason="guidance submodule not checked out (git submodule update --init --recursive)",
)

EXPECTED_CHUNKS = 96


def test_source_constants_are_local_not_vault():
    for p in (bc.DEFAULT_UNITS_DIR, bc.DEFAULT_RELEASES_DIR):
        assert "/opt/brain-live" not in str(p), f"{p} still points at the vault"
    assert bc.DEFAULT_UNITS_DIR.is_dir(), f"missing local units dir: {bc.DEFAULT_UNITS_DIR}"
    assert bc.DEFAULT_RELEASES_DIR.is_dir(), f"missing release manifest dir: {bc.DEFAULT_RELEASES_DIR}"


def test_builds_the_expected_chunk_count_from_the_units():
    tag = bc.release_tag_from(bc.DEFAULT_RELEASES_DIR)
    chunks = bc.build_all(bc.DEFAULT_UNITS_DIR, tag)
    assert len(chunks) == EXPECTED_CHUNKS, f"expected {EXPECTED_CHUNKS} chunks, got {len(chunks)}"
    bc.validate(chunks, tag)


def test_no_chunk_id_carries_a_retired_professional_practice_code():
    """The owner's decision of 2026-09-09: no GPG reference anywhere in the guidance.

    A chunk id is a public URL and the citation on an answer, so this is a reader-facing
    surface and not an internal key.
    """
    tag = bc.release_tag_from(bc.DEFAULT_RELEASES_DIR)
    offenders = [c.id for c in bc.build_all(bc.DEFAULT_UNITS_DIR, tag)
                 if bc.RETIRED_PP_RE.search(c.id)]
    assert offenders == [], f"retired PP identifiers are back: {offenders}"


def test_every_chunk_carries_the_release_tag():
    tag = bc.release_tag_from(bc.DEFAULT_RELEASES_DIR)
    chunks = bc.build_all(bc.DEFAULT_UNITS_DIR, tag)
    assert chunks and all(c.release_tag == tag for c in chunks)
