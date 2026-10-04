# $ask-ai4bcm case 4, run1: Codex, guidance at a9197f5

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1077a-dae5-7072-a4f5-56fae16f7e28`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using **ask-ai4bcm** to route the debrief work and the later skill-building step. I’ll read its data rules and relevant units first; this skill only routes, then stops.

**Start with Validate → `/debrief-to-action`.** Read [Validation, Task choice 2](.agents/skills/ask-ai4bcm/units/stages/validate.md). It turns one tabletop’s notes into proposed findings tied to the exercise objective, with quoted evidence and proposed actions for your accountable reviewer. Each action needs an outcome, a completion check and an owner supported by the sources. Allow **40 minutes**.

**Later, build your own skill.** Read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md): pick one narrow task, check where it may run and its permissions, write the prompt from the pattern, then test it on past work with human review. There is **no separate prompt file** for this route; the pattern is the template. Type `/check-my-ai-tool` to draft its record card using [Looking After Your Prompts and Tools](.agents/skills/ask-ai4bcm/units/keep-it-running.md). Allow **an afternoon**.

Both routes need **Level 2, Repeatable**. The gate is: “the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.”

If your future skill reads connected records, it needs **Level 3, Defined**: each use case is written down with its prompt, sources, review point and limits, has an owner, is entered in the organisation’s AI inventory where one exists, and all five [self-check questions](.agents/skills/ask-ai4bcm/units/levels.md) answer yes with evidence. Keep that record on its card.

**Data rule first:** debriefs can contain personal data and control weaknesses, requiring an approved corporate or private environment. Follow [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md): approve the environment, permissions and retention before entering notes; public free tools cannot receive BCM data, and passwords, keys and tokens go into no tool.

These skills start only when you type their names. I’m stopping at routing because [ask-ai4bcm/SKILL.md](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says: “It never runs a skill or any step of one.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'SKILL.md' -g 'data-rules.md' -g 'levels.md' -g 'validate.md' -g 'exercise.md' -g 'README.md' -g 'keep-it-runni`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/s`
