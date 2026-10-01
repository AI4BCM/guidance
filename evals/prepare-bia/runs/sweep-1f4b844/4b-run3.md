# /prepare-bia case 4b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `68a3961c-da3a-4d1d-870f-bf92c150c1d6`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I've drafted questions for the Site A dispatch lead, who owns activity A2 "Dispatch, chilled". The questions are grouped by BIA stage and point to your files where relevant.

**Which dispatch lead is this?** Your activity list covers Site A only, but the Site B org chart also has a dispatch lead. I've assumed this is the Site A interview. If it's Site B, the questions in section 4 become the main topic. Also, the Site B org chart is an undated HR draft with no version number, so check anything it says before you rely on it.

---

### 1. Confirm the activity (5 min)
1. Does the description of A2 in the approved activity list (v3, 12 March 2026) still match what your team does? Is anything missing, such as returns, cross-docking or labelling?
2. How many people does dispatch need in a normal week, and how many in weeks 49–52? How many of them can do each critical task, for example running LogiStock or loading chilled trucks?
3. The list shows week 14 as a peak as well as weeks 49–52. What causes the week 14 peak (Easter?), and are there other peaks we've missed?

### 2. Impact over time (link to the impact criteria, v1.1)
Hand them the criteria table so they rate against agreed levels rather than gut feel.
4. If dispatch stopped completely, which level would each category reach after 4 hours, 1 day, 3 days and 1 week, in a normal week and in a peak week?
   - Financial: when do daily losses go over EUR 10k (level 2) and over EUR 100k (level 3)?
   - Customer: which key accounts would be late first, and when could one be lost?
   - Regulatory: could a dispatch failure cause a report to the food authority, for example a temperature excursion or recall traceability?
5. What is the longest dispatch could be down before the impact becomes unacceptable (MTPD)? Does the answer change in peak weeks?
6. How soon would dispatch need to be running again (RTO), and at what minimum level (MBCO), e.g. key accounts only or a percentage of normal volume?
7. With chilled goods, how long can finished, released product wait before it has to be written off? Do shelf life and cold-store capacity set the real time limit?

### 3. Dependencies already on record
**LogiStock (warehouse system)**
8. If LogiStock is down, can you dispatch at all? Is there a paper or spreadsheet fallback, and how long could you keep it going?
9. How long can you work without LogiStock data before you lose track of stock or traceability (RPO)?

**Quality release (A3, lab at Site A only)**
10. Product can't be dispatched until it has been released. How long can dispatch wait for QA? Has anything ever been dispatched before release or under positive release?
11. If the Site A lab is out of action, is there any other way to get product released?

**NordFrost (the only carrier recorded)**
12. Is NordFrost really your only chilled carrier? Is there a backup carrier with a contract or framework agreement, and how quickly could they take over?
13. Does the same NordFrost disruption also hit goods receipt (A1)? If so, both activities would fail together.

### 4. Moving dispatch to Site B
The activity list says "manual export to Site B possible".
14. What does "manual export" mean step by step? Who does it, how long does it take, and has it ever been tested or used?
15. Can Site B's three shift leaders take on Site A volumes, especially in weeks 49–52?
16. Site B gets its QA cover from Site A. If Site A is down, who releases product for dispatch from Site B? This may mean the fallback doesn't work.
17. Do LogiStock, the NordFrost contract and your customer agreements cover dispatch from Site B?

### 5. Resources, staff and recovery
18. Which people have skills nobody else has? How long could you manage if they were away, e.g. during flu season in peak weeks?
19. What equipment is critical, such as dock doors, chilled staging areas, label printers and scanners? Are there spares?
20. Which records, contacts or procedures do you need on day one of a disruption, and where are they kept?
21. Have you had any real disruptions in the past two or three years? What happened, and how long did it take to recover?
22. Is there anyone else we should interview, such as the NordFrost account manager, the LogiStock admin or the Site B dispatch lead?

---

**Gaps to resolve after the interview:**
- The impact criteria give only daily amounts, so you'll need to agree time bands (4 h, 1 day and so on) with the BCM manager.
- Site B dispatch relies on Site A QA. This should probably be recorded as a dependency.
- There is no second carrier for A1 or A2.
- HR should provide a versioned and approved Site B org chart.

Would you like this turned into a printable interview template with columns for answers and impact ratings?

**Tool calls (stream-json):**

- Bash: `ls -la && for f in site-a-activity-list.md impact-criteria.md site-b-org-chart.md; do echo "=== $f"; cat "$f"; done`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run3/work/site-b-org-chart.md`
