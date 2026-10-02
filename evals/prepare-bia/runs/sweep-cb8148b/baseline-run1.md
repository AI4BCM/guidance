# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at cb8148b

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a782e340-f751-4c96-907e-9d5f7eccc181`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I couldn't save the guide to the folder because writing files isn't allowed in this session, so the full draft is below. To save it, allow writes and I'll create `site-b-dispatch-interview-guide.md`, or copy it from here.

Three things to know before you use it:

- **Unconfirmed sources.** There is no Site B activity list, and the Site B org chart is an undated draft with no version. The guide relies on Site A only to compare and to find links between the sites, and asks you to confirm the org chart first.
- **Links between the sites.** The guide turns these into "points to test": QA release from the Site A lab, the "manual export to Site B" fallback for Site A dispatch, NordFrost as the only carrier, and the LogiStock warehouse system. If both sites share any of these, one failure could stop dispatch at both sites at once.
- **Gaps in the impact criteria.** The approved criteria give no time points for rating impact. They also don't say how to combine the financial, customer and regulatory ratings, and they don't cover food safety. I used 4 hours, 1 day, 3 days and 1 week as a proposal and took the highest of the three ratings as the overall rating. Both choices need your sign-off.

---

# Site B: BIA interview guide, dispatch

Version 0.1, 2 October 2026. Status: draft, not yet reviewed. Owner: BCM manager (to be confirmed for Site B).

| | |
|---|---|
| Interviewee | Dispatch lead, Site B |
| Optional | One of the three shift leaders (ideally the one covering the busiest shift) |
| Interviewer | BCM manager |
| Duration | 90 minutes |
| Output | Activity entry for Site B dispatch (proposed ID: B2, to mirror A2), impact rating, dependencies, recovery requirements |

## Sources and their status

| Source | Status | What it gives us | Caution |
|---|---|---|---|
| impact-criteria.md | v1.1, approved by top management | The scale for rating impact | Use as is; do not change the levels in the interview |
| site-a-activity-list.md | v3, approved by the Site A site manager | Comparison point and links between the sites | Covers Site A only. Do not assume Site B works the same way |
| site-b-org-chart.md | Undated HR draft, no version | Interviewee and reporting line | Confirm it is current before relying on it |

There is no Site B activity list yet. This interview produces its first dispatch entry.

## Before the interview

- [ ] Confirm with HR or the Site B site manager that the org chart is current and that the dispatch lead is the right owner.
- [ ] Send the interviewee the impact criteria table and the questions in sections 3 and 4 in advance, so they can bring figures.
- [ ] Ask them to bring: daily dispatch volume (normal and peak), the key accounts served from Site B, revenue per day if known, and the current shift pattern.
- [ ] Agree the time points for the impact table (section 3). The approved criteria do not define any; this guide proposes 4 hours, 1 day, 3 days and 1 week.

## Points to test

Each of these comes from the sources and needs to be confirmed or corrected by the interviewee.

1. **QA release comes from Site A.** The org chart says Site A covers QA for Site B, and the Site A list says the only lab is at Site A. If Site B cannot dispatch without a release from that lab, Site B dispatch depends on A3. A lab outage at Site A would then stop dispatch at both sites.
2. **Site B as the fallback for Site A dispatch.** The Site A list notes "manual export to Site B possible" for A2. Find out whether Site B knows about this, has agreed to it and has the capacity, especially in weeks 49–52 when both sites may be at peak.
3. **Carrier.** Site A relies on NordFrost and has no second carrier. If Site B also uses NordFrost, a NordFrost failure stops both sites, and the fallback in point 2 fails at the same time.
4. **Warehouse system.** Site A uses LogiStock. Confirm whether Site B uses the same system or the same instance. If it does, a LogiStock outage also stops both sites.
5. **Peak periods.** Site A dispatch peaks in weeks 49–52 and week 14. Confirm Site B's own peaks.

## Questions

### 1. The activity (10 min)

- In your own words, what does dispatch at Site B cover, from where to where?
- What does a normal day look like: volume, number of loads, departure times, cut-offs?
- Which customers or key accounts do you serve? Which of them are served only from Site B?
- What is the one output that must not stop?

### 2. Timing and peaks (5 min)

- When are your peak weeks, days and hours?
- Are there fixed delivery windows with customers? What happens if a window is missed?
- How long can chilled product wait at Site B before it has to be written off?

### 3. Impact over time (25 min)

Walk through the scenario "dispatch at Site B stops completely" at each time point, first for a normal week, then for a peak week. For each cell, ask for the facts first, then rate them against the approved impact criteria.

| Time since stop | Financial (EUR a day) | Customer | Regulatory | Highest level |
|---|---|---|---|---|
| 4 hours | | | | |
| 1 day | | | | |
| 3 days | | | | |
| 1 week | | | | |

Reference, impact criteria v1.1:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Prompts:

- At what point would a key account be late? At what point might one be lost?
- At what point would product have to be destroyed, and would that need a report to the food authority?
- Does a peak week change the answer? By how much?

### 4. Recovery requirements (15 min)

- **Maximum tolerable period of disruption:** after how long would the impact become unacceptable? (Usually the point where it reaches level 3.)
- **Recovery time objective:** by when must dispatch be running again, at least at a minimum level?
- **Minimum level:** what is the smallest volume, or which customers, must be served to keep the impact at level 1 or 2?
- Which of these answers change in peak weeks?

### 5. Dependencies (20 min)

For each dependency, ask: what is it, who provides it, what happens if it fails, is there an alternative, and how long can you manage without it?

| Type | Prompts | Answer |
|---|---|---|
| People | How many staff per shift at minimum? Who can stand in for you and for each shift leader? Are any skills held by one person only? | |
| Upstream, internal | Does every load need QA release from Site A (point 1)? Does dispatch depend on Site B goods receipt or the warehouse lead? | |
| IT | Which systems do you use (LogiStock? point 4)? What can you do on paper if a system is down, and for how long? | |
| Facilities and equipment | Cold store, dock doors, loading equipment, backup power and refrigeration? | |
| External suppliers | Which carriers (NordFrost? point 3)? Is a second carrier under contract or only known? Packaging or other consumables? | |
| Downstream | Who relies on your output, inside and outside the company? | |

### 6. Workarounds and Site A (10 min)

- What do you do today when dispatch is disrupted? Has it happened? What did you learn?
- Could Site A take over Site B dispatch, or part of it?
- Do you know about the option for Site A to export dispatch manually to Site B (point 2)? Has anyone agreed it with you? How much extra could you take, in a normal week and in weeks 49–52?

### 7. Close (5 min)

- Is there anything we have not asked about that would stop dispatch?
- Who else should we talk to (for example the Site B warehouse lead or the Site A QA manager)?
- Agree when the interviewee will review the written entry.

## After the interview

- [ ] Write up the Site B dispatch entry in the same format as the Site A list (activity, owner, peak weeks, notes, dependencies).
- [ ] Send it to the dispatch lead for review, then to the Site B site manager for approval.
- [ ] Pass findings that affect both sites (points 1–4) to the BCM manager, Site A, as they may change the Site A list.

## Open points for the BCM manager

These are outside the interview but affect how its results are used.

- **Time points.** The approved impact criteria give no time points for the impact table. The 4 hours / 1 day / 3 days / 1 week proposed here should be agreed so that all sites rate on the same basis.
- **Combining dimensions.** The criteria do not say whether the overall rating is the highest of the three dimensions. This guide assumes it is.
- **Food safety.** The criteria have no health or food-safety dimension; Regulatory covers it only indirectly. For a chilled food business, this may need raising with top management.
- **Site B BCM owner.** The Site A list is owned by the BCM manager, Site A. No owner is named for Site B.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/baseline/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/baseline/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/baseline/run1/work/site-b-org-chart.md`
- Write: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
