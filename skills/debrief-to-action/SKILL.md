---
name: debrief-to-action
description: Turns exercise notes into proposed findings tied to the missed objective, each with a proposed owner.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

You judge the notes of one exercise only against the objective written before it, quoted from the plan or exercise
brief the reader attaches; with no such document attached, you write the Gaps and no finding. Every finding and every
owner you return is **proposed**, until the accountable reviewer or the owner decides. The prompt is
[`units/stages/validate.md`](units/stages/validate.md), **Prompts, Task choice 2**.

1. **Find the objective.** With a plan or exercise brief attached, read the objective from it and ask nothing; the
   prompt's Intake is for what the attachments leave open. With none attached, ask for the document that holds the
   objective. An objective the reader types is their own statement: list it under Gaps and judge
   nothing against it. Done when the objective is quoted from an attached document, or, with none attached, the
   reply ends at Gaps.
2. **Draft the proposed findings and what worked** against that objective, in the shape the Output of Task choice 2
   sets, **blameless**: for each proposed finding, the role, the step and the guard that was missing; for each thing
   that worked, the role, the step and the safeguard that held. Where a note you quote names the person who slipped, put their
   role in square brackets in its place. Done when every passage of the notes that bears on
   the objective sits behind a proposed finding or a what-worked line, and each of those names its role, its step,
   and its missing guard or the safeguard that held.
3. **Write the actions**, in the shape the same Output sets; naming the owner of an action is assignment, not blame.
   Done when every proposed finding has at least one action or a line under Gaps saying why it has none, and every
   action with no owner named in the notes or the plan is listed under Gaps. The reply ends there, at proposed
   findings and actions; a theme worth exercising is the reader's separate request, through `/ask-ai4bcm`.

**Reviewer:** the accountable reviewer (exercise director or BCM manager) decides which proposed findings go into
the exercise report or the lessons log. Each proposed owner confirms the action before it is theirs.

Read next: [`units/stages/validate.md`](units/stages/validate.md), Method steps 1, 3 and 5 (the objective
first; the raw record kept apart from the analysis; the pattern put to the people who were there, then the action
tracked to a named owner). Debrief summaries as Level 2 work: [`units/levels.md`](units/levels.md), Where to
start, by level.
