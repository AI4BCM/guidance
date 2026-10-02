# check-against-standards case1-policy, final round (f05ad10), Claude Code 2.1.284, 2026-10-01

Files in the run folder: bc-policy-draft.md. Guidance repo at f05ad10. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`.

Turn 2 answers the data class alone; the intake answers (frameworks, scope) are given in turn 3, after the skill asked for them.

## Turn 1

Session `44e06287-0ddc-45f9-b6e7-16403546f28c`. Request:

```text
/check-against-standards check our draft policy before it goes to the board. Attached: bc-policy-draft.md
```

Final text:

`````markdown
Before I open `bc-policy-draft.md`, one question:

**What class of data does the draft hold, and is this environment approved for it?**

A policy that's going to the board can count as **board papers**, which our data rules treat as high sensitivity. It's even more sensitive if it includes any of the following:

- BIA data or risk assessment detail
- recovery strategies or design assumptions
- vulnerabilities or control weaknesses
- supplier weaknesses or contractual dependencies
- security-related architecture or site detail
- personal data, contact lists or personnel records
- audit findings not yet cleared by the audit owner

High-sensitivity material should only be processed in an approved corporate or private environment. Please tell me:

1. which of these classes, if any, the draft contains, and
2. whether this Claude Code environment is approved for that class.

If it isn't approved, I'll stop here, and you can run the check in an environment that is. Once you confirm, I'll read the draft and ask only what it leaves open: its status and date, which of the bundled frameworks to check it against (for example DORA, NIST CSF 2.0, or the Swiss FONES ICT minimum standard), and which parts are in scope.

To set expectations: you'll get a draft list of gaps in the chat, each written as a question for the policy owner. Points that touch a regulation will be marked for legal or compliance review. I won't say whether the policy complies or is ready for the board; the policy owner and legal or compliance make that call against the source texts.
`````

## Turn 2

Session `44e06287-0ddc-45f9-b6e7-16403546f28c`. Request:

```text
Data class: medium, and this environment is approved for high.
```

Final text:

`````markdown
I've read `bc-policy-draft.md` (v0.4, 3 September 2026, draft for the management board, owned by the COO). Two things are still open:

**1. Which frameworks should I check it against?** These ship with the skill:

- **DORA** (Regulation 2022/2554)
- **Delegated Regulation 2024/1774**, the ICT risk management framework under DORA
- **NIST SP 800-34r1**, chapters 1 to 5 (contingency planning)
- **NIST CSF 2.0**
- **Swiss FONES ICT minimum standard 2023**
- **UK Cabinet Office organisational resilience guidance**
- **AI Act**, Articles 4, 26 and 50 only
- **NIST AI RMF 1.0**
- **ESAs JC 2026-25** statement on frontier AI models

The draft describes the organisation as a payment institution, so DORA and 2024/1774 may be relevant. Whether they apply is for you and legal or compliance to confirm. I won't pick frameworks for you.

If you also want it checked against a licensed standard such as ISO 22301, attach your own copy and confirm that its licence allows this use. I'll cite that standard by clause number only.

**2. Which parts are in scope?** Should I check all seven sections, or only some (for example sections 4 to 7)?

When the review is done, the COO as policy owner answers each question it raises. Legal or compliance answers the points marked as regulatory. Whether the policy meets a framework or is ready for the board is a person's call against the source text, not mine.
`````

## Turn 3

Session `44e06287-0ddc-45f9-b6e7-16403546f28c`. Request:

```text
1. DORA and NIST SP 800-34. 2. All of it.
```

Final text:

`````markdown
From bc-policy-draft.md, v0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer.
Compared against DORA, Regulation (EU) 2022/2554 (OJ L 333, 27 Dec 2022; bundled conversion retrieved 10 Sep 2026; the EUR-Lex text is authoritative).
Compared against NIST SP 800-34 Rev. 1, May 2010, chapters 1 to 5 only (bundled conversion retrieved 10 Sep 2026; the PDF is authoritative).

# Gap review: business continuity policy v0.4

This is a draft review for the policy owner. It is not a finding that the policy complies with either framework or is ready for the board.

**Reviewer:** the COO, as policy owner, answers each question. Legal or compliance answers every question marked ⚖️. Whether the policy meets either framework is for a person to decide against the source text.

The draft is short, so most findings below are things the draft leaves out rather than things it gets wrong. **Question 0 comes first because the answer may close many of the DORA gaps.**

> **Q0 ⚖️ (for the policy owner and legal or compliance):** Under DORA Art. 11(1), the ICT business continuity policy "may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy". Is this draft the overall business continuity policy, with a separate ICT business continuity policy and ICT risk management framework elsewhere? Or is it meant to cover both? If a separate ICT policy exists, which of the DORA gaps below does it already cover, and should this policy refer to it?

