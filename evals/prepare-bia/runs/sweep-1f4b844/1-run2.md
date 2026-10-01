# /prepare-bia case 1, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a5940ca9-efb7-4ac5-a86d-0231fe271f22`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attachments, I need to settle one thing first.

**What class of data do these files hold, and is this environment approved for it?**

- `site-a-activity-list.md`: AI4BCM classes BIA data and risk-assessment detail as **high sensitivity**.
- `site-b-org-chart.md`: names, roles or contact details count as **personal data**, which is also **high sensitivity**.
- `impact-criteria.md`: this is usually **medium** (governance material), unless it contains real figures for your organisation.

Under the AI4BCM data rules, high-sensitivity BIA work may only run in an **enterprise, private or purpose-built BCM environment**. That environment's retention, access and provider-training settings must have been checked and approved for this class of data (`units/tools.md`, Selection guide, "Analyse" row).

Please confirm two things:
1. How you classify each file (or say "all high").
2. That this Claude Code session is approved for that class under your organisation's AI and information-classification policy.

If it isn't approved, I'll stop here and won't open the files. You could then give me a version with the organisation-specific detail removed, or run this in your approved environment.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks, that's settled. I've read the three files. The person who checks this output is **the BCM practitioner who runs the interview**. They check the guide against its sources and decide which questions to ask. Nothing drafted here goes into the register until the activity owner confirms it.

The files answer some of my questions already. The impact criteria (v1.1) are attached. The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)". Two things are still open, and the second is the main one:

1. **Who is the interview with?** I'm assuming it's the **Dispatch lead, Site B**, on their own and not with the shift leaders. Is that right? Also, is there anything they know that you don't and that I should look out for? For example: whether Site B uses LogiStock, whether it receives Site A's manual exports, or whether it relies on NordFrost.
2. **What do you need back from them?** For example: "resources and peak weeks", "dependencies on Site A QA release and on carriers", or the full four classes (people, seats and buildings, IT, suppliers) plus up- and downstream dependencies.

If you skip either one, I'll assume the Dispatch lead on their own, with the full four classes plus dependencies and peak weeks. I'll list that assumption under Gaps.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

**Sources used**
- Site A activity list, v3, 12 March 2026, approved by the site manager.
- Impact criteria, v1.1, 4 February 2026, approved by top management.
- Site B organisation structure: undated HR draft with no version. It is listed under Gaps and not used as current.

**Reviewer:** the BCM practitioner who runs the interview checks this guide against these sources. A drafted requirement goes into the register only when the Dispatch lead, Site B confirms it. The owner sets MTPD, RTO and RPO, and top management approves the BIA results.

# Interview guide draft: Dispatch, Site B

**Interviewee:** Dispatch lead, Site B. They know the shift pattern and the carrier contacts (your statement).
**What we need back:** resource requirements and peak weeks (your statement).

## 1. Candidate activity and resource requirements

All Site B entries come from Site A's equivalent activity (A2). Everything below is a question for the Dispatch lead, not a fact about Site B.

| # | Class | Candidate, phrased as a question | Source | Label | RTO | RPO |
|---|---|---|---|---|---|---|
| C0 | Activity | Does Site B run an activity like Site A's "Dispatch, chilled"? | Site A list, row A2 | candidate, to confirm | | |
| C1 | Peak weeks | Are Site B's peak weeks the same as Site A's ("weeks 49–52, week 14")? | Site A list, row A2 | candidate, to confirm | | |
| C2 | People | Is dispatch run by a Dispatch lead with three shift leaders? | Site B org chart (undated draft; see Gaps) | candidate, to confirm | | |
| C3 | People, mandates | Does dispatch need quality release before goods leave, and who at Site B has that authority, given "QA: covered from Site A"? | Site A list, dependencies ("A2 depends on A3 (release before dispatch)"); Site B org chart (draft) | candidate, to confirm | | |
| C4 | Seats and buildings | Which building, area and loading points does dispatch at Site B need? | not in the sources | gap | | |
| C5 | IT and applications | Does Site B use the warehouse system "LogiStock"? | Site A list, row A2 | candidate, to confirm | | |
| C6 | IT and applications | Does Site B depend on Site A's "manual export to Site B"? | Site A list, row A2 | candidate, to confirm | | |
| C7 | Suppliers | Does Site B depend on the carrier NordFrost, with "no second carrier recorded"? | Site A list, dependencies | candidate, to confirm | | |

