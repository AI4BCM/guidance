<!-- meta: unit=levels version=2026.09.1 -->
# Where You Stand

## Three ways of working

First, work out which of three things you are using. They fail in different ways.

| | Chatbot | AI workflow | Agentic AI |
|---|---|---|---|
| What it does | whatever you ask | runs a set process step by step | pursues a goal over multiple steps |
| Who picks the next step | you, in each prompt | the set process | the model, within set permissions |
| Results | vary each time | repeatable when inputs and method are fixed | vary with the path |

For most BCM work, the workflow is the useful middle option. Picking a step is not the same as having authority. A named person must approve every important action. Results are comparable only when inputs are controlled, the method and output structure are written down, and someone checks the output. A workflow gives you the first three. Checking the output is your job.

## The five maturity levels

| Level | Typical characteristics | Common pitfall at this level |
|---|---|---|
| 1: Ad hoc/Initial | Approved tools used by individuals, each in their own way. Nothing is written down, so no result can be repeated or traced. | Accidental disclosure of sensitive information, and nobody can say which output came from AI. |
| 2: Repeatable | Saved prompts and named tools let a team repeat what worked. It still depends on the people who know how. | Poor prompt patterns get repeated, and the method lives in one person's head. |
| 3: Defined | Use cases, prompts, sources, review points and limits are written down, versioned and owned. Sources come from approved repositories with role-based access. | Too much trust in retrieval quality or in data that comes through connectors. |
| 4: Quantitatively managed | Quality, overrides, failures and the age of sources are counted for each workflow. Each workflow has a named owner, approval gates and a tested fallback. | Hidden dependency on workflows, approval bottlenecks, and a low override rate read as quality. |
| 5: Optimised | The measurements decide which workflows change, grow or stop. People set the limits of AI use and check them afterwards. | Complexity that is greater than governance capability, and unclear accountability across connected systems. |

In our experience most teams are at 1 to 2. Aim for level 3 or 4. Level 5 is an optimisation stage. Proportionate testing comes before operational use at every level. Level 5 also needs ongoing measurement. Integration or automation alone is not proof of maturity. Level 4 needs recorded quality and failures, reviews that change outputs, a named workflow owner, and a tested fallback. Two published tools show what evidence of adoption looks like. They gather it from assigned roles, artefacts, interviews, and sampled documents, not from questionnaires (SEI, 2026; OWASP AIMA, 2025). Their levels are their own and do not map onto these five. `references.md` says when each one helps. The five level names follow the CMMI line (ISACA, 2024), where the levels are Initial, Managed, Defined, Quantitatively Managed and Optimizing; Repeatable is the name the earlier CMM gave level 2. The descriptions here are AI4BCM's own. AI4BCM also publishes the *AI Maturity Playbook for BCM* (Gerner, 2026; CC BY 4.0). It uses the same five levels and scores each of its four axes separately, so it gives four numbers where this guidance gives one. A single guidance level is not four playbook scores, and neither can be converted into the other.

## Self-check

Five questions decide whether you can move from 2 to 3. Answer them with evidence:

1. Are the approved tools named, and does everyone in the team know which is approved for which data?
2. Are the data handling rules written down, or do they live in one person's judgement?
3. Is the source material current enough to ground an answer — and does anyone check its date?
4. Is it defined who reviews an AI-supported output and who approves it?
5. If the tool, connector or identity platform is unavailable, does the work still get done?

Each "no" is the next thing to fix before you connect anything further. None of them is a reason to stop using AI.

## Starting guide

Here is one typical use per level. Each level has a question that tells you when you are ready to work there. Start where the data is least sensitive and the review is simplest. Move up when the next question gets a "yes" backed by evidence. This is a starting guide; it does not assess where you stand. It does not require you to reach Level 5.

| Level | Start with | Ready to work here when |
|---|---|---|
| 1 Ad hoc/Initial | summarising your own notes, first-pass drafting and rewriting of text that discloses nothing about the organisation, translation for review, fictional exercise ideas | the tool is approved for low-risk use and nothing confidential is entered (`data-rules.md`) |
| 2 Repeatable | policy, plan and awareness first drafts (`prompts/draft.md`, `prompts/awareness.md`), the pre-interview BIA draft with recovery fields blank (`prompts/bia.md`), exercise injects to a stated objective (`prompts/exercise.md`), debrief summarisation and the management review narrative (`prompts/management-report.md`) | the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route |
| 3 Defined | retrieval-grounded search across BCMS content, plan consistency checks (`stages/implement.md`), findings across exercise reports (`stages/validate.md`), BIA support and threat relevance over connected records (`stages/analysis.md`) | each use case is written down with its prompt, sources, review point and limits and has an owner, and all five self-check questions answer yes with evidence |
| 4 Quantitatively managed | change-triggered plan and BIA review, scheduled awareness drafts, evidence-pack assembly and bounded incident-support retrieval, each built on the checklist in `workflow-design.md` | each workflow in use shows the four kinds of Level 4 evidence above, recorded and current |
| 5 Optimised | changing, extending or retiring workflows on the evidence of their own measurements, multi-source resilience intelligence, tightly bounded agentic support within configured permissions | the Level 4 measurements have run long enough to show what to change, and people set and review the limits of AI use; this level suits large or mature organisations and is a choice rather than a target |

Whatever the level, the prompt pattern in `prompts/README.md` and the capability rows in `tools.md` apply. The data rules come first.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
