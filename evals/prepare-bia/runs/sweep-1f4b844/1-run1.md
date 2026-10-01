# /prepare-bia case 1, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `10a72cdf-7116-41b3-bf31-084d5a012521`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, I need to know how sensitive they are.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold, and is this environment approved for that class?**

AI4BCM's data rules treat these as **high sensitivity**, allowed only in an approved corporate or private environment:
- BIA data and risk assessment detail. An activity list and impact criteria usually count.
- Personal data, contact lists and personnel records. An org chart with names or contact details counts.
- Security-related architecture or site detail.

For BIA work, the tool guide allows high-sensitivity data only in an enterprise, private or purpose-built BCM platform. So please confirm one of these:

1. **High sensitivity, and this environment is approved for it.** I'll read the files and start on the guide.
2. **Lower sensitivity.** For example, the org chart has roles only and no names, and the lists are generic. Tell me which class applies.
3. **High sensitivity, but this environment isn't approved, or you're not sure.** I'll stop here. You can rerun it in an approved environment, or attach versions with the sensitive detail taken out.

Also, if any file contains passwords, keys or access tokens, remove them first. Those go into no tool, approved or not.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. Before I draft, two things about the interview aren't covered by the files or your request:

1. **Who exactly is the interview with?** The Site B org chart lists a "Dispatch lead, Site B (three shift leaders)". Is it one-to-one with the dispatch lead, or will the shift leaders join? If they join, I'll set it up as a workshop and list each owner. And what does this person know that you don't? A role is enough.
2. **What do you need back from them?** For example "resources and peak weeks", "whether Site B can take Site A's manual export", or "who stands in for whom on shift". I'll make sure each item on your list is covered by at least one question.

You've attached impact criteria v1.1 (4 Feb 2026, approved), so I won't ask for those. Any questions about how dispatch actually runs will go into the guide for the dispatch lead to answer.

The BCM practitioner who runs the interview will check the guide against its sources. Nothing I draft goes into the register until the activity owner confirms it.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

From Site A activity list v3, 12 Mar 2026, approved by the Site A site manager
From Impact criteria v1.1, 4 Feb 2026, approved by top management
From Site B organisation structure: undated draft from HR, no version (see Gaps; not used as current)

**Reviewer:** the BCM practitioner who runs the interview checks this guide against its sources. A drafted requirement goes into the register only once the dispatch lead confirms it. The owner sets MTPD and RTO, and top management approves the BIA results.

# Interview guide: Dispatch (chilled), Site B

**Interviewee:** Dispatch lead, Site B
**Purpose:** to find out what dispatch at Site B needs to run (resources), and when it is busiest (peak weeks)

## Candidate requirements (each one is a question for the dispatch lead)

Every entry below comes from **Site A** data. None of it is known to apply at Site B. Use the draft as something to correct, not something to confirm.

| # | Class | Candidate, phrased as a question | Source | Label | MTPD | RTO | RPO |
|---|---|---|---|---|---|---|---|
| C1 | Activity | Is "Dispatch, chilled" at Site B the same activity as Site A's A2? | Site A list v3, row A2 | candidate, to confirm | | | |
| C2 | Peak weeks | Is dispatch at Site B busiest in weeks 49–52? | Site A list v3, row A2, Peak weeks: "weeks 49–52, week 14" | candidate, to confirm | | | |
| C3 | Peak weeks | Does Site B dispatch peak in week 14? | as C2 | candidate, to confirm | | | |
| C4 | IT and applications | Does dispatch at Site B need the warehouse system LogiStock? | Site A list v3, row A2, Notes: "warehouse system "LogiStock"" | candidate, to confirm | | | |
| C5 | IT and applications | Does Site B need to receive the manual export from Site A's LogiStock? | Site A list v3, row A2, Notes: "manual export to Site B possible" | candidate, to confirm | | | |
| C6 | Suppliers | Does dispatch at Site B depend on the carrier NordFrost? Is there a second carrier? | Site A list v3, Dependencies: "A1 and A2 depend on NordFrost (no second carrier recorded)" | candidate, to confirm | | | |
| C7 | Dependency, upstream | Does dispatch at Site B need quality release (A3, QA manager, Site A) before goods go out? | Site A list v3, Dependencies: "A2 depends on A3 (release before dispatch)"; row A3, Notes: "lab at Site A only" | candidate, to confirm | | | |

