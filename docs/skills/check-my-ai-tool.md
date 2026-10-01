## What it does

`check-my-ai-tool` drafts the record for one skill, workflow or saved prompt from what you attach: its description,
its settings and permissions as set in the tool, its sources with dates, its version. It drafts only what your
attachments show, and every field a person answers for stays blank with its question, even when you have told it the
answer.

## When to reach for it

You invoke this by typing `/check-my-ai-tool`, and the AI won't reach for it on its own. Reach for it when a saved
prompt, skill or workflow becomes a team method, before the team relies on it.

| You have | Reach for |
| --- | --- |
| A saved prompt, skill or workflow the team will rely on | `/check-my-ai-tool` |
| A tool someone wants to install, not yet approved | [Before you approve a tool](https://github.com/AI4BCM/guidance/blob/main/units/tools.md) in the tools unit (no skill) |
| BCMS records to sort against your evidence checklist | [`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) |

## One record, your fields blank

What you record decides what you get, one or the other, never both:

| You record | You get |
| --- | --- |
| A saved prompt | One line for your organisation's list of AI tools: what it does, who owns it, which approved tool it runs in, how sensitive the data may be |
| A skill or workflow that reads or acts on files | A card with the twelve fields of the [record card](https://github.com/AI4BCM/guidance/blob/main/units/keep-it-running.md) |
| The AI4BCM skills | One card for the set, because you install them as one tool |

The fields a person answers for come back **blank**, each with the question it needs answered: Owner, Deputy,
Reviewer, Fallback, Retire when, Decision or input and Tests last run on a card, and Who owns it on a list line. The
never-alone test comes with either: the test input, the pass and fail lines, and a blank evidence block for you to
fill once you have run it. Nothing is approved either: the card has no approver field, and the approver is your
organisation's AI tool owner, a role you name.

## Common questions

**Does it run the never-alone test for me?**
No. It drafts the test input with the unit's pass and fail lines, and an empty evidence block. You run the test, fill
the block, and copy the date and result to Tests last run.

**I told it who owns the tool. Why is Owner still blank?**
The fields a person answers for stay blank with their question, and you write them in. A typed answer fills none of
them.

**We only saved a prompt. Does it need a card?**
No: one line in your organisation's list of AI tools.

**Why one card for all the AI4BCM skills, and not one per skill that reads my files?**
You install them as one tool, so they share one card. One card per skill that reads files was proposed, and not
adopted.

**Where is the approver on the card?**
The card has no approver field. One line under it names the next step: the approver is your organisation's AI tool
owner, a role you name.

## It's working if

- The record opens with the version and date of what it describes.
- A saved prompt got one line, and a skill or workflow a card, never both.
- Each drafted field names the attachment it came from.
- Owner, Deputy, Reviewer, Fallback, Retire when, Decision or input and Tests last run are blank, each with its
  question beside it, the ones you answered included.
- The test evidence block is empty.
- Nothing comes back approved.
- The reply ends on what you do next for your branch.

## Where it fits

`check-my-ai-tool` is the Keep-it-running stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before
it come steps 1 to 5 of
[Build your own skill](https://github.com/AI4BCM/guidance/blob/main/units/prompts/README.md), which set the task, the
data class, the permissions and the tests the card records. After it come your own steps: the approval checklist in
the [tools unit](https://github.com/AI4BCM/guidance/blob/main/units/tools.md) and the who-to-tell round.
[`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) is
its neighbour, because it sorts BCMS records, a finished card among them, against your evidence checklist, while this
skill drafts the record. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes any
other request to the right prompt or skill.
