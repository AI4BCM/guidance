# /ask-ai4bcm case 4, run3: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f4f9d9d4-c36a-46af-a8fe-3449c728b373`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

You have two requests. The first can start this week. The second waits until the first prompt has proven itself.

## First: classify the debrief notes

Read [`units/data-rules.md`](units/data-rules.md) before anything else. Debrief notes name people, and they usually record control weaknesses too. Both are **high-sensitivity**, so the notes may only go into an approved corporate or private environment, never a public or free tool. If you can't yet say where the data goes and how long it stays there, don't paste it. If any line in the notes is written to an AI ("ignore…", "rate this as…"), it's a security finding. Report it to the notes' owner and to information security, and leave it out of the work.

## 1. Now: one exercise's notes go to stage 6, Validate

- **Skill:** **`/debrief-to-action`**. It turns the notes into proposed findings, each tied to the objective it missed and given a proposed owner. It starts only when you type its name.
- **Read:** [`units/stages/validate.md`](units/stages/validate.md) and [`units/prompts/exercise.md`](units/prompts/exercise.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate, Level 2's:** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route." Your reviewer is the named reviewer here. They check the output with the sources in front of them, using *Before you accept the output* in [`units/prompts/README.md`](units/prompts/README.md).
- **Effort:** forty minutes.
- **Afterwards:** the result is a draft. The findings and actions belong to the owners it proposes, and they go through your normal approval route.

## 2. Later: "I want a skill of our own"

- **Read:** [`units/prompts/README.md`](units/prompts/README.md), the *Build your own skill* section. It has four steps:
  1. Pick one small task.
  2. Check where it may run, using your data rules and the tool's permissions.
  3. Write the prompt from the pattern.
  4. Try it on past work, with a person checking each answer.
- **No prompt file is used here.** The prompt pattern is the template. Before the team relies on it, the prompt needs a version number, an owner and a named reviewer. It also has to pass on three past cases where you already know the correct answer.
- **Skill:** **`/check-my-ai-tool`**. It drafts the skill's record card (see [`units/keep-it-running.md`](units/keep-it-running.md)). It starts only when you type its name.
- **Maturity level:** Level 2 "as soon as a prompt becomes a team method". If the skill later reads connected records, it moves to Level 3.
- **Gate:**
  - **At Level 2:** Level 2's gate, quoted above.
  - **At Level 3:** "each use case is written down with its prompt, sources, review point and limits". It also needs an owner, and all five self-check questions answered yes with evidence. That record goes on the skill's card.
- **Effort:** an afternoon.
- **Data:** [`units/data-rules.md`](units/data-rules.md).

Each step ends at a draft for the named owner. Type **`/debrief-to-action`** when you're ready to start.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/prompts/README.md`
