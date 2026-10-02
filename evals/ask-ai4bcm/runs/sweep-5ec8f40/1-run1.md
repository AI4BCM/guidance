# /ask-ai4bcm case 1, run1: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e919f886-acd9-4aa2-a5ab-bd7dd7245c2b`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

Your interview falls under **Stage 3, Analysis**, on the **Before the interview, no connector** route.

**Classify your data first.** Before you paste anything, read [`units/data-rules.md`](units/data-rules.md). BIA material is the most sensitive data in BCM. Dispatch notes may include call volumes, staffing, contract terms or named people. Once something is pasted into the wrong tool, you can't take it back.

**The route:**

- **Skill:** **`/prepare-bia`**. It asks who the interview is with and what you need back, then drafts the interview guide from your material. The recovery fields stay blank because the dispatch lead fills those in. It starts only when you type it.
- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md) and [`units/prompts/bia.md`](units/prompts/bia.md) (Task choice 1). For the wider workflow, see [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** Level 2 (Repeatable).
- **Gate:** You need four things before you start: a saved prompt, approved tools, a written data rule and a named reviewer.
- **Effort:** About forty minutes for one activity.
- **Data rule:** [`units/data-rules.md`](units/data-rules.md). It decides which tool may hold your dispatch material, and it applies before anything else.

**After the draft:** The guide stays in the chat until your named reviewer checks it. After the interview, the AI4BCM BIA-Workflow takes over the record.

If you haven't written a data rule or approved a tool yet, see [`units/data-rules.md`](units/data-rules.md) and then [`units/tools.md`](units/tools.md). Until those exist, no tool is cleared for this material.

**Tool calls (stream-json):**

- none
