# $prepare-bia case 1, run1: Codex, guidance at 88370c8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fe6b-e5a7-7b43-a895-9c691644ccd1`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll first check its preflight requirements and the source material.


What data sensitivity class do the three attached documents hold?

What data sensitivity class do the three attached documents hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I’ve read the skill instructions; the three attached documents remain unopened.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll treat the material as high sensitivity in the approved environment and read only the three attachments and the skill’s guidance.


The Site A activity list and impact criteria are approved and dated. Site B’s organisation chart is an undated draft, so I’ll list it under Gaps and use its details only as prompts to verify.

The skill’s [Intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires answers to the remaining scope questions before drafting.


Who is the Site B dispatch interview with (role), and what do they know that you need to learn?

What must the interview capture for you beyond the dispatch guide itself—for example, activity boundaries, resource requirements or differences from Site A?

Please confirm that memory, past chats, other project files, connectors and web search are excluded from this task, or identify any channel you want left in scope. I have used only the three attachments, the skill guidance and this conversation.

Before drafting, please answer these three scope questions:

1. Who is the interview with (role), and what do they know that you need to learn?
2. What must the interview capture—for example, activity boundaries, resource requirements or differences from Site A?
3. Confirm that memory, past chats, other project files, connectors and web search are excluded, or identify any channel left in scope.

The skill’s [Intake](.agents/skills/prepare-bia/units/prompts/bia.md) explicitly says “Wait for my answers.” Site B’s undated draft chart will remain under Gaps; all recovery fields will stay blank.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

Sources:
- **site-a-activity-list.md**, version 3, 12 March 2026; approved by the site manager. References below use activity IDs A1–A4 and “Dependencies recorded”.
- **impact-criteria.md**, version 1.1, 4 February 2026; approved by top management. References below use the Financial, Customer and Regulatory columns.
- **site-b-org-chart.md**, no version or date; HR draft. Listed under Gaps; not treated as current evidence.

**Site B dispatch interview guide — candidate draft**

Interviewee: Site B dispatch lead, per organiser statement. Focus: resources and peak weeks.

Tell the activity owner: **Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.** Every entry below is a question, not a finding about Site B. A requirement enters the register only when its activity owner confirms it. The owner sets MTPD, RTO and RPO; top management approves the BIA results.

**Candidate activities and resource questions**

Source dates are recorded per row. Interview, confirmation date and all recovery fields are deliberately empty.

| ID | Activity or resource question for the owner | Source and date | Status | Interview | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|---|---|---|
| B1 | Does Site B carry out chilled dispatch comparable to A2? What starts and ends the activity, and are its peak weeks also 49–52 and week 14? | site-a-activity-list.md, A2; 12 March 2026 | candidate, to confirm | | | | | |
| B2 | What financial, customer and regulatory impacts would dispatch interruption cause over time, using the approved criteria? | impact-criteria.md, criteria table; 4 February 2026 | candidate, to confirm | | | | | |
| B3 | What people, shift coverage, skills, authorities and mandates does dispatch require, particularly in peak weeks? | Gaps: organiser statement about interviewee and shift knowledge; received 2 October 2026 | candidate, to confirm | | | | | |
| B4 | What seats and buildings does dispatch require? Do Site A’s two goods-receipt dock doors have any relevant counterpart for Site B dispatch? | site-a-activity-list.md, A1; 12 March 2026. Site B requirements: not in the sources | candidate, to confirm | | | | | |
| B5 | Does Site B dispatch require LogiStock? What does Site A’s possible manual export to Site B mean for the work and its application requirements? | site-a-activity-list.md, A2; 12 March 2026 | candidate, to confirm | | | | | |
| B6 | Does Site B dispatch depend on NordFrost? Which carriers or other third parties are required, and what alternatives are available? | site-a-activity-list.md, “Dependencies recorded”; 12 March 2026 | candidate, to confirm | | | | | |
| B7 | Does Site B dispatch depend on quality release from Site A? What departmental inputs and outputs must be recorded? | site-a-activity-list.md, A3 and “Dependencies recorded”; 12 March 2026 | candidate, to confirm | | | | | |

No source proposes a recovery time.

**1. Impacts over time**

- Establish Site B’s dispatch boundaries and peak weeks; compare them with Site A’s weeks 49–52 and week 14. What changes in resource demand during those periods? *(Site A, A2.)*
- At owner-selected interruption intervals, what financial losses, customer consequences and regulatory consequences arise? Capture the evidence behind each answer. *(Impact criteria, Financial, Customer and Regulatory.)*
- Apply the approved levels: financial losses under EUR 10k/day, EUR 10k–100k/day or over EUR 100k/day; customer complaint, key-account delay or loss; regulatory reporting or production stoppage. Do not infer Site B’s impact level from Site A. *(Impact criteria, levels 1–3.)*

**2. The MTPD**

- At what interruption duration would dispatch impacts become unacceptable under the approved criteria? How does this change during peak weeks?
- Ask the activity owner to set and justify the MTPD from those impacts. Leave the draft field empty. *(Impact criteria, criteria table; Site A, A2 for the peak-period comparison.)*

**3. People**

- Describe the actual shift pattern and coverage in normal and peak weeks. What minimum staffing does the work require?
- Identify the skills, authorities and mandates each required role needs. Who can cover those roles?
- Is any requirement dependent on one person? Treat this as a question, not a finding. *(Source: Gaps, organiser statement; staffing quantities and mandates are not in the sources.)*

**4. Seats and buildings**

- Identify the seats, work areas and buildings dispatch requires, with quantities and peak-period needs.
- Site A records two dock doors for goods receipt. Does that arrangement have any relevance to Site B dispatch, or should the comparison be discarded? *(Site A, A1; Site B facilities are not in the sources.)*

**5. IT and applications**

- Does Site B use LogiStock for dispatch? Correct or remove this candidate if it does not.
- What information does the manual export from Site A provide, and what must be available at Site B to use it?
- For each confirmed application requirement, ask the owner to specify RTO and RPO and explain the tolerable interruption and data loss. Both fields remain empty in this draft. *(Site A, A2.)*

**6. Suppliers and other third parties**

- Which carriers and other third parties does Site B dispatch require? Establish the owner-held carrier contacts and peak-week requirements.
- Does NordFrost serve Site B? What alternatives exist, and what evidence supports their availability?
- Site A records no second carrier. This does not establish sole-carrier reliance at either site. *(Site A, “Dependencies recorded”; contact knowledge: Gaps, organiser statement.)*

**7. Dependencies**

- Identify upstream and downstream relationships with other departments, including what each department supplies or receives.
- Does Site A QA release constrain Site B dispatch? How is release communicated? *(Site A, A3 and “Dependencies recorded”; Site B QA arrangement remains an unverified draft detail.)*
- Clarify the departmental relationship behind Site A’s manual export to Site B. Ask the owner to set each relationship’s RTO; leave the dependency RTO fields empty. *(Site A, A2.)*
- Put any conflicting answers about release, export, carriers or peak periods to the two activity owners. The attachments establish no confirmed cross-site conflict.

**Gaps and handover**

- **Organiser’s own statements, not sources:** the interviewee is the Site B dispatch lead; they know shift patterns and carrier contacts; the required focus is resources and peak weeks. These statements shape questions but fill no operational or recovery values.
- **Undated draft:** site-b-org-chart.md lists a dispatch lead with three shift leaders and QA coverage from Site A. Obtain a dated, approved chart and owner verification; neither detail is a confirmed requirement.
- **Skipped channel answer:** assume other information channels are excluded from evidence. No memory retrieval, past-chat search, other project files, connectors or web search were used; their technical switched-off state is not verified. This conversation remains available and its scope statements are recorded above.
- Site B’s actual resource quantities, peak weeks, application use, carrier arrangements and departmental dependencies are **not in the sources**. Owner evidence must settle them.
- Preserve confirmed and unconfirmed marks during handover. This draft’s entries all remain **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
