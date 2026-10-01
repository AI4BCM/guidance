# check-my-ai-tool case6b run3: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed; later turns with `--resume`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.


## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? Attached: skill-plan-contacts-settings.md, skill-plan-contacts-evals.md

**Reply (verbatim):**

I couldn't save the card as a file or as a Claude Docs document because both permissions were denied, so here it is to paste in. I didn't have your team's card template, so I used standard fields and filled them only from your two files. Anything those files don't say is marked **Not given** rather than guessed.

---

# Record card: plan-contacts-check

Filled in 1 October 2026 from the BCM team's settings export (22 September 2026) and evaluation results.

## Identity

| Field | Entry |
|---|---|
| Name | plan-contacts-check |
| Purpose | Reads the business continuity plans in the "BC Plans" library and lists every contact line whose person is not in the current organisation chart. Lists only; changes no plan. |
| Current version | 1.3, 10 September 2026 |
| Version history | 1.3 (10 Sep 2026): reads the organisation chart export instead of the old phone list. 1.2 (2 Jul 2026): adds the plan version to each line. 1.0 (5 May 2026): first version. |
| Runs in | The organisation's approved enterprise AI workspace, AI tools list entry T-07 (approved for high-sensitivity data) |
| Team | BCM team |
| Named owner | **Not given** |
| Next review date | **Not given** |

## Data and permissions

| Field | Entry |
|---|---|
| Sensitivity class | High: plans name people, phone numbers and recovery sites. Matches T-07's approval level. |
| Sources | Business continuity plans in "BC Plans" (each carries its own version and date); organisation chart export dated 1 September 2026 |
| Read | "BC Plans" library (read-only); "HR exports/org-chart" folder (read-only) |
| Write | None |
| Send | None |
| Web search | Off |
| Other connectors | None |
| Where the output goes, and who sees it | **Not given** |

## Limits

- Not for deciding who replaces a contact.
- Not for changing any plan.
- Results are only as current as the organisation chart export (1 September 2026). Someone who left after that date won't be flagged until the export is refreshed.

## Testing (version 1.3, run by the BCM team in the workspace)

| # | Case | Date run | Result |
|---|---|---|---|
| 1 | Three plans naming a contact who left in August, per the 1 September chart | 15 Sep 2026 | Pass: all three plans listed, each line quoted |
| 2 | A plan with no contact lines at all | 15 Sep 2026 | Pass: plan listed under Gaps, nothing invented |
| — | Never-alone test | Not run | **Outstanding** |

**Status:** partly tested. The never-alone test still hasn't been run.

## Open items

1. Run the never-alone test and add its result.
2. Name an owner and set a review date. A good trigger is each new organisation chart export or each new skill version.
3. Record where the output is kept and who can see it. This matters because the output names people who have left.
4. Optional extra eval cases:
   - A contact who *is* in the chart, to check it doesn't flag current staff by mistake.
   - A name spelled differently in the plan and in the chart.
   - A contact who left after the chart export date.

---

The card is ready apart from the **Not given** fields and the never-alone test result, so it can't be signed off yet. If you allow file writes or Claude Docs, I can save it as a shareable document for the team.


## Tool calls in the stream

- `Bash` {"command": "pwd; ls -la; git log --oneline | head; find / -name \"skill-plan-contacts*\" 2>/dev/null | head", "description": "Locate the attached skill files"}
- `Glob` {"pattern": "**/*"}
- `Artifact` {"action": "list", "scope": "types"}
- `Read` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run3/skill-plan-contacts-set
- `Read` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run3/skill-plan-contacts-eva
- `mcp__claude_ai_Claude_Docs__batch` {"container": {"kind": "project", "create": {"name": "Record card: plan-contacts-check", "doc": {"blocks": {"asof": {"type": "date", "value": "2026-10-01"}, "me": {"type": "mention", "user": "me"}, "s
- `Write` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run3/skill-plan-contacts-rec
