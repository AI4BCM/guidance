# $ask-ai4bcm case 4, run2: Codex, guidance at a9197f5

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1077b-297c-74c2-9219-dc94e693f22c`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using **ask-ai4bcm** to name the route for your debrief and the later skill-building step. Its instructions require me to route and stop until you type the next skill’s name.

First, apply the [data rule](.agents/skills/ask-ai4bcm/units/data-rules.md): debriefs containing personal data or control weaknesses are high-sensitivity and belong only in an approved corporate or private environment, with permissions and retention approved. Passwords, keys and tokens go into no tool.

- **Now — Validate:** type **`/debrief-to-action`**. Read [Validate](.agents/skills/ask-ai4bcm/units/stages/validate.md), Task choice 2, alongside [Exercise](.agents/skills/ask-ai4bcm/units/prompts/exercise.md). It proposes findings tied to the exercise objective and quoted notes, plus actions and proposed owners where the sources name them. Your accountable reviewer decides which become findings; proposed owners confirm their actions. **Level 2, Repeatable; about forty minutes.**
- **Later — your own skill:** read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md): choose one narrow task, check where it may run, write the prompt from the pattern, and test it on past work with human review. Type **`/check-my-ai-tool`** to draft its record card using [Keep it running](.agents/skills/ask-ai4bcm/units/keep-it-running.md). **Level 2 as soon as it becomes a team method; an afternoon.** The same data rule applies.

**Level 2 gate for both:** “the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.”

If the later skill reads connected records, it needs **Level 3**: each use case is written down with its prompt, sources, review point and limits, has an owner, and all five self-check questions answer yes with evidence; record this on its card.

I’m stopping at routing because [ask-ai4bcm’s SKILL.md](.agents/skills/ask-ai4bcm/SKILL.md) says it “never runs a skill or any step of one.” The next skill starts only when you type its name.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "cat .agents/skills/ask-ai4bcm/SKILL.md; rg --files -g 'data-rules.md' -g 'levels.md' -g 'validate.md' -g 'exercise.md' -g 'README.md' -g 'keep-it`
- command_execution: `/bin/bash -lc "ls -a; rg --files --hidden -g 'data-rules.md' -g 'levels.md' -g 'validate.md' -g 'exercise.md' -g 'README.md' -g 'keep-it-running.md'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/skills/ask-ai4bcm/units/prompts/READ`
