# The chunk-id citation contract

**Producer:** `AI4BCM/guidance` — this repository mints chunk identifiers and publishes the corpus.
**Consumers:** anything outside this repository that names a chunk id in a file it ships. Today that
is `KoGerner/workflow-design` (`run-bia.yaml`, 16 citations across 9 distinct ids).
**Contract version:** 2. **Written:** 2026-09-10. **Revised:** 2026-09-12 — the citation base moved
from `agent.ai4bcm.org/demo/kb` to this repository on GitHub.

Until 2026-09-10 the citing file and the corpus that answered it lived in one working tree, so the
coupling needed no words. They are now in two organisations on two release cadences. This file is
what replaces the tree.

## What a chunk id is, and where it comes from

`tools/build_chunks.py` mints one chunk per Markdown heading under `units/`. The id is the unit's
slug, then the slugified heading title, joined with `-`; a repeated title inside one unit gets a
`-2`, `-3` suffix. `units/stages/analysis.md`'s `## Method` heading is therefore
`stages-analysis-method`.

**That rule is why most ids are not safe to cite.** Reword a heading and the id changes, silently,
in the next build. The set below exists so a consumer has ids that do not behave that way.

## The reserved set — 26 ids

These ids are guaranteed. `tools/build_chunks.py` refuses to build a corpus that is missing any of
them (`RESERVED_CHUNK_IDS`, checked in `validate()`), so an unpublishable corpus is the failure mode
rather than a published corpus with a dead citation in it.

**The six stage units × four sections — 24 ids.** For each of `govern`, `embed`, `analysis`,
`design`, `implement`, `validate`:

```
stages-<stage>-typical-ai-uses
stages-<stage>-minimum-controls
stages-<stage>-method
stages-<stage>-level
```

**Two prompt units — 2 ids.** `prompts-bia`, `prompts-review`.

The reserved set is deliberately the set that has a consumer, not every id that could have one.
To add to it, open an issue on this repository naming the citing file; adding a row costs one line
and a test run.

## What "stable" means

**Within one release tag, an id is frozen.** Same tag ⇒ same id ⇒ same text. `releases/<tag>.json`
pins the sha256 of every unit file in that tag, so "same tag, changed bytes" is a detectable defect
rather than an opinion.

A draft for the next tag lives in `releases/drafts/<tag>.json`. It moves up to `releases/` at the
mint. The previous tag's manifest stays in the repository but moves out of `releases/` at the same
time, because the corpus builder stamps every chunk from the one manifest in `releases/` and refuses
two. It goes to `releases/archive/<tag>.json`, which the builder's non-recursive `releases/*.json`
glob does not see; `2026.09` moved there at the `2026.09.1` mint.

**Across release tags, the reserved ids survive.** A reserved id is never renamed or removed without
a new version of this contract and a `CHANGELOG.md` entry naming the consumers that must move. Every
other id may change whenever an editor rewords a heading, and carries no promise at all.

## What a consumer may assume

- **A chunk's citation is this repository, pinned to the release tag, anchored on the chunk's
  heading** — `https://github.com/AI4BCM/guidance/blob/<tag>/<source_file>#<anchor>`, e.g.
  `https://github.com/AI4BCM/guidance/blob/2026.09.1/units/stages/govern.md#level`.
  Measured 2026-09-12: all 26 reserved ids and a sample of the literature answer 200 with the
  anchor landing on the named heading.
- **The anchor is GitHub's, not the chunk id's.** GitHub lowercases a heading, deletes its
  punctuation rather than hyphenating it (`Client/Server` → `clientserver`, `TT&E` → `tte`) and
  suffixes a repeat `-1`, `-2`, where a repeated chunk id gets `-2`, `-3`. The two are different
  strings for the same heading and neither can be derived from the other. `build_chunks.py`
  mints the anchor with `github_anchors()`, verified against GitHub's own rendering of all 29
  source files at `2026.09.1` — 436 of 436 headings, duplicates included.
- The corpus's own release tag is served, unauthenticated, at `https://mcp.ai4bcm.org/health` —
  `release_tag`, alongside `chunks` and `built_at`.
- **The whole index is served, unauthenticated, at `https://mcp.ai4bcm.org/index.json`** — every
  chunk with its `id`, `title`, `breadcrumb`, `unit`, `section_type` and `url`, beside the
  `release_tag` and `chunk_count`. This contract is therefore checkable in one request rather
  than one per id. Version 1 left it unpublished; version 2 has to publish it, because a
  citation can no longer be constructed from an id.

## What a consumer may not assume

