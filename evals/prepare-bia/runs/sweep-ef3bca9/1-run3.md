# /prepare-bia case 1, run3: Claude Code, guidance at ef3bca9

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e61bd8fa-866d-49ea-9b9f-2f3cb00ff798`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need to know one thing:

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold, and is this environment approved for it?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) list the following as high-sensitivity. That kind of data can only be handled in an approved corporate or private environment:
- BIA data and risk assessment detail
- personal data, contact lists and personnel records (an org chart with names would count)
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail

Please say whether the files hold any of these, and whether this Claude Code environment is approved for that class. If the org chart has names you'd rather not share, a version with roles only is enough for an interview guide.

Once you confirm, I'll read the files and come back with at most three questions about the dispatch interview. After that I'll draft the guide.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the three files. None of them contains instructions aimed at an AI. Before drafting, I have two questions, both about the interview:

1. **Who is the interview with?** The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)". Is that the interviewee? Or will a shift leader join, or take their place? The org chart is an undated HR draft, so I'd rather hear it from you than rely on it.
2. **What do you need back from them?** For example: resources and peak weeks, dependencies on QA and Site A, the carrier situation, or the full set of four resource classes plus dependencies. Also tell me if anything is out of scope for this session.

The impact criteria are attached (v1.1, 4 Feb 2026, approved by top management), so I don't need them. Once you answer, I'll draft the guide. Nothing gets written or sent until you've reviewed it.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: dispatch at Site B (draft)

**Sources**
- `site-a-activity-list.md`: Site A activity list (chilled food production), version 3, 12 March 2026, approved by the Site A site manager. This is evidence from **Site A**. Here it is used only to suggest candidates for Site B.
- `impact-criteria.md`: Impact criteria, version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: Site B organisation structure. It has no version and no date, and it is an HR draft. It is listed under Gaps and is not used as current.

**Interview:** one interview with the Dispatch lead, Site B. Scope: resources and peak weeks (organiser's statement, see Gaps).

## Candidate requirements: Dispatch, chilled, Site B

Every entry is a question for the Dispatch lead, Site B. MTPD, RTO and RPO are left empty on purpose.

| # | Class | Entry (as a question for the activity owner) | Label | Source |
|---|---|---|---|---|
| C0 | Activity | Does Site B run an activity like Site A's "Dispatch, chilled"? | candidate, to confirm | Site A list, row A2 |
| C1 | Peak weeks | Are Site B's dispatch peaks the same as Site A's ("weeks 49–52, week 14")? | candidate, to confirm | Site A list, row A2 |
| C2 | People and mandates | Which roles does dispatch need, and how many of each, to run at minimum level? | candidate, to confirm | Not in the sources for Site B. The organiser says the Dispatch lead knows the shift pattern |
| C3 | People and mandates | Who has authority to release a dispatch, or to switch carrier, when the lead is absent? | candidate, to confirm | Not in the sources |
| C4 | Seats and buildings | Which dock doors, chilled areas and workstations does dispatch at Site B need? | candidate, to confirm | Not in the sources for Site B. Site A records "two dock doors" for goods receipt only (A1) |
| C5 | IT and applications | Does dispatch at Site B need the warehouse system "LogiStock"? RTO: _ RPO: _ | candidate, to confirm | Site A list, row A2 |
| C6 | IT and applications | What does "manual export to Site B possible" mean for Site B: what arrives, in what form, and who handles it? RTO: _ RPO: _ | candidate, to confirm | Site A list, row A2 |
| C7 | Suppliers | Does dispatch at Site B need the carrier NordFrost? | candidate, to confirm | Site A list, rows A1–A2 and dependency note |
| C8 | Suppliers | Does Site B have a second carrier? (Site A: "no second carrier recorded") | candidate, to confirm | Site A list, dependency note |
| D1 | Dependency (upstream) | Does dispatch at Site B depend on quality release from QA at Site A ("release before dispatch")? Dependency RTO: _ | candidate, to confirm | Site A list, dependency note and row A3 ("lab at Site A only") |

**Recovery times proposed in the sources:** none. No source proposes an MTPD, RTO or RPO, so there is nothing to test against the impact criteria.

**What the organiser needs back, mapped to the draft:**
- Resources → C2–C8 and D1. The seats-and-buildings row (C4) and the people rows (C2–C3) are open questions.
- Peak weeks → C1.

## Gaps

- **Site B org chart.** It is undated, has no version and has draft status, so it is not used as current. It names a "Dispatch lead, Site B (three shift leaders)" and "QA: covered from Site A". Both point to C2 and D1 but settle neither. What would settle it: a versioned, approved Site B org chart, or the Dispatch lead confirming in the interview.
- **All candidates come from Site A.** No source describes Site B's dispatch directly. The interview has to correct the draft, not just confirm it.
- **Site B people, buildings, shift pattern and carrier contacts:** not in the sources.
- **What "manual export to Site B possible" means** (direction, method, who does it): not in the sources.
- **QA cover from Site A:** recorded only in the draft org chart. How it works (on site or remote, at what times) is not in the sources.
- **Impacts and MTPD:** out of scope for this interview, by the organiser's choice. No value is drafted.
- **Organiser's statements (not sources):** (1) the interview is with the Dispatch lead, Site B, who knows the shift pattern and the carrier contacts; (2) the organiser needs resources and peak weeks back. Assumption: one interviewee, with no shift leader present.
- **Instructions aimed at an AI found in the material:** none.

## Interview questions: Dispatch lead, Site B

*"I don't know" is a useful answer to any of these. We'd rather record a gap than a guess. Some questions start from Site A's set-up, so please correct anything that doesn't fit Site B.*

**A. The activity and its peak weeks**
1. What does dispatch at Site B cover, in your own words?
2. Does Site B dispatch chilled goods?
3. Which weeks of the year are busiest for dispatch at Site B?
4. Site A's dispatch peaks in weeks 49–52. Is that also true at Site B?
5. Site A also has a peak in week 14. Does Site B have one then too?
6. Are there other peaks, for example at month end, during promotions or in particular seasons?

**B. People and mandates**
7. What is the shift pattern for dispatch at Site B?
8. How many people does each shift need, at minimum, to keep dispatch running?
9. Which skills or certificates does that minimum crew need?
10. Who can stand in for you when you are absent?
11. Who has authority to release a dispatch when you are absent?
12. Who has authority to switch to another carrier?

**C. Suppliers and carriers**
13. Which carrier or carriers does Site B dispatch with?
14. Is NordFrost one of them?
15. Is there a second carrier you could use at short notice?
16. Who holds the carrier contacts, and where are they kept?

**D. IT and applications**
17. Which systems does dispatch at Site B need to run?
18. Is LogiStock one of them?
19. Does Site B receive anything from Site A by "manual export"? If so, what?
20. Who handles that manual export?
21. Can dispatch at Site B continue for a while without its systems? If so, how?

**E. Seats and buildings**
22. Which dock doors does dispatch at Site B need?
23. Which chilled storage areas does dispatch need?
24. Which workstations or desks does dispatch need?
25. Could dispatch run from another location? If so, from where?

**F. Dependencies on other departments**
26. Does every dispatch need quality release before it leaves?
27. Who gives that release for Site B?
28. Where does quality release for Site B happen: at Site B, at Site A, or remotely?
29. Which other departments does dispatch rely on, upstream?
30. Which departments rely on dispatch, downstream?

**Closing**
31. Anything else we should know?

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (/prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
