# /prepare-bia on Claude Code: case 1-guide, final round

Date 2026-10-01. Skill text at commit f05ad10 (guidance repo HEAD). Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, fresh scratch folder (`evals-roundA/prepare-bia/1`) with the case files copied in (impact-criteria.md, site-a-activity-list.md, site-b-org-chart.md); later turns with `--resume`. Session b4a10649-0e86-47ac-9c8a-9e5b6f6d5900. One run; no crash. Turn 1 attempted one `ls` through Bash, denied by the permission mode; no attachment was read before the data class was answered.

## Turn 1

**Request:**

> /prepare-bia The three files in this folder (site-a-activity-list.md, impact-criteria.md, site-b-org-chart.md) are attached. Draft the guide for the dispatch interview at Site B.

**Reply** (is_error False):

Before I open the three files, one question (the preflight requires it before any attachment is read):

**What class of data do these files hold, and is this environment approved for it?**

From the names, they probably contain BIA data (the activity list and impact criteria) and personnel or org detail (the Site B org chart). Under AI4BCM's data rules (`units/data-rules.md`, Sensitivity classes), both are **high-sensitivity**, so they can only be handled in an approved corporate or private environment whose permissions and retention have been checked.

Please confirm one of these:
- **"High-sensitivity, and this environment is approved for it."** I'll read the files and continue.
- **"Lower sensitivity"** (for example anonymised or test data). Tell me which, and I'll continue.
- **"Not approved."** I'll stop here and won't read the files.

## Turn 2

**Request:**

> high, and this environment is approved for high

**Reply** (is_error False):

I've read the three files. Before I draft anything, two questions about the interview:

1. **Who is the interview with?** I'm assuming the **Dispatch lead, Site B**. That's the role the Site B org chart names for dispatch. But the org chart is an undated HR draft with no version, so I can't treat it as current. Is that the right person, and will any of the three shift leaders join? Also, what does the interviewee know that you don't? For example, whether Site B also uses LogiStock, or has its own carriers.
2. **What do you need back from them?** For example, "resources and peak weeks", "dependencies on Site A quality release", or "carriers other than NordFrost".

The impact criteria (v1.1, 4 Feb 2026, approved by top management) are attached, so I don't need to ask for them.

The guide's reviewer is **the BCM practitioner who runs the interview**. They check the guide against its sources before using it. A drafted requirement only goes into the register once the Dispatch lead confirms it. The owner sets MTPD and RTO, and top management approves the BIA results.

## Turn 3

**Request:**

> The interview is with the dispatch lead at Site B; they know the shift pattern and the carrier contacts. What I need back: resources and peak weeks.

**Reply** (is_error False):

Source versions:
- from Site A activity list v3, 12 Mar 2026 (approved by the site manager)
- from impact criteria v1.1, 4 Feb 2026 (approved by top management)
- Site B organisation structure: undated, no version, HR draft. Listed under Gaps and not used as current.

**Reviewer:** the BCM practitioner who runs the interview checks this guide against the three sources. Nothing below enters the requirements register until the Dispatch lead, Site B confirms it. The owner sets MTPD and RTO, and top management approves the BIA results.

---

# Interview guide: Dispatch, chilled, Site B (DRAFT)

**Interviewee:** Dispatch lead, Site B. The organiser says they know the shift pattern and the carrier contacts.
**Needed back:** resources and peak weeks.

## 1. Candidate activity and resource requirements

There is no activity list for Site B. Every entry below is taken from Site A's activity A2 ("Dispatch, chilled") and is a question for the Dispatch lead, not a fact about Site B.

**Activity:** Dispatch, chilled, Site B. *Candidate, to confirm.* Source: Site A activity list, row A2.
**MTPD:** _(blank, for the owner)_

