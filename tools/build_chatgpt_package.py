#!/usr/bin/env python3
"""build_chatgpt_package.py — generate `skills/` so the router travels with its units.

The Claude route ships the whole repository: `.claude-plugin/plugin.json` declares
`"skills": ["./"]`, the client reads `ask-ai4bcm/SKILL.md` from the repository root, and the
router's 46 relative links into `units/` resolve because `units/` is sitting right there.

A portable Agent Plugins package does not work that way. It discovers skills from
`skills/<name>/` and nothing else:

    "Portable packages always discover skills in `skills/`"
    — https://developers.openai.com/plugins/build/plugins.md, read 2026-09-10

and the same paragraph says a `skills` declaration in the inline extension or the compatibility
overlay cannot replace, disable or add to that discovery. (Paraphrased rather than quoted: the
sentence names a manifest key this package must not contain anywhere, and the acceptance check
for "no MCP declaration" is a grep over the whole tree.)

So `"skills": ["./"]` cannot carry `units/` into a ChatGPT install, and a router placed at
`skills/ask-ai4bcm/SKILL.md` with the units left at the package root resolves `../units/` to
`skills/units/`, which does not exist: all 46 links dangle. That was measured, not assumed.

This script is the answer. It copies the router and the units into `skills/ask-ai4bcm/` so the
skill carries its own references, as the format intends —

    "Keep each skill with its `SKILL.md`, scripts, references, and assets."
    — https://developers.openai.com/plugins/guides/submit-claude-plugin.md, read 2026-09-10
    "When referencing other files in your skill, use relative paths from the skill root."
    — https://agentskills.io/specification.md, read 2026-09-10

— and rewrites `../units/` to `units/` in `SKILL.md` to match the move. That rewrite is the
only edit made to the router's text, it is mechanical, and `--check` proves it by regenerating
the whole tree from source and comparing.

`skills/` is generated and committed. It has to be committed, because a workspace admin
importing the marketplace from GitHub gets the repository as it stands and nothing runs a build
step for them. `--check` is what keeps a committed copy from drifting away from `units/`.

Usage:
  build_chatgpt_package.py                 regenerate <repo>/skills/ from ask-ai4bcm/ and units/
  build_chatgpt_package.py --check         exit 1 if the committed skills/ tree has drifted
  build_chatgpt_package.py --links DIR     resolve every relative link under DIR, exit 1 on dangle
  build_chatgpt_package.py --archive PATH  write the uploadable .tar.gz

This script never commits, never tags and never pushes.
"""
import argparse
import filecmp
import os
import re
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parent.parent
SKILL_NAME = "ask-ai4bcm"

# The handout is published guidance the router links to, and it lives in the vault. It is
# copied in rather than generated; VAULT_ONLY names what the repository does not carry itself.
VAULT_UNITS = Path("/opt/brain-live/02-Projects/ai4bcm/guidance-rewrite/units")

# `ask-ai4bcm/README.md` points at `install/`, which is repository-only and never enters the
# package. In the package that link has to reach the repository on the web instead.
README_REWRITES = {
    "../install/README.md": "https://github.com/AI4BCM/guidance/blob/main/install/README.md",
}

# Files the archive carries beside the skill: the two manifests and the licence the citation
# line depends on. `install/`, `units/`, `literature/` and `tools/` are repository furniture.
ARCHIVE_EXTRAS = ("plugin.json", ".claude-plugin/plugin.json", "LICENSE")


def build(repo: Path, dest: Path) -> None:
    """Write the packaged skill tree at `dest` (which becomes `<dest>/<SKILL_NAME>/`)."""
    skill = dest / SKILL_NAME
    if skill.exists():
        shutil.rmtree(skill)
    (skill / "agents").mkdir(parents=True)

    src = repo / SKILL_NAME
    # SKILL.md: the one edit. `../units/` becomes `units/` because the units move inside.
    text = (src / "SKILL.md").read_text(encoding="utf-8")
    (skill / "SKILL.md").write_text(text.replace("../units/", "units/"), encoding="utf-8")

    readme = (src / "README.md").read_text(encoding="utf-8")
    for old, new in README_REWRITES.items():
        readme = readme.replace(old, new)
    (skill / "README.md").write_text(readme, encoding="utf-8")

    shutil.copy2(src / "agents" / "openai.yaml", skill / "agents" / "openai.yaml")

    shutil.copytree(repo / "units", skill / "units")
    for extra in ("principles-a4.html",):
        target = skill / "units" / extra
        if not target.exists() and (VAULT_UNITS / extra).exists():
            shutil.copy2(VAULT_UNITS / extra, target)


def tree_diff(left: Path, right: Path) -> list[str]:
    """Every path under `left` or `right` that is missing on the other side or differs."""
    def paths(root: Path) -> set[str]:
        return {
            str(p.relative_to(root))
            for p in root.rglob("*")
            if p.is_file() and "__pycache__" not in p.parts
        }

    out = []
    for rel in sorted(paths(left) | paths(right)):
        a, b = left / rel, right / rel
        if not a.exists():
            out.append(f"only in {right}: {rel}")
        elif not b.exists():
            out.append(f"only in {left}: {rel}")
        elif not filecmp.cmp(a, b, shallow=False):
            out.append(f"differs: {rel}")
    return out


def check_links(root: Path) -> int:
    """Resolve every relative markdown link under `root`. Returns the dangling count."""
    total = dangling = 0
    for md in sorted(root.rglob("*.md")):
        for target in re.findall(r"\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            total += 1
            resolved = (md.parent / target.split("#")[0]).resolve()
            if not resolved.exists():
                dangling += 1
                print(f"  DANGLING  {md.relative_to(root)}  ->  {target}")
    print(f"{total} relative links under {root}, {dangling} dangling")
    return dangling


def write_archive(repo: Path, out: Path) -> None:
    with tarfile.open(out, "w:gz") as tar:
        for extra in ARCHIVE_EXTRAS:
            tar.add(repo / extra, arcname=extra)
        for path in sorted((repo / "skills").rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                tar.add(path, arcname=str(path.relative_to(repo)))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", type=Path, default=DEFAULT_REPO)
    ap.add_argument("--check", action="store_true", help="exit 1 if skills/ has drifted")
    ap.add_argument("--links", type=Path, help="resolve every relative link under this directory")
    ap.add_argument("--archive", type=Path, help="write the uploadable .tar.gz here")
    args = ap.parse_args()

    repo = args.repo.resolve()

    if args.links:
        return 1 if check_links(args.links.resolve()) else 0

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            build(repo, Path(tmp))
            drift = tree_diff(repo / "skills" / SKILL_NAME, Path(tmp) / SKILL_NAME)
        if drift:
            print("skills/ has drifted from ask-ai4bcm/ and units/:")
            for line in drift:
                print(f"  {line}")
            print("regenerate with: build_chatgpt_package.py")
            return 1
        print(f"skills/{SKILL_NAME} is in sync with ask-ai4bcm/ and units/")
        return 0

    build(repo, repo / "skills")
    print(f"wrote {repo / 'skills' / SKILL_NAME}")
    if args.archive:
        write_archive(repo, args.archive.resolve())
        size = os.path.getsize(args.archive.resolve())
        print(f"wrote {args.archive.resolve()} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
