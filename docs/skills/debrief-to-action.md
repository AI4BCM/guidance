## What it does

`debrief-to-action` turns the notes of one exercise into proposed findings, each tied to the objective it missed,
with what worked and the actions that follow. It judges the notes only against the objective written before the
exercise, taken from the plan or exercise brief you attach. With no such document attached it writes the Gaps and no
finding.

## When to reach for it

You invoke this by typing `/debrief-to-action`, and the AI won't reach for it on its own. Reach for it after one
exercise, when you hold its debrief notes and the plan or brief that states its objective.

| You have | Reach for |
| --- | --- |
| Notes from one exercise, and the objective written before it | `/debrief-to-action` |
| Reports from several exercises, and a site to plan for | the [Validate stage prompt](https://github.com/AI4BCM/guidance/blob/main/units/stages/validate.md), Task choice 1 (no skill) |
| A theme worth exercising | the [exercise prompt](https://github.com/AI4BCM/guidance/blob/main/units/prompts/exercise.md), through [`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) |
| BCMS records and your own evidence checklist | [`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) |

## Every finding is proposed

The AI proposes a theme; a person makes it a finding. So everything the skill returns is **proposed**: each finding
names the objective it missed and quotes the notes it rests on, and each action carries an outcome, a check that says
it is done, and an owner only where your notes or the plan name one, marked "proposed, to confirm". Nothing enters
the exercise report or the lessons log until the accountable reviewer decides it belongs there.

The narrative is **blameless**. A finding names the role, the step and the guard that was missing, never the person
who slipped; a "what worked" line names the role, the step and the safeguard that held. Naming the owner of an action assigns the action and blames no one, so the actions still carry names where your sources give them.

## Common questions

**Blameless means no names. Who owns the actions, then?**
Every action still needs a named person. It proposes an owner wherever your notes or the plan name one, marked
"proposed, to confirm". An action with no named owner goes under Gaps, and the reviewer names the person.

**Can I type the objective instead of attaching it?**
A typed objective is your own statement: it goes under Gaps and the run stops there. Attach the plan or exercise
brief that holds it.

**Will it suggest the next exercise?**
No. It ends at findings and actions. A theme worth exercising is a separate request, through `/ask-ai4bcm`.

## It's working if

- The top names the plan or brief the objective comes from, with its version and date.
- Every finding names the objective it missed and quotes your notes.
- Every finding names a role, a step and the guard that was missing; every "what worked" line names a role, a step
  and the safeguard that held.
- Every action has an owner your notes or plan named, marked "proposed, to confirm", or sits under Gaps.
- No person is named as the one who slipped.
- No next exercise is suggested.
- With no objective attached, you got the Gaps and nothing else.

## Where it fits

`debrief-to-action` is the Validate stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before it
comes the exercise, run against an objective written beforehand. After it, the accountable reviewer decides which
findings enter the exercise report or the lessons log, and each proposed owner confirms their action.
[`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) is
its neighbour, because it runs the third Task choice of the same Validate prompt, on your BCMS records and evidence
checklist. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes any
other request, a theme worth exercising included, to the right prompt or skill.
