# /ask-ai4bcm case 1, run2: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `61aa967b-4050-40b7-891f-3ac196364a42`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is a Stage 3 (Analysis) job: you're preparing for the interview, and no records are connected yet.

**Skill to run:** **`/prepare-bia`**. It starts only when you type it. It will ask who the interview is with and what you need back. Then it drafts the interview guide from your material, using Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md), with the recovery fields left blank for the interview to fill.

**Read first:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow is in [`units/workflow-design.md`](units/workflow-design.md).

**Maturity level:** Level 2, Repeatable.

**Gate:** Level 2's. You're ready to work here when:
- the prompt that worked is saved for reuse,
- approved tools are named,
- the data rule is written down,
- every prompt has a named reviewer, and
- outputs go through the normal approval route.

**Effort:** About forty minutes per activity. If the dispatch lead covers more than one activity, budget forty minutes for each.

**Data rule:** Classify your material before anything else, using [`units/data-rules.md`](units/data-rules.md). BIA material is the most sensitive in BCM. Dispatch notes are likely to include named people, supplier contracts and outage costs. If your data rule isn't written down yet, there is no approved tool to paste them into.

**Afterwards:** The guide is a draft for your review. Once the interview is done, the AI4BCM BIA-Workflow takes the record on.

**Tool calls (stream-json):**

- none