There are no candidates for **people and their mandates**, **seats and buildings**, or **downstream dependencies**. The approved sources don't cover them (G4–G6), so the questions below ask about them openly.

*Note on recovery times:* none of the sources proposes an MTPD, RTO or RPO. All recovery fields are left empty.

## Interview questions

*Read this out at the start: "This list was drafted from Site A's records, so some of it will be wrong for Site B. Please correct anything that doesn't fit. 'I don't know' is a useful answer."*

**Peak weeks**
1. At Site A, chilled dispatch is busiest in weeks 49–52. Is that also true at Site B? (C2)
2. Site A also has a peak in week 14. Does Site B have a peak then? (C3)
3. Are there any other weeks when Site B dispatch is especially busy? (C2, C3)
4. In your busiest week, roughly how much more goes out than in a normal week?

**People and shifts**
5. What shift pattern does dispatch work at Site B? (G4)
6. How many shift leaders does dispatch have? (G1)
7. What is the smallest number of people a shift needs to get dispatch out? (G4)
8. Which dispatch tasks need a particular skill or training? (G4)
9. Which dispatch decisions need someone with a specific authority or sign-off? (G4)
10. Who stands in for you when you're not available? (G4)
11. Do you need extra people in peak weeks? (G4)
12. Where do those extra people come from? (G4)

**IT and applications**
13. Does dispatch at Site B use LogiStock? (C4)
14. If not, which system do you use to plan or record dispatch? (C4)
15. Which other applications does dispatch need in order to run? (G4)
16. Site A's records say a manual export from LogiStock to Site B is possible. Does Site B receive that export today? (C5)
17. What would Site B need in order to work from that export? (C5)

**Carriers and other suppliers**
18. Which carriers collect chilled goods from Site B? (C6)
19. Is NordFrost one of them? (C6)
20. Is there a second carrier you could call if your main carrier couldn't collect? (C6)
21. Who holds the carrier contacts for Site B? (C6)
22. Where are those contacts kept? (C6)
23. Which other suppliers does dispatch depend on? (G4)

**Seats and buildings**
24. Which areas of Site B does dispatch need in order to run? (G5)
25. How many workplaces does dispatch need? (G5)
26. Does dispatch need more space in peak weeks? (G5)

**Dependencies on other departments**
27. At Site A, nothing is dispatched until QA has released it. Does dispatch at Site B also wait for a quality release? (C7)
28. Who does that release for Site B? (C7, G1)
29. Which other departments does dispatch rely on before goods can go out? (G6)
30. Which departments rely on dispatch at Site B? (G6)
31. Does Site B ever dispatch goods on Site A's behalf? (C5)

**Closing**
32. Is there anything else we should know?

## Gaps

- **G1. Site B org chart:** an undated draft from HR with no version, so I haven't used it as current. It mentions "three shift leaders" and "QA: covered from Site A"; questions 6 and 28 check both. *To settle it:* HR issues a dated, versioned chart.
- **G2. Your statements, not sources:** the interview is with the dispatch lead at Site B, who knows the shift pattern and the carrier contacts, and you need resources and peak weeks back. These shaped the scope but set no values.
- **G3. No Site B activity list.** Every candidate comes from Site A and may not apply at Site B. *To settle it:* this interview.
- **G4. People and mandates for dispatch:** not in the sources.
- **G5. Seats and buildings for dispatch:** not in the sources. Site A's "two dock doors" belong to goods receipt (A1), not dispatch, so I haven't carried them over.
- **G6. Downstream dependencies on other departments:** not in the sources.
- **G7. Impacts, MTPD, RTO and RPO:** outside your list for this interview, and the fields are left empty. The owner sets them in a later step against impact criteria v1.1.
- **G8. Site A activity list:** approved 12 March 2026. *To settle it:* the Site A BCM manager confirms v3 is still the current version.
- None of the material contains instructions aimed at an AI.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
