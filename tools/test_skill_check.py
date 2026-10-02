"""Tests for skill_check.py, on a scratch repo holding the real units and a fixture skill."""
import shutil
from pathlib import Path

import pytest

import skill_check as sc

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FIXTURE = HERE / "testdata" / "minimal-skill" / "SKILL.md"


@pytest.fixture
def repo(tmp_path):
    shutil.copytree(REPO / "units", tmp_path / "units")
    shutil.copy2(REPO / "preflight.md", tmp_path / "preflight.md")
    (tmp_path / "minimal-skill").mkdir()
    shutil.copy2(FIXTURE, tmp_path / "minimal-skill" / "SKILL.md")
    return tmp_path


def failures(repo, name="minimal-skill"):
    return [line for ok, line in sc.check(name, repo, package=False) if not ok]


def edit(repo, old, new, name="minimal-skill"):
    p = repo / name / "SKILL.md"
    text = p.read_text(encoding="utf-8")
    assert old in text
    p.write_text(text.replace(old, new), encoding="utf-8")


def test_the_minimal_skill_is_green(repo):
    assert failures(repo) == []


def test_a_missing_part_is_red(repo):
    edit(repo, "## For the auditor", "## Notes")
    assert any("missing For the auditor" in f for f in failures(repo))


def test_a_quote_not_in_the_units_is_red(repo):
    edit(repo, "The activity owner confirms", '"the model sets the RTO for you" The activity owner confirms')
    assert any("the model sets the RTO" in f for f in failures(repo))


def test_a_blockquote_is_a_line_to_say_not_a_quote(repo):
    edit(repo, "> Anything else we should know?", '> "Anything else we should know about this?"')
    assert failures(repo) == []


def test_a_quote_with_an_ellipsis_matches_its_parts_in_order(repo):
    edit(repo, '"a resource requirement drafted by AI is only a question for the activity owner."',
         '"a resource requirement drafted by AI … the activity owner"')
    assert failures(repo) == []


def test_an_unknown_citation_is_red(repo):
    edit(repo, "IMDA 2.3.1", "IMDA 9.9.9")
    assert any("IMDA" in f and "9.9.9" in f for f in failures(repo))


def test_a_missing_principle_is_red(repo):
    edit(repo, "principle 4", "principle 9")
    assert any("principle 9" in f for f in failures(repo))


def test_a_unit_heading_that_does_not_exist_is_red(repo):
    edit(repo, "units/data-rules.md, Prompt injection", "units/data-rules.md, Prompt hygiene")
    assert any("Prompt hygiene" in f for f in failures(repo))


def test_a_heading_link_is_red(repo):
    edit(repo, "(../units/prompts/bia.md)", "(../units/prompts/bia.md#task)")
    assert any("links a heading" in f for f in failures(repo))


def test_a_broken_link_is_red(repo):
    edit(repo, "(../units/prompts/bia.md)", "(../units/prompts/nope.md)")
    assert any("does not resolve" in f for f in failures(repo))


def test_a_long_body_is_red(repo):
    edit(repo, "## Reviewer", "## Reviewer\n\n" + "word " * 500)
    assert any("words (at most 500)" in f for f in failures(repo))


def test_the_router_may_run_to_a_thousand_words(repo):
    shutil.copytree(repo / "minimal-skill", repo / "ask-ai4bcm")
    edit(repo, "name: minimal-skill", "name: ask-ai4bcm", name="ask-ai4bcm")
    edit(repo, "## Reviewer", "## Reviewer\n\n" + "word " * 600, name="ask-ai4bcm")
    assert failures(repo, "ask-ai4bcm") == []


def test_frontmatter_name_must_match_the_folder(repo):
    edit(repo, "name: minimal-skill", "name: other")
    assert any("frontmatter" in f for f in failures(repo))


def test_model_invocation_must_stay_off(repo):
    edit(repo, "disable-model-invocation: true", "disable-model-invocation: false")
    assert any("disable-model-invocation" in f for f in failures(repo))


def test_method_needs_numbered_steps(repo):
    edit(repo, "1. Fix", "- Fix")
    edit(repo, "2. Draft", "- Draft")
    assert any("Method: 0" in f for f in failures(repo))


def test_main_exits_one_on_red_and_zero_on_green(repo, capsys):
    assert sc.main(["minimal-skill", "--repo", str(repo), "--no-package"]) == 0
    edit(repo, "## Method", "## Steps")
    assert sc.main(["minimal-skill", "--repo", str(repo), "--no-package"]) == 1
    assert "red" in capsys.readouterr().out


