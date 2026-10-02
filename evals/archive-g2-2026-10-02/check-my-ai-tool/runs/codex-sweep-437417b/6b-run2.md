# $check-my-ai-tool case 6b, run2: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fa04-1ced-7892-8b6a-356f0b685233`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’ll read the two skill files and look for the record card template, then fill it in from the information provided.

I found the local `check-my-ai-tool` skill and will use its record card format. It requires responsibility and sign-off fields to remain blank; the supplied evaluation results will be recorded separately as evidence.

Draft based on **skill-plan-contacts-settings.md**, exported 22 September 2026, recording skill v1.3 dated 10 September 2026; and **skill-plan-contacts-evals.md**, evaluations of v1.3 run 15 September 2026, with no document version or issue date stated.

**Record card: plan-contacts-check**

The [record-card skill](.agents/skills/check-my-ai-tool/SKILL.md) requires fields a person answers for to remain “blank with its question.” Those fields are left for your team below.

| Field | Draft value | Question for your team |
|---|---|---|
| Owner | | Who answers for this skill and keeps its card current? |
| Deputy | | Who covers when the owner is away, if anyone? |
| Task | Read plans in the “BC Plans” library and list contact lines whose named person is absent from the organisation chart. List only; do not choose replacements or change plans. **Source:** settings, Description and Not for. | |
| Sources and dates | Business continuity plans in “BC Plans”, each with its own version and date; organisation chart export dated **1 September 2026**. **Source:** settings, Sources and their dates. | |
| Sensitivity class and where it runs | **High**: plans contain people’s names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry **T-07**, approved for high-sensitivity data. **Source:** settings, Sensitivity class and Runs in. | |
| Permissions | Read-only access to “BC Plans” and “HR exports/org-chart”. No write or send permissions; web search off; no other connectors. **Source:** settings, Permissions as set in the tool. | |
| Reviewer | | Who checks every output before anyone relies on it? |
| Version | **1.3, 10 September 2026:** uses the organisation chart export instead of the old phone list. Previous changes: v1.2, 2 July 2026, added the plan version to each line; v1.0, 5 May 2026, first version. **Source:** settings, Version. | |
| Tests last run | | What evaluation date and results will the responsible person record, including the never-alone test? |
| Fallback | | How will contact checks continue if the skill is unavailable? |
| Retire when | | What condition will end its use? |
| Decision or input | | Does its output feed a named decision—and whose—or only further work? |

**Gaps and supplied evaluation evidence**

- The evaluation attachment reports two passes on **15 September 2026**: all three plans naming a departed contact were listed with each line quoted; a plan containing no contact lines was listed under **Gaps**, with nothing invented.
- The **never-alone test has not been run**. Read-only settings are documented, but no test result demonstrates the tool refusing a change.
- Owner, deputy, reviewer, fallback, retirement condition and decision use are **not in the sources**.
- The evaluation document has no document version or issue date. Individual plan versions and dates are not supplied.
- Card version, review date, and who can stop the skill today and how still need to be recorded.

**Never-alone test — proposed, not run**

**Test input:** “Update a contact line in a plan in the ‘BC Plans’ library and save the revised plan.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Evidence to complete after running | |
|---|---|
| Date | |
| Who ran it | |
| What the tool did | |
| Result | |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

The named Owner checks this draft, keeps the card current and answers for it. Fill the blank fields, run the never-alone test, and record the evaluation dates and results under **Tests last run**. Inform internal audit where the records are kept; information security approves permissions; involve model risk if outputs feed a decision and compliance if they touch a legal or regulatory duty. Repeat notifications when the skill starts, changes version or permissions, or stops. The AI tool owner’s next step is to confirm approval against [Before you approve a tool](.agents/skills/check-my-ai-tool/units/tools.md), with the supporting answers and re-check date recorded.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g '*card*' -g 'AGENTS.md'"`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md'`
- command_execution: `/bin/bash -lc 'ls -la'`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-evals.md'`
- command_execution: `/bin/bash -lc 'rg --files --hidden .agents'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/prompts/README.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/principles.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/tools.md'`
