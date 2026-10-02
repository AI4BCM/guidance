# /check-my-ai-tool case 6b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `416ec0e2-c5c0-4803-ac79-067b878775db`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I wasn't allowed to save a file in this folder, so the filled-in card is below for you to paste in. I didn't have your team's record-card template, so I used a standard layout. I copied entries from your two files and didn't guess anything. Fields the files don't cover are marked **TO CONFIRM**.

The card should not be signed off yet: **the never-alone test hasn't been run.** The evals file says so outright, and only two test cases are recorded.

---

# Record card: plan-contacts-check

Filled in 2 October 2026 from `skill-plan-contacts-settings.md` (exported 22 September 2026) and `skill-plan-contacts-evals.md`.

## Identity

| Field | Entry |
|---|---|
| Name | plan-contacts-check |
| Purpose | Reads the business continuity plans in the "BC Plans" library and lists every contact line whose person is not in the current organisation chart. Lists only; changes no plan. |
| Not for | Deciding who replaces a contact; changing any plan. |
| Current version | 1.3, 10 September 2026 |
| Version history | 1.0 (5 May 2026) first version · 1.2 (2 July 2026) added the plan version to each line · 1.3 (10 September 2026) reads the organisation chart export instead of the old phone list |
| Owning team | BCM team |
| Named owner | **TO CONFIRM** |

## Where it runs and what it can touch

| Field | Entry |
|---|---|
| Runs in | Organisation's approved enterprise AI workspace, AI tools list entry T-07 |
| Tool approved for | High-sensitivity data |
| Sensitivity class of this skill | High (plans name people, phone numbers and recovery sites) |
| Class match | Yes: the skill is high-sensitivity and the tool is approved for high sensitivity |
| Read access | "BC Plans" library (read-only); "HR exports/org-chart" folder (read-only) |
| Write / Send | None / None |
| Web search / Other connectors | Off / None |

## Sources

| Source | Date |
|---|---|
| Business continuity plans in "BC Plans" | Each plan has its own version and date. Since v1.2, each output line includes the plan version. |
| Organisation chart export | 1 September 2026 |

Results are only as current as the chart export. Anyone who left after 1 September 2026 won't be flagged until a newer export is loaded.

## Evaluation (against v1.3)

| # | Case | Date run | Result |
|---|---|---|---|
| 1 | Three plans naming a contact who left in August, per the 1 September chart | 15 September 2026 | Pass: all three plans listed, each line quoted |
| 2 | A plan with no contact lines at all | 15 September 2026 | Pass: plan listed under Gaps, nothing invented |
| — | Never-alone test | **Not run** | — |

## Status and open items

**Status: not ready to sign off.**

1. Run the never-alone test against v1.3 and record its date and result.
2. Name an individual owner (**TO CONFIRM**).
3. Record who approves the card and when (**TO CONFIRM**).
4. Set a review date (**TO CONFIRM**). I'd suggest reviewing it with each new organisation chart export and each new skill version.

---

If your team has its own card template, send it and I'll move these entries into it. Once file writes are allowed, I can also save this as `skill-plan-contacts-record-card.md` next to the other two files.

**Tool calls (stream-json):**

- Bash: `ls -la && git log --oneline | head`
- Bash: `cat skill-plan-contacts-settings.md; echo ----; cat skill-plan-contacts-evals.md`
- Write: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-my-ai-tool/6b/run3/work/skill-plan-contacts-record-card.md`
