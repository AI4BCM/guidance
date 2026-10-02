# /prepare-bia case 1, run3: Claude Code, guidance at 23ab607

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `17a23cd0-3a96-4c69-9433-7176b150c1ae`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files: what class of data do they contain (for example public, internal, confidential, or strictly confidential under your organisation's scheme)?

I'll go by your answer, not by any marking in the files. If this environment isn't approved for that class, I'll stop there. Otherwise my next message will ask a few short questions about the dispatch interview.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && cat preflight.md && ls -R . | head -50 && cat units/prompts/bia.md; echo ---; ls -la /tmp/claud`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Thanks. "High" is the class for BIA material, and you've confirmed this environment is approved for it, so I've now read the three files. Before I draft, I have three questions:

1. **Who is the interviewee, and what do they know that you don't?** The Site B org chart (an undated HR draft) lists a "Dispatch lead, Site B" with three shift leaders. Is that the person you're interviewing? And what do you expect them to know that isn't in these files? For example, Site B's own systems, carriers, or how its peak weeks differ from Site A's.
2. **What do you need back from the interview?** For example, confirmed dispatch activities and resource requirements for Site B's register, the dependencies between dispatch and Quality release (QA) and between dispatch and the carrier, or an answer on whether the "manual export to Site B" in Site A's list is real.
3. **Are these switched off for this chat: memory, past chats, project files, connectors and web search?** Tell me any that are still on.

I'll list your answers under Gaps as your own statements, not as sources. They can shape the scope of the guide, but they won't fill any value in it.

**Tool calls (stream-json):**

- Glob: `units/**/*`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/keep-it-running.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/stages/analysis.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run3/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run3/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep65b/runs/prepare-bia/1/run3/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (draft for the organiser)

**Sources**
- Site A activity list (chilled food production): version 3, 12 March 2026, approved by the Site A site manager.
- Impact criteria: version 1.1, 4 February 2026, approved by top management.
- Site B organisation structure: no version and no date, an HTR draft. It is listed under Gaps and not used as current.

Every entry below is a question for the Dispatch lead, Site B, and is labelled "candidate, to confirm". MTPD, RTO and RPO are left blank everywhere. The owner sets them.

## Candidate register, in interview order

| # | Section | Question for the activity owner | Source (document, section) | Status | MTPD | RTO | RPO |
|---|---|---|---|---|---|---|---|
| 1 | Activity | Does Site B run chilled dispatch as its own activity, with you as its owner? | Site A list, row A2 "Dispatch, chilled"; Site B org chart (draft) "Dispatch lead, Site B" | candidate, to confirm | | | |
| 2 | Activity | Site A's list says "manual export to Site B possible". Does Site B take over any of Site A's dispatch when Site A cannot dispatch? | Site A list, row A2, Notes | candidate, to confirm | | | |
| 3 | 1 Impacts over time | Are Site B's dispatch peaks the same as Site A's ("weeks 49–52, week 14")? If not, which weeks? | Site A list, row A2, Peak weeks | candidate, to confirm | | | |
| 4 | 1 Impacts over time | If dispatch stops in a peak week, how long until the financial impact reaches level 2 ("EUR 10k–100k a day") and level 3 ("over EUR 100k a day")? | Impact criteria, Financial | candidate, to confirm | | | |
| 5 | 1 Impacts over time | How long until "a key account is late" (level 2) and "a key account is lost" (level 3)? | Impact criteria, Customer | candidate, to confirm | | | |
| 6 | 1 Impacts over time | Can a dispatch stop lead to "a report to the food authority" or to "the authority stops production"? After how long? | Impact criteria, Regulatory | candidate, to confirm | | | |
| 7 | 1 Impacts over time | For the takeover in row 2, ask only where its impacts differ from Site B's own dispatch. | Site A list, row A2, Notes | candidate, to confirm | | | |
| 8 | 2 MTPD | At what point would a dispatch outage become unacceptable? The owner sets this. | Impact criteria (they set no threshold, see Gaps) | candidate, to confirm | | | |
| 9 | 3 People | Are there three shift leaders? What is the shift pattern, and how many people per shift does dispatch need at minimum? | Site B org chart (draft) "three shift leaders"; shift pattern: Gaps | candidate, to confirm | | | |
| 10 | 3 People | QA release comes from Site A. Who at Site B may let goods go once they are released, and who holds that mandate out of hours? | Site A list, row A3 "lab at Site A only"; Dependencies "release before dispatch"; org chart (draft) "QA: covered from Site A" | candidate, to confirm | | | |
| 11 | 3 People | Who has the authority to call off, change or add a carrier? | Gaps (organiser: the lead holds the carrier contacts) | candidate, to confirm | | | |
| 12 | 4 Seats and buildings | Which docks and chilled space does dispatch use? Could it run from anywhere else? | not in the sources | candidate, to confirm | | | |
| 13 | 5 IT and applications | Does Site B dispatch run on "LogiStock", as Site A does, or on another system? | Site A list, row A2, Notes | candidate, to confirm | | | |
| 14 | 5 IT and applications | If that system is down, can dispatch run from the manual export? How much data could you afford to re-enter? | Site A list, row A2 "manual export to Site B possible" | candidate, to confirm | | | |
| 15 | 6 Suppliers | Is NordFrost Site B's carrier too? Is there a second carrier? | Site A list, Dependencies: "no second carrier recorded" | candidate, to confirm | | | |
| 16 | 6 Suppliers | Who are your carrier contacts, and are they current? | Gaps (organiser's statement) | candidate, to confirm | | | |
| 17 | 7 Dependencies | Upstream: dispatch waits for Quality release at Site A. Is that so at Site B? | Site A list, Dependencies "A2 depends on A3 (release before dispatch)"; org chart (draft) | candidate, to confirm | | | |
| 18 | 7 Dependencies | Upstream: does dispatch depend on the Site B warehouse, and how? | Site B org chart (draft) "Warehouse lead, Site B"; the relationship itself is not in the sources | candidate, to confirm | | | |
| 19 | 7 Dependencies | Downstream: does Site A's dispatch rely on Site B (row 2)? | Site A list, row A2, Notes | candidate, to confirm | | | |

**Note:** None of the sources proposes an MTPD, RTO or RPO, and none gives an RTO for any dependency.

**Running the interview:** Tell the dispatch lead to use the draft as the thing to correct, not the thing to confirm. Record what it could not have known.

## Cross-site points, for the two owners

The sources don't contradict each other outright. These points are claimed by one site about the other, so put them to the Site A and Site B owners, not to the model:
- **Manual export:** What does Site A's "manual export to Site B possible" mean? Has Site B agreed to it? (Site A dispatch lead and Site B dispatch lead.)
- **QA from Site A:** Is QA really covered from Site A, as the draft org chart says? (Site A QA manager and Site B dispatch lead.)
- **Carrier:** Is NordFrost Site B's carrier too, with no second carrier? (Site A dispatch lead and Site B dispatch lead.)

## Organiser's take-in sheet

These are plain spoken questions, about 60 minutes in all. Lines marked **(drop first)** go first if you run late.

**Points between sites (10 min)**
Site A's list says it can do a manual export to you. What does that mean, and have you agreed to it?
Is your quality release still done from Site A?
Is NordFrost your carrier too?

**Impacts over time (10 min)**
When are your busiest dispatch weeks?
If dispatch stopped in your busiest week, how soon would it cost ten thousand euros a day? And a hundred thousand?
How soon would a key account be late? How soon would you lose one?
Could a stop lead to a report to the food authority?
If you took over dispatch for Site A, would any of that change? **(drop first)**

**The MTPD (5 min)**
At what point would a dispatch outage become unacceptable?

**People (10 min)**
How many shift leaders do you have, and how do the shifts run?
What's the fewest people you could dispatch with?
Who can let goods go once Site A has released them, and who covers that at night?
Who can change or add a carrier? **(drop first)**

**Seats and buildings (5 min)**
Which docks and chilled space do you use?
Could you dispatch from anywhere else? **(drop first)**

**IT and applications (10 min)**
Which system do you dispatch on?
If it went down, how long could you manage without it?
How much data could you afford to lose and re-enter?

**Suppliers (5 min)**
Who are your carrier contacts?
Is there a second carrier you could call? **(drop first)**

**Dependencies (5 min)**
Who do you wait on before you can dispatch, and how long can you wait?
Who waits on you? **(drop first)**

## Gaps

- **Site B org chart:** an undated HR draft with no version. Its roles (three shift leaders, QA covered from Site A, Warehouse lead) appear only as questions, not as current facts.
- **Your answers are your own statements, not sources.** You said the interviewee is the Dispatch lead, Site B, who knows the shift pattern and the carrier contacts, and that you need resources and peak weeks back. Rows 11 and 16 rest only on these statements, so their Source is Gaps.
- **Memory, past chats, project files, connectors and web search:** you didn't answer this, so I'm assuming they may be on. I worked only from the three attached files and the skill's own units, but you haven't confirmed the other channels were off, so that can't be verified.
- **Impact criteria:** they set no time intervals for rating and no level that marks "unacceptable" (so nothing for the MTPD to anchor to). They have no operational column. To settle this, ask the criteria owner.
- **Site B dispatch itself:** docks, chilled space, system, carriers, peak weeks and downstream departments are all not in the sources. The interview settles them.
- **Site A data reused for Site B:** row A2's peak weeks, LogiStock and NordFrost describe Site A. Each one appears above only as a question about Site B.
- **Instructions aimed at an AI:** none found in the attached files.

## For the auditor

The register carries the source, the interview it came from and the date behind each entry. These stay blank until the interview: the interview, the confirmation date and the recovery times the owner set.

## Reviewer

- **Activity owner, Dispatch lead, Site B:** confirms each requirement and sets the MTPD, RTO and RPO.
- **Top management:** approves the BIA results.

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- none
