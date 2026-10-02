# /prepare-bia case 1, run2: Claude Code, guidance at cb8148b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `0c92c0bb-bac9-413d-a7d8-b341109b39a3`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open the three attached files, one question.

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` hold, and is this environment approved for that class?**

Here's why I'm asking. The guidance's sensitivity classes (`units/data-rules.md`) say these kinds of data may only be used in an approved corporate or private environment:
- BIA data and risk assessment detail (likely in the Site A activity list and the impact criteria)
- personal data, contact lists and personnel records (likely in the Site B org chart, if it names people)
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail

Please tell me:
1. Which of these classes the files contain, or that they hold none of them (for example, if names are replaced with roles).
2. Whether this Claude Code environment is approved for that class in your organisation.

If it's approved, I'll read the files and write the Site B dispatch interview guide as a draft. Recovery fields will stay blank and every entry will be marked "candidate, to confirm". If it isn't approved, I'll stop here, and you can run the skill in an environment that is approved.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md; ls -R; echo ---; cd /tmp/claude-1001/-opt-brain-37474441-4853-47e0-bd32-1e52e`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the three files and the skill's BIA prompt. Its Intake step says I have to ask you at most three questions before drafting. Your answers will go under Gaps as your own statements, not as sources, and they won't fill any value.

1. **Interviewee and what you need back.** The org chart lists a "Dispatch lead, Site B (three shift leaders)". Is the dispatch lead the person you're interviewing, and will any shift leaders attend? What do you need from the interview: candidate resource requirements only, or also the owner's first view of impacts over time and the MTPD?
2. **What they know that you don't.** What does the dispatch lead know that the material doesn't cover? For example: which warehouse system Site B uses (Site A uses "LogiStock"), which carriers Site B uses, whether Site B dispatch depends on Site A's quality release, or the peak weeks.
3. **Channels.** In the tool you'll use with this guide, are memory, past chats, project files, connectors and web search switched off? Any channel left on goes under Gaps, because the model may draw on it without saying so.

You can skip any of these. For each one you skip, I'll write my assumption under Gaps and draft anyway.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run2/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, chilled, Site B (pre-interview draft)

**Status:** draft. Every entry is labelled "candidate, to confirm". The MTPD, RTO and RPO fields are empty.

## Sources and dates

- `site-a-activity-list.md`: version 3, 12 March 2026, "approved by the site manager". Owner: BCM manager, Site A.
- `impact-criteria.md`: version 1.1, 4 February 2026, "approved by top management".
- `site-b-org-chart.md`: no version, no date, "Undated draft from HR". It is not used as a current source (see Gaps). It is cited below only as a lead to check.

## Register header (left blank before the interview)

| Field | Value |
|---|---|
| Activity | Dispatch, chilled, Site B (candidate, to confirm) |
| Activity owner | Dispatch lead, Site B (your statement, see Gaps) |
| Interview | |
| Date the owner confirmed | |
| Recovery times the owner set (MTPD / RTO / RPO) | |

**For the interviewer.** Use the draft as the thing to correct, not the thing to confirm. Record what it could not have known. Most entries come from Site A, so a "yes" to a Site A fact is not yet a Site B fact.

## 1. Impacts over time

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 1.1 | If chilled dispatch at Site B stops, after how long does each impact reach level 1, 2 and 3? Financial: "under EUR 10k a day" / "EUR 10k–100k a day" / "over EUR 100k a day". Customer: "one customer complains" / "a key account is late" / "a key account is lost". Regulatory: "none" / "a report to the food authority" / "the authority stops production". | impact-criteria.md, table | candidate, to confirm |
| 1.2 | Which weeks are Site B's dispatch peaks? Site A records "weeks 49–52, week 14" for its own dispatch. Does Site B share them? | site-a-activity-list.md, row A2 | candidate, to confirm |
| 1.3 | Does an outage in a peak week reach a higher impact level sooner than one outside the peaks? | site-a-activity-list.md, row A2; impact-criteria.md | candidate, to confirm |

## 2. MTPD

| # | Question for the activity owner | MTPD | Label |
|---|---|---|---|
| 2.1 | Given your answers in section 1, what is the longest that chilled dispatch at Site B can be disrupted before the impact becomes unacceptable? (The owner sets this value.) | | candidate, to confirm |

## 3. People, with the skills, authorities and mandates the work needs

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 3.1 | The HR draft shows "Dispatch lead, Site B (three shift leaders)". Is that current? How many people does each shift need at minimum, and in which roles? | site-b-org-chart.md (undated draft) | candidate, to confirm |
| 3.2 | What is the shift pattern, and how many shifts can run short-staffed, and for how long? | your statement (Gaps) | candidate, to confirm |
| 3.3 | Who may authorise a dispatch, and who checks that quality release has happened before goods leave? Site A records "release before dispatch". | site-a-activity-list.md, Dependencies | candidate, to confirm |
| 3.4 | Who holds the carrier contacts and can book or rebook transport? If that is one person, who covers for them? | your statement (Gaps) | candidate, to confirm |
| 3.5 | Which skills, such as warehouse system use or chilled-goods handling, does the work need, and who besides the current staff has them? | site-a-activity-list.md, row A2 | candidate, to confirm |

