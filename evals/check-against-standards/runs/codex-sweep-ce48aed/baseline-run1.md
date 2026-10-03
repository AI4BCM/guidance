# check-against-standards baseline (no skill loaded), run1: Codex, guidance at ce48aed

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a101af-6bd2-7752-b5fb-6aac48570811`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’ll review the draft for gaps, unclear requirements, and issues the board should resolve before approval.

Which jurisdiction and standards should this be checked against, and is the institution fully authorised or operating under a small-payment-institution exemption? This determines whether EU DORA requirements apply.

The draft leaves several key decisions undefined: who activates the plans, what recovery targets must be met, and how the board oversees readiness. Its two-year desktop testing cycle would also fall short of full EU DORA requirements if those apply. I’m separating firm drafting gaps from requirements that depend on the institution’s jurisdiction and licence.

**I recommend revising this draft before board approval.** It names owners and activities, but does not yet establish an enforceable continuity programme.

I reviewed [bc-policy-draft.md](/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs-codex/check-against-standards/baseline/run1/work/bc-policy-draft.md) using ISO 22301:2019 as a business continuity benchmark. EU DORA findings below are conditional: the draft does not establish jurisdiction or authorisation status.

| Priority | Finding | Required revision |
|---|---|---|
| High | **Governance is incomplete** (§3). Operational owners are named, but board oversight, accountability, resources and reporting are absent. | Require board approval and oversight; assign executive accountability, business-service owners and deputies; require reporting on readiness, failed tests and overdue corrective actions. |
| High | **The BIA is too narrowly defined** (§4). It covers payment services and customer support but does not require analysis of their dependencies or tolerable disruption. | Require assessment of impacts over time, maximum tolerable disruption, minimum service levels, and dependencies on people, premises, ICT, data and suppliers. Require updates following material changes. An annual review is a sensible policy choice; neither ISO 22301 nor DORA should be described as imposing a universal annual BIA cycle. |
| High | **Testing is insufficient** (§5). A desktop walk-through every two years does not demonstrate that systems can recover. | Require a risk-based exercise programme that includes actual recovery and restoration, relevant failover and supplier scenarios, assessment against recovery targets, and tracked remediation. Under **full DORA**, ICT continuity and response/recovery plans must be tested at least annually and following substantive changes—Article 11(6). |
| High | **Recovery objectives lack business ownership and omit data loss** (§6). The IT manager alone sets every RTO. | Require business-service owners to define recovery needs from the BIA, with IT validating feasibility and dependencies. Approve recovery time objectives **and recovery point objectives** through the designated governance process. Full DORA addresses both in Article 12(6). |
| High | **There is no requirement for continuity strategies or actionable plans.** | Require documented arrangements for maintaining and restoring critical services, including staff, alternative working locations, ICT recovery, key providers and payment reconciliation. Specify activation criteria, decision authority, escalation, communications and return to normal operations. Detailed procedures can sit in supporting plans. |
| High | **Scope and exclusions are unsupported** (§2). Critical suppliers and supporting functions are not explicit; the marketing website is excluded without an impact assessment. | Include dependencies needed to deliver payment services, such as treasury, safeguarding and reconciliation where relevant. Justify exclusions through the BIA. Check whether the website supports customer communications during an incident before excluding it. |
| Medium | **Review and assurance are too weak** (§7). A three-year policy review has no event-driven triggers or feedback mechanism. | Require annual review and review after material changes, major incidents and significant test findings. Add training, document control, effectiveness assessment and corrective-action tracking. Distinguish this recommended policy cadence from ISO’s requirement for review at planned intervals. |

The most urgent replacement wording is:

> **Business impact analysis:** The BCM officer shall coordinate a documented BIA covering all in-scope services and their dependencies. Business-service owners shall validate impacts, tolerable disruption, minimum service levels and recovery requirements. The BIA shall be reviewed annually and following material changes.
>
> **Testing:** Continuity and ICT recovery arrangements shall be exercised at least annually and following material changes, using scenarios proportionate to the risks. Exercises shall demonstrate recovery capability against approved objectives. Findings shall have accountable owners, deadlines and verified closure.
>
> **Recovery objectives:** Business-service owners shall propose recovery time and recovery point objectives based on the BIA. The IT manager shall assess technical feasibility and dependencies. Objectives and any unresolved capability gaps shall be approved through the company’s designated governance process.

Before the board pack is finalised, establish the applicable regulatory framework. **“Small payment institution” does not by itself mean DORA is inapplicable:** exempt payment institutions may fall under its simplified framework, so the full-framework requirements cannot automatically be applied.

Reference basis: ISO 22301:2019, particularly clauses 5, 8–10; [DORA, Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), particularly Articles 5, 11, 12 and 16. I could not retrieve the live standards or legislation in this environment, so this is a substantive draft review, not a verified compliance determination.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g 'AGENTS.md' -g '*policy*' -g '*standard*' -g '*.md'"`
- command_execution: `/bin/bash -lc 'nl -ba bc-policy-draft.md'`
- command_execution: `/bin/bash -lc "python - <<'PY'
import urllib.request
url='https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554'
try:
    with urllib.request.url`
- command_execution: `/bin/bash -lc "python3 - <<'PY'
import urllib.request
url='https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554'
try:
    with urllib.request.ur`
