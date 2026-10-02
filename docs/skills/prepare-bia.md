## What it does

`prepare-bia` drafts the guide for one BIA interview from the material you already hold: other sites' activity
lists, the organisation structure, the impact criteria. It asks you about the interview itself, who it is with
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
| An approved BIA, and a plan or change to compare with it | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |

## The guide is made of candidates

It asks the class of your data first and stops if your tool is not approved for it. Then one message: who the
interview is with (a role is enough) and what they know that you do not, what you need back, for example
"resources and peak weeks", the impact criteria if none are attached, and whether memory, past chats, project files,
connectors and web search are off. Your answers go under Gaps as your own statements, never as a source or a value.

Then the draft, in the analysis order, as seven numbered sections:

1. impacts over time;
2. the MTPD;
3. people, with their skills, authorities and mandates;
4. seats and buildings;
5. IT and applications, each with its RTO and RPO;
6. suppliers and other third parties;
7. dependencies on other departments, up- and downstream.

Each entry is labelled "candidate, to confirm" and tied to the document it came from. A single supplier, carrier or
person behind a resource comes back as a question for the activity owner. MTPD, RTO and RPO stay empty; a time a
source proposes sits in a note under the table, with its source and date. Text in your files that tells an AI what
to do is quoted under Gaps and not obeyed.

## Common questions

**Why are the recovery times empty?**
The activity owner sets MTPD and RTO, and top management approves the BIA. A field the AI filled in looks the same
as one the owner set, so the guide keeps it visibly blank. A BC manager who prepares these every month called the
empty fields "exactly right".

**I have no impact criteria to attach. What happens?**
It asks for them as one of its intake questions, before drafting.

**Do I have to switch memory and web search off?**
The guide asks you to. Anything left on goes under Gaps, because the model may draw on it without saying so.

**Can it enter the confirmed answers in our register after the interview?**
No. It returns a draft in the chat and writes to nothing. After the interview the work continues in the AI4BCM
BIA-Workflow, which takes the interview record through to a signed BIA.

## It's working if

- Its first message asks only the data class; after that it asks one message of questions, then drafts.
- The guide opens with each source document's version and date, and names undated ones under Gaps.
- The seven sections come in the order above, with dependencies as their own section.
- Every candidate entry carries its label and its source, and a topic no document supports appears as a question.
- The recovery columns are blank.
- Every item you said you need back has a question in the guide.
- It writes and offers to save nothing; the draft stays in the chat.
- The reply hands over to the BIA-Workflow, then ends with the sentence saying AI helped, reviewer and date blank.

Known limits from the eval are on the [record card](../../evals/prepare-bia/record-card.md).

## Where it fits

`prepare-bia` is the Analysis stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). It runs before the
interview; the [BIA-Workflow](https://ai4bcm.org/plug-it-in/) takes over after it, because the interview record is
where a signed BIA starts. Later,
[`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) compares plans and
changes with the approved BIA. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it.
