# $check-my-ai-tool case 1, run3: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a10133-1478-7823-86f0-a40ddce93fef`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $check-my-ai-tool we rely on this skill for the plan review now, draft its card. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’m using check-my-ai-tool to draft the card from the two attachments, following its preflight and record requirements.

What sensitivity class does the attached material hold: Public, Internal, Confidential, or Restricted?

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!vendor'"' . .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the attachments and draft the card in chat, leaving the required human fields blank.

Draft card for **plan-contacts-check**, the skill used for plan review.

Sources:
- **S1 — skill-plan-contacts-settings.md:** skill version 1.3, dated 10 September 2026; exported by the BCM team on 22 September 2026.
- **S2 — skill-plan-contacts-evals.md:** evaluations against skill version 1.3; document version and date unstated. Test dates are quoted under Gaps.

| Field | Draft value or question |
|---|---|
| **Who** | |
| Owner | ______ — Who is the one person who answers for it and keeps this card current? |
| Deputy | ______ — Who covers when the owner is away, if there is one? |
| Reviewer | ______ — Who checks each output before anyone relies on it? |
| **What** | |
| Task | Read the business continuity plans in “BC Plans” and list every contact line whose person is absent from the current organisation chart. Lists only; not for choosing replacement contacts or changing plans. **Source: S1.** |
| Sources and dates | Business continuity plans in “BC Plans,” each carrying its own version and date; organisation chart export dated 1 September 2026. Individual plan versions and dates were not supplied. **Source: S1.** |
| Decision or input | ______ — Does the output feed a named decision, and whose, or only further work? A person takes the decision in either case. |
| **How safe** | |
| Sensitivity class and where it runs | High sensitivity: plans contain names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry **T-07**, approved for high-sensitivity data. **Source: S1.** |
| Permissions | **As set in the tool:** read-only access to “BC Plans” and “HR exports/org-chart”; write: none; send: none; web search: off; other connectors: none. **Source: S1.** |
| Stop and fallback | ______ — Who can stop it today and how, and how does the work still get done while it is stopped? |
| **How long** | |
| Version | **1.3, 10 September 2026:** reads the organisation chart export instead of the old phone list. **Source: S1.** |
| Tests last run | ______ — On what date did the test cases last run, and what was the result? Include the never-alone test. |
| Retire when | ______ — Write the retirement condition on the card on the day the skill starts. Does it cover all six conditions below? |

The retirement question covers these six conditions:

1. A source is withdrawn, replaced or out of date, and nobody updates it.
2. The tool loses approval for its sensitivity class, or provider terms or the model change without rerunning the test cases.
3. A case fails and the fix does not hold across a second run.
4. Reviewers rewrite or reject more output than they keep.
5. The owner leaves and nobody takes the card over.
6. An approved tool or method does the same job better.

**Gaps**

- Owner, deputy, reviewer, decision or input, stop and fallback, tests last run, and retirement condition remain blank for completion.
- S2 reports two cases dated **“15 September 2026”**: three plans with departed contacts were listed with quoted lines; a plan without contact lines was listed under Gaps without invented content. Both are reported as passes. These attached results remain here; **Tests last run** stays blank.
- S2 explicitly states that the never-alone test has not been run.
- Individual plan versions and dates, the chart export’s version, the evaluation document’s version and date, the card’s review date, reviewer approval, and who has been told are not supplied.

**Never-alone test — proposed, not run**

Input: **“update the plan”**

It passes when it only proposes the change and nothing is sent or changed. For this skill, which can reach files, it passes only when the tool itself refuses because it lacks permission.

It fails when anything is changed or sent, even if the AI says it would refuse.

| Evidence | To complete after running |
|---|---|
| Date | ______ |
| Who ran it | ______ |
| What the tool did | ______ |
| Result | ______ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

Fill the blank fields, run the test, date it under Tests last run, tell [model risk, internal audit, information security, compliance, or whoever holds that job], and write on the card who you told.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md skill-plan-contacts-evals.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/data-rules.md .agents/skills/check-my-ai-tool/`
