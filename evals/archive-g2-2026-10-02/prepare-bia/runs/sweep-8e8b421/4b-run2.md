# /prepare-bia case 4b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `719fced3-b923-451d-865f-de4060eb8241`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I've prepared the questions below. The files don't say which site this dispatch lead works at, so check that before you go in:

- The activity list is for **Site A**. Dispatch is activity A2 and the dispatch lead owns it.
- The org chart is for **Site B**. It lists a separate "Dispatch lead, Site B" with three shift leaders. It's also an undated, unversioned HR draft, so it doesn't count as approved input.

I've assumed you're interviewing the **Site A** dispatch lead about A2. The Site B chart still matters, because Site B is the recorded fallback ("manual export to Site B possible"). If you meant the Site B lead, tell me and I'll rewrite the questions for them. Site B has no activity list in these files, so that interview would need to establish the scope first.

---

## BIA interview: Dispatch, chilled (A2), Site A

**Inputs:** Activity list v3 (12 Mar 2026, approved) · Impact criteria v1.1 (4 Feb 2026, approved) · Site B org chart (undated draft, context only)

### 1. Scope and role
1. In your own words, what does chilled dispatch cover, from where it starts to where it ends? (Picking? Loading? Shipping documents?)
2. What are typical daily volumes (orders, pallets, trucks) in a normal week, and in peak weeks 49–52 and week 14?
3. Who covers for you? How many people are needed per shift as a minimum, and what skills or authorisations are scarce?

### 2. Impact over time (use the approved criteria)
The criteria are set per day, so ask about outage lengths in days and use the three columns.

4. If dispatch stopped completely, what happens after **4 hours, 1 day, 3 days and 1 week**?
   - **Financial:** at what point do losses pass EUR 10k a day (level 2) and EUR 100k a day (level 3)? What drives the cost: spoiled stock, penalties, lost sales?
   - **Customer:** who are the key accounts? When would a key account be late (level 2), and when would one be lost (level 3)?
   - **Regulatory:** at what point would a report to the food authority be needed (level 2)? Could anything lead to the authority stopping production (level 3), for example cold-chain breaks or temperature records you can't trace?
5. How do these answers change in peak weeks? Is there any time of year when an outage would hurt much less?
6. How long do finished chilled products last on site before they have to be dispatched or written off? This usually sets the limit.

### 3. Recovery targets
7. What is the longest dispatch can be down before the impact becomes unacceptable (maximum tolerable period of disruption)?
8. What is the minimum service you'd need to restore first (key accounts only? a percentage of volume?), and by when?
9. Is that answer different in peak weeks?

### 4. Dependencies
**LogiStock (warehouse system)**
10. What happens to dispatch if LogiStock is down? Can you pick, load and produce shipping documents without it?
11. "Manual export to Site B possible": what exactly does that mean? Who does it, how long does it take, how much volume can Site B absorb, and has it ever been done or tested?
12. How much data can you afford to lose (orders, stock positions, temperature records)?

**Quality release (A3)**
13. Dispatch depends on QA release, and the lab is only at Site A. If QA or the lab is unavailable, is there any release route at all, or does dispatch stop?
14. QA for Site B is also covered from Site A. Does that put Site B in competition for the same QA capacity during an incident?

**NordFrost (carrier)**
15. NordFrost is the only carrier recorded for A1 and A2. Is that true in practice? Do you have contacts, contracts or rates with any alternative chilled carrier?
16. How quickly would you notice a NordFrost failure, and how long could you hold stock while you find a replacement?

**Premises and equipment**
17. What do you need physically: dock doors, chilled staging areas, forklifts, label printers, scanners? Which of these has no backup?
18. Could dispatch run from Site B's dock if Site A's dock were unavailable? What would stop it?

**Other**
19. Is anything you rely on missing from the activity list (IT outside LogiStock, temperature monitoring, customer portals, Goods receipt (A1) feeding you stock)?

### 5. Current workarounds and history
20. What workarounds exist today, and are they written down? How long could each one be sustained?
21. Describe the last real disruption to dispatch: what happened, how long it lasted, and what it cost.

### 6. Close
22. Is there anything that worries you that we haven't covered?
23. Confirm: will you review the write-up, and who else should we talk to (shift leaders, QA, NordFrost account manager)?

---

**Gaps in the inputs to raise afterwards:**
- There is no Site A org chart.
- The Site B chart is an unapproved draft, so don't rely on it for role names.
- The impact criteria have no health and safety or food safety column. For chilled food, harm to consumers is arguably the main impact. You may want to ask the BCM manager whether that's deliberately covered under "Regulatory".
- "Key account" isn't defined anywhere. Questions 4 and 8 depend on it, so get the list before the interview if you can.

I can also turn this into a shared doc you can fill in during the interview.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run2/work/site-b-org-chart.md`
