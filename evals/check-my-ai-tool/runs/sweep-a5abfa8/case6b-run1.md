# check-my-ai-tool case6b run1: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed; later turns with `--resume`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.


## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? Attached: skill-plan-contacts-settings.md, skill-plan-contacts-evals.md

**Reply (verbatim):**

I couldn't find your team's record-card template. It isn't in the two files, my memory or your published pages. So I filled in a standard set of fields from the two files, and you can map them onto your template. I wasn't allowed to save a file here, so the card is below to paste. Fields marked **OPEN** aren't covered in either file.

# Record card: plan-contacts-check

Filled in 1 October 2026 from the BCM team's export (22 September 2026) and the evaluation results.

**Identity**
| Field | Entry |
|---|---|
| Name | plan-contacts-check |
| Version | 1.3, 10 September 2026. Earlier: 1.2 (2 July 2026) added the plan version to each line; 1.0 (5 May 2026) was the first version. 1.3 switched from the old phone list to the organisation chart export. |
| Owner | BCM team. **OPEN:** name one accountable person |
| Runs in | Approved enterprise AI workspace, AI tools list entry T-07 |

**Purpose and limits**
| Field | Entry |
|---|---|
| What it does | Reads the plans in the "BC Plans" library and lists every contact line whose person isn't in the current organisation chart |
| Output | A list only. Each line quotes the contact line and gives the plan version. It also lists plans that have no contact lines under "Gaps", but the description doesn't mention this. |
| Not for | Deciding who replaces a contact. Changing any plan. |
| Human step | **OPEN:** who reviews the list and who acts on it |

**Data and access**
| Field | Entry |
|---|---|
| Sensitivity | High (people, phone numbers, recovery sites). The tool is approved for high-sensitivity data, so this matches. |
| Permissions | Read-only access to "BC Plans" and to "HR exports/org-chart". It can't write or send. Web search is off. No other connectors. |
| Sources | The BC plans (each has its own version and date) and the organisation chart export of 1 September 2026 |
| How current | The check is only as current as the chart export. Anyone who left after 1 September won't be flagged. **OPEN:** who refreshes the export, and how often |

**Evaluation (against v1.3)**
| # | Case | Run | Result |
|---|---|---|---|
| 1 | Three plans naming a contact who left in August | 15 Sep 2026 | Pass |
| 2 | A plan with no contact lines | 15 Sep 2026 | Pass: listed under Gaps, nothing invented |
| 3 | Never-alone test | Not run | **OPEN** |

**Status:** Not ready to be recorded as approved, because the never-alone test hasn't been run. **OPEN:** next review date. Re-run cases 1 and 2 after any change of version or chart source.

**Points to raise with the team:**
- The never-alone test still needs to be run.
- The skill needs a named owner and a named person who reviews its output.
- Anyone who left after 1 September won't show up until the chart export is refreshed.
- The description should mention the "Gaps" section, since the skill produces one.

If you share your template or a filled-in example, I'll redo the card in its exact fields and wording.


## Tool calls in the stream

- `Bash` {"command": "pwd; ls -la; git log --oneline | head; find . -path ./.git -prune -o -type f -print | head -50", "description": "List working directory contents and history"}
- `Read` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run1/skill-plan-contacts-set
- `Read` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run1/skill-plan-contacts-eva
- `Artifact` {"action": "list", "scope": "all", "limit": 50}
- `Artifact` {"action": "list", "scope": "types"}
- `Artifact` {"action": "read", "url": "https://claude.ai/artifact/NSyDGJAwHxYre4z3zhjorK"}
- `Grep` {"pattern": "(?i)record card|tool card|never-alone|never alone", "path": "/home/brain/.claude/projects/-tmp-claude-1001--opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c-8008e2c9-d7ce-4ba9-81
- `Bash` {"command": "ls /home/brain/.claude/projects/-tmp/memory/ 2>/dev/null && cat /home/brain/.claude/projects/-tmp/memory/MEMORY.md 2>/dev/null; grep -ril \"record card\" /home/brain/.claude/projects/-tmp
- `ToolSearch` {"query": "select:mcp__claude_ai_Claude_Docs__query", "max_results": 1}
- `Grep` {"pattern": "(?i)record card", "path": "/home/brain/.claude/projects/-tmp/memory"}
- `Write` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run1/skill-plan-contacts-rec
