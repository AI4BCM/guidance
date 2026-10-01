## What it does

`check-against-bia` takes a plan or a coming change and lists where the plan disagrees with the approved BIA, or
what the change reopens, each finding with a proposed owner. It quotes both sides of every disagreement, names whose
document each side is, and leaves the choice of the right value to those owners. For a change, it searches only the
documents you attach and names each kind it could not see.

## When to reach for it

You invoke this by typing `/check-against-bia`, and the AI won't reach for it on its own. Reach for it when a plan
must still match the approved BIA, or when a coming change to a system, structure, site or supplier may reopen plans
and BIA entries.

| You have | Reach for |
| --- | --- |
| A plan and the approved BIA | `/check-against-bia`, block 1 |
| A coming change, the approved BIA and the plans to search | `/check-against-bia`, block 2 |
| Material, and a BIA interview coming | [`/prepare-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/prepare-bia/SKILL.md) |
| A draft plan to question on its own logic | [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) |

## Every finding is a quote

Each finding rests on quoted lines: both passages for a disagreement, with document, section and date, and the
touched line for an entry a change reopens. Where the plan and the BIA carry different recovery times, both are
**quoted** and neither is chosen; the owner sets the RTO. Owners come from the sources and read "proposed, to
confirm". An entry whose sources name no owner is listed under Gaps without one.

The output follows what you gave it, and the blocks stay apart:

| You give | You get |
| --- | --- |
| A plan | Block 1, **Against the BIA** |
| A change and the documents to search | Block 2, **What it reopens**, then **Coverage unknown** |
| Both | Block 1, then block 2, never merged |

**Coverage** marks the limit of a change search. The skill reports what it found in the set you attached, then
names each kind of document the change could touch that you did not attach, such as contact lists or supplier
contracts, as "coverage unknown". A document it could not see is never reported as untouched.

## Common questions

**Can I give it a change instead of a plan?**
Yes: "new contract trunking supplier from january, what does it touch" is its second input. Attach the plans and
documents it should search; it reopens entries in those only.

**What if I do not attach every plan?**
It reports what it found in the set you gave, then names each kind of document it could not see as "coverage
unknown", never as untouched.

**Which BIA did it compare against?**
The BIA's version and approval date head the output, with each plan's version and date. A draft BIA is listed under
Gaps and not used as current.

**The plan carries an old RTO. Which value is right?**
It quotes both and chooses neither; the owner sets the RTO.

## It's working if

- The top lines name the BIA version with its approval date, and each plan's version and date.
- Each disagreement shows both passages with document, section and date.
- Nothing proposes a new RTO, contact or supplier.
- For a change, every kind of document you did not attach appears as "coverage unknown".
- Each owner reads "proposed, to confirm", or the entry says no owner is named.
- You received the block or blocks your input called for.

## Where it fits

`check-against-bia` is the Implement stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before
it, [`/prepare-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/prepare-bia/SKILL.md) and the [BIA-Workflow](https://ai4bcm.org/plug-it-in/), because
they lead to the approved BIA this skill compares against. After it,
[`/role-card`](https://github.com/AI4BCM/guidance/blob/main/skills/role-card/SKILL.md), because a card drawn from a plan that still disagrees with the BIA carries
the error to the people who act on it. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes you to the skill for your stage.