## 4. Seats and buildings

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 4.1 | Which areas does dispatch at Site B use, such as dock doors and chilled staging? Site A records "two dock doors" for goods receipt only. For Site B dispatch this is not in the sources. | site-a-activity-list.md, row A1 | candidate, to confirm |
| 4.2 | Can dispatch run from another area or site if these areas are unavailable? Site A records "manual export to Site B possible". Does the reverse exist? | site-a-activity-list.md, row A2 | candidate, to confirm |

## 5. IT and applications, each with its RTO and its RPO

| # | Question for the activity owner | Source | RTO | RPO | Label |
|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use the warehouse system "LogiStock", as Site A does, or another system? | site-a-activity-list.md, row A2 | | | candidate, to confirm |
| 5.2 | Site A's entry reads "manual export to Site B possible". What does Site B receive in that export, by what route, and who triggers it? | site-a-activity-list.md, row A2 | | | candidate, to confirm |
| 5.3 | Which other applications does dispatch need, such as carrier booking or labels? This is not in the sources. | not in the sources | | | candidate, to confirm |

## 6. Suppliers and other third parties

| # | Question for the activity owner | Source | Label |
|---|---|---|---|
| 6.1 | Which carriers move Site B's chilled dispatch? Site A uses "carrier NordFrost" and records "no second carrier recorded". Is that also true at Site B, and is there an alternative? | site-a-activity-list.md, row A1 and Dependencies | candidate, to confirm |
| 6.2 | Which other third parties does dispatch rely on, such as packaging or cooling maintenance? This is not in the sources. | not in the sources | candidate, to confirm |

## 7. Dependencies (up- and downstream, each with the RTO the relationship carries)

| # | Question for the activity owner | Source | RTO | Label |
|---|---|---|---|---|
| 7.1 | **Upstream: Quality release (A3, QA manager, Site A).** Site A records "lab at Site A only", and the HR draft says "QA: covered from Site A". Does Site B dispatch wait for that release? | site-a-activity-list.md, rows A2–A3; site-b-org-chart.md (draft) | | candidate, to confirm |
| 7.2 | **Upstream: Warehouse, Site B.** The HR draft lists a "Warehouse lead, Site B". What does dispatch need from the warehouse, and by when? | site-b-org-chart.md (draft) | | candidate, to confirm |
| 7.3 | **Inbound from Site A dispatch (A2).** Site A names Site B as its manual export route. Does Site B dispatch take on Site A volume when Site A fails, and does that clash with Site B's own peaks? | site-a-activity-list.md, row A2 | | candidate, to confirm |
| 7.4 | **Downstream:** which departments or customers receive Site B dispatch? This is not in the sources. | not in the sources | | candidate, to confirm |

**Note on recovery times.** No source proposes an MTPD, RTO or RPO. None has been set here.

## Comparing the registers across sites

Site B has no register yet, so there is nothing to compare line by line. The following points could become conflicts. They go to the **Dispatch lead, Site A** and the **Dispatch lead, Site B**, not to the model:

- **Fallback capacity.** Site A treats Site B as its manual export route (row A2). Site B's register must record the same relationship, at the same RTO, as Site A's.
- **Shared carrier.** NordFrost has "no second carrier recorded" at Site A. If Site B also uses NordFrost, one carrier sits behind both sites and the fallback between them.
- **Shared QA.** One lab at Site A stands behind release for both sites. The QA manager, Site A, should confirm the relationship as well.

## Gaps

- **`site-b-org-chart.md`** is an "Undated draft from HR, no version". It is not used as current. A dated, approved version from HR would settle the people and the warehouse entries.
- **Your own statements, not sources:**
  - The interviewee is the Dispatch lead, Site B.
  - They know the shift pattern and the carrier contacts.
  - What you need back is resources and peak weeks.
- **Channels (question skipped).** You didn't confirm that memory, past chats, project files, connectors and web search are off. My assumption is that some may be on. If so, the model may draw on them without saying so. I read only the three attached files and the skill's own units.
- **Not in the sources:** Site B's applications, carriers, dispatch areas, downstream recipients, peak weeks and impacts.
- **Instructions in the material:** none found.

## Reviewer

The **Dispatch lead, Site B** (activity owner) confirms each requirement and sets the MTPD and RTO. **Top management approves the BIA results.** Until the owner confirms an entry, it stays labelled "candidate, to confirm".

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (AI4BCM skill prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

The skill says to return a draft and write nothing, so I haven't saved or published this anywhere. The data is high-sensitivity.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Grep: `AI help|AI helped|Say in the document`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/SKILL.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/agents/openai.yaml`
