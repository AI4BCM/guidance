# /ask-ai4bcm case 1, run3: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `da0d6726-07bb-4a4e-9fa3-dda2d826cb4d`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**, and the interview hasn't happened yet, so it falls under "Before the interview, no connector."

**Skill to run: `/prepare-bia`**
It starts only when you type it; I haven't started it. It will first ask who the interview is with (your dispatch lead) and what you need back from it. Then it drafts the interview guide from your own material. It uses Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md) and leaves the recovery fields blank for the interview to fill.

- **Read first:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow is in [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate:** You're ready when "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route."
- **Effort:** About forty minutes for this one activity (dispatch).
- **Data rule:** Check [`units/data-rules.md`](units/data-rules.md) before you start. BIA material is the most sensitive in BCM. Dispatch notes may include staff names, customer or site details and dependency data, so check what you're allowed to put into which tool before you paste anything. If your organisation hasn't written down a data rule yet, the answer is "no tool yet."

**After the draft:** The guide is a draft for whoever the unit names as owner. Once the interview is done, the AI4BCM BIA-Workflow takes the record on.

If you want to practise interview technique beforehand, **`/learn-bcm`** covers it in one session. To start the guide, type **`/prepare-bia`**.

**Tool calls (stream-json):**

- none
