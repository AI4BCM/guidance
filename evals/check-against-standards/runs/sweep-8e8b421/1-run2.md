# /check-against-standards case 1, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `79eaf917-62b2-4d6f-a6fb-a05d0a37d1ea`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open `bc-policy-draft.md`, I need one answer from you. The skill's preflight requires it, and I haven't read the file yet.

**What class of data does the draft policy hold, and is this environment approved for that class?**

- **Medium:** an internal policy draft with no high-sensitivity detail.
- **High:** it includes any of the following:
  - BIA or risk assessment detail
  - personal data or contact lists
  - vulnerabilities or control weaknesses
  - recovery strategies or design assumptions
  - supplier weaknesses or contractual dependencies
  - security-related architecture or site detail
  - board papers or executive-session material
  - audit findings the audit owner hasn't cleared yet

The draft is going to the board, so if it's already part of a board pack it counts as **high**. In that case it can only be reviewed in an approved corporate or private environment. Please confirm the class and whether this environment is approved for it. If it isn't approved for that class, I'll stop here.

Once you've confirmed, I'll read the draft. I'll then only ask about what it leaves open: its status and date, which frameworks from the shipped list to check it against (or a licensed standard you hold), and which parts are in scope.

The policy owner will answer each gap question, and legal or compliance will answer the points marked for them. Whether the policy meets a framework is a person's call, made against the source text. I'll give no compliance verdict.

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

I've read `bc-policy-draft.md`. It's version 0.4, dated 3 September 2026, with status "draft for the management board", and the owner is the Chief Operating Officer. I won't ask about any of that. Before I review it, I have three questions the draft leaves open:

1. **Which frameworks should I hold it against?** The skill ships with these:
   - AI Act (Articles 4, 26 and 50 only)
   - DORA
   - Delegated Regulation 2024/1774
   - NIST SP 800-34r1 (chapters 1–5)
   - NIST CSF 2.0
   - NIST AI RMF 1.0
   - Swiss FONES ICT minimum standard 2023
   - UK Cabinet Office organisational resilience guidance
   - ESAs JC 2026-25 statement on frontier AI models

   The draft describes a payment institution, so DORA and Delegated Regulation 2024/1774 look like obvious candidates. But whether they apply to you is for you and legal or compliance to confirm, not me.
2. **Do you hold a licensed copy of a standard you want included, such as ISO 22301?** If so, please attach it and confirm the licence allows this use. I'd cite it by clause number only.
3. **Which parts are in scope?** That could be all seven sections, or only some, for example BIA, testing and recovery objectives.

If you skip a question, I'll note my assumption under Gaps. The review will treat each gap and contradiction as a question for the policy owner (the COO), and I'll mark points on a regulation for legal or compliance review.

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

**Source stamp**
- Reviewed `bc-policy-draft.md`: version 0.4, 3 September 2026, status "draft for the management board", owner Chief Operating Officer.
- Compared against DORA, Regulation (EU) 2022/2554, as adopted (OJ L 333, 27 Dec 2022). The shipped copy was converted on 2026-09-10; where it differs from EUR-Lex, EUR-Lex is authoritative.
- Compared against NIST SP 800-34 Rev. 1, May 2010, executive summary and chapters 1–5 only. The shipped copy was converted on 2026-09-10; where it differs from the PDF, the PDF is authoritative.

**Reviewer:** the policy owner (COO) answers each question below. Legal or compliance answers the ones marked **[L/C]**. These are gaps and questions, not a verdict. Whether the policy meets either framework is a person's call, made against the source text.

---

## Your answers to the intake questions

These are your statements, not sources:
- Data class: "medium"; environment "approved for high".
- Frameworks: "DORA and NIST SP 800-34".
- "2. All of it." I've taken this as the answer to the scope question, so all seven sections are in scope. **Assumption:** you skipped the licensed-standard question, so I treated it as "no licensed copy". ISO 22301 and other licensed standards are not reviewed.

---

## DORA (every point is marked [L/C])

**D1. Who approves and oversees the policy.** [L/C]
- §3 says: "The Chief Operating Officer owns this policy."
- Art. 5(2)(e) says the management body shall "approve, oversee and periodically review the implementation of the financial entity's ICT business continuity policy and ICT response and recovery plans".
- *Question for the COO:* the draft gives the board no role in approving, overseeing or reviewing the policy, or the ICT recovery plans the IT manager owns. Should it?

