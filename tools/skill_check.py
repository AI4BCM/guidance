"""skill_check.py — the builder's gate for one AI4BCM skill: does `<name>/SKILL.md` have the shape?

A skill is the guidance's own definition made runnable (direction note 2026.11, "What a skill is"):
its stage's one control, the Method steps it performs, the Task choice prompt it wraps, what the
auditor must see, the reviewer, and the source behind each rule. This script checks the shape and
the provenance; whether the content runs the stage the way the guide says is the reviewer role's.

What it checks, each a line in the output, any FAIL makes the exit 1:

- frontmatter: `name` equals the folder, `description`, `license`, `disable-model-invocation: true`,
  `metadata.version`;
- a stage skill links `../preflight.md` (the router reads no files and drafts nothing);
- the body is at most 515 words (500 before 2026.11.1) (`ask-ai4bcm`, the router, 1,000);
- a stage skill carries the six headings in REQUIRED, and its Method holds a numbered list;
- every phrase in double quotes ("…" or “…”) of three words or more stands verbatim in `units/`.
  A line the skill tells the model to say is not a quote: write it as a `> ` blockquote;
- every citation under `## Sources` is found: `principle N` in `units/principles.md`, a
  `units/<file>.md` path (with `, <Heading>` a heading in it), or `<source> <locator>` matching a
  entry of `units/references.md` "Cited on these pages" ("Cited in the units" before 2026.11.1);
- every relative link resolves and none points at a heading (`#…`): skills link whole units;
- with `--package` (the default): `build_chatgpt_package.py --check` and
  `claude plugin validate . --strict`.

`--clean` adds the cleaner's checks: no word from `banned_words.txt`, no em-dash, and with
`--max-words N` no longer than the builder left it. `--review` checks the reviewer's verdict file
`evals/<name>/review.md` instead: a `Skill sha:` line matching the current SKILL.md, a `Stage unit:`
line, a table row `| One control | <skill line> | <verdict> |` and one `| Method N | … |` per
numbered step of that unit's Method, and no row whose cells say "missing".

Stdlib only, like the rest of `tools/`.

    python3 tools/skill_check.py prepare-bia
    python3 tools/skill_check.py prepare-bia --no-package     # shape only, no repo-wide checks
    python3 tools/skill_check.py prepare-bia --words           # print the body word count and exit
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ROUTER = "ask-ai4bcm"
MAX_WORDS = 515  # 500 until 2026.11.1; the owner allowed 515 for this release (2026-11-01): the print's longer headings
MAX_WORDS_ROUTER = 1000
MIN_QUOTE_WORDS = 3
REQUIRED = ("The one control", "Method", "Task choice", "For the auditor", "Reviewer", "Sources")
FRONTMATTER_KEYS = ("name", "description", "license", "disable-model-invocation")

QUOTE = re.compile(r"\"([^\"\n]+)\"|“([^”\n]+)”")
LINK = re.compile(r"\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*$", re.M)


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """The flat `key: value` frontmatter (nested keys as `parent.child`) and the body after it."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fields: dict[str, str] = {}
    parent = ""
    for line in text[4:end].splitlines():
        m = re.match(r"^(\s*)([\w-]+):\s*(.*)$", line)
        if not m:
            continue
        indent, key, value = m.groups()
        value = value.strip().strip('"')
        if indent:
            fields[f"{parent}.{key}"] = value
        else:
            parent = key
            fields[key] = value
    return fields, text[end + 5:]


def words(body: str) -> int:
    """Words a reader reads: link targets and markdown punctuation do not count."""
    body = LINK.sub("]", body)
    return len(re.findall(r"[\w’'][\w’'.,/-]*", body))


