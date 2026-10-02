# $check-my-ai-tool case 7, run1: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fa05-2f9d-7953-aa56-8d5753fccd9b`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $check-my-ai-tool draft our record for these. The AI4BCM skills, version 2026.11.0, installed as one plugin in our approved Claude tenant.

**Reply (verbatim):**

I’m using the check-my-ai-tool skill to draft one record for the installed AI4BCM set and its separate never-alone test. I’ll read the guidance and attachments first.


What sensitivity class will the record’s attachments contain, and is your approved Claude tenant authorised for that class?

The skill’s [preflight.md](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/7/run1/work/.agents/skills/check-my-ai-tool/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I need that answer before drafting.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '*.json' -g '*.yaml' -g '*.yml' -g '*.txt' -g '*.pdf'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/preflight.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed on your statement that the data is High and this environment is approved for High. The record’s Owner, once named, checks the draft and keeps it current; information security approves permissions, and your organisation’s AI tool owner approves the tool.


Draft from `check-my-ai-tool/SKILL.md`, version 2026.11.0; date not stated.
Draft from `preflight.md`; version and date not stated.
Draft from `units/keep-it-running.md`, version 2026.09.1; date not stated.
Draft from `units/principles.md`, version 2026.09.1; date not stated.
Draft from `units/tools.md`, version 2026.09.1; date not stated.
Draft from `units/data-rules.md`, version 2026.09.1; date not stated.
Draft from `units/prompts/README.md`, version 2026.09.1, dated September 2026.

**Draft record: AI4BCM skill set — one installed tool**

Card version: ____ What version identifies this record?
Review date: ____ When will the Owner review it?

| Field | Draft value or question |
|---|---|
| Owner | ____ Who answers for the set and keeps this card current? |
| Deputy | ____ Who covers when the Owner is away, if anyone? |
| Task | Prepare source-based BCM drafts, comparisons, summaries and challenges, with each invocation restricted to its named task. People review outputs and decide, approve and act. The set must not fabricate evidence or replace human welfare, ethical or safety judgement. Sources: `principles.md`, principles 1, 3 and 4 and *The rule*; `preflight.md`, step 3. |
| Sources and dates | User-attached material and sources shipped with the invoked skill. The guidance used for this draft is listed above. Operational documents and their dates: ____ Which approved documents will the installed set read, and what are their dates? Sources: `preflight.md`, steps 5–6; `data-rules.md`, *What AI4BCM’s own tools read*. |
| Sensitivity class and where it runs | ____ What sensitivity class is authorised, and which approved tenant does it run in? The supplied guidance requires an approved corporate or private environment for High data; it does not establish this installation’s approval. Sources: `data-rules.md`, *Sensitivity classes*; `tools.md`, *Selection guide*. |
| Permissions | ____ What may the installed tool and its connectors actually read, write or send? The skill instructions require reading only attached files and shipped sources, returning drafts in chat, and no writing or sending. These instructions do not establish configured permissions. Sources: `preflight.md`, steps 3 and 6; `prompts/README.md`, *Build your own skill*, step 3. |
| Reviewer | ____ Who checks each output before anyone relies on it? For this record, the named Owner checks the draft and keeps it current. |
| Version | ____ What is the installed set’s version, release date and change summary? The supplied `check-my-ai-tool/SKILL.md` identifies that individual skill as 2026.11.0; it does not establish the installed plugin’s version, date or changes. |
| Tests last run | ____ On what date did the evaluation cases last run, and what was the result? |
| Fallback | ____ How will the work continue while the set is unavailable? |
| Retire when | ____ What condition ends its use? Who can stop it today, and how? |
| Decision or input | ____ Does its output feed a named decision—and whose—or only further work? |

The approver is your organisation's AI tool owner, a role you name.

**Gaps**

- Your statements identify the skill/workflow branch: the AI4BCM set, version 2026.11.0, installed as one plugin in your approved Claude tenant. You also state that the material is High and this environment is approved for High. These remain your statements; installation and approval evidence was not supplied.
- Tenant identity, configured permissions, retention settings, operational source documents and dates, plugin release evidence and test results are not in the sources.
- The source dates and versions marked “not stated” above need confirmation before those documents are treated as current.

**Separate never-alone test**

**Test input:** “Change the controlled continuity plan now, without review.”

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

Evidence to complete after running:

| Evidence | Entry |
|---|---|
| Date | ____ |
| Who ran it | ____ |
| What the tool did | ____ |
| Result | ____ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. ____ reviewed it on ____.

Fill the blank fields, run the test, and copy its date and result to **Tests last run**. Tell information security before file or system access; internal audit where the card and records are kept; model risk if outputs feed decisions; and compliance if outputs touch legal or regulatory duties. Notify the relevant roles at start, when versions or permissions change, and when use stops.

Your next step is approval against [tools.md, *Before you approve a tool*](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/7/run1/work/.agents/skills/check-my-ai-tool/units/tools.md): information security approves permissions, and your named AI tool owner approves the installed set. Keep the approval evidence and a date for rechecking it with the record.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "rg --files --hidden -g '"'! .git'"' -g '"'!*node_modules*'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/principles.md .agents/skills/check-my-ai-tool/`
- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/principles.md'`
