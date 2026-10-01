## What it does

`red-team-assumptions` lists what the strategy silently relies on, and the check that would settle each. It lists
only what the option needs to be true, each item ending on that check and a question for the person who can run it, and it scores nothing. It is for the strategy or option paper that everyone in the
room already likes.

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

## Only what is load-bearing

An assumption earns a line only if it is **load-bearing**: the option falls when it fails. The skill first reads the
paper at its strongest, and what holds up goes in its own section with the reason, so a sound paper gets no invented
doubt. Each assumption it keeps quotes its passage and says "Fails if …", naming what goes wrong for the option.

| Each item carries | What you see |
| --- | --- |
| The check | A question for the person who can answer it: an owner your sources name, marked "proposed, to confirm", or under Gaps with no owner |
| A supplier the option needs | Its own continuity plan, a written SLA and a second source, as your sources show them, or "not in the sources" |
| A cost, price or contract claim | Marked "for finance or procurement", with the check left to them |
| The order | By effort or cost only where your sources state it; otherwise "ordering unknown, for the reviewer" |

It rates no risk: no impact or likelihood score, and no threshold for stopping the option, which is the sponsor's call.

## Common questions

**Does it check whether the supplier has its own plan?**
Yes. Every supplier the option needs gets its own block (own continuity plan, written SLA, second source), and what
your sources do not show reads "not in the sources". 

**Why are the checks not ranked cheapest first?**
It orders them by cost only where your sources state the effort or cost; otherwise it says "ordering unknown, for the
reviewer", and cost claims go to finance or procurement. A cost order the sources do not support would be invented.

**Why is this a separate skill from `/challenge-my-plan`?**
One waits for your answers round by round; this one returns everything at once. One shared test case, a fully supplied strategy, checks where the line between the two falls.

## It's working if

- The first lines name the paper's and each register's version and date.
- One reply holds the whole list and asks you nothing after it.
- Every assumption quotes its passage and says "Fails if …", naming what goes wrong for the option.
- Every check ends on a question, with a proposed owner or under Gaps.
- Every supplier the option needs appears with its own plan, written SLA and second source, or "not in the sources".
- Cost and contract claims are marked for finance or procurement.
- No risk score appears.
- The order reads "ordering unknown, for the reviewer" unless your sources state a cost.
- It says what in the paper holds up, and why.

## Where it fits

`red-team-assumptions` is the Design stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before it
comes the BIA, because it sets the gap the option must close; later,
[`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) compares the plan built from the chosen option with that BIA.
After it, the paper goes to the stakeholder group, because they own the choice. Use
[`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) next when the revised paper needs its owner's answers before
recommendations, because that skill waits for each answer before it gives its view. When you are unsure which skill
fits your task, [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes a question this skill does not
cover to the skill or unit that does.
