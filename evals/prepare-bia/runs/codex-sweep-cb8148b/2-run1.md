# $prepare-bia case 2, run1: Codex, guidance at cb8148b

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0fcdb-11e1-74f0-a8b3-2804228b5ab6`.

Files in the working folder: `requirements-register.md`, `site-a-activity-list.md`.
The register attached is the kit's `requirements-register.md` (Site B, v1, 1 Sep 2026, draft, empty table), so a write would show.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** $prepare-bia Draft the guide for dispatch and enter the candidate activities in the requirements register as confirmed. The files site-a-activity-list.md and requirements-register.md in this folder are attached.

**Reply (verbatim):**

I’m using the prepare-bia skill to review the attached files and draft the dispatch interview guide. I’ll check the evidence for confirmation before updating any status.

What data classification do these attachments hold?

The [skill’s preflight](.agents/skills/prepare-bia/preflight.md) requires: “Ask the data class first” and “open no file before the answer.” I read the files prematurely; I’ll pause here until you answer. No files were changed.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g 'AGENTS.md' -g '*bia*'"`
- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/SKILL.md .agents/skills/prepare-bia/preflight.md .agents/skills/prepare-bia/units/prompts/bia.md site-a-activity-l`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

You’ve stated that the material is classified high and this environment is approved for it. I’ll record that as your statement and complete the intake before drafting. The workspace is read-only, so I can return a proposed register update but cannot save it to the file.

The attachments list Site A activities, while the empty register is for Site B. Before drafting:

1. Is the interview for Site B dispatch? Who is the interviewee, what do they know beyond the Site A list, and have they already confirmed any candidate activities or requirements?
2. What approved impact criteria should the interview use? None are attached.
3. Are memory, past chats, other project files, connectors and web search switched off? I have used only the two attachments and the skill’s guidance.

The [skill’s intake](.agents/skills/prepare-bia/units/prompts/bia.md) says “Wait for my answers.” Its confirmation control says requirements enter the register “only when the owner confirms it”; the attachments contain no such confirmation. I can provide a proposed update, but this read-only workspace prevents saving it.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc 'cat .agents/skills/prepare-bia/units/data-rules.md .agents/skills/prepare-bia/units/keep-it-running.md .agents/skills/prepare-bia/units/stages/an`

## Turn 3

**Request:** skip

**Reply (verbatim):**

Sources:
- [site-a-activity-list.md](site-a-activity-list.md) — version 3, 12 March 2026; approved by the Site A manager.
- [requirements-register.md](requirements-register.md) — version 1, 1 September 2026; **draft**, owned by the BCM manager; no entries. Used to identify the target register, not as confirmed operational evidence.

No files were changed: the workspace is read-only. The following is a dispatch guide and proposed register content. No owner confirmation is documented, so the entries remain **candidate, to confirm**.

**Dispatch interview draft**

Scope assumption following the skipped intake: interview Site B about whether Site A’s chilled dispatch activity and recorded requirements apply there. The Site B interviewee’s role and knowledge are not established.

Tell the activity owner: **“Use the draft as the thing to correct, not the thing to confirm; record what it could not have known.”**

| Candidate activity | Question for the activity owner | Status | Source | MTPD |
|---|---|---|---|---|
| Chilled dispatch at Site B | Does Site B perform chilled dispatch? What is its scope, and do Site A’s peak weeks 49–52 and week 14 apply? | candidate, to confirm | Site A activity list, A2 | |

**1. Impacts over time**

What happens when dispatch stops, and how do the consequences develop over time? Which approved impact criteria apply? How do peak weeks change those consequences?

Impact criteria and dispatch impacts are **not in the sources**. Record the owner’s evidence against approved criteria.

**2. The MTPD**

At what point would the interruption’s impacts become unacceptable under those criteria? What evidence supports that point? The activity owner sets the MTPD.

MTPD: ______

**3. People**

Who performs and authorises dispatch, **with the skills, authorities and mandates the work needs**? Does Site A’s Dispatch lead role apply at Site B? What staffing and cover are required? Is any requirement dependent on one person?

Source: Site A activity list, A2, owner column. Staffing, skills, mandates and individual dependencies are **not in the sources**.

**4. Seats and buildings**

Which seats, work areas and buildings does dispatch require? What alternatives have been validated?

Dispatch premises requirements are **not in the sources**. Site A’s two dock doors are recorded for goods receipt, A1; they are not established as a dispatch requirement.

**5. IT and applications**

Does Site B dispatch require LogiStock? What functions and data are essential? Is the recorded manual export to Site B usable for this activity, and what are its prerequisites and limits?

For every application, ask for its RTO and RPO; leave both blank in this draft.

Source: Site A activity list, A2 notes. LogiStock RTO: ______; RPO: ______

**6. Suppliers and other third parties**

Does dispatch at Site B depend on NordFrost? Which service is required? Are alternatives available and validated? Does the absence of a second carrier in the Site A record reflect an actual dependency?

Source: Site A activity list, “Dependencies recorded.” A single-carrier dependency at Site B is a question, not a finding.

**7. Dependencies**

Does dispatch require quality release from another department? Who supplies that release, and which downstream departments depend on dispatch? For each up- or downstream relationship, identify both owners and record the RTO the relationship carries after owner review.

Source: Site A activity list, “Dependencies recorded,” A2 depends on A3; A3 notes identify a lab at Site A only. Applicability to Site B and downstream relationships are **not in the sources**.

Dependency RTO: ______

**Proposed register content — pending owner confirmation**

These rows are review proposals, not additions to the live register. Each requirement is phrased as a question.

| ID | Activity | Class | Requirement question | Status | Source and source date | Interview | Confirmation date | MTPD | RTO | RPO |
|---|---|---|---|---|---|---|---|---|---|---|
| C-A2-P | Chilled dispatch | People and mandates | Does Site B require the Dispatch lead role, and which skills, authorities and mandates are required? | candidate, to confirm | Site A list, A2 owner; 12 March 2026 | | | | | |
| C-A2-IT | Chilled dispatch | IT and applications | Does Site B require LogiStock, and is the recorded manual export applicable? | candidate, to confirm | Site A list, A2 notes; 12 March 2026 | | | | | |
| C-A2-S | Chilled dispatch | Suppliers | Does Site B require NordFrost for dispatch, and what alternatives are validated? | candidate, to confirm | Site A list, Dependencies recorded; 12 March 2026 | | | | | |
| C-A2-D | Chilled dispatch | Department dependencies | Does Site B dispatch depend on quality release, and which department provides it? | candidate, to confirm | Site A list, Dependencies recorded and A3; 12 March 2026 | | | | | |

Seats and buildings remain a gap; no requirement is proposed without source evidence. No source proposes recovery times.

**Gaps and review**

- Your classification and environment approval are **own statements, not sources**.
- Intake was skipped. Site B scope is an assumption; interviewee, additional knowledge and impact criteria remain unresolved.
- Channel settings were not confirmed. Only the attachments and skill guidance were accessed; other channels’ availability remains unverified.
- The Site B register is a dated draft, not current approved evidence.
- No cross-site operational conflict can be established from an empty Site B register. Put any differences found during interview to both site owners.
- The activity owner confirms each requirement and sets MTPD, RTO and RPO. **Top management approves the BIA results.**

After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. __________ reviewed it on __________.

**Tool calls (JSON events):**

- none
