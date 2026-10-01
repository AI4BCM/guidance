## What it does

`challenge-my-plan` asks the hard questions about your plan or draft, round by round: your answer first, then its
recommendation. It shows its view on a question only after the plan's owner has answered that question, so the
answer on record is the owner's own thinking. It reads facts from the plan and puts only decisions to you, so it never
asks what the plan already says.

## When to reach for it

You invoke this by typing `/challenge-my-plan`, and the AI won't reach for it on its own. Reach for it when you own a
plan, draft or analysis, or are reviewing one with its owner to hand, and want to be asked the questions you did not
think of, one round at a time, answering each before you see its view.

The one test against its near-twin: this skill interviews you and waits for your answers after every round;
[`/red-team-assumptions`](https://github.com/AI4BCM/guidance/blob/main/skills/red-team-assumptions/SKILL.md) reads the paper and returns its full list in one reply.

| You want | Reach for |
| --- | --- |
| To be asked round by round, and to answer before you see its view | `/challenge-my-plan` |
| The full list of what a strategy or option paper relies on, in one reply, with a check for each | [`/red-team-assumptions`](https://github.com/AI4BCM/guidance/blob/main/skills/red-team-assumptions/SKILL.md) |
| Where a plan or a planned change departs from the BIA | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |
| A policy against the frameworks you select, or your records against your evidence checklist | [`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) |

## One round at a time

A **round** is a set of numbered questions, each naming the section of the plan it comes from, with no
recommendation beside it. The round ends on the questions, and the skill waits. Once you answer, it gives its view on
each answered question, drawn from the material you attached, or says "not in the sources" where nothing attached
supports one. The next round asks only what your answers opened. One question may take the pre-mortem frame:
"imagine it failed; why?".

Asking for the whole list at once gets you the open question again. When no questions remain and you agree to close,
it ends with a review: strengths, key gaps, assumptions to check and follow-up questions. Your answers sit there as
your own statements, and every finding stays open for the plan's owner.

## Common questions

**Why does it not show its recommended answer straight away?**
A recommendation shown first gets nodded through. It comes after your answer, so the answer is yours.

**Why "challenge" and not "grill"?**
"Grill" reads as an interrogation in front of a board or a works council, and the guidance's own practical rule
already says challenge.

**Where did the pre-mortem go?**
Into this skill, as one question type: "imagine it failed; why?".

## It's working if

- The first line names the plan's version and date.
- The first reply ends on numbered questions, each naming its section, with no recommendation.
- Nothing it asks is already answered in the plan.
- Its view on a question appears only after you have answered that question.
- Each later round asks only about what your answers opened.
- Every question it asked appears in the closing review once, answered or still open.
- The closing review lists your answers as your own statements, and every finding in it is still open.

## Where it fits

`challenge-my-plan` is an any-stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/), for any plan, draft
or analysis you own. Beside it sits [`/red-team-assumptions`](https://github.com/AI4BCM/guidance/blob/main/skills/red-team-assumptions/SKILL.md), because a
Design-stage option paper that needs its full list of assumptions in one sitting is that skill's job. After it, the
plan's owner makes the edits, because the skill changes nothing, and then takes the plan to the people who will work
with it. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes a question this skill does not cover to the
skill or unit that does.
