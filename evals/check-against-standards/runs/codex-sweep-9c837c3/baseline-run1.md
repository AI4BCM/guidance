# check-against-standards baseline (no skill loaded), run1: Codex, guidance at 9c837c3

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a10150-1644-7c53-be11-72faa5d42e6a`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’ll read the draft and check for gaps, unclear requirements, and issues the board should resolve before approval.

**I would return this draft for revision before board approval.** It identifies an owner and a scope, but does not establish enough requirements to govern continuity or demonstrate that payment services can recover.

I assessed it against ISO 22301:2019 principles and, conditionally, EU DORA. The organisation’s jurisdiction and authorisation category need confirming: a payment institution exempt under PSD2 can fall under DORA’s simplified framework. “Small” and 140 staff alone do not establish that status.

| Priority | Finding | Recommended change |
|---|---|---|
| High | **Testing is too infrequent and too limited** (§5). A desktop walkthrough every two years does not demonstrate technical recovery. Under DORA’s full framework, Article 11(6) requires at least annual testing of ICT continuity and recovery plans, and testing following substantive changes. | Require annual exercises and relevant testing after material changes. Include technical recovery, backup restoration, failover and supplier disruption where relevant. Record results, assign corrective actions and retest failures. |
| High | **Recovery objectives have no business approval** (§6). The IT manager sets all RTOs; no recovery point objectives or minimum service levels are required. | Business service owners should propose recovery priorities, RTOs, RPOs and minimum acceptable service levels based on the BIA. IT validates feasibility; accountable management approves objectives and accepts residual risks. |
| High | **The BIA requirement is incomplete** (§4). It names services but does not require disruption impacts over time, maximum tolerable disruption, dependencies or recovery resources. A three-year cycle can miss significant changes. | Require those outputs and updates following material changes. An annual review is a sensible baseline for this organisation. ISO 22301 requires planned reviews and updates following significant changes; it does **not** prescribe an annual BIA universally. |
| High | **Response and recovery arrangements are not required**. Plans are mentioned only in the testing section. | Require maintained business continuity and ICT recovery plans covering activation thresholds, escalation, delegated authority, crisis leadership, communications, recovery procedures and return to normal operations. Operational detail can sit in supporting plans. |
| High | **Governance is incomplete** (§3). Ownership is assigned, but board accountability, service-owner responsibilities, resourcing and reporting are absent. | Define management-body approval and oversight, accountable business owners, deputies, funding responsibilities and reporting on readiness, failed tests and overdue corrective actions. |
| Medium | **Scope exclusions lack justification** (§2). Supporting suppliers, outsourced services, people and dependencies are not expressly covered. The website exclusion is unconditional. | Include dependencies supporting in-scope services. Require documented, risk-based exclusions; confirm whether the website supports customer communications, authentication or other recovery needs before excluding it. |
| Medium | **Review is too infrequent and has no event triggers** (§7). | Require annual policy review and review after material changes, significant incidents, exercise findings or regulatory changes. Distinguish policy review from review of plans and the ICT risk framework. |

Suggested replacement wording for the weakest sections:

> **4. Business impact analysis:** The BCM officer coordinates a documented BIA covering in-scope services and their dependencies. It identifies impacts over time, maximum tolerable disruption, recovery priorities, minimum service levels and required resources. Business service owners validate the results. The BIA is reviewed annually and updated following material changes.
>
> **5. Testing:** Business continuity and ICT recovery arrangements are exercised and tested at least annually and following relevant material changes. The programme includes practical recovery tests and scenarios involving critical dependencies. Findings are documented, assigned to owners and tracked to closure, with retesting where necessary.
>
> **6. Recovery objectives:** Business service owners propose RTOs, RPOs and minimum service levels based on the BIA. The IT manager validates technical feasibility. Accountable management approves the objectives and any residual risks.
>
> **7. Review:** The policy owner reviews this policy at least annually and following material changes, significant incidents or material exercise findings. Material revisions are submitted to the management board for approval.

Before resubmission, identify the supporting plans and evidence the board will receive, and confirm the applicable regulatory framework. **The draft alone cannot establish compliance or operational readiness.**

References: [ISO 22301:2019](https://www.iso.org/standard/75106.html), particularly clauses 8.2–8.6 and 9.3; [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), particularly Articles 5, 6, 11 and 16.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g '*.pdf' -g '*.txt' -g '*.docx'"`
- command_execution: `/bin/bash -lc 'nl -ba bc-policy-draft.md'`
