# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at 88370c8

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `47a3772e-f5bb-4bc5-9c0e-77f318d49b70`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I couldn't save the guide as a file because writing to this folder isn't permitted. The full draft is below. Before using it, note three things about the inputs:

- **No activity list exists for Site B yet.** The Site A list is useful for deciding what to ask. But its answers (peak weeks, the NordFrost carrier, the LogiStock system) are Site A's, so the guide asks about each one rather than assuming Site B is the same.
- **The Site B org chart is an undated HR draft with no version.** The guide checks the roles in the interview.
- **Two Site A entries directly affect Site B dispatch.** The org chart says QA for Site B is covered from Site A, and Site A's lab is the only one. Site A's dispatch entry also says "manual export to Site B possible". Each gets its own questions.

---

# BIA interview guide: Dispatch, Site B

Draft, 2 October 2026. Not yet reviewed by the BCM manager.

## 1. Purpose and set-up

| Item | Detail |
|---|---|
| Purpose | Find out how a disruption to Site B dispatch affects the business over time, and what dispatch depends on. Agree recovery targets. The answers become Site B's activity list entry for dispatch. |
| Interviewee | Dispatch lead, Site B. Ask whether one of the three shift leaders should join for the shift-level detail. |
| Interviewer / note-taker | BCM manager (or delegate) and one note-taker |
| Duration | 75 minutes |
| Sign-off | Site manager, Site B |

**Sources and how far to trust them**

| Source | Status | How the guide uses it |
|---|---|---|
| Impact criteria v1.1, 4 Feb 2026 | Approved by top management | The scale for all impact ratings (section 5) |
| Site A activity list v3, 12 Mar 2026 | Approved, but **for Site A only** | A reference for what to ask. Don't copy its answers to Site B. |
| Site B organisation structure | **Undated HR draft, no version** | Confirm roles and reporting lines before relying on it |

**Before the interview**
- [ ] Send the interviewee the impact criteria and the question areas one week ahead.
- [ ] Ask the QA manager at Site A how QA for Site B works today.
- [ ] Ask the dispatch lead at Site A what "manual export to Site B possible" means in practice.
- [ ] Agree the disruption time points with the BCM manager. This guide proposes 4 h, 1 day, 3 days and 1 week. The criteria don't set any.

## 2. Introduction (5 min)
- Purpose of the BIA. Make clear it is not an audit of the team. Explain how the results will be used and that the interviewee will review the notes.
- Confirm the interviewee's role, how long they have held it, and who they report to. This checks the draft org chart.

## 3. The activity (10 min)
1. What does dispatch cover, from released stock to the truck leaving the site?
2. Which products go out: chilled only, or also frozen or ambient? What is the remaining shelf life at dispatch?
3. What are typical and maximum daily volumes (pallets, orders, trucks)?
4. Who are the main customers, and which of them are key accounts?
5. How are shifts organised, and what does each of the three shift leaders cover? What are the operating days?
6. Which parts can only be done at Site B?

## 4. Timing and peaks (5 min)
1. When are Site B's peak weeks? Site A dispatch peaks in weeks 49–52 and week 14. Don't assume Site B is the same.
2. Are there daily cut-offs, such as customer delivery slots or carrier pick-up times?
3. When would a disruption hurt most: time of day, day of week, time of year?

## 5. Impact over time (20 min)
Assume dispatch stops completely at the worst time of year. For each time point, rate each category using the approved criteria, and ask for the reason and figures behind each rating.

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

| Disruption lasts | Financial | Customer | Regulatory | Reason / evidence |
|---|---|---|---|---|
| 4 hours | | | | |
| 1 day | | | | |
| 3 days | | | | |
| 1 week | | | | |

Prompts:
- **Financial:** lost sales, contract penalties, product written off when its shelf life runs out, extra freight costs.
- **Customer:** which key account notices first, and after how long? Do any contracts set delivery service levels?
- **Regulatory:** what happens to traceability and cold-chain temperature records if dispatch works manually?

Then agree:
1. **MTPD** (maximum tolerable period of disruption): when does the impact become unacceptable?
2. **RTO** (recovery time objective): by when must dispatch run again, at least at a minimum level? It must be shorter than the MTPD.
3. **Minimum service level:** what share of normal volume, and which customers or products come first?
4. **RPO** (recovery point objective): how much order and shipment data can be lost and re-entered?

## 6. Dependencies (20 min)
For each dependency, record whether there is an alternative and how long it takes to switch to it.

**People**
- What is the minimum trained staff per shift?
- Which tasks can only one person do? Are there deputies for the dispatch lead and each shift leader?

**Upstream activities**
- **Quality release:** at Site A, dispatch can't start before QA releases the product. Is that the same at Site B? If QA is covered from Site A and the lab is only at Site A, what happens to Site B dispatch when they aren't available? Is there another way to release product?
- **Warehouse, Site B:** what does dispatch need from the warehouse team (picking, stock location, goods receipt)?

**IT systems and data**
- Which warehouse or dispatch system does Site B use? Is it LogiStock, as at Site A? Is it shared with Site A?
- Which other systems are needed (ordering, labels, temperature monitoring, carrier booking)?
- Is there a manual fallback? How long can it run, and at what volume?

**Suppliers and carriers**
- Which carriers serve Site B? Site A depends on NordFrost alone. Is Site B in the same situation?
- Are there contracts or contacts for an alternative chilled carrier?

**Facilities and equipment**
- Chilled storage, refrigeration, dock doors, forklifts, power, labelling and scales.
- If cooling fails, how long does product stay within its temperature limit?

## 7. Links with Site A (5 min)
The Site A list says, for chilled dispatch, "manual export to Site B possible".
1. Is Site B a fallback for Site A dispatch, and did Site B agree to that?
2. How much extra volume could Site B take, and how quickly? Does it have spare capacity in Site A's peak, weeks 49–52?
3. Could Site A take over Site B dispatch?
4. If both sites depend on the same QA lab, carrier or system, one failure stops both, and the fallback fails.

## 8. Current arrangements and history (5 min)
- What workarounds or plans exist today, and have they been tested?
- What disruptions happened in the last two to three years? How long did they last, and what did they cost?
- What one change would most improve resilience?

## 9. Close
- Summarise the ratings, MTPD, RTO and main dependencies, and check them with the interviewee.
- Agree who sends what (contracts, volume figures, system names) and by when.
- Send the notes for review within three working days, then to the site manager, Site B, for approval.

## Open points outside the interview

| # | Point | Ask |
|---|---|---|
| 1 | The Site B org chart is undated and unversioned | HR, Site B |
| 2 | How QA release works for Site B, with the lab only at Site A | QA manager, Site A |
| 3 | What "manual export to Site B" means, and whether Site B agreed to it | Dispatch lead, Site A; BCM manager |
| 4 | Disruption time points (proposed: 4 h, 1 day, 3 days, 1 week) | BCM manager |
| 5 | Who owns the Site B activity list | Site manager, Site B |

---

If you allow writing to the folder, I can save this as `site-b-dispatch-interview-guide.md` or publish it as a shareable page.

**Tool calls (stream-json):**

- Bash: `ls -la && cat *.md`
- Write: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
