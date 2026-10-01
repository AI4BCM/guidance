# /check-against-standards case 6b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `43276ef8-3cfd-47ad-b9d4-9c077b300151`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I reviewed the draft against DORA (Regulation (EU) 2022/2554), mainly Articles 5, 6, 11 and 12, and the RTS on the ICT risk management framework (Delegated Regulation (EU) 2024/1774, Articles 24–26). Short answer: the draft is a reasonable outline, but it falls short of DORA in almost every section. Several things DORA requires are missing altogether.

## Check this first: which DORA regime applies to you?

The draft calls the company a "small payment institution". If you are a payment institution **exempted under PSD2 Art. 32(1)**, DORA Art. 16 applies to you. That is a lighter regime, and its RTS rules are lighter too. If you are not exempted, the full rules in Arts. 5–15 apply. My review assumes the full regime. Most of the gaps below would still apply under Art. 16, though some deadlines and the level of detail would be lower. Confirm this with compliance before you redraft.

## What the current sections say, and the gaps

| § | Draft says | DORA expects | Gap |
|---|---|---|---|
| Status / 3 Roles | COO owns it; "draft for the management board" | **The management body approves, oversees and regularly reviews** the ICT business continuity policy and the response and recovery plans (Art. 5(2)(e)). It also funds them (Art. 5(2)(g)) | The board has no stated role. Add board approval and oversight, and a duty to provide resources |
| 2 Scope | Payment services, card platform, support, offices; marketing site out | Scope is built around **critical or important functions** and covers third-party ICT dependencies. Limits and exclusions are documented with reasons (RTS Art. 24) | Critical or important functions are never identified. ICT third-party providers are not mentioned. The marketing-site exclusion gives no reason (check it isn't your crisis status page) |
| 3 Roles | COO, BCM officer, IT manager | Independent ICT risk control function (Art. 6(4)), **crisis management function** (Art. 11(8)), internal audit review of recovery plans (Art. 11(3)), escalation routes | No crisis management function, no internal audit, no escalation. The IT manager sets RTOs and also owns recovery, so nobody checks that work independently |
| 4 BIA | Every 3 years; covers payment services and support desk | BIA of *severe* disruptions using quantitative and qualitative criteria and scenario analysis. It covers support processes, **third-party dependencies, information assets and interdependencies**, and drives redundancy design (Art. 11(5)) | Too narrow and too infrequent. A 3-year cycle is out of step with the annual asset and function mapping review in Art. 8. Update it at least yearly and after major changes |
| 5 Testing | Every **2 years**, **desktop walk-through only** | **At least yearly**, and also after substantive changes to systems supporting critical or important functions (Art. 11(6)). Tests include cyber-attack scenarios, **switchover to redundant capacity**, backup restoration, recovery within RTO, ICT providers where relevant, and **crisis communication plans**. Results are reported and acted on (RTS Art. 25) | The biggest gap: wrong frequency, and the test type doesn't meet the requirement |
| 6 Recovery objectives | IT manager sets RTOs "for all systems" | **RTO and RPO for each function**, based on the BIA and on whether the function is critical or important (Art. 12; RTS Art. 24) | No RPOs. Objectives are set per system rather than per function, by IT rather than from the BIA. No approval step |
| 7 Review | Owner reviews every 3 years | ICT risk framework reviewed **at least yearly** and after major incidents, supervisory findings, tests or audits (Art. 6(5), Art. 11(7)). Board reviews regularly | Wrong frequency, no event triggers, no board review |

## What DORA requires that the draft doesn't cover at all

1. **Link to the ICT risk management framework.** Under Art. 11(1) the BC policy is part of that framework. Say so, and say how ICT continuity fits with overall business continuity.
2. **Criteria for activating and standing down** the BC plans and the response and recovery plans (RTS Art. 24).
3. **Disruption scenarios** the plans must cover (RTS Art. 26): cyber-attack, failure of premises, failure of ICT or communications, failure of a critical ICT provider, loss of key staff, insider attack, power outage, natural or environmental events, and political instability, including in a provider's jurisdiction. Plans also need fallback options for when the primary recovery route isn't available.
4. **Backup and restoration** (Art. 12). This means a backup policy (scope and frequency by criticality), restoring onto segregated systems, redundant ICT capacity, and integrity checks and reconciliation after restoring.
5. **ICT response and recovery plans** (Art. 11(3); RTS Art. 26), with containment, a first estimate of impact, and prioritised recovery actions (Art. 11(2)).
6. **Crisis communication** for staff, customers, providers and the competent authority (Arts. 11(2)(e), 11(8) and 14), tested as part of the annual exercise.
7. **Link to incident management and reporting** (Arts. 17–19). This includes classifying major incidents and notifying the competent authority.
8. **ICT third-party providers** (Arts. 11(4) and 28): BC plans for outsourced critical or important functions, provider participation in tests, and a link to exit strategies.
9. **Records kept during a disruption** must be readily accessible (Art. 11(9)).
10. **Post-incident review and lessons learned** (Art. 13), fed back into the policy.
11. **Annual cost and loss estimate** for major ICT incidents, ready for the regulator on request (Art. 11(10)).
12. **Training and communication** of the policy to staff (Art. 13(6); RTS Art. 24).

## What to fix first
1. Testing: move to an annual cycle with real switchover, restore and cyber-scenario tests.
2. Recovery objectives: set RTO and RPO for each critical or important function, based on the BIA.
3. Board approval and review, plus annual and event-driven review of the policy.
4. Expand the BIA to cover third-party dependencies, information assets and interdependencies, and identify your critical or important functions.
5. Add the missing sections: activation criteria, scenarios, backup and restoration, crisis communication, and the incident reporting link.

These references are from my knowledge of DORA and RTS 2024/1774; I didn't check them against the official text during this review. Before the draft goes to the board, have compliance or legal confirm the paragraph numbers and which regime applies to you. I can also turn this into a shareable document or draft the missing sections in `bc-policy-draft.md` if that helps.

**Tool calls (stream-json):**

- Bash: `ls -la; wc -l bc-policy-draft.md; cat bc-policy-draft.md`
