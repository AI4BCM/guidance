# ask-ai4bcm case1 run2: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**, on the lower rung: a pre-interview draft that needs no connector.

**Before anything else, classify the material:** read [`units/data-rules.md`](units/data-rules.md). BIA content is the most sensitive material in BCM. Dispatch dependencies, suppliers, staffing and systems may well count as confidential. Decide which tool the material may go into before you paste anything, because you can't take it back afterwards.

**Skill:** type **`/prepare-bia`** when you're ready. It runs [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1, and leaves the recovery fields blank. I won't start it for you.

**Read:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow behind it is in [`units/workflow-design.md`](units/workflow-design.md).

**Level:** 2, Repeatable. **Gate:**
- the prompt that worked is saved for reuse
- the approved tools are named
- the data rule is written down
- the draft has a named reviewer
- the output goes through your normal approval route

**Effort:** about forty minutes for the dispatch activity. The real content is what your dispatch lead tells you in the interview.

**How to use the draft:** treat every resource requirement it drafts as a question for your dispatch lead, not as a register entry. Leave recovery times (RTO, MTPD) blank. Setting them is your dispatch lead's call, not the model's.

**What comes next:**
- **Before the interview:** you can type **`/challenge-my-plan`** to test your question set before you send it.
- **After the interview:** the AI4BCM BIA-Workflow takes the record to a signed BIA.
- **Later:** if you want BIA support that reads your live inventory, that's Level 3. All five self-check questions in [`units/levels.md`](units/levels.md) have to answer yes with evidence first.
