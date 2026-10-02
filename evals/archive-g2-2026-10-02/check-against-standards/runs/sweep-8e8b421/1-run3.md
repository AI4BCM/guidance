# /check-against-standards case 1, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `28c6bb12-fe63-4ec4-9975-890379a954f9`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one answer from you.

**What class of data is in the draft, and is this environment approved for it?**

The AI4BCM data rules say these classes may only go into an approved corporate or private environment:

- BIA data and risk assessment detail
- incident records and live crisis information
- personal data, contact lists and personnel records
- vulnerabilities and control weaknesses
- recovery strategies and design assumptions
- supplier weaknesses and contractual dependencies
- security-related architecture or site detail
- board papers and executive-session material
- audit findings not yet cleared by the audit owner

The draft is going to the board, so it may count as a board paper. Please tell me:

1. Which of these classes, if any, it contains. "None, it's a general policy text" is a fine answer.
2. If it contains any of them, whether this Claude Code session is an environment your organisation has approved for that class.

If the draft contains passwords, keys or access tokens, remove them first. They don't go into any tool.

I'll read the file once you answer. If a high-sensitivity class is present and this environment isn't approved for it, I'll stop there.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read the draft: **Business continuity policy, version 0.4, 3 September 2026**, a draft for the management board, owned by the Chief Operating Officer. It has seven sections: purpose, scope, roles, BIA, testing, recovery objectives and review. It's a policy, so I'll check it against the frameworks you choose.

**Who reviews the output:** the policy owner (the COO) answers each gap question. Legal or compliance answer the questions I mark as regulatory. If anyone states that the policy meets a framework, that's a person's call, made against the source text. I'll give you a draft in the chat and won't change or approve anything.

The draft leaves two things open:

1. **Which frameworks should I check it against?** You can pick any of these, which come with the skill:
   - AI Act (Articles 4, 26 and 50 only)
   - DORA (Regulation 2022/2554)
   - Delegated Regulation 2024/1774
   - NIST SP 800-34r1 (chapters 1 to 5)
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance
   - ESAs JC 2026-25 statement on frontier AI models

   You can also attach your own licensed copy of a standard, such as ISO 22301, if you confirm the licence allows this use. I'll cite a licensed standard by clause number only.

   Whether DORA and its delegated regulation apply to this payment institution is a question for legal or compliance. I won't assume either way.
2. **Which parts are in scope?** I can check all seven sections, or only some, for example sections 4 to 6.

Once you answer, I'll go through each framework you choose and list the gaps and contradictions as questions for the COO.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

I've read both frameworks and am writing up the findings.

---

**Sources**
- **Policy:** Business continuity policy, version 0.4, 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer. No review date or approval record.
- **DORA:** Regulation (EU) 2022/2554, OJ L 333, 27 December 2022, taken from the `dora-regulation-2022-2554.md` file that ships with the skill (retrieved 10 September 2026). The text on EUR-Lex is authoritative.
- **NIST SP 800-34 Rev. 1:** May 2010, Executive Summary and Chapters 1 to 5 only, from the `sp-800-34r1-contingency-planning-body.md` file that ships with the skill (retrieved 10 September 2026). The appendices are not included.

**Who reviews this:** the COO, as policy owner, answers every question. Legal or compliance also answer the ones marked ⚖. The list below shows gaps and contradictions only. It doesn't say whether the policy meets DORA or SP 800-34, or whether it's ready for the board. A person decides that against the source text.

---

## DORA (Regulation 2022/2554)

**What I checked:** the articles that cover a business continuity policy: Arts 2, 4, 5, 6(5), 8(1), 11, 12, 13(2) and 13(6), 14, 16 and 24.

**What I didn't check:**
- Arts 7, 9 and 10 (ICT security controls)
- Chapter III incident reporting, except where Art 11 points to it
- Arts 25 to 27 (testing of ICT tools and threat-led penetration testing)
- Chapter V third-party risk, except Art 5(3) and Art 11(4)
- Chapters VI to IX

