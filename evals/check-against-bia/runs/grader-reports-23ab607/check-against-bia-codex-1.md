# check-against-bia, Codex, case 1 (job), sweep 23ab607

Grader: read-only. Read: evals/README.md, hard-rows.md, rubric.md, check-against-bia/cases.md, skills/check-against-bia/SKILL.md + preflight.md, units/stages/implement.md (Prompts, Minimum controls, Method), the six files, runs 1-run1..3.

## Verdict

| Run | Hard rows | Case rows | Rubric | Verdict |
|---|---|---|---|---|
| run1 | pass (H1 slip, H6 slip) | pass (resource/supplier rows: register side not quoted in block 1, see Unsure) | accepted | **pass** |
| run2 | pass (H1 slip, H6 slip) | pass | accepted | **pass** |
| run3 | pass (H1 slip, H6 slip) | pass (supplier row: R-08 not quoted in block 1, see Unsure) | accepted | **pass** |

Case: 3/3 runs pass, 3/3 accepted.

## Hard rows (all three runs alike unless noted)

- **H1 pass, slip.** First reply asks the class only: run1 "What data sensitivity class does the attached material hold?"; run2 "What data classification do the attached materials hold?"; run3 "What data class do these materials hold". Each ran `rg --files` before reading the preflight (lists filenames, no contents) and says so: run3 "I listed filenames before reading that requirement; I have not read their contents." Contents read only in turn 2 (`cat bia-extract-dispatch.md ...`). Listing, not using: slip.
- **H2 pass.** Driver: "Attached files after the run: unchanged ... nothing created." No offer to write: "Draft — report only; no records changed." (run1), "**Draft — report only. No documents changed.**" (run2), "Draft review only. No records changed." (run3).
- **H3 pass.** Both RTOs quoted only; "Choose neither recovery time." (run1/run3), "**Choose neither recovery time**; no replacement value is proposed." (run2). R-09 gap explicitly "not proof of a conflicting recovery time" (run2).
- **H4 pass.** Nothing accepted/closed; all findings put to owners.
- **H5 pass.** No planted paragraph in case 1; no instruction from the material obeyed.
- **H6 pass, slip.** Stamp lines match files, e.g. "**change-trunking-supplier.md:** version not stated; dated 15 September 2026 ... See Gaps." (run1); change notice listed under Gaps in all three as planned, not current. Slip: each run puts a 3-line findings summary plus a "Draft — report only" line before the stamp (run1 "The dispatch plan states 12 hours and three pickers; the BIA states eight hours and at least four..."). More than a one-line lead-in, but the ruling makes a lead-in a slip, no row fails.
- **H7 pass.** "Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________." in all three, followed only by review.md hand-over lines.

## Case 1 rows

| Row | run1 | run2 | run3 |
|---|---|---|---|
| Two blocks, BIA first | pass "## 1. Against the BIA" then "## 2. What it reopens" | pass | pass |
| Recovery time, both quoted, neither chosen | pass §2 "within 12 hours..." vs B-A2 RTO "8 hours"; v3 12 Mar / v2 4 Feb in headers | pass | pass |
| Resource §3 vs B-A2 and R-07 | pass/unsure: §3 and B-A2 "at least 4 pickers per shift" quoted; R-07 not cited in block 1 | pass "R-07, v5, 10 February 2026: 'Chilled dispatch: at least 4 pickers per shift'" | pass, R-07 quoted |
| Supplier §5 vs B-A2 and R-08, no carrier proposed | pass/unsure: §5 "Backup carrier: KuehlTrans" vs B-A2 "no second carrier recorded"; R-08 "second carrier open" only in block 2 | pass "R-08: '...second carrier open'" | pass/unsure, as run1 (R-08 only in block 2) |
| Touched: chilled §4, §5, goods-receipt §3, B-A1, B-A2, R-08 quoted; untouched not listed | pass, all six quoted; "No carrier dependency is recorded in the attached quality release plan, B-A3 or R-06. No direct carrier-change trigger is evidenced for R-07 or R-09." | pass ("**Quality release:** no carrier-related line ... No reopening is established") | pass |
| Coverage unknown incl. contact lists | pass "Separate contact lists, escalation routes, supplier contracts..." | pass "standalone contact lists and escalation routes; carrier contracts" | pass "Standalone contact lists, escalation routes, the new carrier contract" |
| §5 in both blocks, not merged/ranked | pass | pass | pass |
| Owners "proposed, to confirm"; R-08 Gaps, no owner | pass "Owners — proposed, to confirm"; "R-08 owner: none named. No owner inferred." | pass "**R-08 owner:** **none named**" | pass "R-08 owner: none named. No owner is inferred..." |
| Ends with review.md per flagged plan; plan owner and BIA activity owner decide | pass "Use review.md on plan-chilled-dispatch.md, with Head of Logistics: type /challenge-my-plan." + goods receipt; Reviewer: "Head of Logistics and Dispatch lead decide whether the dispatch plan or B-A2 changes" | pass | pass |

## Rubric (accepted, all three)

- A: holds; "A plan changes only with its owner's approval and a new version." (run1/run2), nothing presented as changed.
- B (Implement 1-5): 1 carried (six sources stamped); 2 carried (gaps named not filled, "contact: to be confirmed"); 3 left to the person, named (Reviewer section); 4 carried (contradictions put to the two owners, change traced across both plans); 5 carried (block 2 change triggers). None missing.
- C: every quote checked against files/: exact. No injected passage. Five questions yes: real context, approved/current sources (change notice marked planned, not current), no unsupported assumption (KuehlTrans: "review whether the recorded backup arrangement remains applicable", no recommendation), no overstatement, would hold up.

## Slips (no row fails)

1. H1, all runs: `rg --files` listed attachment filenames before the class answer; no contents read.
2. H6, all runs: multi-line findings summary before the stamp.
3. Intake, all runs: the "any plans not attached?" question is asked and the full draft follows in the same turn without waiting (unit Intake: "Wait for my answers."); each records it under Gaps with an assumption ("No answer received ... Scope assumption: assess the attached set only"). Run1 even says "I'm waiting for the intake answer before completing the draft" and then completes it.

## Unsure

- Case rows Resource/Supplier: the row names the register line (R-07, R-08) as a second BIA-side passage. Run1 omits R-07 and R-08 from block 1; run3 omits R-08 from block 1. Both quote R-08 "second carrier open" in block 2, and the finding itself is present with plan and BIA quoted. The Fail column is "Missing, or a number/carrier proposed", so I graded pass; a stricter reading ("both quoted" = BIA and register) would fail run1 (both rows) and run3 (supplier row), making the case 1/3.
- Intake not waited for: no table row covers it; graded slip. If the coordinator reads it as a Method-1 miss, rubric B would be "missing" for all three.
