# /prepare-bia case 1, run1: Claude Code, guidance at ef3bca9

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0b99a462-de44-4535-b546-f475043c5395`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attached files, I need one thing from you.

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md hold?**

The likely answer is **high-sensitivity**. BIA data and personnel or contact detail (an org chart often has both) belong in that class, so this environment must be an approved corporate or private one, with its permissions and retention approved. If it is, say so and I'll read the files and start the interview questions. If it isn't, or you're not sure, I'll stop here and not open the files.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files and the skill's sources. The impact criteria are attached, so two things are still open before I draft:

1. **Who is the interview with?** The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)". Is the interview with the dispatch lead alone, or with some or all of the shift leaders as well? And is there anything you already know they hold that you don't, such as how dispatch at Site B differs from Site A?
2. **What do you need back from the interview?** For example "resources and peak weeks", "dependencies on Site A's QA release", or "the full four classes plus dependencies". Should the impacts-over-time questions (which lead to MTPD) be in the guide, or will you cover them separately?

If you skip either one, I'll assume the dispatch lead alone and the full set: impacts over time, the four resource classes, dependencies and peak weeks. I'll record that as an assumption under Gaps.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide (draft): Dispatch, chilled — Site B

**Interviewee:** Dispatch lead, Site B · **Run by:** BCM practitioner · **What we need back:** resources and peak weeks

## Sources

- `site-a-activity-list.md`: Version 3, 12 March 2026, approved by the site manager.
- `impact-criteria.md`: Version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: no version and no date ("Undated draft from HR"). It is listed under Gaps and not used as current.

## Candidate requirements: Dispatch, chilled (Site B)

Every entry is a question for the dispatch lead, labelled "candidate, to confirm". All of them come from Site A's activity A2. None of them describes Site B yet.

| # | Class | Candidate (as a question) | Source | RTO | RPO | Q |
|---|---|---|---|---|---|---|
| C1 | Activity | Does Site B run "Dispatch, chilled" as an activity, with the dispatch lead as owner? *candidate, to confirm* | Site A list, row A2 | — | — | 1–2 |
| C2 | People and mandates | Is the activity owned by a "Dispatch lead", as at Site A? *candidate, to confirm* | Site A list, A2, Owner | — | — | 3–8 |
| C3 | IT and applications | Does dispatch need the warehouse system "LogiStock"? *candidate, to confirm* | Site A list, A2, Notes | *empty* | *empty* | 13–14 |
| C4 | IT and applications | What is the "manual export to Site B possible", and does Site B dispatch need it? *candidate, to confirm* | Site A list, A2, Notes | *empty* | *empty* | 15–16 |
| C5 | Suppliers | Does dispatch need the carrier NordFrost? *candidate, to confirm* | Site A list, A1 Notes; Dependencies line | — | — | 17–20 |
| C6 | Dependency, upstream | Does dispatch depend on Quality release ("release before dispatch")? *candidate, to confirm* | Site A list, Dependencies line; A3 | dependency RTO *empty* | — | 22–24 |
| C7 | Peak weeks | Are the peak weeks for dispatch "weeks 49–52, week 14"? *candidate, to confirm* | Site A list, A2, Peak weeks | — | — | 28–30 |

MTPD for the activity: *empty*.

**Note on recovery times:** none of the sources proposes a recovery time, so there is nothing to check against the impact criteria. The RTO and RPO fields stay empty for the dispatch lead to set at stage 4.

## Interview questions

*Intro for the dispatch lead:* This list is built from Site A's records, so please correct anything that doesn't fit Site B. "I don't know" is a useful answer, and we'll note who would know instead.

**A. The activity**
1. Is "dispatch of chilled goods" the right description of what your team does at Site B?
2. What does dispatch at Site B do that you know Site A's dispatch does not?

**B. People and mandates**
3. How many shifts does dispatch at Site B run?
4. What is the minimum number of people a shift needs to dispatch chilled goods?
5. Who leads each shift?
6. Which decisions during a shift can only certain people take?
7. Which skills does dispatch work need that not everyone in the team has?
8. Who stands in for you when you are away?

**C. Seats and buildings**
9. Which areas of the Site B building does dispatch need in order to work?
10. How many dock doors does dispatch need at a minimum?
11. Does dispatch share any of those areas with goods receipt?

**D. IT and applications**
12. Which systems or applications does dispatch use day to day?
13. Is LogiStock one of them?
14. Which tasks in dispatch can't be done without LogiStock?
15. Site A's list says "manual export to Site B possible". What does that export contain?
16. Who at Site B uses that export?

**E. Suppliers**
17. Which carriers move chilled goods out of Site B?
18. Is NordFrost one of them?
19. Is there a second carrier you could call on?
20. Which role at the carrier does your team contact when a collection is late?
21. Which other suppliers does dispatch rely on?

**F. Dependencies on other departments**
22. Does every load need a quality release before it leaves Site B?
23. Who does that release for Site B?
24. Does that release depend on the lab at Site A?
25. Which department hands goods over to dispatch at Site B?
26. Which departments rely on dispatch finishing its work?
27. Does dispatch at Site B rely on Site A's dispatch in any way?

**G. Peak weeks**
28. Which weeks of the year are busiest for dispatch at Site B?
29. Are weeks 49–52 a peak at Site B?
30. Is week 14 a peak at Site B?
31. Do you need more people on shift in peak weeks?
32. Do you need any other extra resources in peak weeks?

**Close**
33. Anything else we should know?

## Gaps

- **Organiser's statements, not sources:** the interview is with the dispatch lead, Site B, who knows the shift pattern and the carrier contacts. What's needed back is resources and peak weeks.
- **Org chart is an undated draft:** `site-b-org-chart.md` is an "Undated draft from HR, no version", so it is not used as current. It names "three shift leaders" and says QA is "covered from Site A". To settle this, ask HR for the dated, approved version (questions 3, 5 and 23 also ask about it).
- **Everything comes from Site A:** no source describes dispatch at Site B. Every candidate copies Site A's activity A2 and is settled only by the interview.
- **Mandates, skills, deputies:** not in the sources (questions 6–8).
- **Seats and buildings for dispatch:** not in the sources. The "two dock doors" in the Site A list belong to goods receipt (A1), not dispatch (questions 9–11).
- **"Manual export to Site B possible":** the source doesn't say what is exported or in which direction (questions 15–16).
- **Second carrier:** Site A has "no second carrier recorded". Site B is not in the sources (question 19).
- **Downstream dependencies:** not in the sources (questions 26–27).
- **Impacts over time and MTPD:** you scoped this interview to resources and peak weeks, so the guide has no questions on them. The attached impact criteria are needed when those are covered.
- **Recovery fields:** RTO, RPO, MTPD and each dependency's RTO are left empty. The dispatch lead sets them later.
- **Instructions to an AI in the material:** none found.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (AI4BCM skill `prepare-bia`, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

The **reviewer** is the BCM practitioner who runs the interview. They check this guide against the three sources before using it. A candidate enters the register only when the dispatch lead confirms it. Nothing has been written, sent or saved.
