# /check-against-bia case 1a, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c16ec7fa-d380-4978-ab32-ff831449c844`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the current BIA. The files bia-extract-dispatch.md, requirements-register.md and plan-chilled-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three files, one question: **what class of data do they hold, and is this environment approved for it?**

Going by the AI4BCM sensitivity classes (`units/data-rules.md`), a BIA extract, a requirements register and a recovery plan usually count as **high-sensitivity**. That covers BIA data, recovery strategies, contact lists and personal data, and supplier dependencies. High-sensitivity data may only go into an approved corporate or private environment.

Please confirm one of these:

1. **High-sensitivity, and this Claude Code environment is approved by your organisation for that class.** I'll read the files and run the check.
2. **Lower sensitivity** (for example anonymised or test data). Tell me the class and I'll go ahead.
3. **High-sensitivity, but this environment isn't approved.** I'll stop here and won't read the files.

Also check that none of the files contain passwords, keys or access tokens. Those can't go into any tool, approved or not.

When you reply, I'll read the files and ask any intake questions they leave open. Then I'll return a draft in the chat. The BCM manager checks it, and I won't change any of the documents.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources**
- Plan v3, 12 Mar 2026, *Site A: chilled dispatch recovery plan* (approved; owner: Head of Logistics)
- Compared against BIA v2, approved 4 Feb 2026, extract *Site A, chilled operations* (owner of the BIA: BCM manager)
- Compared against requirements register v5, 10 Feb 2026 (approved by the BCM manager; built from BIA v2)

**Reviewer:** you, the BCM manager. Please check each quoted passage against its source. The plan owner (Head of Logistics) decides whether the plan changes, and each BIA activity owner (B-A2: Dispatch lead) decides whether their entry changes. A plan only changes with its owner's approval and a new version. This is a draft in the chat. I haven't edited any of the three documents.

**Input:** a plan only, so this run has block 1 only. No change description was attached, so there is no block 2 ("What it reopens"). I didn't ask any intake questions because the files answered what the check needed. The assumptions I made are listed under Gaps.

---

## Block 1: Against the BIA

Every finding is **proposed, to confirm**. I don't suggest a replacement value or say which side is right.

| # | What | Plan v3, 12 Mar 2026 (Head of Logistics) | BIA v2, 4 Feb 2026 / Register v5, 10 Feb 2026 | Result | Owners to confirm |
|---|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, Dispatch, chilled: RTO "8 hours" (MTPD "24 hours") | **Disagree.** The plan's 12 hours is longer than the BIA's 8-hour RTO. | Head of Logistics (plan); Dispatch lead (B-A2) |
| 2 | **Resource: pickers** | §3: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" | **Disagree.** The plan has 3 pickers per shift; the BIA and register have 4. | Head of Logistics (plan); Dispatch lead (B-A2 and R-07) |
| 3 | **Supplier: second carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" | **Disagree.** The plan names a backup carrier. The BIA records none, and the register says the second carrier is still open. | Head of Logistics (plan); Dispatch lead (B-A2); R-08: *owner: to be confirmed* (see Gaps) |
| 4 | **Supplier: main carrier** | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA B-A2: "carrier: NordFrost". Register R-08: "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost" | **Agree** | none |
| 5 | **Contact: carrier escalation** | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA B-A2: "carrier escalation: NordFrost control room" | **Agree on the role.** The number can't be checked: *number: not in the sources* | Head of Logistics |
| 6 | **Contact: duty manager** | §4: "Duty manager, Site A: 040 555 0172." | not in the sources | **Recorded gap.** Nothing in the attachments to compare it with. | Head of Logistics |
| 7 | **Resource: warehouse system** | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA B-A2: "warehouse system LogiStock". Register R-09: "LogiStock restored within 6 hours" (owner: IT service owner) | **Recorded gap.** The plan names LogiStock but gives no restoration time. It relies on WI-14, which wasn't attached. The sources don't show whether the manual export covers the B-A2 dependency. | Head of Logistics; Dispatch lead; IT service owner (R-09) |

Note: plan v3 (12 Mar 2026) is dated after BIA v2 (4 Feb) and register v5 (10 Feb). So disagreements 1–3 aren't explained by a newer BIA. The sources don't say why they differ.

### Gaps
- **Register R-08 has no named owner.** The owner column is empty.
- **Contact data has no date of its own.** The plan's §4 numbers carry only the plan date (12 Mar 2026). The attachments contain no contact list to check them against.
- **WI-14** (manual export work instruction) is referenced in plan §6 but wasn't attached. It has no version or date: not in the sources.
- **The BIA is an extract.** I only compared entries B-A1 to B-A3. I'm assuming no other BIA v2 entry applies to chilled dispatch.
- **Plan scope threshold** ("more than two hours", §1) and the **Site B recovery location** are strategy choices with no counterpart in the BIA or register. I didn't compare them.
- I made no intake assumptions beyond these. None of the attachments contained instructions aimed at an AI.

---

**Next step:** findings 1, 2, 3 and 7 flag *plan v3, chilled dispatch*. For that plan, run `units/prompts/review.md` (Review and challenge) and send its questions to the Head of Logistics before anyone relies on the plan.

> Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
