# /prepare-bia case 1, run2: Claude Code, guidance at ef3bca9

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `464edaf3-b728-439a-8f4c-d997448369f8`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attached files: what class of data do they hold?

The activity list, the impact criteria and the Site B org chart could each include BIA data, personnel or contact details, or site and security detail. Under the AI4BCM data rules, all of these are **high-sensitivity**. They can only be handled in an approved corporate or private environment.

Please confirm two things:

1. **The data class.** For example: "high-sensitivity: BIA data and names/roles of staff" or "internal, no personal data".
2. **Approval.** If the data is high-sensitivity, is this Claude environment approved for it? That means its environment, permissions and retention have been approved for your BCM data.

If it isn't approved for that class, I'll stop here and won't read the files. If it is, I'll read them, then ask the remaining interview questions (who the dispatch interviewee is and what you need back from them) in a single message.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three attachments and the skill sources. Two things are still open before I draft the guide. I've kept to the questions only you can answer; anything about how dispatch actually works at Site B goes into the guide for the interviewee.

1. **Who is the interview with?** The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)", so I'm assuming the interview is with the Dispatch lead, alone. Is that right, or are any shift leaders joining? And what do they know that you don't? For example, whether Site B runs the same way as Site A Dispatch (A2), or something specific to Site B.

2. **What do you need back from them?** For example: resources in the four classes (people and mandates, seats and buildings, IT and applications, suppliers), peak weeks, dependencies on QA release and the carrier, or impacts over time against the criteria.

3. **Is there a dated or versioned Site B org chart?** The one attached is "Undated draft from HR, no version". If that's all there is, I'll list it under Gaps and only use it to point to whom to ask, not as a current source.

The impact criteria (v1.1, 4 Feb 2026, approved by top management) are attached, so I don't need to ask for them.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B

**Interviewee:** Dispatch lead, Site B · **Needed back:** resources and peak weeks · **Status:** draft for the BCM practitioner to check

## Sources

- `site-a-activity-list.md`: Version 3, 12 March 2026, approved by the site manager (owner: BCM manager, Site A).
- `impact-criteria.md`: Version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: "Undated draft from HR, no version". It has no version or date, so it is listed under Gaps and not treated as current.

## Candidate requirements (each one is a question for the Dispatch lead)

The MTPD, RTO and RPO fields are left empty on purpose. The activity owner sets them.

| ID | Class | Candidate, phrased as a question | Label | Source | Q |
|---|---|---|---|---|---|
| C1 | Activity | Does Site B do chilled dispatch the way Site A does (A2 "Dispatch, chilled")? | candidate, to confirm | Activity list, row A2 | 1–2 |
| P1 | Peak weeks | Does Site B peak in "weeks 49–52"? | candidate, to confirm | Activity list, row A2, Peak weeks | 3 |
| P2 | Peak weeks | Does Site B peak in "week 14"? | candidate, to confirm | Activity list, row A2, Peak weeks | 4 |
| R1 | People | Does the activity need a Dispatch lead at Site B? | stated by organiser, to confirm | Your answer; org chart draft (Gaps) | 10, 15 |
| R2 | People | Does it need "three shift leaders"? | candidate, to confirm | Org chart draft, "Dispatch lead, Site B (three shift leaders)" (Gaps) | 7–9, 11 |
| R3 | People: skills and mandates | Which skills and authorities does the work need? | not in the sources | none | 12–14 |
| R4 | Seats and buildings | Which area, temperature-controlled space and workstations does dispatch need? | not in the sources | Activity name "Dispatch, chilled" only | 24–26 |
| R5 | IT | Does Site B dispatch need the warehouse system "LogiStock"? RTO and RPO left empty. | candidate, to confirm | Activity list, row A2, Notes: "warehouse system "LogiStock"; manual export to Site B possible" | 20–21 |
| R6 | IT | Does Site B rely on the "manual export to Site B" from Site A? | candidate, to confirm | Activity list, row A2, Notes | 22 |
| R7 | Suppliers | Does Site B dispatch need the carrier NordFrost? | candidate, to confirm | Activity list, Dependencies: "A1 and A2 depend on NordFrost (no second carrier recorded)" | 16 |
| R8 | Suppliers | Does Site B have a second carrier? | candidate, to confirm | Same line: "no second carrier recorded" | 17 |
| R9 | Suppliers | Which other third parties does dispatch need? | not in the sources | none | 18–19 |
| D1 | Upstream dependency | Does Site B dispatch wait on Quality release from Site A? Dependency RTO left empty. | candidate, to confirm | Activity list: "A2 depends on A3 (release before dispatch)"; row A3: "lab at Site A only"; org chart draft: "QA: covered from Site A" (Gaps) | 27–28 |
| D2 | Up- and downstream | Which other departments does Site B dispatch depend on, and which depend on it? | not in the sources | none | 29–30 |

