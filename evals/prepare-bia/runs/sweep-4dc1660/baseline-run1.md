# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at 4dc1660

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `8029da80-b786-4151-9ab2-de9b2c53e76d`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I couldn't save the guide as a file because this session doesn't have write permission, so here is the full draft. If you want it saved as `site-b-dispatch-interview-guide.md`, allow writes and I'll create it.

Most of it is built on the impact criteria, which are approved. The Site A list only suggested questions (LogiStock, NordFrost, QA release, the manual export to Site B); it isn't treated as fact about Site B. The Site B org chart is an undated draft, so the guide checks it in the interview.

---

# Site B: BIA interview guide, dispatch

Draft, 3 October 2026. Not yet reviewed.

| | |
|---|---|
| Interviewee | Dispatch lead, Site B (consider also inviting one of the three shift leaders) |
| Interviewer / date / location | |
| Duration | 60–75 minutes |
| Scale used | Impact criteria v1.1, 4 Feb 2026 (approved by top management) |

## Sources and how far to trust them

| Source | Status | Use |
|---|---|---|
| Impact criteria v1.1 | Approved | The rating scale, used as it stands |
| Site B organisation structure | Undated HR draft, no version | Roles only; confirm in the interview |
| Site A activity list v3 | Approved, but **for Site A** | Ideas for questions only. Don't copy its peak weeks, carrier, systems or dependencies into the Site B record unless the interviewee confirms them. |

## Before the interview
- Send the interviewee the impact criteria table and the purpose of the interview.
- Ask for Site B's dispatch procedures, shift plans, carrier contracts and customer delivery terms (SLAs).
- Ask the BCM manager at Site A what "manual export to Site B possible" (A2) means in practice.

## 1. Opening (5 min)
- Purpose: find out what Site B dispatch depends on and how fast a stoppage starts to hurt.
- The write-up goes back to the interviewee for confirmation. No rating is final until the interviewee and the site manager approve it.

## 2. Role and organisation (5 min)
1. Is the structure right: site manager → dispatch lead → three shift leaders? Who stands in for you?
2. How many shifts run, on which days, with how many dispatch staff per shift?
3. Which tasks can only one or two people do?

## 3. The activity (10 min)
4. Describe Site B dispatch: what goes in, what comes out?
5. Product types: chilled only, or also frozen or ambient?
6. Typical daily volume (orders, pallets, trucks), and the key accounts served.
7. Which weeks are peak? (Site A's are weeks 49–52 and week 14; don't assume Site B is the same.)
8. Delivery commitments: cut-off times, delivery windows, penalties.

## 4. Dependencies (15 min)
For each area ask: what do you need, who provides it, is there an alternative, and how long can you manage without it?

| Area | Questions |
|---|---|
| Upstream | QA is "covered from Site A" and the only lab is at Site A. How does release work for Site B stock? What happens if Site A QA or the lab is down? |
| IT | Which system do you use: LogiStock or another? Where is it hosted? Can you dispatch on paper, and for how long? |
| Carriers | Which carriers do you use? Is NordFrost one? Is there a second carrier, and is it under contract? |
| Site and equipment | Dock doors, cold storage, temperature monitoring, forklifts, label printers. Which single failure would stop dispatch? |
| People | What is the minimum staff per shift? Can cover come from Site A, an agency or another department? |
| Services | Packaging, pallets, power, refrigeration, security |

**Link with Site A**
9. Site A says its dispatch can do a "manual export to Site B". Does that mean Site B could take over Site A dispatch?
10. If so: how much extra volume, how fast, and what would you need (staff, dock time, carriers, system access)?
11. Could it work the other way: could Site A take over Site B dispatch?

## 5. Impact over time (15 min)
Scenario: Site B dispatch stops completely on a normal working day. Then ask the same for a peak week. At each time point, rate each category from 1 to 3 and note the reason.

| Time since stop | Financial | Customer | Regulatory | Reason |
|---|---|---|---|---|
| 4 hours | | | | |
| 1 day | | | | |
| 3 days | | | | |
| 1 week | | | | |
| 2 weeks | | | | |

Reference (impact criteria v1.1):

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Prompts: How long does chilled stock stay saleable on site? When would the first key account be late, and when would it be at risk of being lost? Would a stoppage lead to a report to the food authority (cold chain, traceability, recall)?

## 6. Recovery targets (10 min)
12. **Maximum tolerable period of disruption:** after how long does the impact become unacceptable? This is usually the first time point rated level 3.
13. **Recovery time objective:** how soon must dispatch be running again at a minimum level? It must be shorter than the answer to question 12.
14. **Minimum level:** what share of normal volume, or which customers, must come first?
15. **Current workarounds** (paper, the other site, another carrier): have they been tested, and when?
16. **Resources needed to recover:** which people, systems, equipment and data, and by when?

## 7. Close (5 min)
- Read back the main dependencies and the provisional ratings.
- Ask who else to interview: the Site B warehouse lead, QA at Site A, IT, carriers.
- Agree a date to confirm the write-up.

## Open points
| # | Point | Owner | Due |
|---|---|---|---|
| 1 | Get a dated, versioned Site B org chart from HR | | |
| 2 | Record QA release from Site A as a cross-site dependency | | |
| 3 | Clarify the dispatch fallback between Site A and Site B with both dispatch leads | | |
| 4 | Check whether Site B relies on a single carrier | | |

---

**Before you use it, note:**
- **I picked the time points (4 h to 2 weeks).** The impact criteria give only daily amounts, not time points. Change them if your BIA method sets its own.
- **The criteria cover only financial, customer and regulatory impact.** There is no category for food safety or reputation, so the guide doesn't add one. Check with whoever owns the criteria whether that gap is intended.

**Tool calls (stream-json):**

- Bash: `ls -la; for f in *.md; do echo "=== $f"; cat "$f"; done`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/baseline/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/baseline/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/baseline/run1/work/site-b-org-chart.md`
- Write: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
