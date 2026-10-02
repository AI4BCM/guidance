# prepare-bia baseline (no skill loaded), run1: Claude Code, guidance at 5ec8f40

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9ba37358-af73-4380-8382-0139b5ec9c7b`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I couldn't save the guide to the folder because file writes are blocked in this session, so the full draft is below. You can paste it into `site-b-dispatch-interview-guide.md`.

---

# Site B: BIA interview guide, dispatch (chilled)

Draft 0.1, 3 October 2026. Status: draft, not reviewed. Owner: BCM manager (to be confirmed).

## Purpose and scope

This guide is for the business impact analysis (BIA) interview on the dispatch activity at Site B. The interview should produce:

- a description of the activity and its peak periods
- how the impact of an outage grows over time, scored against the approved impact criteria
- the maximum tolerable period of disruption (MTPD), the recovery time objective (RTO) and the minimum level of service the activity has to keep (MBCO)
- dependencies on people, IT, premises, suppliers and other activities
- the workarounds that exist today and the resources needed to recover

Out of scope: goods receipt and warehousing at Site B. These get a separate interview with the warehouse lead.

## Interviewees

| Role | Why | Status |
|---|---|---|
| Dispatch lead, Site B | Owns the activity | To invite |
| One of the three shift leaders (optional) | Knows how shifts run and what is done by hand | Ask the dispatch lead who |

Allow 90 minutes. Send the impact scale at least two days before the interview.

## Sources and how far to trust them

| Source | Version and status | Use here |
|---|---|---|
| Impact criteria | v1.1, 4 Feb 2026, approved by top management | Binding scale for scoring |
| Site A activity list | v3, 12 Mar 2026, approved by the Site A site manager | Reference only. It shows what to ask; it is **not** evidence of how Site B works |
| Site B organisation structure | Undated HR draft, no version | For the invitation only. Confirm the roles in the interview |

Don't copy Site A answers into the Site B record. Every Site A detail below is something to check, not a fact about Site B.

## Before the interview

- [ ] Confirm with HR or the Site B site manager that the organisation draft is current.
- [ ] Ask the Site A QA manager how Site B goods are released today. The Site A list says the lab is at Site A only, and the org chart says QA for Site B is covered from Site A.
- [ ] Ask the Site A dispatch lead what "manual export to Site B possible" means in practice. Is Site B a fallback for Site A dispatch?
- [ ] Check whether the NordFrost contract covers Site B.

## Impact scale (approved, v1.1)

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Score each category separately. The overall level for a time step is the highest of the three.

## Questions

### 1. The activity
1. What does dispatch at Site B cover, from released goods to the truck leaving?
2. What volumes do you handle (orders, pallets or trucks a day), normally and at peak?
3. Which customers do you serve, and which are key accounts?
4. Which cut-off times do you work to (delivery slots, carrier pick-ups)?
5. Are you the activity owner? Who stands in for you?

### 2. Peaks and timing
1. When are your peak weeks? (Site A: weeks 49–52 and week 14. Is Site B the same?)
2. When in the day or week would an outage hurt most?
3. What is the shelf life of the goods you dispatch? How long can they wait before they have to be written off?

### 3. Impact over time
Scenario: dispatch at Site B stops completely at the start of a peak week.

| Time since outage | What happens? | Financial | Customer | Regulatory | Overall |
|---|---|---|---|---|---|
| 4 hours | | | | | |
| 1 day | | | | | |
| 2 days | | | | | |
| 3 days | | | | | |
| 1 week | | | | | |

Prompts: How much do you lose per day in revenue, write-offs, penalties or extra cost? When is a key account late, and when could one be lost? At what point would we have to report to the food authority (for example, a broken cold chain or goods held past their date)? Repeat the scenario for an off-peak week if the answers would differ a lot.

### 4. Recovery objectives
1. After how long would the impact become unacceptable? (MTPD)
2. By when must dispatch be running again, even in a reduced form? (RTO)
3. What is the minimum service you must keep: which customers, which products, what share of normal volume? (MBCO)
4. How long could you run at that minimum level?

Check that the RTO is shorter than the MTPD and that both fit the impact table.

### 5. Dependencies
**Other activities**
1. Goods can only leave after quality release. Who releases Site B goods, and where? If Site A is down, can Site B still dispatch?
2. How does dispatch depend on the Site B warehouse (picking, cold storage)?
3. Does Site B take over Site A dispatch when Site A is down? If so, how much extra volume could you handle, and for how long?

**People**
1. How many staff per shift do you need normally, and at minimum?
2. Are there tasks only one person can do (system administration, carrier booking, export papers)?
3. Can staff from other sites or temporary staff step in? How much training would they need?

**IT and data**
1. Which systems do you use? Is it LogiStock, as at Site A?
2. Where are they hosted, and who supports them?
3. Without the system, what can you still do (paper picking lists, manual export, phone orders), and for how long?
4. Which data do you need to restart (open orders, stock, delivery addresses)?

**Premises and equipment**
1. How many dock doors and chilled loading areas do you have? What happens if one is out of use?
2. Which equipment is critical (cooling, forklifts, label printers, scales)?

**Suppliers and carriers**
1. Which carriers do you use? Is it NordFrost only? (Site A has no second carrier recorded.)
2. Do you have a contract with, or know of, an alternative chilled carrier? How quickly could they start?
3. Which other suppliers are critical (packaging, pallets, cooling service)?

### 6. Current workarounds
1. Has dispatch been disrupted before? What happened, and how did you cope?
2. Which workarounds exist today? Are they written down and tested?
3. How long could each one run, and at what share of normal volume?

### 7. Resources needed up to the RTO

| Resource | Minimum needed | Source | Notes |
|---|---|---|---|
| Staff per shift | | | |
| IT systems and access | | | |
| Dock doors / chilled space | | | |
| Equipment | | | |
| Carrier capacity | | | |
| Other | | | |

### 8. Close
1. Is there anything we haven't asked that could stop or slow dispatch?
2. Which documents should we see (procedures, carrier contracts, SLAs, shift plans)?
3. Agree a date for the interviewee to review the write-up.

## After the interview
- [ ] Write up the results within three working days and send them for review.
- [ ] Record the dependencies on Site A (quality release, any fallback for Site A dispatch) and tell the Site A BCM owner.
- [ ] Log single points of failure (one carrier, one system, one person) as risks to treat.
- [ ] Ask HR for a dated, versioned Site B organisation chart.

---

**Things you should know before using it:**
- **No Site B facts in the inputs:** The files give nothing about Site B dispatch beyond the roles. Peak weeks, LogiStock and NordFrost come from Site A, so the guide asks about each one instead of assuming it.
- **Possible key finding:** QA for Site B is covered from Site A, and the lab exists only at Site A. If Site A goes down, Site B dispatch could stop too. The guide asks about this directly.
- **Org chart reliability:** The Site B org chart is an undated draft, so confirm the dispatch lead's name and role before you send the invitation.
- **My choices:** The time steps (4 hours to 1 week), the 90-minute length and the three-day write-up are my suggestions, not taken from your files. Adjust them to your BIA method.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/baseline/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/baseline/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/baseline/run1/work/site-b-org-chart.md`
- Write: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65/runs/prepare-bia/baseline/run1/work/site-b-dispatch-interview-guide.md`
