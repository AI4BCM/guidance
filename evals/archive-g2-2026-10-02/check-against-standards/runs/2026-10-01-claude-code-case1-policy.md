# check-against-standards case1-policy, Claude Code 2.1.284, 2026-10-01

Files in the run folder: bc-policy-draft.md. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

Intake answers given with the data class in turn 2. Turn 1 is also the evidence for 6(a).

## Turn 1

Session `80ac09d1-4908-4961-8617-c01c31853c09`. Request:

```text
/check-against-standards check our draft policy before it goes to the board. Attached: bc-policy-draft.md
```

Final text:

````markdown
Before I open `bc-policy-draft.md`, I need to know what class of data it holds.

**What sensitivity class does the draft fall under?** Two things matter here:

- **Board material.** If the draft is already part of a board paper or pack, it counts as high-sensitivity under the skill's data rules. It may then be read only in an approved corporate or private environment.
- **Its contents.** It's also high-sensitivity if it contains any of the following:
  - BIA or risk-assessment detail
  - recovery strategies or design assumptions
  - known control weaknesses or vulnerabilities
  - supplier dependencies
  - security architecture or site detail
  - personal or contact data

Please also confirm whether this environment is approved for that class. If it's high-sensitivity and this environment isn't approved for it, I'll stop here and won't read the file.

**Who checks the result:** the policy owner answers each gap question. Legal or compliance answer the ones I mark for them. Whether the policy meets a given framework is decided by a person reading the source text, not by this review. You'll get a draft in this chat, and I won't edit, send or approve anything.

After you answer, I'll read the draft. I'll then ask only what it doesn't already make clear: its status and date, and which frameworks to check it against. The frameworks bundled with the skill are:
- AI Act Art. 4/26/50
- DORA
- Delegated Regulation 2024/1774
- NIST SP 800-34r1
- NIST CSF 2.0
- NIST AI RMF
- Swiss FONES ICT minimum standard
- UK Cabinet Office resilience guidance
- the ESAs statement on frontier AI models

You can also use your own licensed copy of a standard, if you confirm the licence.
````

## Turn 2

Session `80ac09d1-4908-4961-8617-c01c31853c09`. Request:

```text
Data class: medium, and this environment is approved for high. Frameworks: DORA and NIST SP 800-34. Parts in scope: all of it.
```

Final text:

