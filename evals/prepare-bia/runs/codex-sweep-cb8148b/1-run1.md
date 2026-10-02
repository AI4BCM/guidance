# $prepare-bia case 1, run1: Codex, guidance at cb8148b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fcd6-79f4-7551-99bb-7b0e2591ecc5`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to draft the Site B dispatch interview guide. I’ll read the attached material and the skill’s preflight instructions first.

What data classification do the three attachments hold?

The [prepare-bia preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I’ve read the skill instructions; I haven’t opened the attachments.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd; rg --files -g 'AGENTS.md' -g '*.md' -g '"'!node_modules'"' -g '"'!vendor'"' -g '"'!*LICENSE*'"' . .agents"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md'`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I’ll check how the skill handles “high” data, then read the attachments if permitted.

The impact criteria are approved and dated. Site B’s organisation chart is an undated, unversioned HR draft, so its roles and QA arrangement need verification.

Before I draft the guide:

1. Who is the interviewee, and what is their role?
2. What do they know about Site B dispatch that you do not?
3. What must the interview return—for example, corrected activities, resource requirements and unresolved dependencies? Please also confirm whether memory, past chats, other project files, connectors and web search are switched off.

The [prepare-bia skill](.agents/skills/prepare-bia/units/prompts/bia.md) requires this intake and says “Wait for my answers.” Your answers will be recorded as organiser statements under Gaps, rather than as evidence or recovery values.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md impact-criteria.md site-b-org-chart.md'`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/stages/analysis.md .agents/skills/prepare-bia/units/workflow-design.md'`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

I’ll focus the guide on resources and peak weeks for the Site B dispatch lead. Site A provides useful comparison questions, but the attachments do not establish Site B’s systems, staffing or carrier arrangements. I’ll keep those as candidates and leave recovery fields blank.

**Site B dispatch interview guide — draft**

Sources used:

- **S1 — site-a-activity-list.md:** version 3, 12 March 2026; approved by the Site A manager. Sections: activity table A1–A4 and recorded dependencies.
- **S2 — impact-criteria.md:** version 1.1, 4 February 2026; approved by top management. Section: impact-level table.
- **S3 — site-b-org-chart.md:** no version or date; HR draft. Listed under Gaps and used only to frame verification questions, not as current evidence.

Interviewee: Site B dispatch lead, as stated by the organiser. Focus: resources and peak weeks.

Tell the interviewee: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”** An AI-drafted resource requirement enters the requirements register only after the activity owner confirms it.

**Candidate activity and resource questions**

| ID | Class | Question for the activity owner | Source and limitation | Status |
|---|---|---|---|---|
| B1 | Activity and peaks | Does Site B perform chilled dispatch? What are its boundaries and peak weeks? Do Site A’s weeks 49–52 and week 14 apply here? | S1, A2, 12 March 2026. Site B applicability is not established. | candidate, to confirm |
| B2 | People and mandates | Who performs and authorises dispatch? Is the draft structure of a dispatch lead and three shift leaders accurate? What staffing, skills and mandates does each shift need? | S3, dispatch reporting line; undated draft. Staffing requirements are not in the sources. | candidate, to confirm |
| B3 | Seats and buildings | Which seats and buildings does Site B dispatch require, and in what quantities? | Not in the sources. S1, A1’s two dock doors concern Site A goods receipt; they do not establish Site B dispatch requirements. | candidate, to confirm |
| B4 | IT and applications | Does Site B dispatch require LogiStock? What does the manual export from Site A provide, and which applications and data does Site B actually require? | S1, A2, 12 March 2026. Only Site A’s system and export possibility are documented. | candidate, to confirm |
| B5 | Suppliers and third parties | Does Site B dispatch depend on NordFrost? Which carriers and other third parties are required, and are alternatives available? | S1, recorded dependencies, 12 March 2026. No second carrier is recorded for Site A; this does not establish Site B’s position. | candidate, to confirm |
| B6 | Department dependencies | Does Site B dispatch require a prior release from Site A QA? What are its other upstream and downstream departmental relationships? | S1, A2→A3 dependency, 12 March 2026; S3, draft QA arrangement. Site B relationships need verification. | candidate, to confirm |

**Blank capture fields** — linked to the candidate entries above. Source references and dates remain attached to each ID. Empty cells are intentional.

| ID | MTPD | RTO | RPO | Dependency RTO | Interview reference/date | Owner confirmation date |
|---|---|---|---|---|---|---|
| B1 | | | | | | |
| B2 | | | | | | |
| B3 | | | | | | |
| B4 | | | | | | |
| B5 | | | | | | |
| B6 | | | | | | |

For each additional application or departmental relationship identified during the interview, capture it separately with its source, interview reference, confirmation status and date.

**1. Impacts over time**

- Correct B1: what starts and ends the dispatch activity, and what output does it deliver?
- Identify Site B’s peak weeks. Explain how volumes and resource needs change during them. Compare explicitly with Site A’s weeks 49–52 and week 14. [S1, A2]
- At each agreed assessment horizon, what financial, customer and regulatory consequences would interrupted dispatch cause? What evidence supports each consequence? [S2, impact-level table]
- How do those consequences differ during peak weeks?

Use the approved criteria below; do not infer Site B’s impact ratings.

| Level | Financial | Customer | Regulatory |
|---|---|---|---|
| 1 | “under EUR 10k a day” | “one customer complains” | “none” |
| 2 | “EUR 10k–100k a day” | “a key account is late” | “a report to the food authority” |
| 3 | “over EUR 100k a day” | “a key account is lost” | “the authority stops production” |

Source: S2, impact-level table. Assessment horizons and the threshold for unacceptable impact are **not in the sources**; the BCM organiser must supply them.

**2. The MTPD**

- Based on the evidenced impacts over time, when would interruption become unacceptable?
- Which consequence determines that boundary, and does the boundary change during peak weeks?
- What evidence or unresolved issue must be addressed before the activity owner sets the MTPD?

The MTPD field remains empty in this draft.

**3. People**

- Correct B2 and the draft reporting structure. What is the actual shift pattern?
- For each shift, what people are required, **“with the skills, authorities and mandates the work needs”**?
- What changes during peak weeks? Who can cover each required role?
- Does any requirement depend on one person? Treat this as an owner question, not a finding.

Basis: S3, dispatch reporting line, subject to verification. Skills, staffing quantities, mandates and cover arrangements are not in the sources.

**4. Seats and buildings**

- Correct B3: identify the required seats and buildings, their capacity and their availability across shifts.
- Which requirements change during peak weeks?
- Which locations could substitute, and what evidence supports their suitability?

Site B premises requirements are not in the sources. Do not transfer Site A’s goods-receipt dock count to Site B dispatch.

**5. IT and applications**

- Correct B4: identify every required application and its required data.
- Does Site B use LogiStock? Explain and verify the manual export to Site B described in S1, A2.
- What can dispatch do without each application, and what limitations apply?
- For each application, obtain the owner’s RTO and RPO decisions and supporting evidence during the interview.

Keep every application’s RTO and RPO empty in this AI draft.

**6. Suppliers and other third parties**

- Correct B5: identify the required carriers and other third parties, their services and peak-period capacity.
- Verify the carrier contacts known to the interviewee.
- Does NordFrost serve Site B? Are alternatives available and usable?
- Is any requirement dependent on a single supplier or carrier?

S1 records NordFrost dependence for Site A’s A1 and A2. It does not establish a sole-carrier requirement at Site B.

**7. Dependencies**

- Correct B6: identify **“up- and downstream relationships with other departments, each recorded with the RTO the relationship carries”**.
- For each relationship, identify the supplying and receiving department, required input or output, and counterpart owner.
- Verify whether Site A QA releases Site B dispatches and how this relates to the Site A-only laboratory. [S1, A3 and dependencies; S3, draft QA arrangement]
- Obtain each relationship’s RTO from its owner during the interview; leave the dependency RTO empty here.

No direct cross-site contradiction is established by the attachments. Put these unresolved comparisons to both owners:

| Comparison to resolve | Owners |
|---|---|
| Site A dispatch peak weeks versus Site B’s actual peaks | Both dispatch leads |
| Site A’s LogiStock/manual-export arrangement versus Site B’s actual system requirements | Both dispatch leads |
| Site A’s NordFrost dependence versus Site B’s carrier arrangements | Both dispatch leads |
| Site A’s release-before-dispatch dependency and laboratory location versus the draft Site B QA arrangement | Site A QA owner and Site B dispatch owner |

Record any conflict found and refer it to the two owners, not to the model.

**Gaps and handover**

- **Organiser statements, not sources:** the material is high sensitivity and this environment is approved for it; the interviewee is Site B’s dispatch lead and knows the shift pattern and carrier contacts; the requested focus is resources and peak weeks. These statements shape scope but fill no requirement or recovery value.
- **S3:** undated, unversioned HR draft. Obtain an approved, dated organisation chart and owner verification.
- **Missing evidence:** Site B activity boundaries, peak weeks, actual staffing and mandates, premises, applications, carriers, departmental relationships and impacts over time. The owner’s interview record and supporting approved documents would settle these.
- **Source-channel settings:** confirmation that memory, past chats, other project files, connectors and web search are switched off was omitted. Only the three attachments and skill guidance were consulted for this draft; the broader configuration has not been verified. Any channel left on belongs under Gaps because the model may draw on it without saying so.
- No source proposes recovery times. All recovery fields remain empty.

The activity owner confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.** Hand over confirmed and unconfirmed marks intact; every entry in this pre-interview draft remains **candidate, to confirm**.

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
