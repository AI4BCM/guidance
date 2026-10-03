# $ask-ai4bcm case 4, run3: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2d-8dd4-74d0-b0d3-279d591e84b4`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using ask-ai4bcm to identify the route for the debrief and the later skill-building work. It “routes, then stops,” so I’ll name the next skills without starting them.

First, apply [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md): debriefs can identify people and expose weaknesses. Treat that material as high sensitivity, using only an approved corporate or private environment with approved permissions and retention. Keep organisational material out of public tools; passwords, keys and tokens go into no tool.

**For last week’s tabletop:** type **`/debrief-to-action`**. This is Stage 6, Validate: read [Validation, Exercising, Review and Improvement](.agents/skills/ask-ai4bcm/units/stages/validate.md), especially **Task choice 2**. It proposes findings against the objective written before the exercise, quotes supporting notes, and proposes actions with outcomes, completion checks and owners where the sources name them. Your accountable reviewer decides which become findings; proposed owners confirm their actions. Allow **forty minutes**.

The stage also links [Exercise scenario](.agents/skills/ask-ai4bcm/units/prompts/exercise.md), which serves future exercise design. The debrief prompt lives in the Validate unit.

**For your own skill later:** read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md)—its prompt pattern is the template; there is no separate prompt file for this route. Step 2 checks where it may run, using your data rules and tool permissions. Type **`/check-my-ai-tool`** to draft its record card under [Looking After Your Prompts and Tools](.agents/skills/ask-ai4bcm/units/keep-it-running.md). Allow **an afternoon**.

Both routes need **Level 2, Repeatable**, with this gate in full: “the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.”

If the later skill reads connected records, it needs **Level 3, Defined**: each use case is written down with its prompt, sources, review point and limits, has an owner and is entered in the organisation’s AI inventory where one exists, and all five [Self-check questions](.agents/skills/ask-ai4bcm/units/levels.md) answer yes with evidence; the skill keeps that record on its card.

Neither skill has started. [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “routes, then stops”; each next skill starts only when you type its name.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'pwd; rg --files .agents/skills/ask-ai4bcm'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/s`