def normalise(text: str) -> str:
    """Compare text as a reader sees it: no emphasis marks, straight quotes, one space."""
    text = text.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    text = re.sub(r"[*`_]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def units_text(repo: Path) -> str:
    return normalise("\n".join(p.read_text(encoding="utf-8") for p in sorted((repo / "units").rglob("*.md"))))


def quotes(body: str, labels: bool = True) -> list[str]:
    """Double-quoted phrases of MIN_QUOTE_WORDS words or more, outside blockquotes and code.

    `labels=False` skips a list item that opens with a bold quoted label (`- **"…"**`): the router's on-ramps are the
    user's own words, not the guidance's, and `scripts/ai4bcm-router-routes.py` counts routes by exactly that form.
    """
    found = []
    for line in body.splitlines():
        if line.lstrip().startswith(">"):
            continue
        if not labels and re.match(r'\s*- \*\*"', line):
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for a, b in QUOTE.findall(line):
            phrase = a or b
            if len(phrase.split()) >= MIN_QUOTE_WORDS:
                found.append(phrase)
    return found


def quote_found(phrase: str, haystack: str) -> bool:
    """Every part of the phrase between ellipses stands in the units, in order."""
    pos = 0
    for part in re.split(r"\s*(?:…|\.\.\.)\s*", phrase):
        part = normalise(part).strip(" .,;:")
        if not part:
            continue
        pos = haystack.find(part, pos)
        if pos < 0:
            return False
        pos += len(part)
    return True


def sections(body: str) -> dict[str, str]:
    """Each `## ` section's text by heading."""
    out: dict[str, str] = {}
    parts = re.split(r"^##\s+(.+?)\s*$", body, flags=re.M)
    for i in range(1, len(parts), 2):
        out[parts[i]] = parts[i + 1]
    return out


def cited_rows(repo: Path) -> list[tuple[str, str]]:
    """(source cell, whole row) for each entry of references.md "Cited on these pages" (the print's heading
    since 2026.11.1, a bulleted list) or, before it, the table "Cited in the units"."""
    text = (repo / "units" / "references.md").read_text(encoding="utf-8")
    secs = sections(text)
    block = secs.get("Cited on these pages", secs.get("Cited in the units", ""))
    rows = []
    for line in block.splitlines():
        bullet = re.match(r"\s*-\s+\*\*(.+?)\*\*", line)
        if bullet:
            rows.append((normalise(bullet.group(1)), normalise(line)))
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] not in ("Source", "") and not set(cells[0]) <= set("-: "):
            rows.append((normalise(cells[0]), normalise(line)))
    return rows


def unit_headings(path: Path) -> set[str]:
    return {normalise(h) for h in HEADING.findall(path.read_text(encoding="utf-8"))}


def check_citation(cite: str, repo: Path, rows: list[tuple[str, str]]) -> str | None:
    """None when the citation is found, else why not."""
    cite = cite.strip().rstrip(".")
    m = re.fullmatch(r"(?i)principle\s+(\d+)", cite)
    if m:
        ok = any(h.startswith(f"{m.group(1)}.") for h in unit_headings(repo / "units" / "principles.md"))
        return None if ok else f"no principle {m.group(1)} in units/principles.md"
    m = re.fullmatch(r"`?(units/[\w./-]+\.md)`?(?:,\s*(.+))?", cite)
    if m:
        path = repo / m.group(1)
        if not path.exists():
            return f"{m.group(1)} does not exist"
        if m.group(2) and normalise(m.group(2)) not in unit_headings(path):
            return f"no heading {m.group(2)!r} in {m.group(1)}"
        return None
    m = re.fullmatch(r"(.+?)\s+((?:section\s+)?[\w.-]*\d[\w.-]*)", cite)
    name, locator = (m.group(1), m.group(2)) if m else (cite, "")
    locator = re.sub(r"(?i)^section\s+", "", locator)
    for source, row in rows:
        if normalise(name) in source and normalise(locator) in row:
            return None
    return f"no entry in references.md 'Cited on these pages' names {name!r}" + (f" with {locator!r}" if locator else "")


def citations(sources: str) -> list[str]:
    """`- <rule>: <cite>; <cite>` bullets; the part after the first colon holds the citations."""
    out = []
    for line in sources.splitlines():
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if not m:
            continue
        item = m.group(1)
        tail = item.split(":", 1)[1] if ":" in item else item
        out += [c.strip() for c in tail.split(";") if c.strip()]
    return out


def check_links(body: str, base: Path) -> list[str]:
    problems = []
    for target in LINK.findall(body):
        if re.match(r"^[a-z]+:", target):
            continue
        if "#" in target:
            problems.append(f"{target}: links a heading; link the whole unit")
            target = target.split("#", 1)[0]
            if not target:
                continue
        if not (base / target).exists():
            problems.append(f"{target}: does not resolve")
    return problems


