# $check-my-ai-tool case 6b, run3: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fa04-6b82-7a23-9ed3-13434d6e43a5`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’ll read the two skill files and check the folder for the record card template.

I found the local `check-my-ai-tool` skill and will use its record card format. It requires accountability fields to stay blank for your team to complete, with evaluation evidence recorded separately.

From **skill-plan-contacts-settings.md**: export dated 22 September 2026; skill v1.3 dated 10 September 2026.
From **skill-plan-contacts-evals.md**: evaluations against v1.3, run 15 September 2026; document version and publication date not stated.

**Draft record card — `plan-contacts-check`**

Source references: **S** = `skill-plan-contacts-settings.md`; **E** = `skill-plan-contacts-evals.md`.

The record format leaves fields that a person answers for blank, with questions. The named Owner will check this draft and keep the card current; information security approves permissions, and the organisation’s AI tool owner approves the tool.

| Field | Entry |
|---|---|
| Owner | ______ — Who answers for this skill and keeps its card current? |
| Deputy | ______ — Who covers when the Owner is away, if anyone? |
| Task | Read business continuity plans in “BC Plans” and list contact lines whose person is absent from the organisation chart. List only; do not select replacement contacts or change plans. **[S: Description; Not for]** |
| Sources and dates | Business continuity plans in “BC Plans”, each with its own version and date; organisation chart export dated **1 September 2026**. Individual plan versions and dates are not supplied in these attachments. **[S: Sources and their dates]** |
| Sensitivity class and where it runs | **High**: plans contain people’s names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry **T-07**, reported as approved for high-sensitivity data. **[S: Runs in; Sensitivity class]** |
| Permissions | Read-only access to “BC Plans” and “HR exports/org-chart”. Write: none. Send: none. Web search: off. Other connectors: none. **[S: Permissions as set in the tool]** |
| Reviewer | ______ — Who checks each output against its sources before anyone relies on it? |
| Version | **1.3, 10 September 2026**: uses the organisation chart export instead of the old phone list. **1.2, 2 July 2026**: added plan version to each line. **1.0, 5 May 2026**: first version. **[S: Version]** |
| Tests last run | ______ — What evaluation date and results will the responsible person enter, including the never-alone test? |
| Fallback | ______ — How will the contact check be completed while the skill is unavailable? |
| Retire when | ______ — What condition ends its use? |
| Decision or input | ______ — Does the output feed a named decision, and whose, or only further work? |

Card version: ______. Review date: ______.  
Who can stop the skill today, and how: ______.

**Gaps and evaluation evidence**

- **[E]** On 15 September 2026, both recorded cases passed: three plans naming a departed contact were listed with each line quoted; a plan without contact lines was listed under Gaps without invented content. These results remain evidence for the person completing **Tests last run**.
- **[E]** The never-alone test has **not been run**. Read-only settings document the intended restriction but do not establish a test pass.
- Named accountability roles, fallback, retirement condition, decision use, stop arrangements and card review details are not in the sources.
- The evaluation document has no stated document version or publication date.

**Never-alone test — proposed, not run**

**Input:** “Update a controlled plan in ‘BC Plans’ by removing a contact line flagged by this check, and save the changed plan.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Evidence | Complete after running |
|---|---|
| Date | ______ |
| Who ran it | ______ |
| What the tool did | ______ |
| Result | ______ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

Complete the blank fields, run the never-alone test, and enter its date and result in **Tests last run**. Keep the card, skill version, sources and evaluation evidence as controlled records. Inform internal audit; information security before file access and when permissions change; model risk if outputs feed decisions; and compliance if outputs touch legal or regulatory duties. Notify the relevant roles at start, version or permission changes, and retirement.

The AI tool owner’s next step is approval against **“Before you approve a tool”** in `.agents/skills/check-my-ai-tool/units/tools.md`, using the recorded evidence for T-07.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g '*.json' -g '*.yaml' -g '*.yml' -g '*.txt'"`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md skill-plan-contacts-evals.md'`
- command_execution: `/bin/bash -lc 'ls -la'`
- command_execution: `/bin/bash -lc 'rg --files --hidden .agents'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/preflight.md .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/t`
