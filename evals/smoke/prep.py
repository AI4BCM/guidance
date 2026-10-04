#!/usr/bin/env python3
"""prep.py: build the owner's smoke-test bundle (ticket 69) from the eval kit.

One folder per step, all in one zip the owner downloads to his laptop:

  ai4bcm-smoke/
    README.txt, hard-rows.md
    chatgpt-upload/<skill>.zip        the ChatGPT uploads (build_chatgpt_package.write_zips)
    chatgpt/NN-<skill>-<case>/        request.txt, request-after-name.txt, turns.txt, case.md, files/
    copilot/NN-<skill>-<case>/        request.txt, turns.txt, case.md, workspace/
                                      workspace/ = the attachments + .agents/skills/<all ten packages>,
                                      what `npx skills add <repo>/skills -s '*' -a github-copilot --copy`
                                      writes (tools/check_installs.py: byte for byte the package)

The request is copied verbatim from `evals/<skill>/cases.md`; turns.txt holds the case's bold-led
lines (data class, intake answer, scripted turns) verbatim. Grading material (case.md) sits beside
the workspace, never inside it, so Copilot cannot read the checks.

Also writes steps.json (read by wizard.sh) next to the folder. Never edits the repository:
it runs `build_chatgpt_package.py --check` and refuses on drift instead of regenerating skills/.

  prep.py --out DIR      build DIR/ai4bcm-smoke-<commit>/ and DIR/ai4bcm-smoke-<commit>.zip
                         (prints the zip path on the last line)
"""
import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
EVALS = REPO / "evals"

# The ten job cases, in the direction note's build order, then the two hardest other cases
# (wizard.sh header says why these two).
JOBS = ["prepare-bia", "check-against-bia", "ask-ai4bcm", "challenge-my-plan", "learn-bcm",
        "check-against-standards", "role-card", "red-team-assumptions", "debrief-to-action",
        "check-my-ai-tool"]
CASES = [(s, 1, "job") for s in JOBS] + [("check-against-standards", 2, "never-alone"),
                                          ("ask-ai4bcm", 3, "F2")]
# hard-rows.md, "n/a when": H1 and H6 need material; H7 needs a draft meant for a document
# (a route and a lesson are not).
NO_DRAFT = {"ask-ai4bcm", "learn-bcm"}
CLIENTS = [("chatgpt", "ChatGPT"), ("copilot", "GitHub Copilot")]


def kit_commit() -> str:
    out = subprocess.run(["git", "-C", str(REPO), "log", "-1", "--format=%h", "--", "skills", "evals",
                          ":(exclude)evals/smoke"], capture_output=True, text=True, check=True)
    return out.stdout.strip()


def bold_items(lines: list[str]) -> list[str]:
    """Bold-led paragraphs: a line starting with ** opens one, it runs to a blank line or the next."""
    items, cur = [], None
    for line in lines:
        if line.startswith("**"):
            if cur:
                items.append(cur)
            cur = line
        elif not line.strip() or line.startswith(("|", "```", "#")):
            if cur:
                items.append(cur)
            cur = None
        elif cur is not None:
            cur += "\n" + line
    if cur:
        items.append(cur)
    return items


def parse_cases(skill: str) -> tuple[list[str], dict[int, list[str]]]:
    lines = (EVALS / skill / "cases.md").read_text(encoding="utf-8").splitlines()
    header, sections, cur = [], {}, None
    for line in lines:
        m = re.match(r"^## (\d+)\.", line)
        if m:
            cur = int(m.group(1))
            sections[cur] = [line]
        elif line.startswith("## "):
            cur = -1
        elif cur is None:
            header.append(line)
        elif cur > 0:
            sections[cur].append(line)
    return header, sections


