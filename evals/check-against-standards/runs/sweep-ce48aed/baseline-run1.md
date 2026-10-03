# check-against-standards baseline (no skill loaded), run1: Claude Code, guidance at ce48aed

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `f5ca2672-3921-495a-bf76-2f83c19043d6`.

Files in the working folder: `bc-policy-draft.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Check our draft policy before it goes to the board. The file bc-policy-draft.md in this folder is attached.

**Reply (verbatim):**

I reviewed `bc-policy-draft.md` against **DORA** (Regulation (EU) 2022/2554), which has applied to EU payment institutions since January 2025. Your folder contained no standards document, so I chose DORA myself. Tell me if you meant something else, such as ISO 22301 or your regulator's own guidance.

**It's not ready for the board.** Several requirements are missing or contradicted, and one line (testing every two years) directly conflicts with DORA.

## Conflicts with DORA

1. **Testing is too infrequent and too light (§5).** Article 11(6) requires the business continuity and ICT recovery plans to be tested **at least yearly**, and again after significant changes to systems that support critical functions. The draft says every two years. A desktop walk-through on its own also falls short: the detailed technical rules on ICT risk management (Delegated Regulation 2024/1774) expect tests that include cyber-attack scenarios, switching to backup systems, and restoring from backups. Crisis communication plans must be tested too.
2. **The board doesn't approve or review it (§3, §7).** Article 5(2)(e) makes the management body responsible for approving and periodically reviewing the continuity policy and recovery plans. The draft gives that to the COO alone.
3. **The review cycle is too long (§7).** The policy is part of the ICT risk management framework, which Article 6(5) says must be reviewed **at least yearly**, after major ICT incidents, and after audit or supervisory findings. The draft says every three years, with no triggers.
4. **There is no crisis management function.** Article 11(7) requires one for every firm except microenterprises, and at 140 staff you aren't one. It must include procedures for internal and external crisis communications (Article 14). The draft doesn't mention crisis management or communications at all.
5. **The IT manager sets recovery objectives alone (§6).** Recovery time objectives should come from the business impact analysis and depend on how critical each function is (Article 12). They need sign-off from the business owners, not only IT. The draft also has no recovery point objectives (how much data you can afford to lose) and no backup or restoration policy.

## Missing content

6. **What the policy must contain (Article 11(2)):**
   - Which payment functions count as critical or important.
   - How and by whom plans are activated, including containment steps.
   - How the first impact of a disruption is estimated.
   - Plan maintenance.
7. **No independent audit.** Article 11(3) and Article 6(6) require independent internal audit reviews of the recovery plans. The draft never mentions audit.
8. **Third parties are ignored.** If an outside provider runs the card processing platform, Article 11(4) and Article 28 need continuity and testing to cover it, with exit strategies for critical providers.
9. **The business impact analysis is too narrow (§4).** It should cover severe disruption scenarios, including cyber attacks and loss of key suppliers (Article 11(5)), and map dependencies on ICT systems and people. It should also be re-run when there are material changes, not only every three years.
10. **No records or lessons learned.** Records must be kept before and during disruptions (Article 11(8)), with a review after each incident (Article 13). The policy should also link to major-incident reporting (Article 19).

## Smaller points

- **Website exclusion (§2):** if the marketing website is how you'd tell customers about an outage, excluding it weakens your crisis communications.
- **Roles (§3):** name deputies, say who the BCM officer reports to, and add training and awareness.
- **Definitions:** add definitions (critical function, disruption, RTO/RPO) and a version and approval history table.

## Two caveats

- **Which DORA regime applies.** If you're an *exempted* small payment institution under PSD2 Article 32, DORA's lighter regime in Article 16 applies instead of most of Article 11. The core gaps (board ownership, regular testing, backups, review after major incidents) would remain, but some of the specific deadlines above would loosen. 140 staff suggests you're fully authorised, but please confirm.
- **Article numbers.** I cited articles from memory. Check them against the official text before they go into a board paper, and this isn't legal advice.

I haven't changed the file. I can redraft the policy to close these gaps, or turn this into a shareable review page for the board pack.

**Tool calls (stream-json):**

- Bash: `cd /tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/baseline/run1/work && ls -la && git log --one`
- Glob: `**/*`
- Read: `/tmp/claude-1001/-opt-brain-479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/baseline/run1/work/bc-policy-draft.md`
- Read: `/tmp/claude-1001/-opt-brain/479d8506-8a2a-49e4-a75e-50a3b6dbe813/scratchpad/sweep6/runs/check-against-standards/baseline/run1/work/bc-policy-draft.md`