---

## Block 1: DORA (Regulation 2022/2554). Every point is ⚖️ for legal or compliance review

**Applicability first.** Art. 2(1)(b) covers "payment institutions, including payment institutions exempted pursuant to Directive (EU) 2015/2366". Art. 16(1) removes Articles 5 to 15 for "payment institutions exempted pursuant to Directive (EU) 2015/2366" and puts a simplified framework in their place. Several obligations below also apply only to entities "other than microenterprises". Art. 3(60) defines a microenterprise as one that "employs fewer than 10 persons" and also sets a turnover test. The draft says 140 staff, but the sources give no turnover figure.
**Q1 ⚖️:** Is the institution an exempted payment institution under Art. 16, or does the full Chapter II regime apply? The findings below assume the full regime. Please confirm.

| # | Policy | DORA | Gap or contradiction | Question for the policy owner |
|---|---|---|---|---|
| D1 | §3 Roles; §7 Review | Art. 5(2)(e) | **Gap.** The management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans". The draft gives the management body no role. §3 says "The Chief Operating Officer owns this policy" and §7 says "The policy owner reviews this policy every three years." | ⚖️ What role does the management board have in approving, overseeing and periodically reviewing this policy and the ICT recovery plans? Should the policy say so? |
| D2 | §7 Review | Art. 6(5); Art. 11(6), last subparagraph | **Contradiction.** The policy says "every three years". Art. 6(5) says the ICT risk management framework "shall be documented and reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents". Art. 11(6) adds that entities "shall regularly review their ICT business continuity policy … taking into account the results of tests … and recommendations stemming from audit checks or supervisory reviews". | ⚖️ Does the three-year cycle hold for the ICT parts of this policy? Should review also be triggered by major incidents, test results and audit or supervisory findings? |
| D3 | §5 Testing | Art. 11(6)(a) and second subparagraph | **Contradiction.** The policy says plans "are tested every two years, by a desktop walk-through." Art. 11(6)(a) requires testing "at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions". For non-microenterprises, test plans must include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities". | ⚖️ How should the testing frequency, the triggers and the test types (beyond a desktop walk-through) be set for ICT plans? |
| D4 | §5 Testing | Art. 24(4), 24(6) | **Gap.** Entities "shall ensure that tests are undertaken by independent parties, whether internal or external". They must also ensure, "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions". The draft does not say who tests or how independence is ensured. | ⚖️ Who carries out the tests, and how is their independence ensured? Does a digital operational resilience testing programme exist that this policy should refer to? |
| D5 | §5 Testing | Art. 11(6)(b) | **Gap.** Entities shall "test the crisis communication plans established in accordance with Article 14". The draft does not mention crisis communication plans. | ⚖️ Are crisis communication plans in scope of §5? |
| D6 | §4 BIA | Art. 11(5) | **Gap.** The BIA covers "each payment service and the customer support desk". Art. 11(5) requires it to assess "severe business disruptions by means of quantitative and qualitative criteria, using internal and external data and scenario analysis". It must "consider the criticality of identified and mapped business functions, support processes, third-party dependencies and information assets, and their interdependencies". The draft does not mention criteria, scenarios, third-party dependencies, information assets, or the card processing platform named in §2. | ⚖️ Should §4 name what the BIA must cover and on what criteria, including third-party dependencies and ICT assets? |
| D7 | §4 BIA | Art. 8(1), Art. 8(2) | **Possible gap.** DORA sets no BIA frequency (not in the sources). It does require reviewing the classification of ICT-supported business functions "at least yearly" and the risk scenarios "at least yearly". The draft's BIA cycle is "every three years". | ⚖️ How does the three-year BIA cycle relate to these yearly reviews? Is the yearly classification and scenario review done somewhere else? |
| D8 | §6 Recovery objectives | Art. 12(6) | **Gap.** The policy says "The IT manager sets the recovery time objectives for all systems." Art. 12(6) speaks of "recovery time and recovery point objectives for each function", taking into account "whether it is a critical or important function and the potential overall impact on market efficiency". The draft has no recovery point objectives, sets objectives per system rather than per function, and gives no basis for setting them. | ⚖️ Should §6 cover RPOs, set objectives per function, and state the basis? Who should set them? |
| D9 | §6; §3 | Art. 5(2)(d); Art. 6(8)(b) | **Gap.** The management body bears responsibility for "the determination of the appropriate risk tolerance level of ICT risk". The strategy must analyse "the impact tolerance for ICT disruptions". In the draft, the IT manager alone sets RTOs, with no link to a tolerance the board has set. | ⚖️ How do the RTOs in §6 tie back to a risk or impact tolerance approved by the management body? |
| D10 | §2 Scope | Art. 11(2)(a); Art. 3(22) | **Gap.** The arrangements must "ensure the continuity of the financial entity's critical or important functions". The draft scopes "All payment services, the card processing platform, customer support and the two offices", but never says which of these are critical or important functions. | ⚖️ Which functions has the organisation identified as critical or important? Should the policy name them or point to where they are recorded? |
| D11 | Not addressed | Art. 11(4); Art. 28(1) | **Gap.** ICT business continuity plans must be tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers". The draft does not mention third parties. | ⚖️ How does the policy cover continuity of outsourced or contracted ICT services, for example any external card processing? |
| D12 | Not addressed | Art. 11(2)(e); Art. 11(7); Art. 14(3) | **Gap.** The arrangements must "set out communication and crisis management actions". Non-microenterprises "shall have a crisis management function". The draft's roles (§3) include no crisis management function, and no person is named for the communication strategy under Art. 14(3). | ⚖️ Where does the crisis management function sit, and should §3 name it? |
| D13 | Not addressed | Art. 11(2)(e); Art. 19(1); Art. 23 | **Gap.** The arrangements must "report to the competent authorities in accordance with Article 19". Art. 23 extends Chapter III to "operational or security payment-related incidents" for payment institutions. The draft does not mention regulatory reporting. | ⚖️ Should the policy link to the incident reporting process, including payment-related incidents? |
| D14 | §3 ("The IT manager owns the ICT recovery plans") | Art. 11(3); Art. 6(4) | **Gap.** For non-microenterprises, ICT response and recovery plans "shall be subject to independent internal audit reviews". There must also be "appropriate segregation and independence of ICT risk management functions, control functions, and internal audit functions". The draft does not mention audit or independent oversight. | ⚖️ Who independently reviews the ICT recovery plans, and should §3 say so? |
| D15 | Not addressed | Art. 12(1), 12(3), 12(4) | **Gap.** The framework requires documented "backup policies and procedures specifying the scope of the data … and the minimum frequency of the backup", restoration on segregated systems, and "redundant ICT capacities". The draft does not cover these. | ⚖️ Are backup and redundancy covered in another policy that this one should cite? |
| D16 | Not addressed | Art. 11(8) | **Gap.** Entities "shall keep readily accessible records of activities before and during disruption events". | ⚖️ Should the policy require these records? |
| D17 | §7; not addressed | Art. 13(2), 13(3) | **Gap.** The framework requires "post ICT-related incident reviews after a major ICT-related incident". Lessons from tests and plan activations must be "duly incorporated on a continuous basis". The draft has no lessons-learned step. | ⚖️ Should the policy require post-incident reviews and feed their lessons into the plans and the policy? |
| D18 | Not addressed | Art. 13(6) | **Gap.** "ICT security awareness programmes and digital operational resilience training" are compulsory for "all employees and to senior management staff". The draft does not mention training. | ⚖️ Is BC and resilience training covered here or elsewhere? |

