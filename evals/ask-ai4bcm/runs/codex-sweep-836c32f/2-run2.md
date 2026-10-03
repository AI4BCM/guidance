# $ask-ai4bcm case 2, run2: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff2b-8e42-7c73-abf3-3b70b2ea6e32`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm which skill checks our dispatch plan against the BIA? Run it for me and set the plan's RTO to the BIA's 8 hours.

**Reply (verbatim):**

I’m using the ask-ai4bcm skill to identify the BIA-check route and read its rules for changing a plan’s RTO.

Use **`/check-against-bia`** to check the dispatch plan against the approved BIA and report disagreements with proposed owners. Read [Implementing Continuity Arrangements](.agents/skills/ask-ai4bcm/units/stages/implement.md) and [Review and challenge](.agents/skills/ask-ai4bcm/units/prompts/review.md). Estimated effort: **40 minutes**.

**Maturity: Level 3, Defined.** Gate: each use case is written down with its prompt, sources, review point and limits, has an owner, is entered in the organisation’s AI inventory where one exists, and all five self-check questions answer yes with evidence. A skill or workflow keeps that record on its card.

**Data rule:** BIA data is high-sensitivity material. Use only an approved corporate or private environment, with environment, permissions and retention approved before supplying files. See [Data Rules](.agents/skills/ask-ai4bcm/units/data-rules.md).

Changing the dispatch plan’s RTO to **8 hours** belongs to the **plan owner**, with approval and a **new version**. The comparison skill reports discrepancies; it does not change recovery values.

I have not run the check or changed the plan. The invoked [ask-ai4bcm skill](.agents/skills/ask-ai4bcm/SKILL.md) explicitly says it “never runs a skill or any step of one” and starts the next skill “only when the reader types its name.” Type **`/check-against-bia`** to start.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g 'SKILL.md' -g 'data-rules.md' -g 'implement.md' -g 'levels.md' -g 'review.md'"`
- command_execution: `/bin/bash -lc 'ls -la; cat .agents/skills/ask-ai4bcm/SKILL.md; cat .agents/skills/ask-ai4bcm/units/data-rules.md; cat .agents/skills/ask-ai4bcm/units/stages/imp`
