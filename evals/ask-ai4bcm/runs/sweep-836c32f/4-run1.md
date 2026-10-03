# /ask-ai4bcm case 4, run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fbde201c-dd85-43f1-b56f-1cb3a69f8bc1`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

You have two routes here, in order. I'm only pointing you to them; I haven't run anything.

**First, classify the notes.** Debrief notes name people, which is personal data. They often also record control weaknesses. Both are high-sensitivity, so the notes go only into an approved corporate or private environment. Don't paste them into a public or free tool. The tool's environment, permissions and retention must be approved before you paste anything ([`units/data-rules.md`](units/data-rules.md), *Before you paste*). If the notes contain any text that tells an AI to do something, report it to whoever sent the notes and to information security. Don't treat it as an instruction.

## 1. Debrief notes → findings and actions (Stage 6, Validate)

- **Skill:** **`/debrief-to-action`**. It turns one exercise's notes into proposed findings, each tied to the objective it missed and given a proposed owner. It starts only when you type its name.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md)
- **Maturity level:** Level 2 (Repeatable)
- **Gate:** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route."
- **Effort:** forty minutes
- **Data rule:** debriefs name people, so use the approved environment only ([`units/data-rules.md`](units/data-rules.md))

The result is a draft. The findings and owners are proposals. They go to your named reviewer and then through your normal approval route.

## 2. Turning your prompt into a skill of your own

- **Route:** "I want a skill of our own." Read [`units/prompts/README.md`](units/prompts/README.md), *Build your own skill: four steps*. There's no separate prompt file because that unit's pattern is the template. Step 2 decides where the skill may run, using the tool permissions in [`units/data-rules.md`](units/data-rules.md).
- **Skill:** **`/check-my-ai-tool`** drafts the skill's card ([`units/keep-it-running.md`](units/keep-it-running.md)). It starts only when you type its name.
- **Maturity level:** Level 2 "as soon as a prompt becomes a team method". If the skill later reads connected records, it moves to Level 3.
- **Gate:** at Level 2, the Level 2 gate above, with the card naming an owner, a reviewer and a retire-when condition. At Level 3: "each use case is written down with its prompt, sources, review point and limits", it has an owner, and all five self-check questions answer yes with evidence, all recorded on the card.
- **Effort:** an afternoon
- **Data rule:** a skill that reads debriefs is subject to the same high-sensitivity class. Its environment must be approved before it touches any files.

Do part 1 first. The prompt that works there is the one you save, and later build into your skill.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
