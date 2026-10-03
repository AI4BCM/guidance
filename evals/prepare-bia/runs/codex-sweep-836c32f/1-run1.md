# $prepare-bia case 1, run1: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff0e-d6f3-7db2-b896-946620a0b836`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the three attached files. I’ll first read its preflight and the source material.


What data sensitivity class do the three attachments hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I’ve read the skill instructions, but haven’t opened the attachments; their contents must wait until you answer.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"' -g '"'!vendor'"' -g '"'!'"\\.git' ."`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll read the attachments and keep the draft in this chat. Memory, past chats, other project files, connectors and web search are off; I’ll use only the three attachments and the sources shipped with prepare-bia.


Who is the interviewee, and what can they explain about Site B dispatch that you do not already know?

What do you need back from the interview—for example, a corrected activity scope, owner-confirmed resource requirements, or both?

How long is the interview?

The Site A list and impact criteria are approved and dated. Site B’s organisation chart is an undated, unversioned HR draft, so its roles and QA arrangement need checking. The sources also give no activity priority ranking; I won’t treat the list order as a ranking.


Before drafting, I need your answers to the three intake questions:

- Who is the interviewee, and what can they explain that you do not already know?
- What do you need back from the interview?
- How long is it?

The prepare-bia [intake instructions](.agents/skills/prepare-bia/units/prompts/bia.md) explicitly say “Wait for my answers.” That is why I’m pausing before producing the guide.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/prompts/bia.md .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/keep-it-`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/workflow-design.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus on dispatch resources and peak weeks for the Site B dispatch lead. You left the interview length open, so I’ll use a provisional 45-minute agenda. Site A’s peak weeks, LogiStock and NordFrost will be prompts for the owner to correct, not facts about Site B.


**Site B dispatch interview guide — draft, candidate, to confirm**

Sources and dates:

- **site-a-activity-list.md**, version 3, 12 March 2026; approved by the Site A site manager. Evidence about Site A, used here to form questions for Site B.
- **impact-criteria.md**, version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md**, no version or date; HR draft. Listed under Gaps and used only to identify questions, not as evidence of current arrangements.

The interview is intended to establish dispatch resources and peak weeks. Every new Site B entry below is **candidate, to confirm**. Site A’s source retains its approved status; that approval does not confirm any Site B requirement.

Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.

**1. Impacts over time**

Start by checking the activity boundary: does Site B perform chilled dispatch as described for Site A, and where does its responsibility begin and end?  
Source: site-a-activity-list.md, activity A2.

Does Site B share Site A’s dispatch peaks in weeks 49–52 and week 14? Which weeks differ, and how do resource needs and interruption impacts change during those weeks?  
Source: site-a-activity-list.md, activity A2. Site B peak weeks are not in the sources.

For dispatch, ask the owner to describe impacts at each agreed time horizon, separately for normal and peak periods. The sources supply no time horizons or activity priority ranking. Dispatch receives the detailed discussion because it is the requested interview scope.

Use the approved criteria without assigning ratings in advance:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | “under EUR 10k a day” | “one customer complains” | “none” |
| 2 | “EUR 10k–100k a day” | “a key account is late” | “a report to the food authority” |
| 3 | “over EUR 100k a day” | “a key account is lost” | “the authority stops production” |

Source: impact-criteria.md, impact-level table.

Ask when each consequence would first occur, what supports that judgement, and whether peak weeks bring it forward. Clarify how daily financial loss is assessed across an interruption. Record financial, customer and regulatory effects separately.

Goods receipt, quality release and payroll appear in Site A’s list. Ask whether they affect the Site B dispatch boundary; for any additional activity brought into scope, ask initially only where its impacts differ from dispatch.  
Source: site-a-activity-list.md, activities A1, A3 and A4.

**2. MTPD**

At what point would the dispatch interruption become unacceptable under the approved impact criteria, and why? Does that point change during peak weeks?

The activity owner sets the maximum tolerable period of disruption (MTPD). Leave its value empty in this draft.