**D2. Where the ICT business continuity policy sits.** [L/C]
- Art. 11(1) requires a "comprehensive ICT business continuity policy". It sits within the ICT risk management framework (Art. 6(1)) and can be a dedicated policy or part of the overall business continuity policy.
- The draft doesn't say whether it is that ICT policy, contains it, or relies on a separate one.
- *Question:* which is it, and where is the link to the ICT risk management framework?

**D3. Critical or important functions.** [L/C]
- Art. 11(2)(a) and Art. 12(6) are built around "critical or important functions". §2 lists services, a platform, a desk and offices, but names no function as critical or important.
- *Question:* who identifies those functions, and where is that recorded?

**D4. What the BIA covers.** [L/C]
- §4 says: "The BCM officer carries out a business impact analysis every three years, covering each payment service and the customer support desk."
- Art. 11(5) requires the BIA to look at exposure to "severe business disruptions" using "quantitative and qualitative criteria" and "scenario analysis, as appropriate". It must consider "support processes, third-party dependencies and information assets, and their interdependencies".
- The draft names none of these.
- *Question:* will the BIA cover them? Art. 11(5) as shipped sets no BIA interval. Art. 8(1) and 8(2) require classifications and risk scenarios to be reviewed "at least yearly". Does the three-year cycle fit with that?

**D5. How often and how the plans are tested.** [L/C]
- §5 says: "Business continuity plans and ICT recovery plans are tested every two years, by a desktop walk-through."
- Art. 11(6)(a) says: "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
- For entities other than microenterprises, it also requires "scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- *Question:* how does the COO reconcile a two-year desktop walk-through with this?
- The draft also says nothing on:
  - testing the crisis communication plan (Art. 11(6)(b))
  - plans for functions run by ICT third parties (Art. 11(4))
  - testing backup and restoration procedures (Art. 12(2))

  Should it?

**D6. Recovery objectives.** [L/C]
- §6 says: "The IT manager sets the recovery time objectives for all systems."
- Art. 12(6) says: "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function and the potential overall impact on market efficiency."
- The draft has no recovery point objective, sets objectives per system rather than per function, and doesn't base them on the BIA.
- *Question:* who sets the RTO and RPO, on what basis, and who approves them? This connects to the board's job of setting risk tolerance under Art. 5(2)(d) and Art. 6(8)(b).

**D7. Backup.** [L/C]
- Art. 12(1)(a) requires backup policies that set the backup scope and "minimum frequency". Art. 12(3) requires restoration onto segregated systems. Art. 12(4) requires redundant ICT capacity for entities other than microenterprises.
- The draft says nothing on any of these.
- *Question:* are they covered in another document, and should this policy point to it?

**D8. How often the policy is reviewed.** [L/C]
- §7 says: "The policy owner reviews this policy every three years."
- Art. 6(5) says: "The ICT risk management framework shall be documented and reviewed at least once a year". It also requires a review after major ICT-related incidents and after testing or audit findings.
- Art. 11(6) requires the ICT business continuity policy to be reviewed "regularly", taking account of test results and audit or supervisory recommendations.
- *Question:* how does a three-year review with no event triggers fit with this?

**D9. Crisis management and communication.** [L/C]
- The draft has nothing on:
  - the crisis management function (Art. 11(7))
  - crisis communication plans and a named person for communication about ICT-related incidents (Art. 14(1) and 14(3))
  - reporting to authorities (Art. 11(2)(e), linking to Art. 19)
- *Question:* where are these covered?

**D10. Audit, records, lessons learned and training.** [L/C]
- The draft is silent on:
  - independent internal audit of ICT response and recovery plans (Art. 11(3), Art. 6(6))
  - records of activity during disruptions (Art. 11(8))
  - reviews after major ICT-related incidents (Art. 13(2))
  - mandatory resilience training for staff and management (Art. 13(6))
- *Question:* does the policy need to set any of these, or point to where they're set?

**D11. Which DORA regime applies.** [L/C]
- Art. 16 sets a simplified framework for "payment institutions exempted pursuant to Directive (EU) 2015/2366". Several obligations above exclude microenterprises.
- *Question for legal:* is the institution an exempted payment institution or a microenterprise? The answer changes which points above apply.

---

## NIST SP 800-34 Rev. 1 (guidance, not regulation)

