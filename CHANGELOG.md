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
to be checkable rather than merely attributed, add the commit from `releases/2026.09.json`.

Prompts move faster than the rest of the guidance. `units/prompts/` is the living part, so a
citation of a prompt without a release names nothing durable — cite the release or quote the
prompt in full.

## 2026.09 — not yet tagged

The first release of the machine edition. Nothing is tagged: `releases/2026.09.json` records the
commit it was cut against and carries `"tagged": false` until the tag is minted. Until then the
edition is a draft, and a citation should quote a commit rather than the release name.

What this release contains:

- Nineteen guidance units under `units/`, one file per topic, each opening with a `<!-- meta -->`
  anchor and closing with the citation line.
- Six task prompts and the prompt pattern under `units/prompts/`, with thirty evaluation cases.
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
