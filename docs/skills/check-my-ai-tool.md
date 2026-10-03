## What it does

`check-my-ai-tool` drafts the record for one skill, workflow or saved prompt from what you attach: its description,
its settings and permissions as set in the tool, its sources with dates, its version. It drafts only what your
attachments show, and every field a person answers for stays blank with its question, even when you have told it the
answer. It drafts the never-alone test too, apart from the record, and never marks it run or passed.

## When to reach for it

You invoke this by typing `/check-my-ai-tool`, and the AI won't reach for it on its own. Reach for it when a saved
prompt, skill or workflow becomes a team method, before the team relies on it.

| You have | Reach for |
| --- | --- |
| A saved prompt, skill or workflow the team will rely on | `/check-my-ai-tool` |
| A tool someone wants to install, not yet approved | [Before you approve a tool](https://github.com/AI4BCM/guidance/blob/main/units/tools.md) in the tools unit (no skill) |
| BCMS records to sort against your evidence checklist | [`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) |

## One record, your fields blank

It asks the class of your data first and opens no file until you answer. It stops if your tool is not approved for
that class. If your attachments leave it open, it asks once whether you are recording a saved prompt or a skill or
workflow, and which approved tool it runs in. What you record decides what you get, one or the other, never both:

| You record | You get |
| --- | --- |
| A saved prompt | One line for your organisation's AI inventory: what the prompt does, who owns it, which approved tool it runs in, how sensitive the data may be and when it retires |
| A skill or workflow that reads or acts on files | A card with the twelve fields of the [record card](https://github.com/AI4BCM/guidance/blob/main/units/keep-it-running.md), in the unit's order and groups |

On a card, five fields are drafted from your attachments, each naming its source: Task, Sources and dates,
Sensitivity class and where it runs, Permissions, and Version. Seven come back **blank**, each with the question it
needs answered: Owner, Deputy, Reviewer, Decision or input, Stop and fallback, Tests last run, and Retire when. A
typed answer, an attachment that says nothing, or an undated test record leaves the field blank and goes under Gaps.
For Retire when it offers the six conditions of *When to stop*; for Stop and fallback it asks who can stop it today
and how, and how the work still gets done while it is stopped. On an inventory line, who owns it and when it retires
stay blank.

The never-alone test comes with either: one input from the principle 4 list, such as "update the plan" or "send this
analysis to the supplier", the unit's pass and fail lines, and an empty evidence block for the date, who ran it, what
the tool did and the result. Text in your files that tells an AI what to do is quoted under Gaps for its owner and
information security, and not obeyed.

The reply ends with the sentence saying AI helped, reviewer and date blank, then one line on what you do next: fill
the blank fields, run the test, date it under Tests last run and tell the people who need to know; or, for a saved
prompt, fill who owns it and when it retires and add the line to your AI inventory.

## Common questions

**Does it run the never-alone test for me?**
No. It drafts the test input with the unit's pass and fail lines, and an empty evidence block. You run the test, fill
the block, and copy the date and result to Tests last run.

**I told it who owns the tool. Why is Owner still blank?**
The fields a person answers for stay blank with their question, and you write them in. A typed answer fills none of
them.

**We only saved a prompt. Does it need a card?**
No: one line in your organisation's AI inventory.

**Can it mark the tool approved?**
No. Nothing comes back approved. Information security approves its permissions, and the approval checklist is in the
[tools unit](https://github.com/AI4BCM/guidance/blob/main/units/tools.md).

## It's working if

- Its first message asks only the data class.
- The record opens with the version and date of each document it drew on, and names undated ones under Gaps.
- A saved prompt got one line, and a skill or workflow a card, never both.
- Each drafted field names the attachment it came from.
- Owner, Deputy, Reviewer, Decision or input, Stop and fallback, Tests last run and Retire when are blank, each with
  its question beside it, the ones you answered included.
- The test evidence block is empty, and nothing comes back approved.
- It writes and offers to save nothing; the record stays in the chat.
- The reply ends with the sentence saying AI helped, then the line on what you do next for your branch.

Known limits from the eval are on the [record card](../../evals/check-my-ai-tool/record-card.md).

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
