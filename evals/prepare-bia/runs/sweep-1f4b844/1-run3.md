# /prepare-bia case 1, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3b591bb4-6b87-4ea5-b1f4-ec9960633d8c`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need to know what class of data they hold.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` contain, and is this environment approved for it?**

The AI4BCM data rules list these as high-sensitivity. High-sensitivity data may only be handled in an approved corporate or private environment:
- BIA data and risk assessment detail (an activity list and impact criteria usually fall here)
- personal data, contact lists and personnel records (an org chart with names usually falls here)
- security-related site detail, supplier weaknesses and recovery strategies

If any file holds that kind of data, please confirm that this Claude Code environment is approved for high-sensitivity data. If it isn't, I'll stop here. In that case you could send redacted versions, for example with roles instead of names and no site security detail. Passwords, keys and access tokens can't go in either way.

Once you've confirmed, I'll read the files and ask only what they leave open about the interview. Then I'll draft the guide for the BCM practitioner who runs it to check against the sources.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The files are open. The org chart names a **Dispatch lead, Site B** with three shift leaders, and the impact criteria (v1.1, 4 Feb 2026) are attached, so I don't need to ask for them. Two things are still open:

1. **Who is the interview with?** I'll assume the Dispatch lead, Site B, on their own. Is that right, or will a shift leader join too? Also, what do they know that you don't? For example, how Site B dispatch differs from Site A's.
2. **What do you need back from them?** For example "resources and peak weeks", "dependencies on QA and the carrier", or the full four classes of resource requirements.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

Interview guide: Dispatch, chilled, Site B (draft)

- From Site A activity list v3, 12 March 2026 (approved by the Site A site manager)
- Checked against impact criteria v1.1, 4 February 2026 (approved by top management)
- Site B organisation structure: **undated draft from HR, no version** (listed under Gaps)
- Method: AI4BCM prompt `prompts/bia` 2026.09.1, Task choice 1

**Reviewer:** the BCM practitioner who runs the interview checks this guide against the three sources above. Each entry below is a question. It goes into the requirements register only when the Dispatch lead, Site B, confirms it. The activity owner sets MTPD, RTO and RPO. Top management approves the BIA results.

---

## 1. Candidate activity and requirements

All the evidence about dispatch comes from Site A. The Site B org chart only shows that the role exists. So every row is a Site A fact put to Site B as a question. MTPD, RTO and RPO stay blank for the owner to set.

**Activity:** Dispatch, chilled, Site B. *Candidate, to confirm.* Source: Site A list, A2; Site B org chart ("Dispatch lead, Site B"). MTPD: ___

| # | Entry, as a question for the activity owner | Class | Source | RTO | RPO | Label |
|---|---|---|---|---|---|---|
| C1 | Does Site B dispatch peak in weeks 49–52? | Peak weeks | Site A list, A2: "weeks 49–52, week 14" | n/a | n/a | candidate, to confirm |
| C2 | Does Site B dispatch also peak in week 14? | Peak weeks | Site A list, A2 | n/a | n/a | candidate, to confirm |
| C3 | Does dispatch need the Dispatch lead plus three shift leaders to run? | People | Site B org chart (draft): "Dispatch lead, Site B (three shift leaders)" | n/a | n/a | candidate, to confirm |
| C4 | Does Site B dispatch run on the warehouse system "LogiStock"? | IT and applications | Site A list, A2: warehouse system "LogiStock" | ___ | ___ | candidate, to confirm |
| C5 | Is a manual export possible as a workaround, as Site A records? | IT and applications | Site A list, A2: "manual export to Site B possible" | ___ | ___ | candidate, to confirm |
| C6 | Does Site B dispatch use NordFrost as its carrier? | Suppliers | Site A list, A2 notes and dependencies: "A1 and A2 depend on NordFrost" | n/a | n/a | candidate, to confirm |
| C7 | Does Site B dispatch need quality release before a load leaves, done from Site A? | Dependency (upstream) | Site A list, dependencies: "A2 depends on A3 (release before dispatch)"; A3: "lab at Site A only"; Site B org chart: "QA: covered from Site A" | ___ | n/a | candidate, to confirm |

