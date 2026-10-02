# /ask-ai4bcm case 1, run2: Claude Code, guidance at 6aaa84b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `136d5bc0-5279-4ca8-9fb3-ef722bce338a`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**: you're getting ready for one interview, and no records are connected yet.

**Check the data rule first.** Read [`units/data-rules.md`](units/data-rules.md) before you paste anything. BIA material is the most sensitive in BCM: it covers dispatch volumes, customer commitments, dependencies and named staff. Use only an approved tool, and keep to what your written data rule allows. Once something is pasted into the wrong tool, you can't take it back.

**Route**
- **Skill:** **`/prepare-bia`**. This is Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md). Type it yourself when you're ready, because I won't start it.
- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow is in [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** 2.
- **Gate:** a saved prompt, approved tools, a written data rule and a named reviewer. If any of these is missing, sort it out before the interview.
- **Effort:** about 40 minutes for this one activity (dispatch).

**After the draft:** `/prepare-bia` gives you a draft interview pack. Your named reviewer checks it before you use it with the dispatch lead. After the interview, the AI4BCM BIA-Workflow takes the record through to a signed BIA, and the activity owner the unit names signs it off.

Two other routes don't fit this case:
- If you later want to run this over connected records, such as past BIAs or registers, that's Level 3. It needs all five self-check answers in [`units/levels.md`](units/levels.md) to be "yes", with evidence.
- If you're unsure which tool is approved for this material, use the "Which tool may I paste this into?" route first: [`units/data-rules.md`](units/data-rules.md), then [`units/tools.md`](units/tools.md).
