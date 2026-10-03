# /check-against-standards case 1, run1: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c172d77e-0d28-4c2c-9f08-9caaede2c684`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /check-against-standards Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

Before I open bc-policy-draft.md, I need one answer from you. I haven't read the file and won't until you reply.

**What class of data does the draft policy contain?** For example: public, internal, confidential, or restricted (personal data, security details, or anything under a legal or contract restriction).

Go by what's actually in the document, not by any marking on it. Once I know the class, I'll check that this environment is approved for it. If it is, I'll review the draft.

It would also help to know **which frameworks** you want it checked against, for example ISO 22301 or another standard or regulation, and which parts of each. If you have your own copy of a licensed standard, attach it and confirm the licence lets you use it this way.

The review stays here in the chat. I won't edit the file, approve anything, or record anything. Your policy owner, legal or compliance, and management make the final decisions before it goes to the board.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/preflight.md`
- Bash: `ls -la; ls /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards /home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literat`

## Turn 2

**Request:** medium, and this environment is approved for high

**Reply (verbatim):**

Medium-class data is fine here, since this environment is approved for high. I've read the draft: **Business continuity policy, version 0.4, 3 September 2026, a draft for the management board, owned by the Chief Operating Officer.**

Before I review it, I need you to answer up to three questions. Until you do, I have nothing to compare it against.

1. **Which frameworks should I check it against?** These are the texts I have:
   - **DORA**, Regulation (EU) 2022/2554, and its **Delegated Regulation (EU) 2024/1774**. The draft describes a payment institution, so these may apply. Whether they do is for legal or compliance to confirm, not me.
   - **NIST SP 800-34 Rev. 1** (chapters 1–5).
   - **NIST CSF 2.0**.
   - The **Swiss FONES ICT minimum standard** (2023).
   - The **UK Cabinet Office Organisational Resilience Guidance**.
   - **ISO 22301** only if you attach your own copy and confirm your licence allows this use. I don't have a copy of it.

2. **Which parts of each framework?** For example, the whole text, or for DORA only the ICT business continuity and testing articles.

3. **Is there a current approved policy, or other approved source,** that this draft replaces or has to stay consistent with, such as a previous version or the board's risk appetite statement? If so, please attach it with its date.

For any question you skip, I'll list it under Gaps as an assumption. I'll list every framework you don't pick as "not reviewed".

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/data-rules.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/stages/govern.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/README.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/units/keep-it-running.md`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/1/run1/work/bc-policy-draft.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep67/runs/check-against-standards/1/run1/work/bc-policy-draft.md`
- Glob: `literature/**/*.md`

## Turn 3

**Request:** 1. DORA and NIST SP 800-34. 2. All of it.

**Reply (verbatim):**

**Sources reviewed**
- **Document reviewed:** *Business continuity policy*, version 0.4, 3 September 2026. Status: draft for the management board. Owner: Chief Operating Officer. No review date is given (see Gaps).
- **DORA:** Regulation (EU) 2022/2554, as published in the Official Journal L 333 on 27 December 2022, from a copy retrieved from EUR-Lex on 2026-09-10 (`literature/eur-lex/dora-regulation-2022-2554.md`). Reuse is allowed under Decision 2011/833/EU. Every article was checked.
- **NIST SP 800-34 Rev. 1:** May 2010, retrieved 2026-09-10 (`literature/nist/sp-800-34r1-contingency-planning-body.md`). This copy holds the Executive Summary and Chapters 1–5 only; the appendices aren't included. It's a U.S. Government work. Every chapter in the copy was checked.

Every point below is a question for the policy's owner. None of it says the policy meets or fails either framework. That judgement belongs to a person working from the source text.

---

### Block 1: DORA, Regulation (EU) 2022/2554

**⚖️ DORA is a regulation, so legal or compliance should review every point in this block.** That includes whether DORA applies at all and in what form (question D0).

**D0. Applicability ⚖️.** Article 2(1)(b) brings "payment institutions" into scope. Article 16 swaps Articles 5–15 for a simpler framework for "payment institutions exempted pursuant to Directive (EU) 2015/2366". Article 3(60) defines a microenterprise as one that "employs fewer than 10 persons". The policy says nothing on which regime the company falls under.
*Question:* Is the company an exempted payment institution under Article 16? With 140 staff, does it fall outside the microenterprise relief (Article 3(60))? Questions D1–D12 assume the full regime in Articles 5–15. Whether that's right is for legal or compliance to confirm.

**Contradictions (both passages quoted)**

**D1. Testing frequency ⚖️.**
- Policy §5: "tested every two years, by a desktop walk-through."
- DORA Art. 11(6)(a): "test the ICT business continuity plans and the ICT response and recovery plans in relation to ICT systems supporting all functions at least yearly, as well as in the event of any substantive changes to ICT systems supporting critical or important functions".
- DORA Art. 24(6): "at least yearly, that appropriate tests are conducted on all ICT systems and applications supporting critical or important functions."

*Question:* How does a two-year cycle sit with these yearly requirements?