**D1. Which regime applies** ⚖
- **Policy:** the policy doesn't say whether DORA applies or under which regime. The draft describes the company as "a small payment institution with 140 staff".
- **DORA:** Art 2(1)(b) brings payment institutions into scope. Art 16(1) sets a simplified framework instead of Arts 5 to 15 for "payment institutions exempted pursuant to Directive (EU) 2015/2366". Under Art 3(60), a microenterprise has fewer than 10 staff, so several "other than microenterprises" duties may apply.
- **Question for the COO:** Is the institution exempted under Directive 2015/2366, and so under Art 16 rather than Arts 5 to 15? Should the policy say which regime it follows?

**D2. Role of the management body** ⚖
- **Policy:** §3 says "The Chief Operating Officer owns this policy." §7 says "The policy owner reviews this policy every three years."
- **DORA:** Art 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- **Question for the COO:** The policy gives the management body no role in approving, overseeing or reviewing it. Should it?

**D3. Is this also the ICT business continuity policy?** ⚖
- **Policy:** §2 brings "The ICT systems that support them" into scope.
- **DORA:** Art 11(1) requires "a comprehensive ICT business continuity policy, which may be adopted as a dedicated specific policy, forming an integral part of the overall business continuity policy".
- **Question for the COO:** Is this document also the ICT business continuity policy, or is there a separate one it should name?

**D4. The aims set out in Art 11(2)** ⚖
- **Policy:** §1 says the policy "sets out how the company keeps its payment services running through a disruption and recovers them afterwards".
- **DORA:** Art 11(2)(a) is about continuity of "critical or important functions". Nothing in the policy matches the rest of Art 11(2):
  - (b) responding to ICT-related incidents
  - (c) activating containment plans "without delay"
  - (d) estimating "preliminary impacts, damages and losses"
  - (e) communication and crisis management, and reporting under Art 19
- **Question for the COO:** Should the policy name the critical or important functions, or say how they are identified, and cover points (b) to (e)?

**D5. BIA content and frequency** ⚖
- **Policy:** §4 says a BIA is carried out "every three years, covering each payment service and the customer support desk".
- **DORA:**
  - Art 11(5) requires a BIA "of their exposures to severe business disruptions". It must use "quantitative and qualitative criteria, using internal and external data and scenario analysis". It must cover "business functions, support processes, third-party dependencies and information assets, and their interdependencies".
  - Art 8(1) requires a review of the classification of ICT-supported business functions "as needed, and at least yearly".
- **Questions for the COO:**
  - Should §4 name what the BIA covers: third-party dependencies, information assets and scenarios?
  - How does a three-yearly BIA fit with the yearly review in Art 8(1)?

**D6. Testing: contradiction** ⚖
- **Policy:** §5 says plans are "tested every two years, by a desktop walk-through."
- **DORA:**
  - Art 11(6)(a) requires testing the plans "at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
  - For entities other than microenterprises, the testing plans must include "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
  - Art 11(6)(b) requires testing "the crisis communication plans".
  - Art 24(4) requires tests "undertaken by independent parties".
  - Art 24(6) requires appropriate tests "at least yearly" on all ICT systems supporting critical or important functions.
- **Question for the COO:** How should §5 be squared with the yearly frequency, the required scenarios, the crisis communication tests and the independence requirement?

**D7. Recovery objectives** ⚖
- **Policy:** §6 says "The IT manager sets the recovery time objectives for all systems."
- **DORA:**
  - Art 12(6) sets recovery time and recovery point objectives "for each function", taking into account "whether it is a critical or important function". They must ensure that "in extreme scenarios, the agreed service levels are met".
  - Art 5(2)(d) gives the management body responsibility for "the appropriate risk tolerance level of ICT risk".
  - Art 6(8)(b) asks for an analysis of "the impact tolerance for ICT disruptions".
- **Questions for the COO:**
  - The policy sets objectives per system, not per function, and has no recovery point objective. Should it cover both?
  - Who should set the objectives and who approves them? Should they come from the BIA?

**D8. Backup and redundancy** ⚖
- **Policy:** nothing matches.
- **DORA:** Art 12(1)(a) requires "backup policies and procedures specifying the scope of the data that is subject to the backup and the minimum frequency of the backup". Art 12(4) requires "redundant ICT capacities".
- **Question for the COO:** Should the policy cover backup and redundancy itself, or point to the document that does?

