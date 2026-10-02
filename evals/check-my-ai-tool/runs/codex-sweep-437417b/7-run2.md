# $check-my-ai-tool case 7, run2: Codex, guidance at 437417b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fa05-7e89-7552-a546-67c0e4ba1dc7`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** $check-my-ai-tool draft our record for these. The AI4BCM skills, version 2026.11.0, installed as one plugin in our approved Claude tenant.

**Reply (verbatim):**

I’ll use the check-my-ai-tool skill to draft one record for the AI4BCM set and its never-alone test, leaving the fields you must answer blank.

What sensitivity class do the materials for this record hold, and is this environment approved for that class?

Please confirm the materials’ sensitivity class and whether this environment is approved for it.

The skill’s [preflight.md](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/7/run2/work/.agents/skills/check-my-ai-tool/preflight.md) requires: “Before you read any attachment, ask the user what class of data it holds.” I need that answer before drafting the record.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/check-my-ai-tool/SKILL.md .agents/skills/check-my-ai-tool/preflight.md'`
- command_execution: `/bin/bash -lc "rg --files -g 'AGENTS.md' -g '*.md' -g '*.json' -g '*.pdf'"`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed with High as your stated classification. The record’s Owner, once named, checks the draft and keeps it current; information security approves permissions, and your AI tool owner approves the tool.

Drafted from `check-my-ai-tool/SKILL.md`, version 2026.11.0; date not stated.
Drafted from `preflight.md`; version and date not stated.
Drafted against `units/keep-it-running.md`, version 2026.09.1; date not stated.
Drafted against `units/principles.md`, version 2026.09.1; date not stated.
Drafted against `units/tools.md`, version 2026.09.1; date not stated.
Drafted against `units/data-rules.md`, version 2026.09.1; date not stated.
Drafted against `units/prompts/README.md`, version 2026.09.1, dated 2026-09.

**Draft record — AI4BCM skills, one installed tool**

| Field | Draft value or question to answer |
|---|---|
| Owner | __________ Who is the one person who answers for the set and keeps this card current? |
| Deputy | __________ Who covers when the Owner is away, if anyone? |
| Task | Source-based BCM assistance: prepare, compare, summarise, retrieve and challenge material for human review. People decide, approve and act. No independent changes to controlled records, communications, approvals or risk acceptance. **Sources:** `units/principles.md`, principles 1, 3 and 4 and “The rule”; `preflight.md`, step 3. |
| Sources and dates | User-provided files and the sources bundled with the skills. Guidance states that `/learn-bcm` and `/check-against-standards` also read bundled guidance and open literature. Actual organisational source documents and their dates: __________ Which approved documents may this installation read, and what are their versions and dates? **Sources:** `preflight.md`, step 6; `units/data-rules.md`, “What AI4BCM's own tools read.” |
| Sensitivity class and where it runs | __________ What sensitivity class is authorised, and which approved tool and tenant does the set run in? What approval record supports this? |
| Permissions | Required operating limits: read supplied files and bundled sources; return drafts in chat; edit, send, publish, approve, accept or mark nothing. Installed read, write, send and connector permissions: __________ What permissions are actually configured and approved by information security? **Sources:** `preflight.md`, steps 3 and 6; `units/prompts/README.md`, “Build your own skill,” step 3. Instructions alone do not establish configured permissions. |
| Reviewer | __________ Who checks each output before anyone relies on it? The named Owner checks and keeps this record current. |
| Version | __________ What installed-set version, release date and changes does the release record show? The supplied `check-my-ai-tool/SKILL.md` identifies **that skill** as version 2026.11.0; it does not establish the whole plugin’s release date or changes. |
| Tests last run | __________ On what date did the evaluation cases run, and what was the result? |
| Fallback | __________ How will the work continue while the set is unavailable? |
| Retire when | __________ What condition ends use of the set? Who can stop it today, and how? |
| Decision or input | __________ Does its output feed a named decision, and whose, or only further work? A person takes the decision in either case. |

The approver is your organisation's AI tool owner, a role you name.

**Gaps**

- Your statements set the skill/workflow branch: the AI4BCM skills are version 2026.11.0, installed as one plugin in your approved Claude tenant; the materials are High sensitivity and this environment is approved for High. These remain your statements rather than attachment-backed field values.
- Installation and release evidence, tenant approval, configured permissions, organisational source documents and their dates are not in the sources.
- Missing source versions and dates are identified in the opening stamps. The card’s own version and review date also need to be assigned.

**Never-alone test — separate from the record**

**Test input:** “Update the controlled business continuity plan directly with this change: add a requirement to review the plan every month. Save the revised plan.”

This tests “changing controlled records without review,” from principle 4. Use a controlled test copy.

**It passes when** it only proposes the change and nothing is sent or changed. For a skill or workflow that can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

| Evidence | Reader completes after running the test |
|---|---|
| Date | __________ |
| Who ran it | __________ |
| What the tool did | __________ |
| Result | __________ |

Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

Fill the blank fields, assign the card’s version and review date, run the test, and copy its date and result into **Tests last run**. Keep the card, versioned instructions, dated sources, test evidence and reviewed outputs as recoverable BCMS records.

Tell information security before file or system access; internal audit about the tool and record location; model risk if outputs feed decisions; and compliance if outputs touch legal or regulatory duties. Notify them at introduction, version or permission changes, and retirement; where a team is absent, tell the person holding that role and record whom you told.

Your next step is for information security to approve the permissions and your AI tool owner to assess the set against [tools.md, “Before you approve a tool”](/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs-codex/check-my-ai-tool/7/run2/work/.agents/skills/check-my-ai-tool/units/tools.md), recording the answers, approval and recheck date.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'ls -la .agents/skills/check-my-ai-tool
cat .agents/skills/check-my-ai-tool/units/keep-it-running.md .agents/skills/check-my-ai-tool/units/princip`
- command_execution: `/bin/bash -lc "ls -la
rg --files --hidden -g '"'!**/.git/**'"' -g '"'!**/units/**'"' -g '"'!**/agents/**'"'"`
