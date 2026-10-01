# /check-against-bia case 1a, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `506a03d4-3d0f-4177-bd94-a9e80c13a54b`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`, `requirements-register.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia Check the dispatch plan against the current BIA. The files bia-extract-dispatch.md, requirements-register.md and plan-chilled-dispatch.md in this folder are attached.

**Reply (verbatim):**

I'll start the check against the BIA. I haven't opened the three files yet. First I need to know how sensitive they are.

**What class of data do these three files hold, and is this environment approved for it?**

A BIA extract, a requirements register and a continuity plan usually count as **high-sensitivity** data. They tend to contain BIA data, recovery strategies, supplier dependencies and often contact lists or personal data. Data in that class may only go into an approved corporate or private environment.

Please confirm one of these:
- **High-sensitivity, and this environment is approved for it.** I'll go ahead.
- **High-sensitivity, but this environment is not approved, or you're not sure.** I'll stop here, and you can run the check in an approved environment.
- **A lower class**, such as anonymised or test data. Tell me which and I'll go ahead.

Once you've answered, I'll read the files. Then I may ask up to three questions about anything they leave open, and write the comparison. The comparison is a draft in this chat and changes none of the three documents. The BCM manager checks each quoted passage. The plan owner and each BIA activity owner decide whether their document changes.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

From plan "Site A: chilled dispatch recovery plan" v3, 12 Mar 2026 (approved, owner Head of Logistics)
Compared against BIA v2, approved 4 Feb 2026 (extract "Site A, chilled operations", owner BCM manager)
Compared against requirements register "Site A" v5, 10 Feb 2026 (approved by the BCM manager, built from BIA v2)

**Reviewer:** the BCM manager checks each quoted passage below. Each document's owner decides whether their document changes: the Head of Logistics for the plan, the Dispatch lead for BIA entry B-A2, and the requirement owners named in the table. The plan changes only with the Head of Logistics' approval and a new version. This is a draft for review and none of the three documents was changed. I didn't ask any intake questions because the files answered them. My one assumption is listed under Gaps.

## Block 1: Against the BIA

| # | Item | Plan v3, 12 Mar 2026 | BIA v2, 4 Feb 2026 / Register v5, 10 Feb 2026 | Result | Owners named in the sources |
|---|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | B-A2, RTO: "8 hours" (MTPD "24 hours") | **They disagree**: the plan says 12 hours, the BIA RTO says 8. Proposed, to confirm. | Plan: Head of Logistics. B-A2: Dispatch lead. |
| 2 | **Resource: pickers** | §3: "A minimum of 3 pickers per shift travel to Site B." | B-A2: "at least 4 pickers per shift". R-07: "Chilled dispatch: at least 4 pickers per shift" | **They disagree**: the plan says 3, the BIA and register say 4. Proposed, to confirm. | Plan: Head of Logistics. B-A2 and R-07: Dispatch lead. |
| 3 | **Supplier: second carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | B-A2: "carrier: NordFrost, no second carrier recorded". R-08: "one carrier, NordFrost; second carrier open" | **They disagree**: the plan names a backup carrier, while the BIA and register record none. Proposed, to confirm. | Plan: Head of Logistics. B-A2: Dispatch lead. R-08: **no owner named** (see Gaps). |
| 4 | Supplier: main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost". R-08: "one carrier, NordFrost" | They agree. | — |
| 5 | Contact: carrier escalation | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" | They agree on the escalation point. The BIA has no phone number, so the number can't be checked: "number: to be confirmed against a contact list". | Plan: Head of Logistics. |
| 6 | Contact: duty manager | §4: "Duty manager, Site A: 040 555 0172." | Not in the sources | Recorded gap: neither the BIA nor the register gives anything to compare against. | Plan: Head of Logistics. |
| 7 | **Resource: system** | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2: "warehouse system LogiStock". R-09: "LogiStock restored within 6 hours" | **Recorded gap**: the plan names a workaround but gives no restore time for LogiStock, so the 6 hours in R-09 can't be compared. WI-14 isn't attached. Proposed, to confirm. | Plan: Head of Logistics. R-09: IT service owner. |
| 8 | Activation threshold | §1: "Loss of Hall 3 (chilled dispatch) for more than two hours." | Not in the sources | Recorded gap: the BIA sets no threshold to compare against. | Plan: Head of Logistics. |

I haven't proposed a replacement value for any of these, and I haven't picked between the two recovery times.

**Gaps**
- **R-08 has no owner.** The register's Owner column is empty for "Chilled trunking Site A to Site B and outbound: one carrier, NordFrost; second carrier open". Disagreement 3 therefore has no named owner on the register side.
- **The approved strategy isn't attached.** The plan's §1 says "Recovery option: move chilled dispatch to Site B". I couldn't check whether that is the strategy approved in the design stage. The BIA only mentions Site B as "inbound trunking from Site B" (B-A1).
- **Plan v3 doesn't say which BIA version it was built from.** It is dated 12 Mar 2026, after both BIA v2 (4 Feb) and register v5 (10 Feb), and still differs from them on items 1–3.
- **Not attached:** work instruction WI-14, contact lists, and any supplier contract or spot-booking arrangement with KuehlTrans.
- **My assumption:** the request says "current BIA", and I've taken that to mean BIA v2, approved 4 Feb 2026, the version in the extract. No later or draft version was attached.
- **The BIA extract has no section numbers**, so BIA citations above use the entry reference and column.

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** the chilled dispatch plan (v3, 12 Mar 2026) is flagged on items 1, 2, 3 and 7. Run `units/prompts/review.md` on it next.
