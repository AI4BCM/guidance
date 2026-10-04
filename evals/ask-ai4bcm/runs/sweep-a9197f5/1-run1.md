# /ask-ai4bcm case 1, run1: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `70dc0029-8ecd-43ff-9002-d6c1ed45c273`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

You're in **Stage 3, Analysis**, the "before the interview, no connector" route.

**Check the data first.** Before you gather any material, classify it using [`units/data-rules.md`](units/data-rules.md). Dispatch BIA data, activity dependencies, supplier weaknesses and named staff are all **high-sensitivity**. Use them only in an approved corporate or private environment, and never in a public or free online tool. If you can't say where the data goes and how long it stays there, don't paste it yet. Passwords, keys and tokens go into no tool at all.

**What to run:** **`/prepare-bia`**. It asks who the interview is with and what you need back from it. Then it drafts the interview guide from your material, using Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md) with the recovery fields left blank. Those fields are for the dispatch lead to fill in during the interview.

- **Read first:** [`units/stages/analysis.md`](units/stages/analysis.md). For how the steps fit together, see [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate:** You're ready when the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route.
- **Effort:** About forty minutes per activity.
- **Data rule:** BIA data is high-sensitivity, so use an approved environment only ([`units/data-rules.md`](units/data-rules.md)).

**Afterwards:** what you get is a draft guide. You review it before the interview. After the interview, the AI4BCM BIA-Workflow takes over the record.

`/prepare-bia` starts only when you type it.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