def request_of(section: list[str]) -> str | None:
    text = "\n".join(section)
    m = re.search(r"```text\n(.*?)\n```", text, re.S)
    return m.group(1) if m else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()

    chk = subprocess.run([sys.executable, str(REPO / "tools" / "build_chatgpt_package.py"), "--check"],
                         capture_output=True, text=True)
    if chk.returncode:
        sys.stderr.write(chk.stdout + chk.stderr + "\nprep: skills/ has drifted; the builder regenerates "
                         "it (build_chatgpt_package.py) and commits before the sitting.\n")
        return 1

    commit = kit_commit()
    name = f"ai4bcm-smoke-{commit}"
    out = args.out.resolve()
    base = out / name
    root = base / "ai4bcm-smoke"
    if base.exists():
        shutil.rmtree(base)
    root.mkdir(parents=True)

    spec = importlib.util.spec_from_file_location("bcp", REPO / "tools" / "build_chatgpt_package.py")
    bcp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bcp)
    bcp.write_zips(REPO, root / "chatgpt-upload")

    shutil.copy(EVALS / "hard-rows.md", root / "hard-rows.md")
    steps = []
    n = 0
    for client, client_name in CLIENTS:
        for skill, case_no, label in CASES:
            n += 1
            header, sections = parse_cases(skill)
            section = sections[case_no]
            request = request_of(section) or request_of(sections[1])
            assert request, f"{skill} case {case_no}: no request"
            files_dir = EVALS / skill / "files"
            names = sorted({f for f in re.findall(r"[\w.-]+\.md", request)
                            if (files_dir / f).is_file()})
            pasted = "\n---\n" in request
            material = bool(names) or pasted
            folder = f"{n:02d}-{skill}-{label}"
            step_dir = root / client / folder
            step_dir.mkdir(parents=True)
            (step_dir / "request.txt").write_text(request + "\n", encoding="utf-8")
            if client == "chatgpt":
                rest = re.sub(rf"^/{re.escape(skill)}\s*", "", request)
                (step_dir / "request-after-name.txt").write_text(rest + "\n", encoding="utf-8")
                att_dir = step_dir / "files"
            else:
                att_dir = step_dir / "workspace"
                shutil.copytree(REPO / "skills", att_dir / ".agents" / "skills")
            att_dir.mkdir(exist_ok=True)
            for f in names:
                shutil.copy(files_dir / f, att_dir / f)
            head_items = [i for i in bold_items(header) if not i.startswith("**Files** (")]
            case_items = [i for i in bold_items(section)
                          if not i.startswith(("**Request (exact):**", "**From `units/prompts"))]
            turns = ("For this skill (evals/%s/cases.md, header):\n\n" % skill
                     + "\n\n".join(head_items or ["(nothing)"])
                     + "\n\nFor this case (case %d; where it differs from the header, the case wins):\n\n"
                     % case_no + "\n\n".join(case_items or ["(no scripted turns)"]) + "\n")
            (step_dir / "turns.txt").write_text(turns, encoding="utf-8")
            (step_dir / "case.md").write_text(
                "\n".join(header + section) + "\n", encoding="utf-8")
            na = {}
            if not material:
                na["H1"] = na["H6"] = "no material attached or pasted"
            if skill in NO_DRAFT:
                na["H7"] = "a route or a lesson, no draft meant for a document"
            steps.append({"id": f"{client}-{folder}", "n": n, "client": client,
                          "client_name": client_name, "skill": skill, "case": case_no,
                          "label": label, "folder": f"ai4bcm-smoke/{client}/{folder}",
                          "files": names, "pasted": pasted, "na": na})

    (root / "README.txt").write_text(
        f"AI4BCM skills smoke test, ticket 69. Kit and packages at commit {commit}.\n"
        "Run the wizard on brain; it tells you which folder each step uses.\n"
        "chatgpt-upload/: one zip per skill to upload to ChatGPT.\n"
        "chatgpt/NN-*/: request.txt (verbatim), request-after-name.txt (paste after the @skill mention),\n"
        "  turns.txt (what to answer), files/ (attach these), case.md (the case's checks, for you).\n"
        "copilot/NN-*/: open workspace/ in VS Code (it holds the attachments and .agents/skills/);\n"
        "  request.txt, turns.txt and case.md stay outside it so Copilot cannot read the checks.\n",
        encoding="utf-8")
    manifest = {"commit": commit, "bundle": f"{name}.zip", "steps": steps}
    (base / "steps.json").write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")

    zpath = out / f"{name}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(root.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(base))
    print(f"{len(steps)} steps, commit {commit}")
    print(zpath)
    return 0


if __name__ == "__main__":
    sys.exit(main())
