# /check-against-bia case 1a, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fc8de64a-8cbe-4a1e-bca4-351e1ec3ecb5`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the current BIA. The files bia-extract-dispatch.md, requirements-register.md and plan-chilled-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open the three files, one question.

**What class of data do `bia-extract-dispatch.md`, `requirements-register.md` and `plan-chilled-dispatch.md` hold, and is this environment approved for that class?**

The AI4BCM data rules (`units/data-rules.md`, Sensitivity classes) treat these as **high-sensitivity**, allowed only in an approved corporate or private environment:
- BIA data and risk assessment detail
- recovery strategies and design assumptions
- personal data and contact lists
- supplier weaknesses and contractual dependencies

A BIA extract and a dispatch plan will usually include several of these. Please confirm one of these:

1. **This environment is approved** for high-sensitivity BCM data. I'll then read the files and run the check.
2. **The files have been sanitised**, so they contain no real BIA values, contacts or supplier detail. Tell me what was removed.
3. **Neither of the above.** I'll stop here, and you can run the check in an approved environment.

If any file contains passwords, keys or access tokens, remove them first. They can't go into any tool, approved or not.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

**Sources compared**
- From plan *Site A: chilled dispatch recovery plan*, v3, 12 Mar 2026, approved (plan owner: Head of Logistics)
- Compared against BIA v2, approved by top management 4 Feb 2026 (extract *Site A, chilled operations*; BIA owner: BCM manager)
- Compared against Requirements register Site A, v5, 10 Feb 2026, approved by the BCM manager, built from BIA v2

**Reviewer:** you, as the BCM manager, check every quoted passage below against its source. The Head of Logistics decides whether the plan changes. The Dispatch lead (BIA activity owner for B-A2) and the register entry owners decide whether their entries change. The plan changes only with the Head of Logistics' approval and a new version.

The input is a plan only, with no change description, so this reply has block 1 only. I asked no intake questions because the attachments answered what the check needed.

---

## Block 1: Against the BIA

Every row is **proposed, to confirm**. I propose no replacement value and don't choose between the two sides.

| # | Item | Plan v3 (12 Mar 2026), Head of Logistics | BIA v2 (4 Feb 2026) / Register v5 (10 Feb 2026) | Result |
|---|---|---|---|---|
| 1 | **Recovery time** | §2 Recovery objective: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | BIA B-A2, Dispatch, chilled (Dispatch lead): RTO "8 hours"; MTPD "24 hours" | **Disagree.** The plan's 12 hours is longer than the BIA's 8-hour RTO. Owners: Head of Logistics and Dispatch lead |
| 2 | **Resource: staffing** | §3 Staffing: "A minimum of 3 pickers per shift travel to Site B." | BIA B-A2: "at least 4 pickers per shift". Register R-07: "Chilled dispatch: at least 4 pickers per shift" (Dispatch lead) | **Disagree.** The plan has 3 pickers per shift; the BIA and register have 4. Owners: Head of Logistics and Dispatch lead |
| 3 | **Supplier: second carrier** | §5 Suppliers: "Backup carrier: KuehlTrans, by spot booking." | BIA B-A2: "carrier: NordFrost, no second carrier recorded". Register R-08: "one carrier, NordFrost; second carrier open" (no owner named) | **Disagree.** The plan names a backup carrier that the BIA and register don't record. Owners: Head of Logistics, Dispatch lead, and the R-08 owner (**to be confirmed**) |
| 4 | Supplier: main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | BIA B-A2: "carrier: NordFrost". R-08: "one carrier, NordFrost" | Agree |
| 5 | Contact: carrier escalation | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | BIA B-A2: "carrier escalation: NordFrost control room" | The name agrees. The BIA has no number, so the number can't be checked against it (**contact number: to be confirmed** against the carrier contract or contact list) |
| 6 | Contact: duty manager | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources | **Gap.** Nothing to compare it with |
| 7 | **Resource: system** | §6 Systems: "Orders leave LogiStock by the manual export in work instruction WI-14." | BIA B-A2: "warehouse system LogiStock". Register R-09: "LogiStock restored within 6 hours" (IT service owner) | **Gap.** The plan sets no LogiStock recovery time and doesn't refer to R-09's 6 hours. Whether the WI-14 workaround covers R-09 is for the Head of Logistics and the IT service owner to settle |

I didn't compare entries B-A1 (Goods receipt) and B-A3 (Quality release, R-06). They are outside the plan's stated scope (§1, "Loss of Hall 3 (chilled dispatch)").

### Gaps
- **R-08 has no named owner.** Its Owner cell in the register is empty.
- **R-09's "6 hours" doesn't appear in the BIA extract.** The register gives "BIA v2, B-A2" as the source, but B-A2 in the extract only says "warehouse system LogiStock", with no restore time. The BCM manager should confirm where this value comes from.
- **The plan doesn't name the BIA version it was built against.** It's dated after BIA v2 and register v5, but it doesn't cite either one.
- **Not attached:** work instruction WI-14, the carrier contract or agreement with KuehlTrans, and the Site B capacity arrangements. Anything that depends on these is not in the sources.
- **The plan has no BIA-derived requirement for Site B as the recovery location** (§1, "move chilled dispatch to Site B"). The BIA extract records no requirement for it, so I couldn't compare one.
- No undated, draft or replaced sources. No embedded instructions found in the attachments.

---

**Next step:** run the plan through [`units/prompts/review.md`](units/prompts/review.md) for plan v3, *Site A: chilled dispatch recovery plan*. Rows 1, 2 and 3 flag it. Then put each disagreement to the Head of Logistics and the Dispatch lead together.

> Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].
