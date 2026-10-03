# $prepare-bia case 1, run2: Codex, guidance at 4dc1660

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff33-6fb6-7902-94f8-4e61be753c31`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide from the attached material. I’ll read its preflight instructions and the three source files first.

What data sensitivity class does the attached material hold?

What data sensitivity class does the attached material hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first.” I need your answer before reading the attachments and drafting the guide.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g '*.md' -g 'AGENTS.md' -g '"'!node_modules'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Memory, past chats, other project files, connectors and web search are off. I’ll use only the three attachments and the sources shipped with prepare-bia. The draft will stay in this chat, with recovery fields left blank.

Who is the interview with (role or roles)?

What do you need back from the interview—for example, a completed dispatch BIA or a list of requirements and unresolved questions?

How long will the interview run?

Before drafting, please confirm:

- Who is the interview with?
- What do you need back from the interview?
- How long will it run?

The [prepare-bia intake](.agents/skills/prepare-bia/units/prompts/bia.md) requires me to “Wait for my answers.”

The sources establish Site A’s dispatch activity and approved impact criteria. Site B’s organisation chart is an undated draft, so its roles and QA coverage will be questions to verify.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/analysis.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on dispatch resources and peak weeks. Since you left the duration open, I’ll use a provisional 30-minute schedule and mark questions to drop first. Site A’s peak weeks, LogiStock and NordFrost will be prompts for the Site B owner to check; the draft does not establish that they apply at Site B.

**Site B dispatch interview guide — draft**

Sources:

- **site-a-activity-list.md:** version 3, 12 March 2026; approved by the Site A manager. References below identify its activity rows or recorded dependencies.
- **impact-criteria.md:** version 1.1, 4 February 2026; approved by top management.
- **site-b-org-chart.md:** no version or date; HR draft. Listed under Gaps and used only to frame questions.

Interview scope: dispatch resources and peak weeks. All Site B entries below are **candidate, to confirm**.

Ask the activity owner to **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known”.** A resource requirement enters the register only after the owner confirms it.

**1. Impacts over time**

The sources do not rank activities by criticality. Explore dispatch in full because it is the interview scope; for related activities, ask only where their impacts differ.

| Candidate activity or impact | Question for the activity owner | Source |
|---|---|---|
| Dispatch, chilled — candidate, to confirm | Does Site B carry out chilled dispatch, and where does your responsibility start and finish? | Site A activity list, “Dispatch, chilled”; Site B scope remains to confirm |
| Peak weeks — candidate, to confirm | Site A records weeks 49–52 and week 14. Are these also Site B’s peak weeks? What differs, and what changes in the resources needed? | Site A activity list, “Dispatch, chilled” |
| Financial impact — candidate, to confirm | As dispatch remains interrupted, how do daily losses change during normal and peak weeks? When do they cross the approved financial levels? | Impact criteria, Financial column |
| Customer impact — candidate, to confirm | Over the same interruption periods, when would complaints, key-account lateness or loss arise? | Impact criteria, Customer column |
| Regulatory impact — candidate, to confirm | Could the interruption lead to an authority report or production stoppage? If so, when and why? | Impact criteria, Regulatory column |

Use the approved levels:

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | under EUR 10k a day | one customer complains | none |
| 2 | EUR 10k–100k a day | a key account is late | a report to the food authority |
| 3 | over EUR 100k a day | a key account is lost | the authority stops production |

Source: impact-criteria.md, approved criteria table. Interruption intervals and Site B ratings are **not in the sources**; have the owner establish them.

**2. MTPD**

At what interruption duration do dispatch’s impacts become unacceptable, and which impact supports that boundary? Does the boundary change during peak weeks?

The activity owner sets the MTPD. Its field remains blank in this draft.

**3. People**

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Dispatch ownership — candidate, to confirm | Site A records a dispatch lead as owner. Is that also the accountable role at Site B? | Site A activity list, “Dispatch, chilled” |
| Shift coverage — candidate, to confirm | The HR draft lists three shift leaders. Is that still accurate? What staffing is required on each shift, including peak weeks? | Gaps: Site B organisation draft, Dispatch lead branch |
| Skills, authorities and mandates — candidate, to confirm | What skills, authorities and mandates does dispatch need on each shift? Which roles must be able to make decisions? | Gaps: not in the sources |
| Dependence on one person — candidate, to confirm | Does any essential skill, authority or carrier contact depend on one person? Who can cover it? | Gaps: not in the sources |

**4. Seats and buildings**

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Dispatch workspace — candidate, to confirm | Which seats, work areas and buildings does dispatch require, and what capacity is needed in normal and peak weeks? | Gaps: not in the sources |

Site A’s two dock doors are recorded for goods receipt, so they do not establish a dispatch requirement at Site B.

**5. IT and applications**

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Warehouse application — candidate, to confirm | Site A records LogiStock. Is LogiStock still the application used for Site B dispatch, or does Site B use something else? | Site A activity list, “Dispatch, chilled” |
| Manual export — candidate, to confirm | Site A records that manual export to Site B is possible. Is that still possible, what does it support, and what limits would affect dispatch? | Site A activity list, “Dispatch, chilled” |
| Application recovery and data — candidate, to confirm | For each application you identify, what RTO and RPO does dispatch require, and how do these follow from the impacts? | Gaps: Site B application requirements and recovery values are not in the sources |

**6. Suppliers and other third parties**

| Candidate requirement | Question for the activity owner | Source |
|---|---|---|
| Carrier — candidate, to confirm | Site A records NordFrost. Is NordFrost still the carrier for Site B dispatch? Which other carriers or third parties are required? | Site A activity list, recorded dependencies |
| Single-carrier exposure — candidate, to confirm | Site A records no second carrier. Does Site B depend on a single carrier, or is an alternative available? What can it cover during peak weeks? | Site A activity list, recorded dependencies |

Keep carriers in this resource class, separately from departmental dependencies.

**7. Dependencies on other departments**

| Candidate relationship | Question for the activity owner | Source |
|---|---|---|
| Upstream quality release — candidate, to confirm | Site A dispatch depends on quality release before dispatch. Does Site B have the same dependency? Is Site A still providing QA coverage, as the HR draft suggests? | Site A activity list, recorded dependencies; Gaps: Site B organisation draft, QA line |
| Other upstream and downstream relationships — candidate, to confirm | Which other departments provide inputs to dispatch or depend on its outputs? What RTO does each relationship carry? | Gaps: not in the sources |

For related goods receipt or quality-release activities, ask where impacts or resource needs differ from dispatch. Refer any conflicting accounts to the **two activity owners**.

**Blank recording fields**

These fields remain empty. Each requirement above retains its source reference and the source date listed at the top; entries supported only by gaps retain Source **Gaps**.

| Candidate entry | Interview reference | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|
| Site B dispatch | | | | | |
| Each application identified | | | | | |
| Each departmental relationship identified | | | | | |

No recovery times are proposed in the attachments.

**Organiser’s take-in sheet — provisional 30 minutes**

*Source differences and draft checks — 3 minutes; keep these first.*

Does Site B dispatch depend on quality release from Site A, and is the draft organisation chart accurate?

Are LogiStock, NordFrost and manual export to Site B still relevant?

Which Site A arrangements differ at Site B?

*Impacts and peak weeks — 6 minutes.*

What does dispatch cover at Site B?

Are weeks 49–52 and week 14 your peak weeks too?

What resources change during those weeks?

As dispatch stays stopped, when do financial, customer and regulatory impacts worsen?

*MTPD — 3 minutes.*

When would the interruption become unacceptable, and why?

*People — 5 minutes.*

What is the shift pattern, and how many people are needed on each shift?

What skills and decision-making authority must each shift have?

Does anything essential depend on one person?

*Seats and buildings — 3 minutes.*

Which work areas and buildings do you need, and how much capacity is needed at peak?

*IT and applications — 4 minutes.*

Which applications does dispatch need?

What recovery time and acceptable data loss do you require for each?

Can the manual export support dispatch, and for how long?

*Suppliers — 3 minutes.*

Which carriers and other third parties do you rely on?

Can another carrier cover the work during peak weeks?

*Departmental dependencies — 3 minutes.*

What must QA and other departments provide before you can dispatch?

Which departments depend on your outputs?

How quickly must each relationship be restored?

*Drop first if late.*

Where do goods receipt or quality-release impacts differ from dispatch?

What further detail is needed on the manual export?

**Gaps and review**

- **Own statements, not sources:** the organiser identifies the interviewee as Site B’s dispatch lead, says they know the shift pattern and carrier contacts, and requests resources and peak weeks. These statements shape scope; they do not populate requirement values.
- **Duration:** unanswered. The 30-minute schedule is a planning assumption.
- **Site B organisation chart:** undated, unversioned HR draft. Obtain a dated, approved chart or verify its roles and QA coverage with the owners.
- **Site B requirements:** current staffing, mandates, facilities, applications, carriers, peak weeks and recovery requirements remain unconfirmed. The interview must establish them.
- **Source currency:** the approved Site A list establishes Site A’s recorded position, not Site B’s current arrangements. Confirm applicability and any subsequent changes.
- The **activity owner** confirms every requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Preserve confirmed and unconfirmed marks through handover.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
