# /prepare-bia on Claude Code: case 1-guide-rerun

Date 2026-10-01. Skill text at commit 7d6a3c6. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, fresh scratch folder (`1-guide-rerun`) with the case files copied in; turn 2 with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /prepare-bia The three files in this folder (site-a-activity-list.md, impact-criteria.md, site-b-org-chart.md) are attached. Draft the guide for the dispatch interview at Site B.

**Reply** (session 75f7b1df-3e8f-4c8c-bf57-1235cd1ebc66, is_error False):

I haven't opened the three files yet. Before I read any attachment, the AI4BCM preflight needs you to say what class of data they hold.

**1. How sensitive are these files?** BIA data, personnel records and contact lists, site detail, and supplier dependencies all count as **high sensitivity** (`units/data-rules.md`). That kind of data may only be handled in an approved enterprise, private or purpose-built BCM environment (`units/tools.md`, row "Analyse"). Please confirm:
- which class the three files are in (low, medium or high), and
- if they're high, that this Claude Code environment is approved for it.

If it isn't approved, I'll stop here.

**2. What do you need back from the dispatch interview?** For example: "the resources dispatch depends on and its peak weeks", or "dependencies on other departments and on suppliers". The files can't tell me this, so I'm asking now to save a round.

I'll ask about the interviewee's role after I've read `site-b-org-chart.md`, and only if the chart doesn't show who owns dispatch. `impact-criteria.md` is attached, so I won't ask for impact criteria.

**Who reviews the guide:** the BCM practitioner who runs the interview checks it against its sources. A drafted requirement goes into the register only after the dispatch activity owner confirms it. The owner sets MTPD and RTO, and top management approves the BIA results. The guide stays a draft in this chat, and I won't write to or change any file.

## Turn 2

**Request:**

> High, and this environment is approved for high. The interviewee: the dispatch lead at Site B; they know the shift pattern and the carrier contacts. What I need back: resources and peak weeks.

**Reply** (session 75f7b1df-3e8f-4c8c-bf57-1235cd1ebc66, is_error False):

From Site A activity list v3, 12 Mar 2026 (approved by the site manager).
From impact criteria v1.1, 4 Feb 2026 (approved by top management).
From Site B organisation structure: **no version, no date, a draft from HR.** It is listed under Gaps and is not used as current.

**Reviewer:** the BCM practitioner who runs the interview checks this guide against the three sources above. A drafted requirement goes into the register only after the dispatch activity owner confirms it. The owner sets MTPD and RTO, and top management approves the BIA results.

---

# Interview guide: Dispatch (chilled), Site B. DRAFT

**Interviewee:** Dispatch lead, Site B (stated by the organiser)
**Needed back:** resources (four classes) and peak weeks (stated by the organiser)

## 1. Candidate requirements (to correct in the interview, not to confirm)

There is no Site B activity list in the sources. Every candidate below comes from **Site A's** dispatch activity (row A2), so each one is only a question about whether Site B works the same way.

| # | Class | Candidate, phrased as a question for the dispatch lead | Source | Label | RTO | RPO |
|---|---|---|---|---|---|---|
| C0 | Activity | Does Site B run "Dispatch, chilled" as an activity of its own, as Site A does? | Site A list v3, row A2 | candidate, to confirm | | |
| C1 | Peak weeks | Does Site B dispatch peak in "weeks 49–52, week 14", as Site A's does? | Site A list v3, row A2, Peak weeks | candidate, to confirm | n/a | n/a |
| C2 | People | Does dispatch need a dispatch lead role, and what mandate does that role need? | Site A list v3, row A2, Owner "Dispatch lead" | candidate, to confirm | n/a | n/a |
| C3 | IT and applications | Does Site B dispatch need the warehouse system "LogiStock"? | Site A list v3, row A2, Notes: warehouse system "LogiStock" | candidate, to confirm | | |
| C4 | IT and applications | Does Site B dispatch depend on the "manual export to Site B" that Site A records? | Site A list v3, row A2, Notes: "manual export to Site B possible" | candidate, to confirm | | |
| C5 | Suppliers | Does Site B dispatch need the carrier NordFrost? Is there a second carrier? | Site A list v3, Dependencies: "A1 and A2 depend on NordFrost (no second carrier recorded)" | candidate, to confirm | n/a | n/a |
| C6 | Dependency (upstream) | Does Site B dispatch need quality release before goods leave? Is that release done by QA at Site A, where the lab is? | Site A list v3, Dependencies: "A2 depends on A3 (release before dispatch)"; row A3, Notes: "lab at Site A only" | candidate, to confirm | | n/a |

