#!/usr/bin/env python3
"""The guidance tool surface: what an AI4BCM connector exposes, and nothing else.

Lifted from `guidance_tools.py` in `bia-workflow` on 2026-09-10 (kb-move ticket 04). That file is
849 lines and imports `answer_sheet`, `call_log`, `graph_files` and `journeys`. These five functions
were measured to need none of them: every one reads the retrieval index and returns a payload.

The payload shapes are kept byte-compatible with the originals on purpose, so ticket 06 can diff this
server's answers against the live endpoint's before cutting over. Do not tidy a key name here.

Two things were deliberately dropped, and both were BIA session coupling:

- **The guided-journey hint.** `search_fn` and `fetch_fn` decorated results whose `bcm_process` was
  `bia` or `risk-assessment` with a string telling the caller to "Call open_bia with the company
  room". `open_bia` is a BIA session tool and does not exist on this endpoint, so keeping the hint
  would emit an instruction to call a tool that is not there. Callers see one fewer optional key:
  `guided_journey` on a fetch, and the separate hint a search returned alongside its results.
- **`_active_risk_task`.** A process-global set only by `start_journey_fn`, which let a running BIA
  journey override the model's own description of its work. Nothing on this side sets it, so it would
  be permanently `None`; `identify_ai_risks` now always uses the caller's description.
"""
from __future__ import annotations

from pathlib import Path

from retrieval import GuidanceIndex

_index: GuidanceIndex | None = None
_DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def _idx() -> GuidanceIndex:
    global _index
    if _index is None:
        _index = GuidanceIndex(_DATA_DIR)
    return _index


def use_index(index: GuidanceIndex) -> None:
    """Point the tool surface at a specific index. For tests and for a server that owns its own."""
    global _index
    _index = index


def search_fn(query, unit=None, output_type=None, risk_level=None, confidentiality=None,
              bcm_process=None, mode=None):
    unit_norm = unit.lower().strip() if unit else None
    return [
        {"id": c.id, "title": c.breadcrumb, "url": c.url, "section_type": c.section_type,
         "unit": c.unit, "release_tag": c.release_tag, "risk_level": c.risk_level,
         "output_type": c.output_type,
         "mode": c.mode, "bcm_process": c.bcm_process, "confidentiality": c.confidentiality}
        for c in _idx().search(query, unit=unit_norm, output_type=output_type, risk_level=risk_level,
                               confidentiality=confidentiality, bcm_process=bcm_process, mode=mode)
    ]


def fetch_fn(chunk_id):
    c = _idx().get(chunk_id)
    if not c:
        return {"error": "not_found", "message": f"No section found for id {chunk_id}."}
    return {
        "id": c.id, "title": c.breadcrumb, "text": c.text, "url": c.url,
        "metadata": {"breadcrumb": c.breadcrumb, "unit": c.unit, "release_tag": c.release_tag,
                     "section_type": c.section_type,
                     "risk_level": c.risk_level, "output_type": c.output_type,
                     "mode": c.mode, "bcm_process": c.bcm_process,
                     "confidentiality": c.confidentiality,
                     "related_controls": c.related_controls, "source_file": c.source_file,
                     # The one payload that carries a section's words carries the terms they
                     # come under, so a reader who quotes it can cite it (ticket 05).
                     "licence": c.licence, "citation": c.citation},
    }


def get_workflow_fn(workflow_id):
    idx = _idx()
    c = idx.get(workflow_id)
    if not c or c.section_type != "workflow":
        results = idx.search(workflow_id, output_type="workflow", limit=1) or \
                  [ch for ch in idx.chunks if ch.section_type == "workflow"]
        c = results[0] if results else None
    if not c:
        return {"error": "not_found", "message": f"No workflow found for '{workflow_id}'.",
                "available_workflow_ids": [ch.id for ch in idx.chunks if ch.section_type == "workflow"]}
    return {
        "id": c.id, "title": c.breadcrumb, "text": c.text, "url": c.url,
        "metadata": {"unit": c.unit, "release_tag": c.release_tag, "bcm_process": c.bcm_process,
                     "risk_level": c.risk_level,
                     "related_controls": c.related_controls, "related_examples": c.related_examples},
    }


def get_prompt_template_fn(task, risk_level=None):
    idx = _idx()
    results = idx.search(task, output_type="prompt", risk_level=risk_level, limit=3)
    if not results:
        results = [c for c in idx.search(task, limit=3) if c.section_type == "prompt"] or \
                  idx.search(task, limit=1)
    if not results:
        return {"error": "not_found", "message": f"No prompt template found for task '{task}'."}
    return {"task": task, "count": len(results), "templates": [
        {"id": c.id, "title": c.breadcrumb, "text": c.text, "url": c.url,
         "risk_level": c.risk_level, "mode": c.mode, "controls": c.related_controls}
        for c in results
    ]}


def identify_ai_risks_fn(task_description):
    idx = _idx()
    governance = idx.search(task_description, limit=4)
    relevant_dnu = [c for c in idx.search(task_description, limit=3) if c.section_type == "do_not_use"]
    combined = list({c.id: c for c in (governance + relevant_dnu)}.values())
    risk_order = {"critical": 4, "high": 3, "medium": 2, "low": 1, "": 0}
    max_risk = max((risk_order.get(c.risk_level, 0) for c in combined), default=0)
    overall_risk = {4: "critical", 3: "high", 2: "medium", 1: "low", 0: "low"}[max_risk]
    return {
        "task": task_description, "risk_level": overall_risk,
        "applicable_controls": list(dict.fromkeys(ctrl for c in combined for ctrl in c.related_controls)),
        "do_not_use_warnings": [{"id": c.id, "title": c.breadcrumb, "summary": c.text[:400]}
                                for c in combined if c.section_type == "do_not_use"],
        "cited_sections": [{"id": c.id, "title": c.breadcrumb, "url": c.url} for c in combined],
    }