**D9. Crisis management and communication** ⚖
- **Policy:** §3 has no crisis management role and no communication role.
- **DORA:**
  - Art 11(7) requires "a crisis management function".
  - Art 14(1) requires "crisis communication plans".
  - Art 14(3) requires "At least one person ... tasked with implementing the communication strategy for ICT-related incidents and fulfil the public and media function".
- **Question for the COO:** Should §3 name these roles?

**D10. Third parties** ⚖
- **Policy:** the policy says nothing about suppliers. §2 includes "the card processing platform".
- **DORA:**
  - Art 11(4) requires ICT business continuity plans "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers".
  - Art 5(3) requires a role "to monitor the arrangements concluded with ICT third-party service providers".
- **Question for the COO:** Is any in-scope service, including the card processing platform, provided by a third party? If so, how should the policy cover it?

**D11. Audit of recovery plans and records during a disruption** ⚖
- **Policy:** §3 says "The IT manager owns the ICT recovery plans." The policy doesn't mention audit or records kept during a disruption.
- **DORA:** Art 11(3) makes ICT response and recovery plans "subject to independent internal audit reviews". Art 11(8) requires "readily accessible records of activities before and during disruption events".
- **Question for the COO:** Should the policy provide for both?

**D12. Review cycle: contradiction** ⚖
- **Policy:** §7 says "The policy owner reviews this policy every three years."
- **DORA:**
  - Art 6(5) says the ICT risk management framework is "reviewed at least once a year ... as well as upon the occurrence of major ICT-related incidents".
  - Art 11(6) asks for the ICT business continuity policy to be reviewed "regularly ... taking into account the results of tests ... and recommendations stemming from audit checks or supervisory reviews".
  - Art 13(2) requires reviews after major incidents that identify improvements "within the ICT business continuity policy".
- **Question for the COO:** If this policy is part of the ICT risk management framework, how does the three-year cycle fit these requirements? Should the policy list events that trigger a review, such as tests, audits, supervisory findings and major incidents?

**D13. Training** ⚖
- **Policy:** nothing matches.
- **DORA:** Art 13(6) requires "ICT security awareness programmes and digital operational resilience training as compulsory modules" for all employees and senior management.
- **Question for the COO:** Should the policy refer to this training?

---

## NIST SP 800-34 Rev. 1

**What I checked:** §3.1 (the policy statement) in full. I also checked §3.2 (BIA), §3.4.6 (roles), §3.5 (testing, training and exercises) and §3.6 (plan maintenance) where the policy covers the same ground.

**What I didn't check:** Chapters 4 and 5. They cover plan content and technical solutions, not the policy. Those chapters would be better held against the ICT recovery plans.

**Note:** §1.2 says the guide is written for federal information systems and "does not address ... continuity of mission/business processes". These findings only cover the ICT parts of the policy.

**N1. Key policy elements with nothing to match them**
- **Policy:** nothing in the draft matches four of the elements.
- **NIST:** §3.1 lists the key policy elements: "Roles and responsibilities; Scope as applies to common platform types and organization functions (i.e., telecommunications, legal, media relations) ...; Resource requirements; Training requirements; Exercise and testing schedules; Plan maintenance schedule; and Minimum frequency of backups and storage of backup media." The policy has:
  - nothing on resource requirements
  - nothing on training requirements
  - nothing on plan maintenance (§7 covers the policy, not the plans)
  - nothing on backup frequency or storage
- **Question for the COO:** Which of these four belong in the policy?

**N2. Scope of functions**
- **Policy:** §2 lists services, the card processing platform, customer support and the two offices.
- **NIST:** §3.1 names telecommunications, legal and media relations among the functions in scope.
- **Question for the COO:** Are those functions in scope or not?

**N3. Impact categorisation**
- **Policy:** the policy doesn't rank systems by impact.
- **NIST:** §3.1 says "The policy must reflect the FIPS 199 impact levels". §3.5.4 ties the depth of testing to those levels.
- **Question for the COO:** FIPS 199 is a US federal scheme. Does the institution have its own way of ranking systems that the policy should use instead?

