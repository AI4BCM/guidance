# /ask-ai4bcm case 1, run3: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bd9fbabe-5d75-49f8-8c78-934c9fa18994`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

Your situation is **Stage 3, Analysis: before the interview, with no connector.**

**What to run:** **`/prepare-bia`**. It starts when you type its name. It will ask who the interview is with and what you need back. Then it drafts the interview guide from your material, using Task choice 1 with the recovery fields left blank.

**First, check your material:** [`units/data-rules.md`](units/data-rules.md). BIA content is the most sensitive material in BCM. Before you paste anything about dispatch, such as volumes, dependencies, named staff or customer details, confirm it may go into the tool you're using.

**What to read:**
- [`units/stages/analysis.md`](units/stages/analysis.md)
- [`units/prompts/bia.md`](units/prompts/bia.md)
- [`units/workflow-design.md`](units/workflow-design.md) for the workflow around it

**Maturity level:** Level 2 (Repeatable).

**Gate:** Level 2's. You're ready to work here when:
- the prompt that worked is saved for reuse
- approved tools are named
- the data rule is written down
- every prompt has a named reviewer
- outputs go through the normal approval route

**Effort:** about forty minutes for this one activity.

**Afterwards:** the AI4BCM BIA-Workflow takes over the interview record. The guide is a draft for you to own and review before you sit down with the dispatch lead.

**Tool calls (stream-json):**

- none
