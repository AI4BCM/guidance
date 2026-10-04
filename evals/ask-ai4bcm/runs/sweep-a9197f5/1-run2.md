# /ask-ai4bcm case 1, run2: Claude Code, guidance at a9197f5

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `385af0fb-74bc-459e-a5e2-2206abb6e018`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This belongs to **Stage 3, Analysis**, and specifically the "before the interview" part. You're preparing a guide, and no records are connected.

**Check first:** decide how sensitive your material is, using [`units/data-rules.md`](units/data-rules.md). BIA material is the most sensitive in BCM, so do this before you paste anything into a tool.

**Skill to run:** **`/prepare-bia`**. It won't start until you type its name. When you do, it asks who the interview is with and what you need back from it. Then it drafts the interview guide from your own material, leaving the recovery fields blank.

**What to read:**
- [`units/stages/analysis.md`](units/stages/analysis.md)
- [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1
- [`units/workflow-design.md`](units/workflow-design.md), for how the workflow fits together

**Maturity level:** Level 2, Repeatable.

**Gate (Level 2's "Ready to work here when"):** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route."

**Effort:** about forty minutes for the dispatch activity.

**After the interview:** the AI4BCM BIA-Workflow takes the record from there. The guide is a draft. It goes to the owner that [`units/stages/analysis.md`](units/stages/analysis.md) names, through your normal approval route.

**Tool calls (stream-json):**

- none
