# $ask-ai4bcm case 2, run1: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2b-66f9-7fc1-a2cf-6ea41981706f`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to identify the BIA check and the rules for changing the plan’s RTO.

Use **`/check-against-bia`**. It checks the dispatch plan against the approved BIA and reports disagreements with proposed owners.

- **Read:** [Implementing Continuity Arrangements](.agents/skills/ask-ai4bcm/units/stages/implement.md) and [Review and challenge](.agents/skills/ask-ai4bcm/units/prompts/review.md).
- **Maturity:** Level 3, Defined.
- **Gate:** Each use case is written down with its prompt, sources, review point and limits, has an owner and is entered in the organisation’s AI inventory, where one exists, and all five self-check questions answer yes with evidence; a skill or workflow keeps that record on its card.
- **Effort:** Forty minutes.
- **Data rule:** BIA data is high sensitivity. Use only an approved corporate or private environment with approved permissions and retention; never use public, free tools for BCM data.

Changing the dispatch plan’s RTO to **8 hours** belongs to the **plan owner**, with approval and a new version. The check reports disagreements; it does not choose or replace recovery times.

I have not run the check or changed the RTO. The invoked [ask-ai4bcm skill](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says, “It routes, then stops” and “It never runs a skill or any step of one.” **`/check-against-bia` starts only when you type its name.**

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md'`
- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*data-rules*' -g '*implement*' -g '*levels*' -g '*review*'"`
- command_execution: `/bin/bash -lc 'rg --files --hidden .agents'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/prompts/review.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/levels.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/stages/implement.md'`
