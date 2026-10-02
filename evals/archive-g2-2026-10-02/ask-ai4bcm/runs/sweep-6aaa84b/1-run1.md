# /ask-ai4bcm case 1, run1: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `b852f47f-80a0-4177-b896-2a93eafc1045`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This belongs to **Stage 3, Analysis**, on the lower rung: preparing *before* the interview, with no connector to your records.

**First, the data rules: [`units/data-rules.md`](units/data-rules.md).** BIA material is the most sensitive material in BCM. Dispatch work brings in volumes, customer and carrier dependencies, staffing, and what an outage costs. Before you paste anything about dispatch into a tool, check that the tool is approved for that class of data. If your data rules aren't written down yet, no tool is approved, so prepare from public or generic material only. Once something is pasted into the wrong tool, you can't take it back.

**Route**
- **Skill:** **`/prepare-bia`**. Type it when you're ready. It runs Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md) and gives you an interview pack for one activity (dispatch). The pack is a draft. It writes nothing anywhere.
- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow is in [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** 2.
- **Gate:** you need all four of these:
  - a saved prompt
  - approved tools
  - a written data rule
  - a named reviewer for the draft
- **Effort:** about forty minutes for the dispatch activity.

**Not this route:** if you want the AI to read your connected records directly (past BIAs, the dispatch system, contracts), that's Level 3. Its gate is that all five self-check questions in [`units/levels.md`](units/levels.md) answer yes, with evidence. That's more than you need for next week.

**After the draft:** your named reviewer checks the pack before you go into the interview. Afterwards, the AI4BCM BIA-Workflow turns the interview record into a signed BIA, and the activity owner the unit names is the one who decides. If you'd like to rehearse the hard questions first, **`/challenge-my-plan`** can test your interview approach. Type it if you want it.
