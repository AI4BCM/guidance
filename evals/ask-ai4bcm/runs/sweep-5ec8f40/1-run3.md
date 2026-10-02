# /ask-ai4bcm case 1, run3: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `17ef60cf-b506-44bf-9962-3b01f31467bc`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**. You're preparing an interview, so no connector is involved.

**Skill to run: `/prepare-bia`**
- **What it does:** It first asks who the interview is with (your dispatch lead) and what you need back from it. Then it drafts the interview guide from the material you give it. It uses Task choice 1 and leaves the recovery fields blank.
- **What to read:** `units/stages/analysis.md` and `units/prompts/bia.md`. The workflow is in `units/workflow-design.md`.
- **Maturity level:** Level 2, Repeatable.
- **Gate:** You need a saved prompt, approved tools, a written data rule and a named reviewer.
- **Effort:** About forty minutes for this one activity (dispatch).
- **Data rule:** `units/data-rules.md`. **Check this before you start.** BIA material is the most sensitive material in BCM. Dispatch notes often include call volumes, staffing names and supplier or system dependencies. Classify yours first, because anything pasted into the wrong tool can't be taken back.
- **After the draft:** The guide stays in the chat until your named reviewer has checked it. After the interview, the AI4BCM BIA-Workflow takes over the record.

The skill doesn't start until you type it. When you're ready, type `/prepare-bia`.

**Tool calls (stream-json):**

- none
