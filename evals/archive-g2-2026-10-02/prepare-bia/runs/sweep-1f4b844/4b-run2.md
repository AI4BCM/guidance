# /prepare-bia case 4b, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `de67b45e-b00e-43dc-8596-a5f00e505a65`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I've read all three files and drafted a set of questions. Two things need sorting out first, because they change who you interview and how much you can rely on the files.

## Check before the interview

1. **Which dispatch lead?** The Site A activity list gives activity A2 (chilled dispatch) to a "Dispatch lead". The Site B org chart also has a "Dispatch lead, Site B" with three shift leaders under them. Since the activity list is the approved scope, I've assumed you mean the **Site A** lead. If it's the Site B lead, the questions in section 5 become the main ones.
2. **The Site B org chart isn't reliable yet.** It's an undated, unversioned HR draft. The activity list (v3, approved) and the impact criteria (v1.1, approved by top management) are fine to rely on. Anything you take from the Site B chart should be checked in the interview, not assumed.

## Interview questions: Dispatch, chilled (A2)

**1. Scope and role**
- Is the A2 description still correct: chilled dispatch, run on LogiStock, with peaks in weeks 49–52 and week 14?
- What causes the week 14 peak (Easter?), and how much bigger than normal is each peak in volume or loads per day?
- Who stands in for you, and is that written down anywhere?

**2. How the impact grows over time** (use the approved criteria as the scale)
- If dispatch stopped completely, what would happen after 4 hours, 1 day, 3 days and 1 week?
- When would daily losses pass EUR 10k (level 2), and when would they pass EUR 100k (level 3)?
- Which key accounts would be late first? When would a key account be at risk of leaving (customer level 3)?
- Chilled stock has limited shelf life. When does held product have to be written off, and does that make the financial impact jump?
- Could a dispatch outage cause a report to the food authority (regulatory level 2)? For example a cold-chain break or a traceability gap.
- Does any of this change in peak weeks? Ask for a separate answer for weeks 49–52.

**3. Recovery targets**
- What is the longest dispatch can be down before the damage is no longer acceptable (maximum tolerable period of disruption)?
- By when does it need to run again, and at what minimum capacity (for example 50% of normal loads)?
- How much LogiStock data can you afford to lose, such as orders or picking status (recovery point objective)?

**4. Dependencies**
- **QA release (A3):** Dispatch can't ship before QA release, and the lab exists only at Site A. If QA is late or the lab is down, how long until dispatch stops? Is there any conditional or remote release?
- **NordFrost:** The list shows no second carrier for A1 or A2. Is that true? Do you have a fallback carrier, a contract or rates, and how quickly could they take loads?
- **LogiStock:** What happens if it goes down? Can you dispatch on paper or with spreadsheets, how long can you keep that up, and how much catch-up work does it create afterwards?
- What else do you need that isn't on the list: labels and printers, cold storage, forklifts, dock doors (A1 notes two), Wi-Fi or scanners, customer EDI or portals?
- How many people do you need at minimum, and which skills are held by only one or two people?

**5. The Site B workaround**
- The list says "manual export to Site B possible". What does that mean in practice: data, orders, or physically moving product?
- Has it ever been done or tested? How long does it take to set up?
- Does Site B have chilled capacity and dispatch staff free in weeks 49–52, given their own three shift leaders?
- Site B's QA is "covered from Site A". If Site A as a whole is down, who releases product for dispatch from Site B?

**6. Past incidents and wrap-up**
- Have you had real disruptions (carrier failure, a LogiStock outage, a lab delay)? What happened and how long did it last?
- Which single failure worries you most?
- Who else should I talk to? Likely the QA manager, the NordFrost account manager, the LogiStock owner and the Site B dispatch lead.

## Gaps in the files to settle separately
- The impact criteria only give amounts per day. They don't set time points for assessing impact, so you'll need to agree on them (e.g. 4h / 1d / 3d / 1w) so that every interview uses the same ones.
- The criteria have no category for food safety, health or reputation. Dispatch problems in a chilled supply chain could hit those, so they may need adding.

I can put this into a shareable document or an interview template with answer fields if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && for f in *.md; do echo "=== $f"; cat "$f"; done`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/prepare-bia/4b/run2/work/site-b-org-chart.md`
