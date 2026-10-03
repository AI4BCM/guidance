"""Search ranking (connector ticket, 2026-10-03: levels outranked by references).

On 2026.11 the references unit's citation lists, and the long literature chunks, outranked the
units they cite: "maturity levels" put references-further-reading first, and "what does the
guidance say about levels of use" had no levels chunk in the top four. The eval set in
search_eval.json holds the questions nemo's ask lane sends; nemo reads the top four.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from retrieval import GuidanceIndex

REPO = Path(__file__).resolve().parent.parent


def _chunk(id, unit, section_type, title, text):
    return {"id": id, "unit": unit, "section_type": section_type, "title": title,
            "breadcrumb": title, "text": text, "url": "", "char_count": len(text)}


def _index(tmp_path, chunks):
    (tmp_path / "chunks.json").write_text(json.dumps(chunks), encoding="utf-8")
    (tmp_path / "index.json").write_text("{}", encoding="utf-8")
    return GuidanceIndex(tmp_path)


def test_a_reference_list_does_not_outrank_the_unit_it_cites(tmp_path):
    ix = _index(tmp_path, [
        _chunk("references-further-reading", "references", "reference", "Further reading",
               "SEI maturity model: five maturity levels. CMMI levels. OWASP maturity levels. "
               "Each source names its own levels; the maturity levels in levels.md follow CMMI."),
        _chunk("levels-the-five", "levels", "section", "The five AI maturity levels",
               "Level 1 to level 5: where a BCM team stands with AI, from first trials to "
               "measured and optimising use. Pick the levels row that fits and start there."),
        _chunk("tools", "tools", "section", "Tools", "Which tool for which data."),
    ])
    assert [c.id for c in ix.search("maturity levels")][0] == "levels-the-five"


def test_a_reference_list_is_still_found_when_only_it_matches(tmp_path):
    ix = _index(tmp_path, [
        _chunk("references", "references", "reference", "References", "CMMI and OWASP."),
        _chunk("levels", "levels", "section", "Levels", "Level 1 to level 5."),
    ])
    assert [c.id for c in ix.search("OWASP")] == ["references"]


def test_function_words_in_the_question_do_not_decide_the_ranking(tmp_path):
    """A long chunk holds every 'the', 'of' and 'what'; the question's subject must win."""
    filler = "what does the system do about it, and what is it for, and how and why " * 40
    ix = _index(tmp_path, [
        _chunk("long-literature", "nist", "section", "5.4 Manage", filler + " levels"),
        _chunk("levels", "levels", "section", "The five AI maturity levels",
               "Five levels of AI use in a BCM team."),
    ] + [_chunk(f"other-{n}", "other", "section", f"Other {n}", "what the of about")
         for n in range(20)])
    hits = ix.search("what does the guidance say about levels of use")
    assert hits[0].id == "levels"


def test_a_question_of_function_words_only_still_searches(tmp_path):
    ix = _index(tmp_path, [
        _chunk("a", "a", "section", "A", "Can I still ask what this is?"),
        _chunk("b", "b", "section", "B", "Recovery time objective."),
    ])
    assert [c.id for c in ix.search("Can I still ask?")] == ["a"]


# --- the eval set, on the corpus this repo builds (units and literature, as published) ---

EVAL = json.loads((REPO / "tools" / "search_eval.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def published(tmp_path_factory):
    out = tmp_path_factory.mktemp("published")
    subprocess.run([sys.executable, str(REPO / "tools" / "build_chunks.py"), "--data-dir", str(out),
                    "--source-dir", str(REPO / "literature")], check=True, capture_output=True)
    return GuidanceIndex(out)


@pytest.mark.parametrize("question", ["maturity levels",
                                      "what does the guidance say about levels of use"])
def test_the_desk_questions_put_levels_first(published, question):
    assert published.search(question, limit=EVAL["k"])[0].unit == "levels"


def test_the_eval_set_hit_rate_holds(published):
    """16 of 20 when this ranking landed (2026-10-03; the old ranking: 12 on 2026.11).
    A lower number is a regression; a higher one should raise this floor."""
    hits = [q["q"] for q in EVAL["questions"]
            if any(c.unit in q["expect"] for c in published.search(q["q"], limit=EVAL["k"]))]
    assert len(hits) >= 16, sorted(set(q["q"] for q in EVAL["questions"]) - set(hits))
