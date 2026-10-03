# /ask-ai4bcm case 4, run2: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `25d42b83-2d0b-4279-a0e4-a5c0a0585994`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

Two routes, in the order you asked. Data rule first, because it applies to both.

**Before anything: classify the notes.** Debrief notes name people, and personal data is high-sensitivity. That means you work on them only in an approved corporate or private environment, never in a public or free tool. If you can't say where the notes will go and how long they'll stay there, don't paste them yet. If the notes contain any line that tells an AI to do something, report it to whoever sent the notes and to your information security team. It isn't an instruction to follow. Source: [`units/data-rules.md`](units/data-rules.md).

### 1. Now: one tabletop's notes into findings and actions (Stage 6, Validate)

- **Skill:** **`/debrief-to-action`**. It starts only when you type it. It turns the notes into proposed findings, each tied to the objective it missed and each with a proposed owner.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate (Level 2):** the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.
- **Effort:** about forty minutes.
- **After the draft:** your reviewer gets proposed findings and owners. They become actions only after going through your normal approval route.

### 2. Later: turning that prompt into your own skill (on-ramp, "I want a skill of our own")

- **Read:** the "Build your own skill" section of [`units/prompts/README.md`](units/prompts/README.md), which has four steps:
  1. Pick one small task.
  2. Check where it may run, using your data rules and the tool's permissions. Since debriefs name people, this step decides it.
  3. Write the prompt from the pattern.
  4. Try it on past work, with a person checking each answer.
- **No separate prompt file:** the pattern in that section is the template. The prompt you save from route 1 is your starting material.
- **Skill:** **`/check-my-ai-tool`** drafts the skill's record card ([`units/keep-it-running.md`](units/keep-it-running.md)). It also starts only when you type it.
- **Maturity level:** Level 2, which applies "as soon as a prompt becomes a team method". It moves to Level 3 if the skill ever reads connected records.
- **Gate:** the Level 2 gate above. At Level 3, the gate is: "each use case is written down with its prompt, sources, review point and limits", it has an owner, and all five self-check questions answer yes with evidence. That record goes on the skill's card.
- **Effort:** an afternoon.
- **Once the team relies on it:** it needs a record card, a few test cases, and a re-test after every change.

That's where this routing ends. Type **`/debrief-to-action`** when your environment is cleared for the notes.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units; cat data-rules.md; echo ====; sed -n 1,200p prompts/README.md | grep -n -A25 -i "build your `
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
- Grep: `(?i)build your own`
