#!/usr/bin/env python3
"""check_installs.py: install the skills by each route into a clean folder, then check the disk.

Ticket 68's acceptance: "a fresh install by each route on a clean folder carries the preflight
and units (checked on disk)". Each route installs from a fresh `git clone` of HEAD, so what is
checked is what is committed, the way a reader on GitHub gets it, never the working tree.

Routes:
  claude    Claude Code plugin: `claude plugin marketplace add` + `claude plugin install`, under
            a throwaway CLAUDE_CONFIG_DIR (never the user's ~/.claude). Also checks that
            `claude plugin details` counts each skill once.
  skills    The `skills` CLI for Codex and GitHub Copilot: `npx skills add <clone>/skills
            -a codex -a github-copilot --copy` into an empty project folder (project scope,
            never -g). Telemetry off.
  chatgpt   The upload: `build_chatgpt_package.py --zips` from the clone, each zip extracted.

Every installed skill must be byte for byte its package `skills/<name>/`: SKILL.md, preflight.md,
units/, literature/ (shelf 1 everywhere, shelf 2 for two skills). A missing or changed file fails.

Usage:
  check_installs.py                     all three routes, scratch under a temp dir
  check_installs.py --routes skills     one route
  check_installs.py --keep DIR          install under DIR and leave it for inspection

Needs `git`; `claude` for the claude route; `npx` (network) for the skills route. Not part of the
pytest suite, because two routes need those CLIs and the network. Never installs at user scope.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_chatgpt_package as bp  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SKILLS_CLI = os.environ.get("SKILLS_CLI_VERSION", "1.7.0")
ROUTES = ("claude", "skills", "chatgpt")


def run(cmd: list[str], cwd: Path, env: dict | None = None, timeout: int = 300) -> str:
    proc = subprocess.run(cmd, cwd=cwd, env={**os.environ, **(env or {})}, capture_output=True,
                          text=True, timeout=timeout)
    out = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", proc.stdout + proc.stderr)
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} exited {proc.returncode}:\n{out[-2000:]}")
    return out


def check_tree(installed_root: Path, packages: Path, names: list[str]) -> list[str]:
    """One line per skill; a line starting FAIL names what is missing or changed."""
    lines = []
    for name in names:
        got, want = installed_root / name, packages / name
        if not (got / "SKILL.md").is_file():
            lines.append(f"FAIL {name}: no SKILL.md at {got}")
            continue
        drift = bp.tree_diff(want, got)
        units = len(list((got / "units").rglob("*.md"))) if (got / "units").is_dir() else 0
        lit = len(list((got / "literature").rglob("*.md"))) if (got / "literature").is_dir() else 0
        pf = "yes" if (got / bp.PREFLIGHT).is_file() else "NO"
        files = sum(1 for p in got.rglob("*") if p.is_file())
        status = "ok  " if not drift and pf == "yes" and units else "FAIL"
        lines.append(f"{status} {name}: preflight.md {pf}, units {units} .md, literature {lit} .md, "
                     f"{files} files, {'identical to the package' if not drift else f'{len(drift)} differences'}")
        lines += [f"       {d}" for d in drift[:10]]
    return lines


def route_claude(src: Path, work: Path, names: list[str]) -> list[str]:
    env = {"CLAUDE_CONFIG_DIR": str(work / "claude-config")}
    proj = work / "project"
    proj.mkdir(parents=True)
    out = [run(["claude", "--version"], proj).strip()]
    run(["claude", "plugin", "marketplace", "add", str(src)], proj, env)
    run(["claude", "plugin", "install", "ai4bcm-guidance@ai4bcm"], proj, env)
    details = run(["claude", "plugin", "details", "ai4bcm-guidance@ai4bcm"], proj, env)
    m = re.search(r"Skills \((\d+)\)\s+(.*)", details)
    listed = m.group(2).split(", ") if m else []
    once = sorted(listed) == sorted(names)
    out.append(f"{'ok  ' if once else 'FAIL'} plugin details: Skills ({m.group(1) if m else '?'}), "
               f"{'each name once' if once else 'expected ' + ', '.join(names)}")
    installed = json.loads((work / "claude-config" / "plugins" / "installed_plugins.json").read_text())
    path = Path(installed["plugins"]["ai4bcm-guidance@ai4bcm"][0]["installPath"])
    out.append(f"installed at {path}")
    return out + check_tree(path / "skills", src / "skills", names)


def route_skills(src: Path, work: Path, names: list[str]) -> list[str]:
    proj = work / "project"
    proj.mkdir(parents=True)
    run(["git", "init", "-q"], proj)
    env = {"DISABLE_TELEMETRY": "1", "DO_NOT_TRACK": "1"}
    log = run(["npx", "-y", f"skills@{SKILLS_CLI}", "add", str(src / "skills"), "-s", "*",
               "-a", "codex", "-a", "github-copilot", "--copy", "-y"], proj, env)
    found = re.search(r"Found \d+ skills?", log)
    out = [f"skills {SKILLS_CLI}: {found.group(0) if found else 'no count printed'}",
           f"installed at {proj / '.agents' / 'skills'} (Codex and GitHub Copilot share it)"]
    return out + check_tree(proj / ".agents" / "skills", src / "skills", names)


def route_chatgpt(src: Path, work: Path, names: list[str]) -> list[str]:
    zips = work / "zips"
    run([sys.executable, str(src / "tools" / "build_chatgpt_package.py"), "--repo", str(src),
         "--zips", str(zips)], src)
    # The build regenerates skills/ in the clone first; a clone whose committed packages had
    # drifted would show up as a dirty tree here.
    dirty = run(["git", "status", "--porcelain"], src).strip()
    out = [f"{'ok  ' if not dirty else 'FAIL'} committed packages match a fresh build"
           + ("" if not dirty else f": {dirty[:300]}")]
    extracted = work / "extracted"
    for name in names:
        with zipfile.ZipFile(zips / f"{name}.zip") as zf:
            zf.extractall(extracted)
    out.append(f"{len(names)} zips in {zips}, extracted to {extracted}")
    return out + check_tree(extracted, src / "skills", names)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--routes", default=",".join(ROUTES))
    ap.add_argument("--keep", type=Path, help="install under this directory and keep it")
    args = ap.parse_args()
    routes = [r for r in args.routes.split(",") if r]
    unknown = set(routes) - set(ROUTES)
    if unknown:
        ap.error(f"unknown route(s): {', '.join(sorted(unknown))}")

    base = args.keep.resolve() if args.keep else Path(tempfile.mkdtemp(prefix="ai4bcm-installs-"))
    if base.exists() and any(base.iterdir()):
        ap.error(f"{base} is not empty: a check needs a clean folder")
    base.mkdir(parents=True, exist_ok=True)
    head = run(["git", "rev-parse", "--short", "HEAD"], REPO).strip()
    if run(["git", "status", "--porcelain", "--untracked-files=no"], REPO).strip():
        print("note: the working tree has uncommitted changes; this checks HEAD only")
    print(f"checking HEAD {head} of {REPO} in {base}")

    failed = False
    for route in routes:
        work = base / route
        src = work / "clone"
        run(["git", "clone", "-q", "--no-hardlinks", str(REPO), str(src)], base)
        run(["git", "checkout", "-q", "--detach", head], src)
        names = bp.skill_names(src)
        print(f"\n== route {route}")
        try:
            lines = {"claude": route_claude, "skills": route_skills, "chatgpt": route_chatgpt}[route](
                src, work, names)
        except (RuntimeError, OSError, KeyError, subprocess.TimeoutExpired) as exc:
            lines = [f"FAIL {route}: {exc}"]
        for line in lines:
            print(line)
        failed |= any(line.startswith("FAIL") for line in lines)

    if not args.keep:
        shutil.rmtree(base, ignore_errors=True)
    print(f"\n{'RED' if failed else 'GREEN'}: {', '.join(routes)} at {head}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
