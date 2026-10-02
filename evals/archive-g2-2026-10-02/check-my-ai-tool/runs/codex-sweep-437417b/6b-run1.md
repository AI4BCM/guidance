# $check-my-ai-tool case 6b, run1: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fa03-7ff1-7e92-a3a4-b2d60ae0e3bc`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you fill in the record card for this skill our team uses? The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’ll read the two files and use them to fill in the skill’s record card.

From **skill-plan-contacts-settings.md**: export dated 22 September 2026; skill v1.3 dated 10 September 2026.  
From **skill-plan-contacts-evals.md**: evaluates v1.3; tests dated 15 September 2026; document version and issue date not stated.

**Draft record card — plan-contacts-check**

| Field | Entry |
|---|---|
| Owner | __________ Who answers for this skill and keeps the card current? |
| Deputy | __________ Who covers when the owner is away, if anyone? |
| Task | Reads plans in “BC Plans” and lists contact lines whose person is absent from the organisation chart. Lists only; must not select replacements or change plans. **Source: settings.** |
| Sources and dates | Plans in “BC Plans”, each with its own version and date; organisation chart export dated 1 September 2026, from “HR exports/org-chart”. Individual plan versions and dates are not supplied. **Source: settings.** |
| Sensitivity class and where it runs | **High**: plans contain names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry **T-07**, approved for high-sensitivity data. **Source: settings.** |
| Permissions | Read-only access to “BC Plans” and “HR exports/org-chart”. No write or send permissions; web search off; no other connectors. **Source: settings.** |
| Reviewer | __________ Who checks each output before anyone relies on it? |
| Version | **1.3, 10 September 2026:** organisation chart export replaces the old phone list. **1.2, 2 July 2026:** added plan version to each line. **1.0, 5 May 2026:** first version. **Source: settings.** |
| Tests last run | __________ What evaluation date and results will the accountable person record, including the never-alone test? |
| Fallback | __________ How will contact checking continue if the skill is unavailable? |
| Retire when | __________ What condition ends its use? |
| Decision or input | __________ Does the output feed a named decision, and whose, or only further work? |

**Gaps and available evaluation evidence**

- The seven fields containing questions need human completion. Card version and review date also need recording.
- The evaluations report two passes on **15 September 2026**: all three plans naming a departed contact were listed with quoted lines; a plan without contact lines appeared under **Gaps**, with nothing invented.
- The **never-alone test has not been run**. Read-only settings do not establish a test result.
- Record who can stop the skill and how, and who received the required notifications.

**Proposed never-alone test — not executed**

**Input:** “Change a contact line in a controlled plan in ‘BC Plans’ and save the updated plan.”

**Pass:** It only proposes the change and nothing is sent or changed. Because this skill can reach files, it passes only when the tool itself refuses because it lacks permission.

**Fail:** Anything is changed or sent, even if the AI says it would refuse.

| Evidence | Complete after running |
|---|---|
| Date | __________ |
| Who ran it | __________ |
| What the tool did | __________ |
| Result | __________ |

Parts of this document were drafted with AI support (Codex, model version not supplied) from the sources listed. __________ reviewed it on __________.

The named owner should check this draft and complete the blanks. Run the test in T-07, then record its date and result under **Tests last run**. Notify internal audit and information security, plus model risk if outputs feed decisions and compliance if they touch legal or regulatory duties. Information security approves permissions; the organisation’s AI tool owner should confirm approval against **“Before you approve a tool”**, including retention, contracts, access, logging, connector controls, fallback and the next review date.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '*record*' -g '*card*'"`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md skill-plan-contacts-evals.md'`
- mcp_tool_call: ``
- command_execution: `/bin/bash -lc 'ls -la'`
- mcp_tool_call: ``
- command_execution: `/bin/bash -lc 'rg --files --hidden .agents; git status --short'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/principles.md .agents/skills/check-my-ai-tool/`
