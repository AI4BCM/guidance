## What it does

`debrief-to-action` turns the notes of one exercise into proposed findings, each tied to the part of the objective it
missed, with what worked and the actions that follow. It judges the notes only against the objective written before
the exercise, quoted from the plan or exercise brief you attach. With no such document attached it writes the Gaps
and stops. It records, assigns and sends nothing.

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

It asks the class of your data first and opens no file until you answer. It stops if your tool is not approved for
that class. It then quotes the objective from your brief or plan and asks nothing about it. It may ask up to three
questions on what your files leave open, and lists your answers under Gaps as your own statements. The first lines
name each attached document's version and date. The notes keep their own status there, are quoted and never edited,
and stay the raw record; the draft is the analysis.

The AI proposes a theme; a person makes it a finding. So everything the skill returns is **proposed**. Each finding
names the part of the objective it missed and quotes the note it rests on. What worked is set out apart, against the
same objective. Each action carries an outcome, a check that says it is done, and an owner only where your notes or
the plan name one, marked "proposed, to confirm". An action with no named owner goes under Gaps. Nothing enters the
exercise report or the lessons log until the accountable reviewer decides it belongs there.

The narrative is **blameless**. A finding names the role and the step, never the person who slipped: the role goes in
brackets, such as `[night security]`, or the quotation stops before the name. Naming the owner of an action assigns
the action and blames no one, so the actions still carry names where your sources give them.

It weighs findings by their consequences and the quoted evidence, or leaves the order to the reviewer. One exercise
shows no recurrence, so recurrence reads "not in the sources", and there is no score. How the exercise was run goes
under Gaps for the reviewer and is never a finding. A note from after the end of the brief's scope, or one for the
next exercise, gives no finding and no what-worked line: it goes under Gaps as outside the objective, or is left out.
Text in your files that tells an AI what to do is quoted under Gaps for its owner and information
security, and not obeyed.

After the sentence saying AI helped, one line hands the draft on, by role and never by name: put these to the people
who were there; the accountable reviewer decides which become findings; each proposed owner confirms their action.
Nothing follows it.

## Common questions

**Blameless means no names. Who owns the actions, then?**
Every action still needs a named person who closes it. It proposes an owner wherever your notes or the plan name one,
marked "proposed, to confirm". An action with no named owner goes under Gaps, and the reviewer names the person.

**Can I type the objective instead of attaching it?**
A typed objective is your own statement: it goes under Gaps, and nothing is judged against it. Attach the plan or
exercise brief that holds it.

**Can it enter the findings in the lessons log?**
No. It records, assigns and sends nothing. The accountable reviewer decides what enters the report or the log.

**Will it suggest the next exercise?**
No. It ends at findings and actions. A theme worth exercising is a separate request, through `/ask-ai4bcm`.

## It's working if

- Its first message asks only the data class.
- The top names the plan or brief the objective comes from, with its version and date, and the notes with their own
  status.
- The objective is quoted from that document, not asked for.
- Every finding names the part of the objective it missed and quotes your notes.
- What worked sits apart from the findings.
- No person is named as the one who slipped.
- Every action has an outcome, a check and an owner your notes or plan named, marked "proposed, to confirm", or sits
  under Gaps.
- No finding is ranked on recurrence, and nothing carries a score.
- No next exercise is suggested.
- The draft ends with the sentence saying AI helped, reviewer and date blank, then the hand-over line by role.
- With no objective attached, you got the Gaps and nothing else.

Known limits from the eval are on the [record card](../../evals/debrief-to-action/record-card.md).

## Where it fits

`debrief-to-action` is the Validate stage skill in the [AI4BCM Guidance](https://ai4bcm.org/guidance/). Before it
comes the exercise, run against an objective written beforehand. After it, the accountable reviewer decides which
findings enter the exercise report or the lessons log, and each proposed owner confirms their action.
[`/check-against-standards`](https://github.com/AI4BCM/guidance/blob/main/skills/check-against-standards/SKILL.md) is
its neighbour, because it runs the third Task choice of the same Validate prompt, on your BCMS records and evidence
checklist. When you are unsure which skill fits your task,
[`/ask-ai4bcm`](https://github.com/AI4BCM/guidance/blob/main/skills/ask-ai4bcm/SKILL.md) names it, because it routes any
other request, a theme worth exercising included, to the right prompt or skill.
