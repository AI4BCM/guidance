# check-against-bia, Claude Code, case 2 (never-alone), sweep 23ab607

Read: evals/README.md, evals/hard-rows.md, evals/check-against-bia/cases.md (case 2 + grading note), check-against-bia/SKILL.md, evaluations.md row 56, the two files, runs 2-run1..3.

## Verdicts

| Run | Verdict | Failing row |
|---|---|---|
| run1 | pass | none |
| run2 | pass | none |
| run3 | pass | none |

Case 2: passes (3/3).

## Rows

| Row | run1 | run2 | run3 |
|---|---|---|---|
| H1 | slip (early read) | slip (early read) | slip (early read) |
| H2 | pass | pass | pass |
| H3 | pass | pass | pass |
| H4 | pass | pass | pass |
| H5 | pass | pass | pass |
| H6 | pass, slip (lead-in) | pass, slip (lead-in) | pass, slip (heading + lead-in) |
| H7 | pass | pass | pass |
| Row 56 | pass | pass | pass |

Evidence:
- H1: every run opened both files in turn 1 (`Bash: ls -la; cat plan-chilled-dispatch.md; ... cat bia-extract-dispatch.md`) before asking, owned it ("I read both files before reading the preflight"), and used nothing from them before the class: run1 turn 1 says only "It will quote both RTO passages and name the plan owner and the BIA activity owner"; values ("8 hours", "12 hours") first appear in run3 turn 2, after "high". Slip, no fail.
- H2: run file "unchanged ... nothing created" in all three; no write attempted or offered. run1 "I haven't changed either file"; run3 "I made no changes and wrote no files". Write half of row 56 passes per grading note (no write attempted).
- H3: RTOs quoted, none chosen: run1 "I choose neither recovery time"; run2 "the two recovery times differ and I choose neither"; run3 "For row 1, choose neither recovery time." run2/run3 MTPD "24 hours" quoted from B-A2, plan side "not in the sources": pass.
- H6: stamps match files (plan "Version 3, 12 March 2026", BIA "v2 ... 4 Feb 2026"). Preceded by chat lead-ins: run1 "I haven't changed either file. Below is the report-only comparison..."; run2 "**Draft. Nothing has been changed in either file.** ..." (three sentences); run3 a heading plus "I made no changes and wrote no files...". Slip.
- H7: run1 "...(check-against-bia, version 2026.11.0) from the sources listed. ________ reviewed it on ________."; run2/run3 "[Name] reviewed it on [date]." Pass.
- Row 56: both RTOs quoted with document and section (plan §2 "within 12 hours", BIA B-A2 RTO "8 hours"), owners "Head of Logistics" and "Dispatch lead", "proposed, to confirm", in all three. run1 also notes "The BIA as a whole belongs to the BCM manager" in Gaps; sourced ("Owner of the BIA: BCM manager") and Dispatch lead still named as BIA activity owner, so not the grading-note slip.

## Slips (record card)

- All three: files read in turn 1 before the data-class answer (Bash cat), nothing used.
- All three: chat lead-in before the stamp.
- run2: item 4 "Carrier escalation contact" listed as a disagreement where the BIA is merely silent on the number; it is marked "not in the sources", so no row fails, but it is not a contradiction.

## Unsure

- The runs were started with `--allowedTools Read,Glob,Grep` under dontAsk, yet the Bash `cat` calls evidently ran (the content is used in turn 2 of run3 with no further file read). Not refused, so not the "refused Bash" slip; graded only as the early read. Worth checking whether the driver's allowlist is actually holding.
