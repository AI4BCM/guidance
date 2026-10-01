## What it does

`role-card` rewrites one approved document for one audience: a role card for one role from an approved plan, or
a message for one staff group from an approved policy and its awareness notes. It adds nothing the document does
not hold, and each line names the section it came from. Where the material you attach shows the wording will not
fit that audience's site or role, it flags the mismatch and leaves it unfixed for the reviewer to decide.

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

Each run writes for one **audience**. Every wording choice is made for that reader, and the list of changes is
written for them too. Ask for shift leaders, line managers and new starters at once, and you get the first and a
note that the other two are separate runs.

Adapting changes the wording and never the approved intent. When the attached material shows something will not
work for this audience, such as a number the contact list marks as retired or an example taken from another site,
the skill **flags** it under Gaps and leaves the wording as the source has it. Where the material cannot say whether
something fits your site, Gaps puts it to you as a question.

## Common questions

**Can it turn a 40-page plan into a one-page card?**
Yes, for one role at a time, each line cited to its plan section. What the role does not need is listed as left
out, with the reason.

**How will I know the card is out of date?**
The plan version and date sit at the top of the card, so a card older than the plan shows it.

**Can it put the card into the plan, or send it to the shift leaders?**
No. It returns a draft in the chat. The plan owner approves the card and versions it with the plan, and that
approval lets the owner make the edit, never the skill.

## It's working if

- The card or message opens with the plan or policy version and date.
- Every line names the section it came from.
- Nothing in it is missing from the approved document.
- Each action or contact for your audience that the draft leaves out is listed, with the reason.
- A mismatch the attached material shows (a number marked as retired, an example from another site) is listed under
  Gaps and still stands in the draft for you to decide.
- Where the material cannot settle whether something fits your site, Gaps puts it to you as a question.
- You got one card or message, for one audience.

## Where it fits

`role-card` is the Embed stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/); for a role card it
runs the Implement stage prompt's fourth Task choice. Before it,
[`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md), because a card drawn from a plan that disagrees with
the BIA carries the disagreement to the people who act on it. After it, the reviewer releases the draft through the
normal route. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes you to the skill for your stage.
