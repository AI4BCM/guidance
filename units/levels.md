<!-- meta: unit=levels version=2026.09 -->
# Where You Stand

## Three ways of working

Settle which of three things you are using. They fail differently.

| | Chatbot | AI workflow | Agentic AI |
|---|---|---|---|
| What it does | whatever you ask | runs a defined process step by step | pursues a goal over multiple steps |
| Who picks the next step | you, in each prompt | the defined process | the model, within configured permissions |
| Results | vary each time | repeatable when inputs and method are fixed | vary with the path |

For most BCM work the workflow is the useful middle. Picking a step is not authority; a named person approves every consequential action. Results are comparable only when inputs are controlled, method and output structure documented, and someone evaluates the output. A workflow supplies the first three; evaluation is yours.

## The five maturity levels

| Level | Typical characteristics | Common pitfall at this level |
|---|---|---|
| 1: Assisted individual productivity (ad hoc) | approved but ad hoc individual use, low-risk tasks, no integration | uncontrolled individual use and accidental disclosure of sensitive information |
| 2: Team-level structured use (repeatable) | approved tools, basic guidance, repeatable prompts or skills | poor prompt patterns repeated, uneven quality across the team |
| 3: Connected and governed use (defined) | retrieval over approved repositories, role-based access, documented use cases, auditable | overconfidence in retrieval quality or in connector-fed data |
| 4: Operationally embedded AI support (measured) | multiple governed workflows, approval gates, quality monitoring, fallbacks | hidden operational dependency on workflows, or approval bottlenecks |
| 5: Advanced and optimised use (optimising) | mature governance, strong data foundations, continuing measurement of AI-enabled processes | complexity exceeding governance capability, unclear accountability across integrated systems |

In our experience most teams are at 1 to 2. Aim for 3 to 4. Level 5 is an optimisation stage. Proportionate testing comes before operational use at every level; Level 5 adds continuing measurement. Integration or automation alone is not evidence. Level 4 needs recorded quality and failures, review that changes outputs, a named workflow owner and a tested fallback. Two published instruments show what evidence of adoption looks like, gathered from assigned roles, artefacts, interviews and sampled documents rather than from questionnaires (SEI, 2026; OWASP AIMA, 2025). Their levels are their own and do not map onto these five; `references.md` says when each helps.

## Self-check

Five questions decide whether you can move from 2 to 3. Answer them with evidence:

1. Are the approved tools named, and does everyone in the team know which is approved for which data?
2. Are the data handling rules written down, or do they live in one person's judgement?
3. Is the source material current enough to ground an answer — and does anyone check its date?
4. Is it defined who reviews an AI-supported output and who approves it?
5. If the tool, connector or identity platform is unavailable, does the work still get done?

Each "no" is the next thing to fix before connecting anything further; none is a reason to stop using AI.

## Starting guide

One representative use per level, with the question that says you are ready to work there. Start where the data is least sensitive and the review is simplest, and move up when the next question answers yes with evidence. This is a starting guide and no assessment instrument, and it does not require reaching Level 5.

| Level | Start with | Ready to work here when |
|---|---|---|
| 1 Assisted individual productivity | summarising your own notes, first-pass drafting and rewriting of text that discloses nothing about the organisation, translation for review, fictional exercise ideas | the tool is approved for low-risk use and nothing confidential is entered (`data-rules.md`) |
| 2 Team-level structured use | policy, plan and awareness first drafts (`prompts/draft.md`, `prompts/awareness.md`), the pre-interview BIA draft with recovery fields blank (`prompts/bia.md`), exercise injects to a stated objective (`prompts/exercise.md`), debrief summarisation and the management review narrative (`prompts/management-report.md`) | approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route |
| 3 Connected and governed use | retrieval-grounded search across BCMS content, plan consistency checks (`stages/implement.md`), findings across exercise reports (`stages/validate.md`), BIA support and threat relevance over connected records (`stages/analysis.md`) | all five self-check questions answer yes with evidence |
| 4 Operationally embedded AI support | change-triggered plan and BIA review, scheduled awareness drafts, evidence-pack assembly and bounded incident-support retrieval, each built on the checklist in `workflow-design.md` | each workflow in use shows the four kinds of Level 4 evidence above, recorded and current |
| 5 Advanced and optimised use | multi-source resilience intelligence, advanced dependency analytics, tightly bounded agentic support within configured permissions | governance and data foundations already carry the Level 4 workflows and their measurement continues; this level suits large or mature organisations and is a choice rather than a target |

Whatever the level, the prompt pattern in `prompts/README.md` and the capability rows in `tools.md` apply, and the data rules run first.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