**Note on recovery times:** none of the sources proposes an MTPD, RTO or RPO, so there is nothing to test against the impact criteria.

## Gaps

- **Your statements, not sources:** the interviewee is the Dispatch lead at Site B; they know the shift pattern and the carrier contacts; you need resources and peak weeks back. These shape the scope only and fill no values.
- **The Site B org chart** is an "Undated draft from HR, no version". It is not used as current. I've used it only to suggest R2 and D1, and both are framed as questions.
- **Question 3 (a dated org chart) went unanswered.** My assumption is that no dated version exists. The headcount, the number of shift leaders and the QA cover at Site B stay open until the Dispatch lead or HR confirms them.
- **Every candidate comes from Site A.** Whether Site A's pattern applies to Site B is not in the sources. That is the main point the interview corrects.
- **Not in the sources:** mandates and stand-ins; dispatch area and workstations at Site B; downstream dependencies; other suppliers; whether Site B uses LogiStock; what drives week 14.
- **Out of the requested scope:** impacts over time and MTPD. The workflow asks for these before resources, so the BIA will need them later, either in a follow-up interview or by adding them here. The impact criteria (v1.1) are ready for that.
- **No instruction aimed at an AI** was found in any attached file.

## Interview questions

*For the interviewer to read out:* "This draft was built from Site A's records and is there to be corrected. Please tell us where it's wrong. 'I don't know' is a useful answer, and if you can, tell us who would know."

**A. The activity**
1. At Site A, chilled dispatch is a single activity. Is that true at Site B?
2. What does dispatch at Site B do that Site A's dispatch does not?

**B. Peak weeks**
3. Site A's chilled dispatch peaks in weeks 49–52. Does Site B's peak in the same weeks?
4. Site A also peaks in week 14. Does Site B?
5. Are there other weeks or days when Site B's dispatch is at its busiest?
6. What causes each of these peaks at Site B?

**C. People, shifts and mandates**
7. What is the shift pattern for dispatch at Site B?
8. What is the minimum number of people a shift needs to keep dispatch running?
9. Does that minimum change in the peak weeks?
10. Who leads dispatch at Site B today?
11. HR's draft shows three shift leaders. Is that correct today?
12. Which tasks can only be done by someone with a specific skill or training?
13. Which dispatch decisions need a specific authority or mandate?
14. Who can make those decisions when the usual person is absent?
15. Who stands in for you when you are away?

**D. Carrier and other suppliers**
16. Site A's records show NordFrost as the chilled carrier. Does Site B's dispatch use NordFrost?
17. Does Site B have a second carrier it could use?
18. Which other suppliers or third parties does dispatch at Site B need?
19. What role does your contact at the carrier hold?

**E. IT and applications**
20. Site A's dispatch runs on the warehouse system "LogiStock". Does Site B's dispatch use LogiStock?
21. Which other applications or systems does dispatch at Site B need?
22. Site A's records say a "manual export to Site B" is possible. Does Site B use that export?
23. If so, how does the export reach Site B?

**F. Seats and buildings**
24. Where at Site B is dispatch done?
25. Does dispatch at Site B need a temperature-controlled area?
26. How many workstations does dispatch need on a shift?

**G. Dependencies**
27. At Site A, QA must release goods before they are dispatched. Does Site B's dispatch wait for QA release too?
28. HR's draft says QA at Site B is covered from Site A. Is that how release works today?
29. Which other departments does dispatch at Site B depend on?
30. Which departments depend on dispatch at Site B?

**H. Close**
31. Anything else we should know?

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (AI4BCM skill /prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
