# $ask-ai4bcm case 4, run2: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0feff-9324-7661-83dc-4a207be07ef7`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using ask-ai4bcm to name the route for your debrief and the later skill-building work, then stop as the skill requires.

**First, the data rule:** debriefs can name people and expose weaknesses. [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md) requires classification before entry and an approved environment with permissions and retention agreed. Public free tools must not receive BCM material; passwords, keys and tokens go into no tool.

**Now: Validate → `/debrief-to-action`.** Read [Validate, Task choice 2](.agents/skills/ask-ai4bcm/units/stages/validate.md). It proposes findings tied to the exercise’s missed objective, quotes supporting notes, and proposes actions with outcomes, completion checks and owners where the sources name them. Your accountable reviewer accepts findings; proposed owners confirm actions. Without the objective, it lists gaps and stops.

- **Maturity:** Level 2, Repeatable.
- **Gate:** saved prompt, named approved tools, written data rule, named reviewer.
- **Effort:** forty minutes.

**Later: build your own skill.** Read [Prompts → Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md): choose one narrow task, check its permitted environment, use the prompt pattern, and test against past work with human review. `/check-my-ai-tool` drafts its record card, described in [Keep it running](.agents/skills/ask-ai4bcm/units/keep-it-running.md).

- **Maturity and gate:** Level 2 to save for the team, with the same gate above; Level 3 once the team relies on it, requiring five self-checks answered yes with evidence in [Levels](.agents/skills/ask-ai4bcm/units/levels.md).
- **Effort:** an afternoon. The same data rule applies.

Each skill starts only when you type its name. I’m stopping here because [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says: “It routes, then stops.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/s`
