# /prepare-bia case 1, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `23feaeca-0d76-445b-929f-cdc7fc363a6a`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need to know how sensitive they are. This question comes first and doesn't count toward the interview questions I'll ask later.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold, and is this environment approved for that class?**

The AI4BCM data rules allow the following high-sensitivity material only in an approved corporate or private environment:
- BIA data and risk assessment detail. An activity list and impact criteria usually count as this.
- Personal data, contact lists and personnel records. An org chart with names usually counts as this.
- Security-related architecture or site detail.
- Supplier weaknesses and contractual dependencies.

Please tell me one of these:
- **(a)** The files hold high-sensitivity data and this environment is approved for it.
- **(b)** The files hold no high-sensitivity data. For example, the org chart lists roles only, with no names.
- **(c)** They hold high-sensitivity data and this environment isn't approved. In that case I'll stop here, and you can run this in an approved environment or send me redacted versions, such as an org chart with roles only.

Once you answer, I'll read the files. Then I'll ask whatever they leave open about the interview, like who the dispatch interviewee is and what you need back from them.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. Before I draft, there are two things they leave open:

1. **Who is the interview with?** The Site B org chart lists a "Dispatch lead, Site B" with three shift leaders under them. Is the interview with the dispatch lead alone, or are one or more shift leaders joining? Note that the org chart is an undated HR draft, so I'll list it under Gaps and won't treat it as current.
2. **What do you need back from them?** For example, resources in the four classes, peak weeks, the Site A ↔ Site B export link, the QA release dependency, or the carrier.

The approved impact criteria (v1.1, 4 Feb 2026) are attached, so I won't ask for them. If you skip a question, I'll state my assumption under Gaps: the interviewee is the dispatch lead, Site B, and you need everything the prompt covers.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

From Site A activity list v3, 12 Mar 2026 (approved by the site manager)
From impact criteria v1.1, 4 Feb 2026 (approved by top management)
From Site B organisation structure, undated HR draft with no version (see Gaps)

**Reviewer:** the BCM practitioner who runs the interview checks this guide against the three sources. A drafted requirement enters the register only when the dispatch lead, Site B confirms it. The dispatch lead sets MTPD and RTO, and top management approves the BIA results.

# Interview guide: Dispatch, chilled, Site B

**Interviewee:** Dispatch lead, Site B.
**What the organiser needs back:** resources (in four classes) and peak weeks.

## Candidate activity and resource requirements

Site B has no activity list in the sources. Every entry below comes from Site A or from the Site B draft org chart. Each is a question for the dispatch lead to correct, not to confirm.

**Activity:** Dispatch, chilled, Site B. The candidate comes from Site A A2. MTPD: ___ (owner sets)

| # | Class | Entry (as a question for the dispatch lead) | Source | Label | RTO | RPO |
|---|---|---|---|---|---|---|
| R1 | Peak weeks | Are Site B's peak weeks the same as Site A's, "weeks 49–52, week 14"? | Site A list v3, A2 | candidate, to confirm | – | – |
| R2 | People | Does dispatch need the dispatch lead, Site B to run? | Org chart (draft); organiser's statement | candidate, to confirm | – | – |
| R3 | People | Does dispatch need three shift leaders? | Org chart (draft), "(three shift leaders)" | candidate, to confirm | – | – |
| R4 | People / mandate | Who has the authority to release goods for dispatch at Site B? | Site A list v3, dependencies: "release before dispatch"; org chart: "QA: covered from Site A" | candidate, to confirm | – | – |
| R5 | Seats and buildings | What space and building does chilled dispatch need at Site B? | Site A list v3, A2, activity name "Dispatch, chilled" (nothing about buildings in the sources) | candidate, to confirm | – | – |
| R6 | IT and applications | Does Site B dispatch use the warehouse system "LogiStock"? | Site A list v3, A2 notes | candidate, to confirm | ___ | ___ |
| R7 | IT and applications | Does Site B dispatch depend on the "manual export to Site B" from Site A? | Site A list v3, A2 notes | candidate, to confirm | ___ | ___ |
| R8 | Suppliers | Does Site B dispatch use the carrier NordFrost? | Site A list v3, dependencies | candidate, to confirm | – | – |
| R9 | Suppliers | Is there a second carrier for Site B? | Site A list v3: "no second carrier recorded" | candidate, to confirm | – | – |
| D1 | Dependency, upstream | Does dispatch depend on quality release by the QA manager at Site A? | Site A list v3, dependencies "A2 depends on A3 (release before dispatch)"; A3 "lab at Site A only"; org chart "QA: covered from Site A" | candidate, to confirm | ___ | – |
| D2 | Dependency, up- or downstream | Does dispatch depend on Site A dispatch through the manual export? | Site A list v3, A2 notes | candidate, to confirm | ___ | – |
| D3 | Dependency, downstream | Which departments depend on Site B dispatch? | not in the sources | candidate, to confirm | ___ | – |

