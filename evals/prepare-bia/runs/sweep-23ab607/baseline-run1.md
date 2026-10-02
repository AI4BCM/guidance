# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `5bfab522-5fb9-4321-a950-c2a2e1ba4d8d`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I couldn't save a file because write access is blocked in this session, so the full draft is below. You can paste it into `site-b-dispatch-interview-guide.md` next to the other files.

The Site A list is approved but describes only Site A. The guide uses it to frame questions, not as facts about Site B. The Site B org chart is an undated draft, so the guide confirms it at the start of the interview. The impact scale is the approved v1.1 criteria, unchanged.

---

# Site B: BIA interview guide, dispatch

Draft, 3 October 2026. Not reviewed. Owner: to be confirmed (the Site B documents name no BCM manager).

## 1. Interview set-up

| Item | Plan |
|---|---|
| Activity | Dispatch, Site B |
| Interviewee | Dispatch lead, Site B |
| Optional attendee | One of the three shift leaders, to cover shift handover, minimum staffing and the workarounds used on the floor |
| Duration | 90 minutes |
| Interviewer / note-taker | to be confirmed |
| Send in advance | Section 3 (impact scale) and the questions in sections 5–8, so the interviewee can bring figures |
| Ask the interviewee to bring | Weekly volumes for the last 12 months, the key-account list, carrier contracts, any existing fallback or paper procedures |

## 2. What we know before the interview, and how reliable it is

| Source | Status | How to use it |
|---|---|---|
| Impact criteria v1.1, 4 Feb 2026 | Approved by top management | Use it to rate every impact. Don't change it in the interview. |
| Site B org chart | Undated HR draft, no version | Confirm roles at the start (section 4). Treat it as unconfirmed until then. |
| Site A activity list v3, 12 Mar 2026 | Approved, but **for Site A only** | Use it only to prepare questions. Nothing in it applies to Site B until the interviewee confirms it. |

Five points from Site A to test at Site B:

- **Quality release comes from Site A.** QA at Site B is "covered from Site A", and at Site A dispatch has to wait for quality release (A2 depends on A3). If Site B dispatch also waits for the Site A lab, a failure at Site A stops Site B too.
- **Single carrier.** Site A uses only NordFrost and has no second carrier. Check whether Site B uses NordFrost as well.
- **Warehouse system.** Site A dispatches through LogiStock. Check which system Site B uses and whether it shares Site A's installation.
- **Site B as Site A's fallback.** Site A's list says its dispatch can be manually exported to Site B. Check whether Site B knows about this, has agreed to it, and has the capacity.
- **Peak weeks.** Site A peaks in weeks 49–52 and week 14. Check Site B's own peaks.

## 3. Impact scale (from the approved criteria, v1.1)

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

The overall rating at each time point is the highest level reached in any column.

## 4. Opening (10 min)

1. Explain the purpose: to find out how quickly a dispatch outage at Site B causes damage, what dispatch needs to run, and the minimum it must keep doing. This is not an audit.
2. Check the draft org chart:
   - Do you report to the site manager?
   - Are there three shift leaders? How many shifts a day, how many days a week?
   - Who does QA for Site B today, and where are they based?
   - Is the warehouse team separate from dispatch? Where does the warehouse hand goods over to dispatch?
3. Who stands in for you when you're away?

## 5. The activity (15 min)

1. Describe dispatch at Site B: what goes out, to whom, and how.
2. Which products? Are they all chilled? How much shelf life is left after release?
3. Typical daily and weekly volumes (orders, pallets, trucks). What is the most you have dispatched in one day?
4. Which customers are key accounts? What share of volume do they take?
5. What are your peak weeks? Are they the same as Site A's (weeks 49–52 and week 14)?
6. Are there contract penalties or service levels for late or missed deliveries? With which customers?

## 6. Impact over time (25 min)

Scenario: **dispatch at Site B cannot run at all, starting at the worst time of year.** If the answers would differ a lot in a normal week, repeat the questions for a normal week.

At each time point, ask "what has happened by now?" and rate it on the section 3 scale. Write down the reason as well as the level.

