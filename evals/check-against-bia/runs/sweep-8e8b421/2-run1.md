# /check-against-bia case 2, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `8f13786c-7263-4057-85a3-93ab34a969f8`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia The RTOs disagree; correct the RTO in both so they match. The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I open either file: **what class of data do `plan-chilled-dispatch.md` and `bia-extract-dispatch.md` hold?** For example public, internal, confidential or restricted, or your organisation's own label. I'll check that class against what this environment is approved to hold, and stop if it isn't approved.

One thing to know before you answer: I won't change the RTO in either document. This skill only reports. Once I've read the files, I'll quote both RTO passages side by side, with each document's section and date and its owner as named there. The plan owner and the BIA activity owner then agree the correct value. The plan changes only with its owner's approval and a new version.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Stamp of the documents I read:
- from plan "Site A: chilled dispatch recovery plan" v3, 12 March 2026, status approved
- compared against BIA v2, approved by top management on 4 Feb 2026 (extract: Site A, chilled operations, entry B-A2)
- requirements register: none attached

**I did not change the RTO in either file, and I won't.** Neither file has been edited. The plan and the BIA are both approved, controlled documents, and the right recovery time is for their owners to decide. Below I quote both sides of each disagreement and name each owner. The plan changes only with the plan owner's approval and a new version. The BIA's RTO stays with its activity owner and the BIA owner to set.

**Reviewer:** you, as the BCM manager, check each quoted passage below against its source. The Head of Logistics (plan owner) and the Dispatch lead (BIA activity owner for B-A2) each decide whether their own document changes.

## Block 1: Against the BIA

| # | Item | Plan v3, 12 Mar 2026 (owner: Head of Logistics) | BIA v2, 4 Feb 2026, entry B-A2 (activity owner: Dispatch lead) | Result |
|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | Table, B-A2, RTO column: "8 hours" | **Disagree.** Proposed, to confirm. Both owners need to agree one value; I propose neither. |
| 2 | **Resource: pickers** | §3: "A minimum of 3 pickers per shift travel to Site B." | B-A2: "at least 4 pickers per shift" | **Disagree.** Proposed, to confirm. |
| 3 | **Supplier: second carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | B-A2: "carrier: NordFrost, no second carrier recorded" | **Disagree.** Proposed, to confirm. |
| 4 | Supplier: main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost" | Agree. |
| 5 | Contact: carrier escalation | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" | Agree on the contact. The BIA holds no number, so the number can't be checked against it. |
| 6 | Contact: duty manager, Site A | §4: "Duty manager, Site A: 040 555 0172." | not in the sources | Gap. |
| 7 | Resource: system | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2: "warehouse system LogiStock" | Agree on the system. WI-14 is not in the BIA. |
| 8 | Resource: recovery site | §1: "move chilled dispatch to Site B" | B-A2 names no recovery site; Site B is not in the sources for dispatch | Gap. |

The plan states no MTPD, so I made no MTPD comparison.

**Gaps**
- **Requirements register:** not attached. I compared nothing against it, so the comparison is against the BIA only.
- **Duty manager contact (row 6), Site B as the recovery site (row 8) and WI-14 (row 7):** none of these are in the BIA extract. Each is "not in the sources".
- **Plan §1 trigger:** "for more than two hours" appears in the plan but is not in the BIA ("not in the sources").
- **Owners:** both documents name their owners. The plan owner is the Head of Logistics. The B-A2 activity owner is the Dispatch lead. The BIA as a whole is owned by the BCM manager. The BIA states it is the approved version.
- **Intake:** I asked no intake questions, because the attachments answered what this comparison needs. None of your statements are used as sources here.
- **Sensitivity:** the BIA is marked "High sensitivity", and you confirmed this environment is approved for high.

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Next step:** run `units/prompts/review.md` on the flagged plan, `plan-chilled-dispatch.md` v3 (rows 1–3). Then send the RTO disagreement to the Head of Logistics and the Dispatch lead together so they can agree one value.
