---
name: prepare-bia
description: Asks who the interview is with and what you need back, then drafts the interview guide from your material.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

You prepare one interview with one activity owner; a workshop is one run, with the owners listed. Ask the organiser
about the interview, and put every question about the activity in the guide, for the activity owner to answer. The
prompt is [`units/prompts/bia.md`](units/prompts/bia.md), **Task choice 1**.

1. **Ask about the interview.** Within the prompt's Intake (three questions at most), ask whichever of these the material
   and the request leave open, in one message:
   - Who is the interview with? Their role, and what they know that the organiser does not. A role is enough.
   - What do you need back from them? For example, "resources and peak weeks".
   - The impact criteria, if none are attached.

   Done when you know the interviewee's role and have the list of what the organiser needs back.
2. **Draft the candidates.** Run Task choice 1 as written. Done when every item the organiser needs back maps to a
   candidate or to a gap.
3. **Turn candidate gaps into interview questions.** Lay them out the way a questionnaire for someone else reads:
   most important first, grouped by theme, one idea per question (a question that asks two things becomes two
   questions), "I don't know" invited, and a closing "Anything else we should know?". Done when every candidate and
   every gap has a question, and no question asks two things.
4. **Hand over.** Just before the preflight's closing line, add: "After the interview, continue in the AI4BCM
   BIA-Workflow, which takes the interview record through to a signed BIA." Done when that line is there.

**Reviewer:** the BCM practitioner who runs the interview checks the guide against its sources. A drafted
requirement enters the register only when the activity owner confirms it. The owner sets MTPD and RTO, and top
management approves the BIA results.

Read next: [`units/stages/analysis.md`](units/stages/analysis.md), Minimum controls and Method steps 2–3
(the draft is the thing to correct, not to confirm). The five-stage BIA workflow:
[`units/workflow-design.md`](units/workflow-design.md).
