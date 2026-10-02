# /prepare-bia case 1, run2: Claude Code, guidance at 88370c8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `71e53b7c-27fd-426b-a68d-2ac8a0c4d83e`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the attached files, I need to know one thing:

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` contain?** For example: public, internal, confidential or strictly confidential. If your organisation uses its own classification scheme, give the label from that scheme.

I won't read the files until I have your answer. I'll then check that this environment is approved for that class, using `units/data-rules.md`, Sensitivity classes. If it isn't approved, I'll stop there.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R; echo ----; cd /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

The environment is approved for high-sensitivity data, so I've read the three attached files. Before drafting I have three questions about things the material leaves open. Your answers will be listed in the draft under Gaps as your own statements, not as sources. They can shape the scope of the guide but won't fill in any value. If you skip a question, I'll write down the assumption I made instead.

1. **Who is the interviewee, and what do you know that the files don't?** The Site B org chart (an undated draft, no version) shows a "Dispatch lead, Site B" with three shift leaders. Is that the person you're interviewing, will any shift leaders join, and do they have the authority to confirm requirements for Site B dispatch? Also tell me anything you already know about Site B dispatch that the files leave out, such as its systems, carriers, peak weeks or how it links to Site A. If you don't know, say so and I'll leave it as a question for the interview.
2. **What do you need back?** For example: a guide for one interview of a given length, a question list only, or a guide plus a candidate register table for Site B dispatch.
3. **Are memory, past chats, project files, connectors and web search switched off in this environment?** I'm only using the three files here, but if any of those is on, the model may draw on it without saying so. I'll note any that are still on under Gaps.

You attached the impact criteria (v1.1, 4 February 2026, approved by top management), so I don't need to ask for them.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run2/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (pre-interview draft)

**Sources**
- `site-a-activity-list.md`: Site A activity list (chilled food production), version 3, 12 March 2026, "approved by the site manager".
- `impact-criteria.md`: Impact criteria, version 1.1, 4 February 2026, "approved by top management".
- `site-b-org-chart.md`: no version or date. It is listed under Gaps and is not used as a current source.

**Interviewee:** Dispatch lead, Site B (your statement, see Gaps).
**Focus you asked for:** resources and peak weeks. The seven sections below follow the standard order. Sections 3–7 and the peak-week questions in section 1 carry most of the weight.

**For the interviewer:** Use the draft as the thing to correct, not the thing to confirm, and record what it could not have known. Site B has no register of its own. Every entry below is based on Site A's dispatch activity (A2), so assume it may be wrong for Site B.

---

## Candidate activity

| # | Candidate activity | Owner (role) | Label | Source |
|---|---|---|---|---|
| B-D1 | Is there a chilled dispatch activity at Site B, and does it match Site A's "Dispatch, chilled"? | Dispatch lead, Site B | candidate, to confirm | Site A list, row A2; Gaps (interviewee role) |
| B-D2 | Does Site B dispatch anything other than chilled goods, or carry out any activity Site A doesn't (for example, receiving Site A's "manual export")? | Dispatch lead, Site B | candidate, to confirm | Site A list, row A2 Notes |

## 1. Impacts over time

| # | Question for the activity owner | Label | Source |
|---|---|---|---|
| 1.1 | Site A's dispatch peaks in "weeks 49–52, week 14". What are Site B's dispatch peak weeks? | candidate, to confirm | Site A list, row A2 |
| 1.2 | Does the shift pattern change in the peak weeks? If so, how? | candidate, to confirm | Gaps (organiser: interviewee knows the shift pattern) |
| 1.3 | If dispatch stops, after how many hours or days is the financial impact "EUR 10k–100k a day" (level 2), and when does it pass "over EUR 100k a day" (level 3)? Answer separately for peak and off-peak weeks. | candidate, to confirm | Impact criteria, Financial column |
| 1.4 | When is "a key account is late" (level 2) reached, and when "a key account is lost" (level 3)? | candidate, to confirm | Impact criteria, Customer column |
| 1.5 | Can a dispatch stoppage lead to "a report to the food authority" (level 2) or to "the authority stops production" (level 3)? Through what, for example chilled goods held too long? | candidate, to confirm | Impact criteria, Regulatory column |

## 2. MTPD

| # | Question for the activity owner | MTPD | Label | Source |
|---|---|---|---|---|
| 2.1 | Based on your answers to section 1, after what time does a dispatch stoppage become unacceptable? Is that different in peak weeks? | *(blank, set by the owner)* | candidate, to confirm | Impact criteria; Site A list, row A2 |

## 3. People, with the skills, authorities and mandates the work needs

| # | Question for the activity owner | Label | Source |
|---|---|---|---|
| 3.1 | How many people does dispatch need per shift, at the minimum and in the peak weeks? | candidate, to confirm | Gaps (shift pattern: organiser statement; staffing: not in the sources) |
| 3.2 | Who can stand in for you, and for each of the three shift leaders? Is any task held by only one person? | candidate, to confirm | Gaps (org chart is an undated draft) |
| 3.3 | Who has the mandate to release a shipment that is short or late, or to switch carrier? | candidate, to confirm | not in the sources |
| 3.4 | Who holds the carrier contacts, and are they written down anywhere other than with you? | candidate, to confirm | Gaps (organiser statement) |
| 3.5 | Which skills are needed (for example, chilled goods handling, the warehouse system), and how many people have each one? | candidate, to confirm | not in the sources |

## 4. Seats and buildings

| # | Question for the activity owner | Label | Source |
|---|---|---|---|
| 4.1 | How many dispatch dock doors and how much chilled staging space does Site B have? (Site A records "two dock doors" for goods receipt only, not for dispatch.) | candidate, to confirm | Site A list, row A1 Notes; Site B: not in the sources |
| 4.2 | Where do the shift leaders work (office, desk, terminal), and can that work be done elsewhere? | candidate, to confirm | not in the sources |
| 4.3 | Could dispatch move to Site A, or does Site A's dispatch move to Site B ("manual export to Site B possible")? Which way does it work, and how much volume can it take? | candidate, to confirm | Site A list, row A2 Notes |

## 5. IT and applications, each with its RTO and its RPO

| # | Question for the activity owner | RTO | RPO | Label | Source |
|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use "LogiStock"? Is it the same instance as Site A's? | *(blank)* | *(blank)* | candidate, to confirm | Site A list, row A2 Notes |
| 5.2 | Is there a manual fallback (paper picking lists, export), and how long can you work on it? | *(blank)* | *(blank)* | candidate, to confirm | Site A list, row A2 Notes ("manual export") |
| 5.3 | Which other systems does dispatch use (carrier booking, temperature logging, labelling)? | *(blank)* | *(blank)* | candidate, to confirm | not in the sources |

## 6. Suppliers and other third parties

| # | Question for the activity owner | Label | Source |
|---|---|---|---|
| 6.1 | Which carriers does Site B dispatch use? Is NordFrost one of them? | candidate, to confirm | Site A list, rows A1 and A2, Dependencies; Gaps (organiser: carrier contacts) |
| 6.2 | Site A records "no second carrier recorded". Does Site B have a second carrier, or an arrangement for one? | candidate, to confirm | Site A list, Dependencies |
| 6.3 | Which other third parties does dispatch need (packaging, cooling maintenance, temperature monitoring)? | candidate, to confirm | not in the sources |

A single carrier or a single person behind a resource is a question for the activity owner to answer, not a finding.

## 7. Dependencies: up- and downstream relationships with other departments, each recorded with the RTO the relationship carries

| # | Question for the activity owner | Direction | RTO of the relationship | Label | Source |
|---|---|---|---|---|---|
| 7.1 | At Site A, dispatch depends on quality release ("release before dispatch"). Does Site B dispatch wait for release from Site A's QA, and how is the release passed on? | upstream | *(blank)* | candidate, to confirm | Site A list, Dependencies and row A3 ("lab at Site A only"); Gaps (org chart: "QA: covered from Site A") |
| 7.2 | Does dispatch depend on the Site B warehouse (picking, goods receipt)? | upstream | *(blank)* | candidate, to confirm | Gaps (org chart, undated draft) |
| 7.3 | Does Site A's dispatch rely on Site B (the "manual export to Site B")? If so, Site B dispatch is downstream of Site A dispatch. | upstream/downstream | *(blank)* | candidate, to confirm | Site A list, row A2 Notes |

**Note on recovery times:** none of the sources proposes an MTPD, RTO or RPO. All recovery fields stay blank.

---

## Comparing registers across sites

Only Site A has an attached register. Site B has none yet, so I can't name any conflicts between the two. Two points need to go to both owners (the Dispatch lead at Site A and the Dispatch lead at Site B), not to the model:
- Site A's dependencies list A2→A3 and NordFrost, but no relationship with Site B, even though row A2 mentions a "manual export to Site B". If 7.1 or 7.3 is confirmed, the relationship has to appear in both registers.
- If Site B uses NordFrost (6.1), both sites depend on the same carrier, and Site A records "no second carrier".

## Gaps

- **Your own statements, not sources:** the interviewee is the Dispatch lead at Site B; they know the shift pattern and the carrier contacts; you need the resources and peak weeks back. These shape the scope but fill in no value.
- **Question 3 not answered:** you didn't say whether memory, past chats, project files, connectors and web search are switched off. I assumed they may be on. If any is on, the model may draw on it without saying so. I used only the three attached files.
- **`site-b-org-chart.md`:** "Undated draft from HR, no version." Not used as current. What would settle it: an approved, dated org chart from HR.
- **Not in the sources:** Site B dispatch volumes, staffing, systems, carriers, dock capacity, peak weeks, and any Site B impact data. The interview settles these.
- **Instructions found in the material:** none.

## For the auditor

Every entry is labelled "candidate, to confirm". In this pre-interview draft these three fields stay blank: the interview (date and interviewee), the date the owner confirmed it, and the recovery times the owner set.

| Entry | Source | Interview | Confirmed on | MTPD / RTO / RPO |
|---|---|---|---|---|
| all of the above | as cited | *(blank)* | *(blank)* | *(blank)* |

## Reviewer

- **Activity owner, Dispatch lead, Site B:** confirms each requirement and sets MTPD and RTO.
- **Top management:** approves the BIA results.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
