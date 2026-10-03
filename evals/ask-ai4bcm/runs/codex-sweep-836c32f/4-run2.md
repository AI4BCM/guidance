# $ask-ai4bcm case 4, run2: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2d-17dd-76b3-9c04-b429c0a73fe1`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using ask-ai4bcm to identify the route for your debrief and the later reusable skill. It routes only; it stops before running either task.

Treat the debrief as **high sensitivity** if it names people or exposes weaknesses: use only an approved corporate or private environment, with permissions and retention approved first. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md). Never enter passwords, keys or tokens.

- **Now — Validate:** type **`/debrief-to-action`**. Read [Validate, Task choice 2](.agents/skills/ask-ai4bcm/units/stages/validate.md). It proposes findings tied to the exercise’s missed objective and supporting notes, plus actions with outcomes, completion checks and proposed owners. Your accountable reviewer accepts findings; proposed owners confirm actions. **Level 2, Repeatable; about forty minutes.**
- **Later — your own skill:** read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md): choose one narrow task, check its environment and permissions, use the prompt pattern, then test on past work with human review. There is no separate prompt file for this route. Type **`/check-my-ai-tool`** to draft its record card using [Keep it running](.agents/skills/ask-ai4bcm/units/keep-it-running.md). **Level 2 once the prompt becomes a team method; about an afternoon.**

**Level 2 gate for both:** the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.

If the future skill reads connected records, **Level 3** applies: each use case is written down with its prompt, sources, review point and limits, has an owner, is entered in the organisation’s AI inventory where one exists, and all five [self-check questions](.agents/skills/ask-ai4bcm/units/levels.md) answer yes with evidence; keep that record on its card.

These skills start only when you type their names. [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “routes, then stops,” so neither task has been run here.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'SKILL.md' -g 'data-rules.md' -g 'levels.md' -g 'validate.md' -g 'exercise.md' -g 'README.md' -g 'keep-it-running.md'"`
- command_execution: `/bin/bash -lc 'rg --files --hidden .agents'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/skills/ask-ai4bcm/units/prompts/exercise.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/levels.md .agents/skills/ask-ai4bcm/units/prompts/README.md .agents/skills/ask-ai4bcm/units/keep-it-running.m`
