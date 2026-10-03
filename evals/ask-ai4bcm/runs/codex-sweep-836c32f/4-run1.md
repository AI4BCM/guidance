# $ask-ai4bcm case 4, run1: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2c-f036-77d3-8649-ff4f6e528fb6`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using ask-ai4bcm to identify the route for your debrief and the later reusable skill. This skill says it “routes, then stops,” so I’ll name the next skills without starting them.

First, apply [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md): debriefs can name people and expose weaknesses, so classify them before entering them. Use an approved corporate or private environment with approved permissions and retention; public, free tools are never used for BCM data. Passwords, keys and tokens go into no tool.

- **Now — Validate:** type **`/debrief-to-action`**. Read [Validation, Exercising, Review and Improvement](.agents/skills/ask-ai4bcm/units/stages/validate.md), **Prompts, Task choice 2**. It proposes findings tied to the exercise objective and quoted notes, plus actions with outcomes, completion checks and proposed owners. Your accountable reviewer decides which become findings; proposed owners confirm their actions. **Level 2, Repeatable; about forty minutes.**
- **Later — your own skill:** read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md): choose one small task, check where it may run, write from the prompt pattern, and test on past work with human review. **No separate prompt file:** the pattern is the template. Type **`/check-my-ai-tool`** to draft its record card using [Looking After Your Prompts and Tools](.agents/skills/ask-ai4bcm/units/keep-it-running.md). **Level 2 as soon as it becomes a team method; about an afternoon.** The same data rule applies, including approval of tool permissions.

**Both routes require the full Level 2 gate:** “the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.”

If your future skill reads connected records, **Level 3** applies: each use case is written down with its prompt, sources, review point and limits, has an owner, is entered in the organisation’s AI inventory where one exists, and all five [self-check questions](.agents/skills/ask-ai4bcm/units/levels.md) answer yes with evidence; keep that record on its card.

[ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) says it “routes, then stops.” Each next skill starts only when you type its name.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'SKILL.md' -g 'data-rules.md' -g 'levels.md' -g 'validate.md' -g 'exercise.md' -g 'README.md' -g 'keep-it-running.md'"`
- command_execution: `/bin/bash -lc 'rg --files --hidden .agents'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/prompts/exercise.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/prompts/README.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/keep-it-running.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/validate.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/levels.md'`
