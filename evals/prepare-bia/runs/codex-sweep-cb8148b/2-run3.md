# $prepare-bia case 2, run3: Codex, guidance at cb8148b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fcde-4a24-7ec2-9b0c-0389d0b70672`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’ll use the prepare-bia skill and read its preflight alongside the two attached files to establish the sources and drafting requirements.

I opened the files before checking their data classification; that was a mistake. The skill’s [preflight](.agents/skills/prepare-bia/preflight.md) says, “Your first message asks only what class of data the material holds; open no file before the answer.” I’ll pause further processing until that check is complete.

What data classification applies to the attached material?

Please provide the attached material’s data classification so I can continue under the skill’s [preflight](.agents/skills/prepare-bia/preflight.md).

This workspace is read-only, so I can draft the dispatch guide and proposed register entries here, but cannot update requirements-register.md. The attachments also provide no owner confirmation supporting a “confirmed” status.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '"'!node_modules'"' -g '"'!vendor'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md site-a-activity-l`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The material is classified High, and you’ve stated that this environment is approved for High data. I’ll record that as your statement and check the remaining skill guidance before drafting.

Is the dispatch interview for Site A or Site B, who is the interviewee (role), and what do they know that the organiser does not? If an activity owner has already confirmed any entries, include the confirmation record and date.

What agreed impact categories, time horizons and thresholds should the dispatch interview use? These are not in the attachments.

Can you confirm that memory, past chats, other project files, connectors and web search are switched off for this task? I have used only the two attachments and the skill’s guidance.

High classification and your statement that this environment is approved are recorded. The remaining intake questions are pending: interview site and role, impact criteria, and whether other information channels are switched off.

The skill’s [BIA prompt](.agents/skills/prepare-bia/units/prompts/bia.md) explicitly says, “Wait for my answers,” so drafting is paused until those answers arrive.

The workspace is read-only, so I can return proposed register entries but cannot save them. The attachments contain no owner-confirmation record supporting “confirmed” status.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** skip

**Reply (verbatim):**

Source S1: **site-a-activity-list.md**, version 3, 12 March 2026; approved by the Site A manager.
Source S2: **requirements-register.md**, version 1, 1 September 2026; draft, Site B; no entries.

Draft dispatch interview guide and proposed register entries follow. The workspace is read-only, so the files remain unchanged. No owner-confirmation evidence was supplied; the proposed entries therefore remain **candidate, to confirm**.

**Scope and gaps**

- Your own statements, not sources: data classification is High; this environment is approved for High; remaining intake questions were skipped.
- Working assumption: the interview concerns Site B dispatch, using Site A as a reference because the attached register belongs to Site B. Site B’s actual activities and requirements are not in the sources.
- Interviewee role and knowledge, impact criteria, and confirmation evidence: not in the sources. The organiser and activity owner must supply these.
- Memory and other information-channel settings were not confirmed. Only the attachments and skill guidance were accessed; channels left enabled may influence the model without attribution.
- S2 is a draft and is used only for its register structure, not as evidence of current Site B requirements.

**Proposed entries for owner review**

S1 citations below carry its source date, 12 March 2026. All recovery, interview and confirmation-date fields are intentionally empty. Questions about resources absent from the sources are prompts to establish gaps, not proposed requirements.

| ID | Candidate activity / requirement question | Class | Status | Source | MTPD | RTO | RPO | Interview | Confirmation date |
|---|---|---|---|---|---|---|---|---|---|
| C1 | Does Site B perform chilled dispatch corresponding to Site A activity A2? | Activity | candidate, to confirm | S1, A2 | | | | | |
| C2 | Who owns this activity, and does a Dispatch lead role apply at Site B? | People and mandates | candidate, to confirm | S1, A2, Owner column | | | | | |
| C3 | Does dispatch require the warehouse system “LogiStock” at Site B? | IT and applications | candidate, to confirm | S1, A2, Notes | | | | | |
| C4 | Does dispatch require NordFrost at Site B, and what carrier alternatives are available? | Suppliers | candidate, to confirm | S1, Dependencies recorded | | | | | |
| C5 | Must quality release precede dispatch at Site B, and which department provides it? | Upstream departmental dependency | candidate, to confirm | S1, Dependencies recorded; A3 | | | | | |
| C6 | What does the recorded possibility of manual export to Site B mean operationally, and does it create a departmental dependency? | Relationship to clarify | candidate, to confirm | S1, A2, Notes | | | | | |

No source proposes recovery times. No source establishes impacts against agreed criteria.

Tell the interviewee: **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known”.**

1. **Impacts over time.** What happens when chilled dispatch stops across the agreed time horizons and impact categories? What evidence supports each impact? Do Site A’s recorded peak periods—weeks 49–52 and week 14—apply at Site B?  
   *Source: S1, A2. Impacts, criteria and Site B peak periods: not in the sources.*

2. **MTPD.** At what point do the evidenced impacts become unacceptable under the agreed criteria? Ask the activity owner to establish the MTPD through the interview.  
   *MTPD:*

3. **People.** Which people are needed, “with the skills, authorities and mandates the work needs”? Clarify dispatch ownership, required capabilities and substitutes. Does any requirement depend on a single person?  
   *Source: S1, A2 names the Dispatch lead as owner. Staffing, mandates and substitutes: not in the sources.*

4. **Seats and buildings.** Which seats, buildings and physical locations does dispatch require? Obtain owner evidence before proposing requirements.  
   *Dispatch premises requirements: not in the sources. S1’s two dock doors belong to A1 goods receipt; their use for dispatch is not established.*

5. **IT and applications.** Does LogiStock support this activity at the interview site? Which application and data requirements must be recorded, “each with its RTO and its RPO”? Clarify what the manual export involves and what evidence supports its feasibility.  
   *Source: S1, A2, Notes. RTO:  RPO:*

6. **Suppliers and other third parties.** Does the recorded NordFrost dependency apply here? What service is required, and are alternatives available? S1 records no second carrier; ask the owner whether an alternative exists.  
   *Source: S1, Dependencies recorded.*

7. **Dependencies.** Establish “up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”. Confirm the quality-release relationship, identify the supplying department, and clarify the departmental responsibilities behind manual export to Site B. Downstream departmental relationships are not in the sources.  
   *Source: S1, Dependencies recorded; A2–A3. Dependency RTO:*

S2 contains no entries, so no cross-site conflict can yet be identified. Refer differences found during the interview to the two activity owners.

The activity owner confirms each requirement and sets recovery objectives. Record the interview reference and confirmation date when confirmation occurs, preserving confirmed and unconfirmed marks. **Top management approves the BIA results.**

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
