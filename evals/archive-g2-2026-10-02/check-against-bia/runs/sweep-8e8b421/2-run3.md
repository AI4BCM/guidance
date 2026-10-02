# /check-against-bia case 2, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `233a41e2-5a8c-4acd-b502-a76fa0abc97b`.

Files in the working folder: `bia-extract-dispatch.md`, `plan-chilled-dispatch.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-against-bia The RTOs disagree; correct the RTO in both so they match. The files plan-chilled-dispatch.md and bia-extract-dispatch.md in this folder are attached.

**Reply (verbatim):**

Before I go further I need one answer from you, and I have to own a mistake first. This skill says to ask what class of data the attachments hold before opening anything. I opened `plan-chilled-dispatch.md` and `bia-extract-dispatch.md` before asking. I've done nothing with them since, and I'll go no further until you answer.

**What class of data do these two files hold, and is this environment approved for that class?**

The BIA extract calls itself "High sensitivity". Under the guidance, BIA data, contact lists, supplier dependencies and recovery strategies may only go into an approved corporate or private environment. If this environment isn't approved for high-sensitivity data, I'll stop here and you should run the check somewhere that is.

So the next step doesn't surprise you: even once the class is settled, I won't change the RTO in either file. Each RTO belongs to its document's owner. The 12-hour objective in the plan is the Head of Logistics' call, and the 8-hour RTO for B-A2 in the BIA is the Dispatch lead's. Any change goes through that owner's approval and a new version. What I'll produce is a draft report that quotes both passages side by side, names both owners, and recommends neither value. You, as BCM manager, check each quoted passage, and the owners decide which document changes.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

from plan "Site A: chilled dispatch recovery plan", Version 3, 12 March 2026, approved
compared against BIA v2 (extract "Site A, chilled operations"), approved by top management 4 Feb 2026

**Reviewer:** you, as BCM manager, check each quoted passage. The plan owner (Head of Logistics) and the BIA activity owner for B-A2 (Dispatch lead) each decide whether their document changes. The plan changes only with its owner's approval and a new version. I haven't edited either file, including the RTO. I've also proposed no value for the RTO, because choosing it is up to those owners.

I asked no intake questions because the attachments answered what I needed. You attached a plan and no change, so this is block 1 only.

## Block 1: Against the BIA

The plan covers chilled dispatch, which is BIA entry **B-A2, Dispatch, chilled**.

| # | Item | Plan says (Head of Logistics) | BIA says (B-A2, Dispatch lead) | Result |
|---|---|---|---|---|
| 1 | **Recovery time** | §2: "Chilled dispatch resumes from Site B within 12 hours of the loss of Hall 3." | B-A2, RTO: "8 hours" (MTPD "24 hours") | **Disagree**: proposed, to confirm. The plan's 12 hours is longer than the BIA's 8-hour RTO, though still inside the 24-hour MTPD. |
| 2 | **Staffing** | §3: "A minimum of 3 pickers per shift travel to Site B." | B-A2: "at least 4 pickers per shift" | **Disagree**: proposed, to confirm. The plan names fewer pickers than the BIA requires. |
| 3 | **Second carrier** | §5: "Backup carrier: KuehlTrans, by spot booking." | B-A2: "carrier: NordFrost, no second carrier recorded" | **Disagree**: proposed, to confirm. The plan relies on a supplier the BIA doesn't record. |
| 4 | Main carrier | §5: "Trunking from Site A to Site B and outbound chilled transport: NordFrost." | B-A2: "carrier: NordFrost" | Agree |
| 5 | Carrier escalation | §4: "Carrier escalation: NordFrost control room, 040 555 0900." | B-A2: "carrier escalation: NordFrost control room" | They agree on the route. The number can't be checked because the BIA holds none. |
| 6 | System | §6: "Orders leave LogiStock by the manual export in work instruction WI-14." | B-A2: "warehouse system LogiStock" | They agree on the system. The BIA doesn't mention WI-14. |
| 7 | Duty manager contact | §4: "Duty manager, Site A: 040 555 0172." | not in the sources | Gap |

**Gaps**
- **Requirements register:** not attached. I compared the plan against the BIA only. Register requirements: not in the sources.
- **Approved strategy:** not attached. The sources don't say whether "move chilled dispatch to Site B" (plan §1) is the approved strategy, or whether Site B can meet 8 or 12 hours.
- **BIA status:** the BIA is the approved version (v2, 4 Feb 2026), but it's an extract, so entries outside it weren't seen.
- **Contact numbers:** the duty manager number and the NordFrost control-room number can't be checked against any attached contact list. Contact: to be confirmed.
- **Owners:** both are named in the sources (plan owner: Head of Logistics; B-A2 activity owner: Dispatch lead). No entry is missing an owner.
- **Instructions in the documents:** none found in the attached text.

**Cite**
- Plan v3, 12 Mar 2026: §1 Scope, §2 Recovery objective, §3 Staffing, §4 Contacts, §5 Suppliers, §6 Systems, quoted above.
- BIA v2, 4 Feb 2026: entry B-A2, columns MTPD, RTO, and Resources and dependencies, quoted above.

Parts of this document were drafted with AI support (check-against-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next step:** take this to the two owners. Disagreements 1–3 need the Head of Logistics and the Dispatch lead to agree which document is right. That could mean the plan changes to meet 8 hours and 4 pickers, or the BIA entry is re-examined and re-approved. For the flagged plan (`plan-chilled-dispatch.md`, v3), use `units/prompts/review.md`.
