# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f18fd4e9-3911-4675-ada8-6959c9d306c1`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I wasn't able to save the guide as a file because write permission was denied, so the full draft is below. It's based on the three files you attached. One caveat: there's no activity list for Site B yet, so anything taken from Site A is treated as an assumption to check in the interview, not a fact about Site B.

---

# Interview guide: BIA interview, Dispatch, Site B

Status: draft for review, prepared 3 October 2026. Not yet approved.

| | |
|---|---|
| Interviewee | Dispatch lead, Site B. Invite one of the three shift leaders as well if possible. |
| Interviewer | BCM manager (or delegate) |
| Duration | 90 minutes |
| Purpose | Find out what Site B dispatch needs to keep running, what happens over time if it stops, and how quickly it has to be back. |
| Sources | Impact criteria v1.1 (approved); Site A activity list v3 (approved, **Site A only**); Site B org chart (undated HR draft) |

## 1. Before the interview

**What the sources tell us and how reliable they are**
- **Impact criteria v1.1** are approved by top management. Rate impacts against them as written; don't change the scales during the interview.
- **The Site B org chart is an undated draft with no version.** At the start of the interview, check the roles and reporting lines.
- **There is no activity list for Site B yet.** Everything below that comes from Site A is a hypothesis we need to test.

**Hypotheses carried over from Site A (confirm or reject each one)**

| # | Hypothesis | Origin |
|---|---|---|
| H1 | Site B dispatch handles chilled goods. | Site A, A2 |
| H2 | Peaks fall in weeks 49–52 and week 14. | Site A, A2 |
| H3 | Site B uses the warehouse system "LogiStock". | Site A, A2 |
| H4 | Goods can't be dispatched until QA has released them, and QA release depends on the lab at Site A, the only lab. | Site A, A3; org chart says "QA: covered from Site A" |
| H5 | NordFrost is the only carrier, with no second carrier on record. | Site A dependencies |
| H6 | Site B is the fallback for Site A dispatch ("manual export to Site B possible"). | Site A, A2 notes |

**Prepare**
- [ ] Send the interviewee the impact criteria table and the time scale from section 5 in advance.
- [ ] Bring a blank activity-list template in the Site A format.
- [ ] If possible, put the open question in section 9 to the BCM manager before the interview.

## 2. Opening (5 min)
- Explain why we're running the BIA, how the results will be used, and that the interviewee will review the notes before anything is finalised.
- Confirm the org chart. Who reports to the Dispatch lead? How are the three shift leaders organised? Who deputises for the Dispatch lead?

## 3. The activity (15 min)
1. In your own words, what does Site B dispatch do? Where does the work start and end?
2. What do you dispatch: chilled, frozen, ambient? Roughly what volumes per day or week? *(H1)*
3. Who are the main customers? Which of them are key accounts? What delivery windows or service levels have you agreed with them?
4. What are the operating hours and shift pattern? Do you work weekends or public holidays?
5. When are your peak periods, and how much does volume rise? Are they the same as Site A's? *(H2)*
6. Does Site B dispatch anything for Site A, or would it in an emergency? What does "manual export to Site B" mean in practice, and has it ever been tested? *(H6)*
7. Does Site B depend on Site A for anything else (goods, staff, systems, planning)?

## 4. Dependencies (20 min)
For each dependency, ask three things: is there an alternative, how long does it take to switch, and has the switch ever been done?

- **People:** What is the minimum number of staff at normal volume, and at peak? Are there tasks only one person can do, such as system admin, customer portals or temperature records? Who can step in for the Dispatch lead and the shift leaders?
- **QA release** *(H4)*: Who releases goods for dispatch, how is the release passed on, and how long does it take? If Site A or its lab is unavailable, can anything ship? Is there any provision for conditional or emergency release?
- **IT and data** *(H3)*: Which systems do you use (warehouse, transport planning, labels, EDI or customer portals, temperature logging)? Is it LogiStock? Where are the systems hosted, and are they shared with Site A? Is there a manual fallback, and how long could you keep it going?
- **Carriers** *(H5)*: Is NordFrost the only carrier? Is there a contract or a known alternative for chilled transport? How long would it take to bring in a replacement?
- **Facilities and equipment:** How many dock doors and how much chilled storage do you have? What happens if the refrigeration or power fails? Which equipment is critical (forklifts, label printers, scanners)?
- **Other inputs:** Packaging, pallets, data loggers and similar.

## 5. Impact over time (20 min)
Scenario: **Site B dispatch can't operate at all.** Rate each category from 1 to 3 using the approved criteria. Ask for the reasoning and any evidence, such as contract penalties, revenue per day or product shelf life.

| Duration | Financial | Customer | Regulatory | Reasoning / evidence |
|---|---|---|---|---|
| 4 hours | | | | |
| 1 day | | | | |
| 3 days | | | | |
| 1 week | | | | |
| 2 weeks | | | | |

Repeat the rating for a **peak-week disruption** if the interviewee expects a materially different result.

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Follow-up questions:
- How long are chilled goods saleable once held? When does stock waiting to go out turn into waste?
- At what point would a key account start moving volume elsewhere?
- What would trigger a report to the food authority, for example a break in the cold chain or gaps in traceability?

## 6. Recovery requirements (15 min)
1. How long can dispatch be down before the impact becomes unacceptable? Use the table above to justify the answer.
2. Within what time must dispatch resume, and at what minimum level (for example, key accounts only, or a share of volume)?
3. What do you need to reach that minimum: people, systems, a carrier, QA release, space?
4. How much data or paperwork can you afford to lose (orders, temperature records, delivery notes)? Where are they backed up?
5. What workarounds exist today, and are they written down? Could Site A take over Site B's dispatch, and the other way round?

## 7. Close (5 min)
- Summarise the activities, dependencies and ratings back to the interviewee.
- Agree which documents they'll send (key-account contracts, carrier contract, shift plan, existing procedures).
- Agree a review date and who approves the Site B activity list.

## 8. Output to produce after the interview
- A Site B activity list in the Site A format, with dispatch as the first entry.
- The completed impact-over-time table and the recovery requirements, with the reasoning behind them.
- Each hypothesis H1–H6 marked as confirmed or rejected.
- Cross-site dependencies (QA and the lab at Site A, the Site A to Site B fallback, a shared carrier) passed to the Site A owner, since the Site A list may need updating.

## 9. Open points for the BCM manager (not for the interviewee)
- **No threshold has been defined for "unacceptable".** The impact criteria set out three levels but don't say which level marks the maximum tolerable disruption. Get this decided before you set recovery times, so Site B is assessed on the same basis as Site A.
- **The Site B org chart needs a dated, versioned release from HR** before the BIA can be approved.

---

If you allow file writes, I can save this as `site-b-dispatch-interview-guide.md` in the folder.

**Tool calls (stream-json):**

- Bash: `ls -la && cat *.md`
- Write: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
