# /check-against-standards case 6b, run2: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `52ccb756-40fd-4b95-b4de-c03d708c6397`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I've reviewed `bc-policy-draft.md` against DORA (Regulation (EU) 2022/2554) and its RTS on the ICT risk management framework (Delegated Regulation (EU) 2024/1774). The draft covers the basics (purpose, scope, owners, an impact analysis, testing, recovery targets, review), but it's too thin and too infrequent to meet DORA. Five of its seven sections set a rule that DORA directly contradicts, and several required parts are missing entirely. I worked from my own knowledge of the regulation and didn't pull the official text, so please check the article references before they go into the policy.

## First question: which DORA regime applies to you?

The draft calls the firm "a small payment institution". This changes the answer:
- **If you hold a PSD2 Article 32 exemption,** you fall under DORA's lighter regime (Art. 16 and Title III of the RTS). The gaps below mostly still apply, but some requirements are less strict, especially how often you must test.
- **If you're a fully authorised payment institution,** the full requirements in Articles 5–15 apply. With 140 staff you're well above the "microenterprise" threshold (fewer than 10 staff), so none of those exemptions help.

The gaps below assume the full regime.

## Where the draft contradicts DORA

| Draft says | DORA requires |
|---|---|
| §5: tested every two years, desk-based walk-through only | **At least once a year**, and again after any significant change to systems supporting critical or important functions. Tests must include **cyber-attack scenarios** and **actual switchovers** to backup infrastructure and redundant facilities (Art. 11(6); Art. 24(6) for testing of critical systems). A walk-through alone isn't enough. |
| §7: policy reviewed every three years | **At least once a year**, plus after major ICT incidents, findings from tests or audits, and supervisory instructions (Art. 6(5)). |
| §6: IT manager sets recovery time objectives (RTOs) "for all systems" | RTOs and RPOs (recovery point objectives: how much data you can afford to lose) are set **per business function**. They depend on whether the function is critical or important and on its wider impact, they come out of the impact analysis, and they're approved through governance (Art. 12(6)). The draft has no RPOs at all. |
| §4: impact analysis every three years, covering only payment services and the support desk | It must use quantitative and qualitative criteria and severe-but-plausible scenarios. It must cover information assets, ICT assets and **interdependencies, including third-party providers**. ICT design and redundancy must follow from it (Art. 11(5), Art. 8). Three years is incompatible with a framework reviewed every year. |
| §3: the COO owns the policy | The **management body** (your board) must approve the business continuity policy and the ICT response and recovery plans, review them periodically, and hold final responsibility (Art. 5(2)(e)). The policy should say so. Board members also need regular ICT risk training (Art. 5(4)). |

## What's missing entirely

1. **Critical or important functions.** The scope lists services, not functions. DORA is built around identifying and documenting these (Art. 3(22), Art. 8). Likely candidates beyond payments: safeguarding of client funds, fraud and AML monitoring, regulatory reporting.
2. **Third-party ICT providers.** Nothing on outsourced or ICT-provider dependencies, although the card processing platform probably relies on one. DORA requires:
   - business continuity plans that specifically cover functions run by third parties (Art. 11(4));
   - exit strategies (Art. 28(8));
   - contract terms covering the provider's own continuity plans and its part in your tests (Art. 30(3)(c));
   - a register of information on these arrangements (Art. 28(3)).
3. **When and how plans are triggered.** No criteria for activating the plans, no escalation path, nothing on containment or a first estimate of impact (Art. 11(2)).
4. **Crisis management function** with internal and external communication procedures (Art. 11(7)).
5. **Communication plans** for clients, counterparties and the public, with a named person responsible for incident communication (Art. 14).
6. **Backup, restoration and redundancy.** DORA requires:
   - a backup policy whose scope and frequency depend on how critical the data is;
   - backups held separately from the source systems, both physically and logically;
   - tested restore procedures;
   - redundant ICT capacity (Art. 12).
7. **ICT response and recovery plans** as defined documents that are **independently reviewed by internal audit** (Art. 11(3)). Right now §3 only names an owner.
8. **Link to incident management and reporting.** The policy should point to the process for classifying and reporting major ICT incidents to the regulator and to clients (Arts. 17–19).
9. **Records** of actions taken before and during disruptions, kept readily accessible (Art. 11(8)).
10. **Lessons learned.** Reviews after incidents, test findings feeding back into the plans, and staff awareness training (Art. 13).
11. **Cost reporting.** The ability to give the regulator, on request, an estimate of the total yearly costs and losses from major ICT incidents (Art. 11(10)).
12. **Independence and assurance.** An ICT risk control function separate from those running ICT, and regular internal audit of the framework (Art. 6(4), 6(6)).
13. **Required policy content under the RTS.** The policy should state its objectives, how ICT continuity relates to overall business continuity, its timeframe, and documented reasons for anything excluded. The marketing website exclusion needs a justification, ideally from the impact analysis. The RTS also sets more detailed rules on test scenarios and on response and recovery plans (RTS Arts. 24–26).

## Suggested order of fixes

1. Confirm which regime applies.
2. Identify your critical or important functions and redo the impact analysis to cover dependencies and third parties.
3. Set RTOs and RPOs per function from the analysis, approved by the board.
4. Move to yearly testing that includes switchover and cyber scenarios, and yearly policy review.
5. Add sections on activation and crisis management, communications, backup and redundancy, third parties, records and lessons learned.
6. Add a statement that the board approves the policy, and an internal audit review step.

I can also write up the gap analysis as a page or document for the board.

**Tool calls (stream-json):**

- Bash: `ls -la; wc -l bc-policy-draft.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-against-standards/6b/run2/work/bc-policy-draft.md`
