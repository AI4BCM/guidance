# /prepare-bia case 1, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `82bdb842-2746-4db5-9db0-134b49231b3b`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three attachments, I need one thing settled first. This is step 1 of the skill's preflight.

**What class of data do these files hold, and is this environment approved for it?**

- `site-a-activity-list.md`: activities from an existing or draft BIA.
- `impact-criteria.md`: your organisation's impact scales.
- `site-b-org-chart.md`: may include names, roles or contact details.

Under the AI4BCM data rules (`units/data-rules.md`), BIA data and personal data or personnel records are **high sensitivity**. High-sensitivity data may only be handled in an approved enterprise, private or purpose-built BCM environment (`units/tools.md`, Selection guide, "Analyse" row). Before I open the files, please confirm:

1. The class of data in each file (high, medium or low, or "contains personal data").
2. That this Claude Code session is approved for that class under your organisation's AI and information-classification policy, including its retention and access settings.

If the session isn't approved for high-sensitivity data, I'll stop here. One way forward then is to send me versions with names and site-specific detail removed.

Once you confirm, I'll read the files. After that I'll ask at most three questions about the interview: who it's with, and what you need back from them.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all three files. Before I draft anything, I have two questions about the interview. Both answers go under Gaps as your statements, not as sources.

1. **Who is the interview with?** The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)". Is the interview with the Dispatch lead alone, or are one or more shift leaders joining? If so, I'll prepare it as a workshop with the owners listed. The chart is an undated HR draft with no version, so I'll treat that role as unconfirmed until you say so.
2. **What do you need back from them?** For example: resources and peak weeks, the dependency on QA release from Site A, the carrier situation, or something else. Give me the list and I'll map each item to a candidate or a gap.

You've attached the impact criteria (v1.1, approved 4 Feb 2026), so I don't need to ask for them.

The BCM practitioner who runs the interview checks the guide against these three sources. A drafted requirement only enters the register when the Site B dispatch owner confirms it. That owner sets MTPD and RTO, and top management approves the BIA results.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

*Source stamp*
- From Site A activity list v3, 12 Mar 2026 (approved by the site manager)
- From impact criteria v1.1, 4 Feb 2026 (approved by top management)
- Site B organisation structure: no version, no date (HR draft). It is listed under Gaps and not used as current.

# Interview guide: chilled dispatch, Site B (draft)

**Interviewee:** Dispatch lead, Site B. **What the organiser needs back:** resources and peak weeks.
**Reviewer:** the BCM practitioner who runs the interview checks this guide against the sources above. A requirement only enters the register when the Dispatch lead confirms it. The Dispatch lead sets MTPD and RTO, and top management approves the BIA results.

Every candidate below comes from Site A. Use them as something to correct, not as something to confirm.

## Candidate activities, resource requirements and dependencies

| # | Entry, as a question for the activity owner | Class | Source | Label | RTO | RPO |
|---|---|---|---|---|---|---|
| C1 | Does Site B run "Dispatch, chilled" as one activity? | Activity | Site A list v3, row A2 | candidate, to confirm | | |
| C2 | Are Site B's peak weeks the same as Site A's: "weeks 49–52, week 14"? | Peak weeks | Site A list v3, row A2 | candidate, to confirm | | |
| C3 | Is the Dispatch lead the role that owns dispatch at Site B? | People | Site A list v3, row A2 (owner column); organiser | stated by organiser, to confirm | | |
| C4 | Does dispatch at Site B need the warehouse system "LogiStock"? | IT and applications | Site A list v3, row A2 notes | candidate, to confirm | | |
| C5 | Does dispatch at Site B use the "manual export to Site B" that Site A records as possible? | IT and applications | Site A list v3, row A2 notes | candidate, to confirm | | |
| C6 | Does dispatch at Site B depend on the carrier NordFrost? | Suppliers | Site A list v3, row A2 notes and Dependencies line | candidate, to confirm | | |
| C7 | Does Site B have a second carrier? Site A has "no second carrier recorded". | Suppliers | Site A list v3, Dependencies line | candidate, to confirm | | |
| D1 | Upstream: does dispatch at Site B depend on quality release by Site A QA ("release before dispatch"; "lab at Site A only")? | Dependency | Site A list v3, row A3 and Dependencies line | candidate, to confirm | *(dependency RTO blank)* | |

