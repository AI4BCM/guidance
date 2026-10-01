# /prepare-bia case 4b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `54ee4b55-892e-42cc-b5f8-6fd2a41a97cc`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I've drafted the questions below, but first you need to confirm which site's dispatch lead you're interviewing. The activity list is for **Site A**, where the dispatch lead owns A2. The org chart is for **Site B**, which has its own dispatch lead with three shift leaders. I've assumed Site A because that's the site the approved activity list covers. Section 5 has questions about Site B, which is the fallback route for dispatch.

---

## BIA interview: Dispatch lead, Site A (activity A2, chilled dispatch)

### 1. Scope and how the activity works
1. In a few sentences, what does chilled dispatch involve, from released stock to truck departure?
2. What volumes do you handle on a normal day, on a peak day in weeks 49–52, and in week 14? What drives the week 14 peak?
3. Which customers or key accounts depend directly on your dispatch? Which have the tightest delivery windows or penalty clauses?
4. Does anything you do fall outside "A2" as the activity list describes it, such as returns, cross-docking or labelling?

### 2. Impact over time (scored against the approved criteria, v1.1)
*Ask for each time point: after 4 hours, 1 day, 2 days, 3 days and 1 week, assuming the outage happens during a peak week.*

5. **Financial:** What would the loss be per day? Is it under €10k, €10k–100k, or over €100k? What makes up that figure: spoiled stock, penalties, lost sales?
6. **Customer:** When does the first customer complain (level 1)? When is a key account late (level 2)? When could a key account be lost (level 3)?
7. **Regulatory:** At what point would a dispatch failure lead to a report to the food authority (level 2)? Could it ever lead to a production stop (level 3), for example through cold-chain breaches or product held beyond shelf life?
8. How much longer can chilled product wait for dispatch before it has to be written off? This is probably the hardest limit on your tolerable downtime.
9. Based on those answers, what is the longest dispatch can be down before the damage is unacceptable (MTPD)? By when must it be running again, even at reduced capacity (RTO)?
10. What is the lowest output that would still be acceptable during a disruption, such as key accounts only or X pallets a day?

### 3. Dependencies
**Upstream: quality release (A3)**
11. Release must happen before dispatch. If the QA lab at Site A is down, can anything be dispatched at all, for example under a positive-release procedure or with an external lab?
12. How long after release does product usually wait before it ships? Is there a buffer?

**IT: LogiStock**
13. What can't you do without LogiStock? Picking, labels, delivery notes, carrier booking?
14. Is there a manual or paper workaround? Has it been used for real, how long could you keep it going, and how much would throughput drop?
15. How much data could you afford to lose, for example the last hour of picks (RPO)?

**Carrier: NordFrost**
16. The activity list shows NordFrost as the only carrier for both receipt and dispatch. Is that accurate? Is there an informal alternative, such as a spot-market chilled haulier, a customer's own collection, or a contract at Site B?
17. If NordFrost failed during week 50, how fast could you get refrigerated capacity elsewhere, and at what cost?

**People and facilities**
18. How many people do you need at minimum to run dispatch? Who are the key people, and who can stand in for them?
19. Are any skills held by only one person, such as LogiStock admin, ADR or cold-chain sign-off, or customer portal access?
20. What equipment and space must be available: chilled loading bays, forklifts, label printers, temperature loggers?

### 4. Existing workarounds and continuity
21. The activity list says "manual export to Site B possible." In practice, how does that work? Who triggers it, what data or stock moves, and how long does it take?
22. Has it been tested or used? When, and what happened?
23. What other incidents have you had, such as IT outages, carrier no-shows or cooling failures? How were they handled, and what went wrong?

### 5. Site B as the fallback
24. Who at Site B do you deal with? (The org chart lists a dispatch lead with three shift leaders.)
25. Could Site B take on Site A's dispatch volume, and how much of it? Do they have spare chilled capacity in weeks 49–52, when they are probably at peak too?
26. QA for Site B is covered from Site A. If Site A is lost entirely, who would release product at Site B?

### 6. Wrap-up
27. What worries you most about dispatch that we haven't covered?
28. Who else should we talk to? (Probably the QA manager for A3, the warehouse lead for A1 and shared NordFrost use, and the LogiStock owner.)

---

### Gaps to check before the interview
- **The Site B org chart is an undated, unversioned HR draft.** Have Site B confirm the names and roles before relying on them for the fallback discussion.
- **The impact criteria have no category for food safety or public health,** which is a significant gap for chilled food. The closest is "Regulatory," and it only covers authority actions. If the interviewee raises product safety risks, write them down separately rather than forcing them into a level.
- **The criteria have no time dimension.** You need to build the impact-over-time table yourself during the interview, as in section 2.
- **The activity list lists only one carrier, NordFrost,** and that dependency is shared with goods receipt (A1). Expect it to be one of the main findings.

I can also put this into a shareable doc or a printable interview template with blank impact-over-time tables.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run3/work/site-b-org-chart.md`
