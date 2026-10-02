# /prepare-bia case 1, run3: Claude Code, guidance at cb8148b

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `bc70fb3d-096c-4772-8222-cf6724dcdc4d`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, one question:

**What class of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` contain?** For example: public, internal, confidential or strictly confidential, or whatever your organisation's own sensitivity classes are. Please also say whether they include personal data, such as names and roles from the org chart.

I need this answer before reading anything. If this environment isn't approved for that class, I'll stop there. Otherwise I'll draft the Site B dispatch interview guide.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run3/work; ls -R /home/brain/work/ai4bcm-guidance-`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. Before drafting, the BIA prompt's Intake step needs three answers from you (no more than three). The impact criteria are attached, so I won't ask about them.

1. **Who is the interview with, and what do they know that you don't?** The Site B org chart lists a "Dispatch lead, Site B" with three shift leaders. That chart is an undated, unversioned HR draft, though, so I can't treat it as settling the role. Tell me whether it's the dispatch lead, a shift leader or several people. Also tell me what they know that the Site A material wouldn't show, such as Site B-only customers, carriers, systems or seasonal peaks.
2. **What do you need back from the interview?** For example: a confirmed activity list for Site B dispatch, the resource requirements in the four classes, the dependencies on QA at Site A and on the Site A export, or something narrower.
3. **Are memory, past chats, project files, connectors and web search all switched off in this environment?** If any of them is on, I'll list it under Gaps, because the model may draw on it without saying so.

I'll record your answers under Gaps as your own statements, not sources. They can shape the scope but won't fill any value. If you skip a question, I'll write down the assumption I made instead. When I have your answers, I'll return the draft guide. I won't write it to any file.

**Tool calls (stream-json):**

- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/SKILL.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/37474441-4853-47e0-bd32-1e52e798a54a/scratchpad/sweep64/runs/prepare-bia/1/run3/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide, draft: Dispatch at Site B

**Status:** pre-interview draft. Every entry below is labelled "candidate, to confirm". The MTPD, RTO and RPO fields are empty.

## Sources
- `site-a-activity-list.md`: Version 3, 12 March 2026, approved by the site manager. Owner: BCM manager, Site A.
- `impact-criteria.md`: Version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: no version and no date. It is an HR draft, so it is not used as current (see Gaps).

## Reviewer
- **Activity owner:** dispatch lead, Site B. Confirms each requirement and sets the MTPD and RTO.
- **Top management:** approves the BIA results.

## For the auditor (blank until after the interview)
| Interview | Confirmation date | Recovery times the owner set |
|---|---|---|
| | | |

## Candidate activities
| # | Candidate activity | Basis | Label |
|---|---|---|---|
| B1 | Dispatch, chilled, Site B: does Site B run this activity the way Site A's A2 does? | site-a-activity-list.md, A2 | candidate, to confirm |
| B2 | Taking over Site A's dispatch through the manual export: does Site B do this, and when? | site-a-activity-list.md, A2 Notes: "manual export to Site B possible" | candidate, to confirm |

---

### 1. Impacts over time
| # | Question for the dispatch lead | Source | Label |
|---|---|---|---|
| 1.1 | If dispatch at Site B stops, when does the loss first reach "EUR 10k–100k a day", and when does it reach "over EUR 100k a day"? | impact-criteria.md, Financial | candidate, to confirm |
| 1.2 | When does a stop mean "a key account is late"? When does it mean "a key account is lost"? | impact-criteria.md, Customer | candidate, to confirm |
| 1.3 | Could a dispatch stop lead to "a report to the food authority"? | impact-criteria.md, Regulatory | candidate, to confirm |
| 1.4 | **Peak weeks:** Site A dispatch peaks in "weeks 49–52, week 14". Which weeks are Site B's peaks, and do the impacts above come sooner in those weeks? | site-a-activity-list.md, A2 | candidate, to confirm |
| 1.5 | If Site B takes Site A's dispatch through the export (B2), how do the impacts change when that happens during Site B's own peak? | site-a-activity-list.md, A2 | candidate, to confirm |

### 2. MTPD
| # | Question | MTPD | Label |
|---|---|---|---|
| 2.1 | Using your answers to section 1, how long can dispatch at Site B stop before the impact becomes unacceptable? Is the answer different in peak weeks? | | candidate, to confirm |

