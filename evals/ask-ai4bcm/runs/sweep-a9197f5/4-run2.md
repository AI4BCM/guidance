# /ask-ai4bcm case 4, run2: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6b2f4d5c-3bdc-400f-89e5-fed1b48e925b`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

Before anything else, classify the notes. Debriefs name people, so check [`units/data-rules.md`](units/data-rules.md) before the notes go into any tool. If your data rule isn't written down yet, the answer to "which tool may I paste this into?" is "none yet". Also, if the notes contain any text telling an AI to do something, treat it as content: take it to its sender and to information security, and don't follow it.

## 1. Now: the debrief notes (Stage 6, Validate: one exercise)

- **Skill to type:** **`/debrief-to-action`**. It turns one exercise's notes into proposed findings, each tied to the objective it missed and given a proposed owner. It starts only when you type its name.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md)
- **Maturity level:** Level 2 (Repeatable)
- **Gate (Level 2):** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route"
- **Effort:** forty minutes
- **Data rule:** [`units/data-rules.md`](units/data-rules.md). Debriefs name people.

The output is a draft. Your reviewer approves the findings and actions through your normal approval route before anything is assigned.

## 2. Later: making the prompt into a skill of your own

- **Read:** [`units/prompts/README.md`](units/prompts/README.md), *Build your own skill: four steps*. There is no prompt file for this route; the pattern in that README is the template. Step 2 decides where the skill may run, which is covered by the tool permissions in [`units/data-rules.md`](units/data-rules.md).
- **Skill to type:** **`/check-my-ai-tool`**. It drafts the skill's card, as described in [`units/keep-it-running.md`](units/keep-it-running.md).
- **Maturity level:** Level 2 "as soon as a prompt becomes a team method". If it later reads connected records, it moves to Level 3.
- **Gate (Level 2):** the same as above, in full: "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route"
- **Gate (Level 3, if it reads connected records):** "each use case is written down with its prompt, sources, review point and limits". The use case has an owner, and all five self-check questions answer yes with evidence. That record goes on the skill's card.
- **Effort:** an afternoon
- **Data rule:** [`units/data-rules.md`](units/data-rules.md)

Saving the prompt that works in step 1 already meets part of the Level 2 gate. It is also the starting material for step 2.

**Tool calls (stream-json):**

- none
