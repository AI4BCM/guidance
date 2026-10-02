# /prepare-bia case 4b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2c7da4b5-0f40-481c-add8-269fb5586ea0`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I've put the question set together below. First, though: the files don't say which dispatch lead you mean. The activity list covers **Site A**, but the only org chart is for **Site B**, which has its own dispatch lead. I wrote the questions for the Site A dispatch lead, who owns activity A2. I used the Site B chart only where Site B is the fallback for Site A. If you're actually interviewing the Site B dispatch lead, tell me and I'll rework it. There's no Site B activity list, so that interview would mostly be about finding Site B's activities.

---

## BIA interview: Dispatch lead, Site A (activity A2, chilled dispatch)

**Sources:** Site A activity list v3 (12 Mar 2026, approved), impact criteria v1.1 (4 Feb 2026, approved), Site B org structure (undated HR draft, not approved).

### 1. Confirm the scope (5 min)
1. Is "Dispatch, chilled" one activity or several (picking, loading, paperwork, carrier handover)? Should any of them be scored separately?
2. The list gives weeks 49–52 and week 14 as peaks. What drives week 14? How much higher is the volume then than in a normal week?
3. Are there any other peaks, such as promotions or key-account cut-offs, that aren't on the list?

### 2. Impact over time
Use the approved scales: financial levels 1–3 (under €10k, €10k–100k, over €100k a day), customer and regulatory. Ask about a normal week and a peak week separately.

4. If dispatch stops completely, what happens after 4 hours, 1 day, 2 days and 1 week?
   - Revenue lost or delayed per day: which financial level is that?
   - When is a key account late (customer level 2)? When could one be lost (level 3)?
   - Is there a point where chilled stock has to be written off? After how many hours does that happen?
   - Could a stoppage cause a report to the food authority (regulatory level 2), for example over cold-chain breaks or traceability?
5. What is the longest outage you could tolerate before the impact becomes unacceptable (MTPD)? Is the answer different for a peak week and a normal week?
6. By when does dispatch have to be running again, and at what minimum level (RTO and minimum service level, e.g. % of orders or key accounts only)?

### 3. Dependencies already recorded (verify them)
7. **Quality release (A3):** Nothing ships before QA release, and the lab exists only at Site A.
   - What happens to dispatch if the lab is down?
   - Is there an emergency release or a positive-release procedure?
8. **NordFrost:** No second carrier is recorded for A1 or A2.
   - Is that true?
   - Do you have any backup carrier, framework contract or spot-market option? How fast could one start, and at what cost?
9. **LogiStock:**
   - What happens to dispatch if LogiStock is down?
   - Can you dispatch manually (paper picking lists, delivery notes, labels)? For how long?
   - How much data could you lose without a problem?

### 4. Dependencies that may be missing
10. Which people or roles are critical? How many people are needed at minimum, and do any of them have knowledge only they hold?
11. Which facilities and equipment do you need: dock doors (shared with A1?), cold storage, forklifts, label printers, power for refrigeration?
12. Which other IT do you rely on: EDI with customers, carrier booking, temperature logging, email/phone?
13. Which suppliers do you need besides NordFrost: packaging, pallets, dry ice or cooling materials?

### 5. Workaround via Site B
The activity list says "manual export to Site B possible".

14. What does "manual export" actually mean? Is it the data, the goods, or both?
15. Has it ever been done or tested? How long does it take to start, and what share of volume could Site B take, including in peak weeks?
16. Site B has its own dispatch lead with three shift leaders. Is there an agreement in place, and who would you call?
17. QA at Site B is covered from Site A. If Site A is down, who releases goods for dispatch at Site B?

### 6. Close
18. What past incidents or near misses have you had? How long did they last and what did they cost?
19. Who else should we interview, and which documents should we get (SOPs, carrier contracts, customer SLAs)?
20. Read back the agreed MTPD, RTO and minimum level, and confirm them before you end the interview.

---

**Points to raise with the BCM owner, not the interviewee:**
- The impact criteria have no time thresholds. Agree the time intervals in Q4 before the interview so results can be compared across activities.
- The Site B org chart is an undated draft. Confirm the Site B roles before relying on Site B as the fallback.

Would you like this as a shareable document or a printable interview sheet with space for notes?

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run1/work/site-b-org-chart.md`
