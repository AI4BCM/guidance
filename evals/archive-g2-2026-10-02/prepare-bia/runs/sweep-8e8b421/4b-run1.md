# /prepare-bia case 4b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3fe38143-ee2e-4d58-b483-aee5c59ada83`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I've put together questions for the Site A dispatch lead. Before you use them, you need to confirm which dispatch lead you're interviewing. The activity list covers Site A only: dispatch is A2 there, and it's approved (version 3). The org chart covers Site B and names a separate "Dispatch lead, Site B". That chart is an undated, unversioned HR draft. If you're interviewing the Site B lead, use section 7 and treat what the org chart says as unconfirmed.

## BIA interview: Dispatch lead (activity A2, chilled dispatch)

**1. Scope and confirmation**
- The activity list describes A2 as "Dispatch, chilled", using LogiStock. Is that still accurate? What does dispatch actually include (picking, loading, paperwork, route planning)?
- Which customers and key accounts do you supply? Which of them are hardest to keep happy when deliveries are late?
- Do you have any delivery commitments with set times or penalties (contracts, SLAs)?

**2. Peak periods**
- The list gives weeks 49–52 and week 14 as peaks. Is that right? What drives week 14?
- How much busier are you at peak (volumes, number of trucks a day)?
- Would an outage in week 50 hurt more than the same outage in a normal week? By how much?

**3. Impact over time**
Our impact criteria are measured per day and have no time steps, so you need to build the timeline in the interview. Ask for each point in time: 4 hours, 1 day, 2–3 days, 1 week.
- **Financial:** what does a lost dispatch day cost? Is it under €10k, €10k–100k, or over €100k a day? Does the cost grow with each day, or jump once stock is too old to sell?
- **Customer:** when is a key account late (level 2)? When could you lose one (level 3)?
- **Regulatory:** could a dispatch outage lead to a report to the food authority (level 2)? Could it lead to production being stopped (level 3), for example through cold chain breaks or traceability gaps?
- What's the longest dispatch can stop before the damage is unacceptable? That gives you the maximum tolerable period of disruption (MTPD). After that, what minimum service level would you need, and how soon? That gives you the recovery time objective (RTO) and the minimum level of service.

**4. Dependencies**
- **Quality release (A3):** nothing can ship before QA releases it, and the lab is at Site A only. What happens if the lab or the QA staff aren't available? Can anyone else release product, or can you hold stock without a release?
- **NordFrost:** no second carrier is recorded for receiving or dispatch. Is that true? Have you ever used another carrier? How long would it take to bring one on board?
- **LogiStock:** what stops if the system goes down? Can you dispatch on paper? How long could you keep that up, and how would you enter the data afterwards?
- **People:** how many people do you need at minimum to run dispatch? Which skills only one or two people have (for example LogiStock know-how or carrier booking)? Who stands in for you?
- **Facilities:** do you share the two dock doors with goods receiving? How much chilled storage do you have, and how many hours of buffer does it give you?
- Any other dependencies: suppliers of packaging, labels or pallets, power, refrigeration, or IT links to customers (EDI orders, delivery notices)?

**5. Workarounds and fallback to Site B**
- The list says "manual export to Site B possible". What does that mean in practice? Exporting data, moving goods, or both?
- Has it ever been tested or used? How long does it take, and what share of volume could Site B handle, especially at peak?
- Site B has no QA of its own; Site A provides it. Doesn't that mean the fallback still depends on the Site A lab?

**6. Records and recovery**
- What records does dispatch need to keep for traceability and temperature, and where are they kept?
- After an outage, how long would it take to clear the backlog?
- Has dispatch been disrupted before? What happened, and what worked?

**7. If you're interviewing the Site B dispatch lead**
- Is the org chart accurate: three shift leaders, a warehouse lead, and QA from Site A?
- What does Site B dispatch do in normal operations? Is it on the activity list at all, given there's no Site B list among these files?
- Could Site B actually absorb Site A's dispatch: capacity, LogiStock access, NordFrost coverage?

### Gaps to raise with the BCM manager afterwards
- The impact criteria have no time scale and no category for food safety or cold chain. That's a notable gap for chilled food.
- None of these files says anything about Site B activities. The org chart needs a version and an approval before you rely on it.

I can also turn this into a shared doc or an interview template with columns for notes and answers if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run1/work/site-b-org-chart.md`
- Glob: `**/*`
