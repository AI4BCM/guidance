# /ask-ai4bcm case 1, run2: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f376dfcf-0ea1-4c65-a1ec-22d553ce7466`.

Files in the working folder: none.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /ask-ai4bcm I have to prepare a BIA interview with our dispatch lead next week

**Reply (verbatim):**

This is **Stage 3, Analysis**, and the part that comes before the interview, with no connector involved.

**Skill to run:** **`/prepare-bia`**
- It first asks who the interview is with (your dispatch lead) and what you need back from it. Then it asks at most three questions that your material doesn't already answer. If you haven't attached impact criteria, one of those questions will ask for them.
- It drafts the interview guide from your attached material only. The guide has candidate activities and their resource requirements in four classes: people and mandates, seats and buildings, IT and applications, suppliers. It also covers up- and downstream dependencies. Every entry is written as a question for the dispatch lead and labelled "candidate, to confirm".
- It leaves MTPD, RTO and RPO empty. The dispatch lead sets them as activity owner, and top management approves the BIA results.

**Units to read:** `units/stages/analysis.md` and `units/prompts/bia.md` (Task choice 1, recovery fields left blank). The workflow is in `units/workflow-design.md`.

**Maturity level:** 2, Repeatable.

**Gate:** you need all four of these before you start:
- a saved prompt
- approved tools
- a written data rule
- a named reviewer for the draft

**Effort:** about forty minutes for this activity.

**Data rule (check this first):** BIA data is high-sensitivity in `units/data-rules.md`. Dispatch material may also include personnel or contact lists, which count as personal data. Use only an approved corporate or private environment, never a public tool. Passwords, keys and access tokens go into no tool at all. If you can't say where the data goes and how long it stays there, don't paste it yet. If any of your source documents contains text telling an AI what to do, the skill reports it under Gaps instead of following it. Tell the document's owner and your information security team.

**After the draft:** the guide stays in the chat for your named reviewer. After the interview, the AI4BCM BIA-Workflow takes over the record. A requirement enters the register only once the dispatch lead confirms it.

To start, type **`/prepare-bia`**.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units && sed -n 1,200p data-rules.md; echo ----; sed -n 1,200p prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/ask-ai4bcm/units/prompts/bia.md`