| Candidate activity | Status | MTPD | Interview | Confirmation date |
|---|---|---|---|---|
| Does chilled dispatch belong in Site B’s activity scope? Source: site-a-activity-list.md, version 3, 12 March 2026, A2. | candidate, to confirm | | | |

**3. People, with the skills, authorities and mandates the work needs**

Does the dispatch lead own the activity and have authority to confirm its requirements? Does the HR draft’s description of three shift leaders still apply? What staffing is needed by shift in ordinary and peak weeks, and what skills, authorities and mandates must those people hold?

The Site A list identifies a dispatch lead, but does not establish Site B staffing. The three-shift-leader description is an unverified HR draft statement.  
Sources: site-a-activity-list.md, A2; site-b-org-chart.md, dispatch reporting line, **draft under Gaps**.

**4. Seats and buildings**

Which seats, work areas and buildings does Site B dispatch require, and how do those requirements change at peak?

These requirements are **not in the sources**. Site A’s two dock doors are recorded for goods receipt, not dispatch; ask whether there is any corresponding requirement at Site B rather than transferring it.  
Source: site-a-activity-list.md, A1.

**5. IT and applications, each with its RTO and its RPO**

Is LogiStock still the warehouse system used for dispatch at Site A, and does Site B use it too? Which applications does Site B dispatch actually require?

The Site A list says “manual export to Site B possible”. What is exported, who performs and receives it, and can Site B use it during a dispatch interruption?  
Source: site-a-activity-list.md, A2.

For each confirmed application, ask the owner to set its recovery time objective (RTO) and recovery point objective (RPO), supported by dispatch impacts and acceptable data loss. Both fields stay empty here.

**6. Suppliers and other third parties**

Is NordFrost still the carrier for Site A, and is it also a carrier for Site B dispatch? Who else carries dispatch loads, and which carrier contacts need checking?

Site A records no second carrier. Does Site B have a different arrangement, especially during peak weeks? Do not infer that Site B has a sole carrier.  
Source: site-a-activity-list.md, A1 and recorded dependencies.

If a resource depends on a single supplier, carrier or person, ask the owner to identify and confirm that dependence.

**7. Dependencies**

Record up- and downstream relationships with other departments separately from suppliers, each with the RTO the relationship carries.

Does Site B require quality release before dispatch, as Site A does? Is Site A’s QA team still providing Site B’s coverage, as the HR draft suggests? Who authorises release, and what does dispatch need to receive?  
Sources: site-a-activity-list.md, A3 and recorded A2–A3 dependency; site-b-org-chart.md, QA line, **draft under Gaps**.

What relationship with Site A supports the manual export, and what must each department deliver to the other?  
Source: site-a-activity-list.md, A2.

Are there additional upstream or downstream departmental relationships needed for dispatch? Those relationships are **not in the sources**. Ask the respective owners to establish them and set their relationship RTOs; leave the fields empty here.

**Candidate requirement sheet**

All entries remain questions. They enter the requirements register only after the activity owner confirms them. The source dates below are evidence dates, not confirmation dates.

| Class | Candidate question | Source, date and section | Status | RTO | RPO | Interview | Confirmation date |
|---|---|---|---|---|---|---|---|
| People | Who owns dispatch, and what shift staffing, skills, authorities and mandates does it require? | site-a-activity-list.md, v3, 12 March 2026, A2; Site B detail: Gaps | candidate, to confirm | | | | |
| Seats and buildings | Which seats and buildings does Site B dispatch require? | Gaps: not in the sources | candidate, to confirm | | | | |
| IT and applications | Does dispatch require LogiStock, and which other applications are required? | site-a-activity-list.md, v3, 12 March 2026, A2; additional applications: Gaps | candidate, to confirm | | | | |
| IT and applications | Is the recorded manual export usable by Site B, and what resources does it require? | site-a-activity-list.md, v3, 12 March 2026, A2 | candidate, to confirm | | | | |
| Suppliers | Is NordFrost still the carrier, does Site B use it, and are other carriers required? | site-a-activity-list.md, v3, 12 March 2026, A1 and dependencies | candidate, to confirm | | | | |
| Departmental dependencies | Does Site B dispatch depend on quality release from Site A? | site-a-activity-list.md, v3, 12 March 2026, A3 and dependencies; Site B arrangement: Gaps | candidate, to confirm | | | | |
| Departmental dependencies | What interdepartmental relationship supports the manual export to Site B? | site-a-activity-list.md, v3, 12 March 2026, A2 | candidate, to confirm | | | | |

