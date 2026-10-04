# /ask-ai4bcm case 4, run1: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3dffdc7a-f5ba-4094-892b-6cbddab137ea`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

You're asking for two separate things, so there are two routes. Before either one, classify your data: [`units/data-rules.md`](units/data-rules.md) applies first. Debrief notes name people, so check which tool they may go into before you paste them anywhere.

## 1. Last week's tabletop notes → findings and actions

This is **Stage 6, Validate: one exercise's notes.**

- **Skill:** **`/debrief-to-action`** turns the notes into proposed findings tied to the missed objective, each with a proposed owner. It only starts when you type its name. I haven't run it or any step of it.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md)
- **Maturity level:** Level 2, Repeatable
- **Gate (Level 2's):** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route"
- **Effort:** forty minutes
- **Data rule:** [`units/data-rules.md`](units/data-rules.md). Debriefs name people.

**Next:** the result is a draft. Your named reviewer checks it, and it then goes through your normal approval route. The owners and actions in it are proposals until the people named accept them.

## 2. Later: turning your prompt into a skill of your own

This is the on-ramp **"I want a skill of our own."**

- **Read:** [`units/prompts/README.md`](units/prompts/README.md), *Build your own skill: four steps*. There's no separate prompt file because the README's pattern is the template. Step 2 decides where the skill may run, using the tool permissions in [`units/data-rules.md`](units/data-rules.md).
- **Skill:** **`/check-my-ai-tool`** drafts the skill's card ([`units/keep-it-running.md`](units/keep-it-running.md)). It starts when you type it.
- **Maturity level:** Level 2 "as soon as a prompt becomes a team method". It becomes Level 3 once the skill reads connected records.
- **Gate:** Level 2's, as written above. If it later reads connected records, Level 3's applies: "each use case is written down with its prompt, sources, review point and limits", it has an owner, and all five self-check questions answer yes with evidence. That evidence goes on the skill's card.
- **Effort:** an afternoon
- **Data rule:** [`units/data-rules.md`](units/data-rules.md)

**Order:** do route 1 first. Running `/debrief-to-action` on real notes and having the result reviewed tells you which prompt worked well enough to save, and that saved prompt is what route 2 turns into a skill.

**Tool calls (stream-json):**

- none