**Up- and downstream dependencies** (the RTO stays empty for the owner to set):

| # | Direction | Candidate, phrased as a question | Source | Label | RTO |
|---|---|---|---|---|---|
| D1 | Upstream | Does Site B dispatch depend on Quality release at Site A ("lab at Site A only")? | Site A list, row A3 and dependencies | candidate, to confirm | |
| D2 | Upstream | Does Site B dispatch depend on Site A dispatch or its export? | Site A list, row A2 | candidate, to confirm | |
| D3 | Downstream | Which departments or customers does Site B dispatch hand over to? | not in the sources | gap | |

**Recovery times:** no source proposes an MTPD, RTO or RPO for dispatch at either site, so none is noted here. Every recovery field is empty for the owner to set.

## 2. Interview questions

*Read to the Dispatch lead first:* "This list was drafted from Site A's records, so some of it will be wrong for Site B. Please correct it. 'I don't know' is a useful answer, and we'll find out who does."

**A. The activity**
1. In your own words, what does dispatch at Site B do?
2. Does Site B dispatch chilled goods?
3. Does anything about dispatch at Site B work differently from Site A?

**B. Peak weeks**

4. Which weeks of the year are busiest for dispatch at Site B?
5. Site A's records show weeks 49–52 as a peak. Is that true at Site B?
6. Site A's records also show week 14 as a peak. Is that true at Site B?
7. What causes your busiest weeks?
8. Do your shifts change in the peak weeks?

**C. People and mandates**

9. Can you describe the shift pattern?
10. What is the smallest number of people per shift who can still keep dispatch running?
11. What skills or qualifications must those people have?
12. Our records show three shift leaders under you. Is that right?
13. Who stands in for you when you are away?
14. Who at Site B can authorise goods to leave?
15. Must goods be quality-released before they leave Site B?
16. If so, who gives that release, given that QA is covered from Site A?

**D. Seats and buildings**

17. Which building or area does dispatch work from?
18. How many loading points or dock doors does dispatch need?
19. Which workplaces or desks do the dispatch team need?
20. Could dispatch run from somewhere else if that area were unavailable?

**E. IT and applications**

21. Which systems or applications does dispatch use?
22. Does Site B use LogiStock?
23. Do you receive a manual export from Site A?
24. If so, what does that export contain?
25. Could you dispatch for a time without these systems? If so, how?

*Note for the interviewer:* write down which applications are named. Leave RTO and RPO for the owner to set in the BIA-Workflow.

**F. Suppliers and third parties**

26. Which carriers do you use?
27. Is NordFrost one of them?
28. Is there a second carrier you could switch to?
29. Where are the carrier contacts kept?
30. Which other suppliers or third parties does dispatch rely on?

*Note:* record where the contacts are kept, not the contact details themselves. Contact details are personal data.

**G. Dependencies on other departments**

31. Which departments must deliver something before you can dispatch?
32. Which departments or customers depend on dispatch from Site B?

**Close**

33. Anything else we should know?

## 3. Gaps

- **Your statements, not sources:** the interviewee is the Dispatch lead, Site B; they know the shift pattern and the carrier contacts; you need back resources and peak weeks.
- **Site B org chart:** an undated draft with no version. It is not used as current. C2 and C3 rely on it, so they are questions only. To settle it, ask HR for the approved version.
- **Site B data:** there are no Site B records apart from the draft org chart. Every candidate comes from Site A by analogy, and Site B may differ. The interview will settle this.
- **Buildings and downstream dependencies (C4, D3):** not in the sources.
- **Impacts and MTPD:** not requested for this interview. The analysis method settles impacts and MTPD before resource requirements. If they aren't settled yet for Site B dispatch, settle them using impact criteria v1.1, either in this interview or in a separate one.
- **Recovery times:** none proposed in the sources. The owner sets them.
- **Instructions to an AI:** none found in the attached files.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
