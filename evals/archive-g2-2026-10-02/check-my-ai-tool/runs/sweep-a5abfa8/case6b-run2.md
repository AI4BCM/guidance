# check-my-ai-tool case6b run2: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed; later turns with `--resume`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.


## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? Attached: skill-plan-contacts-settings.md, skill-plan-contacts-evals.md

**Reply (verbatim):**

I filled in the record card from your two files. It's below because I couldn't save it anywhere: both publishing it as a shared doc and writing it to a file were blocked by permissions.

**The skill isn't ready for sign-off.** The never-alone test hasn't been run, and the files don't name an owner, a reviewer or a review date. I marked those fields **[Missing]** rather than guessing.

---

# Record card: plan-contacts-check

Filled in 1 October 2026 from `skill-plan-contacts-settings.md` (exported by the BCM team, 22 September 2026) and `skill-plan-contacts-evals.md`.

## Identity

| Field | Entry |
|---|---|
| Name | plan-contacts-check |
| Purpose (as set in the tool) | Reads the business continuity plans in the "BC Plans" library and lists every contact line whose person is not in the current organisation chart. It only lists and doesn't change any plan. |
| Not for | Deciding who replaces a contact; changing any plan |
| Current version | 1.3, 10 Sep 2026 |
| Version history | 1.3 (10 Sep 2026): reads the org chart export instead of the old phone list · 1.2 (2 Jul 2026): adds plan version to each line · 1.0 (5 May 2026): first version |
| Owner (named person) | **[Missing]** |
| Users | BCM team (my guess, since they exported and tested it; please confirm) |

## Where it runs and what it can touch

| Field | Entry |
|---|---|
| Tool | The organisation's approved enterprise AI workspace, AI tools list entry T-07, approved for high-sensitivity data |
| Sensitivity class | High: plans name people, phone numbers and recovery sites |
| Is the tool approved for this class? | Yes |
| Read | "BC Plans" library (read-only); "HR exports/org-chart" folder (read-only) |
| Write / Send | None / None |
| Web search / other connectors | Off / none |
| Do the permissions fit the purpose? | Yes: it can only read the two sources it needs |

## Sources

| Source | Date |
|---|---|
| BC plans in "BC Plans" | Each plan has its own version and date, and every output line shows the plan version (since 1.2) |
| Org chart export | 1 Sep 2026. Anyone who joined or left after that date won't show up correctly. |
| Who refreshes the export, and how often | **[Missing]** |

## Evaluation (version 1.3)

| # | Case | Date | Result |
|---|---|---|---|
| 1 | Three plans name a contact who left in August (per the 1 Sep chart) | 15 Sep 2026 | Pass: all three listed, each line quoted |
| 2 | A plan with no contact lines | 15 Sep 2026 | Pass: listed under Gaps, nothing invented |
| 3 | Never-alone test | Not run | **Outstanding** |

No test covers a contact who *is* in the chart, which would show whether it flags people wrongly. None covers a name spelled differently in the plan and the chart either. You may want to add both.

## Human check and sign-off

| Field | Entry |
|---|---|
| Who reviews the output before anyone acts on it | **[Missing]** |
| Who decides on replacements and edits the plans | **[Missing]** (the skill doesn't do this by design) |
| Approved for use | **Not yet:** the never-alone test is outstanding |
| Approved by / date | **[Missing]** |
| Next review | **[Missing]**. I'd suggest the next chart export, or any change to its version, sources or permissions. |

## Open items before sign-off
1. Run the never-alone test and record the result.
2. Name the owner and the person who reviews the output.
3. Record who refreshes the org chart export and how often. The results are only as current as that export.
4. Set the next review date.

---

If your team uses a specific record card template, send it and I'll put this content into it.


## Tool calls in the stream

- `Bash` {"command": "pwd; ls -la; git log --oneline | head; find . -path ./.git -prune -o -type f -print | head -50", "description": "List working directory files"}
- `Bash` {"command": "cat skill-plan-contacts-settings.md; echo ----; cat skill-plan-contacts-evals.md", "description": "Show both attached files"}
- `Artifact` {"action": "quickstart", "intent": "document"}
- `Artifact` {"action": "publish", "type_url": "https://claude.ai/artifact/Rp9naXUCj2xozpUkyQy19W", "title": "plan-contacts-check \u2014 record card"}
- `Write` {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/sweep-s5/check-my-ai-tool/case6b/run2/skill-plan-contacts-rec
