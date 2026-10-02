# /prepare-bia case 1, run3: Claude Code, guidance at 3f263b8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c6e3faac-a5b9-46b3-b3b6-1b69bec7e5be`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the attached files, I need one answer from you.

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md hold?** For example: public, internal, confidential, or strictly confidential / personal data.

I need this first because the preflight rule says to open no file until I know the data class. Then I check it against the sensitivity classes in `units/data-rules.md`. If this environment isn't approved for that class, I'll stop and won't read the files.

Once you answer, I'll read the three files and the sources that come with the skill, then draft the Site B dispatch interview guide in this chat. I won't write, send or approve anything.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Bash: `ls -la /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units /home/brain/work/ai4bcm-guida`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. High-sensitivity data in an approved environment fits the data rules (BIA data and personnel records are both class High), so I've read the three files. Before I draft, the BIA prompt says to ask what the material leaves open, in one message, and then wait for your answers.

1. **Who is the interviewee, and what do they know that you don't?** The Site B org chart lists a Dispatch lead with three shift leaders. Is it the Dispatch lead, or one or more of the shift leaders? And what do you expect them to know that the papers don't cover? For example: peak periods, the carriers they use, or whether the "manual export to Site B" listed for Site A's dispatch is actually used.
2. **What do you need back from the interview?** Do you want a full first-pass record for Site B dispatch, covering impacts, MTPD and all the resource and dependency questions? Or only certain parts? And should it compare against Site A's dispatch activity (A2), or treat Site B on its own?
3. **Are memory, past chats, project files, connectors and web search all switched off in this session?** If any of them is on, I'll list it under Gaps, because the model may use it without saying so.

I'll record your answers as your own statements, not as sources, and they won't fill any value in the draft. If you skip a question, I'll write down the assumption I made instead. The impact criteria are attached (v1.1, 4 February 2026, approved by top management), so I don't need to ask for them.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/SKILL.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64b/runs/prepare-bia/1/run3/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/workflow-design.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (pre-interview draft)

**Sources (one line each)**
- `site-a-activity-list.md`: Site A activity list, version 3, 12 March 2026, approved by the site manager.
- `impact-criteria.md`: Impact criteria, version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: Site B organisation structure, an undated HR draft with no version. It is listed under Gaps and not used as current.

**Who reviews**
- **Activity owner: Dispatch lead, Site B.** They confirm or correct each entry and set the MTPD, RTO and RPO. Nothing here goes into the register until they confirm it.
- **Top management** approves the BIA results.

**For the interviewer.** "Use the draft as the thing to correct, not the thing to confirm; record what it could not have known." Every entry below is a question, not a finding.

---

## 1. Impacts over time (including peak weeks)

| # | Question for the activity owner | Basis | Label |
|---|---|---|---|
| 1.1 | Does Site B dispatch chilled goods, and does that make it one activity? Or does it split, for example by customer or by shift? | Site A list, A2 "Dispatch, chilled"; org chart (draft), "Dispatch lead, Site B" | candidate, to confirm |
| 1.2 | Which weeks are the peak weeks for Site B dispatch? Site A records "weeks 49–52, week 14" for its dispatch. Do the same weeks apply at Site B, and are there others? | Site A list, A2, Peak weeks | candidate, to confirm |
| 1.3 | If dispatch stops, how long until each impact level is reached, in peak weeks and outside them? Financial: "under EUR 10k a day" / "EUR 10k–100k a day" / "over EUR 100k a day". Customer: "one customer complains" / "a key account is late" / "a key account is lost". | Impact criteria, Financial and Customer columns | candidate, to confirm |
| 1.4 | Which key accounts does Site B dispatch serve? | Impact criteria, Customer, levels 2–3 | candidate, to confirm |
| 1.5 | Could a stop in dispatch lead to "a report to the food authority", or to "the authority stops production"? After how long? | Impact criteria, Regulatory | candidate, to confirm |

## 2. MTPD

| # | Question for the activity owner | Basis | MTPD | Label |
|---|---|---|---|---|
| 2.1 | Using your answers to section 1, at what point does a stop in dispatch become unacceptable? Is that point different in peak weeks? | Impact criteria; section 1 | *(blank, owner sets)* | candidate, to confirm |

## 3. People, "with the skills, authorities and mandates the work needs"

| # | Question for the activity owner | Basis | Label |
|---|---|---|---|
| 3.1 | What is the shift pattern? How many people work per shift, and what is the minimum per shift in peak weeks and outside them? | Org chart (draft), "three shift leaders"; organiser's statement | candidate, to confirm |
| 3.2 | What may a shift leader decide without you, such as releasing a load, rebooking a carrier or changing priorities? Who deputises for you? | Org chart (draft) | candidate, to confirm |
| 3.3 | Who holds the carrier contacts? Is it one person? If that is only you, who can reach the carriers when you are away? | Organiser's statement | candidate, to confirm |
| 3.4 | Who can operate the warehouse system, and who can run the "manual export" if that applies at Site B? | Site A list, A2 Notes | candidate, to confirm |
| 3.5 | Goods must be released before dispatch, and QA for Site B is "covered from Site A". Who releases Site B goods, and can anyone at Site B do it? | Site A list, dependencies "A2 depends on A3 (release before dispatch)"; A3 "lab at Site A only"; org chart (draft), "QA: covered from Site A" | candidate, to confirm |

