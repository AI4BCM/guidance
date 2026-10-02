# /ask-ai4bcm case 1, run1: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `7cec79cc-7383-40ee-baff-d14e2f8d907e`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

**First, the data rule.** Read [`units/data-rules.md`](units/data-rules.md) before you paste anything. Dispatch details often include customer names, driver or staff rosters, contract volumes and site addresses. BIA material is the most sensitive in BCM, and something pasted into the wrong tool can't be taken back. If your organisation hasn't written down which tools are approved for this material, the answer for now is "none yet".

**Your route: Stage 3, Analysis, before the interview, with no connector.**

- **Skill:** type **`/prepare-bia`** to start it. It runs [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1, and leaves the recovery fields blank. Recovery times and targets come from the dispatch lead in the interview, not from the AI.
- **Read first:** [`units/stages/analysis.md`](units/stages/analysis.md). If you're setting this up for more than one interview, also read [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate:** you need a saved prompt, approved tools, a written data rule and a named reviewer for the draft. If any of these is missing, sort it out before next week.
- **Effort:** about forty minutes for the dispatch activity.

**After the draft:** the result is interview preparation for your named reviewer to check, not a BIA. Once the interview is done, the AI4BCM BIA-Workflow takes the record through to a signed BIA, and the activity owner decides what goes in it.

**Other routes:**
- If you plan to pull in connected records, such as dispatch system data or earlier BIAs, through a connector, you need Level 3. The gate is that all five self-check questions in [`units/levels.md`](units/levels.md) answer yes with evidence, and it takes about an afternoon.
- If you'd like to brush up on running a BIA interview first, type **`/learn-bcm`**.
