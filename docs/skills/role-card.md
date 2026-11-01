## What it does

`role-card` rewrites one approved document for one audience: a role card for one role from an approved plan, or
a message for one staff group from an approved policy. It adds nothing the document does not hold, and each line
names the section it came from. Where the other material you attach shows the wording will not fit, it flags the
mismatch and leaves it unfixed for the reviewer to decide. It publishes, records and sends nothing.

## When to reach for it

You invoke this by typing `/role-card`, and the AI won't reach for it on its own. Reach for it when a plan or
policy is approved and one group of people needs their part of it in words they will read: a shift leader's card
from a 40-page plan, an onboarding message for a new site.

| You have | Reach for |
| --- | --- |
| An approved plan, and one role that must act on it | `/role-card`, role card |
| An approved policy or awareness notes, and one staff group | `/role-card`, staff message |
| A draft plan to question before it is approved | [`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) |
| A plan to compare with the approved BIA | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |

## One audience, and a flag for what does not fit

It asks the class of your data first and opens no file until you answer. It stops if your tool is not approved for
that class. It may then ask up to three questions in one message, only on what your request leaves open: the
document, the audience (one role or group) and the format. It never asks what the document gives, such as its
version, status or role. Your answers go under Gaps as your own statements, never as a line or a source. A card runs
the [Implement stage prompt](https://github.com/AI4BCM/guidance/blob/main/units/stages/implement.md), Task choice 4,
with its Intake; a message runs the
[awareness prompt](https://github.com/AI4BCM/guidance/blob/main/units/prompts/awareness.md) as printed, with no Intake.

The draft opens with the behaviour it means to change, in one line. If your request does not say, that line is an
assumption and Gaps says so. The first lines name the approved document with its version and date. Each run writes
for one **audience**: ask for shift leaders, line managers and new starters at once, and you get the first, with the
others left for further runs.

Adapting changes the wording and never the approved intent. Wording copied from the document is quoted whole, never a
key word inside it, and wording of its own cites its section. Your other attachments are read for mismatches only and
never give a line. When they show something will not work for this audience, such as a number the contact list marks
as retired or a place from another site, the skill **flags** it under Gaps, naming both documents, and the line stays
as the source has it. Where the document has no source for a cell:

- a contact the plan lacks reads "contact: to be confirmed", never filled from elsewhere;
- each card step whose how, by whom or with what the plan leaves open gets a Gaps question for the reviewer, under
  "what the plan does not settle for this role", with nothing assumed;
- for a message, an approver the policy does not name reads "names none".

Text in your files that tells an AI what to do is quoted under Gaps, with a note to inform its owner and your
information security team. It never reaches the card or message, and it is not obeyed.

The draft ends with the sentence saying AI helped, reviewer and date blank, then one release line. For a card: the
plan owner approves and versions it with the plan, the team confirms the actions are realistic, and the effect is
reviewed with participation data and feedback. For a message: the approver the policy names, or none named, checks
accuracy, tone and local fit before release. Nothing follows it.

## Common questions

**Can it turn a 40-page plan into a one-page card?**
Yes, for one role at a time, each line cited to its plan section. What the role does not need is listed as left
out, with the reason.

**How will I know the card is out of date?**
The plan version and date sit at the top of the card, so a card older than the plan shows it.

**The contact list has a newer number. Will it use that?**
No. The card keeps the number the plan has and flags the mismatch under Gaps with both documents named. The plan owner,
as the card's reviewer, decides it.

**Can it put the card into the plan, or send it to the shift leaders?**
No. It returns a draft in the chat. The plan owner approves the card and versions it with the plan, and that
approval lets the owner make the edit, never the skill.

## It's working if

- Its first message asks only the data class.
- The draft opens with the behaviour line and the approved document's version and date.
- Every line names the section it came from, and copied wording is in quotation marks.
- Everything in it comes from the approved document.
- Each action or contact for your audience that the draft leaves out is listed, with the reason.
- A mismatch the attached material shows (a number marked as retired, a place from another site) is listed under
  Gaps with both documents named, and the line still stands as the source has it.
- Each step the plan leaves open (how, by whom, with what) is a question under Gaps, and nothing is assumed.
- A contact the plan lacks reads "contact: to be confirmed".
- You got one card or message, for one audience.
- The draft ends with the sentence saying AI helped, reviewer and date blank, then the release line.

Known limits from the eval are on the [record card](../../evals/role-card/record-card.md).

## Where it fits

`role-card` is the Embed stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/); for a role card it
runs the Implement stage prompt's fourth Task choice. Before it,
[`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md), because a card drawn from a plan that disagrees with
the BIA carries the disagreement to the people who act on it. After it, the reviewer releases the draft through the
normal route: for a card, the plan owner approves and versions it with the plan. When you are unsure which skill
fits your task, [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it,
because it routes you to the skill for your stage.
