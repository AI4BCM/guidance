<!-- meta: unit=levels version=2026.09.1 -->
# Where You Stand

## Four ways of working with AI

First, work out which of four things you are using. They fail in different ways.

| | Chatbot | Skill | Workflow | Agentic AI |
|---|---|---|---|---|
| What it is | a conversation | your best prompt, with sources | fixed steps, checked by rules | a model working towards a goal |
| How you use it | ask, and ask again | save it once, reuse it | run it step by step | set a goal and permissions |
| Who decides what comes next | you, in each prompt | you; the saved prompt guides | the set process | the model, within permissions |
| Results | vary each time | similar, still checked | comparable, if inputs are fixed | vary with the path |

For most BCM work, a skill or a workflow is the useful choice. Deciding the next step is not the same as having authority. A named person must approve every important action. Results are comparable only when inputs are controlled, the method and output structure are written down, and someone checks the output. A workflow gives you the first three. Checking the output is your job.

These are kinds of AI tool in general. AI4BCM's own ways to use this guidance are the AI4BCM Guidance chatbot at ai4bcm.org/chat, the `/ask-ai4bcm` skill, the connector and the BIA workflow. `data-rules.md` says what each one reads.

## The five maturity levels

| Level | Typical characteristics | Common mistake at this level |
|---|---|---|
| 1: Ad hoc | Approved tools used by individuals, each in their own way. Nothing is written down, so no result can be repeated or traced. | Accidental disclosure of sensitive information, and nobody can say which output came from AI. |
| 2: Repeatable | Saved prompts and named tools let a team repeat what worked. It still depends on the people who know how. | Poor prompt patterns get repeated, and the method lives in one person's head. |
| 3: Defined | Use cases, prompts, sources, review points and limits are written down, given a version number and owned. Sources come from approved repositories with role-based access. | Too much trust in retrieval quality or in data that comes through connectors. |
| 4: Measured | Quality, overrides, failures and the age of sources are counted for each workflow. Each workflow has a named owner, approval gates and a tested fallback. | Hidden dependency on workflows, approval bottlenecks, and a low override rate read as quality. |
| 5: Optimising | The measurements decide which workflows change, grow or stop. People set the limits of AI use and check them afterwards. | Complexity that is greater than governance capability, and unclear accountability across connected systems. |

In our experience most teams are at 1 to 2. Aim for level 3 or 4; level 5 is optional. At every level, test before real use. More tools or more automation do not make a team more mature. Level 4 needs recorded quality and failures, reviews that change outputs, a named workflow owner and a tested fallback.

## Self-check

Five questions decide whether you can move from level 2 to level 3. Answer them with evidence:

1. Are the approved tools named, and does everyone in the team know which is approved for which data?
2. Are the data handling rules written down, or do they live in one person's judgement?
3. Is the source material current enough to base an answer on — and does anyone check its date?
4. Is it defined who reviews an AI-supported output and who approves it?
5. If the tool, connector or identity platform is unavailable, does the work still get done?

Each "no" is the next thing to fix before you connect anything further. Keep working at your AI maturity level meanwhile.

## Starting guide

The table gives one typical use per level. Each level has a question that tells you when you are ready to work there. Start where the data is least sensitive and the review is simplest. Move up when the next question gets a "yes" backed by evidence. Use it to choose where to start; it does not assess where you stand. Level 5 is optional.

| Level | Start with | Ready to work here when |
|---|---|---|
| 1 Ad hoc | summarising your own notes, first-pass drafting and rewriting of text that discloses nothing about the organisation, translation for review, fictional exercise ideas | the tool is approved for low-risk use, nothing confidential is entered (`data-rules.md`), and you have read the organisation's AI use policy, where one exists |
| 2 Repeatable | policy, plan and awareness first drafts (`prompts/draft.md`, `prompts/awareness.md`), the pre-interview BIA draft with recovery fields blank (`prompts/bia.md`), exercise injects to a stated objective (`prompts/exercise.md`), debrief summaries and the management review narrative (`prompts/management-report.md`) | the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route |
| 3 Defined | search across BCMS content based on retrieval, checks that plans agree (`stages/implement.md`), findings across exercise reports (`stages/validate.md`), BIA support and threat relevance over connected records (`stages/analysis.md`) | each use case is written down with its prompt, sources, review point and limits (`prompts/README.md`, Build your own skill), has an owner and is entered in the organisation's AI inventory, where one exists, and all five self-check questions answer yes with evidence; a skill or a workflow keeps that record on the card in `keep-it-running.md` |
| 4 Measured | plan and BIA review when something changes, awareness reminders on a fixed calendar, evidence-pack assembly and narrow incident-support retrieval, each built on the checklist in `workflow-design.md` | each workflow in use shows the four kinds of Level 4 evidence above, recorded and current on its card in `keep-it-running.md`, and the people named there have been told it is running |
| 5 Optimising | changing, extending or retiring workflows on the evidence of their own measurements, multi-source resilience intelligence, narrow agentic support within configured permissions | the Level 4 measurements have run long enough to show what to change, and people set and review the limits of AI use; this level suits large or mature organisations and is optional |

Whatever the level, the prompt pattern in `prompts/README.md` and the type-of-tool rows in `tools.md` apply. The data rules come first.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