def clean_failures(repo, max_words=None):
    return [line for ok, line in sc.check_clean("minimal-skill", repo, max_words) if not ok]


def test_the_minimal_skill_is_clean(repo):
    assert clean_failures(repo, max_words=sc.words(sc.split_frontmatter(FIXTURE.read_text())[1])) == []


def test_a_banned_word_is_red(repo):
    edit(repo, "The activity owner confirms", "The activity owner robustly confirms, moreover")
    assert any("moreover" in f for f in clean_failures(repo))


def test_an_em_dash_is_red(repo):
    edit(repo, "The activity owner confirms", "The activity owner — and only they — confirms")
    assert any("em-dashes: 2" in f for f in clean_failures(repo))


def test_the_cleaner_may_not_lengthen_the_body(repo):
    assert any("builder left 5" in f for f in clean_failures(repo, max_words=5))


REVIEW = """# Review of minimal-skill

Skill sha: {sha}
Stage unit: units/stages/analysis.md

| Unit item | Skill line | Verdict |
|---|---|---|
| One control | "a resource requirement drafted by AI …" | carried |
{rows}
"""


def write_review(repo, rows=None, sha=None):
    import subprocess
    sha = sha or subprocess.run(["git", "hash-object", str(repo / "minimal-skill" / "SKILL.md")],
                                capture_output=True, text=True).stdout.strip()
    n = sc.unit_method_steps(repo / "units" / "stages" / "analysis.md")
    rows = rows if rows is not None else "\n".join(f"| Method {i} | step {i} | carried |" for i in range(1, n + 1))
    (repo / "evals" / "minimal-skill").mkdir(parents=True, exist_ok=True)
    (repo / "evals" / "minimal-skill" / "review.md").write_text(REVIEW.format(sha=sha, rows=rows))


def review_failures(repo):
    return [line for ok, line in sc.check_review("minimal-skill", repo) if not ok]


def test_a_full_review_is_green(repo):
    write_review(repo)
    assert review_failures(repo) == []


def test_a_review_of_an_older_skill_is_red(repo):
    write_review(repo, sha="0000000")
    assert any("current SKILL.md" in f for f in review_failures(repo))


def test_a_missing_method_row_is_red(repo):
    write_review(repo, rows="| Method 1 | step 1 | carried |")
    assert any("missing Method 2" in f for f in review_failures(repo))


def test_a_row_marked_missing_is_red(repo):
    n = sc.unit_method_steps(repo / "units" / "stages" / "analysis.md")
    rows = "\n".join(f"| Method {i} | step {i} | carried |" for i in range(1, n)) + f"\n| Method {n} | none | missing |"
    write_review(repo, rows=rows)
    assert any(f"nothing missing: Method {n}" in f for f in review_failures(repo))


def test_no_review_is_red(repo):
    assert review_failures(repo) == ["evals/minimal-skill/review.md does not exist"]


def test_a_router_on_ramp_label_is_the_users_words_not_a_quote():
    line = '- **"I inherited forty BIAs and no requirements register."** Stage 3 with `/prepare-bia`.'
    assert sc.quotes(line, labels=False) == []
    assert sc.quotes(line) == ["I inherited forty BIAs and no requirements register."]


def test_a_unit_with_no_method_owes_one_row_per_skill_step(repo):
    write_review(repo, rows="| Method 1 | step 1 | carried |")
    p = repo / "evals" / "minimal-skill" / "review.md"
    p.write_text(p.read_text().replace("units/stages/analysis.md", "units/prompts/review.md"))
    n = sc.skill_method_steps("minimal-skill", repo)
    assert n > 1 and any(f"missing Method 2" in f for f in review_failures(repo))


def test_a_named_section_with_no_numbered_list_falls_back_to_the_skill_steps(repo):
    n = sc.skill_method_steps("minimal-skill", repo)
    write_review(repo, rows="\n".join(f"| Method {i} | step {i} | carried |" for i in range(1, n + 1)))
    p = repo / "evals" / "minimal-skill" / "review.md"
    p.write_text(p.read_text().replace("units/stages/analysis.md", "units/stages/govern.md, Onboarding new BCM staff"))
    assert review_failures(repo) == []


def test_missing_inside_a_quoted_skill_line_is_not_a_verdict(repo):
    n = sc.unit_method_steps(repo / "units" / "stages" / "analysis.md")
    rows = "\n".join(f"| Method {i} | step {i} | carried |" for i in range(2, n + 1))
    write_review(repo, rows='| Method 1 | "Label each missing value" | carried |\n' + rows)
    assert review_failures(repo) == []
