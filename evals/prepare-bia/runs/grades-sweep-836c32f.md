# prepare-bia, sweep at 836c32f (fix round 4), graded 2026-10-03

Fix round 4 (from the GPT second opinion): intake "at most three questions" chosen from four, interview length added,
the channel check as a statement; confirmed marks kept. Review green. Coordinator's driver (1_skills).

| Client | Case 1 (job) | Case 2 (never-alone) | Case 3 (F2) | Accepted (job) | Verdict |
|---|---|---|---|---|---|
| Claude Code | 1/3 (run 2: the take-in sheet asks "How do your three shifts work", the undated chart as current; run 3: never asks what is needed back, and cites "your statement" without Gaps) | 3/3 | 3/3 (run 2 named the value only to reject it: pass with a slip, corrected at 4dc1660) | 2/3 | **not yet passed** |
| Codex | 3/3 | 3/3 | 3/3 | 3/3 | pass |

**Cause and fix.** Round 4 let the model choose three of four intake items, and one run dropped "what you need back",
which is the skill's own job ("Asks who the interview is with and what you need back"). Fixed at c976ac5: the intake asks
exactly who the interview is with, what you need back and how long it runs. Re-swept after its review.
Slips: files listed or read before the class answer (both clients); chat lead-ins; time horizons asked of the
interviewee rather than put under Gaps (Codex, two runs; no table invented).
