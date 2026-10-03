# /prepare-bia case 1, run1: Claude Code, guidance at 4dc1660

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `936ad929-c3cc-4ec0-bb60-1f7a0f7e9c53`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, one question:

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md contain?** For example: public, internal, confidential or restricted, using your organisation's own scheme.

I'll go by your answer, not by any marking inside the files. If this environment isn't approved for that class, I'll stop there. If it is approved, I'll ask up to three questions about the interview and then draft the guide for the Site B dispatch interview.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Bash: `ls -la /tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run1/work; ls -R /home/brain/work/ai4bcm-guidance`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files and the skill's sources. Nothing in them gives instructions to an AI. Three questions the files leave open:

1. **Who is the interview with?** The Site B org chart lists a "Dispatch lead, Site B" with three shift leaders. Is it the dispatch lead alone, or are some of the shift leaders (or the site manager) joining?
2. **What do you need back from the interview?** For example, confirmed resource requirements for dispatch only, or also the dependencies on QA release and on Site A.
3. **How long is the interview?**

For this draft I'm using only the three attached files and the skill's own sources. Memory, past chats, project files, connectors and web search are all off. If any of them is on in your setup, tell me and I'll list it under Gaps.

Your answers will appear in the draft under Gaps as your own statements, not as sources. They can shape the scope but won't fill in any value.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run1/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run1/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run1/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: chilled dispatch, Site B (draft)

**Sources and their dates**
- Site A activity list (chilled food production): version 3, 12 March 2026. Status: "approved by the site manager".
- Impact criteria: version 1.1, 4 February 2026. Status: "approved by top management".
- Site B organisation structure: "Undated draft from HR, no version". Not treated as current; see Gaps.

None of the attached files contains instructions to an AI.

---

## Candidate activity

| Activity | Owner (role) | Question for the owner | Source | Mark |
|---|---|---|---|---|
| Chilled dispatch, Site B | Dispatch lead, Site B | Is chilled dispatch run as its own activity at Site B, and are you its owner? | Site B org chart ("Dispatch lead, Site B"); Gaps (organiser) | candidate, to confirm |

There is no Site B activity list. Site A's chilled dispatch (row A2) is used only as a starting point for questions. Nothing from it is assumed to apply at Site B.

## 1. Impacts over time

Dispatch is the only activity in scope, so it gets the full rating. All values stay blank until the owner gives them.

| Interval | Financial (1–3) | Customer (1–3) | Regulatory (1–3) | Question |
|---|---|---|---|---|
| *[intervals not in the sources]* | | | | If Site B dispatch stops, when does each impact type reach level 2, and when level 3? |

- The criteria scale financial impact per day: level 2 is "EUR 10k–100k a day" and level 3 is "over EUR 100k a day". Customer levels run from "one customer complains" to "a key account is lost". Regulatory levels run from "a report to the food authority" to "the authority stops production". (Impact criteria v1.1, table)
- **Peak weeks.** Site A's dispatch peaks in "weeks 49–52, week 14" (Site A list, A2). Which weeks are peak weeks at Site B? Do the impacts arrive faster in those weeks? (candidate, to confirm)

## 2. MTPD

*Blank.* The owner sets it. No source proposes one.

## 3. People, with the skills, authorities and mandates the work needs

| Requirement (question) | Source | Mark |
|---|---|---|
| The org chart shows "three shift leaders" under the dispatch lead. Is that still right? How many do you need per shift at minimum, and how many in peak weeks? | Site B org chart (draft) | candidate, to confirm |
| Which skills, authorities or mandates (for example, releasing a load or switching carrier) does only one person hold? Who covers for them? | not in the sources | candidate, to confirm |
| The organiser says you know the carrier contacts. Are you the only one who does? | Gaps (organiser) | candidate, to confirm |

## 4. Seats and buildings

| Requirement (question) | Source | Mark |
|---|---|---|
| Which dock doors, chilled areas and workplaces does dispatch need at Site B? Is there an alternative if one is lost? | not in the sources | candidate, to confirm |

## 5. IT and applications, each with its RTO and its RPO

