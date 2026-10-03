# $prepare-bia case 2, run2: Codex, guidance at 836c32f

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0ff16-3568-7a30-a6cd-bb12176d097f`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the dispatch interview guide and check which register entries the sources support as confirmed.

What data classification do the attached files hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) says: “Ask the data class first.” I read the attachments before that check; that was my mistake. I’ll pause here. No files were changed.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '"'!node_modules'"' -g '"'!vendor'"'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md site-a-activity-l`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

You’ve classified the material as High and confirmed this environment is approved for it. Memory, past chats, other project files, connectors and web search are off; I’ll use only the attachments and the skill’s guidance.

Who is the interview with, and is the dispatch guide for Site A or Site B? The activity list covers Site A, but the register is headed Site B.

How long is the interview?

Which approved impact criteria and time bands should the interview use? None are attached.

Please answer the three intake questions so I can draft the guide.

The attachments contain no owner confirmation. Under [prepare-bia](.agents/skills/prepare-bia/SKILL.md), a requirement enters the register “only when the owner confirms it,” so proposed entries must remain **candidate, to confirm**, with recovery fields blank.

This workspace is read-only. I can return the guide and proposed register rows in chat, but cannot edit the files.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** skip

**Reply (verbatim):**

I’ll proceed with the intake answers marked as skipped. I’ll use Site A’s dispatch activity as the interview focus and flag the Site B register heading for review. No owner confirmation is documented, so the proposed entries will remain “candidate, to confirm”; the read-only workspace also prevents file edits.

Sources:
- **site-a-activity-list.md** — version 3, 12 March 2026; approved by the Site A manager.
- **requirements-register.md** — version 1, 1 September 2026; draft, headed Site B; contains no entries.

**Draft dispatch interview guide and proposed register content**

No files were changed: the workspace is read-only. The sources document activities but contain no activity-owner confirmation of requirements. All proposed entries below therefore remain **candidate, to confirm**.

**Gaps and working assumptions**

- Intake answers were skipped: **own statements, not sources**. For planning only, assume a 30-minute interview focused on Site A dispatch; interviewee unconfirmed.
- The Site A activity list and Site B register cover different sites. Resolve the intended site before transferring any rows; Site A requirements cannot establish Site B requirements.
- Approved impact criteria, time bands and activity priority rankings are **not in the sources**. Dispatch receives the detailed impact discussion because it is the requested focus, not because the sources rank it highest.
- The Site B register is a draft, not an approved source of current requirements.
- Required staffing, skills, authorities, mandates, dispatch premises, downstream departments and owner-set recovery times are **not in the sources**.
- Whether the March activity list remains current needs owner review.

**Candidate activities and resource questions**

These are proposed rows for review, not confirmed register entries. Each cited source is dated 12 March 2026. Interview and confirmation-date fields remain empty.

| Activity | People and mandates | Seats and buildings | IT and applications | Suppliers | Source | Status | Interview | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Goods receipt, chilled | Is the Warehouse lead still the owner? What people, skills, authorities and mandates does the work require? | Are the two dock doors still required? | What is required? Not in the sources. | Is NordFrost still the carrier? Is there an alternative? | Site A activity list, A1 and Dependencies recorded | candidate, to confirm | | | | | |
| Dispatch, chilled | Is the Dispatch lead still the owner? What people, skills, authorities and mandates does the work require? | What seats and buildings are required? Not in the sources. | Is LogiStock still required? Is manual export to Site B still possible, and what does it support? | Is NordFrost still the carrier? Is there an alternative? | Site A activity list, A2 and Dependencies recorded | candidate, to confirm | | | | | |
| Quality release | Is the QA manager still the owner? What people, skills, authorities and mandates does the work require? | Is the lab still at Site A only, and is it required for release? | What is required? Not in the sources. | What is required? Not in the sources. | Site A activity list, A3 | candidate, to confirm | | | | | |
| Payroll | Is HR shared service still the owner? What people, skills, authorities and mandates does the work require? | Is payroll still run from head office, and what premises are required? | What is required? Not in the sources. | What is required? Not in the sources. | Site A activity list, A4 | candidate, to confirm | | | | | |

The four activities are documented at Site A. Their applicability to Site B remains a question.

**Department dependencies**

Carrier questions belong under suppliers. Department relationships are recorded separately.

| Activity | Relationship question | Source | Source date | Status | Interview | Confirmation date | Relationship RTO |
|---|---|---|---|---|---|---|---|
| Dispatch, chilled | Must Quality release still finish before dispatch? Which departments own each side of that relationship? | Site A activity list, Dependencies recorded | 12 March 2026 | candidate, to confirm | | | |
| Dispatch, chilled | Does manual export involve a department at Site B? If so, what does each department provide or receive? | Site A activity list, A2 | 12 March 2026 | candidate, to confirm | | | |

Other upstream and downstream department relationships are **not in the sources**. Any conflict found when comparing sites goes **to the two owners, not to the model**.

**Organiser’s take-in sheet — provisional 30 minutes**

*Scope conflict — 3 minutes*

Are we interviewing about Site A dispatch, or preparing candidates for Site B?
Why is the register headed Site B when the activity list covers Site A?
Which owners should resolve that scope difference?

*1. Impacts over time — 7 minutes*

Which approved impact criteria and time bands should we use?
At each agreed time band, what happens if chilled dispatch stops?
How do those impacts change during weeks 49–52 and week 14?
What evidence supports each impact rating?
Where do goods receipt, quality release and payroll differ from dispatch? **Drop first if late.**

*2. MTPD — 3 minutes*

At what point would dispatch disruption become unacceptable under the approved criteria?
What evidence supports the MTPD you set?

*3. People — 4 minutes*

Is the Dispatch lead still the activity owner?
Which people are required, with the skills, authorities and mandates the work needs?
Does the work depend on one person, and who can cover them?

*4. Seats and buildings — 2 minutes*

Which seats and buildings does dispatch require?
Which location constraints affect the ability to continue dispatch?

*5. IT and applications — 4 minutes*

Is LogiStock still the warehouse system dispatch needs?
Which applications are required, each with its RTO and its RPO set by you?
Is manual export to Site B still possible?
What work can that export support, and what limits have been demonstrated?

*6. Suppliers and other third parties — 3 minutes*

Is NordFrost still the carrier?
Is a second carrier available, although none was recorded in the activity list?
Which other third parties are essential to dispatch?

*7. Department dependencies — 4 minutes*

Must quality release still occur before dispatch?
Which departments provide inputs to dispatch and receive its outputs?
What RTO does each relationship carry?
Do the owners on both sides record the same requirement?

If time runs short, drop the comparison with other activities first and record unanswered questions for follow-up.

The activity owner should **“use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”** The activity owner confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Interview references, confirmation dates and recovery fields remain blank until those steps occur.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
