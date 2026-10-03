# $ask-ai4bcm case 1, run2: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2a-f128-7062-a2ce-fd242db6b45b`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

I’m using **ask-ai4bcm** to identify the route and its prerequisites. It routes only: “It never runs a skill or any step of one,” so interview preparation starts when you type the recommended skill’s name.


For next week’s dispatch interview, use **`/prepare-bia`** under **Stage 3 — Analysis**, before the interview, with no connector.

- **Read:** [Analysis](.agents/skills/ask-ai4bcm/units/stages/analysis.md) and [BIA prompt, Task choice 1](.agents/skills/ask-ai4bcm/units/prompts/bia.md). The skill drafts a guide from your material, leaving recovery fields blank.
- **Maturity:** Level 2 — Repeatable.
- **Gate:** “the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route”.
- **Effort:** Forty minutes per activity.
- **Data rule:** Classify material before entering it. BIA detail is high-sensitivity: use only an approved corporate or private environment with approved permissions and retention. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md).
- **Review:** The activity owner confirms requirements and sets recovery times; top management approves BIA results.

Type **`/prepare-bia`** to start. [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) requires routing only: “It never runs a skill or any step of one.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md; cat .agents/skills/ask-ai4bcm/units/data-rules.md; cat .agents/skills/ask-ai4bcm/units/stages/analysis.md`
