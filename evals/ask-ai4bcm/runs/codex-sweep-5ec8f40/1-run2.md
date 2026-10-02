# $ask-ai4bcm case 1, run2: Codex, guidance at 5ec8f40

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fed2-7509-77b1-a2f6-540be4649c44`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

I’m using ask-ai4bcm to route your interview preparation to the right skill and prerequisites.

For next week’s dispatch-lead interview, use **Stage 3: Analysis → `/prepare-bia`**.

- **Read:** `units/stages/analysis.md` and `units/prompts/bia.md`, **Task choice 1**.
- **Maturity:** Level 2 — Repeatable.
- **Gate:** A saved prompt, approved tools, a written data rule and a named reviewer.
- **Effort:** About 40 minutes per activity.
- **Data rule:** Classify material before entering it. BIA details are high sensitivity and belong only in an approved corporate or private environment with approved permissions and retention. See `units/data-rules.md`.

Type **`/prepare-bia`** to start. It will ask what you need back from the dispatch lead, then draft an interview guide from your material, with recovery fields blank. Preparation uses **no connector**; the draft stays in chat for the named reviewer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/SKILL.md'`
- command_execution: `/bin/bash -lc "rg --files .agents | rg '(data-rules|analysis|bia)\\.md"'$'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/ask-ai4bcm/units/data-rules.md'`
