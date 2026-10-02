# $ask-ai4bcm case 4, run3: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff00-08f8-77f2-8ebf-c4adf03d416b`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using **ask-ai4bcm** to identify the route for your debrief and the later skill-building work. Its instruction is to “route, then stop,” so this turn will name the next skills without running them.

Your immediate route is **Stage 6: Validate → `/debrief-to-action`**.

- **Read:** [Validate, Prompts—Task choice 2](.agents/skills/ask-ai4bcm/units/stages/validate.md). This covers debrief analysis; `exercise.md` is for scenario drafting.
- **Result:** proposed findings tied to the exercise objective and quoted notes, plus proposed actions for your reviewer. The accountable reviewer accepts findings; proposed owners confirm actions.
- **Maturity:** Level 2, Repeatable.
- **Gate:** saved prompt, named approved tools, written data rule and named reviewer.
- **Effort:** about forty minutes.

**Data rule first:** debriefs can contain personal data and control weaknesses. Under [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md), classify them before entering them and use an approved corporate or private environment with approved permissions and retention.

For your **later custom skill**, read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md), which supplies the prompt pattern; then type **`/check-my-ai-tool`** to draft its [record card](.agents/skills/ask-ai4bcm/units/keep-it-running.md). Allow an afternoon. Level 2 uses the same gate above; once the team relies on it, Level 3 requires all five [self-check questions](.agents/skills/ask-ai4bcm/units/levels.md) answered yes with evidence. The same data rule applies.

Each skill starts only when you type its name. I’m stopping here because [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “routes, then stops” and never runs a step of another skill.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'pwd; rg --files .agents/skills/ask-ai4bcm'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/skills/ask-ai4bcm/units/prompts/exercise.md .agents/skills/ask-ai4bcm/units/prompt`
