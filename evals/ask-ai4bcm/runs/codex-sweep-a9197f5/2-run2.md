# $ask-ai4bcm case 2, run2: Codex, guidance at a9197f5

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10779-03a5-79e0-8242-593d4e9d522d`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to identify the BIA-checking route and its requirements. I’ll read its data rules and plan-maintenance guidance first.

Use **`/check-against-bia`** to compare the dispatch plan with the approved BIA and report disagreements with proposed owners.

- **Read:** [Implementing Continuity Arrangements](.agents/skills/ask-ai4bcm/units/stages/implement.md) and [Review prompt](.agents/skills/ask-ai4bcm/units/prompts/review.md).
- **Maturity:** Level 3, Defined. **Gate:** each use case is written down with its prompt, sources, review point and limits, has an owner and is entered in the organisation’s AI inventory, where one exists, and all five self-check questions answer yes with evidence; the skill or workflow keeps that record on its card.
- **Effort:** Forty minutes.
- **Data rule:** BIA data is high-sensitivity: use only an approved corporate or private environment, with environment, permissions and retention approved first.

Setting the plan’s RTO to **8 hours** is the **dispatch plan owner’s change**, requiring their approval and a new version. The checking skill reports discrepancies; it does not change recovery times.

The [ask-ai4bcm skill](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “routes, then stops” and “never runs a skill or any step of one.” I therefore haven’t run the check or changed the plan. It starts only when you type **`/check-against-bia`**.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "cat .agents/skills/ask-ai4bcm/SKILL.md; rg --files -g 'data-rules.md' -g 'implement.md' -g 'levels.md' -g 'review.md' -g 'SKILL.md'"`
- command_execution: `/bin/bash -lc "rg --files --hidden -g 'data-rules.md' -g 'implement.md' -g 'levels.md' -g 'review.md' -g 'AGENTS.md'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/implement.md .agents/skills/ask-ai4bcm/units/levels.md'`