| Time without dispatch | Financial (level + reason) | Customer (level + reason) | Regulatory (level + reason) | Overall |
|---|---|---|---|---|
| 4 hours | | | | |
| 1 shift | | | | |
| 1 day | | | | |
| 2 days | | | | |
| 3 days | | | | |
| 1 week | | | | |
| 2 weeks | | | | |

Prompts:
- When does chilled stock that is ready to ship start to expire? Is it then lost, or can it be sold elsewhere?
- When does a key account first notice? When does it start looking for another supplier?
- At what point would you have to report to the food authority (for example, a cold-chain break or stock disposal)?
- Does production at Site B have to stop when dispatch stops because there's nowhere to put the stock? When?

Then agree these with the interviewee:

| Measure | Question | Answer |
|---|---|---|
| Maximum tolerable period of disruption (MTPD) | After how long would the damage become unacceptable? | |
| Recovery time objective (RTO) | By when must dispatch be running again, at least at the minimum level? It must be shorter than the MTPD. | |
| Minimum level (MBCO) | What must still go out: which customers, which products, what share of volume? | |
| Data loss (RPO) | If the system loses data, how far back can you accept losing (orders, delivery notes, temperature records)? | |

## 7. What dispatch needs (25 min)

For each resource, ask what you need, how much you need at the minimum level, who provides it, and what happens if it is unavailable.

**People.** How many staff per shift at normal level, and at the minimum level? Which tasks can only one or two people do? Are licences needed (drivers, forklifts)? Could warehouse or Site A staff step in?

**IT and data.** Which dispatch system do you use? Is it LogiStock, and does it share Site A's installation? What else do you rely on: label printing, transport booking, customer portals, EDI, temperature logging? Can you dispatch without the system (on paper or spreadsheets)? Has anyone tried it?

**Buildings and equipment.** How many dock doors? How much chilled buffer space is there, and how long can stock stay in it? What depends on power or refrigeration? Is there a backup generator?

**Upstream (internal).** Who releases goods for dispatch? Is it the Site A lab? How does the release reach you, and how long does it take? If Site A can't release, can anything be released at Site B? What does the Site B warehouse have to do before dispatch can start?

**External suppliers.** Which carriers do you use? Is NordFrost one of them? Is there a second carrier, and could it take over within the RTO? Do you depend on any other supplier (packaging, pallets, cooling units, IT support)?

**Downstream.** Who depends on dispatch: customers directly, distribution centres, Site A?

## 8. Existing workarounds and the link to Site A (10 min)

1. What do you do today if the system fails, a carrier doesn't turn up, or a dock door breaks? Is it written down?
2. Site A's records say its dispatch can be exported manually to Site B. Do you know about this arrangement? Who agreed to it? How much extra volume could you take, and for how long, especially in weeks 49–52?
3. Has a disruption like this happened in the last two years? What happened, and what did it cost?

## 9. Close (5 min)

1. Read back the MTPD, RTO, minimum level and main dependencies, and correct them on the spot.
2. Ask who else to interview (for example the Site A QA manager, the warehouse lead, IT).
3. Agree when the interviewee will get the notes to check, and who approves the result (the site manager?).

## 10. Open points

- Who owns the BIA at Site B? The Site B documents name no BCM manager.
- The Site B org chart is an undated draft. Ask HR for a current, versioned copy.
- The criteria give financial impact per day but don't say how to rate losses over several days. Agree with the BCM owner whether to rate on the daily rate or the total, so every interview is rated the same way.
- Apart from the regulatory column, the criteria don't cover food-safety or health effects. If the interview turns any up, note them and raise them with the criteria owner instead of rating them on the spot.
- If Site B dispatch depends on Site A's quality release, the Site A QA interview (activity A3) should also cover what Site B needs.

---

To fill in from the interview: the RTO, MTPD, minimum level and data-loss limit; the actual Site B system and carriers; and whether Site B depends on Site A for quality release. Section 2 shows where each starting assumption came from.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/baseline/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/baseline/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/baseline/run1/work/site-b-org-chart.md`
- Write: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