**D2. Test method ⚖️.**
- Policy §5: "by a desktop walk-through."
- DORA Art. 11(6), second subparagraph, for entities other than microenterprises: "include in the testing plans scenarios of cyber-attacks and switchovers between the primary ICT infrastructure and the redundant capacity, backups and redundant facilities".
- DORA Art. 24(4): "tests are undertaken by independent parties".

*Question:* Is the desktop walk-through meant to be the only test method? If so, how does it cover switchovers, cyber-attack scenarios and independent testers?

**D3. Who sets recovery objectives ⚖️.**
- Policy §6: "The IT manager sets the recovery time objectives for all systems."
- DORA Art. 5(2): the management body "shall define, approve, oversee and be responsible for the implementation of all arrangements related to the ICT risk management framework".
- DORA Art. 6(8)(b): "establishing the risk tolerance level for ICT risk … and analysing the impact tolerance for ICT disruptions".
- DORA Art. 12(6): "In determining the recovery time and recovery point objectives for each function, financial entities shall take into account whether it is a critical or important function…"

*Question:* Should the IT manager set RTOs alone, without the management body? And should RTOs be set per system, as the policy says, or per function, as Art. 12(6) frames them?

**D4. Review frequency ⚖️.**
- Policy §7: "The policy owner reviews this policy every three years."
- DORA Art. 6(5): the ICT risk management framework is "reviewed at least once a year … as well as upon the occurrence of major ICT-related incidents, and following supervisory instructions or conclusions derived from relevant digital operational resilience testing or audit processes".
- DORA Art. 11(6), last subparagraph: "regularly review their ICT business continuity policy … taking into account the results of tests".
- DORA Art. 5(2)(e): the management body shall "approve, oversee and periodically review" the ICT business continuity policy.

*Question:* Is a three-year review by the COO meant to cover these duties? What events, if any, should trigger an earlier review?

**Gaps (DORA text with no counterpart in the policy)**

| # | DORA passage | What the policy says | Question for the owner ⚖️ |
|---|---|---|---|
| D5 | Art. 5(2)(e): the management body shall "approve, oversee and periodically review" the ICT business continuity policy | §3 names the COO as owner; it never mentions the management body | Should the policy name the management body as the approving and overseeing body? |
| D6 | Art. 11(1): an ICT business continuity policy "forming an integral part of the overall business continuity policy" | §2 brings ICT systems into scope, but no ICT business continuity policy is named | Is this policy also the ICT business continuity policy, or does a separate one exist? |
| D7 | Art. 11(5): the BIA covers "severe business disruptions", using "quantitative and qualitative criteria", "scenario analysis", "third-party dependencies and information assets, and their interdependencies" | §4 sets a three-year BIA "covering each payment service and the customer support desk" | Should the policy set what the BIA covers, and what should trigger a new BIA between cycles? |
| D8 | Art. 11(4): plans tested "notably with regard to critical or important functions outsourced or contracted through arrangements with ICT third-party service providers"; Art. 5(3): a role to monitor ICT third-party arrangements | §2 and §3 name no third parties and no role for them | Should outsourced functions and an ICT third-party monitoring role be in the scope and roles? |
| D9 | Art. 11(7): "a crisis management function"; Art. 14: "crisis communication plans" and "at least one person … tasked with implementing the communication strategy"; Art. 11(6)(b): those plans are tested | Nothing in the policy | Should the policy name a crisis management function and a crisis communications owner? |
| D10 | Art. 12(1)–(4): backup policies, restoration procedures, segregated restore systems, "redundant ICT capacities" | Nothing in the policy | Should the policy refer to the backup and redundancy arrangements, or name where they're set? |
| D11 | Art. 11(3): response and recovery plans "subject to independent internal audit reviews"; Art. 6(6)–(7): internal audit and follow-up | Nothing in the policy | Should internal audit's role appear in the policy? |
| D12 | Art. 11(8): "readily accessible records of activities before and during disruption events"; Art. 13(2): "post ICT-related incident reviews"; Art. 13(5): yearly reporting to the management body; Art. 13(6): compulsory training | Nothing in the policy | Should the policy cover records, post-incident review, reporting to the board and training? |
| D13 | Art. 11(2)(e) and Art. 19: reporting to competent authorities; Art. 17: incident management process | Nothing in the policy | Should the policy link to incident management and regulatory reporting? |

DORA Articles 31–64 cover the oversight of critical ICT third-party providers, competent authorities, penalties and amendments to other regulations. I found no passage there that a financial entity's business continuity policy would need to match.

---

### Block 2: NIST SP 800-34 Rev. 1

NIST SP 800-34 is guidance written for U.S. federal information systems. It isn't a regulation, so nothing in this block is marked for legal or compliance review.

**Contradictions (both passages quoted)**

**N1. Testing.**
- Policy §5: "tested every two years, by a desktop walk-through."
- §3.1, sample policy statement: "The plan recovery capabilities and personnel shall be tested annually".
- §3.5.4: "For moderate-impact systems, a functional exercise … Exercise procedures should be developed to include an element of system recovery from backup media." For low-impact systems only: "a tabletop exercise at an organization-defined frequency is sufficient."