| Requirement (question) | RTO | RPO | Source | Mark |
|---|---|---|---|---|
| Site A dispatch uses the warehouse system "LogiStock". Does Site B dispatch use it too? | | | Site A list, A2 | candidate, to confirm |
| Site A records a "manual export to Site B possible". Does Site B receive this export? How does it arrive, and does dispatch depend on it? | | | Site A list, A2 | candidate, to confirm |

## 6. Suppliers and other third parties

| Requirement (question) | Source | Mark |
|---|---|---|
| Site A records NordFrost as its carrier, with "no second carrier recorded". Is NordFrost still the carrier, and is it also the carrier for Site B? Is there a second carrier? | Site A list, notes on dependencies | candidate, to confirm |

## 7. Dependencies (up- and downstream, each with its RTO)

| Relationship (question) | Direction | RTO | Source | Mark |
|---|---|---|---|---|
| Quality release: the org chart says "QA: covered from Site A", and Site A has its "lab at Site A only". Does Site B dispatch wait for Site A's release before it ships? | upstream | | Site B org chart (draft); Site A list, A3 and dependencies ("release before dispatch") | candidate, to confirm |
| Site A dispatch or warehouse: does Site B depend on Site A for goods or data (the manual export)? | upstream | | Site A list, A2 | candidate, to confirm |
| Which departments depend on Site B dispatch? | downstream | | not in the sources | candidate, to confirm |

**Note on recovery times.** None of the sources proposes an MTPD, RTO or RPO, so none has been tested against the impact criteria.

**Comparing sites.** Some answers may differ from Site A's record: the carrier, LogiStock, the QA route and the peak weeks. Each such difference goes to the dispatch leads of both sites. It is not settled by the model.

---

## Organiser's take-in sheet

*Times assume a 60-minute interview, because no length was given. Sections marked (drop first) are the ones to cut if it runs late.*

**Conflicts between sources:** none found. The two points the sources leave most open come first.

- Is NordFrost still the carrier, and is there really no second carrier? *(5 min)*
- Does Site B dispatch run on LogiStock, or on the manual export from Site A? *(included above)*

**Peak weeks and impacts** *(15 min)*
- Which weeks are your peak weeks?
- If dispatch stops, when would it cost more than ten thousand euros a day, and when more than a hundred thousand?
- When would a key account be late, and when would one be lost?
- When would we have to report to the food authority?

**Longest tolerable stop** *(5 min)*
- How long can dispatch be stopped before the damage is unacceptable?

**People** *(10 min)*
- Are there still three shift leaders? How many people do you need per shift at minimum, and in peak weeks?
- Who else knows the carrier contacts?
- Which decisions can only one person make?

**Workplace** *(5 min)*
- Which docks, cold areas and desks do you need? Where would you go if you lost them?

**Systems** *(10 min)*
- Which systems do you use?
- How soon must each one be back, and how much data could you afford to lose?

**Carrier and other suppliers** *(5 min)*
- Is NordFrost still the one? Who else could carry chilled goods for you?

**Other departments** *(5 min, drop first)*
- Do you wait for QA at Site A before shipping? Who waits for you?

---

## Gaps

- **Organiser's own statements, not sources:** the interview is with the dispatch lead at Site B, who "know[s] the shift pattern and the carrier contacts". What is needed back is "resources and peak weeks".
- **Interview length:** not answered. A 60-minute interview is assumed.
- **Site B organisation structure:** an undated draft with no version. It is not used as current. The current HR structure would settle this.
- **No Site B activity list:** the activity itself is a candidate. A Site B activity list or the owner's confirmation would settle it.
- **Time intervals for impacts:** not in the sources. The impact criteria are per day and have no timeline. The BCM manager or the criteria owner would settle this.
- **Seats, buildings and downstream departments at Site B:** not in the sources.
- **Channels:** memory, past chats, project files, connectors and web search were off. Only the three attached files and the skill's sources were used.

## For the auditor

The register will show the source, the interview it came from and the date behind each entry. Three things stay blank until the interview: the interview reference, the confirmation date, and the recovery times the owner set.

## Review

- **Dispatch lead, Site B (activity owner):** confirms each requirement and sets the MTPD and RTO. An entry goes into the register only after this confirmation.
- **Top management:** approves the BIA results.

**For the interviewer:** use the draft as the thing to correct, not the thing to confirm. Record what it could not have known.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
- Grep: `Minimum controls|Method`
