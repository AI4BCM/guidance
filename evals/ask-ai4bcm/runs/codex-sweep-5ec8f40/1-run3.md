# $ask-ai4bcm case 1, run3: Codex, guidance at 5ec8f40

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fed2-c466-7ce0-b61b-93458fb2306c`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to route your interview preparation.

For next week’s dispatch interview, use **Stage 3: Analysis → `/prepare-bia`**.

- **Read:** [Analysis](.agents/skills/ask-ai4bcm/units/stages/analysis.md) and [BIA prompt, Task choice 1](.agents/skills/ask-ai4bcm/units/prompts/bia.md).
- **Maturity:** Level 2, Repeatable.
- **Gate:** Saved prompt, approved tools, written data rule, named reviewer.
- **Effort:** About 40 minutes per activity.
- **Data rule:** Classify material first. BIA details are high sensitivity; use only an approved corporate or private environment with approved permissions and retention. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md).

Type **`/prepare-bia`** to start. It asks who you’re interviewing and what you need back, then drafts a guide with recovery fields blank. No connector is needed; the draft stays in chat for the named reviewer.

I’m stopping at routing because [ask-ai4bcm’s instructions](.agents/skills/ask-ai4bcm/SKILL.md) say: “It routes, then stops” and “A skill starts only when its name is typed.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md'`
- command_execution: `/bin/bash -lc "rg --files -g 'data-rules.md' -g 'bia.md' -g 'analysis.md' -g 'AGENTS.md'"`
- command_execution: `/bin/bash -lc "rg --files --hidden -g '*data-rules*' -g 'bia.md' -g 'analysis.md' -g 'AGENTS.md'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