*Question:* What impact level do the card processing platform and payment systems have? Is a two-yearly walk-through intended for systems above low impact?

**N2. Who sets RTOs.**
- Policy §6: "The IT manager sets the recovery time objectives for all systems."
- §3.2.1: the coordinator "with the process owners, leadership and business managers determine the acceptable downtime". MTD is "the total amount of time the system owner/authorizing official is willing to accept", and "the RTO must normally be shorter than the MTD".

*Question:* Who sets the maximum tolerable downtime that each RTO has to fit within? Are process owners involved?

**N3. Plan review.**
- Policy §7: "every three years."
- §3.1, sample policy statement: "must be reviewed annually and updated as necessary".
- §3.6: "whenever significant changes occur to any element of the plan".

*Question:* Is the three-year cycle for the policy meant to differ from the cycle for the plans? And what counts as a significant change?

**Gaps (NIST text with no counterpart in the policy)**

| # | NIST passage | Question for the owner |
|---|---|---|
| N4 | §3.1, key policy elements: "Resource requirements; Training requirements; … Plan maintenance schedule; and Minimum frequency of backups and storage of backup media" | The policy names none of these four. Should it? |
| N5 | §3.1: "the policy should define the organization's overall contingency objectives" | §1 states a purpose but gives no objectives. Are objectives meant to be in the policy? |
| N6 | §3.2: the BIA's results are used "to determine contingency planning requirements and priorities". §3.6: "When a significant change occurs, the BIA should be updated" | §4 doesn't link the BIA to §6 on RTOs, and gives no trigger for updating the BIA. Is that link intended? |
| N7 | §3.5.2: "Training should be provided at least annually" | The policy is silent on training. |
| N8 | §3.4.6: "a single authoritative role for overall decision-making responsibility, including plan activation" | §3 names no one with authority to activate plans. Who has it? |
| N9 | §3.1: plans "coordinated with related organization-wide policies and programs, including information system security, physical security, human resources" | The policy refers to no related policies. Should it? |

Chapters 4 and 5 cover what goes into a plan and technical platforms (client/server, telecommunications, mainframe). They describe plans rather than policy, so the review raises only one question from them. **N10:** Should the policy say where plan content and structure are set?

---

### Challenge: clauses that are ambiguous or open to two readings

- **§2 Scope.** "The ICT systems that support them": which systems are these, and who keeps the list? Does "all systems" in §6 include the marketing website, which §2 excludes?
- **§4.** When does the three-year BIA clock start? Who approves the result, given that the BIA officer "carries out" the BIA but approval isn't mentioned?
- **§5.** Does "by a desktop walk-through" mean that's the *only* method allowed, or the *minimum*? Are business continuity plans and ICT recovery plans tested together or separately?
- **§6.** Without a link to the BIA, is "sets" meant to be the IT manager's own judgement? Does that read as a decision or as a proposal to someone else? Who sets recovery point objectives (RPOs)? (General practice, not in the sources: the policy doesn't use the term RPO, though DORA Art. 12(6) does.)
- **§3.** Who stands in when the COO, the BCM officer or the IT manager is unavailable? (General practice, not in the sources. NIST §3.4.6 asks for alternates for team leaders, not for policy roles.)
- **§1.** It says "keeps its payment services running", but §2 also covers customer support and offices. Is the purpose meant to be narrower than the scope?

---

### Gaps

- **Document status:** The draft is version 0.4, dated 3 September 2026, a draft for the management board. It's still the document reviewed here, and its status hasn't changed.
- **No review date** appears in the document control. It names an owner and a version, but no review or next-review date.
- **Your intake answers:** You selected DORA and NIST SP 800-34 and said "all of it". These are your own statements, not sources.
- **Question 3 skipped:** I assumed there's no current approved policy, risk appetite statement or earlier management review output to check consistency against. If any exists, consistency with it hasn't been reviewed.
- **Not reviewed:** Delegated Regulation (EU) 2024/1774, the RTS that sets out the components of the ICT business continuity policy and testing (see DORA Art. 15(d)–(f)). It wasn't selected. This is probably the most relevant text left out, and legal or compliance may want it checked. Also not reviewed: ISO 22301, NIST CSF 2.0, FONES, the UK Cabinet Office guidance, the ESAs statement and any national transposition or supervisory guidance.
- **NIST SP 800-34 coverage:** The appendices (sample templates, BIA template) aren't in the copy, so they weren't reviewed.
- **Facts I can't confirm:** The company's licence type, exemption status, which functions are critical or important, and FIPS-equivalent impact levels. These aren't in the sources, and D0, N1 and D3 depend on them.
- **No embedded instructions:** I found no text in the document addressed to an AI.

---

Parts of this document were drafted with AI support (check-against-standards, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

Chief Operating Officer answers these, [legal or compliance] the marked points.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Grep: `^#+ `
- Grep: `^#+ |^\d\.\d+(\.\d+)? [A-Z]`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/eur-lex/dora-regulation-2022-2554.md`
- Grep: `microenterprise'|critical or important function'`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/check-against-standards/literature/nist/sp-800-34r1-contingency-planning-body.md`
