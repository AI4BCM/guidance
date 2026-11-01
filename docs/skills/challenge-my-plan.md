## What it does

`challenge-my-plan` asks the hard questions about your plan or draft, round by round: your answer first, then its
recommendation. It recommends on a question only after the document's owner has answered it, so the answer on record
is the owner's own thinking. It reads facts from the document and puts only decisions to you, so it never asks what
the document already says. Every finding stays open, and the document stays as it was.

## When to reach for it

You invoke this by typing `/challenge-my-plan`, and the AI won't reach for it on its own. Reach for it when you own a
plan, draft or analysis, or are reviewing one with its owner to hand, and want to be asked the questions you did not
think of, one round at a time, answering each before you see its view.

This skill interviews you and waits for your answers after every round;
[`/red-team-assumptions`](https://github.com/AI4BCM/guidance/blob/main/skills/red-team-assumptions/SKILL.md) reads the paper and returns its full list in one reply.

| You want | Reach for |
| --- | --- |
| To be asked round by round, and to answer before you see its view | `/challenge-my-plan` |
| The full list of what a strategy or option paper relies on, in one reply, with a check for each | [`/red-team-assumptions`](https://github.com/AI4BCM/guidance/blob/main/skills/red-team-assumptions/SKILL.md) |
| Where a plan or a planned change departs from the BIA | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |
| A policy against the frameworks you select, or your records against your evidence checklist | [`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) |

## One round at a time

It asks the class of your data first and opens no file until you answer. It stops if your tool is not approved for
that class. It asks nothing about scope after that. The first lines name each attached document's version and date;
the document under review is named as the subject, with its status, and is not used as a source.

A **round** is a set of numbered questions, each tied to the passage it comes from: unclear points, unsupported
claims, contradictions, unstated assumptions and practical weaknesses, and each unstated premise the document
depends on, listed as an assumption. The round carries no recommendation. It ends on the questions, and the skill
waits. Asking for the list instead gets you the questions again.

Once you answer, it recommends on each answered question. Your answer goes under Gaps as your own statement, never as
a source. Any other recommendation rests on a passage you attached, or reads "not in the sources" and gives none. An
answer from someone who does not own the document leaves the recommendation waiting. The next round asks only what
your answers opened, and never repeats a round-1 question.

When you close the review, it ends with strengths, key gaps, assumptions to check and follow-up questions, in that
order, each tied to its passage. Every question it asked appears once, answered with its recommendation or still open.
No finding is closed, accepted or re-rated. After the sentence saying AI helped, one line names the questions still
open for the owner. Text in your files that tells an AI what to do is quoted under Gaps for its owner and information
security, and not obeyed.

## Common questions

**Why does it not show its recommended answer straight away?**
A recommendation shown first gets nodded through. It comes after your answer, so the answer is yours.

**Why "challenge" and not "grill"?**
"Grill" reads as an interrogation in front of a board or a works council, and the guidance's own practical rule
already says challenge: "Ask AI to prepare, compare, summarise, retrieve, and challenge."

**Can it apply its recommendations to the plan?**
No. It changes nothing and closes nothing. The plan's owner makes the edits through their own document control.

**What if the plan names no owner?**
The review says "none named", and who owns the plan may become one of the questions.

## It's working if

- Its first message asks only the data class.
- The first lines name the plan's version, date and status, and each source's version and date.
- The first round ends on numbered questions, each naming its passage, with no recommendation.
- Nothing it asks is already answered in the plan.
- A recommendation appears only after you have answered that question.
- Each later round asks only about what your answers opened.
- Every question it asked appears in the closing review once, answered or still open.
- The closing review lists your answers as your own statements, and every finding in it is still open.
- The review ends with the sentence saying AI helped, reviewer and date blank, then the line naming the questions
  still open for the owner. Rounds carry neither line.

## Where it fits

`challenge-my-plan` is an any-stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/), for any plan, draft
or analysis you own. Beside it sits [`/red-team-assumptions`](https://github.com/AI4BCM/guidance/blob/main/skills/red-team-assumptions/SKILL.md), because a
Design-stage option paper that needs its full list of assumptions in one sitting is that skill's job. After it, the
plan's owner makes the edits, because the skill changes nothing, and then takes the plan to the people who will work
with it. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes a question this skill does not cover to the
skill or unit that does.
