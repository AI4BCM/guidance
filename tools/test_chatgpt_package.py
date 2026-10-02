"""The ChatGPT package's invariants, pinned.

The one that matters is the third: the router names its units by relative link, and a portable
plugin discovers skills only from `skills/<name>/`. If the units stop travelling inside the skill
folder, every one of those links dangles in a reader's ChatGPT and the router is worse than
nothing. `test_no_dangling_links` is the guard on that, and `test_committed_tree_matches_build`
is the guard on the committed copy quietly falling behind `units/`.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

import build_chatgpt_package as bp

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "ask-ai4bcm"


def relative_links(text: str) -> list[str]:
    return [
        t for t in re.findall(r"\]\(([^)]+)\)", text)
        if not re.match(r"^[a-z][a-z0-9+.-]*:", t) and not t.startswith("#")
    ]


def test_package_has_the_shape_the_schema_requires():
    assert (REPO / "plugin.json").is_file()
    assert (SKILL / "SKILL.md").is_file()
    manifest = json.loads((REPO / "plugin.json").read_text())
    assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert manifest["name"] == "ai4bcm-guidance"
    # additionalProperties is false in Agent Plugins 1.0.0, so an unknown key is a broken manifest.
    allowed = {
        "$schema", "name", "version", "description", "author",
        "homepage", "repository", "license", "keywords", "extensions",
    }
    assert set(manifest) <= allowed, f"not in the schema: {sorted(set(manifest) - allowed)}"


def test_packaged_router_is_the_source_router_under_one_path_transform():
    """The only edit the packaging makes, and the reason it is safe to make it."""
    source = (REPO / "ask-ai4bcm" / "SKILL.md").read_text(encoding="utf-8")
    packaged = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert packaged == source.replace("../units/", "units/")
    assert "](../units/" not in packaged


def test_no_dangling_links(tmp_path):
    """Build, then resolve every relative link from inside the built tree."""
    bp.build(REPO, tmp_path)
    built = tmp_path / "ask-ai4bcm"
    checked = 0
    for md in built.rglob("*.md"):
        for target in relative_links(md.read_text(encoding="utf-8")):
            checked += 1
            resolved = (md.parent / target.split("#")[0]).resolve()
            assert resolved.exists(), f"{md.relative_to(built)} -> {target}"
    assert checked >= 48, f"the router carried 48 links; only {checked} were checked"


def test_the_router_still_carries_all_of_its_links():
    source = relative_links((REPO / "ask-ai4bcm" / "SKILL.md").read_text(encoding="utf-8"))
    packaged = relative_links((SKILL / "SKILL.md").read_text(encoding="utf-8"))
    # 46 until 2026-09-28; the keep-it-running on-ramp carries two more. The 2026.11 rebuild (ticket 13) adds
    # the clause 8.4 on-ramp's two links (data rules, the Validate stage prompt): 50.
    assert len(source) == len(packaged) == 50


def test_no_mcp_declaration_anywhere_in_the_package():
    """A package declaring an MCP server is labelled Desktop only and loses ChatGPT on the web."""
    for name in ("mcp.json", ".mcp.json"):
        assert not list(REPO.glob(f"**/{name}")), f"{name} would cost the web surface"
    # Built rather than written out, so this file is not itself a hit for its own check.
    key = "mcp" + "Servers"
    for path in REPO.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                assert key not in path.read_text(encoding="utf-8"), path
            except (UnicodeDecodeError, OSError):
                pass


def test_disable_model_invocation_survives_packaging():
    """Owner decision: it stays, although the Agent Skills reference validator rejects it."""
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert text.count("disable-model-invocation") == 1


def test_no_claude_specific_wording_in_the_package():
    """The conversion guide asks for provider-neutral language in a submitted skill.

    Shelf 1 (`literature/cited/`) is exempt: those are publishers' texts carried verbatim under
    their licences (the UK AI Playbook names Claude among public tools), not the skill's own
    words. The literature README is ours and is checked."""
    for path in SKILL.rglob("*"):
        if path.is_relative_to(SKILL / "literature" / "cited"):
            continue
        if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
            body = path.read_text(encoding="utf-8").lower()
            for term in ("claude", "userconfig", "${user_config"):
                assert term not in body, f"{path.relative_to(SKILL)} still says {term!r}"


def test_committed_tree_matches_a_fresh_build(tmp_path):
    bp.build(REPO, tmp_path)
    assert bp.tree_diff(SKILL, tmp_path / "ask-ai4bcm") == []


def test_check_catches_drift(tmp_path):
    bp.build(REPO, tmp_path)
    (tmp_path / "ask-ai4bcm" / "units" / "tools.md").write_text("drifted", encoding="utf-8")
    assert bp.tree_diff(SKILL, tmp_path / "ask-ai4bcm") == ["differs: units/tools.md"]


def test_archive_extracts_with_the_skill_at_the_documented_path(tmp_path):
    """A direct upload needs a skill at skills/<name>/SKILL.md in the archive root."""
    import tarfile

    out = tmp_path / "package.tgz"
    bp.write_archive(REPO, out)
    with tarfile.open(out) as tar:
        names = tar.getnames()
    assert "skills/ask-ai4bcm/SKILL.md" in names
    assert ".claude-plugin/plugin.json" in names
    assert "plugin.json" in names
    assert any(n.startswith("skills/ask-ai4bcm/units/") for n in names)
    assert not any(n.endswith("mcp.json") for n in names)


@pytest.mark.skipif(sys.platform == "win32", reason="posix shell")
def test_cli_check_exits_zero_on_the_committed_tree():
    proc = subprocess.run(
        [sys.executable, str(REPO / "tools" / "build_chatgpt_package.py"), "--check"],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


@pytest.mark.parametrize("name", bp.skill_names(REPO))
def test_every_skill_is_user_invoked_only(name):
    """Preflight 4: a skill runs only when the user types its name, on every client that reads a flag."""
    text = (REPO / name / "SKILL.md").read_text(encoding="utf-8")
    front = text.split("---", 2)[1]
    assert re.search(r"^name: " + re.escape(name) + r"$", front, re.M)
    assert re.search(r"^disable-model-invocation: true$", front, re.M)
    policy = (REPO / name / "agents" / "openai.yaml").read_text(encoding="utf-8")
    assert re.search(r"^\s+allow_implicit_invocation: false$", policy, re.M)


@pytest.mark.parametrize("name", [n for n in bp.skill_names(REPO) if n != bp.SKILL_NAME])
def test_task_skills_carry_the_preflight(name):
    """Every task skill opens on the shared preflight, and its package carries a copy of it."""
    source = (REPO / name / "SKILL.md").read_text(encoding="utf-8")
    body = source.split("---", 2)[2]
    assert body.lstrip().split("\n\n")[0].startswith(f"First run [`../{bp.PREFLIGHT}`](../{bp.PREFLIGHT}).")
    packaged = (REPO / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
    assert packaged == (source.replace("../units/", "units/").replace(f"../{bp.PREFLIGHT}", bp.PREFLIGHT)
                        .replace("../literature/", "literature/"))
    if "../literature/" in source:
        assert (REPO / "skills" / name / "literature").is_dir()
    assert (REPO / "skills" / name / bp.PREFLIGHT).read_bytes() == (REPO / bp.PREFLIGHT).read_bytes()


def test_shelf_one_goes_everywhere_and_shelf_two_only_to_the_two(tmp_path):
    """Ticket 63: the guidance's own sources (literature/cited/ and the licence table) ship in
    every package; the comparison frameworks ship with /check-against-standards and /learn-bcm
    only (direction note 2026.11, "Units and literature")."""
    bp.build(REPO, tmp_path)
    shelf_one = {p.relative_to(REPO / "literature") for p in (REPO / "literature" / "cited").rglob("*.md")}
    shelf_two = {p.relative_to(REPO / "literature") for p in (REPO / "literature").rglob("*.md")
                 if p.relative_to(REPO / "literature").parts[0] not in bp.SHELF_1}
    assert shelf_one and shelf_two
    with_frameworks = set()
    for name in bp.skill_names(REPO):
        lit = tmp_path / name / "literature"
        carried = {p.relative_to(lit) for p in lit.rglob("*.md")}
        assert shelf_one | {Path("README.md")} <= carried, name
        if carried & shelf_two:
            assert carried == shelf_one | shelf_two | {Path("README.md")}, name
            with_frameworks.add(name)
    assert with_frameworks == {"check-against-standards", "learn-bcm"}