No source proposes recovery times. All MTPD, RTO and RPO fields remain empty.

**Organiser’s take-in sheet**

Provisional total: 45 minutes. No source conflict is established; check possible differences first. Questions marked **Drop first** may be deferred if time runs short.

*Source differences and scope — 5 minutes*

Where does Site B’s dispatch arrangement differ from the Site A list or the HR draft?

Does the HR draft still describe your team and the QA coverage correctly?

Where does dispatch responsibility begin and end?

*Impacts over time and peak weeks — 10 minutes*

Which weeks are your dispatch peaks, and do weeks 49–52 and week 14 apply here?

Which interruption time horizons should we use?

At each horizon, what financial, customer and regulatory effects would you expect?

What evidence supports those effects?

How do those effects change during peak weeks?

**Drop first:** For any other activity we bring into scope, where do its impacts differ from dispatch?

*MTPD — 4 minutes*

When would the dispatch interruption become unacceptable, and which impact makes it unacceptable?

Does that point change during peak weeks?

*People — 7 minutes*

Who can confirm dispatch requirements?

What is the shift pattern, and how does it change at peak?

How many people are needed on each shift, with what skills, authorities and mandates?

Does any requirement depend on one particular person?

*Seats and buildings — 4 minutes*

Which seats, work areas and buildings does dispatch need?

What changes during peak weeks?

*IT and applications — 6 minutes*

Is LogiStock still the system used at Site A, and do you use it here?

Which applications does dispatch need?

How does the manual export from Site A work, and can you use it during an interruption?

For each application, what recovery time and acceptable data loss will you set?

*Suppliers and other third parties — 4 minutes*

Is NordFrost still the carrier, and does it carry for Site B?

Which other carriers do you use, and who holds their current contacts?

Are any carrier arrangements dependent on a single provider?

**Drop first:** What further carrier detail needs a separate follow-up?

*Departmental dependencies — 5 minutes*

Does dispatch need QA release from Site A before it can proceed?

What must QA deliver, who authorises it, and by when must that relationship recover?

What must Site A and Site B deliver to each other for the manual export?

Which other departments supply dispatch or depend on its output, and what recovery time does each relationship carry?

**Gaps**

- **Organiser’s own statements, not sources:** the interviewee is Site B’s dispatch lead, who knows the shift pattern and carrier contacts; the requested return is resources and peak weeks. These statements shape the interview, but supply no requirement values. Entries supported only by them have Source **Gaps**.
- **Interview duration omitted:** assume a provisional 45-minute agenda for planning only.
- **Site B organisation chart:** undated, unversioned HR draft. Current ownership, three shift leaders and Site A QA coverage require owner confirmation and a current approved source.
- **Not in the sources:** Site B peak weeks, staffing requirements, seats and buildings, application inventory, carrier arrangements, contact details, impact evidence, time horizons and recovery values. Obtain these through the owner interview.
- **Activity ranking:** not in the sources. Do not treat the numbered Site A list as a priority order.
- **Currentness:** check whether the approved Site A list and impact criteria have been superseded.
- **Reviewers:** the dispatch activity owner confirms each requirement and sets MTPD, RTO and RPO; top management approves the BIA results. Individual names are not in the sources.

Compare the interview findings with Site A’s register. Put each conflict to the two owners, not to the model. Hand on the confirmed and unconfirmed marks intact, retaining each entry’s source, source date, interview and owner confirmation date.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. Reviewer: __________. Review date: __________.

**Tool calls (JSON events):**

- none
