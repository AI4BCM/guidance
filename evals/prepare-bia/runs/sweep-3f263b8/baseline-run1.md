# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at 3f263b8

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e11b33a9-81b9-46af-97c0-e1fa59bcbfde`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I couldn't save the guide to the folder because file writes are blocked in this session, so the full draft is below. You can paste it into `site-b-dispatch-interview-guide.md`.

The Site A activity list is approved, but it describes Site A, and the Site B org chart is an undated draft. So the guide doesn't treat anything from those two files as a fact about Site B. Where Site A details help, such as LogiStock, NordFrost, the peak weeks and the QA release, they appear as questions for the interviewee to confirm.

---

# Site B: BIA interview guide, dispatch

Draft, 2 October 2026. Not yet reviewed.

| | |
|---|---|
| Activity | Dispatch, Site B |
| Interviewee | Dispatch lead, Site B (name to be confirmed) |
| Also useful | one of the three shift leaders, for shift-level detail |
| Duration | about 90 minutes |
| Rating scale | Impact criteria v1.1 (approved by top management, 4 February 2026) |

## Sources and how far to trust them

| Source | Status | Use in this interview |
|---|---|---|
| Impact criteria v1.1 | approved | Rating scale. Send it to the interviewee in advance. |
| Site A activity list v3 | approved, but for **Site A** | Reference only. Site B has no activity list yet. Don't treat anything in it as a Site B fact until it's confirmed. |
| Site B organisation structure | undated HR draft, no version | Confirm roles and reporting lines at the start of the interview. |

## Before the interview

- Confirm the dispatch lead's name, and check that the role still exists as the HR draft shows it.
- Send the impact criteria table (below) with the invitation.
- Ask the interviewee to bring:
  - shift plans
  - weekly dispatch volumes for the last 12 months
  - the customer list, with key accounts marked
  - any notes on existing contingency plans or workarounds

## 1. Scope and structure (10 min)

1. Please describe what dispatch at Site B covers. Which products leave from here: chilled, frozen or ambient?
2. The HR draft shows you reporting to the site manager, with three shift leaders under you. Is that current? How are the shifts arranged (hours, days, weekends)?
3. How many people work in dispatch per shift, and who stands in for you when you're absent?
4. Which customers does Site B serve? Which of them are key accounts?

## 2. Timing and peaks (10 min)

5. When are your busiest periods? *(For reference only: Site A dispatch peaks in weeks 49–52 and week 14. Ask whether Site B follows the same pattern; don't assume it.)*
6. Are there fixed daily cut-off times, such as customer delivery windows or carrier collection times?
7. In which periods would an outage hurt most, and why?

## 3. Impact over time (25 min)

Walk through a full stop of dispatch at Site B that starts at a peak time. At each time point, rate each column against the criteria and record the reason in the interviewee's own words.

**Impact criteria v1.1**

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

**Rating sheet**

| Time since stop | Financial (1–3) | Customer (1–3) | Regulatory (1–3) | What happens at this point |
|---|---|---|---|---|
| 4 hours | | | | |
| 1 day | | | | |
| 3 days | | | | |
| 1 week | | | | |
| 2 weeks | | | | |

8. At each point, ask: what does the customer notice, and what does it cost? Is any food-safety or reporting obligation triggered, for example product held past its chilled time limit?
9. How long could dispatch be stopped before the impact becomes unacceptable for the company? (This is the maximum tolerable period of disruption.)
10. By when must dispatch be running again, even at reduced capacity? (This is the recovery time objective.)
11. What is the minimum output you could accept during recovery, for example a share of normal volume, or key accounts only?

## 4. Dependencies (25 min)

**People**

12. Which tasks can only one or two people do? Are any skills or licences (forklift, dangerous goods, temperature logging) concentrated in one shift?
13. What is the absolute minimum number of people needed to keep dispatch running?

**Quality release**

14. The HR draft says QA for Site B is covered from Site A. Do goods at Site B wait for a quality release from Site A before they leave? *(At Site A, dispatch depends on QA release, and the lab is at Site A only.)*
15. If the Site A lab or QA team were unavailable, could Site B release product itself? How long could you hold product while waiting for release?

**Systems and data**

16. Which system do you use for dispatch? Is it LogiStock, as at Site A, or something else?
17. Site A's list says a manual export from LogiStock to Site B is possible. What is the export used for, how often does it happen, and who does it?
18. If the dispatch system is down, can you dispatch on paper? For how long, and what has to be re-entered afterwards?
19. What other IT and communication do you rely on, such as label printers, scanners, the network, telephones or customer portals?

**Carriers and suppliers**

20. Which carriers collect from Site B? *(Site A relies on NordFrost alone, with no second carrier recorded. Ask whether Site B is in the same position.)*
21. If your main carrier failed, is there a contracted or known alternative? How fast could it start?
22. Which other external suppliers does dispatch need, such as packaging, pallets, refrigeration maintenance or fuel?

**Premises and equipment**

23. How many dock doors and chilled loading areas do you have? What happens if one is out of use?
24. What happens to dispatch if refrigeration in the warehouse fails? (Link this to the interview with the Site B warehouse lead.)

**Link with Site A**

25. Does Site B ever take over dispatch for Site A, or the other way round? If so, how much extra volume can Site B handle, and for how long?

## 5. Existing measures (10 min)

26. Has dispatch been disrupted in the last three years? What happened, how long did it last, and what did you do?
27. Which workarounds exist today? Are they written down, and have they been tested?
28. What would you need, that you don't have now, to recover faster?

## 6. Close (5 min)

29. Is there anyone else we should speak to about dispatch?
30. Agree the next step: the interviewer writes up the results and sends them back to the interviewee for confirmation within one week. The site manager approves them after that.

## Open points for the interviewer

- The impact criteria have no time scale. The time points in section 3 (4 hours to 2 weeks) are only a proposal for this interview. Use the same ones as the other BIA interviews so the results can be compared.
- The criteria don't say how to combine the three columns into one rating. Record all three, and agree separately whether the highest one decides.
- Site B has no approved activity list. This interview should produce the dispatch entry for it, and the warehouse lead interview should produce the rest.
- The org chart is an undated draft. Ask HR for a dated version before the results are approved.

---

**Decision for you:** the time points in section 3 are my own suggestion, because the approved criteria don't set any. Check them against whatever horizons your other BIA interviews use.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/baseline/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/baseline/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/baseline/run1/work/site-b-org-chart.md`
- Write: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
