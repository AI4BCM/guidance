# check-my-ai-tool baseline (no skill loaded), run1: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a1013a-c137-7a12-ae80-bbbfd07af9da`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** We rely on this skill for the plan review now, draft its record card. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’ll read the two attached files and use them to draft the skill’s record card.

## Draft record card — plan-contacts-check

| Field | Record |
|---|---|
| Purpose | Support business continuity plan review by listing contact lines whose named person is absent from the current organisation chart. |
| Version | 1.3, dated 10 September 2026. Replaced the old phone list with the organisation chart export. |
| Business owner | BCM team; accountable individual to be recorded. |
| Environment | Organisation’s approved enterprise AI workspace, tool entry T-07, approved for high-sensitivity data. |
| Data sensitivity | High: plans contain names, phone numbers and recovery sites. |
| Sources | “BC Plans” library, with each plan’s version and date; “HR exports/org-chart”, export dated 1 September 2026. |
| Access and actions | Read-only access to both sources. No write or send permissions; web search off; no other connectors. |
| Output | Contact exceptions for review, with plan version and quoted contact line; plans without contact lines reported under **Gaps**. |
| Outside scope | Choosing replacement contacts or changing plans. |

**Evidence recorded:** The BCM team tested version 1.3 on 15 September 2026. Both documented cases passed: all three plans naming a departed contact were listed with quoted lines; a plan without contact lines was reported under Gaps without invented content.

**Assurance status:** Evidence is limited to those two cases. The **never-alone test has not been run**. The workspace’s approval for high-sensitivity data does not establish that the skill is reliable enough to complete a plan review independently.

**Human review control — proposed for adoption:** A BCM reviewer verifies findings against the relevant plan and a sufficiently current organisation chart, investigates gaps, and authorises any subsequent plan changes. Absence from the chart is a review flag, not proof that a contact is invalid. A clean result should not by itself close the contact review.

**Known limitations:** Chart omissions, name differences and outdated source data may affect results. The documented tests do not establish performance across these conditions. The September export may miss later staffing changes.

**Outstanding before treating the skill as an assured review control:** Run and record the never-alone test; confirm source freshness; assign the accountable owner and next review date.

*Sources: [settings](skill-plan-contacts-settings.md) and [evaluation results](skill-plan-contacts-evals.md), exported by the BCM team on 22 September 2026.*

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g 'AGENTS.md' -g 'skill-plan-contacts*' -g '*record*' -g '*card*'"`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-evals.md'`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md'`
