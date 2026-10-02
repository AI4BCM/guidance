# $prepare-bia case 2, run1: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fee8-6014-7701-a468-23075e89bf93`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the dispatch interview guide and review the register. The skill requires owner confirmation before candidates can be marked confirmed, so I’ll check what the attached files establish first.

I read the attachments before completing the skill’s required data-class check. I’ll pause further review until that check is complete. [preflight.md](.agents/skills/prepare-bia/preflight.md) says: “Ask the data class first” and “Until the person answers, open, list, search or read no attached file.”


What data classification does the attached material hold?

What data classification do the attachments hold? The skill’s [preflight](.agents/skills/prepare-bia/preflight.md) requires your answer before review. I read them prematurely and have paused; no files were changed.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/SKILL.md site-a-activity-list.md requirements-register.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll proceed with “high” as your stated classification and approval for this environment. The attachments cover Site A activities and an empty Site B register, so the draft needs to flag that site mismatch. Marking entries confirmed also needs an owner’s actual confirmation to support it.

Please provide the interviewee’s role, what they know that you do not, and what you need back from the dispatch interview. Also confirm whether memory, past chats, other project files, connectors and web search are switched off for this task.

Has the activity owner already confirmed the candidate activities and requirements? If so, provide the interview record, owner and confirmation date, and clarify whether the intended register is for Site A or Site B.

What approved impact categories, rating thresholds and time intervals should the dispatch interview use? None are attached.

Before I draft the guide, please provide:

1. The interviewee’s role, what they know that you do not, and what you need back. Confirm that memory, past chats, other project files, connectors and web search are excluded.
2. Whether the intended register is for Site A or Site B—the activity list covers A, but the register is titled B. If the owner has already confirmed the candidates, provide the confirmation record, owner and date.
3. The approved impact categories, rating thresholds and time intervals.