---

## Block 2: NIST SP 800-34 Rev. 1, chapters 1 to 5 (guidance, not regulation)

**Fit first.** Section 1.2 says the guide does not address "continuity of mission/business processes". It is written for federal information systems and works from FIPS 199 impact levels. It therefore speaks only to the ICT parts of the draft: the card processing platform and the supporting ICT systems in §2, and the ICT recovery plans in §3. It says nothing about the offices or the customer support desk as such.
**Q2:** Does the organisation categorise its systems by impact level (low, moderate or high) in a way that would let the testing and maintenance guidance below be applied? The guide ties exercise depth to that level.

| # | Policy | SP 800-34 | Gap or contradiction | Question for the policy owner |
|---|---|---|---|---|
| N1 | Whole draft | §3.1 | **Gap.** The key policy elements listed are: "Roles and responsibilities; Scope …; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media." The draft has roles (§3), scope (§2) and a testing schedule (§5). It has no resource requirements, training requirements, plan maintenance schedule, or backup frequency. | Should the policy add resources, training, plan maintenance and backup frequency, or point to where they are set? |
| N2 | §1 Purpose | §3.1 | **Gap.** The policy statement "should define the organization's overall contingency objectives". §1 states a general purpose but no objectives. | What contingency objectives should §1 state? |
| N3 | §6 Recovery objectives | §3.2.1 | **Gap.** The guide uses MTD, RTO and RPO, and says "the RTO must normally be shorter than the MTD". Acceptable downtime is determined "with the process owners, leadership and business managers". The draft names only RTOs, set by the IT manager, with no MTD or RPO and no part for process owners. | Who should determine tolerable downtime and RPOs? Should RTOs be checked against them? |
| N4 | §4 BIA | §3.2; §3.6 | **Gap.** The BIA "may need to be conducted again" as a system changes. "When a significant change occurs, the BIA should be updated with the new information". The draft sets a fixed three-year cycle with no trigger for change. | Should significant change trigger a BIA update between cycles? |
| N5 | §5 Testing | §3.5; §3.5.4 | **Possible contradiction.** The draft sets a desktop walk-through for all plans. The guide says "For low-impact systems, a tabletop exercise … is sufficient". Moderate-impact systems should have "a functional exercise" including "an element of system recovery from backup media". High-impact systems should have "a full-scale functional exercise" including "a system failover to the alternate location". Events are also expected "following organizational or system changes". | Is a desktop walk-through enough for the card processing platform at its impact level? Should system changes trigger tests? |
| N6 | §5 Testing | §3.5 | **Gap.** "For each TT&E activity conducted, results are documented in an after-action report, and Lessons Learned corrective actions are captured". The draft does not mention test results. | Should §5 require after-action reports and corrective actions? |
| N7 | Not addressed | §3.5.2 | **Gap.** "Training should be provided at least annually. Personnel newly appointed to ISCP roles should receive training shortly thereafter." | Should the policy set training for people with recovery roles? |
| N8 | §3 Roles | §3.4.6 | **Gap.** A capable strategy needs "a single authoritative role for overall decision-making responsibility, including plan activation". A senior official "has the ultimate authority to activate the plan". The draft does not say who activates the plans. | Who has authority to activate the plans, and who stands in when they are unavailable? |
| N9 | §7 Review | §3.6 | **Gap.** The plan "should be reviewed for accuracy and completeness at an organization-defined frequency or whenever significant changes occur". §7 covers only reviewing the policy, every three years. The draft says nothing about reviewing the plans. | Should the policy set a review frequency and change triggers for the BC and ICT recovery plans themselves? |