Recovery times: none of the sources proposes an MTPD, RTO or RPO, so there is nothing to test against the impact criteria.

## 2. Gaps

| Gap | What would settle it |
|---|---|
| The Site B org chart is an undated HR draft with no version. I have used it only to name roles, not as a current structure. | A dated, approved Site B org chart, or the Dispatch lead's confirmation (Q5–Q6) |
| No source covers Site B dispatch directly. C1–C7 are Site A facts. | The interview |
| Mandates for dispatch: not in the sources. | Q7–Q8 |
| Seats and buildings for dispatch: not in the sources. Site A records two dock doors under goods receipt (A1), not under dispatch. | Q9–Q11 |
| Shift pattern at Site B: not in the sources. | Q12–Q14 |
| "Manual export to Site B possible" (A2) doesn't say which way the export goes or who does it. | Q17–Q18 |
| No second carrier is recorded at Site A, and none is recorded for Site B. | Q20 |
| Carrier contacts: not in the sources. | Q21 (ask how the contacts are held; leave names out of the guide) |
| Upstream dependency on the Site B warehouse: not in the sources. The org chart lists a Warehouse lead, Site B. | Q24 |
| Downstream recipients of dispatch: not in the sources. | Q25 |
| The impact criteria set levels but no time horizons (the points in time at which impacts are assessed). The workflow treats these as method parameters agreed before the BIA starts. | The BCM manager, before the interview |
| A Site B scope statement (BIA workflow stage 1) is not attached. | The organiser |
| Your own statements, not sources: the interviewee is the Dispatch lead, Site B; they know the shift pattern and the carrier contacts; you need resources and peak weeks back. They set the scope and priority of this guide. They fill no value. | n/a |
| No instructions to an AI were found in the attached files. | n/a |

## 3. Interview questions

*For the Dispatch lead, Site B. Some of what follows was drafted from another site's records, so please correct anything that is wrong. "I don't know" is a useful answer. It tells us whom to ask next.*

**Peak weeks**
1. Which weeks of the year are busiest for dispatch at Site B?
2. Site A peaks in weeks 49–52. Is that true for Site B too?
3. Site A also peaks in week 14. Is that true for Site B?
4. Are there other busy periods, such as month end, promotions or a particular customer's schedule?

**People and mandates**
5. Which roles must be present for dispatch to run?
6. Is dispatch run by you and three shift leaders, or is it set up differently now?
7. Which decisions in dispatch need a named person's authority, such as releasing, holding or re-routing a load?
8. Who can take those decisions when you are not on site?

**Seats and buildings**
9. Which areas of the site does dispatch need, such as docks, chilled staging or an office?
10. How many dock doors does dispatch use?
11. Could dispatch run from another location, and if so, which?

**Shift pattern**
12. Which shifts does dispatch run?
13. On which days does dispatch run?
14. Does the shift pattern change in the peak weeks?

**IT and applications**
15. Which systems does dispatch use?
16. Is LogiStock one of them?
17. Is there a manual way to dispatch when the system is down?
18. Site A records that a manual export to Site B is possible. What does that export mean for your work at Site B?

**Suppliers**
19. Which carrier takes chilled loads from Site B?
20. Is there a second carrier you could use?
21. How are the carrier contacts held, and who keeps them up to date?
22. Do you depend on any other supplier, such as packaging, pallets or cooling?

**Dependencies on other departments**
23. Must QA release each load before it leaves Site B?
24. Does dispatch depend on the Site B warehouse?
25. Who receives what dispatch produces, inside or outside the company?

**Impacts over time** *(owner's view; the owner sets MTPD later)*
26. If dispatch stopped, after how long would the financial impact pass EUR 10k a day?
27. After how long would a key account be late?
28. After how long would a report to the food authority be needed?

**Close**
29. Anything else we should know?

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (/prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
