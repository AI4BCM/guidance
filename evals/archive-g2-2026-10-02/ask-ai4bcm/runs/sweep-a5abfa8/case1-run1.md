# ask-ai4bcm case1 run1: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

**Your situation: Stage 3, Analysis, on the lower rung (the draft you prepare before the interview).**

**Data rule first:** BIA material is the most sensitive content in BCM. Dispatch volumes, dependencies, supplier names and the people who cover each role are all in scope. Before you paste anything, check its class and which tool it may go into in [`units/data-rules.md`](units/data-rules.md). Anything pasted into the wrong tool stays there.

- **Skill:** **`/prepare-bia`**. You start it by typing the name. It runs [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1, and leaves the recovery fields blank.
- **Read:** [`units/stages/analysis.md`](units/stages/analysis.md). The workflow behind it is in [`units/workflow-design.md`](units/workflow-design.md).
- **Level:** Level 2, Repeatable. You need no connector.
- **Gate:** all five of these must hold before you start:
  - you save the prompt that worked so you can reuse it
  - the tool you use is on the approved list
  - the data rule is written down
  - the draft has a named reviewer
  - the output goes through your normal approval route
- **Time:** about forty minutes for the dispatch activity. The real content is what the dispatch lead tells you in the interview.
- **What the draft is:** each resource requirement it drafts is a question to ask the dispatch lead. None of them goes into the register. The recovery fields stay empty because the dispatch lead sets those values.

**After the draft, three people or steps can act on it:**
- **The owner decides.** The dispatch lead confirms, corrects or rejects each requirement in the interview.
- **Another skill reads it.** If you want the question set tested before you send it, run **`/challenge-my-plan`** on the draft.
- **Next step after the interview:** the AI4BCM BIA-Workflow turns the interview record into a signed BIA.

If you start preparing BIAs for more than one activity, write the method down as you go. Next year's round can then reuse it instead of starting again, and that written method is what moves you to Level 3 once retrieval can reach your live records.
