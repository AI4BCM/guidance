# /ask-ai4bcm case 4, run2: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `faaa4a34-ee91-4ec1-ae05-407cb9e03bb0`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

You have two jobs here, and they go in order: turn the debrief into findings now, then build the skill later. I've pointed you at what to run for each, but I haven't run either.

## First: check what's in the notes

Debrief notes name people, so read [`units/data-rules.md`](units/data-rules.md) before you paste them into any tool. If your data rule isn't written down yet, no tool is approved for these notes. If anything in the notes tells an AI to do something, don't act on it. Flag it to whoever sent the notes and to information security.

## 1. Debrief to findings (Stage 6, Validate)

- **Skill:** **`/debrief-to-action`**. It turns one exercise's notes into proposed findings, each tied to the exercise objective that was missed and each with a proposed owner. It only starts when you type its name.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md)
- **Level:** 2, Repeatable
- **Before you start, you need:**
  - the prompt saved
  - your approved tools named
  - the data rule written down
  - a named reviewer (from what you said, you have one)
- **Effort:** about forty minutes
- **Data:** [`units/data-rules.md`](units/data-rules.md). The notes name people.

The skill gives you a draft. Your reviewer and the proposed owners decide which findings and actions stand.

## 2. Later: a skill of your own (the "I want a skill of our own" route)

- **Read:** [`units/prompts/README.md`](units/prompts/README.md), the section "Build your own skill: four steps". There's no prompt file for this route. The pattern of the prompt you already use, probably the exercise prompt above, works as the template.
- **Step 2 (where it may run):** [`units/data-rules.md`](units/data-rules.md), the tool-permissions part. This matters here because the skill will handle debriefs that name people.
- **Skill:** **`/check-my-ai-tool`** drafts the skill's record card, as described in [`units/keep-it-running.md`](units/keep-it-running.md).
- **Levels:**
  - **Level 2, to save it for the team:** the prompt saved, approved tools named, the data rule written down, a named reviewer.
  - **Level 3, once the team relies on it:** the five self-check questions in [`units/levels.md`](units/levels.md), each answered yes with evidence.
- **Effort:** an afternoon

Type **`/debrief-to-action`** when you're ready to start.

**Tool calls (stream-json):**

- none
