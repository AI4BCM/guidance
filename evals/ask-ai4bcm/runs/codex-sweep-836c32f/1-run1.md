# $ask-ai4bcm case 1, run1: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2a-7b88-7110-b0b7-f81c07e6dbed`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

I’m using ask-ai4bcm to identify the route for your interview preparation. It “routes, then stops”; `/prepare-bia` starts only when you type its name.

For next week’s dispatch-lead interview, use **Stage 3: Analysis → `/prepare-bia`**.

- **Read:** [Analysis](.agents/skills/ask-ai4bcm/units/stages/analysis.md) and [BIA prompt](.agents/skills/ask-ai4bcm/units/prompts/bia.md), Task choice 1. It drafts an interview guide from approved material, with MTPD, RTO and RPO fields blank. No connector is needed.
- **Maturity:** Level 2, Repeatable.
- **Gate:** “the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route”.
- **Effort:** Forty minutes per activity.
- **Data rule:** Treat BIA material as high-sensitivity: use only an approved corporate or private environment with approved permissions and retention. Keep organisational material out of public tools; passwords, keys and tokens go into no tool. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md).

Type **`/prepare-bia`** to start.

[ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “routes, then stops,” so this response identifies the route and leaves interview preparation to that skill.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md'`
- command_execution: `/bin/bash -lc 'rg --files | head -60'`
- command_execution: `/bin/bash -lc "rg --files --hidden -g '"'! .git'"' .agents | head -70"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/analysis.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/levels.md'`