**N1. Policy elements the guide lists (§3.1).**
- Section 3.1 lists: roles and responsibilities, scope, resource requirements, training requirements, exercise and testing schedules, plan maintenance schedule, and "Minimum frequency of backups and storage of backup media".
- The draft has roles (§3), scope (§2) and a testing schedule (§5). Resources, training, plan maintenance and backup are missing.
- *Question:* should the policy add them?

**N2. Who can activate the plan (§3.4.6).**
- The guide calls for "a single authoritative role for overall decision-making responsibility, including plan activation".
- *Question:* who activates the plans, and who stands in when that person is unavailable?

**N3. Recovery objectives and the BIA (§3.2, §3.2.1).**
- In the guide, the BIA produces the MTD, RTO and RPO and the recovery priorities. Acceptable downtime is determined "with the process owners, leadership and business managers".
- Against this, §6 has the IT manager setting RTOs alone, with no MTD or RPO.
- *Question:* should the business owners set these objectives through the BIA?

**N4. How much testing, how often (§3.1 sample, §3.5.4).**
- The guide says: "For low-impact systems, a tabletop exercise at an organization-defined frequency is sufficient." Moderate-impact systems call for functional exercises with recovery from backup. High-impact systems call for a full-scale exercise with failover.
- The sample policy statement says: "The plan recovery capabilities and personnel shall be tested annually".
- *Question:* has the card processing platform been rated for impact? If not, how is one desktop walk-through for all plans justified? The guide also expects after-action reports (§3.5); the draft is silent.

**N5. Training (§3.5.2).**
- The guide says: "Training should be provided at least annually." The draft is silent.
- *Question:* who is trained, and how often?

**N6. Plan maintenance and BIA updates (§3.6).**
- The guide says plans are reviewed "at an organization-defined frequency or whenever significant changes occur", and "When a significant change occurs, the BIA should be updated". The sample statement says plans "must be reviewed annually".
- §7 covers only the policy, every three years.
- *Question:* who maintains the plans, and when?

**N7. Coordination with related plans (§3.1).**
- The guide calls for coordination with security, physical security, HR and emergency-preparedness plans. The draft names none of them.
- *Question:* which related plans should the policy refer to?

---

## Within the draft (general practice, not in the sources)

These cite nothing:
- **G1. Scope and BIA don't match.** §2 includes "the card processing platform" and "the two offices". §4 has the BIA covering only "each payment service and the customer support desk". Is the gap intended?
- **G2. Marketing website.** §2 excludes it with no reason given. Should the reason be recorded?
- **G3. Document control.** The draft has no next review date, approval record or AI-support disclosure line. Should these be added before it goes to the board?

---

## Coverage

| Section | DORA | NIST 800-34 |
|---|---|---|
| §1 Purpose | D2 | N1 (overall objectives, partly covered) |
| §2 Scope | D3, D11 | N1 (counterpart), N7 |
| §3 Roles | D1, D9 | N1, N2 |
| §4 BIA | D4 | N3, N6 |
| §5 Testing | D5 | N4, N5 |
| §6 Recovery objectives | D6, D7 | N3 |
| §7 Review | D8, D10 | N6 |

## Gaps

- **Not reviewed:**
  - Delegated Regulation 2024/1774. DORA Art. 15(d)–(f) leaves the detailed parts of the ICT continuity policy to regulatory technical standards; this regulation is likely where that detail sits. It's worth selecting.
  - The AI Act articles, NIST CSF 2.0, NIST AI RMF, Swiss FONES, UK Cabinet Office guidance and ESAs JC 2026-25.
  - Any licensed standard.
- **Not held against the draft, provision by provision:**
  - DORA chapters III–IX (incident reporting, resilience testing including threat-led penetration testing, ICT third-party risk). This is unresolved: legal should say whether the policy must refer to them.
  - NIST chapters 4–5. These are plan-level detail, not policy content. Whether the policy should refer to them is the owner's call.
- **The draft itself:** version 0.4, an unapproved draft. I treated it as evidence of what's intended, not of what is in force.
- **NIST SP 800-34** is written for US federal systems around FIPS 199 impact levels. Using it as a reference is your choice; it doesn't bind you.

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

I haven't changed anything; `bc-policy-draft.md` is as you left it. Next, the COO answers the questions above, and the eleven [L/C] points (D1–D11) go to legal or compliance before the draft goes to the board. D5, D6 and D8 are the most pressing: in each, the draft's wording differs from the DORA article quoted next to it.
