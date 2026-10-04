# $ask-ai4bcm case 2, run1: Codex, guidance at a9197f5

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10778-669f-73a2-bcc2-af5dd965875d`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to identify the BIA-checking route and who owns the RTO change.

The skill is **`/check-against-bia`**, under **Stage 5: Implement**. It reports disagreements between the dispatch plan and approved BIA, with proposed owners.

- **Read:** [Implementing Continuity Arrangements](.agents/skills/ask-ai4bcm/units/stages/implement.md) and [Review prompt](.agents/skills/ask-ai4bcm/units/prompts/review.md).
- **Maturity:** Level 3, Defined.
- **Gate:** Each use case is written down with its prompt, sources, review point and limits, has an owner and is entered in the organisation’s AI inventory where one exists. All five self-check questions must answer yes with evidence: approved tools are known; data rules are written; source currency is checked; reviewers and approvers are defined; and a fallback exists. The skill’s card keeps that record.
- **Effort:** About forty minutes.
- **Data rule:** BIA data is high sensitivity: use only an approved corporate or private environment with approved permissions and retention. Keep organisational case material out of public tools.

Setting the dispatch plan’s RTO to **8 hours** is the **plan owner’s change**, requiring their approval and a new version. The plan owner and BIA activity owner decide how to resolve any disagreement.

I haven’t run the check or changed the plan. The invoked [ask-ai4bcm skill](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says, “It never runs a skill or any step of one.” It routes and stops; **`/check-against-bia` starts only when you type its name**.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'SKILL.md' -g 'data-rules.md' -g 'implement.md' -g 'levels.md' -g 'review.md'"`
- command_execution: `/bin/bash -lc "rg --files --hidden -g '"'!'"\\.git'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/implement.md .agents/`
