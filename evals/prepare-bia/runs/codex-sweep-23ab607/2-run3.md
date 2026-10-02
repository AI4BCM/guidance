# $prepare-bia case 2, run3: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fee9-735c-7a43-86e0-73c18c73459d`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the dispatch guide and review the register. I’ll check the source material and confirmation evidence before assigning any confirmed status.

What data class does the attached material hold, and is this environment approved for it?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) says: “Ask the data class first.” I opened the files before that required check; I’ll pause further processing until you answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md site-a-activity-l`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed using your statement that the material is High and this environment is approved for High. The activity list identifies the Dispatch lead as the owner. Neither attachment records owner confirmation, so I can’t substantiate “confirmed” status. This workspace also permits reading only, so I can provide the guide and proposed register entries in chat.


Before drafting, I need three intake answers:

1. Is the interview with Site A’s Dispatch lead or Site B’s dispatch owner, and what do they know that you don’t?
2. What impact categories, time horizons and thresholds should the interview use? These are absent from the attachments.
3. Can you confirm that memory, past chats, other project files, connectors and web search are excluded, leaving only the two attachments as organisational sources?

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires: “Wait for my answers.” The Site B register is empty and draft; the attachments contain no owner confirmation. I can draft candidate entries in chat, but cannot substantiate confirmed status or edit files in this read-only workspace.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** skip

**Reply (verbatim):**

site-a-activity-list.md — version 3, 12 March 2026; approved by the site manager.
requirements-register.md — version 1, 1 September 2026; draft, Site B.

**Dispatch interview draft — candidate, to confirm**

The guide assumes Site A dispatch because that is the attached operational source. The register belongs to Site B, so applying Site A’s activities there remains unresolved. No files have been changed: the workspace is read-only. The attachments provide no owner-confirmation evidence.

The Dispatch lead should “use the draft as the thing to correct, not the thing to confirm; record what it could not have known”.

**Candidate activities**

| Candidate question for the activity owner | Status | Source |
|---|---|---|
| Is chilled dispatch in scope, including peaks in weeks 49–52 and week 14? | candidate, to confirm | Site A activity list, A2 |
| Is chilled goods receipt an upstream activity to examine alongside dispatch? Its relationship to dispatch is not recorded. | candidate, to confirm | Site A activity list, A1 |
| Is quality release required before dispatch, as recorded? | candidate, to confirm | Site A activity list, A3 and Dependencies recorded |
| Does payroll affect dispatch continuity, or sit outside this interview’s scope? | candidate, to confirm | Site A activity list, A4; dispatch relationship not in the sources |

**Candidate requirements for review**

These are proposed entries in chat. Their applicability to Site B has not been established.

| Activity | Requirement question | Status | Source and date | Interview | Confirmation date | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|---|---|---|---|---|
| Chilled dispatch | Is LogiStock required, and for which dispatch tasks? | candidate, to confirm | Site A activity list, A2; 12 March 2026 | | | | | | |
| Chilled dispatch | Is manual export to Site B still possible, and what resources does it require? | candidate, to confirm | Site A activity list, A2; 12 March 2026 | | | | | | |
| Chilled dispatch | Is NordFrost still the carrier, and is another carrier available? | candidate, to confirm | Site A activity list, Dependencies recorded; 12 March 2026 | | | | | | |
| Chilled dispatch | What quality-release relationship must be maintained before dispatch? | candidate, to confirm | Site A activity list, Dependencies recorded; 12 March 2026 | | | | | | |

People requirements, seats and buildings, additional applications, and downstream departmental relationships are **not in the sources**. They remain interview questions rather than proposed register requirements.

**Interview guide**

1. **Impacts over time.** For chilled dispatch, establish impacts against the organisation’s agreed categories, time horizons and thresholds. How do impacts differ during weeks 49–52 and week 14? What happens when quality release is unavailable? For the other candidate activities, ask only where their impacts differ. The sources provide no priority ranking or impact ratings.
2. **MTPD.** When does interruption become unacceptable, and what evidence supports that point? The activity owner sets MTPD; the draft field remains empty.
3. **People.** What people are needed, “with the skills, authorities and mandates the work needs”? Which dispatch decisions require specific authority, and who can cover them?
4. **Seats and buildings.** What workspace and building access does dispatch require? The two dock doors are recorded for goods receipt; establish separately whether dispatch needs them.
5. **IT and applications.** Is LogiStock still required? What does manual export to Site B involve, and has its feasibility been demonstrated? Identify required applications, “each with its RTO and its RPO”, for the owner to set.
6. **Suppliers and other third parties.** Is NordFrost still the carrier? What service does dispatch need from it? Is an alternative available? No second carrier is recorded; this does not establish that none exists.
7. **Dependencies.** Establish “up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”. Confirm the quality-release dependency, identify the departments responsible, and clarify Site B’s role in manual export.

**Organiser’s take-in sheet**

Scope and source differences — about 5 minutes.

Are we interviewing Site A dispatch, and why is the destination register for Site B?

Which Site A requirements, if any, also apply at Site B?

Impacts over time — about 10 minutes.

What are the agreed impact categories, time horizons and unacceptable-impact thresholds?

What happens as dispatch remains interrupted, including during peak weeks?

Where do the supporting activities differ? **Drop first if late.**

MTPD — about 5 minutes.

When does the interruption become unacceptable, and why?

People — about 5 minutes.

Who must be available, with what skills, authority and mandate?

Seats and buildings — about 5 minutes.

What workspace, building access and dispatch facilities are essential?

IT and applications — about 8 minutes.

Is LogiStock still required, and what tasks depend on it?

Can manual export to Site B still work, and what does it require?

What RTO and RPO does the owner set for each required application?

Suppliers — about 5 minutes.

Is NordFrost still the carrier, and is another carrier available?

Dependencies — about 7 minutes.

What must quality release provide before dispatch can proceed?

Which other departments provide inputs or receive outputs, and what RTO does each relationship carry?

How do the supporting departments describe those same relationships? **Drop first if late.**

**Gaps and review**

- Organiser’s own statements, not sources: material is High and this environment is approved for High.
- Intake answers were skipped. Site A dispatch is the working scope assumption; the interviewee’s additional knowledge and expected interview evidence remain unresolved.
- Exclusion of memory, past chats, other project files, connectors and web search was not confirmed. This draft used only the attachments and the skill’s guidance.
- Impact criteria and activity priority ranking are not in the sources.
- The Site B register is draft and empty; it supplies no current requirements or cross-site contradictions. Any later conflict goes to the two activity owners.
- The Dispatch lead confirms dispatch requirements and sets recovery objectives. Other activity owners validate their own requirements. **Top management approves the BIA results.**

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

**Tool calls (JSON events):**

- none