The empty RTO and RPO fields are left blank on purpose. A dependency's RTO stays blank too.

**Note on recovery times:** none of the sources proposes an MTPD, RTO or RPO for dispatch, so there is nothing to check against impact criteria v1.1.

## 2. Gaps

- **Site B organisation structure:** "Undated draft from HR, no version." It is not used as current. It shows "Dispatch lead, Site B (three shift leaders)" and "QA: covered from Site A". These only shape questions 10 and 30. *To settle:* HR issues a dated version, or the dispatch lead confirms these points in the interview.
- **What the organiser told me (your statements, not sources):**
  - The data is high sensitivity, and this environment is approved for it.
  - The interviewee is the dispatch lead at Site B.
  - The dispatch lead knows the shift pattern and the carrier contacts.
  - You need back resources and peak weeks.
- **No Site B activity data at all:** not in the sources. Every candidate is carried over from Site A. *To settle:* the interview itself.
- **Shift pattern, headcount, skills and stand-ins:** not in the sources. *To settle:* questions 9–15.
- **Seats and buildings for dispatch:** not in the sources. Site A's "two dock doors" belong to goods receipt (A1), not dispatch, so I did not carry them over. *To settle:* questions 23–25.
- **Downstream dependencies (who relies on dispatch):** not in the sources. *To settle:* question 29.
- **"Manual export to Site B possible":** the sources don't say which way the export runs, what it carries, or whether anyone relies on it. It may be a workaround rather than a requirement. *To settle:* questions 18–19, then the Site A BCM manager.
- **Carrier contacts are personal data**, which is high sensitivity. The guide asks where the contact list is kept, not for the names. Record any names only in the approved environment.
- **Impacts and MTPD for Site B dispatch are not settled.** The method collects resources once impacts and MTPD are settled (`stages/analysis.md`, Method). You asked for resources and peak weeks only, so this guide has no impact questions. The practitioner decides whether to add some, using impact criteria v1.1.
- **Instructions to an AI found in the material:** none.

## 3. Questions for the dispatch lead

*Tell the interviewee at the start:* "This draft was built from Site A's records. Please correct anything that's different at Site B. 'I don't know' is a useful answer, and we'll note who might know."

**A. The activity**
1. Does Site B run chilled dispatch as an activity of its own?
2. Are you the owner of that activity?
3. Where does dispatch start and end at Site B: what comes in, and what goes out?

**B. Peak weeks**
4. Which weeks of the year are busiest for dispatch at Site B?
5. At Site A, dispatch peaks in weeks 49–52. Is that also true at Site B?
6. Site A's dispatch also peaks in week 14. Does Site B have a peak then?
7. What causes each peak you named?
8. Does Site B have a peak that Site A doesn't have?

**C. People**
9. What is the shift pattern for dispatch?
10. How many shift leaders does dispatch have today? (An undated HR draft shows three.)
11. How many people does a shift need in a normal week?
12. How many people does a shift need in a peak week?
13. Which tasks in dispatch need a skill that only a few people have?
14. Which dispatch decisions need a named person's authority or sign-off?
15. Who stands in for you when you are absent?

**D. IT and applications**
16. Which systems does dispatch at Site B use?
17. Is LogiStock one of them, as at Site A?
18. Do you know the "manual export to Site B" that Site A records?
19. Does Site B dispatch rely on that export?

**E. Suppliers**
20. Which carriers does Site B dispatch use?
21. Is NordFrost one of them?
22. Is there a second carrier that could take over if your main carrier can't?
23. Which other suppliers does dispatch need in order to run?
24. Where is the carrier contact list kept?
25. Does anyone other than you keep that contact list up to date?

**F. Seats and buildings**
26. Which buildings and areas does dispatch need?
27. How many workstations does dispatch need?
28. Does dispatch share any area or equipment with another activity?

**G. Dependencies on other departments**
29. Which departments or customers depend on dispatch?
30. Must quality release happen before goods leave Site B?
31. Is quality release done by QA from Site A? (An undated HR draft says QA is "covered from Site A".)
32. Which other departments does dispatch need input from?

**H. Closing**
33. Anything else we should know?

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