**Seats and buildings:** no candidate. See Gaps.

*Note on recovery times:* none of the sources proposes an MTPD, RTO or RPO, so none is set here. The approved impact criteria (v1.1) are there for the owner to test recovery times against later.

**What the organiser needs back, and where it is covered:**
- Peak weeks: C2, and questions 2–3.
- Resources: C3–C7, D1 and the gaps below, covered by questions 4–24.

## Gaps

- **Site B org chart: an undated HR draft with no version.** It is not used as current. What it says, "three shift leaders" and "QA: covered from Site A", is only asked about (questions 7 and 22). HR can confirm it with a dated version.
- **Nothing in the sources describes Site B itself.** Every candidate is carried over from Site A.
- **Seats and buildings for dispatch:** not in the sources. Site A records "two dock doors" only for goods receipt (A1).
- **People:** roles, minimum numbers per shift, skills, mandates and deputies are not in the sources.
- **Other IT applications and other suppliers:** not in the sources.
- **Downstream dependencies** (who depends on dispatch at Site B): not in the sources.
- **Impacts and MTPD:** the organiser didn't ask for them. The method settles impacts and MTPD before resources (analysis.md, Method). My assumption is that they are covered in a separate step.
- **What the organiser told me** (these are statements, not sources):
  - The interview is with the Dispatch lead, Site B.
  - The Dispatch lead knows the shift pattern and the carrier contacts.
  - What's needed back is resources and peak weeks.
- **Instructions to an AI found in the material:** none.

## Questions for the Dispatch lead, Site B

*If you don't know the answer to a question, "I don't know" is a useful answer. We'll find out from someone else.*

**The activity**
1. Is chilled dispatch at Site B one activity, or does it split into parts you would treat separately? (C1)

**Peak weeks**
2. At Site A, dispatch peaks in weeks 49–52 and week 14. Which weeks are peak weeks for dispatch at Site B? (C2)
3. Are there other times in the year when dispatch at Site B is busier than normal? (C2)

**People**
4. Which roles does dispatch at Site B need in order to run? (C3, gap)
5. What is the smallest number of people per role you need on a shift? (gap)
6. What shift pattern does dispatch at Site B work? (organiser's statement)
7. The draft org chart shows three shift leaders reporting to you. Is that correct? (gap)
8. Which skills or qualifications does the work need that not everyone on site has? (gap)
9. Which decisions in dispatch need someone with a specific authority or mandate? (gap)
10. Who stands in for you when you are not there? (gap)

**Carriers and other suppliers**
11. Does Site B use NordFrost, the carrier Site A uses? (C6)
12. Which other carriers, if any, can collect chilled goods from Site B? (C7)
13. Which role at Site B holds the carrier contacts? The contact details themselves go in the contact list, not in this record. (organiser's statement)
14. Which other suppliers does dispatch at Site B need? (gap)

**IT and applications**
15. Does dispatch at Site B use LogiStock? (C4)
16. Which other applications does dispatch at Site B need? (gap)
17. Site A's records say a "manual export to Site B" is possible. Does dispatch at Site B use that export? (C5)

**Building and workspace**
18. Which areas of the site does dispatch at Site B need in order to work? (gap)
19. How many dock doors does dispatch at Site B need? (gap)
20. How many workplaces does the dispatch team need? (gap)

**Dependencies on other departments**
21. Do goods at Site B have to wait for quality release before they are dispatched? (D1)
22. Who carries out quality release for goods leaving Site B? (D1, gap)
23. Which other departments does dispatch at Site B depend on? (gap)
24. Which departments depend on dispatch at Site B? (gap)

**Closing**
25. Anything else we should know?

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
