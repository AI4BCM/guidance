# $ask-ai4bcm case 1, run2: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fefd-9371-7b80-8b04-d31cb78f9090`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to identify the route for preparing your dispatch BIA interview and its data requirements.

For next week’s dispatch-lead interview, use **`/prepare-bia` — Stage 3: Analysis, before the interview, no connector**.

- **Read:** [Analysis](.agents/skills/ask-ai4bcm/units/stages/analysis.md) and [BIA prompt](.agents/skills/ask-ai4bcm/units/prompts/bia.md), Task choice 1.
- **Maturity:** Level 2, Repeatable.
- **Gate:** a saved prompt, approved tools, a written data rule and a named reviewer.
- **Effort:** about 40 minutes per activity.
- **Data rule:** classify material before entering it. BIA detail is high-sensitivity and belongs only in an approved corporate or private environment with approved permissions and retention. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md).

The skill drafts a guide from your approved material, leaving recovery fields blank. The activity owner confirms requirements and sets recovery times.

Per [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md), “It routes, then stops.” **Preparation starts only when you type `/prepare-bia`.**

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md'`
- command_execution: `/bin/bash -lc "rg --files -g 'data-rules.md' -g 'analysis.md' -g 'bia.md' -g 'AGENTS.md'"`
- command_execution: `/bin/bash -lc "rg --files --hidden -g 'data-rules.md' -g 'analysis.md' -g 'bia.md' -g 'AGENTS.md' -g '"'! .git'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/analysis.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/prompts/bia.md'`
