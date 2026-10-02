# /ask-ai4bcm case 1, run3: Claude Code, guidance at 0bd09b1

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c23ee65a-9b18-4ce6-a508-eb025e6fcb62`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

## Your route: Stage 3 (Analysis), preparing for the interview without a connector

**First, check the data rule:** [`units/data-rules.md`](units/data-rules.md). BIA material is the most sensitive material in BCM. Classify what you plan to use before you paste anything about dispatch into a tool, including volumes, customer names, supplier contracts and the dispatch lead's own notes. Anything pasted into the wrong tool cannot be taken back.

- **Skill:** **`/prepare-bia`**. It starts only when you type it, and it gives you a draft. It writes nothing.
- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md), then [`units/prompts/bia.md`](units/prompts/bia.md), **Task choice 1**. Leave the recovery fields blank. The dispatch lead fills those in during the interview; the AI doesn't guess them beforehand. For how the steps fit together, see [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** 2, Repeatable.
- **Gate:** you need four things in place: a saved prompt, approved tools, a written data rule and a named reviewer. If one is missing, sort that out before you run the skill.
- **Effort:** about forty minutes per activity. If dispatch breaks down into several activities, prepare each one separately. Inbound scheduling, outbound loading and carrier handover would be three runs.

**After the draft:** the reviewer you named checks the prep pack before the interview. After the interview, the AI4BCM BIA-Workflow takes the record through to a signed BIA, and the activity owner decides what goes into it.

If you'd rather work over connected records such as existing BIAs, the requirements register or incident logs, that's Level 3. It needs yes answers, with evidence, to all five self-check questions in [`units/levels.md`](units/levels.md). Most people start with the route above.
