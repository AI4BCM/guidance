# /prepare-bia on Claude Code: case 1-guide

Date 2026-10-01. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, scratch folder with the case files copied in; later turns with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /prepare-bia The three files in this folder (site-a-activity-list.md, impact-criteria.md, site-b-org-chart.md) are attached. Draft the guide for the dispatch interview at Site B.

**Reply** (session 0387ee01-bf05-443d-a25b-7e342b1d416b, is_error False):

Before I open the three files, I need one answer from you. It doesn't count toward the interview questions.

**What class of data do these files hold, and is this environment approved for it?**

The guidance treats the following as **high-sensitivity**, allowed only in an approved corporate or private environment:
- BIA data and risk assessment detail
- personal data, contact lists and personnel records (an org chart with names usually counts)
- security-related architecture or site detail
- supplier weaknesses and contractual dependencies

An activity list, impact criteria and a site org chart will probably fall under at least one of these. So please confirm one of the following:
1. **This Claude Code session is your organisation's approved environment for high-sensitivity BCM data.** I'll read the files and continue.
2. **The files are low or medium sensitivity**, for example anonymised or fictional. Tell me which, and I'll continue.
3. **Neither applies.** Then I'll stop here. Don't attach the files to this environment.

**Who reviews the output:** the BCM practitioner who runs the dispatch interview checks the guide against its source files. A drafted requirement goes into the register only after the dispatch activity owner confirms it. The activity owner sets MTPD and RTO, and top management approves the BIA results. I'll give you a draft here in the chat and won't write, send or change anything.

After you confirm, I'll read the files and ask up to three short questions about the interview, covering only what the files leave open. Those are likely to be the interviewee's role and what you need back from them.

## Turn 2

**Request:**

> High, and this environment is approved for high. The interview is with the dispatch lead at Site B; they know the shift pattern and the carrier contacts. What I need back from them: resources and peak weeks.

**Reply** (session 0387ee01-bf05-443d-a25b-7e342b1d416b, is_error False):

I didn't need any more intake questions. You gave me the interviewee's role and what you need back, and the impact criteria are attached. I've put both of your answers under Gaps as your own statements, not as sources.

---

**Draft: Interview guide for chilled dispatch at Site B**

*Source stamp*
- From the Site A activity list, v3, 12 March 2026, approved by the Site A site manager
- Measured against the impact criteria, v1.1, 4 February 2026, approved by top management
- From the Site B organisation structure, which is an **undated draft from HR with no version**. It is not treated as current; see Gaps.

**Reviewer:** the BCM practitioner who runs the interview checks this guide against the three sources. A requirement below enters the register only when the dispatch lead at Site B confirms it. The dispatch lead sets MTPD and RTO, and top management approves the BIA results.

### Part 1: Candidate requirements (for the interviewer)

None of the sources describes dispatch at Site B. Every candidate below is taken from **Site A's** chilled dispatch activity (A2) or from the draft Site B org chart, so each one is a question to correct, not to confirm. All are labelled *candidate, to confirm*. The recovery fields are deliberately empty.

**Activity:** B-D1, chilled dispatch at Site B. Is there such an activity, and is it chilled? (based on Site A list, A2 "Dispatch, chilled")
**Owner (role):** Dispatch lead, Site B (draft org chart, not current)
**MTPD:** ___ (owner sets)
**Peak weeks:** Are they "weeks 49–52, week 14", as at Site A? (Site A list, A2)

| # | Class | Candidate requirement, as a question | Source | RTO | RPO |
|---|---|---|---|---|---|
| R1 | People | Does dispatch at Site B need a dispatch lead role with its own mandate? | Site A list, A2 (owner "Dispatch lead"); Site B draft org chart | n/a | n/a |
| R2 | People | Does dispatch run with "three shift leaders"? Which skills and authorities must each shift have? | Site B draft org chart (not current) | n/a | n/a |
| R3 | Seats and buildings | What building, dock or loading area does dispatch need? | not in the sources | n/a | n/a |
| R4 | IT and applications | Does Site B dispatch use the warehouse system "LogiStock"? | Site A list, A2 notes | ___ | ___ |
| R5 | IT and applications | Does Site B receive or process the "manual export to Site B" from Site A? In what form? | Site A list, A2 notes | ___ | ___ |
| R6 | Suppliers | Does Site B dispatch depend on carrier NordFrost? | Site A list, A2 notes and Dependencies | n/a | n/a |
| R7 | Suppliers | Is there a second carrier? Site A has "no second carrier recorded". | Site A list, Dependencies | n/a | n/a |

