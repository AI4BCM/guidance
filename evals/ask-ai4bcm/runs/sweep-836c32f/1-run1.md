# /ask-ai4bcm case 1, run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `56f93e9a-1c23-45fa-9ff0-f62b38136db2`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**. You're preparing for the interview and have no connector, so use **`/prepare-bia`**.

- **Skill:** `/prepare-bia`. It starts only when you type it. First it asks who the interview is with (your dispatch lead) and what you need back. Then it drafts the interview guide from your own material, with the recovery fields left blank (Task choice 1 in the BIA prompt).
- **Read first:** [`units/stages/analysis.md`](/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/stages/analysis.md) and [`units/prompts/bia.md`](/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/prompts/bia.md). The workflow is in [`units/workflow-design.md`](/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/workflow-design.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate (Level 2):** "the prompt that worked is saved for reuse, approved tools are named, the data rule is written down, every prompt has a named reviewer, and outputs go through the normal approval route."
- **Effort:** about forty minutes per activity. If dispatch covers several activities, allow forty minutes for each.
- **Data rule:** check [`units/data-rules.md`](/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md) before you paste anything. BIA material is the most sensitive material in BCM. Classify your dispatch documents first, and use only a tool approved for that class.

**After the interview:** the AI4BCM BIA-Workflow takes over the record. If you later want to work across connected records, that's Level 3 and needs Level 3's gate.

To begin, type `/prepare-bia`.

**Tool calls (stream-json):**

- none