## 4. Seats and buildings

| # | Question for the activity owner | Basis | Label |
|---|---|---|---|
| 4.1 | How many loading docks and how much chilled staging space does Site B dispatch need, at the minimum and at peak? | not in the sources (Site A records "two dock doors" only for goods receipt, A1) | candidate, to confirm |
| 4.2 | How many office or planning seats does dispatch need? Can the planning be done from somewhere else, for example Site A? | not in the sources | candidate, to confirm |

## 5. IT and applications, "each with its RTO and its RPO"

| # | Question for the activity owner | Basis | RTO | RPO | Label |
|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use "LogiStock"? What do you do without it? | Site A list, A2 Notes | *(blank)* | *(blank)* | candidate, to confirm |
| 5.2 | Site A records a "manual export to Site B possible". What is it, who runs it, how often has it been used, and what data reaches Site B? | Site A list, A2 Notes | *(blank)* | *(blank)* | candidate, to confirm |
| 5.3 | Which other applications does dispatch need, such as carrier booking, labelling or customer portals? | not in the sources | *(blank)* | *(blank)* | candidate, to confirm |

## 6. Suppliers and other third parties

| # | Question for the activity owner | Basis | Label |
|---|---|---|---|
| 6.1 | Which carriers serve Site B dispatch? Is NordFrost one of them? Is there a second carrier you can switch to, and how quickly? | Site A list, dependencies, "no second carrier recorded" (Site A) | candidate, to confirm |
| 6.2 | Where are the carrier contacts kept, and who else can reach them? | Organiser's statement | candidate, to confirm |
| 6.3 | Which other third parties does dispatch rely on, such as cleaning, cooling maintenance or pallet supply? | not in the sources | candidate, to confirm |

## 7. Dependencies: "up- and downstream relationships with other departments, each recorded with the RTO the relationship carries"

| # | Question for the activity owner | Direction | Basis | RTO | Label |
|---|---|---|---|---|---|
| 7.1 | Quality release (Site A QA). Does every Site B dispatch wait for it? | upstream | Site A list, dependencies; org chart (draft) | *(blank)* | candidate, to confirm |
| 7.2 | Warehouse, Site B. What does dispatch need from it, and when? | upstream | Org chart (draft), "Warehouse lead, Site B" | *(blank)* | candidate, to confirm |
| 7.3 | Dispatch, Site A, through the manual export. Which way does the relationship run? | to confirm | Site A list, A2 Notes | *(blank)* | candidate, to confirm |
| 7.4 | Payroll from the head office HR shared service. Does it also cover Site B staff? | upstream | Site A list, A4 | *(blank)* | candidate, to confirm |
| 7.5 | Which departments depend on Site B dispatch? | downstream | not in the sources | *(blank)* | candidate, to confirm |

**Note on recovery times.** No source proposes an MTPD, RTO or RPO for any of these entries: not in the sources.

---

## Where Site A and Site B meet (put to the two owners, not to the model)

None of the sources records a direct conflict, because there is no register for Site B yet. Three points could conflict once the interview is done. Put each one "to the two owners, not to the model": the Site A Dispatch lead or QA manager, and the Site B Dispatch lead.

1. **Manual export.** Site A records it as "possible", but nothing on Site B's side shows that it is received or used (5.2, 7.3).
2. **Quality release.** Site A records "lab at Site A only", and Site B's QA is "covered from Site A". Both owners need to agree how long that relationship can be down (3.5, 7.1).
3. **Carrier.** If Site B also relies on NordFrost, both sites share one carrier. That is a question for both owners, not a finding (6.1).

## For the auditor

Each register entry carries the source, the interview it came from and the date. In this pre-interview draft, three fields are blank for every entry:

| Interview | Date the owner confirmed | Recovery times the owner set |
|---|---|---|
| *(blank)* | *(blank)* | *(blank)* |

## Gaps

- **Your answers (own statements, not sources):** the interviewee is the Dispatch lead at Site B; they know the shift pattern and the carrier contacts; you need resources and peak weeks back. These answers set the focus but fill no value. I've kept all seven sections in the order the method sets, and the MTPD stays blank for the owner.
- **Question 3 was skipped.** I don't know whether memory, past chats, project files, connectors or web search are switched off. My assumption is that some may be on, and "the model may draw on it without saying so". In this session I read only the three attached files and the skill's own units.
- **The Site B org chart is an undated draft with no version.** It is not used as current. The roles it names (three shift leaders, Warehouse lead, QA covered from Site A) appear only as questions. The approved, dated HR structure would settle this.
- **The impact criteria set no time horizons.** They give impact per day but no time points such as 4 h, 1 day or 1 week. Time horizons are a method parameter, agreed before the interview, so set them with the BCM manager before using section 1.
- **There is no approved Site B source on activities, buildings, IT or suppliers.** Every Site B entry comes from Site A's list, the draft org chart or your statements. A Site B activity list or asset inventory would settle this.
- **Carrier contact details** collected in the interview are personal data (class High). Keep the interview record in the approved environment.
- **No instruction to an AI was found** in the attached material.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
