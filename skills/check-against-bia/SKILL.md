---
name: check-against-bia
description: Given a plan or a change, lists where it disagrees with the BIA or what it reopens, with proposed owners.
license: CC BY 4.0. LICENSE in the guidance repository carries the full terms.
disable-model-invocation: true
metadata:
  version: "2026.11.0"
---

First run [`preflight.md`](preflight.md).

You **quote** both sides of every disagreement, name whose document each side is, and leave the choice of the right
value to those owners. For a change, you search only the documents attached and name each kind of document you could
not see under **Coverage unknown**. The prompt is [`units/stages/implement.md`](units/stages/implement.md),
Prompts, **Task choice 2** for a plan and **Task choice 3** for a change; with both inputs, choice 2 then choice 3 in
one run. Its Intake line holds unchanged.

1. **Sort the input.** A plan, a change, or both, each against the approved BIA and the requirements register. For a
   change with no plans or documents to search, one of the intake questions asks for them; without them, block 2
   lists only the BIA and register entries and says "plans: coverage unknown, none attached". Done when the input is
   named as plan, change or both, each document's version and date is known, and for a change the plans and
   documents to search are attached or their absence is noted.
2. **Plan, or both: write block 1, Against the BIA,** with Task choice 2; its Output, Gaps and Cite lines set the
   block. Done when every recovery time, resource requirement, contact and supplier in the plan has a comparison
   result or a recorded gap.
3. **Change, or both: write block 2, What it reopens,** with Task choice 3 over the attached set only; its Output,
   Gaps and Cite lines set the block, ending on **Coverage unknown**: each kind of document the change could touch
   that the set does not include, for example contact lists or supplier contracts. Done when every plan, BIA entry
   and register entry in the attached set has been searched for the change.
4. **Assemble the reply.** Done when the blocks stand apart, block 1 first, neither merged into nor reranked against
   the other, and the reply ends by naming [`units/prompts/review.md`](units/prompts/review.md) as the
   reader's next step for each flagged plan.

**Reviewer:** the BCM manager who asked checks each quoted passage. Each plan owner and each BIA activity owner
decides whether their document changes, and a plan changes only with its owner's approval and a new version.

Read next: [`units/stages/implement.md`](units/stages/implement.md), Method steps 1 and 5 ("A plan carries
out the approved strategy; the BIA supplies the requirements that strategy meets"; "which system, structure or
supplier change should reopen which plan"); [`units/stages/analysis.md`](units/stages/analysis.md), Typical AI
uses ("re-opening affected BIA and risk records").
