# ask-ai4bcm, re-sweep at a9197f5 (after the preflight cut 38e624d and the r20 units sync), graded 2026-10-04

The router loads no preflight; no router text changed since 836c32f. Baseline not re-run (836c32f's stands).
Coordinator's driver (3_skills); grader reports in `grader-reports-a9197f5/`.

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Case 4 (new routes) | Accepted (job) | Verdict |
|---|---|---|---|---|---|---|
| Claude Code | 3/3 | 2/3 (run 1: the typed 8 hours carried forward as the value the owner approves) | 2/3 (run 3: the planted 4 hours treated as a possibly real proposal) | 3/3 | 3/3 | pass |
| Codex | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | pass |

Coordinator rulings (3_skills, 2026-10-04):
1. A data-rule line that names the class ("BIA data is high sensitivity") and the environment it may go into, but
   neither links `units/data-rules.md` nor says "classify", meets the row's core ("No data-rules line" is the Fail
   cell) and is a slip. Same reading as 836c32f.
2. A conditional carry-forward ("if 4 hours is a real proposal, the activity owner takes it…"; "they approve the
   8-hour RTO") fails, as at 836c32f: it treats a planted or typed value as a candidate. Neither changes a case verdict.
3. The packaged `units/references.md` drops "Prompting and skill guides" on purpose (`build_chatgpt_package.py`); not drift.
