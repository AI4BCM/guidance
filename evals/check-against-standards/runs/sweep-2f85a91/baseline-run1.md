# check-against-standards baseline (no skill loaded), run1: Claude Code, guidance at 2f85a91

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `2889b323-a1bf-442d-997c-ae3c48fcc413`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

The draft isn't ready for the board. It's well short of the business continuity rules a payment institution has to meet. You didn't name a standard, so I checked it against **DORA** (EU Regulation 2022/2554, which has applied to EU payment institutions since January 2025). The detailed rules are in its technical standard, Commission Delegated Regulation 2024/1774. If you're regulated in the UK instead, see the note at the end.

## Clear conflicts with DORA

| § | Draft says | DORA expects | Fix |
|---|---|---|---|
| 5 Testing | Every **two years**, **desktop walk-through only** | Test business continuity and ICT response/recovery plans **at least yearly** and after any major change (Art. 11(6)). Tests must use realistic scenarios, including a severe cyber attack and switching over to backup systems and sites (RTS Art. 25). | Test at least once a year and after major changes, using a mix of methods. Include failover to backups, the cyber attack scenario, failure of a key supplier, and crisis communications. |
| 7 Review | Every **three years** by the COO | The ICT risk management framework, which this policy belongs to, is reviewed **at least yearly** and after major incidents or supervisory findings (Art. 6(5)). | Review yearly and when those events occur. The **board approves** each review. |
| 3 Roles | COO owns it; the board isn't mentioned | The management body is ultimately responsible. It must approve, oversee and periodically review the ICT continuity policy and the response and recovery plans (Art. 5(2)(e)). | Add the board's approval and oversight role, and say how often it receives reporting. |
| 6 Recovery objectives | The IT manager sets RTOs (maximum time to restore a system) for all systems | RTOs and RPOs (maximum acceptable data loss) are set **for each function**. They must account for whether the function is critical or important and for the wider impact (Art. 12). | Derive RTOs **and RPOs** from the impact analysis. Business owners agree them and the board approves them. The IT manager then designs recovery to meet them. RPOs are missing from the draft entirely. |

## Material gaps (the draft doesn't cover these at all)

- **Crisis management function** (Art. 11(7)): who declares a crisis, who sits on the crisis team, and how it escalates to the board.
- **Crisis communications** (Art. 14): how you inform staff, customers, partners and the regulator. This should link to the major-incident reporting rules in Art. 19.
- **Backup and restoration** (Art. 12): a backup policy, a separate backup site, and restore testing.
- **Third-party dependencies**: the card platform and other critical suppliers. The policy needs to cover supplier exit and continuity plans (Art. 28) and the impact analysis should map these suppliers.
- **Records** of what happened before and during a disruption (Art. 11(8)), and lessons learned after incidents and tests.
- **Independent assurance**: the framework must be audited regularly by internal audit (Art. 6(6)).
- **Training** and awareness for staff who have a role in the plans.

## Weaker points (not outright breaches, but likely to draw questions)

- **§4 impact analysis every three years**: DORA sets no frequency, but three years is long for a payment institution. Do it yearly and whenever services, systems or suppliers change. Widen it beyond "each payment service and the support desk" to cover the ICT systems, data, people, premises and suppliers those services depend on.
- **§2 scope**: excluding the marketing website is reasonable. Confirm it doesn't host anything customer-critical, such as a service status page, onboarding or payment links.
- **§1 purpose**: say that the policy covers ICT continuity, or point to a separate ICT continuity policy that forms part of it (Art. 11(1)).

## Housekeeping before the board sees it

- The organisation line contains "(invented for this eval)". Remove it.
- Add a version history and approval block: approved by, date, next review date.

## Assumptions

- **Full DORA framework applies.** I assumed you're an authorised payment institution, not one exempted under PSD2 Art. 32. Exempted institutions can use DORA's lighter framework (Art. 16), which relaxes several of these points. At 140 staff you're well above the micro-enterprise carve-outs either way.
- **If you're UK-regulated**, the benchmark is instead the FCA's operational resilience rules (SYSC 15A). The headline gaps would then be: important business services, impact tolerances, mapping of what those services depend on, severe-but-plausible scenario testing, and an annual self-assessment signed off by the board.

I can redraft the policy with these fixes, or turn this into a one-page summary for the board.

**Tool calls (stream-json):**

- Bash: `ls -la; cat bc-policy-draft.md`
