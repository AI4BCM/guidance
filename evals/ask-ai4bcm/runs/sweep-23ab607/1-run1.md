# /ask-ai4bcm case 1, run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a091a0e9-abc1-4e1e-b956-090d64715148`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is Stage 3, **Analysis**, before the interview. You don't need a connector for it.

**Check the data first.** Anything about your dispatch activity counts as BIA data, which [`units/data-rules.md`](units/data-rules.md) classes as high-sensitivity. That means you may only use your approved corporate or private environment. Never put it into a public online tool. If you can't say where the data goes and how long it stays there, don't paste it yet.

**Skill to run: `/prepare-bia`**
- **What it does:** It asks who the interview is with (your dispatch lead) and what you need back. Then it drafts the interview guide from the material you attach: candidate activities, resource requirements in four classes (people, seats and buildings, IT and applications, suppliers), dependencies, and questions. It leaves the recovery fields blank.
- **Read first:** [`units/stages/analysis.md`](units/stages/analysis.md), then [`units/prompts/bia.md`](units/prompts/bia.md), Task choice 1. The workflow is in [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate:** A saved prompt, approved tools, a written data rule and a named reviewer.
- **Effort:** About forty minutes for the dispatch activity.

**Points from the unit for next week:**
- Write down the sources you attach and their dates. Switch off memory, connectors and web search so the draft is built only from what you give it.
- Treat the draft as something for the dispatch lead to correct, not to confirm. Record what it couldn't have known.
- Every resource requirement the AI drafts is only a question for the activity owner. It goes into the register only once they confirm it. Your dispatch lead or the activity owner sets the RTO and MTPD, not the AI.

**After the interview,** the AI4BCM BIA-Workflow takes the record on.

The skill starts only when you type **`/prepare-bia`**.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/analysis.md`