def check(name: str, repo: Path = REPO, package: bool = True) -> list[tuple[bool, str]]:
    """Every check as (passed, line)."""
    results: list[tuple[bool, str]] = []
    path = repo / name / "SKILL.md"
    if not path.exists():
        return [(False, f"{name}/SKILL.md does not exist")]
    fields, body = split_frontmatter(path.read_text(encoding="utf-8"))

    missing = [k for k in FRONTMATTER_KEYS if not fields.get(k)]
    if fields.get("name") and fields["name"] != name:
        missing.append(f"name is {fields['name']!r}, folder is {name!r}")
    if fields.get("disable-model-invocation", "true") != "true":
        missing.append("disable-model-invocation is not true")
    if not fields.get("metadata.version"):
        missing.append("metadata.version")
    results.append((not missing, "frontmatter" + (f": {', '.join(missing)}" if missing else "")))

    if name != ROUTER:
        results.append(("../preflight.md" in body, "links ../preflight.md"))

    limit = MAX_WORDS_ROUTER if name == ROUTER else MAX_WORDS
    n = words(body)
    results.append((n <= limit, f"body {n} words (at most {limit})"))

    if name != ROUTER:
        secs = sections(body)
        absent = [h for h in REQUIRED if h not in secs]
        results.append((not absent, "required parts" + (f": missing {', '.join(absent)}" if absent else "")))
        if "Method" in secs:
            steps = re.findall(r"^\d+\.\s", secs["Method"], re.M)
            results.append((bool(steps), f"Method: {len(steps)} numbered steps"))
        if "Sources" in secs:
            rows = cited_rows(repo)
            cites = citations(secs["Sources"])
            bad = [f"{c}: {why}" for c in cites if (why := check_citation(c, repo, rows))]
            results.append((bool(cites) and not bad, f"citations: {len(cites)} found, {len(bad)} not"))
            results += [(False, f"  citation {b}") for b in bad]

    haystack = units_text(repo)
    qs = quotes(body, labels=name != ROUTER)
    bad_q = [q for q in qs if not quote_found(q, haystack)]
    results.append((not bad_q, f"quotes: {len(qs)} checked, {len(bad_q)} not in units/"))
    results += [(False, f"  not verbatim in units/: \"{q}\"") for q in bad_q]

    bad_links = check_links(body, path.parent)
    results.append((not bad_links, f"links: {len(LINK.findall(body))} checked"))
    results += [(False, f"  {b}") for b in bad_links]

    if package:
        for label, cmd in (
            ("package in sync", [sys.executable, str(repo / "tools" / "build_chatgpt_package.py"), "--check"]),
            ("claude plugin validate --strict", ["claude", "plugin", "validate", ".", "--strict"]),
        ):
            try:
                p = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, timeout=300)
                ok, out = p.returncode == 0, (p.stdout + p.stderr).strip()
            except (OSError, subprocess.TimeoutExpired) as e:
                ok, out = False, str(e)
            results.append((ok, label))
            if not ok:
                results += [(False, f"  {line}") for line in out.splitlines()[-15:]]
    return results


BANNED = Path(__file__).resolve().parent / "banned_words.txt"
REVIEW_ROW = re.compile(r"^\|\s*(One control|Method \d+)\s*\|(.*)\|\s*$", re.M | re.I)


def banned(repo: Path = REPO) -> list[str]:
    path = repo / "tools" / "banned_words.txt"
    path = path if path.exists() else BANNED
    return [w.strip() for w in path.read_text(encoding="utf-8").splitlines() if w.strip() and not w.startswith("#")]


def check_clean(name: str, repo: Path = REPO, max_words: int | None = None) -> list[tuple[bool, str]]:
    """The cleaner's extra checks: no banned word, no em-dash, not longer than the builder left it."""
    _, body = split_frontmatter((repo / name / "SKILL.md").read_text(encoding="utf-8"))
    results: list[tuple[bool, str]] = []
    low = body.lower()
    hits = [w for w in banned(repo) if re.search(rf"(?<![\w-]){re.escape(w)}(?![\w-])", low)]
    results.append((not hits, "banned words" + (f": {', '.join(hits)}" if hits else "")))
    dashes = body.count("—")
    results.append((dashes == 0, f"em-dashes: {dashes}"))
    if max_words is not None:
        n = words(body)
        results.append((n <= max_words, f"body {n} words, builder left {max_words}"))
    return results


