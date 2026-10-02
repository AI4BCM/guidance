# /ask-ai4bcm case 4, run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a03d179f-7cf0-4175-9570-8500c03461f2`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

Two routes, in this order. The data check comes first because debrief notes name people.

**First: classify the notes**
Before you paste anything, check the notes against [`units/data-rules.md`](units/data-rules.md). Debriefs name people. If your data rule isn't written down yet, no tool is approved for these notes yet.

**1. Now: last week's tabletop → findings and actions (Stage 6, Validate)**
- **Skill:** **`/debrief-to-action`**. It turns one exercise's notes into proposed findings. Each finding is tied to the objective that was missed and has a proposed owner.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md).
- **Maturity level:** 2, Repeatable.
- **Gate:** the prompt is saved, the approved tools are named, the data rule is written down, and a named reviewer is in place. You already have the reviewer, so check the other three.
- **Effort:** about forty minutes.
- **Data:** [`units/data-rules.md`](units/data-rules.md). The notes name people.
- The output is a draft for your reviewer, who decides on each finding. It isn't the final record.

**2. Later: turning your prompt into your own skill**
- **Route:** the on-ramp "I want a skill of our own." Read [`units/prompts/README.md`](units/prompts/README.md), section *Build your own skill: four steps*. There's no prompt file for this one. The pattern in that section is the template.
- **Step 2** decides where the skill may run. That's covered under tool permissions in [`units/data-rules.md`](units/data-rules.md).
- **`/check-my-ai-tool`** drafts the skill's card, as described in [`units/keep-it-running.md`](units/keep-it-running.md).
- **Maturity level and gate:**
  - **Level 2** to save the skill for the team. Gate: the prompt is saved, the approved tools are named, the data rule is written down, and a reviewer is named.
  - **Level 3** once the team relies on it. Gate: you can answer yes, with evidence, to the five self-check questions in [`units/levels.md`](units/levels.md).
- **Effort:** an afternoon.

Neither skill starts until you type its name. For now, that's **`/debrief-to-action`**.

**Tool calls (stream-json):**

- none