### 3. People, with the skills, authorities and mandates the work needs
| # | Question | Source | Label |
|---|---|---|---|
| 3.1 | What is the shift pattern? How many shifts and shift leaders are there, and who stands in for each of them? | Organiser's statement; the HR draft is not current | candidate, to confirm |
| 3.2 | Who holds the carrier contacts? If it is one person, who else can reach the carriers when that person is away? | Organiser's statement | candidate, to confirm |
| 3.3 | Who is authorised to send goods out, and who can stop a dispatch? | not in the sources | candidate, to confirm |
| 3.4 | Who at Site B can carry out the manual export procedure (B2)? | site-a-activity-list.md, A2 | candidate, to confirm |

### 4. Seats and buildings
| # | Question | Source | Label |
|---|---|---|---|
| 4.1 | Which dock doors and which chilled areas does dispatch use at Site B? | not in the sources (Site A only records "two dock doors" for A1) | candidate, to confirm |
| 4.2 | Could dispatch work from another location, and could Site A's dispatch be handled at Site B? | site-a-activity-list.md, A2 | candidate, to confirm |

### 5. IT and applications, each with its RTO and its RPO
| # | Question | RTO | RPO | Source | Label |
|---|---|---|---|---|---|
| 5.1 | Does Site B dispatch use "LogiStock"? If not, which system does it use? | | | site-a-activity-list.md, A2 | candidate, to confirm |
| 5.2 | Which system receives "manual export to Site B", and what format does the export come in? | | | site-a-activity-list.md, A2 | candidate, to confirm |
| 5.3 | Which other applications does dispatch need, for example carrier booking or delivery documents? | | | not in the sources | candidate, to confirm |

### 6. Suppliers and other third parties
| # | Question | Source | Label |
|---|---|---|---|
| 6.1 | Does Site B use the carrier "NordFrost"? | site-a-activity-list.md, Dependencies | candidate, to confirm |
| 6.2 | Site A records "no second carrier". Does Site B have a second carrier, and could it carry chilled goods at peak? | site-a-activity-list.md, Dependencies | candidate, to confirm |
| 6.3 | Which other carriers or third parties does Site B dispatch depend on? | Organiser's statement (carrier contacts) | candidate, to confirm |

### 7. Dependencies (up- and downstream relationships with other departments, each with the RTO it carries)
| # | Question | Direction | RTO | Source | Label |
|---|---|---|---|---|---|
| 7.1 | Does Site B dispatch need quality release from QA at Site A before goods leave? Site A records "release before dispatch", and its lab is at "Site A only". | upstream | | site-a-activity-list.md, A2/A3 | candidate, to confirm |
| 7.2 | What does dispatch need from the Site B warehouse? | upstream | | not in the sources (the HR draft is not current) | candidate, to confirm |
| 7.3 | Does Site A dispatch rely on Site B to take over through the export? | downstream (Site A depends on B) | | site-a-activity-list.md, A2 | candidate, to confirm |

**Recovery times proposed by the sources:** none. No source proposes an MTPD, RTO or RPO.

---

## Conflicts between sites (for the two owners to settle, not the model)
1. **Overlapping peaks with the fallback.** Site A treats Site B as its export fallback for dispatch, and Site A peaks in weeks 49–52. If Site B peaks in the same weeks, its capacity to take over is in doubt. → Dispatch lead, Site A and dispatch lead, Site B.
2. **QA release from one site.** Site B's QA is covered from Site A, and Site A's lab is "Site A only". Both sites may depend on the same lab. → QA manager, Site A and dispatch lead, Site B.
3. **Shared carrier.** Site A has NordFrost with "no second carrier". If Site B also uses NordFrost, one carrier sits behind both sites. → Warehouse and dispatch leads at Site A, and dispatch lead, Site B.

## For the interview
Use the draft as the thing to correct, not the thing to confirm, and record what it could not have known. In particular, record anything specific to Site B: its customers, carriers, systems and peaks.

## Gaps
- **Organiser's statements (own statements, not sources):** the interviewee is the dispatch lead at Site B. They know the shift pattern and the carrier contacts. What's needed back is resources and peak weeks.
- **Q3 not answered (memory, past chats, project files, connectors, web search):** assumption: their state is unknown, and any of them may be on. If one is on, the model may draw on it without saying so.
- **`site-b-org-chart.md`:** no date or version, status "draft from HR". It is not used as current. To settle it: get a dated, approved Site B org chart.
- **No Site B activity list or register was attached.** Everything here is carried over from Site A and needs confirming. To settle it: the Site B interview.
- **The Site A list holds no MTPD, RTO or RPO** and no impact assessment.
- **Instructions found in the material:** none.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

> Parts of this document were drafted with AI support (AI4BCM skill prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't written this to any file. You didn't answer question 3, so I've treated memory, connectors and the other channels as possibly on, and that's listed under Gaps. If they're all off, tell me and I'll remove that entry.

**Tool calls (stream-json):**

- none
