# /check-against-standards case 6b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `368ff1b1-b7a2-4fbf-8b45-780e5a343e8d`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I've reviewed the draft against DORA (Regulation (EU) 2022/2554, mainly Articles 5, 6 and 11–14) and the RTS on the ICT risk management framework (Delegated Regulation (EU) 2024/1774, Articles 24–26). The draft is a sound outline, but it is a long way from what DORA expects. Of its seven sections, two conflict with DORA (testing and review frequency), and most of the required content isn't there yet.

## First, check which DORA regime applies to you

The draft calls the firm "a small payment institution". If that means it is **exempted under PSD2 Article 32**, DORA Article 16 applies: you are in scope but under the **simplified ICT risk management framework**, and Articles 5–15 don't apply. You would be assessed against RTS 2024/1774 Title III instead, which asks for less (for example, testing at regular intervals rather than strictly every year).

If you are a fully authorised payment institution, the full regime applies, and with 140 staff you are not a microenterprise. The findings below assume the full regime. Confirm this point first, because it changes several of them.

## Where the draft conflicts with DORA

| Draft | DORA requirement | Gap |
|---|---|---|
| §5: tested **every two years** | Art. 11(6)(a): ICT continuity plans and response and recovery plans tested **at least yearly**, and after substantial changes to systems supporting critical or important functions | Testing too infrequent |
| §5: **desktop walk-through only** | Art. 11(6) and RTS Art. 25: tests must include **cyber-attack scenarios** and **switchovers** from primary systems to backup or redundant capacity; crisis communication plans tested too (Art. 11(6)(b)) | Wrong kind of test |
| §7: policy reviewed **every three years** | Art. 6(5): the ICT risk management framework, which this policy is part of, is reviewed **at least yearly** and after major ICT incidents, supervisory instructions, or test and audit findings | Review too infrequent, and no event-driven reviews |
| §4: impact analysis **every three years** | Art. 11(5): impact analysis using quantitative and qualitative criteria and scenario analysis, covering mapped functions, supporting processes, **third-party dependencies, information assets and how they depend on each other**; ICT design and redundancy must follow from it | No method or coverage, and three years doesn't fit an annual review cycle |
| §6: **IT manager sets** recovery time objectives | Art. 12(6): recovery time **and recovery point** objectives set per function, based on whether it is critical or important and its wider impact. They should come out of the impact analysis and be approved, not set by one person | No recovery point objectives, and the objectives aren't tied to the impact analysis |
| §3: COO owns the policy; board is only the audience | Art. 5(2)(a) and (e): the **management body** is ultimately responsible and must **approve and periodically review** the continuity policy and the response and recovery plans | Board approval and responsibility missing |

## What's missing entirely

1. **Critical or important functions.** The policy never identifies them, yet DORA builds almost everything around them (Art. 8, Art. 11(2)(a)).
2. **ICT third-party providers.** There are no continuity arrangements for outsourced or contracted functions (Art. 11(4); see also Art. 28 on exit strategies). For a card processing platform this is probably your biggest dependency.
3. **Backup, restoration and redundancy** (Art. 12):
   - a backup policy with backups kept physically and logically separate
   - restoration procedures
   - redundant ICT capacity
   - data integrity checks and reconciliations after recovery
4. **Response and recovery plans** (Art. 11(2)(b)–(d), Art. 11(3), RTS Art. 26):
   - criteria for activating and standing down the plans
   - containment measures for each type of incident
   - an early estimate of impact and losses
   - a defined set of scenarios: cyber-attack, provider failure, power or telecoms loss, loss of a site, insider threat
5. **Crisis management and communication.** No crisis management function (Art. 11(7)), no crisis communication plan for staff, customers and other external parties (Art. 14), and no link to major-incident reporting to the authorities (Art. 11(2)(e), Art. 19).
6. **Independent audit.** The response and recovery plans must be subject to independent internal audit reviews (Art. 11(3)).
7. **Records.** Activities before and during a disruption must be recorded and kept readily accessible (Art. 11(8)). The authorities can also ask for an estimate of the annual costs and losses from major ICT incidents (Art. 11(10)).
8. **Lessons learned.** No post-incident reviews, and no step to feed test results and deficiencies back into the plans (Art. 13).
9. **Training.** Nothing on continuity awareness for staff, or ICT resilience training for the management body (Art. 5(4), Art. 13(6)).
10. **Link to the wider framework.** The policy should say it is part of the ICT risk management framework (Art. 11(1)) and refer to the incident management, ICT security and third-party risk policies. The control function's role (Art. 6(4)) and the second line of defence's role are also absent.

## Smaller points
- **Scope.** Leaving out the marketing website is probably fine, but the impact analysis should be what justifies leaving it out.
- **Roles.** Name deputies for the BCM officer and IT manager, and set out who has authority to declare a crisis.
- **Policy vs. plans.** Separate the policy (principles, approvals, how often things happen) from the plans (procedures). DORA expects both, as distinct documents.

I cited the articles from memory, not checked against the official text. Have compliance verify them, especially the simplified-regime question and the RTS article numbers, before this goes to the board.

I can put this together as a shareable doc or page for the board pack, or draft a revised policy that closes these gaps.

**Tool calls (stream-json):**

- Bash: `ls -la; wc -l bc-policy-draft.md`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-against-standards/6b/run3/work/bc-policy-draft.md`
