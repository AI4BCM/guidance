# /prepare-bia case 1, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `41bb229a-6c67-49b8-86bd-e47c40cbd41f`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attachments I need one answer from you. I'm asking it on its own, and it doesn't count toward the interview questions that come later.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold, and is this environment approved for that class?**

Under the AI4BCM data rules, these count as high sensitivity: BIA data and risk-assessment detail, personal data such as names, contact lists and personnel records, and security-related site detail. An org chart with names, or an activity list with BIA ratings, usually counts. High-sensitivity material may only be used in an approved corporate or private environment.

- If the files are high sensitivity and this environment is approved for that class, say so and I'll read them and continue.
- If the files are high sensitivity and this environment isn't approved, I'll stop here. You can rerun the skill in an approved environment, or attach versions with names and sensitive detail removed. For the org chart, roles are enough.
- If the files are lower sensitivity, tell me which class and I'll continue.

Once you've answered, I'll read the files. Then I'll ask only what they leave open, such as who the dispatch interviewee at Site B is and what you need back from them. After that I'll draft the guide.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The files are read. Before I draft, I need answers to a few questions the files leave open:

1. **Who is the interview with?** The Site B org chart (an undated HR draft) lists a "Dispatch lead, Site B" with three shift leaders. Is the interview with the Dispatch lead alone, or are some shift leaders joining? What do you expect them to know that you don't? The role is enough; I don't need a name.
2. **What do you need back from them?** For example: Site B's peak weeks, the systems dispatch uses, the carriers, whether dispatch depends on quality release from Site A, or the volumes and customers that drive the impact ratings. Please list the items you need, most important first.
3. **Is there any Site B material besides the org chart?** For example a system list, a carrier contract or an earlier activity list. If not, I'll draft from Site A's approved list and mark each item as a Site A analogy for the owner to confirm or correct.

The impact criteria are attached (v1.1, 4 Feb 2026, approved), so I don't need them.

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

Sources this draft was built from:
- Site A activity list, v3, 12 Mar 2026, approved by the Site A site manager.
- Impact criteria, v1.1, 4 Feb 2026, approved by top management.
- Site B organisation structure: no version and no date (a draft from HR). It is listed under Gaps.

**Reviewer:** the BCM practitioner who runs the interview checks this guide against these sources. A requirement goes into the register only once the Dispatch lead at Site B confirms it. The Dispatch lead sets MTPD and RTO, and top management approves the BIA results.

# Interview guide: Dispatch (chilled), Site B

**Interviewee:** Dispatch lead, Site B. They know the shift pattern and the carrier contacts.
**What we need back:** the resources dispatch needs, and its peak weeks.

## Candidates to correct in the interview

There are no Site B sources for dispatch. Each entry below is taken from Site A and is a question for the Dispatch lead, not a fact about Site B.

| # | Class | Candidate (to correct) | Source | Label | RTO | RPO |
|---|---|---|---|---|---|---|
| C1 | Peak weeks | Are Site B's dispatch peaks in weeks 49–52 and week 14, as at Site A? | Site A list, A2 | candidate, to confirm | — | — |
| C2 | People | Does dispatch need the Dispatch lead and three shift leaders? | Site B org chart (undated draft) | candidate, to confirm | — | — |
| C3 | People | Which shift pattern, staffing levels and authority to release shipments does dispatch need? | not in the sources | gap → questions 4–9 | — | — |
| C4 | Seats and buildings | Which docks, staging areas and offices does dispatch need? | not in the sources (the two dock doors in A1 belong to goods receipt at Site A) | gap → questions 10–12 | — | — |
| C5 | IT and applications | Does Site B dispatch use the warehouse system "LogiStock"? | Site A list, A2 | candidate, to confirm | *empty* | *empty* |
| C6 | Suppliers | Is NordFrost the carrier for Site B dispatch? | Site A list, A2 and dependencies | candidate, to confirm | — | — |
| C7 | Suppliers | Is there a second carrier? At Site A, "no second carrier recorded". | Site A list, dependencies | candidate, to confirm | — | — |
| C8 | Dependency, upstream | Does dispatch depend on quality release by QA at Site A? Site A records that A2 "depends on A3 (release before dispatch)", the lab is "at Site A only", and QA for Site B is "covered from Site A". | Site A list A3 and dependencies; Site B org chart | candidate, to confirm | *empty* (dependency) | — |
| C9 | Dependency, upstream | Does Site B dispatch handle goods coming from Site A? Site A's dispatch entry notes "manual export to Site B possible". | Site A list, A2 | candidate, to confirm | *empty* (dependency) | — |
| C10 | Dependency | Does dispatch depend on the warehouse at Site B, and which teams depend on dispatch further down the chain? | Site B org chart (role only) | gap → questions 25–26 | *empty* (dependency) | — |

