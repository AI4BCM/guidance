# AI4BCM Guidance

The frozen, CC BY 4.0 guideline on AI use in business continuity management, and the open read-only
connector that serves it. This glossary fixes the words; the decisions behind them are in
`docs/adr/`.

## The published objects

**Corpus**:
The normative text under `units/`, plus the literature registered in `tools/sources.json`. Frozen at
a named release, citable, and changed only by a release with a changelog.
_Avoid_: the knowledge base, the KB, the docs, the content

**Normative corpus**:
The 96 chunks built from `units/` — the guidance's own text, which it speaks for and is answerable
for. The half of the corpus small enough (about 24,000 tokens at release 2026.09.1) to be carried
whole rather than retrieved.
_Avoid_: the guidance chunks, the core, the primary corpus

**Literature**:
The 287 chunks built from the eight class-A documents registered in `tools/sources.json` — NIST
SP 800-34r1, the NIST AI RMF, DORA, the EU AI Act articles, the delegated regulation, the Swiss
FONES minimum standard, the UK Cabinet Office guidance and the ESAs statement. Cited on their own
authority, never as the guidance. Too large to carry whole; reached by retrieval.
_Avoid_: the standards, the references, the external sources, class A

**Connector**:
The open MCP server at `mcp.ai4bcm.org` that serves the corpus. It reads nothing of the caller's.
What it returns can change without the corpus changing, and that is the point.
_Avoid_: the server, the API, the chatbot, the guidance chatbot

**Unit**:
One normative markdown file under `units/`. The thing a route names and a reader is sent to.
_Avoid_: page, doc, article, chapter

**Part**:
One of the eight numbered steps of the red thread, 0 to 7, from "Is this for me?" to "Keep it
running and defend it". Named by the reader's question it answers, it groups one or more units in
the print edition and on the website, and exists nowhere else. Never a unit, never a chunk, never
cited; a reader sees the question, never "Part 3". Distinct from the six parts of the prompt pattern
and the five parts of a route, which are parts of one thing, not of the guidance.
_Avoid_: chapter, section, step, stage, group

**Chunk**:
One addressable fragment of the corpus, keyed on its unit path and heading, carrying its own
citation, licence and release tag. The unit of retrieval and the unit of attribution.
_Avoid_: passage, section, snippet, result

**Release**:
A tagged edition of the corpus. The edition a citation names. Changing normative text means cutting
one; changing what the connector returns does not.
_Avoid_: version, build, bump

## The four questions

**Sensitivity class**:
What `data-rules.md` publishes: either the material is **high-sensitivity BCM material** — one of the
seven kinds at `data-rules.md:14-20`, approved corporate or private environment only — or it
**discloses nothing about the organisation** (`data-rules.md:8`). Two states, not a scale.
_Avoid_: sensitivity level, classification, risk class, data class

**Sensitivity hint**:
The `low | low to medium | medium | medium to high | high` value in the Selection guide's Sensitivity
column (`tools.md:34-51`). An editorial note on one table row. Quotable verbatim as part of that row;
never presented as a sensitivity class, despite `tools.md:32`.
_Avoid_: class, sensitivity class, the five classes

**Tier**:
One of the five deployment tiers at `tools.md:22-28`, from free public service to private
self-hosted. A closed list, and the thing a sensitivity class points at.
_Avoid_: environment, plan, licence, deployment level

**Never-alone action**:
One of the nine actions in `principles.md:18-37`: seven that are "not allowed or tightly limited"
and enforced by permissions, two that are "fully prohibited" and enforced by review.
_Avoid_: prohibited task, banned use, red line, do-not-use

**Level**:
One of the five maturity levels at `levels.md:16-26`. A level the guidance names for a piece of work,
never a level the guidance assesses a reader as holding.
_Avoid_: maturity score, rating, stage

**Gate**:
What must be true before work may happen at a level. The five self-check questions at
`levels.md:28-38` gate 2 to 3; every other gate is the "Ready to work here when" sentence in the
starting guide or the route.
_Avoid_: criteria, requirements, checklist, prerequisite

**Route**:
The five-part answer to a situation: unit, prompt, level with its gate, effort, and the data rule.
Published in `ask-ai4bcm/SKILL.md`. A route without its gate is a number.
_Avoid_: recommendation, path, journey, answer

**Effort**:
What a route says the work costs in time — "ten minutes", "forty minutes", "an afternoon". Published
prose, quoted, never computed.
_Avoid_: estimate, duration, cost, sizing

## The seam

**Way in**:
One of the routes by which a reader reaches the guidance, distinguished by what it reads of theirs
(`data-rules.md:26`). The connector reads nothing; the skill reads your files in your tenant; the
BIA workflow reads your process data.
_Avoid_: channel, client, interface, product

**Origin**:
The scheme, hostname and port a connector is submitted under — `mcp.ai4bcm.org` for this one. OpenAI
cannot change it after publication; a different origin is a new plugin from scratch. The BIA product
has its own, and that separation is what keeps this connector's contract true.
_Avoid_: endpoint, URL, host, domain, deployment

**Determination**:
An answer that is a verdict from a closed set plus the clause that binds it, rather than prose the
caller must read and judge. What separates the connector from a search box.
_Avoid_: assessment, analysis, judgement, recommendation

**Silence**:
The returnable state meaning the corpus does not address this. A distinct verdict, never an empty
result set and never an error.
_Avoid_: no match, not found, unknown, null
