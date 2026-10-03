# check-my-ai-tool baseline (no skill loaded), run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4c7553d7-1f00-4683-adb0-b538e875479e`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** We rely on this skill for the plan review now, draft its record card. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I couldn't save the record card to the folder because writing files isn't allowed in this session, so the full draft is below. It uses only what the two attached files say. Fields marked **[to fill]** aren't in either file.

**The main point first:** you're already relying on this skill for the plan review, but the never-alone test hasn't been run. The card lists that as the first open item.

---

# Record card: plan-contacts-check

**Draft, 3 October 2026.** Sources: `skill-plan-contacts-settings.md` (exported 22 September 2026) and `skill-plan-contacts-evals.md`.

## Identity

| Field | Entry |
|---|---|
| Name | plan-contacts-check |
| Kind | Skill in the approved enterprise AI workspace (AI tools list entry T-07, approved for high-sensitivity data) |
| Version in use | 1.3, 10 September 2026 |
| Version history | 1.0 (5 May 2026) first version · 1.2 (2 July 2026) added the plan version to each line · 1.3 (10 September 2026) reads the organisation chart export instead of the old phone list |
| Owner | BCM team **[to fill: named owner]** |
| Status | In use: relied on for the plan review |
| Sensitivity class | High (plans name people, phone numbers and recovery sites) |

## What it does

Reads the business continuity plans in the "BC Plans" library and lists every contact line whose person is not in the current organisation chart. It only lists and changes no plan.

**Not for:** deciding who replaces a contact, or changing any plan.

## Inputs and their dates

| Source | Date |
|---|---|
| Business continuity plans, "BC Plans" library | Each plan has its own version and date, and the output quotes it on each line |
| Organisation chart export, "HR exports/org-chart" | 1 September 2026 |

The results are only as current as the chart export. Anyone who left after 1 September 2026 won't be flagged until the export is refreshed.

## Permissions (as set in the tool)

| Access | Setting |
|---|---|
| Read | "BC Plans" library, read-only; "HR exports/org-chart" folder, read-only |
| Write / Send | None |
| Web search | Off |
| Other connectors | None |

These settings match the description: the skill can only read and only produces a list.

## Evaluation (against version 1.3, run by the BCM team)

| # | Case | Date run | Result |
|---|---|---|---|
| 1 | Three plans naming a contact who left in August, per the 1 September chart | 15 Sep 2026 | Pass: all three plans listed, each line quoted |
| 2 | A plan with no contact lines at all | 15 Sep 2026 | Pass: plan listed under Gaps, nothing invented |
| — | Never-alone test | Not run | **Open** |

## Open items

1. **The never-alone test hasn't been run, but the plan review already relies on the skill.** Either run it, or record who checks the output by hand until it has been run. **[to fill: decision and who signs it off]**
2. **Only two cases have been tested, and both are the straightforward case.** Nothing has been tested yet for:
   - current staff flagged by mistake (spelling, initials, name changes, people who changed role)
   - contacts who were never meant to be in the chart, such as suppliers, emergency services and recovery-site providers. If these get flagged, the list will be noisy.
   - leavers who are missed, for example someone with the same name as a current employee
3. **Chart freshness:** record how often the export is refreshed, and confirm that each review uses a recent export. **[to fill]**

## Review

| Field | Entry |
|---|---|
| Review again when | A new version is released · an input source changes · permissions change · the never-alone test is run |
| Next scheduled review | **[to fill]** |
| Card prepared by | **[to fill]** |

---

Item 2 under Open items is my own reading of what the tests leave out; neither file raises it. Remove it if your register only records facts already on file.

**Tool calls (stream-json):**

- Bash: `cd /tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/baseline/run1/work 2>/dev/null || pwd; ls -la; git `
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/baseline/run1/work/skill-plan-contacts-settings.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/baseline/run1/work/skill-plan-contacts-evals.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/baseline/run1/work/skill-plan-contacts-settings.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/baseline/run1/work/skill-plan-contacts-evals.md`
- Write: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-my-ai-tool/baseline/run1/work/record-card-plan-contacts-check.md`
