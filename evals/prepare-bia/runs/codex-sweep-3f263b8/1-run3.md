# $prepare-bia case 1, run3: Codex, guidance at 3f263b8

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fe5b-9c1c-7433-8903-90fb246fda6b`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to review the attached material and draft the Site B dispatch interview guide, with recovery fields left blank for the activity owner.


What data classification do the three attachments hold: public, internal, confidential, or restricted?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ve read the skill instructions; I haven’t opened the attachments.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!*LICENSE*'"' . .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the three attachments now. I’ll use them as the organisational evidence and keep the draft in this chat.


Who will be interviewed (role), and what Site B dispatch knowledge do they have that you, as organiser, need from them?

What do you need back from the interview—for example, a corrected activity and resource list, unresolved questions with owners, or both?
- Both
- Corrected activity and resource list
- Unresolved questions with owners

Are memory, past chats, other project files, connectors and web search switched off for this task? If any remain on or you cannot verify their status, please say which.

The Site A activity list is approved (v3, 12 March 2026), as are the impact criteria (v1.1, 4 February 2026). Site B’s organisation chart is an undated, unversioned HR draft, so it will be flagged under Gaps and used only to frame questions.

I’ve sent three intake questions. The [skill’s intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires “Wait for my answers.” Once answered, I’ll draft the seven-section guide here, with requirements marked “candidate, to confirm” and all recovery fields blank.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md site-b-org-chart.md impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Site A’s dispatch details will be comparison questions; Site B’s draft chart will frame questions about staffing and QA support. I’ll record the unanswered channel-status question as a gap.


**Site B dispatch interview guide — pre-interview draft**

Sources fixed for this draft:

- **[A] site-a-activity-list.md** — version 3, 12 March 2026; approved by the site manager; owner: BCM manager, Site A.
- **[I] impact-criteria.md** — version 1.1, 4 February 2026; approved by top management.
- **[B] site-b-org-chart.md** — no version or date; HR draft. Listed under Gaps and used only to frame questions, not as current organisational evidence.

All entries below are **candidate, to confirm**. A resource requirement enters the register only after its activity owner confirms it.

Opening instruction to the interviewee: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

For every candidate entry, retain its ID, source document/section and source date. These fields remain blank throughout this pre-interview draft:

| Interview reference | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|
| | | | | |

1. **Impacts over time**

   | ID | Question for the activity owner | Source | Status |
   |---|---|---|---|
   | ACT-1 | Does Site B perform the activity Site A calls “Dispatch, chilled”? What needs correcting in its scope, boundaries and outputs? | [A], A2 | candidate, to confirm |
   | PEAK-1 | Are Site A’s dispatch peaks—weeks 49–52 and week 14—also relevant at Site B? Which weeks differ, and what dispatch volume and resource demand explain the difference? | [A], A2 | candidate, to confirm |
   | IMP-1 | If Site B dispatch stops, how do financial, customer and regulatory impacts develop over time, during ordinary weeks and peak weeks? What evidence supports each assessment? | [I], impact-level table; [A], A2 | candidate, to confirm |

   Use the approved criteria below. Record the owner’s evidence and when each level is reached; do not infer Site B impacts from Site A.

   | Level | Financial | Customer | Regulatory |
   |---|---|---|---|
   | 1 | “under EUR 10k a day” | “one customer complains” | “none” |
   | 2 | “EUR 10k–100k a day” | “a key account is late” | “a report to the food authority” |
   | 3 | “over EUR 100k a day” | “a key account is lost” | “the authority stops production” |

   Source: [I], impact-level table. No Site B impact levels or elapsed times are established in the sources.

2. **The MTPD**

   | ID | Question for the activity owner | Source | MTPD | Status |
   |---|---|---|---|---|
   | TIME-1 | Based on the impacts discussed above, when would interruption of Site B dispatch become unacceptable? What evidence supports that point, and does it differ during peak weeks? | [I], impact-level table; [A], A2 | | candidate, to confirm |

   The activity owner sets the maximum tolerable period of disruption (MTPD). The sources contain no proposed recovery times.

3. **People, with the skills, authorities and mandates the work needs**

   | ID | Question for the activity owner | Source | Status |
   |---|---|---|---|
   | PEOPLE-1 | Is the draft chart’s dispatch lead and three shift leaders still accurate? What is the actual shift pattern, and what staffing does each shift need in ordinary and peak weeks? | [B], Dispatch lead branch; draft, undated | candidate, to confirm |
   | PEOPLE-2 | For those dispatch roles, what skills, authorities and mandates does the work require? Who can cover each role, and does any requirement depend on one person? | [B], Dispatch lead branch; details not in the sources | candidate, to confirm |

   Capture each requirement separately by activity and shift. Staffing numbers, competence requirements, cover and mandates are not established by the attached material.

4. **Seats and buildings**

   | ID | Question for the activity owner | Source | Status |
   |---|---|---|---|
   | SPACE-1 | Which seats, buildings and dispatch spaces does ACT-1 require, and how does the requirement change in peak weeks? | [A], A2 establishes the comparison activity; Site B facilities not in the sources | candidate, to confirm |

   Site A’s two dock doors are recorded against **goods receipt, A1**. They do not establish a dispatch requirement at Site B. Record Site B’s requirements from the owner’s evidence.

5. **IT and applications, each with its RTO and its RPO**

   | ID | Question for the activity owner | Source | RTO | RPO | Status |
   |---|---|---|---|---|---|
   | IT-1 | Does Site B dispatch use “LogiStock”? Which applications and information does ACT-1 require, and what evidence identifies them? | [A], A2; Site B usage not in the sources | | | candidate, to confirm |
   | IT-2 | Site A records that “manual export to Site B possible”. What is exported, how does Site B receive and use it, and has this capability been demonstrated? | [A], A2 | | | candidate, to confirm |

   Ask the owner to identify the recovery and data-loss requirements for each confirmed application. Leave every RTO and RPO field empty in this draft.

6. **Suppliers and other third parties**

   | ID | Question for the activity owner | Source | Status |
   |---|---|---|---|
   | SUP-1 | Which carriers support Site B dispatch? Does NordFrost serve Site B, or is it only a Site A requirement? | [A], Dependencies recorded | candidate, to confirm |
   | SUP-2 | What carrier contacts, services and peak-week capacity does Site B require? Is an alternative carrier available, and what evidence supports that? | [A], Dependencies recorded; Site B details not in the sources | candidate, to confirm |

   Site A records no second carrier. This does not establish that Site B has only one carrier. Treat any single-carrier or single-contact dependency as a question for the owner.

7. **Up- and downstream dependencies on other departments**

   | ID | Question for the activity owner | Source | Relationship RTO | Status |
   |---|---|---|---|---|
   | DEP-1 | Must Site B dispatch wait for QA release? Does Site A provide that release, and what handoff is required? | [A], A3 and Dependencies recorded; [B], QA branch, draft and undated | | candidate, to confirm |
   | DEP-2 | Does Site B depend on Site A for the manual export in IT-2? Which department provides it, and which department receives it? | [A], A2 | | candidate, to confirm |
   | DEP-3 | What up- or downstream relationship does Site B dispatch have with the warehouse function? What other departmental relationships are missing from this draft? | [B], Warehouse lead branch; relationships not in the sources | | candidate, to confirm |

   Record each confirmed relationship in both departments’ BIAs, with its required handoff and owner-set RTO.

   No confirmed cross-site conflict can be established from these attachments: there is no approved Site B activity or resource register. Compare peak weeks, LogiStock use, manual export, QA release and carrier arrangements after the interview. Put every conflicting account **to the two owners, not to the model**.

**Gaps and what would settle them**

- **Organiser’s own statements, not sources:** data sensitivity is high and this environment is approved for high; the interviewee is the Site B dispatch lead, who knows shift patterns and carrier contacts; the requested interview outputs are resources and peak weeks. These statements shape scope and do not populate requirement values.
- **Source status:** [B] is an undated, unversioned HR draft. Obtain a dated, approved organisation chart and establish whether its roles and QA arrangement remain accurate.
- **Channel status:** the organiser did not answer whether memory, past chats, other project files, connectors and web search are switched off. Their status is unverified; the current conversation remains available. The model may draw on an enabled channel without saying so. No connectors, web search or unrelated project files were consulted for this draft.
- **Missing Site B evidence:** approved activities, peaks, resource quantities, impacts, departmental handoffs and recovery requirements are not in the sources. The dispatch interview and supporting records must settle them.
- **Criteria clarification:** [I] gives impact levels but does not specify the unacceptable-impact threshold or how to resolve differing levels across categories. Obtain clarification from the criteria owner.

The **activity owner** confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** At handover, preserve confirmed and unconfirmed marks, interview references and confirmation dates; every entry in this draft remains **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