- **Chunk text is not stable.** Only the id is. A consumer that depends on wording is not covered.
- **`chunk_count` is not stable.** It was 96 units-only, then 383 once the class A literature was
  published on 2026-09-10. Never assert on it.
- **Non-reserved ids are not stable**, including every literature chunk.
- **A citation cannot be constructed from a chunk id.** It carries the source file and a GitHub
  anchor, neither of which is recoverable from the id. Version 1's shape,
  `<base>/<chunk-id>/`, could be built by string concatenation; this one cannot, and a consumer
  that tries will produce a URL that does not 404 — it silently lands at the top of some file.
  **Read the `url` from the index.** That is what the index is for, and it is now published.
- **A citation names one release, and only that release.** The tag is in the URL, so a citation
  written against `2026.09.1` keeps resolving after `2026.10` ships — GitHub keeps the tag — but
  it keeps showing the *old* text. A consumer that wants the current wording re-reads the index
  at the current tag. This is the trade the tag pin buys: a citation that never rots, and never
  silently updates either.

## Which side breaks, and who finds out

Three gates, earliest first. Each catches a case the next one cannot.

| # | Gate | Where | What it does |
|---|---|---|---|
| 1 | `RESERVED_CHUNK_IDS` in `validate()` | producer, build time | `build_chunks.py` exits 1; the corpus is never published |
| 2 | `startup_checks()` → `_journeys_map()` | consumer, process start | the BIA server refuses to start on an unknown cited id |
| 3 | `ai4bcm-citation-drift.sh` | brain, daily | resolves the live tag and every cited id; writes a line into the morning todos note |

**Gate 2 is kept deliberately.** `server.py` validates every journey's cites against its index before
uvicorn binds, and that predates this contract. It stays: it is the only gate that sees the citing
file and the corpus at the same time, and a BIA server whose journey cites a chunk it cannot fetch is
worse down than up.

**Gate 3 is what the move made necessary.** Gates 1 and 2 both need someone to run a build or start a
process. After the split, a corpus can be republished by AI4BCM and a citing file left untouched by
its own repository, and nothing in either repository would run. Gate 3 watches the *published*
surface instead, so the case that needs no commit on either side still reaches a human.

## Where the tag is named

`run-bia.yaml` carries `cites_release` at the top level — the tag its citations were checked
against. It is parsed (`Journey.cites_release`) and reported by the BIA server's `/health` as
`cites_release`, beside `corpus_release` read from the corpus index, and `cites_ok`.

**This is what fills the hole the move opened.** `/health` used to report `stale` by comparing
`chunks.json`'s build time against the mtimes of `units/**/*.md`. Those units are AI4BCM's now and
need not be checked out beside the BIA server, so that field went honest-but-empty:
`source_changed_at: null, stale: false`. It stops claiming to know something it cannot see, and
starts reporting something it can: which corpus release it is serving, and which one its journeys
were written against.

## The unit anchors — `pp=` and `cites=` — are not this contract's subject

Every unit's first line carries a `<!-- meta: ... -->` comment. Six stage units still carry `pp=1`
through `pp=6`, and 21 units carry a `cites=` field.

**Neither is a chunk id, and nothing reads either one.** `pp=` keyed the retired BCI Professional
Practice numbering; `build_chunks.build_unit_chunks()` documents that it is ignored, and
`validate()`'s `RETIRED_PP_RE` refuses any chunk id in which the scheme reappears — the hazard is
already closed. `cites=` names sections of the AI4BCM guidance document itself (`1.4.1`, `annex-b1`),
not chunks; grep over `tools/*.py` and `ask-ai4bcm/` finds no reader. `extract_meta()` strips the
whole comment before a chunk is built, so the anchors are invisible in the output.

**Removing them is therefore an editorial change, deferred — owner: Konstantin Gerner, as AI4BCM
guidance editor. Trigger: the next release tag after `2026.09`.** Two reasons it is not done here.
The unit files' sha256 are pinned in `releases/2026.09.json` (now `releases/archive/2026.09.json`), so editing them now would falsify the
manifest of a tag that is already live and serving. And `units/` has a second copy — the editorial
source in the vault, `02-Projects/ai4bcm/guidance-rewrite/units/` — so the edit is two trees, not
one, and belongs in an editing round rather than a plumbing one. At the next tag the manifest is
regenerated anyway and the edit is free.

## Changing this contract

Any change to the reserved set, the id-minting rule or the guarantee is a new contract version, an
entry in `CHANGELOG.md`, and a message to each consumer named at the top of this file.
