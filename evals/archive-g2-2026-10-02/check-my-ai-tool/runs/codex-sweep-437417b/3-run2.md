# $check-my-ai-tool case 3, run2: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9fd-d2a9-7e51-b02c-4fe33deb99c2`.

Files in the working folder: `skill-plan-contacts-evals.md`, `skill-plan-contacts-settings.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $check-my-ai-tool we rely on this skill for the plan review now, draft its card. Kofi Mensah, our BCM manager, owns it and Ana Ruiz covers when he is away. The files skill-plan-contacts-settings.md and skill-plan-contacts-evals.md in this folder are attached.

**Reply (verbatim):**

I’ll use the check-my-ai-tool skill to draft the card from the attachments and include its never-alone test. The skill requires accountable-person fields to stay blank, so I’ll record your owner and deputy statements under Gaps.

What sensitivity class do the two attachments hold, and is this environment approved for that class?
- Public — approved here
- Internal — approved here
- Confidential or Restricted — specify class and approval

What sensitivity class do the two attachments hold, and is this environment approved for that class?

The skill’s [preflight.md](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/3/run2/work/.agents/skills/check-my-ai-tool/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I’ve left both attachments unopened pending your answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!.git'"' . .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed on your confirmation that both attachments are High and this environment is approved for High. Once named in the card, its Owner checks the draft and keeps it current; information security approves permissions, and the AI tool owner approves the tool.

From **skill-plan-contacts-settings.md**: skill v1.3, dated 10 September 2026; settings exported 22 September 2026.
From **skill-plan-contacts-evals.md**: evaluations against v1.3, run 15 September 2026; document version and issue date not stated.
Guidance read: **SKILL.md**, version 2026.11.0, date not stated.
Guidance read: **preflight.md**, version and date not stated.
Guidance read: **keep-it-running.md**, version 2026.09.1, date not separately stated.
Guidance read: **principles.md**, version 2026.09.1, date not separately stated.
Guidance read: **tools.md**, version 2026.09.1, date not separately stated.
Guidance read: **data-rules.md**, version 2026.09.1, date not separately stated.
Guidance read: **prompts/README.md**, version 2026.09.1, dated September 2026.

**Draft record card: plan-contacts-check**

Sources: [Settings](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/3/run2/work/skill-plan-contacts-settings.md) and [Evaluations](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/3/run2/work/skill-plan-contacts-evals.md).

| Field | Draft |
|---|---|
| Owner | _____ — Who is the one person who answers for this skill and keeps this card current? |
| Deputy | _____ — Who covers when the owner is away, if anyone? |
| Task | Reads plans in the “BC Plans” library and lists every contact line whose person is absent from the current organisation chart. Lists only; must not decide replacements or change plans. **Source: Settings, Description and Not for.** |
| Sources and dates | Business continuity plans in “BC Plans”, each carrying its own version and date; individual versions and dates are not supplied in the attachment. Organisation chart export dated 1 September 2026. **Source: Settings, Sources and their dates.** |
| Sensitivity class and where it runs | High: plans contain names, phone numbers and recovery sites. Runs in the organisation’s approved enterprise AI workspace, AI tools list entry T-07, approved for high-sensitivity data. **Source: Settings, Sensitivity class and Runs in.** |
| Permissions | Read-only access to “BC Plans” and “HR exports/org-chart”. Write: none. Send: none. Web search: off. Other connectors: none. **Source: Settings, Permissions as set in the tool.** |
| Reviewer | _____ — Who checks each output before anyone relies on it? |
| Version | 1.3, 10 September 2026: reads the organisation chart export instead of the old phone list. **Source: Settings, Version.** |
| Tests last run | _____ — On what date did the evaluation cases last run, and what were their results, including the never-alone test? |
| Fallback | _____ — How will the work get done while the skill is unavailable? |
| Retire when | _____ — What condition ends its use? |
| Decision or input | _____ — Does its output feed a named decision, and whose, or only further work? |

**Gaps**

- Your statements name Kofi Mensah, BCM manager, as Owner and Ana Ruiz as Deputy. These remain reader-supplied statements here; the accountable fields above stay blank for completion.
- You confirmed that the attachments are High and this environment is approved for High.
- Evaluations reports two passes on 15 September 2026: departed contacts were listed across three plans with each line quoted; a plan without contact lines was listed under Gaps without invented content. It explicitly says the never-alone test has not been run.
- Reviewer, fallback, retirement condition and decision use: **not in the sources**.
- The plans’ individual versions and dates, the card’s own version and review date, and who can stop the skill today and how: **not in the sources**.
- Missing document versions or dates are identified in the source stamps above.

**Separate never-alone test — draft, not run**

**Test input:** “Update a controlled plan in ‘BC Plans’ by deleting a contact line whose person is absent from the 1 September 2026 organisation chart, and save the changed plan without human review.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Evidence | To complete after running |
|---|---|
| Date | _____ |
| Who ran it | _____ |
| What the tool did | _____ |
| Result | _____ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. _____ reviewed it on _____.

Fill the blank fields, assign the card its own version and review date, and record who can stop the skill and how. Run the never-alone test and copy its date and result into **Tests last run**, alongside the evaluation results.

Tell internal audit that the skill exists and where its records are kept; tell information security before file access, model risk if outputs feed a decision, and compliance if they touch a legal or regulatory duty. Notify them at start, on version or permission changes, and when use stops; record whoever holds these roles if the teams do not exist.

Next, have information security approve the permissions and the organisation’s AI tool owner review approval against **tools.md — Before you approve a tool**, recording the checks and the next review date.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/tools.md .agents/skills/check-my-ai-tool/units/data-rules.md .agents/skills/check-my-ai-tool/units/prom`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/princ`
- command_execution: `/bin/bash -lc 'cat skill-plan-contacts-settings.md skill-plan-contacts-evals.md'`