def unit_method_steps(unit: Path, heading: str = "Method") -> int:
    return len(re.findall(r"^\d+\.\s", sections(unit.read_text(encoding="utf-8")).get(heading, ""), re.M))


def skill_method_steps(name: str, repo: Path = REPO) -> int:
    """Numbered steps of the skill's own `## Method`: the rows a review owes when its unit has no numbered Method."""
    _, body = split_frontmatter((repo / name / "SKILL.md").read_text(encoding="utf-8"))
    return len(re.findall(r"^\d+\.\s", sections(body).get("Method", ""), re.M))


def check_review(name: str, repo: Path = REPO) -> list[tuple[bool, str]]:
    """The reviewer's verdict file: of this SKILL.md, naming the one control and every Method step
    of its stage unit with the skill line that carries it, and no row marked missing."""
    review = repo / "evals" / name / "review.md"
    if not review.exists():
        return [(False, f"evals/{name}/review.md does not exist")]
    text = review.read_text(encoding="utf-8")
    results: list[tuple[bool, str]] = []
    sha = subprocess.run(["git", "hash-object", str(repo / name / "SKILL.md")],
                         capture_output=True, text=True).stdout.strip()
    m = re.search(r"^Skill sha:\s*([0-9a-f]{7,40})\s*$", text, re.M)
    results.append((bool(m) and sha.startswith(m.group(1)),
                    "review is of the current SKILL.md" + ("" if m else ": no 'Skill sha:' line")))
    m = re.search(r"^Stage unit:\s*`?(units/[\w./-]+\.md)`?(?:,\s*(.+?))?\s*$", text, re.M)
    unit = repo / m.group(1) if m else None
    heading = m.group(2) if m and m.group(2) else "Method"
    known = bool(unit and unit.exists()) and (heading == "Method" or heading in sections(unit.read_text(encoding="utf-8")))
    results.append((known, "stage unit named" + (f": {m.group(1)}" + (f", {heading}" if heading != "Method" else "") if m else ": no 'Stage unit:' line")))
    rows = REVIEW_ROW.findall(text)
    labels = {r[0].lower() for r in rows}
    results.append(("one control" in labels, "row: One control"))
    if known:
        n = unit_method_steps(unit, heading) or skill_method_steps(name, repo)
        absent = [f"Method {i}" for i in range(1, n + 1) if f"method {i}" not in labels]
        results.append((not absent, f"rows: Method 1 to {n}" + (f", missing {', '.join(absent)}" if absent else "")))
    empty = [r[0] for r in rows if len([c for c in r[1].split("|") if c.strip()]) < 2]
    results.append((not empty, "each row names the skill line and a verdict" + (f": not {', '.join(empty)}" if empty else "")))
    missing = [r[0] for r in rows if re.search(r"\bmissing\b", r[1].split("|")[-1], re.I)]
    results.append((not missing, "nothing missing" + (f": {', '.join(missing)}" if missing else "")))
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("name", help="the skill folder, e.g. prepare-bia")
    ap.add_argument("--repo", type=Path, default=REPO)
    ap.add_argument("--no-package", action="store_true", help="skip the repo-wide package and plugin checks")
    ap.add_argument("--words", action="store_true", help="print the body word count and exit")
    ap.add_argument("--clean", action="store_true", help="add the cleaner's checks")
    ap.add_argument("--max-words", type=int, help="with --clean: the builder's word count")
    ap.add_argument("--review", action="store_true", help="check evals/<name>/review.md only")
    args = ap.parse_args(argv)
    if args.words:
        _, body = split_frontmatter((args.repo / args.name / "SKILL.md").read_text(encoding="utf-8"))
        print(words(body))
        return 0
    repo = args.repo.resolve()
    if args.review:
        results = check_review(args.name, repo)
    else:
        results = check(args.name, repo, package=not args.no_package)
        if args.clean:
            results += check_clean(args.name, repo, args.max_words)
    for ok, line in results:
        print(("ok    " if ok else "FAIL  ") + line if not line.startswith("  ") else "      " + line.strip())
    failed = sum(1 for ok, line in results if not ok and not line.startswith("  "))
    print(f"{args.name}: {'green' if not failed else f'red, {failed} failing'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
