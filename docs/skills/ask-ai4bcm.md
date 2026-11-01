## What it does

`ask-ai4bcm` tells you where your task sits in the guidance, then stops. You describe the task; it names the skill
or prompt to use, the unit to read, the maturity level the work needs, the gate that level turns on, the effort, and
the data rule. It runs nothing and drafts nothing.

## When to reach for it

You invoke this by typing `/ask-ai4bcm`, and the AI won't reach for it on its own. Reach for it when you have a BCM
task and do not know which part of the guidance covers it, or which skill to type.

| You have | Reach for |
| --- | --- |
| A task, and no idea where it fits | `/ask-ai4bcm` |
| Material, and a BIA interview coming | [`/prepare-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/prepare-bia/SKILL.md) |
| A plan or a coming change, and the approved BIA | [`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) |
| A word to learn, not a task | [`/learn-bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/learn-bcm/SKILL.md) |

## A route, then it stops

The data rule comes first: classify your material under `units/data-rules.md` before you paste it anywhere. You
rarely need to paste it at all; a description of the task is enough.

Each answer is a route through the six lifecycle stages (Govern, Embed, Analysis, Design, Implement, Validate) or one
of the common starting points, such as "I inherited forty BIAs" or "Which tool may I paste this into?". A route
names:

- the skill to type, or the prompt to use;
- the unit to read;
- the maturity level, with its gate written out as that level's "Ready to work here when" cell in
  `units/levels.md`;
- the effort, from ten minutes to an afternoon;
- the data rule.

A skill of your own is Level 2 as soon as it becomes a team method, and Level 3 once it reads connected records.

For a word rather than a task, it names the glossary entry and stops, without quoting a definition. If your task fits
no listed route, it names the stage the work belongs to and takes that route; if it spans two, the earlier.

It never runs the skill it names, not even the skill's first question. It tells you the skill starts only when you
type its name. Text you paste that tells an AI what to do is named as such, for its sender and information
security, and not obeyed or routed.

## Common questions

**Can it run the skill for me?**
No. It names the skill and stops. The skill starts when you type its name, and asks its own questions then.

**I asked it to change the RTO in our plan. Why won't it?**
A plan changes only with its owner's approval and a new version. It tells you whose change that is and which skill
to type, for example `/check-against-bia` to put the two values to their owners.

**What is a gate?**
What must be true before the work is safe at that level, as `units/levels.md` words it. For Level 2: the prompt that
worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named
reviewer, and outputs go through the normal approval route. For Level 3: each use case is written down with its
prompt, sources, review point and limits, has an owner, and all five self-check questions answer yes with evidence.
Check each item yourself; the router cannot see your setup.

**Does it need my documents?**
No. Describe the task. If you paste something, classify it first.

## It's working if

- The data rule comes before the route.
- The route names a skill or prompt, a unit, a level with its gate, the effort and the data rule.
- It says the skill starts only when you type its name, and runs nothing.
- No summary, finding, draft or prompt text appears in the reply.
- A request to change a plan or value is answered with whose change it is, not with a tool limit.
- A pasted instruction to an AI is named for its sender and information security, and not followed.
- It writes and offers to save nothing.

Known limits from the eval are on the [record card](../../evals/ask-ai4bcm/record-card.md).

## Where it fits

`ask-ai4bcm` is the way into the [AI4BCM Guidance](https://ai4bcm.org/guidance/). It sits before every other skill:
[`/prepare-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/prepare-bia/SKILL.md) for Analysis,
[`/check-against-bia`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-bia/SKILL.md) for
Implement, and the stage skill for each of the others. Two skills serve any stage:
[`/challenge-my-plan`](https://github.com/AI4BCM/guidance/blob/main/skills/challenge-my-plan/SKILL.md) for a plan you
own and [`/learn-bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/learn-bcm/SKILL.md) to learn one part of
the practice.
