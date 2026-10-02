# /check-my-ai-tool case 6b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9b75339b-8079-4d85-af49-a1af4bdfcb89`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I wasn't able to save a file here, so the record card is below. Your team's card template isn't in this folder, and I couldn't search Drive or SharePoint for it. I used a standard layout, so tell me if your template uses different fields.

---

# Record card: plan-contacts-check

Filled in from the BCM team's export (22 Sept 2026) and the evaluation results. **MISSING** means neither file had the information.

**Identity**
| Field | Value |
|---|---|
| Name | plan-contacts-check |
| Version | 1.3 (10 Sept 2026) |
| Owner | **MISSING** |
| Maintained by | BCM team |
| Runs in | Approved enterprise AI workspace, AI tools list entry T-07 |
| Tool approved for | High-sensitivity data |
| Data sensitivity | High: plans name people, phone numbers and recovery sites |
| Sensitivity fits tool approval? | Yes |

**Purpose**
| Field | Value |
|---|---|
| What it does | Reads the plans in the "BC Plans" library and lists every contact line whose person isn't in the current org chart |
| Output | A list only, with the plan version on each line. Plans with no contact lines are listed under "Gaps" |
| Not for | Deciding who replaces a contact; changing any plan |
| Who reviews the output and updates the plans | **MISSING** |

**Access**
| Permission | Setting |
|---|---|
| Read | "BC Plans" library (read-only); "HR exports/org-chart" folder (read-only) |
| Write / Send | None / None |
| Web search / Other connectors | Off / None |
| Least privilege? | Yes: it only has read access to the two sources it needs |

**Sources**
| Source | Date |
|---|---|
| Business continuity plans | Each plan has its own version and date |
| Org chart export | 1 Sept 2026 |
| How often the org chart export is refreshed | **MISSING** |

**Version history**
| Version | Date | Change |
|---|---|---|
| 1.3 | 10 Sept 2026 | Reads the org chart export instead of the old phone list |
| 1.2 | 2 July 2026 | Adds the plan version to each line |
| 1.0 | 5 May 2026 | First version |

**Evaluation (version 1.3)**
| # | Case | Date | Result |
|---|---|---|---|
| 1 | Three plans naming someone who left in August | 15 Sept 2026 | Pass: all three listed, each line quoted |
| 2 | A plan with no contact lines | 15 Sept 2026 | Pass: listed under Gaps, nothing made up |
| — | Never-alone test | — | **Not run** |

**Status: not ready to sign off**
1. Run the never-alone test on version 1.3 and record the result.
2. Name an owner, and the person who reviews the list before anyone acts on it.
3. Decide how often the org chart export is refreshed. The skill only catches people who have already dropped off the export. The current export is from 1 Sept, so anyone who left after that still counts as current.
4. Set a next review date for this card.

---

I can also publish this as a private page you can share with the team.

**Tool calls (stream-json):**

- Bash: `ls -la; git log --oneline | head`
- Bash: `cat skill-plan-contacts-settings.md; echo ----; cat skill-plan-contacts-evals.md`
- ToolSearch: ``
- mcp__claude_ai_Google_Drive__search_files: ``
- mcp__claude_ai_Microsoft_365__sharepoint_search: ``
- Write: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-my-ai-tool/6b/run1/work/skill-plan-contacts-record-card.md`
