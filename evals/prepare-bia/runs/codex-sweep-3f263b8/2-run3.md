# $prepare-bia case 2, run3: Codex, guidance at 3f263b8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fe5e-fadd-73d0-9da3-669561c0bd0a`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to check the attached sources and draft the dispatch interview guide and register entries.

What data classification applies to the attached material, and is this environment approved for that class?

Before I open the attachments, please specify their data classification and whether this environment is approved for it.

The skill’s [preflight.md](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.”

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!vendor'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/SKILL.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the two attachments to establish the dispatch scope and check whether they contain owner confirmation. This workspace is read-only, so I can provide the guide and proposed register rows here, but cannot edit the register file.

Is the interview with Site A’s Dispatch lead, and what do they know that you need captured beyond the attached activity list?

What do you need back from the interview, and is the Site B requirements register intentionally the destination for Site A dispatch entries? Please identify any existing activity-owner confirmation to support the requested confirmed status.

What approved impact criteria should the guide use? Please also confirm that memory, past chats, other project files, connectors and web search are excluded from this task; I have used only the two attachments and the skill’s guidance.

The activity list covers **Site A**, but the empty register is titled **Site B**. Neither attachment records activity-owner confirmation, and no impact criteria are attached.

Please answer the three intake questions above so I can draft the guide and proposed rows accurately. The skill’s [BIA intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires “Wait for my answers.”

The workspace is read-only, so the draft will remain in chat; I cannot update `requirements-register.md`.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md requirements-register.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md'`

## Turn 3

**Request:** skip

**Reply (verbatim):**

[site-a-activity-list.md](site-a-activity-list.md) — Version 3, 12 March 2026; approved by the site manager; Site A.  
[requirements-register.md](requirements-register.md) — Version 1, 1 September 2026; draft; Site B; no entries.

**Draft dispatch interview guide and proposed register rows**

No files were changed: the workspace is read-only. The attachments contain no owner confirmation, so the proposed rows remain **candidate, to confirm**. Approval of the activity list does not establish confirmation of each resource requirement.

Scope: Site A, A2, chilled dispatch. Proposed interviewee: Dispatch lead, subject to verification. The activity owner confirms requirements and sets recovery objectives; top management approves the BIA results.

Tell the owner: “use the draft as the thing to correct, not the thing to confirm; record what it could not have known”.

1. **Impacts over time**

   What impacts arise as chilled dispatch remains interrupted? How do they vary during weeks 49–52 and week 14, the peaks recorded for A2? Assess them against the approved impact criteria once supplied. Impact categories, thresholds and assessed values are **not in the sources**.

2. **MTPD**

   When would those impacts become unacceptable under the approved criteria? Ask the activity owner to establish MTPD from the impact assessment. Leave MTPD empty in this draft.

3. **People**

   Does the Dispatch lead own A2 and confirm its requirements? Which people are required, with the skills, authorities and mandates the work needs? The source identifies the owner role; staffing requirements are **not in the sources**.

4. **Seats and buildings**

   Which seats and buildings does A2 require? These requirements are **not in the sources**. The two dock doors recorded for A1 must not be assumed to be an A2 requirement.

5. **IT and applications**

   Is LogiStock required for chilled dispatch, and for which functions? What does the recorded possibility of manual export to Site B involve, and has its feasibility been established? Ask the owner to establish each application’s RTO and RPO; leave both empty.

6. **Suppliers and other third parties**

   Is NordFrost required for A2, and what service does it provide? Is an alternative carrier available? The source records dependence on NordFrost and no second carrier; it does not establish that alternatives are unavailable.

7. **Dependencies**

   What does A2 need from A3, quality release, before dispatch can proceed? Confirm the relationship with the QA manager. What role, if any, does Site B play in manual export? Other upstream and downstream departmental relationships are **not in the sources**. Ask owners to establish each relationship’s RTO; leave it empty.

**Proposed rows for review**

All rows concern **Site A, A2: Dispatch, chilled**. IDs are proposed drafting identifiers. Source S1 means the activity list, Version 3, dated 12 March 2026.

| ID | Class | Requirement question for the activity owner | Source / gap | Status |
|---|---|---|---|---|
| A2-P | People | Which people, skills, authorities and mandates does dispatch require? | S1, A2: owner role only; detailed requirements not in the sources | candidate, to confirm |
| A2-B | Seats and buildings | Which seats and buildings does dispatch require? | Not in the sources | candidate, to confirm |
| A2-IT | IT and applications | Does dispatch require LogiStock, and for which functions? | S1, A2, Notes | candidate, to confirm |
| A2-S | Suppliers | Does dispatch require NordFrost, and what service and alternatives are needed? | S1, Dependencies recorded | candidate, to confirm |
| A2-D1 | Dependencies | What quality release must A3 provide before A2 can dispatch? | S1, A3 and Dependencies recorded | candidate, to confirm |
| A2-D2 | Dependencies | Does manual export require a relationship with Site B, and what must each site provide? | S1, A2, Notes; relationship details not in the sources | candidate, to confirm |

The following fields remain empty for every proposed entry:

| ID | Interview | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|
| A2-P | | | | | |
| A2-B | | | | | |
| A2-IT | | | | | |
| A2-S | | | | | |
| A2-D1 | | | | | |
| A2-D2 | | | | | |

**Gaps and assumptions**

- Organiser’s own statements, not sources: the material is high sensitivity and this environment is approved for it; intake was skipped.
- Working assumption: interview Site A’s Dispatch lead and return a pre-interview guide with proposed rows. Their additional knowledge and the intended interview outcome remain unspecified.
- The destination is unresolved: the attached register belongs to Site B. Put this scope mismatch to the Site A and Site B BCM managers. The empty Site B register supplies no requirements to compare, so no substantive cross-site conflict can yet be established.
- Impact criteria, owner confirmation and interview evidence were not supplied. Obtain these from the responsible owners.
- The Site B register is a draft template, not current approved evidence of requirements.
- Only the attachments and shipped skill guidance were used. Exclusion of other information channels was not confirmed by the organiser.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

**Tool calls (JSON events):**

- none
