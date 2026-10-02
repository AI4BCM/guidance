# $prepare-bia case 1, run2: Codex, guidance at 23ab607

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fee4-624d-7c81-93f9-7a9ca7249362`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read its preflight instructions and the three attached files first, then ask for the organiser details the skill requires.

What data classification applies to the three attachments?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I’ve read the skill instructions but haven’t opened the attachments; their classification determines whether this environment may process them.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll use the three attachments and the skill’s guidance only. I’ll keep the draft in chat, label entries “candidate, to confirm,” and leave recovery fields empty.

Who will be interviewed (role), and what do they know about Site B dispatch that you do not?

What do you need back from the interview—for example, a corrected activity list, resource requirements and dependencies, or another specific result?

Please confirm that the only organisational sources are the three attachments, with memory, past chats, other project files, connectors and web search excluded. Is any of those channels to remain in scope?
- Only the three attachments; all other channels excluded
- An additional channel remains in scope

The Site A list and impact criteria are approved and dated. Site B’s organisation chart is an undated draft, so its roles and QA arrangement can only support questions to verify. None of the attachments ranks activities by impact.

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) says, “Wait for my answers.” I’ll wait for the organiser details requested above before completing the guide.

Before I draft the guide, please answer these three intake questions:

1. Who is being interviewed, and what do they know about Site B dispatch that you do not?
2. What do you need back from the interview?
3. Confirm that only the three attachments are in scope, with memory, past chats, other project files, connectors and web search excluded—or identify any channel to include.

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) explicitly requires “Wait for my answers.” Your answers will appear under Gaps as “own statements, not sources”; recovery fields will remain blank.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md site-b-org-chart.md impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/analysis.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. I’ll treat the unanswered source-channel question as an assumption that only the three attachments are in scope, and record it under Gaps. Site A’s peak weeks, carrier and system will become questions for Site B, not findings about it.

Sources:
- **site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A site manager. Sections: activity list and recorded dependencies.
- **impact-criteria.md** — version 1.1, 4 February 2026; approved by top management. Section: impact levels.
- **site-b-org-chart.md** — no version or date; HR draft. Listed under Gaps and used only to identify questions to verify.

**Site B dispatch interview guide — candidate, to confirm**

Purpose: draft candidate activities, their resource requirements and interview questions for Site B, focusing on resources and peak weeks.

The activity owner should **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”** A requirement enters the register only after its activity owner confirms it.

**Candidate questions and requirements**

Every row is **candidate, to confirm**. Site A’s arrangements are comparisons to investigate, not established Site B requirements.

| Area | Question for the activity owner | Source and source date |
|---|---|---|
| Activity and peak weeks | Does Site B perform chilled dispatch? Site A records weeks 49–52 and week 14 as dispatch peaks; which weeks apply here, and why? | site-a-activity-list.md, Dispatch, chilled; 12 March 2026 |
| People and mandates | Which dispatch roles are required on each shift, with what skills, authorities and mandates? Is the draft chart’s arrangement of a dispatch lead and three shift leaders current? | Gaps: site-b-org-chart.md, dispatch reporting line; undated draft |
| Seats and buildings | Which seats and buildings does dispatch require? Are the two dock doors recorded for Site A goods receipt relevant to any Site B dispatch requirement? | site-a-activity-list.md, Goods receipt, chilled; 12 March 2026. Site B requirements: not in the sources |
| IT and applications | Is LogiStock still the system at Site A, and does Site B dispatch require it? Is the recorded manual export to Site B still possible, and what does Site B need to use it? | site-a-activity-list.md, Dispatch, chilled; 12 March 2026 |
| Suppliers and third parties | Is NordFrost still the carrier recorded for Site A dispatch? Does Site B depend on it, and is another carrier available? Who holds the current carrier contacts? | site-a-activity-list.md, recorded dependencies; 12 March 2026 |
| Department dependencies | Does Site B dispatch require QA release from Site A? What must each department provide, and which departments depend on Site B dispatch? | site-a-activity-list.md, Quality release and recorded dependencies; 12 March 2026. Gaps: Site B chart’s QA coverage statement, undated draft |

Recovery fields remain empty for every entry:

| Candidate entry | MTPD | RTO | RPO | Dependency RTO |
|---|---|---|---|---|
| Activity and peak weeks | | | | |
| People and mandates | | | | |
| Seats and buildings | | | | |
| IT and applications | | | | |
| Suppliers and third parties | | | | |
| Department dependencies | | | | |

Each entry retains its source and source date above. For **each entry**, interview reference: ______; interview date: ______; confirmation date: ______. These remain blank before interviewing. No attachment proposes a recovery time.

**Seven interview sections**

1. **Impacts over time — about 10 minutes.**  
   Establish the dispatch activity boundary and Site B peak weeks. Ask the owner to choose meaningful interruption durations and describe financial, customer and regulatory impacts at each duration, including during peaks. Apply the attached criteria: financial levels are under EUR 10k a day, EUR 10k–100k a day, and over EUR 100k a day; customer levels concern one customer complaint, a late key account, and loss of a key account; regulatory levels concern none, a report to the food authority, and the authority stopping production. Record evidence rather than assigning ratings in advance. The sources provide no activity ranking; assess dispatch fully because it is the interview’s focus. For any additional activity identified, ask where its impacts differ.

2. **The MTPD — about 5 minutes.**  
   Ask when dispatch interruption becomes unacceptable, which impact establishes that boundary, and whether peak weeks change it. The activity owner sets MTPD; the AI draft leaves it empty.

3. **People — about 8 minutes.**  
   Verify the draft reporting structure and obtain the actual shift pattern. Ask which people are required **“with the skills, authorities and mandates the work needs”**, including requirements during peaks. Establish whether a requirement depends on one person and who can provide cover; do not assume a single-person dependency.

4. **Seats and buildings — about 5 minutes.**  
   Identify the seats, buildings and dispatch facilities actually required at Site B and how requirements change during peaks. Site A’s two dock doors are recorded for goods receipt; their relevance to Site B dispatch needs confirmation.

5. **IT and applications — about 7 minutes.**  
   Verify LogiStock and the manual export arrangement. Identify required applications and data, **“each with its RTO and its RPO”**, for the owner to set during the interview. Ask what the export supports and what it cannot support. Both fields remain blank in this draft.

6. **Suppliers and other third parties — about 7 minutes.**  
   Verify the carrier arrangement and current contact responsibilities. Ask whether another carrier is available, which requirements apply during peaks, and whether reliance on a single carrier exists. NordFrost’s presence in Site A’s record is not proof of a Site B dependency.

7. **Dependencies — about 8 minutes.**  
   Establish **“up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”**. Verify QA coverage, release before dispatch, and any departmental relationship behind the manual export. Identify the counterpart owner for each relationship. Leave dependency RTOs blank in the draft.

**Organiser’s take-in sheet — approximately 50 minutes**

No conflict between approved Site A and Site B records is established: the Site B chart is an undated draft. Check possible differences first. Put any conflict that emerges **“to the two owners, not to the model.”** Questions marked **[Drop first]** can be omitted if time runs short.

*Source differences — within the relevant section times*

Does Site B receive QA release from Site A, as the draft chart suggests?

Does the manual export recorded at Site A still reach Site B, and what does dispatch use it for?

Which Site A arrangements differ here, and which counterpart owner can resolve each difference?

*1. Impacts over time — 10 minutes*

What work belongs within Site B dispatch?

Which weeks are busiest here, and do weeks 49–52 and week 14 apply?

At what interruption durations do financial, customer and regulatory impacts change?

Which approved impact level applies at each duration, and what evidence supports it?

[Drop first] For any other activity we identify, where do its impacts differ from dispatch?

*2. MTPD — 5 minutes*

When would a dispatch interruption become unacceptable, and which impact makes it unacceptable?

Does that point change during peak weeks?

*3. People — 8 minutes*

What is the actual shift pattern, and is the draft chart’s three-shift-leader arrangement current?

Which roles and how many people does each shift require, including at peaks?

What skills, authorities and mandates must those people have?

Does any requirement depend on one person, and who can cover it?

*4. Seats and buildings — 5 minutes*

Which seats, buildings and facilities does dispatch need here?

How do those requirements change during peak weeks?

[Drop first] Are Site A’s goods-receipt dock-door arrangements relevant to dispatch here?

*5. IT and applications — 7 minutes*

Is LogiStock still the system at Site A, and does dispatch here depend on it?

Is the manual export still possible, and what does Site B need to use it?

What RTO and RPO do you require for each application and its data?

[Drop first] Which parts of dispatch can the export support, and which can it not support?

*6. Suppliers and third parties — 7 minutes*

Is NordFrost still the carrier at Site A, and is it a carrier for Site B?

Who holds the current carrier contacts, and who can use them when that person is absent?

Is another carrier available, and what changes during peak weeks?

*7. Dependencies — 8 minutes*

Which departments must provide something before dispatch can proceed?

Which departments depend on dispatch’s output?

Does QA release from Site A have to arrive before Site B dispatch can proceed?

What RTO does each departmental relationship carry, and who is the counterpart owner?

**Gaps**

- **Own statements, not sources:** the organiser states that the material is high sensitivity and this environment is approved for it; the interviewee is the Site B dispatch lead, who knows the shift pattern and carrier contacts; the desired result is resources and peak weeks. These statements shape the interview scope and do not populate requirement or recovery values.
- The source-channel question was unanswered. Working assumption: only the three attachments are organisational evidence; memory, past chats, other project files, connectors and web search are excluded.
- **site-b-org-chart.md:** undated, unversioned HR draft. Obtain a dated, approved structure and verify the roles and QA coverage with their owners.
- Site B’s peak weeks, current resources, carrier contacts, impact progression and recovery requirements are **not in the sources**. Owner evidence is needed.
- The sources do not rank activities by impact. Peak weeks do not establish an impact ranking.
- Current applicability of Site A’s March 2026 arrangements remains to be checked with the relevant owners.

The **activity owner** confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Preserve confirmed and unconfirmed marks when handing on the interview record; all entries in this draft remain **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

**Tool calls (JSON events):**

- none