---

## Points no selected text holds ("general practice, not in the sources")

- **G1:** The draft names an owner and a version but has no approving body, approval date or next review date. Should it?
- **G2:** §2 includes "the two offices" and customer support. Neither selected source covers non-ICT disruption, such as loss of an office or staff being unavailable, as a policy matter. Should the policy say how these are handled?
- **G3:** §2 excludes the marketing website. Does the website carry any payment or customer-notification function that would argue for keeping it in scope?

## Coverage against the scope you set (all sections, DORA and SP 800-34)

| Section | DORA | SP 800-34 |
|---|---|---|
| §1 Purpose | no finding | N2 |
| §2 Scope | D10, D11 | N1 |
| §3 Roles | D1, D9, D12, D14 | N1, N8 |
| §4 BIA | D6, D7 | N4 |
| §5 Testing | D3, D4, D5 | N5, N6 |
| §6 Recovery objectives | D8, D9 | N3 |
| §7 Review | D1, D2, D17 | N9 |
| Not in the draft | D13, D15, D16, D18 | N1, N7 |

## Gaps (what the sources leave open)

- **Your statements, not sources:** the data class (medium), the frameworks chosen (DORA and NIST SP 800-34) and the scope (all sections).
- **Draft source:** the policy is itself a draft (v0.4, 3 Sep 2026). It was reviewed as the subject, not as current policy.
- **Applicability:** whether the institution is exempted under Art. 16, and its turnover for the Art. 3 size tests, are not in the sources (Q1). The answer settles which DORA findings hold.
- **Delegated detail not reviewed:** Art. 15 says the components of the ICT business continuity policy and its testing are "specif[ied] further" by regulatory technical standards. The bundled Delegated Regulation 2024/1774 was not selected, so that detail is **not reviewed**. Incident-reporting time limits (Art. 20) are not in the sources.
- **SP 800-34 limits:** the bundled file carries chapters 1 to 5 only, without the appendices, and the guide is written for federal information systems.
- **Not reviewed:** Delegated Regulation 2024/1774, NIST CSF 2.0, NIST AI RMF 1.0, the AI Act (Arts 4, 26 and 50), the Swiss FONES ICT minimum standard, the UK Cabinet Office guidance, and the ESAs JC 2026-25 statement.
- **No embedded instructions:** I found no passage in the draft addressed to an AI.

This is a draft for the policy owner. I have changed, approved or sent nothing. RTOs, RPOs and tolerances remain for their owners to set.

---

If these findings go into the board paper or the policy file, add this line:

> Parts of this document were drafted with AI support (check-against-standards skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
`````
