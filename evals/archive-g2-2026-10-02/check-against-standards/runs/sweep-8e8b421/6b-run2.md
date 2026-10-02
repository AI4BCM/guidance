# /check-against-standards case 6b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `27788bc7-cd65-4d94-a05b-9a39dcabd451`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I've reviewed the draft (v0.4) against DORA, Regulation (EU) 2022/2554, and the Commission Delegated Regulation (EU) 2024/1774, which sets out how the ICT risk management framework must work. The draft has a reasonable structure but falls well short of DORA. Four of its seven sections conflict with explicit requirements, and several required elements are missing entirely.

**One thing to confirm first:** if the company is a payment institution *exempted* under PSD2 Art. 32, it may qualify for DORA's lighter regime (Art. 16), which changes some of what follows. I've assumed it's a fully authorised payment institution with 140 staff, so the full regime applies.

## Where the draft conflicts with DORA

| Draft section | What it says | What DORA requires |
|---|---|---|
| §5 Testing | Every **two years**, **desktop walk-through only** | Plans tested **at least yearly** and after any significant change to ICT systems supporting critical or important functions (Art. 11(6)). Tests must include **cyber-attack scenarios** and **switchovers** to redundant capacity, backups and redundant facilities. Crisis communication plans must be tested too. Relevant ICT providers should take part (RTS). |
| §7 Review | Every **three years** | The ICT risk framework, which includes this policy, must be reviewed **at least yearly**. It must also be reviewed after major ICT incidents, after supervisory instructions, and after findings from testing or audit (Art. 6(5)). |
| §6 Recovery objectives | IT manager sets RTOs (recovery time objectives) alone | RTOs **and RPOs** (recovery point objectives) must be set per function. They should reflect whether a function is critical or important and its wider impact (Art. 12(6)), so they come from the business impact analysis (BIA), not IT alone. RPO isn't mentioned at all. |
| §4 BIA | Every three years, covering payment services and support | Must assess **severe business disruption** using scenarios, including severe but plausible ones (Art. 11(5)). It needs to run on the annual cycle, since the classification of functions and assets is reviewed at least yearly (Art. 8). It should also cover ICT and third-party dependencies, not just services. |
| §3 Roles | Owned by the COO | The **management body** must approve and periodically review the ICT business continuity policy and the response and recovery plans, and it carries ultimate responsibility (Art. 5(2)). The draft never says the board approves it. |

## What's missing entirely

1. **Critical or important functions.** DORA's core concept isn't defined or identified anywhere, and most other obligations depend on it (Art. 8, Art. 11).
2. **Backup, restoration and recovery.** There's no backup policy, backup scope or frequency, restoration testing, segregation of backups, or redundant ICT capacity (Art. 12).
3. **Third-party providers.** The card processing platform almost certainly relies on external providers. The policy needs continuity plans for outsourced critical functions (Art. 11(4)), provider-failure scenarios, and exit strategies (Art. 28(8)).
4. **Crisis management and communication.** No crisis management function, escalation path, or internal and external communication procedures, including to clients, the competent authority and the media (Art. 11(7), Art. 14).
5. **Activation criteria.** Nothing says when the plans are triggered or who can trigger them. The RTS expects the policy to cover activation, governance and escalation.
6. **Response and recovery plans.** These are referred to, but the policy doesn't require them to cover specific scenarios such as cyber-attack, insider threat, power loss, loss of premises, or third-party failure (RTS).
7. **Independent internal audit** of the response and recovery plans (Art. 11(3)) and of the framework (Art. 6(6)).
8. **Records during disruptions.** Records of what was done before and during a disruption must be kept readily accessible (Art. 11(8)).
9. **Lessons learned.** No post-incident reviews, and no step for feeding test results back into the plans (Art. 13).
10. **Links to incident management and reporting.** No connection to the ICT incident process and major-incident reporting (Art. 17–19), or to estimating the yearly costs and losses from major incidents when asked (Art. 11(10)).
11. **Training and awareness** on continuity for staff and the management body (Art. 5(4), Art. 13(6)).
12. **Link to the wider ICT risk framework** and to the digital operational resilience testing programme (Art. 6, Art. 24–25).

## Smaller points

- **Scope (§2):** excluding the marketing website is fine if it supports no critical function. Say so explicitly and give the reason, since the RTS expects scope limitations and exclusions to be stated.
- **Roles:** there's no deputy for the BCM officer or IT manager, and no link to the independent ICT risk control function (Art. 6(4)).

## Fixes in priority order

1. Move testing and review to a yearly cycle.
2. Get the policy approved by the board.
3. Define the critical or important functions.
4. Add backup and RTO/RPO requirements.
5. Add third-party, crisis communication and audit requirements.

I've cited the article references from memory, so check them against the official texts before the policy goes to the board. The RTS article numbers in particular may need confirming. It would also be worth getting a compliance review, since local regulators may add their own expectations.

If it would help you share this with the team or the board, I can put this gap analysis into a document.

**Tool calls (stream-json):**

- Bash: `ls -la; wc -l bc-policy-draft.md`
- Read: `/tmp/claude-1001/-opt-brain-172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-against-standards/6b/run2/work/bc-policy-draft.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-against-standards/6b/run2/work/bc-policy-draft.md`