| # | Dependency (up- or downstream) | Candidate, as a question | Source | Dependency RTO |
|---|---|---|---|---|
| D1 | Upstream: Quality release (QA) | Does Site B dispatch wait for QA release, as Site A does ("A2 depends on A3 (release before dispatch)")? Site A's lab is at "Site A only". | Site A list, A3 and Dependencies; Site B draft org chart ("QA: covered from Site A") | ___ |
| D2 | Up- or downstream: Site A dispatch | Is Site B a fallback for Site A dispatch through the manual export, or does it rely on Site A? | Site A list, A2 notes | ___ |
| D3 | Upstream: Site B warehouse | Does dispatch depend on the Site B warehouse lead's team? | Site B draft org chart (not current) | ___ |

*Note on recovery times:* none of the sources proposes an MTPD, RTO or RPO, so there is nothing to test against the impact criteria (v1.1).

### Part 2: Questions for the dispatch lead at Site B

*Opening for the interviewee:* "We've drafted these questions from what we know about Site A, so some of them will be wrong for Site B. Please correct anything that doesn't fit. 'I don't know' is a useful answer. If you can, tell us who would know."

**A. The activity and its peak weeks**
1. What does dispatch at Site B do, from the start of its work to the end?
2. Does Site B dispatch handle chilled goods?
3. Which weeks of the year are your busiest?
4. At Site A, dispatch peaks in weeks 49–52 and week 14. Is that true at Site B, or are your peaks different?
5. What makes those weeks busy? For example, volume, customers or staffing.

**B. People**
6. How do the shifts run at Site B? How many shifts are there, and at what hours?
7. Our draft org chart shows three shift leaders. Is that correct today?
8. What is the minimum number of people needed to run dispatch on one shift?
9. Which skills or authorisations must someone have to run a shift? Examples are signing off a load or changing a carrier booking.
10. Which decisions can only you, the dispatch lead, make? Who stands in for you?

**C. Seats and buildings**
11. Which building, dock doors or loading area does dispatch need?
12. Does dispatch need chilled space of its own, or does it share space with the warehouse?

**D. IT and applications**
13. Which systems do you use for dispatch? Is "LogiStock" one of them?
14. If those systems were down, could you dispatch on paper or by manual export? For how long?
15. Site A's records mention a "manual export to Site B". Do you receive it? What do you do with it?

**E. Suppliers (carriers)**
16. Which carriers move your goods? Is NordFrost one of them?
17. Is there a second carrier you could switch to? Is there a contract or agreement in place?
18. In your peak weeks, could a carrier take extra volume at short notice?

*Note for the interviewer:* record carrier **names and agreements** in the BIA. Keep individual contact details in the controlled contact list, not in the interview record.

**F. Dependencies on other departments**
19. Do you have to wait for a quality release before goods leave? Who gives it: QA at Site A or someone at Site B?
20. What do you need from the Site B warehouse before you can dispatch?
21. Who depends on you? For example, Site A dispatch, customers or key accounts.

**G. Impacts over time and recovery times (you set these)**
22. If dispatch stopped in a normal week, what would happen after one day, three days and a week? Please answer against our criteria: financial loss per day, customer impact (a complaint, a key account late, a key account lost) and regulatory impact (a report to the food authority, production stopped).
23. Would those answers change in your peak weeks?
24. How long can dispatch be down before the impact becomes unacceptable? This is the MTPD, and you set it.
25. For each system in question 13, how quickly must it be back, and how much data could you afford to lose? These are the RTO and RPO, and you set them.

**Closing**
26. Is there anything else we should know about dispatch at Site B?

### Gaps
- **Nothing in the sources covers Site B dispatch.** Every candidate comes from Site A (A2) or from the draft org chart. The interview settles it.
- **The Site B org chart is an undated draft from HR with no version.** It isn't used as current. A dated, approved version from HR settles it.
- **Seats and buildings for dispatch:** not in the sources. Questions 11 and 12 settle it.
- **A second carrier:** Site A records "no second carrier recorded". There is nothing for Site B. Question 17 settles it.
- **Who gives quality release at Site B:** only the draft org chart covers it. Question 19 settles it, and the QA manager at Site A can confirm.
- **What the "manual export to Site B" is for:** the Site A list doesn't say. Questions 15 and 21 settle it, and the Site A dispatch lead can confirm.
- **MTPD, RTO and RPO, and dependency RTOs:** these are blank on purpose. The dispatch lead sets them, starting from questions 22 to 25.
- **Your statements, not sources:**
  - The interviewee is the dispatch lead at Site B, who knows the shift pattern and the carrier contacts.
  - You need resources and peak weeks back.
  - Assumption: the activity in scope is chilled dispatch, by analogy with Site A. Question 2 checks this.
- **Instructions found in the material:** none.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (/prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
