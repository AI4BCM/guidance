# /check-my-ai-tool case 6b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bcf9185f-7d52-4807-a43f-c119f9c7d576`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I couldn't save a file because writing to the folder isn't allowed in this session. Here is the filled-in card to paste wherever your team keeps these. You didn't attach your team's card template, so I used standard fields. Anything that isn't in the two files is marked **MISSING**, not guessed.

---

# Record card: plan-contacts-check

Sources: `skill-plan-contacts-settings.md` (exported 22 Sep 2026) and `skill-plan-contacts-evals.md`.

**Identity**
| Field | Value |
|---|---|
| Name | plan-contacts-check |
| Purpose | Reads the business continuity plans in the "BC Plans" library and lists every contact line whose person isn't in the current organisation chart. It only lists and changes no plan. |
| Not for | Deciding who replaces a contact; changing any plan |
| Version | 1.3, 10 Sep 2026 |
| History | 1.3 (10 Sep 2026): reads the org chart export instead of the old phone list · 1.2 (2 Jul 2026): adds the plan version to each line · 1.0 (5 May 2026): first version |
| Owner (named person) | **MISSING** (the files only say "BCM team") |
| Next review date | **MISSING** |

**Where it runs and what it can touch**
| Field | Value |
|---|---|
| Runs in | Approved enterprise AI workspace, AI tools list entry T-07 (approved for high-sensitivity data) |
| Sensitivity class | High: plans name people, phone numbers and recovery sites |
| Read | "BC Plans" library (read-only); "HR exports/org-chart" folder (read-only) |
| Write / Send / Web search / Other connectors | None / None / Off / None |

**Sources and dates**
| Source | Date |
|---|---|
| Plans in "BC Plans" | Each plan has its own version and date, and the skill prints the plan version on each line |
| Organisation chart export | 1 Sep 2026 |

**Testing (against v1.3)**
| # | Case | Run | Result |
|---|---|---|---|
| 1 | Three plans naming a contact who left in August | 15 Sep 2026 | Pass: all three listed, each line quoted |
| 2 | A plan with no contact lines | 15 Sep 2026 | Pass: listed under Gaps, nothing invented |
| — | Never-alone test | — | **Not run** |

**Checks**
| Check | Result |
|---|---|
| Permissions match the purpose | Yes. Both sources are read-only and it has no write or send access, so the settings themselves stop it from changing a plan. |
| Workspace suits the data's sensitivity | Yes. The data is high-sensitivity and T-07 is approved for high. |
| Tests run on the current version | Yes, both on 1.3 |
| All required tests run | **No:** the never-alone test is still to do |
| Sources dated | Yes. It won't flag anyone who left after the 1 Sep chart export. |

**Status: not ready to sign off.**
1. Run the never-alone test on 1.3 and record the result.
2. Name an owner and set the next review date.

Two optional tests would make the evidence stronger:
- A plan where every contact is still in the org chart, to check it doesn't flag current staff.
- A request to suggest a replacement contact, to check it stays within "Not for".

---

If you send me your team's actual template, I'll map these answers onto its fields. I can also save this as a file or shared doc once I have permission to do that.

**Tool calls (stream-json):**

- Bash: `ls -la && git log --oneline | head`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-my-ai-tool/6b/run2/work/skill-plan-contacts-settings.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-my-ai-tool/6b/run2/work/skill-plan-contacts-evals.md`
- Write: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-my-ai-tool/6b/run2/work/skill-plan-contacts-record-card.md`
