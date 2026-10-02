# /ask-ai4bcm case 1, run3: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `944f7629-54ae-4e19-a10c-09c14c1e4605`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

Next week's interview fits **Stage 3, Analysis**. It's the "before the interview, no connector" route.

**Skill to type: `/prepare-bia`**
- It starts only when you type it. I haven't started it here.
- It first asks who the interview is with (your dispatch lead) and what you need back from it.
- Then it drafts the interview guide from the material you give it, using Task choice 1 in [`units/prompts/bia.md`](units/prompts/bia.md).
- It leaves the recovery fields blank. Your dispatch lead fills those in during the interview.

**Read first:** [`units/stages/analysis.md`](units/stages/analysis.md). For how the guide feeds the rest of the BIA, see [`units/workflow-design.md`](units/workflow-design.md).

**Maturity level:** 2, Repeatable.

**Gate:** all four must be in place before you run it:
- the prompt is saved
- the tools are approved
- the data rule is written down
- a reviewer is named

**Effort:** about forty minutes for the dispatch activity.

**Data rule:** classify your material with [`units/data-rules.md`](units/data-rules.md) before you paste anything into a tool. BIA material is the most sensitive material in BCM. Dispatch notes may include call volumes, staffing, supplier and system details, and the names of people.

**After the interview:** the guide is a draft for you, as the interviewer, and for your named reviewer. The AI4BCM BIA-Workflow then takes the completed record on.

If your BIA records are already connected and you want to work across them, that's the Level 3 route. It's gated on the five self-check questions in [`units/levels.md`](units/levels.md) being answered yes with evidence. You don't need it for this interview.

**Tool calls (stream-json):**

- none