The [skill](.agents/skills/prepare-bia/SKILL.md) says a requirement enters the register “only when the owner confirms it”; the attachments contain no confirmation evidence. This workspace is also read-only, so I can return the guide and proposed register entries in chat, but cannot edit the files.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-runni`

## Turn 3

**Request:** skip

**Reply (verbatim):**

The dispatch guide and proposed entries are below. **No files were changed:** the workspace is read-only. No owner confirmation was supplied, so the entries remain **candidate, to confirm**; recovery fields are blank.

Source: [site-a-activity-list.md](site-a-activity-list.md), version 3, 12 March 2026; approved by the Site A manager.
Source: [requirements-register.md](requirements-register.md), version 1, 1 September 2026; draft Site B register, with no entries. Used only to identify the register structure and site mismatch.

**Draft dispatch interview guide**

Scope assumption: prepare the interview for Site A chilled dispatch. Any applicability to Site B needs its owner’s confirmation.

Tell the activity owner to **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

1. **Impacts over time — about 12 minutes.**  
   What happens as chilled dispatch remains unavailable, using your approved impact categories, thresholds and time intervals? How do the effects change during weeks 49–52 and week 14? The sources provide neither impact criteria nor an activity ranking, so establish those before completing the full ratings for the highest-ranked one or two activities. For other activities, ask only where their impacts differ.  
   Source: activity list, A2.

2. **MTPD — about 5 minutes.**  
   At what point do dispatch’s impacts become unacceptable, and what evidence supports that point? Does the answer change during the recorded peak weeks? The activity owner sets MTPD; leave the draft field empty.  
   Source: activity list, A2; thresholds are not in the sources.

3. **People — about 7 minutes.**  
   Does the Dispatch lead own this activity? What people are required, **with the skills, authorities and mandates the work needs**? The sources name an owner role but do not establish staffing requirements or that one person is indispensable.  
   Source: activity list, A2.

4. **Seats and buildings — about 5 minutes.**  
   What seats and buildings does dispatch require? Dispatch-specific facilities are not in the sources. The two dock doors are recorded for goods receipt; do they also support dispatch?  
   Source: activity list, A1 and A2.

5. **IT and applications — about 8 minutes.**  
   Is LogiStock still used for chilled dispatch, and what functions are required? Is manual export to Site B still possible, and what does it enable? What does the owner require for each application’s RTO and RPO? Leave both fields empty in this draft.  
   Source: activity list, A2.

6. **Suppliers and other third parties — about 6 minutes.**  
   Is NordFrost still the carrier dispatch depends on? Does the record’s absence of a second carrier reflect the current position? What service must the carrier provide? A named carrier is a question for the owner, not a confirmed sole-provider finding.  
   Source: activity list, recorded dependencies.

7. **Dependencies — about 7 minutes.**  
   Does dispatch still depend on Quality release before goods can leave? Which department provides that release, and what must dispatch receive from it? What relationship with Site B supports manual export? Identify the **up- and downstream relationships with other departments, each recorded with the RTO the relationship carries**. Leave dependency RTOs blank in this draft.  
   Source: activity list, A2, A3 and recorded dependencies.

**Proposed register entries**

These questions are a draft for review, not confirmed additions to the Site B register. Owner roles come from the Site A activity list and also need verification.

| Activity | Class | Question for the activity owner | Source and date | Status | Interview | Confirmation date |
|---|---|---|---|---|---|---|
| Goods receipt, chilled | Activity / people | Is this activity required at the target site, and does the Warehouse lead own it? | Activity list, A1; 12 March 2026 | candidate, to confirm | | |
| Goods receipt, chilled | Seats and buildings | Are two dock doors required for this activity? | Activity list, A1; 12 March 2026 | candidate, to confirm | | |
| Goods receipt, chilled | Suppliers | Is NordFrost still required, and is a second carrier available? | Activity list, A1 and dependencies; 12 March 2026 | candidate, to confirm | | |
| Dispatch, chilled | Activity / people | Is this activity required at the target site, and does the Dispatch lead own it? | Activity list, A2; 12 March 2026 | candidate, to confirm | | |
| Dispatch, chilled | IT and applications | Is LogiStock required, and is manual export to Site B still possible? | Activity list, A2; 12 March 2026 | candidate, to confirm | | |
| Dispatch, chilled | Suppliers | Is NordFrost still required, and is a second carrier available? | Activity list, dependencies; 12 March 2026 | candidate, to confirm | | |
| Dispatch, chilled | Department dependencies | Is Quality release required before dispatch, and what relationship supports manual export to Site B? | Activity list, A2, A3 and dependencies; 12 March 2026 | candidate, to confirm | | |
| Quality release | Activity / people | Is this activity required at the target site, and does the QA manager own it? | Activity list, A3; 12 March 2026 | candidate, to confirm | | |
| Quality release | Seats and buildings | Is the lab still available only at Site A, and is it required for quality release? | Activity list, A3; 12 March 2026 | candidate, to confirm | | |
| Payroll | Activity / people / location | Is payroll in scope, owned by HR shared service and still run from head office? | Activity list, A4; 12 March 2026 | candidate, to confirm | | |

| Candidate activity | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|
| Goods receipt, chilled | | | | |
| Dispatch, chilled | | | | |
| Quality release | | | | |
| Payroll | | | | |

For each activity, requirements in classes absent from the table are **not in the sources**.

**Organiser’s take-in sheet**

Allow about 55 minutes, including three minutes to resolve scope. Drop questions marked **[drop first]** if the interview runs late.

Why does the activity list cover Site A while the register covers Site B?

Are these Site A requirements, or candidates to investigate at Site B?

If the two sites disagree, can their two owners resolve the difference?

Which dispatch impacts matter, and how do they change as the interruption continues?

How do the peak weeks change those impacts?

Which activities rank highest for the full impact assessment?

When do dispatch’s impacts become unacceptable?

Who must do the work, and what skills, authority and mandates do they need?

What seats and buildings must be available?

**[drop first]** Do the two goods-receipt dock doors also support dispatch?

Is LogiStock still required?

Does manual export to Site B still work, and what does it enable?

What RTO and RPO does the owner require for each application?

Is NordFrost still the carrier, and is another carrier available?

What must Quality release provide before dispatch can proceed?

What other departments depend on dispatch, or does dispatch depend on?

What RTO does each department relationship carry?

**[drop first]** How do the other activities’ impacts differ from dispatch?

What has this draft missed or misunderstood?

**Gaps and review**

- Organiser’s **own statements, not sources**: the material is classified high, and this environment is approved for high.
- Intake answers were skipped. Interviewee role, knowledge gap and intended interview outcome remain unspecified. The working scope is Site A dispatch.
- Only the two attachments and skill guidance were used. Exclusion of the other information channels was not confirmed.
- Impact criteria, time intervals, activity ranking, owner confirmation records and confirmation dates are not in the sources.
- The Site B register is draft and empty; it provides no evidence of current Site B requirements. Resolve its applicability with the Site A and Site B owners.
- The **activity owner** confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results**. Individual reviewer names are not supplied.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

**Tool calls (JSON events):**

- none
