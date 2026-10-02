# /prepare-bia case 1, run3: Claude Code, guidance at 88370c8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a7c5b7e5-4696-40f4-b4f8-0ecf0dd71572`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, I need one answer from you.

**What kind of data do `site-a-activity-list.md`, `impact-criteria.md` and `site-b-org-chart.md` contain?**

The AI4BCM data rules count the following as high-sensitivity. These may only be processed in an approved corporate or private environment:

- BIA data and risk assessment detail, such as Site A's activity list or the impact criteria
- personal data, contact lists and personnel records, such as names in the Site B org chart
- supplier weaknesses and contractual dependencies
- security-related site detail
- recovery strategies and design assumptions

If the files contain any of these, please also confirm that this Claude Code environment is approved for high-sensitivity data. If it isn't, I'll stop here and won't read the files. If the data is less sensitive, or the names are already pseudonymised, tell me and I'll go ahead.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia; cat preflight.md; echo ======; cat units/prompts/bia.md; echo =====; ls -R units | head -50; echo`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `*`
- Grep: `Sensitivity classes`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read the three files. Before drafting, the BIA prompt's Intake has me ask you up to three questions about what the files leave open. Your answers will be recorded under Gaps as your own statements, not as sources. They can shape the scope of the guide but will never fill in a value.

1. **Who is being interviewed, and what do they know that you don't?** The only file that mentions Site B is the org chart, an undated HR draft with no version. It lists a "Dispatch lead, Site B (three shift leaders)". Is that the person you'll interview? Also, what do they know about dispatch at Site B that you don't, for example:
   - the warehouse system
   - the carriers
   - whether Site B receives the "manual export to Site B" mentioned for Site A's activity A2?
2. **What do you need back from the interview?** For example: a candidate activity list for Site B, resource requirements and dependencies to put to the owner, or input for comparing Site B with Site A.
3. **Are these switched off: memory, past chats, project files, connectors and web search?** In this environment that means CLAUDE.md or auto-memory, any connected MCP servers, and web search. Whatever stays on goes under Gaps, because the model could draw on it without saying so.

You've already attached the impact criteria (version 1.1, approved by top management), so I won't ask for them. If you skip a question, I'll record an assumption under Gaps instead.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep64c/runs/prepare-bia/1/run3/work/site-b-org-chart.md`
- Grep: `Say in the document that AI helped`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (pre-interview draft)

**Sources and dates**
- `site-a-activity-list.md`: version 3, 12 March 2026, approved by the site manager. Owner: BCM manager, Site A.
- `impact-criteria.md`: version 1.1, 4 February 2026, approved by top management.
- `site-b-org-chart.md`: undated HR draft with no version. It is not used as current (see Gaps G1).
- Prompt: `units/prompts/bia.md`, version 2026.09.1. Task: "draft candidate activities, their resource requirements and interview questions for the site in the attached material".

**Interviewee and owner:** the Dispatch lead, Site B. This comes from your statement (G2), because the org chart is undated.
**Reviewer:** the activity owner, Dispatch lead, Site B, confirms each requirement and sets MTPD and RTO. "Top management approves the BIA results."

Every entry below is labelled **"candidate, to confirm"**. In each table these fields stay blank until the interview: Interview, Confirmed on, and the recovery times the owner sets (MTPD / RTO / RPO).

**Guidance for the interviewer:** use the draft as the thing to correct, not the thing to confirm, and record what it could not have known. The sources contain almost nothing about Site B. Most rows ask whether Site B works the way Site A records it.

---

### 1. Impacts over time

The impact criteria give three levels (financial per day, customer, regulatory), but no time bands. So for each impact type, ask how long an outage takes to reach each level.

| # | Question for the activity owner | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|
| 1.1 | Is "Dispatch" a separate activity at Site B? Is it chilled, like Site A's "A2 Dispatch, chilled"? | Site A list, A2 | | | candidate, to confirm |
| 1.2 | Which weeks are Site B's peak weeks for dispatch? Site A records "weeks 49–52, week 14" for A2. Are Site B's the same or different? | Site A list, A2; G3 | | | candidate, to confirm |
| 1.3 | If dispatch at Site B stops, after how long (hours or days, in and out of peak weeks) does the financial loss pass "EUR 10k–100k a day" (level 2) and "over EUR 100k a day" (level 3)? | Impact criteria, table | | | candidate, to confirm |
| 1.4 | After how long is "a key account is late" (level 2), and when is "a key account is lost" (level 3)? Which key accounts does Site B dispatch to? | Impact criteria, table | | | candidate, to confirm |
| 1.5 | Can a dispatch outage at Site B lead to "a report to the food authority" (level 2) or "the authority stops production" (level 3)? After how long? | Impact criteria, table | | | candidate, to confirm |

### 2. MTPD

| # | Question for the activity owner | Source | Interview | Confirmed on | MTPD | Mark |
|---|---|---|---|---|---|---|
| 2.1 | Using your answers in section 1, what is the longest period dispatch at Site B can be disrupted before the impact becomes unacceptable? Is it different in peak weeks? | Impact criteria, table | | | | candidate, to confirm |

### 3. People, with the skills, authorities and mandates the work needs

