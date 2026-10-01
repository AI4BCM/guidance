## What it does

`prepare-bia` drafts the guide for one BIA interview from the material you already hold: other sites' activity
lists, the organisation structure, the impact criteria. It asks you only about the interview itself, who it is with
and what you need back from them, and never about the activity, because the activity owner is the person who knows
that. Everything it drafts is a **candidate**: a question for the owner to correct, with every recovery time left
blank.

## When to reach for it

You invoke this by typing `/prepare-bia`, and the AI won't reach for it on its own. Reach for it before a BIA
interview or workshop, when the material is on your desk and the questions for the activity owner are not.

| You have | Reach for |
| --- | --- |
| Material, and an interview coming | `/prepare-bia` |
| The interview record, and a BIA to finish | the [AI4BCM BIA-Workflow](https://ai4bcm.org/plug-it-in/) |
| An approved BIA, and a plan or change to compare with it | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/check-against-bia/SKILL.md) |

## The guide is made of candidates

Two questions come first: who the interview is with (a role is enough) and what you need back, for example
"resources and peak weeks". Each thing you need back gets its own question in the guide. Then the draft: candidate
activities, their resources in four classes (people, seats and buildings, IT with its RTO and RPO, suppliers) and
their dependencies on other departments, each labelled "candidate, to confirm" and tied to the document it came
from. Where no document supports an entry, the guide asks about it instead. MTPD, RTO and RPO stay empty; a time
quoted from another department's confirmed BIA sits in a note under the table, with its source and date.

The questions read like a questionnaire for someone else: most important first, grouped by theme, one idea each,
with "I don't know" welcome and a closing "anything else?".

## Common questions

**Why are the recovery times empty?**
The activity owner sets MTPD and RTO, and top management approves the BIA. A field the AI filled in looks the same
as one the owner set, so the guide keeps it visibly blank. A BC manager who prepares these every month called the
empty fields "exactly right".

**I have no impact criteria to attach. What happens?**
It asks for them as one of its intake questions, before drafting.

**Can it enter the confirmed answers in our register after the interview?**
No. It returns a draft in the chat and writes to nothing. After the interview the work continues in the AI4BCM
BIA-Workflow, which takes the interview record through to a signed BIA.

**Can I use it for a workshop with three activity owners?**
Yes: one run, with the owners listed.

## It's working if

- It asks you at most three questions, about the interview and not the activity, then drafts.
- The guide opens with each source document's version and date, and names undated ones under Gaps.
- Every line reads "candidate, to confirm" and names its document; the recovery columns are blank.
- Every item you said you need back has a question in the guide.
- The reply ends by handing over to the BIA-Workflow.

## Where it fits

`prepare-bia` is the Analysis stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). It runs before the
interview; the [BIA-Workflow](https://ai4bcm.org/plug-it-in/) takes over after it, because the interview record is
where a signed BIA starts. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/ask-ai4bcm/SKILL.md) names it.
