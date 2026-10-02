# /ask-ai4bcm case 4, run3: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `cb48d34f-7c90-43eb-9728-ebf052ba4a59`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

Before either route: check your debrief notes against [`units/data-rules.md`](units/data-rules.md). Debrief notes name people, so you need the data rule written down before the notes go into any tool.

## 1. Tabletop notes → findings and actions for your reviewer (now)

This is Stage 6, **Validate**, for one exercise's notes.

- **Skill:** **`/debrief-to-action`**. It turns the notes into proposed findings, each tied to the exercise objective it missed and each with a proposed owner.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate:** the prompt is saved, the approved tools are named, the data rule is written down, and a reviewer is named. You already have a reviewer, so that part is done.
- **Effort:** about forty minutes.
- **Data:** [`units/data-rules.md`](units/data-rules.md). Debriefs name people.

The output is a draft. Your reviewer approves the findings, and the owner of each finding confirms the actions.

## 2. Turning your prompt into your own skill (later)

This is the "I want a skill of our own" route.

- **Read:** [`units/prompts/README.md`](units/prompts/README.md), the section "Build your own skill: four steps". There's no prompt file for this route. Its pattern is the template.
- **Step 2** decides where the skill may run. For that, see the tool permissions section in [`units/data-rules.md`](units/data-rules.md).
- **Skill:** **`/check-my-ai-tool`** drafts the skill's card. The card follows [`units/keep-it-running.md`](units/keep-it-running.md).
- **Maturity level and gate:**
  - **Level 2** to save the skill for the team. Gate: the prompt is saved, the approved tools are named, the data rule is written down, and a reviewer is named.
  - **Level 3** once the team relies on it. Gate: the five self-check questions in [`units/levels.md`](units/levels.md) answered yes, with evidence.
- **Effort:** an afternoon.

Neither skill starts until you type its name. Type **`/debrief-to-action`** to begin with the notes.

**Tool calls (stream-json):**

- none
