"""Tests for the guidance-only tool surface (kb-move ticket 04).

The point of these is not coverage for its own sake: ticket 06 cuts a live endpoint over to this
code, so what matters is that the payload shapes did not drift when the BIA coupling came out.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import guidance_tools as gt
from retrieval import GuidanceIndex

REPO = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def data_dir(tmp_path_factory):
    """Build the units corpus once, from this repo, into a scratch dir."""
    out = tmp_path_factory.mktemp("data")
    subprocess.run([sys.executable, str(REPO / "tools" / "build_chunks.py"),
                    "--data-dir", str(out)], check=True, capture_output=True)
    return out


@pytest.fixture(autouse=True)
def _index(data_dir):
    gt.use_index(GuidanceIndex(data_dir))
    yield
    gt.use_index(None) if False else None


def test_corpus_is_the_ninety_six(data_dir):
    chunks = json.loads((data_dir / "chunks.json").read_text(encoding="utf-8"))
    assert len(chunks) == 96


def test_search_returns_hits_with_the_expected_keys():
    results = gt.search_fn("business impact analysis")
    assert results
    assert set(results[0]) == {"id", "title", "url", "section_type", "unit", "release_tag",
                               "risk_level", "output_type", "mode", "bcm_process", "confidentiality"}


def test_search_carries_no_journey_hint():
    """The hint told callers to call open_bia, which does not exist on this endpoint."""
    for r in gt.search_fn("business impact analysis"):
        assert "guided_journey" not in r


def test_search_filters_by_unit_case_insensitively():
    hits = gt.search_fn("analysis")
    assert hits
    unit = hits[0]["unit"]
    assert gt.search_fn("analysis", unit=unit.upper())


def test_fetch_roundtrips_a_real_id():
    first = gt.search_fn("business impact analysis")[0]
    payload = gt.fetch_fn(first["id"])
    assert payload["id"] == first["id"]
    assert payload["text"]


def test_fetch_carries_licence_and_citation():
    """A payload that carries a section's words carries the terms they come under."""
    first = gt.search_fn("business impact analysis")[0]
    meta = gt.fetch_fn(first["id"])["metadata"]
    assert "licence" in meta and "citation" in meta


def test_fetch_of_a_missing_id_is_an_error_not_an_exception():
    out = gt.fetch_fn("no-such-chunk-id")
    assert out["error"] == "not_found"
    assert "no-such-chunk-id" in out["message"]


def test_fetch_carries_no_guided_journey_key():
    first = gt.search_fn("business impact analysis")[0]
    assert "guided_journey" not in gt.fetch_fn(first["id"])


def test_get_workflow_falls_back_and_lists_ids_when_absent():
    out = gt.get_workflow_fn("definitely-not-a-workflow-id")
    assert "id" in out or out.get("error") == "not_found"
    if out.get("error"):
        assert "available_workflow_ids" in out


def test_get_prompt_template_returns_templates_or_a_clean_error():
    out = gt.get_prompt_template_fn("draft a business impact analysis")
    assert "templates" in out or out.get("error") == "not_found"
    if "templates" in out:
        assert out["count"] == len(out["templates"])


def test_identify_ai_risks_uses_the_callers_description():
    """_active_risk_task is gone, so nothing can override what the caller said."""
    out = gt.identify_ai_risks_fn("summarise a recovery plan with an assistant")
    assert out["task"] == "summarise a recovery plan with an assistant"
    assert out["risk_level"] in {"critical", "high", "medium", "low"}
    assert "cited_sections" in out


def test_no_bia_session_module_is_importable_from_here():
    """The seam: this surface must not reach back into the BIA session code."""
    import guidance_tools
    src = Path(guidance_tools.__file__).read_text(encoding="utf-8")
    for mod in ("answer_sheet", "call_log", "graph_files", "journeys"):
        assert f"import {mod}" not in src