| Class | Candidate requirement (question for the owner) | Label | Source | RTO | RPO |
|---|---|---|---|---|---|
| Peak weeks | Are Site B's dispatch peaks the same as Site A's, "weeks 49–52, week 14"? | candidate, to confirm | Site A list, A2 | – | – |
| People and mandates | Is dispatch run by a Dispatch lead with shift leaders under them? | candidate, to confirm | Site B org chart (undated draft) | – | – |
| People and mandates | Which skills and authorities does a shift need to release a dispatch? | candidate, to confirm | not in the sources | – | – |
| Seats and buildings | Which dock doors and loading areas does dispatch at Site B need? | candidate, to confirm | not in the sources (Site A records "two dock doors" for goods receipt, A1, not for dispatch) | – | – |
| IT and applications | Does dispatch at Site B need the warehouse system "LogiStock"? | candidate, to confirm | Site A list, A2 | _(blank)_ | _(blank)_ |
| IT and applications | Does Site B receive a "manual export" from Site A, and does dispatch depend on it? | candidate, to confirm | Site A list, A2 ("manual export to Site B possible") | _(blank)_ | _(blank)_ |
| Suppliers | Does dispatch at Site B depend on the carrier NordFrost? | candidate, to confirm | Site A list, dependencies ("A1 and A2 depend on NordFrost") | – | – |
| Suppliers | Is there a second carrier? | candidate, to confirm | Site A list, dependencies ("no second carrier recorded") | – | – |
| Dependency, upstream | Does dispatch at Site B wait for quality release from Site A? | candidate, to confirm | Site A list, dependencies ("A2 depends on A3 (release before dispatch)"); A3 "lab at Site A only"; Site B org chart (draft): "QA: covered from Site A" | _(blank)_ | – |
| Dependency, downstream | Which departments or customers receive what dispatch sends out? | candidate, to confirm | not in the sources | _(blank)_ | – |

*Note on recovery times:* none of the sources proposes an MTPD, RTO or RPO for dispatch, so there is nothing to test against the impact criteria (v1.1).

## 2. Interview questions

*Please answer from your own experience at Site B. "I don't know" is a useful answer, so say it whenever it applies. The draft above came from another site, so correcting it is more useful than confirming it.*

**A. The activity**
1. Is "Dispatch, chilled" the right name for what your team does at Site B?
2. Does your team dispatch anything other than chilled goods?

**B. Peak weeks**
3. In which weeks of the year is dispatch busiest at Site B?
4. Site A's peaks are weeks 49–52 and week 14. Do Site B's peaks differ?
5. What makes those weeks busier: volume, customers or something else?
6. Are there busy days within a normal week?

**C. People and shifts**
7. How many shifts does dispatch at Site B run?
8. How many shift leaders do you have today?
9. How many people does a shift need at minimum to keep dispatching?
10. Which tasks can only certain people do?
11. Who may authorise a dispatch when you are absent?
12. Who stands in for a shift leader who is absent?

**D. Carriers**
13. Which carriers collect from Site B today?
14. Is NordFrost one of them?
15. Is there a second carrier you could use if your main one failed?
16. Who holds the carrier contacts, and where are they kept?

**E. Systems**
17. Which system does dispatch at Site B work in?
18. Is that LogiStock, the system Site A uses?
19. Does Site B receive a manual export from Site A?
20. If it does, what does your team use that export for?
21. Can dispatch continue on paper if the system is down?

**F. Building and docks**
22. How many dock doors does dispatch use at Site B?
23. Which other areas does dispatch need, such as chilled staging or an office?
24. Is any of that space shared with goods receipt?

**G. Who you depend on, and who depends on you**
25. Must goods be released by QA before you dispatch them?
26. Does that release come from Site A?
27. Besides QA, which other departments must deliver something before you can dispatch?
28. Who receives what you dispatch?

**Closing**
29. Anything else we should know?

---

## Gaps

- **Site B organisation structure:** "Undated draft from HR, no version". It isn't used as current. The shift leader count and "QA: covered from Site A" go to the owner (questions 8, 25 and 26). Settled by a dated, approved version from HR.
- **No Site B activity list.** Every candidate comes from Site A, A2. Settled by the interview.
- **"manual export to Site B possible"** (Site A, A2): the sources don't say what is exported or which way. Questions 19–20.
- **Second carrier:** "no second carrier recorded" for Site A. Not in the sources for Site B. Question 15.
- **Mandates, dock doors, staging space and downstream dependencies at Site B:** not in the sources.
- **Recovery fields** (MTPD, RTO, RPO, and the dependency RTOs) are left blank for the owner.
- **Organiser's statements (not sources):** the interviewee is the Dispatch lead, Site B; they know the shift pattern and the carrier contacts; the organiser needs back resources and peak weeks. *Assumption:* impacts and MTPD are not in scope for this interview, so the guide has no impact questions.
- No instructions to an AI were found in the attached material.

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (/prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
