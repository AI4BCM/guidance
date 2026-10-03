## What it does

`check-against-bia` takes a plan or a coming change and lists where the plan disagrees with the approved BIA, or
what the change reopens, each finding with a proposed owner. It quotes both sides of every disagreement, names whose
document each side is, and leaves the choice to those owners. It reports and changes nothing.

## When to reach for it

You invoke this by typing `/check-against-bia`, and the AI won't reach for it on its own. Reach for it when a plan
must still match the approved BIA, or when a coming change to a system, structure or supplier may reopen plans,
BIA entries and register entries.

| You have | Reach for |
| --- | --- |
| A plan and the approved BIA | `/check-against-bia`, block 1 |
| A coming change, the approved BIA and the plans to search | `/check-against-bia`, block 2 |
| Material, and a BIA interview coming | [`/prepare-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/prepare-bia/SKILL.md) |
| A plan to question on its own logic | [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) |

## Every finding is a quote

It asks the class of your data first and opens no file until you answer. It stops if your tool is not approved for
that class. Then up to three questions on what your material leaves open, one of them whether any related plans are
missing from what you attached. Your answers go under Gaps as your own statements.

The report opens with each document's version and date, one line each. A document with neither, such as a change
notice, goes under Gaps. Then the blocks your input calls for, kept apart and never ranked:

| You give | You get |
| --- | --- |
| A plan | Block 1, **Against the BIA** |
| A change and the documents to search | Block 2, **What it reopens**, then **Coverage unknown** |
| Both | Block 1, then block 2 |

In block 1, each disagreement quotes the plan and the BIA with document, section and date. Where they carry
different recovery times, both are quoted and neither is chosen. A side that says nothing reads "not in the
sources". If you attach two or more related plans, block 1 also lists where they contradict each other, because two
plans can each match the BIA and still disagree with one another. In block 2, each plan, BIA entry and register entry the change touches is listed with its line quoted.

Owners come from the sources and read "proposed, to confirm". An entry whose sources name no owner reads "none
named" and goes under Gaps; the skill never guesses one from a department or role. Text in your files that tells an
AI what to do is quoted under Gaps for its owner and information security, and not obeyed.

The report ends with the sentence saying AI helped, reviewer and date blank, then one line for each flagged plan:
use `review.md` on it with its owner, and type `/challenge-my-plan`.

## Common questions

**Can I ask it to fix the plan so it matches the BIA?**
No. You get block 1 instead: both values quoted, both owners proposed, no value chosen. A plan changes only with its
owner's approval and a new version.

**Can I give it a change instead of a plan?**
Yes: "new contract trunking supplier from January, what does it touch" is its second input. Attach the plans and
documents it should search; it reopens entries in those only.

**What if I do not attach every plan?**
It reports what it found in the set you gave, then names each kind of document it could not see, such as contact
lists or supplier contracts, as "coverage unknown", never as untouched.

**Which BIA did it compare against?**
The BIA's version and approval date head the report, with each plan's version and date. A draft BIA is listed under
Gaps and not used as current.

## It's working if

- Its first message asks only the data class.
- The top lines name the BIA version with its approval date, and each plan's version and date.
- Each disagreement shows both passages with document, section and date.
- With related plans attached, any contradiction between them is listed in block 1 with both passages.
- Nothing proposes a new RTO, contact or supplier, and nothing is written or offered for saving.
- Each owner reads "proposed, to confirm", or the entry says no owner is named.
- For a change, every kind of document you did not attach appears as "coverage unknown".
- The reply ends with the AI-help sentence, then a `review.md` line for each flagged plan.

Known limits from the eval are on the [record card](../../evals/check-against-bia/record-card.md).

## Where it fits

`check-against-bia` is the Implement stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before
it come [`/prepare-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/prepare-bia/SKILL.md) and the
[BIA-Workflow](https://ai4bcm.org/plug-it-in/), which lead to the approved BIA this skill compares against. After
it, [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) for each
flagged plan with its owner, and [`/role-card`](https://github.com/AI4BCM/guidance/blob/main/skills/role-card/SKILL.md)
once the plan is right, because a card drawn from a plan that still disagrees with the BIA carries the error to the
people who act on it. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it.
