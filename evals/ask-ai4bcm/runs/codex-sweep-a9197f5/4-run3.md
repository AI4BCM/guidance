# $ask-ai4bcm case 4, run3: Codex, guidance at a9197f5

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a1077b-9f4b-7942-bf55-edbc581e500a`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using **ask-ai4bcm** to name the route for your debrief and the later skill-building step. It routes and stops; the next skill starts only when you type its name.

First, apply [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md): debriefs can name people and expose weaknesses, so use an approved corporate or private environment with approved permissions and retention. Public, free tools must not receive BCM data; passwords, keys and tokens go into no tool.

- **Now — Validate:** type **`/debrief-to-action`**. Read [Validation, Exercising, Review and Improvement](.agents/skills/ask-ai4bcm/units/stages/validate.md), **Task choice 2**. It proposes findings tied to the exercise objective and quoted notes, plus actions with outcomes, completion checks and proposed owners supported by the sources. Your accountable reviewer decides which become findings; proposed owners confirm their actions. **Level 2, Repeatable; about forty minutes.**
- **Later — build your own skill:** read [Build your own skill: four steps](.agents/skills/ask-ai4bcm/units/prompts/README.md). **No separate prompt file:** use its prompt pattern. Step 2 checks where it may run, under the data rules and tool permissions. Type **`/check-my-ai-tool`** to draft its record card using [Looking After Your Prompts and Tools](.agents/skills/ask-ai4bcm/units/keep-it-running.md). **Level 2 as soon as the prompt becomes a team method; about an afternoon.**

**Level 2 gate for both:** the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.

If your later skill reads connected records, **Level 3** applies: each use case is written down with its prompt, sources, review point and limits, has an owner and is entered in the organisation’s AI inventory where one exists, and all five self-check questions answer yes with evidence; keep that record on its card.

These skills start only when you type their names. I’m stopping here because [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) says it “routes, then stops” and never runs another skill or any step of one.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md; rg --files .agents/skills/ask-ai4bcm'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/skills/ask-ai4bcm/units/prompts/exer`
