#!/usr/bin/env python3
"""Build machine-readable chunks from the AI4BCM guidance units (guidance/ submodule).

The July snapshot (`addendum-clean.md` + `knowledge/*.md`) and its `ppN-section`
identifier scheme were retired on 2026-09-10, publish-and-audit ticket 05. Chunk ids
are now keyed on the unit path and its heading — `stages/analysis.md` `## Method`
becomes `stages-analysis-method` — because a chunk id is a public URL and the citation
on an answer, and no GPG Professional Practice code appears in the guidance.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path


_HERE = Path(__file__).resolve().parent  # file-relative defaults (C15, 2026-08-18)
_REPO = _HERE.parent  # tools/ lives beside units/, literature/ and releases/ (kb-move 02)
DEFAULT_UNITS_DIR = _REPO / "units"
DEFAULT_RELEASES_DIR = _REPO / "releases"
DEFAULT_DATA_DIR = _REPO / "data"
DEFAULT_SOURCES_FILE = _HERE / "sources.json"
PUBLIC_BASE_URL = "https://agent.ai4bcm.org/demo/kb"


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
META_RE = re.compile(r"<!--\s*meta:\s*(.+?)\s*-->")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RETIRED_PP_RE = re.compile(r"\bpp[1-6]\b", re.I)

# Navigation files: the vault keeps three index.md files that never travel to the repo,
# and prompts/README.md is a unit. Anything else under units/ is content.
SKIP_FILENAMES = {"index.md"}

# Heading title → section_type. The stage units all carry the same seven headings; the
# two extra ones (analysis' Risk assessment, govern's Learning the practice, embed's Case
# studies and scheduled awareness) fall through to the unit default.
SECTION_TYPES = {
    "situation": "situation",
    "typical ai uses": "typical_uses",
    "minimum controls": "minimum_controls",
    "method": "method",
    "prompts": "prompts",
    "case example": "case_example",
    "level": "level",
}

# Routing metadata the units do not state in their own frontmatter. Values are the ones
# the retired snapshot used for the same subject matter, so `bcm_process` still reaches
# JOURNEY_FOR_PROCESS in guidance_tools and a fetch still hints the BIA journey.
# unit slug → (section_type default, bcm_process, output_type)
UNIT_DEFAULTS: dict[str, tuple[str, str, str]] = {
    "principles": ("principle", "ai-governance", "governance"),
    "levels": ("section", "adoption", "guidance"),
    "data-rules": ("section", "data-handling", "governance"),
    "tools": ("comparison", "tool-selection", "tool-selection"),
    "workflow-design": ("workflow", "workflow-design", "workflow"),
    "glossary": ("glossary", "terminology", "definition"),
    "references": ("reference", "reference", "reference"),
    "stages-govern": ("section", "bcms-governance", "guidance"),
    "stages-embed": ("section", "awareness", "guidance"),
    "stages-analysis": ("section", "bia,risk-assessment", "guidance"),
    "stages-design": ("section", "solutions-design", "guidance"),
    "stages-implement": ("section", "plan-management", "guidance"),
    "stages-validate": ("section", "exercise,validation", "guidance"),
    "prompts-readme": ("prompt", "prompting", "prompt"),
    "prompts-draft": ("prompt", "drafting", "prompt"),
    "prompts-review": ("prompt", "drafting,review", "prompt"),
    "prompts-bia": ("prompt", "bia", "prompt"),
    "prompts-awareness": ("prompt", "awareness", "prompt"),
    "prompts-exercise": ("prompt", "exercise", "prompt"),
    "prompts-management-report": ("prompt", "reporting", "prompt"),
    "prompts-evaluations": ("prompt", "prompting", "prompt"),
}

# `identify_ai_risks` reads this type. In the units the never-alone list is principle 4;
# nothing else carries it.
DO_NOT_USE_IDS = {"principles-4-what-ai-never-does-alone"}

# Types the units are expected to supply. `faq` and the old per-tool `comparison` pages
# went with the snapshot; the FAQ has no home in the units (recorded as a guidance finding
# by ticket 05).
REQUIRED_SECTION_TYPES = frozenset({"prompt", "workflow", "do_not_use", "comparison"})

# Every stage unit owes these four: the BIA journey cites them.
STAGE_UNITS = ("govern", "embed", "analysis", "design", "implement", "validate")
STAGE_REQUIRED_SECTIONS = ("typical-ai-uses", "minimum-controls", "method", "level")


# --- The source registry (improvements ticket 05, 2026-09-10) --------------------------
#
# Nothing becomes a served chunk without its terms. Every input file must be claimed by a
# row in sources.json, and only licence class A -- an open licence permitting inclusion
# with attribution, the audit's R10 vocabulary -- may enter the chunks at all. The other
# classes are refused with the reason, so a source is quoted or cited in a unit's own text
# rather than silently republished as our bytes.
#
#   A              open licence permitting inclusion with attribution
#   A-share-alike  open, but share-alike against the guidance's CC BY (OWASP): quote, never chunk
#   B              free to read and quotable with attribution
#   C              citation only
#   D              unverified
LICENCE_CLASSES = ("A", "A-share-alike", "B", "C", "D")
CHUNKABLE_CLASSES = ("A",)
SOURCE_FIELDS = ("id", "title", "edition", "licence", "licence_class", "citation", "paths")
RELEASE_SENTINEL = "@release"  # edition: the guidance's own edition IS the release tag


@dataclass(frozen=True)
class Source:
    id: str
    title: str
    edition: str
    licence: str
    licence_class: str
    citation: str
    paths: tuple[str, ...]
    publisher: str = ""

    def edition_for(self, release_tag: str) -> str:
        return release_tag if self.edition == RELEASE_SENTINEL else self.edition

    def citation_for(self, source_file: str, release_tag: str) -> str:
        return (
            self.citation
            .replace("{edition}", self.edition_for(release_tag))
            .replace("{source_file}", source_file)
        )


def load_sources(path: Path) -> tuple[Source, ...]:
    """Read sources.json, refusing a row that does not carry its own terms.

    A row missing any of SOURCE_FIELDS, or carrying a licence class outside the audit's
    vocabulary, is a build error: an unterminated source is exactly what this registry
    exists to keep out of the knowledge base.
    """
    if not path.is_file():
        raise SystemExit(f"no source registry at {path}")
    rows = json.loads(path.read_text(encoding="utf-8")).get("sources", [])
    if not rows:
        raise SystemExit(f"source registry {path} lists no sources")
    sources: list[Source] = []
    for row in rows:
        missing = [f for f in SOURCE_FIELDS if not row.get(f)]
        if missing:
            raise SystemExit(
                f"source {row.get('id', '<unnamed>')!r} in {path}: "
                f"missing required field(s): {', '.join(missing)}"
            )
        if row["licence_class"] not in LICENCE_CLASSES:
            raise SystemExit(
                f"source {row['id']!r}: unknown licence_class {row['licence_class']!r} "
                f"(one of {', '.join(LICENCE_CLASSES)})"
            )
        sources.append(
            Source(
                id=row["id"],
                title=row["title"],
                edition=row["edition"],
                licence=row["licence"],
                licence_class=row["licence_class"],
                citation=row["citation"],
                paths=tuple(row["paths"]),
                publisher=row.get("publisher", ""),
            )
        )
    ids = [s.id for s in sources]
    if len(set(ids)) != len(ids):
        raise SystemExit(f"duplicate source ids in {path}: {', '.join(sorted(ids))}")
    return tuple(sources)


def source_for(source_file: str, sources: tuple[Source, ...]) -> Source:
    """The registry row claiming this input file, or a build error naming the file.

    Patterns are matched with fnmatch, where `*` crosses directory separators, so
    `units/*` claims the whole unit tree.
    """
    for source in sources:
        if any(fnmatch.fnmatchcase(source_file, pattern) for pattern in source.paths):
            if source.licence_class not in CHUNKABLE_CLASSES:
                raise SystemExit(
                    f"{source_file}: source {source.id!r} is licence class "
                    f"{source.licence_class} ({source.licence}) and may not enter the chunks. "
                    f"Class {'/'.join(CHUNKABLE_CLASSES)} only; quote or cite it in a unit instead."
                )
            return source
    raise SystemExit(
        f"no registered source for {source_file} — add a row to sources.json with an id, "
        f"edition, licence, licence_class and citation form before this file can be built"
    )


@dataclass
class Heading:
    level: int
    title: str
    line: int


@dataclass
class Chunk:
    id: str
    unit: str
    section_type: str
    title: str
    breadcrumb: str
    text: str
    url: str
    char_count: int
    release_tag: str
    # Source terms, from the registry: no chunk exists without them (ticket 05)
    source_id: str
    source_edition: str
    licence: str
    citation: str
    # Extended metadata (all optional; defaults allow un-annotated chunks to build cleanly)
    bcm_process: str = ""
    ai_capability: str = ""
    risk_level: str = ""
    confidentiality: str = ""
    intended_user: str = ""
    output_type: str = ""
    mode: str = ""
    related_controls: list[str] = field(default_factory=list)
    related_examples: list[str] = field(default_factory=list)
    source_file: str = ""


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"


def title_key(title: str) -> str:
    return re.sub(r"\s+", " ", title.lower().strip())


def unit_slug(path: Path, units_dir: Path) -> str:
    """`units/stages/analysis.md` → `stages-analysis`; `units/prompts/README.md` → `prompts-readme`."""
    rel = path.relative_to(units_dir).with_suffix("")
    return "-".join(slugify(part) for part in rel.parts)


def parse_sections(text: str) -> list[tuple[Heading, str]]:
    lines = text.splitlines()
    headings: list[Heading] = []
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            headings.append(Heading(len(match.group(1)), match.group(2).strip(), idx))

    sections: list[tuple[Heading, str]] = []
    for pos, heading in enumerate(headings):
        end = headings[pos + 1].line if pos + 1 < len(headings) else len(lines)
        body = "\n".join(lines[heading.line + 1 : end]).strip()
        if body:
            sections.append((heading, body))
    return sections


def extract_meta(body: str) -> tuple[dict[str, str], str]:
    """Extract the first <!-- meta: key=val --> comment from body.

    Returns (meta_dict, body_with_comment_removed). All meta fields are optional.
    """
    lines = body.split("\n")
    meta: dict[str, str] = {}
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        m = META_RE.search(stripped)
        if m:
            for pair in m.group(1).split():
                if "=" in pair:
                    k, _, v = pair.partition("=")
                    meta[k.strip()] = v.strip()
            lines.pop(i)
            return meta, "\n".join(lines).strip()
        break  # only check the first non-empty line
    return meta, body


def release_tag_from(releases_dir: Path) -> str:
    """The tag every chunk is stamped with, read from the guidance release manifest.

    One manifest, one tag. Two manifests or none is a build error rather than a guess:
    a citation naming a tag has to name the same text everywhere.
    """
    manifests = sorted(releases_dir.glob("*.json")) if releases_dir.is_dir() else []
    if len(manifests) != 1:
        raise SystemExit(
            f"expected exactly one release manifest in {releases_dir}, found {len(manifests)}"
        )
    tag = str(json.loads(manifests[0].read_text(encoding="utf-8")).get("tag", "")).strip()
    if not tag:
        raise SystemExit(f"release manifest {manifests[0]} carries no tag")
    return tag


def build_unit_chunks(
    text: str, unit: str, source_file: str, release_tag: str, source: Source
) -> list[Chunk]:
    """Build chunks from one guidance unit.

    The H1 section is the unit itself; every deeper heading hangs off it. The unit's
    `<!-- meta -->` comment is read for `version` and stripped from the text; its `pp`
    field is deliberately ignored — the Professional Practice scheme was retired with the
    snapshot it keyed.
    """
    default_type, bcm_process, output_type = UNIT_DEFAULTS.get(unit, ("section", "", ""))
    chunks: list[Chunk] = []
    seen: dict[str, int] = {}

    # The unit title comes from the raw text, not from the parsed sections: a stage unit's H1
    # is followed straight by `## Situation`, so it has no body of its own and never reaches
    # parse_sections — which used to leave every breadcrumb reading "Situation > Level".
    h1_title = next((m.group(2).strip() for line in text.splitlines()
                     if (m := HEADING_RE.match(line)) and len(m.group(1)) == 1), unit)

    for heading, body in parse_sections(text):
        meta, clean_body = extract_meta(body)

        if heading.level == 1:
            base_id = unit
            breadcrumb = heading.title
        else:
            base_id = f"{unit}-{slugify(heading.title)}"
            breadcrumb = f"{h1_title} > {heading.title}"

        count = seen.get(base_id, 0)
        seen[base_id] = count + 1
        chunk_id = base_id if count == 0 else f"{base_id}-{count + 1}"

        # The H1 is the unit itself and takes the unit's own type; only deeper headings
        # are read against the shared stage-section vocabulary.
        section_type = meta.get("section_type") or (
            default_type
            if heading.level == 1
            else SECTION_TYPES.get(title_key(heading.title), default_type)
        )
        if chunk_id in DO_NOT_USE_IDS:
            section_type = "do_not_use"

        chunk_text = f"{breadcrumb}\n\n{clean_body}".strip()
        related_controls = [c.strip() for c in meta.get("controls", "").split(",") if c.strip()]
        related_examples = [e.strip() for e in meta.get("examples", "").split(",") if e.strip()]

        chunks.append(
            Chunk(
                id=chunk_id,
                unit=unit,
                section_type=section_type,
                title=heading.title,
                breadcrumb=breadcrumb,
                text=chunk_text,
                url=f"{PUBLIC_BASE_URL}/{chunk_id}/",
                char_count=len(chunk_text),
                release_tag=release_tag,
                source_id=source.id,
                source_edition=source.edition_for(release_tag),
                licence=source.licence,
                citation=source.citation_for(source_file, release_tag),
                bcm_process=meta.get("bcm_process", bcm_process),
                ai_capability=meta.get("capability", ""),
                risk_level=meta.get("risk", ""),
                confidentiality=meta.get("confidentiality", ""),
                intended_user=meta.get("user", ""),
                output_type=meta.get("output", output_type),
                mode=meta.get("mode", ""),
                related_controls=related_controls,
                related_examples=related_examples,
                source_file=source_file,
            )
        )
    return chunks


def build_all(
    units_dir: Path,
    release_tag: str,
    sources: tuple[Source, ...] | None = None,
    extra_dirs: tuple[Path, ...] = (),
) -> list[Chunk]:
    """Chunk the guidance units, plus any extra source directory given on the command line.

    A file's registry key is its path relative to the *parent* of the directory it was
    found in, so `guidance/units/principles.md` is `units/principles.md` and a literature
    directory beside it is `literature/<source>/<file>.md`. That is the path ticket 08's
    class A sources are registered under, and an unregistered one stops the build.
    """
    if sources is None:
        sources = load_sources(DEFAULT_SOURCES_FILE)
    chunks: list[Chunk] = []
    for root in (units_dir, *extra_dirs):
        for md_file in sorted(root.rglob("*.md")):
            if md_file.name.lower() in SKIP_FILENAMES:
                continue
            source_file = str(md_file.relative_to(root.parent))
            chunks.extend(
                build_unit_chunks(
                    md_file.read_text(encoding="utf-8"),
                    unit_slug(md_file, root),
                    source_file,
                    release_tag,
                    source_for(source_file, sources),
                )
            )
    return chunks


def build_index(chunks: list[Chunk], release_tag: str) -> dict[str, object]:
    return {
        "title": "AI4BCM guidance knowledge index",
        "release_tag": release_tag,
        "chunk_count": len(chunks),
        "topics": [
            {
                "id": chunk.id,
                "title": chunk.title,
                "breadcrumb": chunk.breadcrumb,
                "unit": chunk.unit,
                "section_type": chunk.section_type,
                "url": chunk.url,
            }
            for chunk in chunks
        ],
    }


def validate(chunks: list[Chunk], release_tag: str) -> None:
    # The registry check runs first: a chunk with no terms is the one defect that must
    # never reach the served corpus, whatever else is wrong with the build.
    unsourced = sorted(
        chunk.id
        for chunk in chunks
        if not (chunk.source_id and chunk.source_edition and chunk.licence and chunk.citation)
    )
    if unsourced:
        raise SystemExit(f"chunks without source terms: {', '.join(unsourced[:10])}")

    ids = {chunk.id for chunk in chunks}

    required = {
        f"stages-{stage}-{section}"
        for stage in STAGE_UNITS
        for section in STAGE_REQUIRED_SECTIONS
    }
    missing = sorted(required - ids)
    if missing:
        raise SystemExit(f"missing required chunks: {', '.join(missing)}")

    # The upper bound was 300 while the corpus was the guidance units alone. Improvements
    # ticket 08 added the class A literature beside them (EUR-Lex, UK Cabinet Office, the
    # Swiss minimum standard and the rest), and one regulation is 65 chunks on its own, so
    # the bound is now a sanity check on a runaway build rather than a count of the units.
    if not 45 <= len(chunks) <= 2000:
        raise SystemExit(f"unexpected chunk count: {len(chunks)}")

    # The retired scheme must not come back through a heading or a meta override.
    retired = sorted(cid for cid in ids if RETIRED_PP_RE.search(cid))
    if retired:
        raise SystemExit(f"retired PP identifiers in chunk ids: {', '.join(retired)}")

    seen_ids = Counter(chunk.id for chunk in chunks)
    duplicated = sorted(cid for cid, n in seen_ids.items() if n > 1)
    if duplicated:
        raise SystemExit(f"duplicate chunk ids across sources: {', '.join(duplicated[:10])}")

    malformed = sorted(cid for cid in ids if not ID_RE.match(cid))
    if malformed:
        raise SystemExit(f"malformed chunk ids: {', '.join(malformed)}")

    untagged = sorted(chunk.id for chunk in chunks if chunk.release_tag != release_tag)
    if untagged:
        raise SystemExit(f"chunks without the release tag: {', '.join(untagged[:10])}")

    bad = [chunk.id for chunk in chunks if "{#" in chunk.text or "Table of content" in chunk.text]
    if bad:
        raise SystemExit(f"cleaning artifacts remain in chunks: {', '.join(bad[:10])}")

    # Soft check: the section types the server's retrieval helpers filter on.
    present_types = {chunk.section_type for chunk in chunks}
    for st in sorted(REQUIRED_SECTION_TYPES):
        if st not in present_types:
            print(f"note: no chunks of type '{st}' — a unit that carried it may have moved")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--units-dir", type=Path, default=DEFAULT_UNITS_DIR)
    parser.add_argument("--releases-dir", type=Path, default=DEFAULT_RELEASES_DIR)
    parser.add_argument("--release-tag", default="")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES_FILE,
                        help="the source registry (identifier, edition, licence, citation)")
    parser.add_argument("--source-dir", type=Path, action="append", default=[],
                        help="an extra source directory to chunk (repeatable); its files are "
                             "registered under <dirname>/... in sources.json")
    parser.add_argument("--dry-run", action="store_true",
                        help="build and validate, write nothing")
    args = parser.parse_args()

    if not args.units_dir.is_dir():
        raise SystemExit(
            f"no guidance units at {args.units_dir} — the guidance submodule is not checked out "
            "(git submodule update --init --recursive)"
        )

    release_tag = args.release_tag or release_tag_from(args.releases_dir)
    sources = load_sources(args.sources)
    chunks = build_all(args.units_dir, release_tag, sources, tuple(args.source_dir))

    validate(chunks, release_tag)
    if args.dry_run:
        by_source = Counter(chunk.source_id for chunk in chunks)
        print(f"dry run: {len(chunks)} chunks ({release_tag}), nothing written")
        for source_id, count in sorted(by_source.items()):
            source = next(s for s in sources if s.id == source_id)
            print(f"  {count:4d}  {source_id}  {source.edition_for(release_tag)}  "
                  f"{source.licence} (class {source.licence_class})")
        return 0
    args.data_dir.mkdir(parents=True, exist_ok=True)
    (args.data_dir / "chunks.json").write_text(
        json.dumps([asdict(chunk) for chunk in chunks], indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (args.data_dir / "index.json").write_text(
        json.dumps(build_index(chunks, release_tag), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(chunks)} chunks ({release_tag}) to {args.data_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
