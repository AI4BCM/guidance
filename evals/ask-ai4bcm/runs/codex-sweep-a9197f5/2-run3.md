# $ask-ai4bcm case 2, run3: Codex, guidance at a9197f5

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10779-a0bc-7fc3-b7c9-b96e7a62b914`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to identify the BIA check and the plan owner’s change process.

Use **`/check-against-bia`** for Stage 5, Implement. It lists disagreements between the dispatch plan and the approved BIA, with proposed owners.

- **Read:** [Implement](.agents/skills/ask-ai4bcm/units/stages/implement.md) and [Review](.agents/skills/ask-ai4bcm/units/prompts/review.md).
- **Level:** 3, Defined. **Effort:** about 40 minutes.
- **Gate:** Each use case is written down with its prompt, sources, review point and limits, has an owner, and is entered in the organisation’s AI inventory where one exists. All five self-check questions must answer yes with evidence: approved tools, written data rules, current sources, named reviewers and approvers, and a fallback. A skill or workflow keeps this record on its card.
- **Data rule:** BIA data is highly sensitive; use only an approved corporate or private environment with approved permissions and retention. Never enter passwords, keys or tokens.

The **dispatch plan owner** owns the change to an 8-hour RTO and must approve a new plan version. The check reports disagreements; it does not choose or replace recovery times.

The invoked [ask-ai4bcm skill](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “routes, then stops” and “never runs a skill or any step of one.” I haven’t run the check or changed the RTO. **It starts only when you type `/check-against-bia`.**

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'SKILL.md' -g 'data-rules.md' -g 'implement.md' -g 'levels.md' -g 'review.md'"`
- command_execution: `/bin/bash -lc "rg --files --hidden -g '"'! .git'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md .agents/skills/ask-ai4bcm/units/data-rules.md .agents/skills/ask-ai4bcm/units/stages/implement.md .agents/`
