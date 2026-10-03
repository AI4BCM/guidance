# check-against-standards baseline (no skill loaded), run1: Codex, guidance at 6d0d3fb

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a10173-fe80-7723-b141-42e22435f2e5`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’ll read the draft and check for gaps, inconsistencies, and decisions that need to be resolved before board review.

**I recommend revising this draft before board approval.** It identifies owners and scope, but leaves testing, recovery priorities, board accountability, and incident response materially underspecified.

I reviewed it against ISO 22301:2019 as a good-practice benchmark and, **if this is an EU payment institution within scope**, DORA. The draft does not establish jurisdiction or authorisation status, so DORA applicability needs confirming. This is a document review; supporting procedures may address some gaps.

| Draft section | Finding | Change before approval |
|---|---|---|
| **3. Roles** | The COO owns the policy, but the board’s accountability, approval role, and oversight are absent. | Specify board approval and oversight, reporting on readiness and deficiencies, and responsibility for providing resources. Under DORA Article 5, the management body retains responsibility for ICT risk. |
| **4. Business impact analysis** | A three-year cycle can leave priorities outdated. Coverage does not explicitly include dependencies, suppliers, staff, premises, or supporting processes. | Require a BIA covering critical services and their dependencies, with reviews after material changes or incidents. An annual review is a sensible internal requirement; **ISO 22301 does not prescribe a universal annual BIA frequency**. See clause 8.2.2 and DORA Article 11(5). |
| **5. Testing** | Biennial desktop walkthroughs provide little evidence that systems can recover. | Require an annual exercise programme plus testing after substantive changes, including practical restoration and appropriate failover scenarios. Record results, assign corrective actions, and retest failures. Where applicable, DORA Article 11(6) requires at least yearly testing of ICT continuity and response/recovery plans and testing after substantive changes; ISO 22301 clause 8.5 requires a planned exercise programme without fixing an annual interval. |
| **6. Recovery objectives** | IT alone sets recovery times, with no connection to business impact. Recovery point objectives—acceptable data loss—are missing. | Have service owners establish business recovery requirements through the BIA; IT translates these into system recovery time and recovery point objectives and validates feasibility. Escalate gaps for management decision. See ISO 22301 clause 8.2.2 and DORA Article 12(6). |
| **2. Scope** | Services and offices are listed, but outsourced services and shared dependencies are not explicit. The website exclusion has no rationale. | Include relevant third parties, payment infrastructure, telecommunications, utilities, data, and key personnel. Validate the website exclusion against its actual dependencies and role in customer communications. |
| **Missing: response and recovery framework** | The policy does not require activation criteria, incident leadership, deputies, communications, workarounds, or controlled return to normal operations. | Require maintained business continuity and ICT recovery plans covering these elements, with clear links to incident management and regulatory reporting procedures. See ISO 22301 clause 8.4 and DORA Articles 11 and 14. |
| **7. Review** | Triennial policy review has no change-triggered review or board reporting requirement. | Require annual review and review following material changes, major incidents, exercises, or regulatory developments. Distinguish policy review from management review of the programme’s effectiveness. Annual policy review is a recommended internal control; ISO 22301 requires management review at planned intervals, not a universal annual policy revision. |

Suggested wording for the most urgent clauses:

> **Testing:** Business continuity and ICT response and recovery plans shall be tested at least annually and following substantive changes. The programme shall combine scenario exercises with practical recovery tests appropriate to critical services and dependencies. Results and corrective actions shall be documented, reported to management, and tracked to closure.
>
> **Recovery objectives:** Business service owners shall establish recovery priorities, recovery time objectives, and recovery point objectives using the business impact analysis. The IT manager shall maintain aligned system recovery objectives and validate recovery capability. Unmet requirements shall be escalated for management decision.
>
> **Governance and review:** The management board shall approve this policy and oversee its implementation. The COO shall report at least annually on continuity readiness, exercise results, material deficiencies, and remediation. This policy shall be reviewed annually and after material changes or significant incidents.

Before submission, confirm the applicable regulatory regime, reference the supporting plans and procedures, and include an implementation plan for any controls that are not yet operating. Also remove “invented for this eval” from the organisation description.

Regulatory references: [DORA, Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj). I have not verified subsequent amendments or jurisdiction-specific requirements against live sources.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g 'AGENTS.md' -g '*.md'"`
- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`
