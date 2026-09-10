---
name: ask-ai4bcm
description: Ask which unit, prompt and level fit your BCM situation. A router over the AI4BCM guidance.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.09"
---

# Ask AI4BCM

You don't remember fifteen units, so ask.

This routes. Every answer names the unit to read, the prompt file to run, the level the work needs **and the gate that level turns on**, what it costs in time, and the data rules — which run before all of it. Then it hands over. It never runs a prompt itself.

Give every answer in that shape. A route without its gate is a number, and a route without the data-rules line is a hope.

The unit links below are relative, and they resolve when the units travel with this file, which they do in a clone of the guidance repository and in the plugin install. In a bare skill-folder install they do not, and the units are read from github.com/AI4BCM/guidance under `units/`.

## The main flow: the six lifecycle stages

The route most BCM work travels, in order. The worked example is one case: a food company acquires a processor in another country. Figures in the units are illustrative.

1. **Govern** — the site is not in scope and no role exists to put it there. [`../units/stages/govern.md`](../units/stages/govern.md) + [`../units/prompts/draft.md`](../units/prompts/draft.md). Level 2, team-level structured use — gate: approved tools and a written data rule; Level 3 only when the same question runs against the live governance repository. Forty minutes for the draft; the approval route is not forty minutes. Classify first: [`../units/data-rules.md`](../units/data-rules.md). ([`../units/prompts/management-report.md`](../units/prompts/management-report.md) is the other governance prompt; a newer practitioner learning the BCMS starts in the same unit, under **## Learning the practice**.)
2. **Embed** — the staff have never heard the message, and not in this language. [`../units/stages/embed.md`](../units/stages/embed.md) + [`../units/prompts/awareness.md`](../units/prompts/awareness.md). Level 2 — gate: a defined content base and a named reviewer; the bounded staff assistant is Level 3, because it retrieves under access control. Forty minutes for the script; in the case the dubbing took three weeks. Classify first: [`../units/data-rules.md`](../units/data-rules.md).
3. **Analysis** — nobody has written down what the site does. [`../units/stages/analysis.md`](../units/stages/analysis.md) + [`../units/prompts/bia.md`](../units/prompts/bia.md), recovery fields blank. Level 3, connected and governed use — gate: the method and sources are written down, so the draft can be regenerated when the inventory changes. An afternoon: sources and their dates first. Classify first — this is the most sensitive material in BCM: [`../units/data-rules.md`](../units/data-rules.md). Workflow behind it: [`../units/workflow-design.md`](../units/workflow-design.md). Risk assessment is in the same unit, under **## Risk assessment** — a model proposes relevance, a person accepts the risk.
4. **Design** — one shipping company quietly serving both sites. [`../units/stages/design.md`](../units/stages/design.md) + [`../units/prompts/review.md`](../units/prompts/review.md). Level 3 — gate: retrieval across **both** registers with role-based access and a documented use case; one register alone does not contain the finding. An afternoon, and only once both registers are in one place. Classify first: [`../units/data-rules.md`](../units/data-rules.md).
5. **Implement** — the plans now disagree with the organisation chart. [`../units/stages/implement.md`](../units/stages/implement.md) + [`../units/prompts/review.md`](../units/prompts/review.md). Level 3 — gate: retrieval over the approved plan repository, auditable; the change-triggered version is Level 4 and needs approval gates and a tested fallback first. Forty minutes to find them; in the case the sign-off took three weeks. Classify first: [`../units/data-rules.md`](../units/data-rules.md).
6. **Validate** — no exercise history here, and years of reports nobody read together. [`../units/stages/validate.md`](../units/stages/validate.md) + [`../units/prompts/exercise.md`](../units/prompts/exercise.md), once the objective is fixed. Level 3 — gate: retrieval over the controlled validation record, so the comparison re-runs after the next exercise. An afternoon. Classify first — debriefs name people: [`../units/data-rules.md`](../units/data-rules.md).

Each stage unit closes with a **## Level** section: what the work needs, and what the next rung would take.

## On-ramps

A starting situation that generates work, then merges onto the flow above.

- **"I inherited forty BIAs and no requirements register."** Stage 3: [`../units/stages/analysis.md`](../units/stages/analysis.md) + [`../units/prompts/bia.md`](../units/prompts/bia.md). Every drafted resource requirement is a question for the activity owner, never a register entry; recovery fields stay empty. Level 3 — gate: the method is written down well enough to re-run next year; without it you redo this from scratch. Not a forty-minute job: an afternoon per site, and the register is what comes back from the owners. Classify first: [`../units/data-rules.md`](../units/data-rules.md).

- **"My board wants a one-page AI policy for BCM."** What exists is a handout, and no policy: [`../units/principles.md`](../units/principles.md), rendered as [`../units/principles-a4.html`](../units/principles-a4.html) — the scope statement, five rules, the never-alone list and the eight-box checklist, published guidance to hand to the board. The policy itself is adopted through your own governance route; [`../units/prompts/draft.md`](../units/prompts/draft.md) fits the house wording, and the five rules stay unchanged. Level 2 — gate: fixed approved sources and a named reviewer, no connector. Forty minutes. Classify first: [`../units/data-rules.md`](../units/data-rules.md).

- **"Where do we start?"** [`../units/levels.md`](../units/levels.md), **## Starting guide** — one representative use and one readiness question for each of the five levels, built on the self-check above it; then the prompt or stage unit the row names. Level 1 or 2 — gate: the tool is approved and nothing confidential goes in. Ten minutes to place yourself; the first task is whatever the row names. Classify first: [`../units/data-rules.md`](../units/data-rules.md).

- **"I have three years of exercise reports."** Stage 6: [`../units/stages/validate.md`](../units/stages/validate.md); the **## Prompts** section inside that unit carries the read-across that clusters recurring findings, then [`../units/prompts/exercise.md`](../units/prompts/exercise.md) once a theme is worth exercising. AI proposes a theme; a person makes it a finding. Level 3 — gate: retrieval over the whole set, or you have one person's sample. An afternoon. Classify first: [`../units/data-rules.md`](../units/data-rules.md).

- **"We are acquiring a company."** The main flow from the top: [`../units/stages/govern.md`](../units/stages/govern.md) + [`../units/prompts/draft.md`](../units/prompts/draft.md), Level 2, then stages 2 to 6. Do not start at analysis because the BIA feels urgent: without the scope change nothing you draft has an owner. Weeks, not a sitting — forty minutes buys stage 1's two action lists. Classify first: [`../units/data-rules.md`](../units/data-rules.md).

- **"Which tool may I paste this into?"** [`../units/data-rules.md`](../units/data-rules.md) — classes, the never-public line, what each way in reads; tiers behind it in [`../units/tools.md`](../units/tools.md); then the pattern in [`../units/prompts/README.md`](../units/prompts/README.md). Level 2 — gate: the data rules are written down. Until they are you are Level 1 whatever the licence says, and the answer is "none yet". Ten minutes, and it is the ten that saves the rest.

- **"Which capability fits this task, and may we approve the tool?"** The selection guide in [`../units/tools.md`](../units/tools.md) pairs each stage's tasks with a capability and the tier it may run in; the checklist under **Evaluating a tool** in the same unit is what a tool is approved against, licence and contract terms included. Level 2 — gate: the answers are recorded with the approval. An hour with whoever owns the contract. Classify first: [`../units/data-rules.md`](../units/data-rules.md).

## Vocabulary underneath

[`../units/glossary.md`](../units/glossary.md) is the single source for the words: BIA, MTPD, RTO, RA, RAG, LLM, connector, skill, workflow, agentic system. Reach for it when the **word**, not the process, is the problem. [`../units/levels.md`](../units/levels.md) holds the ladder itself — three ways of working, five levels with their pitfalls, the five-question self-check that decides whether you can move from 2 to 3, and the starting guide with a representative use and a readiness question per level. [`../units/references.md`](../units/references.md) holds the source behind every citation in the units and the further reading, each with the question it answers; route there when the reader asks what a claim rests on.

## Precondition

[`../units/data-rules.md`](../units/data-rules.md) runs first, before any route above, which is why every route names it again. It decides where the task may happen, and it is the one rule you cannot recover from: what is pasted into the wrong tool cannot be unpasted.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