| # | Question for the activity owner | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|
| 3.1 | What is the shift pattern? How many people per shift are needed at minimum, in normal weeks and in peak weeks? | G2 | | | candidate, to confirm |
| 3.2 | The undated HR draft shows "three shift leaders" under you. Is that current? Can each of them run dispatch without you? | Org chart (undated, G1) | | | candidate, to confirm |
| 3.3 | Who holds the carrier contacts besides you? If only you hold them, who can deputise and where are the contacts kept? | G2 | | | candidate, to confirm |
| 3.4 | Who has the authority to release goods for dispatch at Site B? Site A records "A2 depends on A3 (release before dispatch)", and the HR draft says QA is "covered from Site A". | Site A list, dependencies; org chart (G1) | | | candidate, to confirm |
| 3.5 | Which skills or system rights does someone need to stand in (warehouse system, carrier booking, manual export)? | Site A list, A2 | | | candidate, to confirm |

### 4. Seats and buildings

| # | Question for the activity owner | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|
| 4.1 | Which buildings, areas and workplaces does dispatch at Site B need, and how many? | not in the sources | | | candidate, to confirm |
| 4.2 | Could dispatch run from another location, for example Site A, and for how long? | not in the sources | | | candidate, to confirm |

### 5. IT and applications, each with its RTO and its RPO

| # | Question for the activity owner | Source | Interview | Confirmed on | RTO | RPO | Mark |
|---|---|---|---|---|---|---|---|
| 5.1 | Does Site B use "LogiStock" for dispatch, as Site A's A2 does, or another system? | Site A list, A2 | | | | | candidate, to confirm |
| 5.2 | Site A's list says "manual export to Site B possible". What does Site B receive through it, how often, and who handles it at Site B? | Site A list, A2 | | | | | candidate, to confirm |
| 5.3 | How long can dispatch at Site B run without the system, on paper or by manual export? How much data can be lost? | not in the sources | | | | | candidate, to confirm |

### 6. Suppliers and other third parties

| # | Question for the activity owner | Source | Interview | Confirmed on | Mark |
|---|---|---|---|---|---|
| 6.1 | Which carriers serve dispatch at Site B? Is NordFrost one of them? | Site A list, A1/A2; G2 | | | candidate, to confirm |
| 6.2 | Site A records "no second carrier recorded". Does Site B have a second carrier? If so, at what notice can it step in, including in peak weeks? | Site A list, dependencies | | | candidate, to confirm |
| 6.3 | Which other third parties does dispatch at Site B need? | not in the sources | | | candidate, to confirm |

### 7. Dependencies (up- and downstream, each with the RTO the relationship carries)

| # | Question for the activity owner | Direction | Source | Interview | Confirmed on | RTO | Mark |
|---|---|---|---|---|---|---|---|
| 7.1 | Does dispatch at Site B depend on quality release by Site A QA ("lab at Site A only")? How quickly must release resume for Site B to keep dispatching? | upstream | Site A list, A3 and dependencies; org chart (G1) | | | | candidate, to confirm |
| 7.2 | What is the relationship behind "manual export to Site B possible": does Site B take over Site A dispatch, or receive data from it? | up/downstream, to confirm | Site A list, A2 | | | | candidate, to confirm |
| 7.3 | Which Site B departments come before dispatch (for example the Warehouse lead, Site B, in the HR draft) and which come after it? | up/downstream | Org chart (G1); otherwise not in the sources | | | | candidate, to confirm |

**Recovery times proposed by a source:** none. No attached source proposes an MTPD, RTO or RPO.

---

### Comparison across sites (to the two owners, not to the model)

I can't name any conflicts yet: Site B has no register, only an undated org chart. After the interview, put these points to the Dispatch lead, Site A, and the Dispatch lead, Site B (with the BCM manager, Site A, who owns the Site A list):
- **Peak weeks:** Site A's A2 lists weeks 49–52 and week 14. Do Site B's peak weeks match?
- **Manual export:** Site A says the export to Site B is "possible". Does Site B confirm it can receive it, and at what capacity?
- **Carrier:** Site A records only NordFrost. If Site B uses the same carrier, both sites depend on one carrier.
- **QA:** Site A's lab is the only lab, and the HR draft says Site B's QA is covered from Site A. Do both owners agree how release works when Site A is down?

---

### Gaps

- **G1:** `site-b-org-chart.md` is an "undated draft from HR, no version". It is not used as current. Every entry citing it is a question. What would settle it: a dated, approved Site B organisation chart.
- **G2:** Your own statement, not a source: "The dispatch lead at Site B; they know the shift pattern and the carrier contacts."
- **G3:** Your own statement, not a source: what you need back from the interview is "Resources and peak weeks". This shaped the scope (sections 1, 3–6) but fills no value.
- **G4:** You didn't answer question 3 (memory, past chats, project files, connectors, web search). Assumption: they may be on, and the model may draw on them without saying so. In this session I called no web search or connector tool, and I read only the three attached files and the skill's own units.
- **G5:** There is no activity list, peak-week record, IT list or supplier list for Site B. Everything about Site B is not in the sources. What would settle it: the interview, and any Site B register.
- **G6:** The impact criteria have no time bands, so impacts over time must come from the owner.
- **G7:** The meaning and direction of "manual export to Site B possible" (Site A list, A2) is not settled.
- **Instructions found in the material:** none.

---

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