````markdown
From `bc-policy-draft.md` **v0.4, 3 September 2026**, status "draft for the management board", owner the Chief Operating Officer.
Compared against **DORA, Regulation (EU) 2022/2554** as adopted (OJ L 333, 27 Dec 2022; the skill's copy was retrieved 10 Sep 2026) and **NIST SP 800-34 Rev. 1**, May 2010, chapters 1 to 5 only (retrieved 10 Sep 2026).

# Gap review: BC policy v0.4 against DORA and NIST SP 800-34

I found **28 gaps or contradictions: 18 against DORA and 10 against NIST SP 800-34**. Four are contradictions, where the policy says something different from the framework text. **D1 is the one to settle before anything else.** Each point below is a question for you as policy owner. Points marked ⚖️ are also for legal or compliance. Whether the policy satisfies either framework is for a person to decide from the source text; this review doesn't decide it. The review only asks questions; nothing has been edited, sent or recorded anywhere.

## DORA: every point here is ⚖️ for legal or compliance

The policy describes the organisation as "a small payment institution with 140 staff". Payment institutions are in scope under Art. 2(1)(b). With 140 staff it isn't a microenterprise under Art. 3(60), which covers firms that employ "fewer than 10 persons". So the obligations DORA lifts from microenterprises would apply to it.

**Which rules apply**
- **D1.** Art. 16(1) says "Articles 5 to 15 of this Regulation shall not apply to … payment institutions exempted pursuant to Directive (EU) 2015/2366". Those exempted institutions get a simplified framework instead. The policy doesn't say whether the institution is exempted. **Is it, and so does the full regime (Arts 5 to 15) or the simplified one (Art. 16) apply?** Every finding below assumes the full regime. The policy also doesn't state the proportionality basis that Art. 4 provides for.
- **D2.** Art. 11(1) requires an ICT business continuity policy "forming an integral part of the overall business continuity policy". **Is this document meant to be that ICT business continuity policy, or does a separate one exist?** If it's this one, then D3 to D18 are gaps in this document.

**Contradictions**
- **D3. Testing (§5).**
  - The policy says plans "are tested every two years, by a desktop walk-through."
  - Art. 11(6)(a) requires testing of the ICT business continuity and response and recovery plans "at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
  - For entities that aren't microenterprises, Art. 11(6) also requires the testing plans to include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
  - Art. 24(6) requires appropriate tests "at least yearly" on all ICT systems supporting critical or important functions.
  - **Which testing frequency and method should §5 state? Can a desktop walk-through alone cover switchover testing?**
- **D4. Review (§7).**
  - The policy says the owner "reviews this policy every three years."
  - If the policy is part of the ICT risk management framework, Art. 6(5) applies: "reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents".
  - Art. 11(6) also requires a regular review "taking into account the results of tests" and audit or supervisory recommendations.
  - **Should §7 set an annual review and list the events that trigger an earlier one?**
- **D5. BIA cycle (§4).**
  - The policy sets a BIA "every three years".
  - Art. 8(1) requires a review "at least yearly" of the classification of ICT-supported functions and assets. Art. 8(2) requires the risk scenarios to be reviewed "at least yearly".
  - **Is a three-year BIA cycle consistent with those yearly reviews? Should a major change trigger the BIA again, as Art. 8(3) requires a risk assessment "upon each major change"?**

**Gaps**
- **D6. Management body (§3).** Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". §3 names only the COO, the BCM officer and the IT manager. **Should §3 state the management body's role, the annual reporting to it by senior ICT staff (Art. 13(5)), and the training its members need (Art. 5(4))?**
- **D7. Recovery objectives (§6).** The policy says "The IT manager sets the recovery time objectives for all systems."
  - Art. 12(6) bases the objectives on functions: "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
  - **Should §6 set objectives per function, add recovery point objectives (the policy has none), and say who agrees them besides the IT manager?** The values themselves stay with their owners.
- **D8. Critical or important functions.** The policy never uses this concept, but Art. 11(2)(a), 11(4), 12(6), 24(6) and 28(8) all depend on it. **Which payment services count as critical or important functions, and should the policy say how they're identified?**
- **D9. What the BIA covers (§4).** The policy's BIA covers "each payment service and the customer support desk".
  - Art. 11(5) requires the BIA to consider "the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies".
  - Art. 11(5) also requires "quantitative and qualitative criteria … and scenario analysis". The policy's BIA scope leaves out the card processing platform and the two offices that §2 puts in scope.
  - **Should §4 match the scope in §2 and the Art. 11(5) elements?**
- **D10. The marketing website left out of scope (§2).** Art. 8(1) requires the institution to identify and document "all ICT supported business functions". Art. 11(6)(a) requires testing of plans covering "ICT systems supporting all functions". **Is excluding the marketing website consistent with those two provisions?**
- **D11. Third parties.** The policy doesn't mention them.
  - Art. 11(4) requires business continuity plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
  - Art. 28(8) adds: "For ICT services supporting critical or important functions, financial entities shall put in place exit strategies." It also requires those exit plans to be tested.
  - Art. 8(5) requires mapping of processes that depend on third-party providers.
  - **Is the card processing platform, or any other in-scope service, provided by a third party? Where are exit plans and the Art. 28 to 30 obligations held?**
- **D12. Crisis management and communication.** The policy doesn't mention either.
  - Art. 11(7) requires entities that aren't microenterprises to "have a crisis management function".
  - Art. 14(3) requires "At least one person in the financial entity shall be tasked with implementing the communication strategy for ICT-related incidents".
  - Art. 11(6)(b) requires testing of "the crisis communication plans established in accordance with Article 14."
  - **Where are these assigned, and should the policy name them?**
- **D13. Incident management and reporting.** The policy doesn't mention it. Arts 17 to 19 require an incident management process, classification of incidents, and reporting of major incidents. Art. 23 says "The requirements laid down in this Chapter shall also apply to operational or security payment-related incidents" for payment institutions. **Does another policy cover this, and should this one point to it?**
- **D14. Backup and redundancy.** The policy doesn't mention them.
  - Art. 12(1)(a) requires "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup".
  - Art. 12(3) requires restores to run on segregated systems.
  - Art. 12(4) says entities that aren't microenterprises "shall maintain redundant ICT capacities".
  - Art. 12(7) requires integrity checks after recovery.
  - **Where are these set?**
- **D15. Independent audit.** Art. 11(3) says ICT response and recovery plans "shall be subject to independent internal audit reviews". Art. 6(6) and 6(7) require internal audit of the framework and follow-up of the findings. **Should the policy provide for this?**
- **D16. Testing programme and independence.** Art. 24 requires a testing programme. It also requires "tests are undertaken by independent parties, whether internal or external" (Art. 24(4)) and remediation of findings (Art. 24(5)). Advanced threat-led penetration testing (TLPT) under Art. 26 applies only if the competent authority has identified the institution. **Has it? Who carries out the §5 tests?**
- **D17. Learning, records and training.** Three requirements have no counterpart:
  - post-incident reviews (Art. 13(2))
  - "readily accessible records of activities before and during disruption events" (Art. 11(8))
  - ICT security and resilience training "as compulsory modules in their staff training schemes" (Art. 13(6))

  **Should the policy cover these, or point to where they're covered?**
- **D18. Strategy and tolerance.** Art. 6(8)(b) requires "establishing the risk tolerance level for ICT risk, in accordance with the risk appetite of the financial entity, and analysing the impact tolerance for ICT disruptions". **Where is impact tolerance set, and should this policy refer to it?** Arts 7, 9 and 10 (ICT systems, protection, detection) usually sit in an information security policy. **Is that where they are held?**

The rest of DORA has no policy counterpart to expect:
- Arts 15, 18(3), 20 to 22, 31 to 44, 46 to 64 are addressed to authorities, the ESAs or the Commission, or they amend other regulations.
- Art. 45, cyber-threat information sharing, is voluntary.

⚖️ Legal or compliance should confirm that none of these binds the institution directly.

## NIST SP 800-34 Rev. 1 (guidance, so no legal mark)

NIST SP 800-34 covers ICT contingency planning only. §1.2 says it doesn't address "continuity of mission/business processes", so it bears on §2's ICT systems and §6, not on the policy as a whole. It was also written for US federal systems.

**Contradictions**
- **N1. Testing and review frequency (§5, §7).**
  - The guide's sample policy statement says the plan "must be reviewed annually and updated as necessary" and "shall be tested annually to identify weaknesses of the capability" (§3.1).
  - The policy says every two years for testing and every three for review.
  - **Is the difference intended?**
- **N2. Kind of exercise (§5).**
  - §3.5.4 matches exercise depth to how much availability matters: "For low-impact systems, a tabletop exercise at an organization-defined frequency is sufficient." For moderate-impact systems, "a functional exercise … should be conducted", including recovery from backup media. For high-impact systems, the exercise "should include a system failover to the alternate location".
  - **Does the institution rate its systems by impact? Is a desktop walk-through enough for the card processing platform?**

**Gaps against the key policy elements in §3.1**
- **N3.** The policy has no "Resource requirements", no "Training requirements", no "Plan maintenance schedule" and no "Minimum frequency of backups and storage of backup media". **Should it add them?** Only the policy's own review cycle is set (§7). §3.5.2 also says "Training should be provided at least annually."
- **N4.** §3.1 says "senior management, most likely the CIO, must support a contingency program". **Should the policy name the senior ICT sponsor?** It names the IT manager only as owner of the ICT recovery plans.
- **N5.** §3.1 says plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources". **Which related policies should this one refer to?**

**Other gaps**
- **N6. Downtime and objectives (§6).**
  - §3.2.1 has the acceptable downtime set "with the process owners, leadership and business managers". It also says "the RTO must normally be shorter than the MTD".
  - The policy sets RTOs by the IT manager alone, with no maximum tolerable downtime (MTD) and no RPO.
  - **Who sets the maximum tolerable downtime, and how are RTOs tied to it and to the BIA?**
- **N7. Activation authority.** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation". It adds that "Team leaders should have a designated alternate". **Who activates the plans, and who stands in for them?**
- **N8. Preventive controls and strategies.** The policy says nothing about preventive controls, alternate sites, or the use of the second office (§3.3 to §3.4). **Should it set the expectation or point elsewhere?**
- **N9. After tests and changes.** The guide expects three things the policy doesn't mention:
  - results "documented in an after-action report" (§3.5)
  - updating the BIA "When a significant change occurs" (§3.6)
  - controlled distribution of the plans and a record of changes (§3.6)

  **Should the policy require these?**
- **N10. Plan structure.** Chapter 4 sets activation and notification, recovery, and reconstitution phases for a plan. **Should the policy require ICT recovery plans to follow a set structure?** Chapter 5 is technical, plan-level detail with no policy counterpart to expect.

## Other points, not from either framework
- The AI4BCM guidance asks for every BCMS document to carry a **review date**. The policy gives a cycle but no next review date. **Should one be added?**
- §3 says the IT manager owns the ICT recovery plans, but nothing says who approves them. **Who does?**

## What this review couldn't settle
- **Your answers** (your own statements, not sources): the data class is medium and this environment is approved for high; the frameworks selected are DORA and NIST SP 800-34; the whole policy is in scope.
- **Status of sources:**
  - The policy is a **draft** (v0.4, 3 Sep 2026), so I reviewed it as a draft and not as current policy.
  - The skill's DORA copy is the text **as adopted**. Any later amendments aren't reflected; legal should check the consolidated version on EUR-Lex.
  - The NIST copy leaves out the appendices, including the sample policy and plan templates, so I didn't review against those.
- **Not reviewed:**
  - **Delegated Regulation 2024/1774.** It sets out further detail for the Art. 11 policy and plans and for the Art. 16 simplified regime. Legal may want it added before the board meeting.
  - The AI Act articles, NIST CSF 2.0, NIST AI RMF, the Swiss FONES standard, the UK Cabinet Office guidance and the ESAs statement.
- **Facts the review needs and the policy doesn't give:**
  - whether the institution is exempted (D1)
  - whether it has been identified for TLPT (D16)
  - which functions are critical or important (D8)
  - which services are outsourced (D11)
  - where incident, information security and third-party policies sit (D13, D18)

If this review goes into the board pack, add this line and fill in the blanks:

> Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
````
