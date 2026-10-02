# /check-against-standards case 6b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6c6ba161-298e-46e5-8a89-f755b0c5ae37`.

Files in the working folder: `bc-policy-draft.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you review our draft business continuity policy against DORA and tell us what is missing? The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I reviewed the draft against DORA (Regulation (EU) 2022/2554) and the Commission Delegated Regulation (EU) 2024/1774, which sets the detailed ICT risk rules. The draft has the basic outline of a business continuity policy, but it is missing most of what DORA requires. Several of its settings actually conflict with DORA: how often it tests, how it tests, and how often it is reviewed.

## Check first: which DORA regime applies?

The draft calls the firm "a small payment institution." If that means a payment institution exempted under PSD2 Art. 32(1), DORA Art. 16 applies. That is a lighter regime, and its detailed rules sit in Title III of the Delegated Regulation instead of Art. 24–26. If the firm is a fully authorised payment institution, the full regime in Art. 5–14 applies, whatever its size. I've reviewed against the full regime below, since that is the usual case. The policy should state which regime applies.

## Where the current sections fall short

| Section | Draft says | DORA expects |
|---|---|---|
| **Header / 3. Roles** | COO owns it; it is a "draft for the management board" | The **management body** has ultimate responsibility and must **approve** the ICT business continuity policy and the ICT response and recovery plans, and review them periodically (Art. 5(2)(e)). The policy should say this, not just send the draft to the board. |
| **2. Scope** | Lists services, systems and offices | Scope should be built around **critical or important functions**, which the draft never identifies. It should also cover functions supported by **ICT third-party providers** (Art. 11(4)), and record any exclusions with a reason. The marketing website may be out of scope, but you may need it for crisis messages to customers. |
| **4. Business impact analysis** | Every 3 years; covers payment services and the support desk | DORA requires a BIA based on **severe disruption scenarios**, using quantitative and qualitative criteria and internal and external data. It must look at how critical functions, processes and information assets are, and at the **dependencies between them**, including third parties (Art. 11(5)). Three years is too long because the BIA must feed the yearly review cycle. |
| **5. Testing** | Every **2 years**, **desktop walk-through only** | **At least once a year**, and also after any substantial change to ICT systems that support critical functions (Art. 11(6)). Tests must include **cyber-attack scenarios** and **switchovers** between primary systems and backup capacity, backups and backup facilities. Crisis communication plans must also be tested. Results must be documented (Delegated Reg. Art. 25). |
| **6. Recovery objectives** | IT manager sets RTOs for all systems | RTOs **and RPOs** must be set **per function**, based on how critical it is and its overall impact, and must match agreed service levels (Art. 12(6)). They should come from the BIA and be approved through governance, not set by IT alone. RPOs are missing entirely. |
| **7. Review** | Every **3 years** | The ICT risk management framework, which includes this policy, must be reviewed **at least once a year**. It must also be reviewed after major ICT incidents, supervisory instructions, and findings from tests or audits (Art. 6(5)). |

## What is missing entirely

1. **A separate ICT business continuity policy.** DORA wants a specific ICT business continuity policy that is part of the overall business continuity policy (Art. 11(1)). The draft treats ICT only as "systems in scope."
2. **ICT response and recovery plans.** These need:
   - criteria for switching them on and off;
   - containment measures;
   - fallback options if the main recovery approach fails;
   - an **independent internal audit review** (Art. 11(3); Delegated Reg. Art. 26).
3. **A scenario list.** Plans should cover extreme but plausible events: cyber-attack, insider threat, failure of an ICT provider, loss of premises, natural disaster, pandemic, and so on.
4. **Backups and restoration** (Art. 12):
   - what data is backed up and how often;
   - restoring onto systems that are physically and logically separate from the source;
   - spare ICT capacity;
   - integrity checks after recovery.
5. **Crisis management and communication.** You need a crisis management function with procedures for internal and external communication (Art. 11(7)). You also need a communication plan for customers, counterparties and the public, with at least one named person responsible for it (Art. 14).
6. **Third-party continuity.** The policy should cover the business continuity of ICT providers that support critical functions. It should also refer to **exit strategies** (Art. 28(8)) and to testing done together with those providers where relevant.
7. **Learning and evolving** (Art. 13):
   - reviews after incidents and lessons from tests;
   - reporting those findings to the management body at least once a year.
8. **Records and reporting.** Keep records that are easy to reach of what happened before and during a disruption (Art. 11(8)). Be able to give the regulator, on request, an estimate of the yearly costs and losses from major ICT incidents (Art. 11(10)).
9. **Links to other processes:**
   - ICT incident management and major-incident reporting (Art. 17–19);
   - the wider digital operational resilience testing programme (Art. 24–25).
10. **Roles that need adding.** The policy should give:
    - responsibilities to the management body;
    - escalation paths;
    - a crisis communications lead;
    - deputies for the BCM officer and IT manager.

## What to fix first

The biggest problems are testing (yearly and realistic, not a desktop walk-through every two years), the review cycle (yearly, not every three years), and approval by the management body. Next comes identifying critical or important functions, because the BIA, the RTOs and RPOs, the scope and the third-party sections all depend on it. After that, add the backup, crisis communication and third-party sections.

I wrote this from my knowledge of DORA and didn't check it against the official text in this session. Please check the article references against EUR-Lex before you rely on them in the board paper.

If it would help, I can turn this into a shareable page or rewrite the draft itself as a version 0.5.

**Tool calls (stream-json):**

- Bash: `ls -la; wc -c bc-policy-draft.md 2>/dev/null`
- Read: `/tmp/claude-1001/-opt-brain/172e68eb-beff-4eff-a578-707de5e8742d/scratchpad/g2/runs/check-against-standards/6b/run1/work/bc-policy-draft.md`
