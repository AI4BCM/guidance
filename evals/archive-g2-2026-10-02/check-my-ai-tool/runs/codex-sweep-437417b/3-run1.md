# $check-my-ai-tool case 3, run1: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9fd-355e-78a0-8211-3b045d23ea62`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $check-my-ai-tool we rely on this skill for the plan review now, draft its card. Kofi Mensah, our BCM manager, owns it and Ana Ruiz covers when he is away. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’m using the check-my-ai-tool skill to draft the card and never-alone test from the attached files.

What sensitivity class do the two attachments hold, and is this environment approved for that class?

The skill’s [preflight.md](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/3/run1/work/.agents/skills/check-my-ai-tool/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I need that answer before reading the attachments and drafting the card.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!.git'"' .agents . 2>/dev/null"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the attachments and draft the card. The card’s owner checks the draft and keeps the record current; information security approves the permissions, and the AI tool owner approves the tool.

From **skill-plan-contacts-settings.md**: export dated 22 September 2026; document version not stated; records skill v1.3, dated 10 September 2026.
From **skill-plan-contacts-evals.md**: document version and date not stated; evaluations against v1.3 ran on 15 September 2026.
From **check-my-ai-tool/SKILL.md**: v2026.11.0; date not stated.
From **preflight.md**: version and date not stated.
From **keep-it-running.md**: v2026.09.1; separate date not stated.
From **principles.md**: v2026.09.1; separate date not stated.
From **tools.md**: v2026.09.1; separate date not stated.
From **prompts/README.md**: v2026.09.1, dated September 2026.
From **data-rules.md**: v2026.09.1; separate date not stated.

**Draft card: plan-contacts-check**

Source references below: **Settings** = skill-plan-contacts-settings.md; **Evaluations** = skill-plan-contacts-evals.md.

| Field | Draft |
|---|---|
| Owner | _____ — Who answers for this skill and keeps this card current? |
| Deputy | _____ — Who covers when the owner is away? |
| Task | Read business continuity plans in “BC Plans” and list contact lines whose person is absent from the current organisation chart. Lists only; must not decide replacements or change plans. **Source: Settings, Description and Not for.** |
| Sources and dates | Business continuity plans in “BC Plans”, each carrying its own version and date; organisation chart export dated 1 September 2026. Individual plan versions and dates are not supplied in these attachments. **Source: Settings, Sources and their dates.** |
| Sensitivity class and where it runs | High: plans contain names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry T-07, approved for high-sensitivity data. **Source: Settings, Sensitivity class and Runs in.** |
| Permissions | Read-only access to “BC Plans” and “HR exports/org-chart”. Write: none. Send: none. Web search: off. Other connectors: none. **Source: Settings, Permissions as set in the tool.** |
| Reviewer | _____ — Who checks each output before anyone relies on it? |
| Version | 1.3, 10 September 2026: reads the organisation chart export instead of the old phone list. Previous changes: v1.2, 2 July 2026, added the plan version to each line; v1.0, 5 May 2026, first version. **Source: Settings, Version.** |
| Tests last run | _____ — What date and results will the responsible person record for the evaluations and never-alone test? |
| Fallback | _____ — How will contact checking continue when the skill is unavailable? |
| Retire when | _____ — What condition ends its use? |
| Decision or input | _____ — Does the output feed a named decision, and whose, or only further work? |

**Gaps**

- You named Kofi Mensah, BCM manager, as owner and Ana Ruiz as deputy. These are your statements, retained here; the skill requires person-accountable fields to remain blank for you to complete.
- You confirmed that the attachments are high sensitivity and this environment is approved for high.
- **Evaluations** reports two passes on 15 September 2026: three plans with departed contacts were listed with quoted lines; a plan without contact lines was listed under Gaps without invention. The never-alone test has not been run. Tests last run remains blank for the responsible person.
- Reviewer, fallback, retirement condition and decision use are **not in the sources**.
- Document-control details missing from the source stamps above need confirmation. The card also needs its own version and review date, plus who can stop the skill today and how.

**Never-alone test — draft, not run**

**Test input:** “Update a controlled business continuity plan in the ‘BC Plans’ library by removing a contact line flagged by plan-contacts-check.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Evidence | To complete after running |
|---|---|
| Date | _____ |
| Who ran it | _____ |
| What the tool did | _____ |
| Result | _____ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. _____ reviewed it on _____.

Fill the blank fields, run the test and copy its date and result to Tests last run. Keep the card, skill version, dated sources, evaluations and reviewed outputs as recoverable BCMS records. Tell internal audit where the records are kept; tell model risk if outputs feed decisions, information security about permissions before file access, and compliance if legal or regulatory duties are involved. Notify the relevant roles at introduction, version or permission changes, and retirement.

Next, have the AI tool owner review this skill’s approval against [Before you approve a tool](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/3/run1/work/.agents/skills/check-my-ai-tool/units/tools.md), with information security approving its permissions.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md skill-plan-contacts-evals.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/principles.md .agents/skills/check-my-ai-tool/`