**Recovery times:** none of the sources proposes an RTO, RPO or MTPD. All recovery fields stay empty for the Dispatch lead to set.

## Interview questions

*If you don't know an answer, please say so. "I don't know" is a useful answer, and we'll find out from someone else. Where we mention Site A, it's only a starting point; please correct anything that's different at Site B.*

**Peak weeks**
1. In which weeks of the year does dispatch at Site B peak? (At Site A: weeks 49–52 and week 14.)
2. What causes each of those peaks?
3. How much more do you dispatch in a peak week than in a normal week?

**People and shifts**
4. What is your shift pattern?
5. How many people does each shift need, at the least, to keep dispatch running?
6. Does that minimum rise in peak weeks?
7. Which tasks can only certain people do, for example because of training, a licence or system access?
8. Who may release or sign off a shipment when you are absent?
9. Could staff from the warehouse or from Site A cover dispatch work?

**Carriers and other suppliers**
10. Which carriers collect from Site B?
11. Is NordFrost one of them?
12. If your main carrier can't collect, is there another carrier you could call?
13. Can you reach each carrier outside office hours?
14. Which other suppliers or service providers does dispatch need in order to run?

**Systems**
15. Does dispatch at Site B use LogiStock?
16. Which other systems or applications does dispatch use?
17. Can you dispatch by hand if a system is down?
18. How long could dispatch keep going without each system?
19. If a system lost recent data, how much could you re-enter by hand?

**Seats and buildings**
20. Which parts of the site does dispatch need, for example docks, chilled staging or an office?
21. How many dock doors does dispatch need, at the least?
22. Could dispatch run from another site, for example Site A?

**Links to other teams**
23. Does a shipment have to wait for quality release from QA at Site A before it leaves?
24. How does that release reach you?
25. Does dispatch rely on the warehouse at Site B?
26. Which teams or customers are waiting on your dispatch?
27. Site A's activity list says "manual export to Site B possible". What does that mean for your work?

**Closing**
28. Anything else we should know?

## Gaps

- **Your answers to my questions:**
  - Interviewee: Dispatch lead, Site B. This is your statement.
  - They know the shift pattern and the carrier contacts. This is your statement.
  - What you need back: resources and peak weeks. This is your statement.
  - You didn't answer question 3, so I assumed there is no other Site B material. Every candidate above therefore comes from Site A.
- **The Site B org chart** is an undated draft with no version, so I haven't used it as current. The three shift leaders and the QA line come only from it. The current version from HR would settle both.
- **Impacts over time and MTPD aren't covered.** The BIA workflow covers them first in every interview, and impact criteria v1.1 is available for them. Whether to add them, or cover them in a separate session, is your call.
- **Seats and buildings:** not in the sources.
- **The Site A note "manual export to Site B possible":** it doesn't say whether it means exported data or exported goods. Question 27 covers it.
- **Second carrier:** not in the sources for either site.
- **Embedded instructions:** none of the attached files contains an instruction aimed at an AI.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
