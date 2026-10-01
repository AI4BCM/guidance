# check-against-standards case6b-no-name, Claude Code 2.1.284, 2026-10-01

Files in the run folder: bc-policy-draft.md. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

stream-json; (a) is evidenced by case 1 turn 1.

## Turn 1

Session `ee463f2b-c38d-48cc-bec3-26ac1d5e6a5c`. Request:

```text
Can you review our draft business continuity policy against DORA and tell us what is missing? Attached: bc-policy-draft.md
```

Tool calls: `Glob {"pattern": "**/bc-policy-draft*"}`; `Read {"file_path": "/tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/check-against-s`; `Bash {"command": "ls -la /tmp/claude-1001/-opt-brain--claude-worktrees-ai4bcm-guidance-skills-c6b26c/8008e2c9-d7ce-4ba9-8116-b067d4fb8e32/scratchpad/evals/check-agai`

Final text:

````markdown
I've reviewed the draft against DORA (Regulation (EU) 2022/2554) and the RTS on the ICT risk management framework (Delegated Regulation (EU) 2024/1774). The draft covers the right topics, but it is a skeleton. Four of its seven sections set a frequency or an owner that contradicts DORA, and most of what DORA requires in a business continuity policy isn't there at all.

**One assumption to confirm first.** I've reviewed against the full DORA regime. If you are a payment institution exempted under PSD2 Art. 32, Art. 16 of DORA (the simplified ICT risk management framework) applies instead and some requirements below are lighter. With 140 staff and your own card processing platform, the full regime seems more likely. The "small payment institution" wording in the draft makes this ambiguous, so the policy should say which regime applies.

## Where the draft contradicts DORA

| Draft | DORA requirement | Fix |
|---|---|---|
| §3, §7: the COO owns and reviews the policy | The management body approves, oversees and periodically reviews the ICT business continuity policy and the response and recovery plans, and is ultimately responsible (Art. 5(2)) | The board approves it; the COO owns it day to day |
| §7: policy reviewed every 3 years | The ICT risk management framework is reviewed at least yearly, and after major ICT incidents, supervisory instructions, or test or audit findings (Art. 6(5)). Plans are also reviewed in light of test and audit results (Art. 11(6)) | Review yearly plus those triggers |
| §4: business impact analysis (BIA) every 3 years, covering payment services and support only | The BIA must cover business functions, support processes, third-party dependencies, information assets and how they depend on each other. It must use quantitative and qualitative criteria and scenario analysis (Art. 11(5)). ICT assets must be designed in line with it, including redundancy for critical components | Widen the scope. Tie the BIA to the yearly review cycle and to major changes |
| §5: tests every 2 years, desktop walk-through only | Test the ICT business continuity plans and ICT response and recovery plans **at least yearly** and after substantive changes to systems that support critical or important functions. Tests must include cyber-attack scenarios and switchover to redundant capacity and backups (Art. 11(6)). Systems that support critical or important functions are tested yearly (Art. 24(6)) | Testing every year, including technical failover and restore tests, not only desktop walk-throughs |
| §6: the IT manager sets recovery time objectives (RTOs) for all systems | RTOs **and recovery point objectives (RPOs)** are set **per function**, based on whether the function is critical or important and on its wider impact (Art. 12(6)) | Set them per function from the BIA, have the business owner agree them, and include RPOs |

## What is missing entirely

1. **Critical or important functions.** The draft never identifies them, but most DORA obligations depend on them. Add how they are identified and mapped to ICT assets and third parties (Art. 8).
2. **ICT third-party providers.** Business continuity plans must cover critical functions that are outsourced (Art. 11(4)). You also need exit strategies for ICT services that support critical functions (Art. 28(8)). For a card processing platform this is probably your biggest exposure.
3. **Backup and restoration.** The draft has nothing on backup policy, restore procedures, restoring onto segregated systems, or redundant ICT capacity (Art. 12).
4. **Crisis management and communication.**
   - You need a crisis management function with procedures for internal and external communication (Art. 11(7)).
   - You need crisis communication plans with a named spokesperson (Art. 14), and these must be tested too (Art. 11(6)(b)).
5. **Link to incident management and reporting.** The plans must connect to incident handling (Art. 17) and to reporting major incidents to your regulator (Arts. 11(2)(e) and 19).
6. **ICT response and recovery plans.** The draft names them but doesn't describe them. They need independent internal audit review (Art. 11(3)). They must also cover a defined set of scenarios (RTS Art. 26):
   - cyber-attack
   - failure of a third-party provider
   - loss of premises or a data centre
   - loss of key staff
   - power or telecoms failure
   - pandemic
   - natural disaster and climate-related events
7. **Content the RTS requires in the policy itself (RTS Art. 24).** The draft is missing:
   - objectives, and how ICT continuity fits with overall business continuity
   - how long the policy covers
   - criteria for activating and stopping each plan
   - escalation paths and resources
   - how plans are prioritised by risk
   - reasons for scope exclusions (for example, why the marketing website is out of scope)
8. **Governance and independence.** The policy should say:
   - ICT risk is overseen by an independent control function (Art. 6(4))
   - internal audit regularly audits the framework (Art. 6(6))
   - the board receives test results and gaps found
9. **Records and learning.**
   - Keep records of what happened before and during a disruption (Art. 11(8)).
   - Review what went wrong after major incidents and put test lessons back into the plans (Art. 13).
   - Give staff and the board mandatory resilience training (Arts. 5(4) and 13(6)).
   - Report your estimated annual costs and losses from major incidents when the regulator asks (Art. 11(10)).
10. **Structure.** Say whether the ICT business continuity policy is part of this policy or a separate document under it (Art. 11(1)). Either is allowed, but it has to be stated.

**Beyond DORA:** the EBA Guidelines on outsourcing still apply to business continuity for outsourced functions. Physical and people continuity (both offices, staff) is only partly covered by DORA, so you may want to test the policy against ISO 22301 as well.

**Suggested priority before the board sees it:**
1. Board approval and yearly review.
2. Critical or important functions, plus RTOs and RPOs set per function.
3. Yearly testing that includes failover and cyber-attack scenarios.
4. Third-party continuity and exit strategies.
5. Backups.
6. Crisis communication and the link to incident reporting.

The article references are from my knowledge of the texts, so check them against the official versions before the policy goes to the board. This review isn't legal advice. I can turn it into a shareable gap-analysis page or doc, or redraft the policy with these sections added, if that's useful.
````
