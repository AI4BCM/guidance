# $ask-ai4bcm case 1, run1: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fefd-44f8-7fa1-9fcc-9361bd6384da`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

I’m using ask-ai4bcm to identify the route for preparing your dispatch BIA interview and its data requirements.

Use **`/prepare-bia`** for next week’s interview with your dispatch lead.

- **Stage:** 3 — Analysis. Read [Analysis](.agents/skills/ask-ai4bcm/units/stages/analysis.md) and [BIA prompt, Task choice 1](.agents/skills/ask-ai4bcm/units/prompts/bia.md).
- **Maturity:** Level 2, Repeatable; no connector needed.
- **Gate:** saved prompt, approved tools, written data rule, named reviewer.
- **Effort:** about 40 minutes per activity.
- **Data rule:** BIA material is high-sensitivity; use only an approved corporate or private environment with approved permissions and retention. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md).
- **Review:** the guide is a draft. Recovery fields stay blank; the activity owner confirms requirements and sets recovery times.

Type **`/prepare-bia`** to start. I’m stopping at routing because [ask-ai4bcm](.agents/skills/ask-ai4bcm/SKILL.md) says it “never runs a skill or any step of one.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/analysis.md .agents/s`
