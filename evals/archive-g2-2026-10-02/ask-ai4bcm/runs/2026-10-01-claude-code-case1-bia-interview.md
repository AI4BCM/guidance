# ask-ai4bcm case1-bia-interview: Claude Code 2.1.284, 2026-10-01

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**, on the lower rung: a draft you prepare before the interview, with no connector needed.

**Data rule first.** Read [`units/data-rules.md`](units/data-rules.md) and classify what you plan to paste in before you open any tool. BIA material is the most sensitive in BCM. For dispatch that likely means routes, customer names, carrier contracts and staffing. Anything that names people or customers goes only into a tool your data rule approves for that class. If you have no written data rule yet, you're at Level 1 and the answer is that no tool is approved yet.

**Skill: `/prepare-bia`.** It runs [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1, and leaves the recovery fields blank. It drafts what dispatch probably does and needs, as questions for your dispatch lead.

- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow behind it is in [`units/workflow-design.md`](units/workflow-design.md).
- **Level:** 2, Repeatable.
- **Gate:** You need all of these:
  - the prompt that works is saved for reuse
  - the approved tools are named
  - the data rule is written down
  - the draft has a named reviewer
  - the output goes through your normal approval route
- **Effort:** About 40 minutes for the dispatch activity. The real content is what the dispatch lead tells you in the interview.
- **What the draft is:** Every resource requirement it lists is a question for your dispatch lead, never an entry in the register. The recovery figures (RTO, MTPD) stay blank. The dispatch lead sets them, not the model.

**After the draft:**
- Your dispatch lead decides. Take the draft into the interview as a question list.
- Optionally, run **`/challenge-my-plan`** on your question list first if you want to test it before the meeting.
- After the interview, the AI4BCM BIA-Workflow takes the record through to a signed BIA.

When you're ready, type `/prepare-bia` to start it.
