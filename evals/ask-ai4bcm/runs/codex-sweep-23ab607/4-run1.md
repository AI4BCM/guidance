# $ask-ai4bcm case 4, run1: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0feff-6bb3-7b32-998a-e2cf4e516e00`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm We ran a tabletop last week and I have the debrief notes. I want them turned into findings and actions for our reviewer, and later I want to turn the prompt we use into a skill of our own.

**Reply (verbatim):**

I’m using ask-ai4bcm to identify the route for your debrief and the later skill-building work. It routes only; it won’t process the notes yet.

First apply [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md): debriefs can contain personal data and control weaknesses. Use an approved corporate or private environment with approved permissions and retention. Public free tools must not receive BCM notes; passwords, keys and tokens go into no tool.

**Now: Validate → `/debrief-to-action`.** Read [Validate](.agents/skills/ask-ai4bcm/units/stages/validate.md), Task choice 2—the debrief prompt. It proposes findings tied to the exercise objective and quoted notes, plus actions with outcomes, completion checks and proposed owners supported by the sources. Your accountable reviewer accepts findings; proposed owners confirm actions. A missing objective means Gaps and stop.

- **Level:** 2, Repeatable.
- **Gate:** saved prompt, named approved tools, written data rule and named reviewer.
- **Effort:** about forty minutes.

**Later: build your own skill.** Read [Build your own skill](.agents/skills/ask-ai4bcm/units/prompts/README.md): choose one narrow task, check where it may run, use the prompt pattern, and test on past work with human review. There is no separate prompt file for this route. Type `/check-my-ai-tool` to draft its [record card](.agents/skills/ask-ai4bcm/units/keep-it-running.md).

- **Level and gate:** Level 2 to save it for the team, with the same four controls above; Level 3 once the team relies on it, with all five [self-check questions](.agents/skills/ask-ai4bcm/units/levels.md) answered yes with evidence.
- **Effort:** an afternoon. The same data rule applies.

[ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) says it “routes, then stops” and “never runs a skill or any step of one.” `/debrief-to-action` starts only when you type its name.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md; rg --files .agents/skills/ask-ai4bcm'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/validate.md .agents/skills/ask-ai4bcm/units/prompts/exercise.md .agents/skills/ask-ai4bcm/units/prompt`
