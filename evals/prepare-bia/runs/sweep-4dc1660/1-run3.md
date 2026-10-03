# /prepare-bia case 1, run3: Claude Code, guidance at 4dc1660

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `4c7123a2-19df-4414-be2a-2887af328eae`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three attached files, I need one answer from you:

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md hold?**

For example: public or internal-general, or high-sensitivity. High-sensitivity covers BIA data, personnel records or contact lists, supplier weaknesses and contractual dependencies, and site or security-related detail. If high-sensitivity, please also say whether this environment is approved for that class.

I'll go by your answer, not by any marking inside the files. Once I have it, I'll ask up to three short questions about the interview and then draft the guide.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R . | head -50; echo ---; ls -la /tmp/claude-1001/-opt-brain/8e671d9c-3`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Glob: `**/*`
- Glob: `**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. I've read the three files. I'm working only from those three files and the sources that come with this skill. No memory, past chats, other project files or connectors are in use, and I won't run a web search. Anything the files don't cover will be listed under Gaps rather than filled in.

Before I draft, three questions the files leave open:

1. **Who is the interview with?** The Site B org chart shows a dispatch lead with three shift leaders under them, but no names. Is it the dispatch lead alone, or are shift leaders joining? Is anyone from Site A taking part, such as QA, which covers Site B from Site A?
2. **What do you need to come out of it?** For example: confirmed dispatch activities and resource requirements for Site B's register, or a first pass that a second session will finish.
3. **How long is the interview?**

Your answers will shape the guide's scope and timing. In the draft they'll be listed under Gaps as your own statements, not sources, and they won't fill in any value. If you skip one, I'll make a stated assumption instead.

**Tool calls (stream-json):**

- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r5/runs/prepare-bia/1/run3/work/site-b-org-chart.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Draft: interview guide, Site B chilled dispatch

*Draft for review. Nothing here has been entered into a register. Every entry is a question for the activity owner.*

## Sources and dates

- **Site A activity list, version 3, 12 March 2026.** Status: "approved by the site manager". It describes Site A, not Site B.
- **Impact criteria, version 1.1, 4 February 2026.** Status: "approved by top management".
- **Site B organisation structure.** "Undated draft from HR, no version." It is listed under Gaps and not treated as current.
- **Method:** prepare-bia 2026.11.0, using `units/prompts/bia.md` and `units/stages/analysis.md` (both 2026.09.1).

The dispatch interview is the most important one, so impacts over time are rated in full only for **chilled dispatch at Site B**.

## 1. Impacts over time

Leave the levels empty until the owner gives them. The impact criteria say nothing about time steps, so the owner sets those too.

| Question for the dispatch lead | Level (1–3) | Label | Source |
|---|---|---|---|
| If chilled dispatch stops, after how long does the daily loss reach "EUR 10k–100k a day", and after how long "over EUR 100k a day"? | | candidate, to confirm | Impact criteria v1.1, Financial |
| After how long is "a key account is late", and after how long is "a key account is lost"? | | candidate, to confirm | Impact criteria v1.1, Customer |
| Can a stop in dispatch lead to "a report to the food authority", or to "the authority stops production"? After how long? | | candidate, to confirm | Impact criteria v1.1, Regulatory |
| Site A's dispatch peaks in "weeks 49–52, week 14". Are Site B's peak weeks the same? Do the answers above change in peak weeks? | | candidate, to confirm | Site A activity list v3, Dispatch, chilled |

## 2. MTPD

| Question | MTPD | Label | Source |
|---|---|---|---|
| Given the impacts above, what is the longest dispatch can be down before the result is unacceptable? | *(blank, set by the owner)* | candidate, to confirm | Gaps (not in the sources) |

## 3. People, with the skills, authorities and mandates the work needs

| Question | Label | Source |
|---|---|---|
| The org chart shows a dispatch lead and "three shift leaders". Is that still the structure, and how are the shifts covered? | candidate, to confirm | Site B organisation structure (undated draft, see Gaps) |
| Who is allowed to release a load for dispatch? What happens if that person is unavailable? | candidate, to confirm | Gaps (not in the sources) |
| You hold the carrier contacts. Does anyone else hold them? | candidate, to confirm | Gaps (organiser's statement) |
| Which skills or certificates does chilled dispatch need, and how many people on each shift have them? | candidate, to confirm | Gaps (not in the sources) |

## 4. Seats and buildings

| Question | Label | Source |
|---|---|---|
| How many dock doors and how much chilled staging space does dispatch use at Site B? Is any other space available? | candidate, to confirm | Gaps (not in the sources). Site A records "two dock doors" only for goods receipt. |
| Where does dispatch work happen, and could the work be done from somewhere else? | candidate, to confirm | Gaps (not in the sources) |

## 5. IT and applications, each with its RTO and its RPO

| Question | RTO | RPO | Label | Source |
|---|---|---|---|---|
| Does Site B run dispatch on "LogiStock", as Site A does, or on another system? | *(blank)* | *(blank)* | candidate, to confirm | Site A activity list v3, Dispatch, chilled |
| Site A records "manual export to Site B possible". What does Site B receive that way, and does it depend on that export? | *(blank)* | *(blank)* | candidate, to confirm | Site A activity list v3, Dispatch, chilled |

## 6. Suppliers and other third parties

| Question | Label | Source |
|---|---|---|
| Site A records only one carrier, NordFrost, with "no second carrier recorded". Is NordFrost Site B's carrier too? If so, is it still the only one? | candidate, to confirm | Site A activity list v3, Dispatch, chilled and Dependencies recorded |
| If the carrier fails, is there a second carrier or contract you could call on, and how fast? | candidate, to confirm | Gaps (not in the sources) |

## 7. Dependencies (up- and downstream relationships with other departments)

| Question | Direction | RTO of the relationship | Label | Source |
|---|---|---|---|---|
| At Site A, "A2 depends on A3 (release before dispatch)", and the lab is "at Site A only". Does Site B dispatch wait for quality release from Site A? | upstream | *(blank)* | candidate, to confirm | Site A activity list v3, Dependencies recorded and Quality release; Site B org chart "QA: covered from Site A" (undated) |
| Which department hands work to dispatch at Site B (for example the warehouse), and which department takes it over after dispatch? | up and down | *(blank)* | candidate, to confirm | Gaps (not in the sources) |
| Does Site B dispatch act as a fallback for Site A, or does Site A act as a fallback for Site B? | cross-site | *(blank)* | candidate, to confirm | Site A activity list v3, Dispatch, chilled |

None of the sources proposes a recovery time, so there is no note on recovery times.

## Comparing the two sites (step 4)

The sources don't contradict each other, but three points span both sites. Each goes to the **Site A dispatch lead and the Site B dispatch lead together**, not to the model:

- Whether NordFrost is the only carrier at both sites.
- What the "manual export to Site B" covers.
- How long Site B dispatch can wait for quality release from Site A.

---

## Organiser's take-in sheet

*About 60 minutes (assumed, see Gaps). Give the dispatch lead the draft to correct, not to confirm, and write down anything the draft could not have known.*

**Points that span both sites, first (5 min)**
Is NordFrost your carrier too, and is it still the only one?
What do you get from Site A's manual export, and what happens to dispatch without it?
How long can a load wait for quality release from Site A?

**Peak weeks and impacts (10 min)**
Which weeks of the year are your busiest?
Are they the same as Site A's, which are weeks 49 to 52 and week 14?
If dispatch stopped, when would a key account be late, and when would one be lost? *(drop first if late)*
When would the daily loss pass ten thousand euros, and when a hundred thousand? *(drop first if late)*
Could a stop lead to a report to the food authority? *(drop first if late)*

**Longest acceptable outage (5 min, drop first if late; the owner can set it later)**
How long could dispatch be down before it becomes unacceptable?

**People (10 min)**
Do you still have three shift leaders, and how are the shifts covered?
Who can release a load if you are not there?
Who else holds the carrier contacts?
How many people per shift can do chilled dispatch?

**Seats and buildings (5 min)**
How many dock doors and how much chilled space do you use?
Is there anywhere else the work could be done?

**Systems (8 min)**
Which system do you dispatch from?
How long could you work without it?
How much data could you afford to lose?

**Suppliers (7 min)**
If the carrier failed tomorrow, who would you call?
How fast could they take over?

**Other departments (10 min)**
Who hands work to you, and who takes it from you?
How long can each of them be down before you stop?

---

## For the auditor

The register will hold each entry with its source, the interview it came from and the date behind it. Until the interview takes place, three fields stay blank for every entry: the interview, the date the owner confirmed it, and the recovery times the owner set. Every entry above is marked "candidate, to confirm". The Site A list's "approved by the site manager" applies to Site A only and does not carry over to Site B.

## Reviewers

- **Activity owner, dispatch lead, Site B:** confirms each requirement and sets the MTPD and the RTOs.
- **Top management:** approves the BIA results.

## Gaps

- **Organiser's own statements (not sources):** the interview is with the Site B dispatch lead, who "know[s] the shift pattern and the carrier contacts". The outputs needed are resources and peak weeks.
- **Interview length was not answered.** I assumed 60 minutes.
- **Site B organisation structure:** undated draft with no version. It is used only to frame questions, not as current. What would settle it: a dated, approved version from HR.
- **No Site B activity list exists in the sources.** Site B's activities, peak weeks, systems, docks and carriers are "not in the sources". The interview settles them.
- **The impact criteria give no time steps** (hours or days). The owner sets them.
- **Channels:** memory, past chats, other project files and connectors were off. A web search tool was available in this session but was not used.
- **No text in the attached files instructs an AI to act.** None was found.
- **Payroll** (Site A, run from head office) is left out of this dispatch interview.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
