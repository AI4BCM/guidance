# check-against-standards baseline (no skill loaded), run1: Codex, guidance at 2f85a91

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a101d2-dd94-75f1-9c33-712655cf2712`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I’ll read the draft and check for gaps, inconsistencies, and points that need clarification before board review.

**I recommend revising this draft before asking the board to approve it.** It identifies owners, but leaves key decisions about continuity, recovery and oversight undefined.

I assessed it against ISO 22301:2019 principles and, conditionally, EU DORA requirements. The draft does not state the jurisdiction or regulatory status; “small payment institution” alone does not establish which DORA requirements apply.

| Priority | Finding | Recommended change |
|---|---|---|
| High | **Testing every two years, by desktop walkthrough only** ([§5](bc-policy-draft.md:26)) provides insufficient evidence that services can recover. Under DORA’s full framework, annual testing and testing after substantive changes are required. | Require an annual exercise programme, including practical ICT recovery, backup restoration and relevant supplier dependencies. Record results, assign corrective actions and verify completion. |
| High | **Recovery objectives are set solely by IT** ([§6](bc-policy-draft.md:30)). There are no recovery point objectives or business-approved service priorities. | Business service owners should establish recovery needs from the impact analysis, with IT validating feasibility and management approving them. Define recovery time objectives, acceptable data loss and minimum service levels. |
| High | **Board accountability is absent** ([§3](bc-policy-draft.md:16)). Operational ownership by the COO does not establish management oversight. | Specify board approval and oversight, responsibility for resources, and reporting on readiness, exercise failures and overdue corrective actions. |
| High | **The impact analysis is narrow and refreshed only every three years** ([§4](bc-policy-draft.md:21)). It does not require analysis of dependencies or impacts over time. | Include people, premises, technology, data, suppliers and payment infrastructure. Identify recovery priorities and maximum tolerable disruption. Require updates after material changes; an annual review is a sensible policy baseline. |
| High | **There are no requirements for activation, crisis management or communications.** | Require supporting plans to define activation authority, escalation, deputies, internal and external communications, regulatory reporting, recovery and return to normal operations. Detailed procedures can sit outside the policy. |
| Medium | **The scope omits explicit supplier coverage and gives no rationale for excluding the marketing website** ([§2](bc-policy-draft.md:11)). | Include third-party dependencies supporting payment services. Justify the website exclusion through dependency and impact analysis, including whether it supports customer incident communications. |
| High | **A three-year policy review cycle has no change triggers** ([§7](bc-policy-draft.md:34)). | Require annual review and review after material business changes, incidents, exercises or regulatory changes. Specify approval of material revisions. Under full DORA, the ICT risk management framework must be reviewed at least annually, subject to its microenterprise exception. |

Two distinctions matter for the board paper:

- **ISO 22301 does not prescribe a universal annual BIA or annual policy-review cycle.** It requires planned reviews and updates when relevant changes occur. Annual review is a recommendation here; the draft’s lack of change-triggered review is the clearer weakness.
- **DORA applicability needs confirmation.** Payment institutions generally fall within scope, but certain exempt payment institutions use its simplified framework. Staff count alone does not settle that question.

Suggested replacement wording for the most urgent clause:

> Business continuity and ICT response and recovery plans shall be exercised at least annually and following substantive changes affecting critical or important services. The exercise programme shall include practical recovery and restoration tests and relevant third-party dependencies. Findings shall be documented, assigned to accountable owners and tracked to verified closure.

The board pack should include the revised policy, confirmation of the applicable regulatory framework, and a remediation plan showing owners and dates for any capabilities still being implemented.

References: **ISO 22301:2019**, clauses 5.3, 8.2–8.5 and 9.3; **[DORA, Regulation (EU) 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)**, particularly Articles 2, 5, 6, 11, 12 and 16. This is a document-level gap review; supporting plans and evidence were not supplied.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g '*.md' -g '*.pdf' -g '*.txt' -g '*.docx'"`
- command_execution: `/bin/bash -lc 'cat bc-policy-draft.md'`
- command_execution: `/bin/bash -lc 'nl -ba bc-policy-draft.md'`
