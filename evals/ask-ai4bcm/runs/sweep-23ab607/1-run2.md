# /ask-ai4bcm case 1, run2: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `777280cb-6074-46dd-827f-3048d1e5efed`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

Preparing for a BIA interview is Stage 3, Analysis, specifically the "before the interview" step. You don't need a connector for it.

**Before anything else: classify your material.** BIA data is in the high-sensitivity class (`units/data-rules.md`). Your dispatch notes, process maps and earlier BIA records may only go into an approved corporate or private environment, never a public online tool. Passwords, keys and access tokens go into no tool. If you can't say where the data goes and how long it stays there, don't paste it yet.

**The route**

- **Skill:** **`/prepare-bia`**. It asks who the interview is with (your dispatch lead) and what you need back. Then it drafts the interview guide from your material, using Task choice 1 with the recovery fields left blank. It starts only when you type `/prepare-bia` yourself. I haven't started it.
- **Read first:** [`units/stages/analysis.md`](units/stages/analysis.md) and [`units/prompts/bia.md`](units/prompts/bia.md). The workflow is in [`units/workflow-design.md`](units/workflow-design.md).
- **Maturity level:** Level 2, Repeatable.
- **Gate:** you need all four of these before you run it:
  1. a saved prompt
  2. approved tools
  3. a written data rule
  4. a named reviewer for the draft guide
- **Effort:** about forty minutes for this one activity.
- **Data rule:** [`units/data-rules.md`](units/data-rules.md). BIA material stays in your approved environment.

**After the draft:** the guide is a draft for you and your named reviewer to check before next week's interview. After the interview, the AI4BCM BIA-Workflow takes the record on.

If the gate isn't met yet, say a data rule hasn't been written down, sort that out first. Until then, no tool is approved for this material.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