**N4. Who decides acceptable downtime: contradiction**
- **Policy:** §6 says "The IT manager sets the recovery time objectives for all systems." §4 doesn't mention downtime.
- **NIST:** §3.2.1 says the coordinator, "with the process owners, leadership and business managers", should "determine the acceptable downtime". It defines maximum tolerable downtime (MTD), recovery time objective (RTO) and recovery point objective (RPO). It says "the RTO must normally be shorter than the MTD".
- **Question for the COO:** Should §6 bring in the business owners and leadership, and take MTD, RTO and RPO from the BIA in §4?

**N5. Activation authority**
- **Policy:** §3 doesn't name who can activate the plans.
- **NIST:** §3.4.6 calls for "a single authoritative role for overall decision-making responsibility, including plan activation".
- **Question for the COO:** Who activates the plans?

**N6. Type and frequency of testing**
- **Policy:** §5 says "every two years, by a desktop walk-through."
- **NIST:**
  - §3.5.4 says a tabletop exercise is "sufficient" for low-impact systems.
  - For moderate-impact systems, it calls for a functional exercise including "system recovery from backup media".
  - For high-impact systems, it calls for a full-scale exercise including "a system failover to the alternate location".
  - The sample policy statement in §3.1 reads "tested annually".
  - §3.5 asks for "an after-action report" with "Lessons Learned corrective actions".
- **Question for the COO:** Is a walk-through enough for the card processing platform? Should the policy require after-action reports?

**N7. Training frequency**
- **Policy:** nothing matches.
- **NIST:** §3.5.2 says "Training should be provided at least annually."
- **Question for the COO:** Should the policy set a training requirement?

**N8. Event-driven updates**
- **Policy:** §4 sets a fixed three-year BIA cycle. §7 sets a fixed three-year review.
- **NIST:** §3.6 says plans are reviewed "at an organization-defined frequency or whenever significant changes occur", and "When a significant change occurs, the BIA should be updated".
- **Question for the COO:** Should a significant change trigger a BIA or plan update?

**N9. Coordination with other policies**
- **Policy:** nothing matches.
- **NIST:** §3.1 says plans "should be coordinated with related organization-wide policies and programs, including information system security, physical security, human resources".
- **Question for the COO:** Should the policy name the related policies?

---

## General practice, not in the sources

- **G1.** The policy has an owner and a version, but no next review date and no record of approval. Should it have both?
- **G2.** The policy doesn't say how exceptions to it or breaches of it are handled. Should it?
- **G3.** The policy uses "business continuity plans", "ICT recovery plans" and "recovery time objectives" without defining them. Should it?

---

## Gaps

- **Your answers to my questions (your statements, not sources):**
  - The data is medium sensitivity, and this environment is approved for high.
  - The frameworks to use are DORA and NIST SP 800-34.
  - All seven sections are in scope.
- **Not checked:** AI Act Arts 4, 26 and 50; Delegated Regulation 2024/1774; NIST CSF 2.0; NIST AI RMF 1.0; Swiss FONES minimum standard; UK Cabinet Office guidance; ESAs JC 2026-25.
  - Under DORA Art 15(d), regulatory technical standards "specify further the components of the ICT business continuity policy". Delegated Regulation 2024/1774 ships with this skill but wasn't selected, so those components weren't checked. Choosing it would settle that.
- **Unresolved:**
  - Whether DORA applies, and under which regime (D1), is for legal or compliance to decide. Until then, every DORA finding depends on the answer.
  - Whether the institution is a microenterprise, small or medium-sized enterprise: the policy gives staff numbers but not turnover. Not in the sources.
- **Source status:**
  - Whether SP 800-34 Rev. 1 (May 2010) has been replaced: not in the sources.
  - Both framework files are conversions. EUR-Lex and the NIST PDF are authoritative.
- **No embedded instructions:** I found no instructions aimed at an AI in the draft.

*Parts of this document were drafted with AI support (/check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

I haven't edited the draft or saved any files. Every gap marked ⚖ needs legal or compliance to answer D1 first, because D1 decides which DORA obligations apply.
