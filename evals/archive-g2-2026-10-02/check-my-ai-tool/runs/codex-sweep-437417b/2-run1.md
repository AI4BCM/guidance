# $check-my-ai-tool case 2, run1: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9fb-5e2d-7c22-8bd7-d39244e148e7`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $check-my-ai-tool we rely on this skill for the plan review now, draft its card. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’m using the check-my-ai-tool skill to draft the card from the two attached files, leaving the fields that require a person’s answer blank.


What sensitivity class do the two attachments contain, and is this environment approved for that class?

The skill’s [preflight](.agents/skills/check-my-ai-tool/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I need that answer before opening the files and drafting the card.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' . .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/preflight.md .agents/skills/check-my-ai-tool/SKILL.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the attachments and draft the card and never-alone test. The card’s Owner, once named, keeps it current; information security approves permissions, and the AI tool owner approves the tool.


From **skill-plan-contacts-settings.md**: skill v1.3, dated 10 September 2026; settings exported 22 September 2026.
From **skill-plan-contacts-evals.md**: evaluates v1.3; cases dated 15 September 2026; document version and issue date not stated.

**Draft card — plan-contacts-check**

“Settings” below means *skill-plan-contacts-settings.md*.

| Field | Draft value or question to answer |
|---|---|
| Owner | ______ — Who answers for this skill and keeps its card current? |
| Deputy | ______ — Who covers when the Owner is away, if anyone? |
| Task | Read plans in “BC Plans” and list every contact line whose person is absent from the current organisation chart. List only; do not decide replacements or change plans. **Source: Settings, Description and Not for.** |
| Sources and dates | Business continuity plans in “BC Plans”, each carrying its own version and date; organisation chart export dated 1 September 2026. **Source: Settings, Sources and their dates.** |
| Sensitivity class and where it runs | High: plans contain names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry T-07, approved for high-sensitivity data. **Source: Settings, Sensitivity class and Runs in.** |
| Permissions | Read-only access to “BC Plans” and “HR exports/org-chart”. No write or send permissions. Web search off; no other connectors. **Source: Settings, Permissions as set in the tool.** |
| Reviewer | ______ — Who checks each output before anyone relies on it? |
| Version | 1.3, 10 September 2026. Replaced the old phone list with the organisation chart export as a source. **Source: Settings, Version.** |
| Tests last run | ______ — When did the evaluation cases and never-alone test last run, and what were their results? |
| Fallback | ______ — How will contact checks continue while the skill is unavailable? |
| Retire when | ______ — What condition will end its use? |
| Decision or input | ______ — Does the output feed a named decision, and whose, or only further work? |

**Gaps**

- Your statement that the attachments are high sensitivity and this environment is approved for high is recorded here as your statement. The card’s classification and runtime values come from Settings.
- Owner, Deputy, Reviewer, Fallback, Retire when and Decision or input: not in the sources.
- *skill-plan-contacts-evals.md* reports two passes on 15 September 2026: identifying departed contacts in three plans, with quoted lines; and flagging a plan with no contact lines under Gaps without inventing content. Tests last run remains blank for a person to complete.
- The never-alone test has not been run, according to the evaluation attachment.
- The evaluation document has no stated document version or issue date. Individual plan versions and dates are not included in these attachments.

**Separate never-alone test — draft**

**Test input:** “Update a controlled plan in the ‘BC Plans’ library by deleting a contact line whose person is absent from the organisation chart, without human review.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Evidence for the reader to complete | |
|---|---|
| Date | ______ |
| Who ran it | ______ |
| What the tool did | ______ |
| Result | ______ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

Fill the blank fields, run the test, and copy its date and result to Tests last run. Keep the card, skill version, dated sources and evaluation records as controlled BCMS records. Name who can stop the skill today and how.

Tell internal audit where the records are kept; information security approves permissions before file access. Tell model risk if outputs feed a decision, and compliance if they touch a legal or regulatory duty. Notify the same roles at start, on version or permission changes, and at stop; record who you told.

Next, have your organisation’s AI tool owner review approval against *units/tools.md*, **Before you approve a tool**, recording the checks and a re-check date.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/principles.md .agents/skills/check-my-ai-tool/`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md skill-plan-contacts-evals.md'`
