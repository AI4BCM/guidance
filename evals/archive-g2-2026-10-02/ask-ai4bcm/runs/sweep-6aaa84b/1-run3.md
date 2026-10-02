# /ask-ai4bcm case 1, run3: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a5bf54e8-44c0-43bc-95f6-8086b4efcff9`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3: Analysis**, the step before the interview. Most people start here, with no connector.

**Check the data rule first:** [`units/data-rules.md`](units/data-rules.md). BIA material is the most sensitive material in BCM. Dispatch notes often hold driver names, customer addresses, contract terms and recovery figures. Decide what may go into which tool before you paste anything. Anything pasted into the wrong tool can't be taken back.

**What to run:** **`/prepare-bia`**. Type it yourself when you're ready, because the skill only starts when you type its name. It runs Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md).

**Read:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow is in [`units/workflow-design.md`](units/workflow-design.md).

**Maturity level:** Level 2.

**Gate:** you need all four of these before you start:
- a saved prompt
- approved tools
- a written data rule
- a named reviewer

**Effort:** about forty minutes for one activity, which here is dispatch.

**Not this route:** if you want the AI to work over connected records, such as earlier BIAs or the requirements register, that is Level 3. It needs all five self-check questions in [`units/levels.md`](units/levels.md) answered yes with evidence, and takes an afternoon. You don't need that to prepare for one interview.

**After the draft:** the skill returns an interview prep draft for your named reviewer and saves nothing. After the interview, the AI4BCM BIA-Workflow takes the record through to a signed BIA, and the activity owner the unit names signs it off.
