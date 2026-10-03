# check-against-standards baseline (no skill loaded), run1: Claude Code, guidance at 9c837c3

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a74cb355-f048-4ccc-977d-26a89170c941`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I checked the draft against **DORA**, the EU Digital Operational Resilience Act (Regulation (EU) 2022/2554), and the detailed rules under it on the ICT risk management framework (Delegated Regulation (EU) 2024/1774). No standard was attached, so I picked DORA because it applies directly to an authorised EU payment institution. If you meant another standard, such as ISO 22301 or your national regulator's rules, tell me and I'll check again.

**My view: the draft isn't ready for the board.** Several sections fall short of what DORA requires, and two of them affect the board directly.

## Gaps that need fixing

1. **The board never approves anything (§3, §7).** DORA Art. 5(2)(e) says the management board must approve and regularly review the business continuity policy and the ICT response and recovery plans. The draft only names the COO as owner. Add a line saying the board approves the policy and the plans, and that the policy reports to the board.

2. **A review every three years is too slow (§7).** The business continuity policy is part of the ICT risk management framework. Art. 6(5) requires that framework to be reviewed **at least once a year**, and also after major ICT incidents, testing or audit findings, and supervisory instructions. Change to an annual review with those extra triggers.

3. **Testing is too rare and too light (§5).** Art. 11(6) requires testing **at least yearly** and after major changes. The tests must include **cyber-attack scenarios** and **switchovers** between your main ICT systems and your backup capacity and facilities. A walk-through on paper every two years falls short on both counts. Art. 11(4) also requires testing the plans for critical functions that rely on ICT third-party providers.

4. **Recovery objectives are left to IT alone (§6).** Recovery time and recovery point objectives should come from the business impact analysis. Under Art. 12, they must reflect whether a function is critical or important. They also need to be agreed by the people who own each business process, not set by the IT manager alone. As written, IT sets the targets it is then measured against.

5. **The business impact analysis is narrow and infrequent (§4).** It leaves out the card processing platform, the offices and the supporting ICT, even though §2 puts all of these in scope. Art. 11(5) expects a business impact analysis of exposure to severe disruptions, using quantitative and qualitative criteria and scenario analysis. Running it every three years also doesn't fit an annual policy review. Rerun it on material change and feed it into each annual review.

6. **Several things DORA requires are missing:**
   - A **crisis management function** (Art. 11(7)) and crisis communication plans (Art. 14).
   - **Independent internal audit** of the ICT response and recovery plans (Art. 11(3)). The micro-enterprise exemption doesn't apply with 140 staff.
   - **Record-keeping** before and during disruptions (Art. 11(8)).
   - **ICT third-party providers**: continuity of outsourced critical functions, and links to exit strategies (Art. 28(8)). This is especially relevant if the card processing platform is run by an outside provider.
   - **Learning after incidents** and feeding lessons back into the plans (Art. 13).

## Smaller points

- **The marketing website exclusion (§2)** is probably fine, but the business impact analysis should justify it rather than the policy just stating it.
- **"Critical or important functions"** is the term DORA's obligations depend on, and it never appears in the draft. Define it, or point to where the firm's list of these functions is kept.
- **Check whether the simplified regime applies.** If the firm is a *PSD2-exempted* payment institution rather than a fully authorised one, a lighter set of DORA rules applies (Art. 16). Some of the points above would then be softer. Confirm which licence you hold.

I'm confident about the article references above. I'd still have compliance check the exact paragraph numbers before the paper goes to the board. I can also turn this into a redlined v0.5 of the policy or a one-page gap summary for the board pack.

**Tool calls (stream-json):**

- Bash: `ls -la; cat bc-policy-draft.md`
