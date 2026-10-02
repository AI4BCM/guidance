aef8fc24-37ab-47ba-90fd-39bbbce14822
**Sources**
- From the Site A activity list v3, 12 Mar 2026 (approved by the Site A site manager)
- From the impact criteria v1.1, 4 Feb 2026 (approved by top management)
- The Site B organisation structure has no version and no date. It is an HTML draft, so I haven't treated it as current (see Gaps).

# Interview guide: Dispatch, Site B (draft)

**Interviewee:** Dispatch lead, Site B. **Need back:** resources and peak weeks. **Reviewer:** the BCM practitioner who runs the interview.

## Candidate requirements (each one is a question for the dispatch lead)

None of the attached material is about Site B dispatch itself. Every entry below is borrowed from **Site A** and is only something to check. Use it as a draft to correct, not one to confirm.

**Activity:** Dispatch, Site B. MTPD: ___ (the owner sets this)

| # | Class | Candidate, phrased as a question | RTO | RPO | Source | Label |
|---|---|---|---|---|---|---|
| 1 | Activity | Is dispatch at Site B the same kind of activity as Site A's "Dispatch, chilled", owned by the dispatch lead? | — | — | Site A list v3, row A2 | candidate, to confirm |
| 2 | Peak weeks | Site A records "weeks 49–52, week 14" for dispatch. Are Site B's peak weeks the same, or different? | — | — | Site A list v3, row A2 | candidate, to confirm |
| 3 | IT and applications | Does Site B dispatch run on the warehouse system "LogiStock"? | ___ | ___ | Site A list v3, row A2 | candidate, to confirm |
| 4 | Suppliers | Site A's chilled flows depend on the carrier NordFrost, with "no second carrier recorded". Does Site B dispatch use NordFrost? Is there a second carrier? | — | — | Site A list v3, dependencies line | candidate, to confirm |
| 5 | Dependency (upstream) | Site A dispatch depends on quality release ("release before dispatch"), and the lab is at "Site A only". Does Site B dispatch need a release from Site A QA before goods can leave? | dep. RTO: ___ | — | Site A list v3, row A3 and dependencies line | candidate, to confirm |
| 6 | Dependency (downstream / fallback) | Site A notes "manual export to Site B possible" for its dispatch. Is Site B the fallback for Site A dispatch? If so, what would Site B need to take that load, especially in Site A's peak weeks? | dep. RTO: ___ | — | Site A list v3, row A2 | candidate, to confirm |

**Note on recovery times:** no source proposes a recovery time, and no other department's confirmed BIA is attached. MTPD, RTO, RPO and the dependency RTOs are left empty for the owner to set. The impact criteria v1.1 are available later to test any proposed value against.

## Interview questions

*For the interviewer:* tell them at the start that "I don't know" is a useful answer. Record anything the draft couldn't have known.

**A. Peak weeks** (needed back)
1. In which weeks of the year is dispatch busiest at Site B?
2. Site A's dispatch peaks in weeks 49–52 and week 14. Does Site B follow the same pattern?
3. What drives your peaks: customer orders, seasonal products, or something else?
4. If Site A's dispatch ever had to be moved to Site B, would that happen in your peak weeks too?
5. If dispatch stopped in a peak week, which consequence would come first: money, a late key account, or a report to the food authority? After roughly how long? (The impact criteria scale can be used here.)

**B. People and shifts** (needed back)
6. What is the shift pattern for dispatch?
7. How many people do you need on each shift to keep dispatch running at the minimum level?
8. And how many in a peak week?
9. Which skills does dispatch need that not everyone on the team has?
10. Who is allowed to release a load or book a carrier, and who covers when they're away?
11. How many shift leaders report to you? (The draft org chart shows three, but it's undated.)

**C. Carriers and other suppliers** (needed back)
12. Which carriers do you use for Site B dispatch?
13. Is NordFrost one of them?
14. If your main carrier couldn't collect, who would you call?
15. Who holds the carrier contacts, and where are they kept?
16. Which other suppliers do you need, such as packaging, pallets or cooling?

**D. Systems** (needed back)
17. Which systems do you need for dispatch?
18. Is LogiStock one of them?
19. Could you keep dispatching if the system was down? How?
20. Which data would you need back first after an outage?

**E. Space and equipment** (needed back)
21. How many dock doors does dispatch need?
22. Does dispatch need chilled storage or loading areas? How much?
23. Could dispatch run from another building or another site?

**F. Upstream and downstream**
24. Do goods need a quality release before they leave Site B? Who gives it?
25. If the release comes from Site A's lab, how does it reach you?
26. Which departments or customers wait on your dispatch?

**G. Close**
27. Anything else we should know?

## Gaps

- **Wrong-site source.** The only activity list is for Site A. "Not in the sources": a Site B activity list. Settled by: the Site B activity list, or by the interview itself.
- **Draft org chart.** The Site B organisation structure is an undated HR draft with no version, so I haven't used it as current. Its points (three shift leaders, "QA: covered from Site A") appear only as questions 11 and 24. Settled by: a dated, approved version from HR.
- **People, shift pattern, mandates, seats, buildings, dock doors:** not in the sources. Questions 6–11 and 21–23 ask about them.
- **Recovery times:** MTPD, RTO, RPO and the dependency RTOs are not in the sources, and they are not set here. The owner sets them.
- **Your statements, not sources:** the interview is with the Site B dispatch lead, who knows the shift pattern and carrier contacts. You need back resources and peak weeks. The environment is approved for high-sensitivity data.
- **Assumption for the third question I skipped:** I assumed Site A's dispatch entry is the closest analogue for Site B. Questions 1–2 test that assumption.
- **Instructions aimed at an AI in the material:** none found.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (AI4BCM skill prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