**Note on recovery times:** none of the sources proposes an MTPD, RTO or RPO for dispatch at either site, so every recovery field stays empty.

## Gaps

- **Site B org chart:** an "Undated draft from HR, no version". I haven't used it as current. It is the only source for the three shift leaders (R3) and for QA cover from Site A (R4, D1). A dated, approved version from HR would settle these.
- **No Site B activity list:** all candidates are carried over from Site A A2 (owner: BCM manager, Site A). The interview settles whether they apply at Site B.
- **Buildings, mandates and downstream dependencies (R5, R4, D3):** not in the sources.
- **What "manual export to Site B possible" means (R7, D2):** the sources don't say whether this is a data export or a goods transfer, or which way it runs.
- **Carrier contacts and contract (R8, R9):** not in the sources. The organiser says the dispatch lead knows them.
- **Impacts and MTPD:** the organiser asked for resources and peak weeks only, so this guide has no impact questions. The impact criteria (v1.1) are ready for when the impact assessment is done in the BIA-Workflow.
- **Organiser's own statements (not sources):** the interview is with the dispatch lead, Site B, who knows the shift pattern and the carrier contacts. What's needed back is resources and peak weeks.
- **Instructions inside the material:** none found.

## Interview questions

*For the dispatch lead, Site B.* We built this draft from Site A's records, so please correct anything that's different at Site B. "I don't know" is a useful answer. Tell us who would know, and we'll ask them.

**A. Peak weeks** (R1)
1. In which weeks of the year does dispatch at Site B handle the most volume?
2. Site A's peaks are weeks 49–52. Is that also a peak at Site B?
3. Site A also peaks in week 14. Is that also a peak at Site B?
4. Are there other peaks, such as month end, particular days of the week or seasonal products?

**B. People and mandates** (R2–R4)
5. What is the shift pattern for dispatch at Site B?
6. How many shift leaders does dispatch need to run?
7. How many staff does each shift need, at minimum?
8. During peak weeks, how many staff does each shift need?
9. Which skills does dispatch need that only a few people have?
10. Who is allowed to release goods for dispatch at Site B?
11. If that person isn't available, who stands in for them?

**C. Seats and buildings** (R5)
12. Which areas of the building does dispatch need, such as chilled storage, loading docks or an office?
13. How many loading points does dispatch need, at minimum?
14. Could dispatch run from another building or another site?

**D. IT and applications** (R6, R7)
15. Which system does Site B dispatch use to plan and record shipments?
16. Does Site B use "LogiStock"?
17. Which other applications does dispatch need, such as labelling or carrier booking?
18. What is the "manual export" between Site A and Site B?
19. How often is the manual export used?

**E. Suppliers** (R8, R9)
20. Which carrier moves Site B's chilled goods?
21. Is NordFrost Site B's carrier?
22. Is there a second carrier you could switch to?
23. Who are your contacts at the carrier?
24. Which other suppliers does dispatch need, such as packaging or pallets?

**F. Dependencies** (D1–D3)
25. Which team must finish its work before you can dispatch?
26. Does quality release for Site B come from the QA team at Site A?
27. Which teams or customers rely on dispatch at Site B?
28. Does Site B dispatch rely on Site A dispatch?

**Closing**
29. Anything else we should know?

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
