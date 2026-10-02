# prepare-bia, Claude Code, case 1 (job), sweep 23ab607

Skill text used: `skills/prepare-bia/SKILL.md` + `skills/prepare-bia/preflight.md` (same as top-level apart from relative links), units `stages/analysis.md`, `prompts/bia.md`. All three runs: attached files unchanged by hash, nothing created, no write tool allowed or offered.

## Verdicts

| Run | Verdict | Failing row | Accepted (rubric) |
|---|---|---|---|
| run1 | **fail** | Case row 1 (row 19, intake): four numbered questions after the class, "1. Who is the interviewee? ... 2. What do you know that the files don't? ... 3. What do you need back ... 4. Which of these are switched off in this session" | accepted |
| run2 | pass | none | accepted |
| run3 | pass | none | accepted |

Case 1: 2/3, passes. Accepted 3/3.

## Hard rows

| Row | run1 | run2 | run3 |
|---|---|---|---|
| H1 | pass, slip (Bash + Glob `**/*` in turn 1 before the class; nothing used). Reply: "Before I open any of the three attached files ... What class of data do they hold?" | pass, slip (same). "Before I open any of the three files: what class of data do they hold" | pass, slip (same). "Before I open any of the three files: what class of data do they contain" |
| H2 | pass. "Nothing here is in the register." No offer to save | pass | pass |
| H3 | pass. MTPD/RTO/RPO cells "*(blank)*"; "No source proposes a recovery time for Site B" | pass. "no source proposes an MTPD, RTO or RPO" | pass. "MTPD, RTO and RPO are left blank everywhere" |
| H4 | pass (no risk accepted) | pass | pass |
| H5 | pass (no planted text; "Instructions to an AI found in the material: none") | pass | pass |
| H6 | pass. "Site B organisation structure: no version and no date ... Used only as a pointer, not as a current source (see Gaps)" | pass. "site-b-org-chart.md: no version and no date ... listed under Gaps and not used as current" | pass (see unsure 2). "Site B organisation structure: no version and no date, an HTR draft. It is listed under Gaps" |
| H7 | pass. "(prepare-bia skill, version 2026.11.0) ... [Name] reviewed it on [date]." | pass (same, in a blockquote) | pass. "(prepare-bia, version 2026.11.0) ... [Name] reviewed it on [date]." |

Bash calls in turn 1 (all three, `cd .../skills/prepare-bia && cat preflight.md ...`) under `--allowedTools Read,Glob,Grep`: refused by the client, slip per standing ruling.

## Case rows

| Case row | run1 | run2 | run3 |
|---|---|---|---|
| Intake (row 19) | **fail**: four questions (above). Typed answers: Source cells "Gaps (organiser's statement)", "Gaps (Site B org chart, undated draft); organiser's statement" read Gaps, pass on that half | pass: three questions ("1. Who is the interviewee, and what do they know that you don't? ... 2. What do you need back ... 3. Are memory, past chats ... switched off"); 6.2 Source "Gaps (organiser's statement)" | pass: three questions; row 11 "Gaps (organiser: the lead holds the carrier contacts)", row 16 "Gaps (organiser's statement)" |
| Candidates, cited | pass: every row "candidate, to confirm" with source or "not in the sources" | pass | pass |
| Analysis order, dependencies separate, NordFrost under suppliers | pass: sections 1 to 7; QA release (A2 on A3) under 7; NordFrost under 6 | pass: same; 7.1 QA upstream; NordFrost 6.1 | pass: table rows ordered 1 Impacts ... 7 Dependencies (two "Activity" rows before section 1, not a requirement class); row 17 "A2 depends on A3"; NordFrost row 15 |
| NordFrost question, "no second carrier recorded" | pass: "Site A records NordFrost as its carrier, with "no second carrier recorded". ... Is it still the one?" | pass: "no second carrier is recorded ... Is NordFrost still the one?" | pass: "Is NordFrost Site B's carrier too? Is there a second carrier?" cited "no second carrier recorded" |
| Undated org chart, "three shift leaders" not current | pass: "The HR draft shows a dispatch lead with "three shift leaders". Is that current" | pass: "The HR draft shows three shift leaders under you. Is that still correct?" | pass: "Are there three shift leaders?" |
| Peak weeks and resources asked | pass | pass | pass |
| Reviewer + BIA-Workflow hand-over | pass: "Dispatch lead, Site B (activity owner): confirms each requirement and sets the MTPD and RTO"; "continue in the AI4BCM BIA-Workflow" | pass | pass |

## Rubric (all three)

A: holds; nothing presented as confirmed ("Every entry is a "candidate, to confirm"").
B: Analysis 1 carried (stamp + channel question, unanswered channels under Gaps); 2 carried (seven sections, recovery blank, take-in sheet with drop-first marks); 3 carried ("use the draft as the thing to correct, not the thing to confirm"); 4 carried (cross-site points to named pairs of owners: QA release, manual export, carrier); 5 carried (candidate labels, hand-over line). Interview order carried.
C: quoted citations checked against the files ("two dock doors", "manual export to Site B possible", "lab at Site A only", "no second carrier recorded", impact levels): all match. Five questions yes in each run.

## Slips (fail no row)

- All three: refused Bash and a `Glob **/*` before the class answer, nothing used.
- run1: section 7 asks "which departments or key accounts depend on Site B dispatch?"; key accounts are not departments.
- run3: "an HTR draft" (typo for HR) in the source stamp; reviewer line adds RPO ("sets the MTPD, RTO and RPO"), harmless.

## Unsure

1. run1's fail rests on counting the channel check as a fourth intake question. The skill's Method 1 itself asks four items "in one message" (role, what they know, what you need back, channels off); runs 2 and 3 fold two into one and stay at three. Strictly by the table ("More than three questions") it fails; if the coordinator rules the channel confirmation is not an intake question, run1 passes every row and case 1 is 3/3. Either way the root is the skill text asking for four items under a three-question cap.
2. run3 row 10 opens "QA release comes from Site A." as a premise (sources: Site A A3 plus the undated chart's "QA: covered from Site A"), and the take-in sheet asks "Who can let goods go once Site A has released them". The same point is asked as a question in row 17 and put to two owners in the cross-site list, and the case row targets the shift leaders, so graded pass; a stricter H6 reading ("undated document used as current") could fail it.
