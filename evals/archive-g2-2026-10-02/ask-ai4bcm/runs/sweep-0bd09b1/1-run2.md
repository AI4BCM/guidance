# /ask-ai4bcm case 1, run2: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fb1ea662-f72c-43ac-b4a0-b38408bf46ad`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**, and it falls under *Before the interview, no connector*.

**Before anything else, classify your material.** Read [`units/data-rules.md`](units/data-rules.md) first. Dispatch details such as volumes, customer commitments, named staff and supplier dependencies are among the most sensitive material in BCM. Once something is pasted into the wrong tool, you can't take it back.

**The route**
- **Skill:** **`/prepare-bia`**. It starts only when you type it. It returns a draft for a reviewer and writes nothing.
- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md) and [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1. Leave the recovery fields blank, because the dispatch lead fills those in during the interview.
- **Workflow context:** [`units/workflow-design.md`](units/workflow-design.md)
- **Maturity level:** Level 2, Repeatable
- **Gate:** you need four things in place:
  - a saved prompt
  - approved tools
  - a written data rule
  - a named reviewer

  If any of these is missing, sort it out before you start.
- **Effort:** about forty minutes for the dispatch activity.

**After the draft:** your named reviewer checks the prep before you go into the interview. After the interview, the AI4BCM BIA-Workflow takes the record through to a signed BIA. If you later want to run this over connected records instead of one interview at a time, that is Level 3. The gate for that is all five self-check questions in [`units/levels.md`](units/levels.md) answered yes, with evidence.
