# /check-against-standards case 6b, run3: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `eb242df9-ec2f-45f9-a555-74a6318bac7d`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I reviewed the draft against DORA (Regulation (EU) 2022/2554) and its ICT risk management standard (Delegated Regulation (EU) 2024/1774, the "RTS"). The draft is a short framework: it has a purpose, a scope, roles, a business impact analysis (BIA), testing, recovery objectives and review. Most of DORA's specific requirements are either missing or set below the required level.

**One assumption first:** a payment institution with 140 staff isn't a microenterprise, so I've assumed the full framework applies (Arts. 11–12 and RTS Arts. 24–26). If you're a payment institution exempted under PSD2, the lighter regime in Art. 16 applies, and some points below get softer.

## Where the draft conflicts with DORA

| Draft | DORA requirement | Fix |
|---|---|---|
| **§5 Testing:** every two years, desktop walk-through only | **Art. 11(6):** test the continuity plans and the response and recovery plans **at least once a year**, and after major changes to systems supporting critical or important functions. Tests must include **cyber-attack scenarios** and **switchovers** to backup or redundant infrastructure. **RTS Art. 25:** results must be documented and gaps fixed. | Test every year and after major changes. Run real switchover and restore tests, not only tabletops, with a cyber scenario. Record results and track fixes. |
| **§6 Recovery objectives:** IT manager sets recovery time objectives (RTOs) "for all systems" | **Art. 12(6):** set an RTO **and a recovery point objective (RPO)** for **each function**, based on how critical it is. They should come from the BIA. | Set RTO and RPO per business function, taken from the BIA and approved by the business owners and the board. Keep the IT manager's role to delivering them. RPO is missing completely. |
| **§7 Review:** policy owner reviews it every three years | **Art. 6(5):** the ICT risk management framework, which includes this policy, is reviewed **at least once a year** and after major incidents or test findings. **Art. 5(2)(e):** the **management body approves** the policy and reviews it periodically. | Review every year and after major incidents. The management board approves the policy, not just the COO. |
| **§3 Roles:** COO, BCM officer, IT manager | **Art. 5:** the management body is ultimately responsible. **Art. 6(4):** an independent ICT risk control function. **Art. 11(3):** independent internal audit of the recovery plans. **Art. 11(7):** a crisis management function. | Add the board's role, the independent risk function, internal audit and a named crisis management team with escalation routes. |
| **§4 BIA:** every three years, covering payment services and support | **Art. 11(5):** the BIA must look at severe disruption scenarios, using both quantitative and qualitative criteria. It must cover **third-party dependencies, information assets and how they depend on each other**. | Expand what the BIA covers. Three years isn't strictly a breach, but **Art. 8** requires the critical-function and asset inventory to be reviewed every year. The BIA should follow that annual cycle and any major change. |

## Missing entirely

1. **Critical or important functions (Art. 8).** The draft never identifies them, yet most of DORA's continuity duties hang off them.
2. **ICT continuity policy as part of overall business continuity (Art. 11(1)–(2)).** It should say how ICT continuity fits into the wider continuity policy.
3. **RTS Art. 24 policy contents:**
   - Objectives
   - Time frame covered
   - **When to activate and stand down the plans**
   - Escalation routes
   - Enough resources
   - Plans kept documented and **reachable during an emergency**
4. **Third-party ICT providers (Art. 11(4), Art. 28; RTS Art. 26).** The policy should cover:
   - Continuity of outsourced critical functions, such as the card processing platform if it's outsourced
   - Provider failure as a scenario
   - Involving providers in tests
   - Exit plans
5. **Backup and restore (Art. 12).** There's no backup policy, no restore testing, no requirement to keep backups separate from production, and no redundant capacity.
6. **Crisis communication (Art. 11(2)(e), Art. 14).** There are no plans for telling customers, counterparties, the public or staff, and no named spokespeople.
7. **Records (Art. 11(8)).** Records of what was done before and during a disruption must be kept and easy to reach.
8. **Lessons learned and training (Art. 13).** The policy should require:
   - Reviews after an incident and after a test
   - Feeding the lessons back into the plans
   - Resilience training for staff **and the board**
9. **Links to other processes.** These should be cross-referenced:
   - Incident management and major-incident reporting (Arts. 17–19)
   - The resilience testing programme (Art. 24)
   - The yearly cost and loss estimate for major ICT incidents, which you must give the regulator on request (Art. 11(10))

## Smaller points

- **§2 Scope:** leaving out the marketing website is fine, and the RTS expects exclusions to be written down. Say why it's excluded, for example because it supports no critical function. Also name the third-party providers and data centres that are in scope.
- **Header:** "Owner: COO" is fine, but add an approval line for the management board and a version history.

**Priorities:** fix testing, the per-function RTO/RPO and the board approval with annual review first. A regulator would flag those straight away. Then add the third-party, backup and crisis communication sections.

The article numbers come from my knowledge of DORA and the RTS; I didn't check them against the live texts here. Your compliance team should confirm the RTS article numbers in particular before you rely on them in a gap analysis.

If you'd like this as a shareable document for the team or the board, I can put it in a doc.

**Tool calls (stream-json):**

- Bash: `ls -la; cat bc-policy-draft.md`
