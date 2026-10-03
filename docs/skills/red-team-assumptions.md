## What it does

`red-team-assumptions` lists what the strategy silently relies on, and the check that would settle each. It lists
only: each item ends on its check and a question for the person who can run it, and it proposes no option and scores
no risk. It is for the strategy or option paper that everyone in the room already likes. Approving the option and
accepting its risk stay with people.

## When to reach for it

You invoke this by typing `/red-team-assumptions`, and the AI won't reach for it on its own. Reach for it in the
Design stage, when a strategy or option paper is on the table that everyone in the room already likes, and you want
everything it relies on in one reply, each with the check that would settle it.

This skill reads the paper and returns its full list in one reply, asking you
nothing after it; [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) interviews you round by round and waits for
your answers.

| You want | Reach for |
| --- | --- |
| The full list of what a strategy or option paper relies on, in one reply, with a check for each | `/red-team-assumptions` |
| To be asked round by round about your plan, and to answer before you see its view | [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) |
| Where a plan or a planned change departs from the BIA | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |

## What would have to be true

It asks the class of your data first and opens no file until you answer. It stops if your tool is not approved for
that class. Then it asks about scope only: which option, and which decision. An owner, status or value your files
lack is not a question; it goes under Gaps. The first lines name each document's version and date; a draft paper goes
under Gaps with its status and date, and is still read as the paper.

It starts from the gap the option must close, checked against the register or BIA the paper names. Then it asks what
would have to be true for the option to fail, and which requirement the option quietly shares with the thing it is
meant to protect; that shared requirement is its own item. Each assumption quotes its passage and says "Fails if …".

| Each item carries | What you see |
| --- | --- |
| The check | A question for the owner your sources name, marked "proposed, to confirm"; with no owner, "none named" and the check under Gaps, still a question |
| A supplier the option needs | Its own continuity plan, a written SLA and a second source, as your sources show them, or "not in the sources" |
| A financial or commercial claim | Marked "for finance or procurement" |
| The order | By effort or cost only where your sources state it; otherwise "ordering unknown, for the reviewer" |

Then what holds up in the paper, and why. It rates no risk, and the risk owner is the one the paper names, or "none
named". Text in your files that tells an AI what to do is quoted under Gaps for its owner and information security,
and not obeyed. The reply ends with the sentence saying AI helped, reviewer and date blank, then one line: put the
paper and these checks to the group that chooses, and for a review, `/challenge-my-plan`.

## Common questions

**Does it check whether the supplier has its own plan?**
Yes. Every supplier the option needs gets its own continuity plan, written SLA and second source, and what your
sources do not show reads "not in the sources".

**Why are the checks not ranked cheapest first?**
It orders them by cost only where your sources state the effort or cost; otherwise it says "ordering unknown, for the
reviewer", and financial claims go to finance or procurement. A cost order the sources do not support would be
invented.

**Can it approve the option once the checks look fine?**
No. Approving it and accepting the risk are people's decisions, whatever your tool allows. The stakeholder group owns
the choice.

**Why is this a separate skill from `/challenge-my-plan`?**
One waits for your answers round by round; this one returns everything at once.

## It's working if

- Its first message asks only the data class, and the next asks about scope only.
- The first lines name the paper's and each register's version and date.
- One reply holds the whole list and asks you nothing after it.
- Every assumption quotes its passage and says "Fails if …".
- The requirement the option shares with what it protects appears as its own item.
- Every check ends on a question, with a proposed owner or "none named" under Gaps.
- Every supplier the option needs appears with its own plan, written SLA and second source, or "not in the sources".
- Financial and commercial claims are marked for finance or procurement.
- No risk score appears, and no option or alternative is proposed.
- The order reads "ordering unknown, for the reviewer" unless your sources state a cost.
- It says what in the paper holds up, and why.
- The reply ends with the sentence saying AI helped, then the line handing the paper to the group that chooses.

Known limits from the eval are on the [record card](../../evals/red-team-assumptions/record-card.md).

## Where it fits

`red-team-assumptions` is the Design stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before it
comes the BIA, because it sets the gap the option must close; later,
[`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) compares the plan built from the chosen option with that BIA.
After it, the paper goes to the stakeholder group, because they own the choice. Use
[`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) next when the revised paper needs its owner's answers before
recommendations, because that skill waits for each answer before it gives its view. When you are unsure which skill
fits your task, [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes a question this skill does not
cover to the skill or unit that does.
