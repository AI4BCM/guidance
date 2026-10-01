---
name: prepare-bia
description: Asks who the interview is with and what you need back, then drafts the interview guide from your material.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

# Prepare a BIA interview

First run [`preflight.md`](preflight.md).

You prepare one interview with one activity owner. A workshop counts as one run, with the owners listed. The prompt
is [`units/prompts/bia.md`](units/prompts/bia.md), **Task choice 1**. Run it as written; the steps below add
only what the prompt leaves open.

1. **Ask about the interview itself.** Use the prompt's Intake, which allows three questions at most. Two of
   them are always these, asked in one message:
   - Who is the interview with? Ask for their role and what they know that the user does not. A role is enough;
     no name is needed.
   - What do you need back from them? For example, "resources and peak weeks".

   Use the third question for the impact criteria if none are attached; otherwise, use it for one point the material
   leaves open. Wait for the answers. Done when you know the role and have a list of what the user needs back.
2. **Draft the guide.** Produce the prompt's Output for Task choice 1, labelling every entry "candidate, to
   confirm". Where no document supports an entry, ask about it in the guide instead. Leave MTPD, RTO and RPO empty,
   and every dependency's RTO too. A recovery time quoted from another department's confirmed BIA goes in the note
   under the table, with its source, date and status.
3. **Lay out the interview questions** the way a questionnaire for someone else reads: most important first,
   grouped by theme, one idea per question, "I don't know" invited, and a closing "Anything else we should know?".
   Done when every item from the answer to "what do you need back" has a question.
4. **Hand over.** Just before the closing line of the preflight, add: "After the interview, continue in the AI4BCM
   BIA-Workflow, which takes the interview record through to a signed BIA." This skill stops there and does not
   process the interview record.

**Reviewer:** the BCM practitioner who runs the interview checks the guide against its sources. A drafted
requirement enters the register only when the activity owner confirms it. The owner sets MTPD and RTO, and top
management approves the BIA results.

Read next: [`units/stages/analysis.md`](units/stages/analysis.md), Minimum controls and Method steps 2–3
(the draft is the thing to correct, not to confirm). The five-stage BIA workflow:
[`units/workflow-design.md`](units/workflow-design.md).
