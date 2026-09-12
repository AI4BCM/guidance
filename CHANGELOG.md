# Changelog

Releases are named by calendar month, `YYYY.MM`. Each one is a git tag, and a manifest under
[`releases/`](releases/) resolves that tag to a commit and to a SHA-256 for every citable file, so
a reader who wants a unit as it stood at a release can prove they have the same bytes.

## How to cite a unit at a release

Name the release and the unit path:

> Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals,
> 2026.09, `units/stages/analysis.md`. CC BY 4.0.

The print edition carries the same release as its edition tag, so a citation of a printed page
names the release the same way and gives the sheet instead of the unit path. Where a claim needs
to be checkable rather than merely attributed, add the commit from the release's manifest:
`releases/<tag>.json` for the current release, `releases/archive/<tag>.json` for an earlier one.

Prompts move faster than the rest of the guidance. `units/prompts/` is the living part, so a
citation of a prompt without a release names nothing durable — cite the release or quote the
prompt in full.

## Citation contract version 2 — 2026-09-12

Not a release of the guidance: no unit changed, no chunk id changed, no chunk text changed. What
changed is **where a citation points.**

Until now every chunk carried `https://agent.ai4bcm.org/demo/kb/<chunk-id>/`. That base was
inherited, not chosen — until the 2026-09-10 split the corpus and the BIA product shared one tree,
and that is simply where the built pages landed. It is the *other* product's hostname, in the
other product's design system, under a `/demo/` tree that is now being retired, and a reader who
followed a citation from `ai4bcm.org` landed on a page that looked like someone else's product.

A citation is now this repository, pinned to the release tag, anchored on the chunk's heading:

```
https://github.com/AI4BCM/guidance/blob/2026.09.1/units/stages/govern.md#level
```

`data/index.json` is published at `https://mcp.ai4bcm.org/index.json`, unauthenticated, beside
`/health`. It has to be: a citation carries a source file and a GitHub anchor, so it can no longer
be built from a chunk id by string concatenation, and the index is where a consumer reads it.

**Consumers, and what each must do.**

| consumer | effect | action |
|---|---|---|
| `KoGerner/workflow-design` — `run-bia.yaml` | none. It cites chunk **ids**, and no id changed | none |
| the question box on `ai4bcm.org` (`bia-workflow` `/ask`) | the `url` in every answer's source list | rebuild its corpus; it runs its own copy of `build_chunks.py` |
| the connector on `mcp.ai4bcm.org` | `search` and `fetch` both return the new `url` | rebuild and restart |
| `brain`'s `ai4bcm-citation-drift.sh` | it probes the old base and will alarm daily once `/demo/` dies | repoint it at `/index.json` |
| anything holding a `/demo/kb/<id>/` link | the page is going away | read the `url` from `/index.json` |

The reserved set, the id-minting rule and the guarantee are all unchanged, so this is a version of
the contract rather than a version of the corpus. `CITATION-CONTRACT.md` carries the detail,
including why a GitHub anchor is not a chunk id and must never be derived from one.

## 2026.09.1

A point release in September, published ahead of the November final `2026.11` by owner decision
on 2026-09-11. `2026.09` stays exactly as minted (`1f137d3`), so everyone who cited it keeps the
text they cited. Its manifest moved to `releases/archive/2026.09.json`; `releases/2026.09.1.json`
is now the one manifest the corpus builder reads.

What changed:

- **The plain-English rewrite is the default text** of every unit and of the router: shorter
  declarative sentences in place of the earlier register. The guarded strings, the BIA vocabulary,
  the prompt fences and every citation stayed as they were.
- **A new maturity ladder.** The five levels are now `Ad hoc/Initial`, `Repeatable`, `Defined`,
  `Quantitatively managed` and `Optimised`, in the lineage of CMM/CMMI and cited as such. They
  replace the five earlier names, and the descriptions were rewritten to the process-maturity
  meaning. `units/levels.md`, the starting guide and every stage unit's `## Level` section changed
  with them.
- **The Quick Start** returns in the print edition, as a sheet after the cover.
- **The glossary** gained the terms a newcomer needs (AI, machine learning, prompt, invention,
  RPO; generative AI, LLM and RAG extended) and prints as its own sheet.
- "From prompt to team method" joins `units/prompts/README.md`.
- Every unit's `<!-- meta -->` anchor reads `version=2026.09.1`. The anchor is stripped before a
  chunk is built, so it changes no chunk id and no chunk text.

**No reserved id changed.** All 26 ids of `CITATION-CONTRACT.md` are still built, and so are the 9
distinct ids `run-bia.yaml` cites: `prompts-bia`, `prompts-review`, `stages-analysis-level`,
`stages-analysis-method`, `stages-analysis-minimum-controls`, `stages-analysis-typical-ai-uses`,
`stages-design-method`, `stages-design-minimum-controls`, `stages-design-typical-ai-uses`. Chunk
text is not covered by the contract, and much of it changed.

## 2026.09 — minted 2026-09-10, tag at `1f137d3`

*Written before the mint, and kept as written below; the manifest now lives at
`releases/archive/2026.09.json`.*

The first release of the machine edition. Nothing is tagged: `releases/2026.09.json` records the
commit it was cut against and carries `"tagged": false` until the tag is minted. Until then the
edition is a draft, and a citation should quote a commit rather than the release name.

**2026-09-10 — resynced from the source of record.** The vault at
`02-Projects/ai4bcm/guidance-rewrite` is the source of record and this repository is its mirror.
Eleven files were brought forward: the prompt pattern in `units/prompts/README.md`, the six task
prompts, the three stage prompts in `units/stages/design.md`, `implement.md` and `validate.md`, and
the interview order in `units/workflow-design.md`. `units/prompts/evaluations.md`, the thirty
evaluation cases, joined the repository with this resync and is the 24th citable file. Three files
stay in the vault only: `units/index.md`, `units/prompts/index.md` and `units/stages/index.md` are
vault-side navigation and say so in their own opening paragraph. So does `units/principles-a4.html`,
which is a sheet of a print edition this repository does not carry. `ask-ai4bcm/README.md` has no
vault counterpart because it says how this repository is used rather than what the guidance says.

What this release contains:

- Nineteen guidance units under `units/`, one file per topic, each opening with a `<!-- meta -->`
  anchor and closing with the citation line.
- Six task prompts and the prompt pattern under `units/prompts/`, with thirty evaluation
  cases in `units/prompts/evaluations.md`, three for each of the ten prompts in the guidance.
- `ask-ai4bcm/`, the router: it names the unit, the prompt, the maturity level and the gate that
  level turns on, and it never runs a prompt itself.
- `install/`, one page per client for Claude Code, Codex, GitHub Copilot and ChatGPT, and a
  Claude Code plugin manifest that installs the router with the units beside it.
- Provenance: based on draft v0A by Willem A. Hoekstra FBCI, 2026. Published under CC BY 4.0.

Known at the time of writing, and not fixed in this release:

- The guidance chatbot named as the first of the three ways in is not built. `units/data-rules.md`
  and the print edition say so; the row that describes what it would read stays, qualified.
- The `cites=` values in each unit's `<!-- meta -->` anchor address the numbering of the superseded
  July 2026 draft, which is being retired from the server. They resolve to nothing and are due to
  be removed in the same pass that rebuilds the served chunks.
