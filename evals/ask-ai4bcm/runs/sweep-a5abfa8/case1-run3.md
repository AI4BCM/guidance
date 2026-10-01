# ask-ai4bcm case1 run3: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **stage 3, Analysis**, on the lower rung: the pre-interview draft, with no connector.

**Data rule first.** Classify before you paste anything: [`units/data-rules.md`](units/data-rules.md). BIA material is the most sensitive material in BCM. Dispatch volumes, customer commitments, named staff and supplier dependencies may all sit above what your tool is approved for. If the rules aren't written down yet, you're at Level 1 and the answer is "no tool yet." To check which tool may hold which class, see [`units/tools.md`](units/tools.md).

**Skill:** type **`/prepare-bia`** when you're ready. It runs [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1, and leaves the recovery fields blank.

**Read:** [`units/stages/analysis.md`](units/stages/analysis.md). For the workflow behind it, see [`units/workflow-design.md`](units/workflow-design.md).

**Level 2 (Repeatable).** You can do this before next week with no connector. The gate:
- the prompt that worked is saved for reuse
- approved tools are named
- the data rule is written down
- the draft has a named reviewer
- the output goes through your normal approval route

**Time:** about forty minutes for the dispatch activity.

**What the draft is and isn't:** every resource requirement it drafts is a question for your dispatch lead, not an entry for the register. Recovery times and impact figures stay empty until the dispatch lead gives them. The real content of the BIA is what you hear in the interview.

**After the draft:**
- **Before you send it:** you can type **`/challenge-my-plan`** to test your question set first.
- **After the interview:** the AI4BCM BIA-Workflow takes the record to a signed BIA, and the dispatch lead, as activity owner, decides each requirement.
- **If dispatch is one of several activities:** the inherited-BIAs on-ramp uses the same route. Write the method down as you go, so next year is a re-run rather than starting over.
