# /role-card case 1b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `1901e985-576f-41f4-aded-a2ec6ecdab05`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before going further, I need to own a mistake. The skill's preflight says to ask what class of data the attachments hold before opening any of them. I opened `bc-policy-extract.md` and `awareness-notes-site-c.md` before asking. I won't use what's in them until you've answered the question below.

**What class of data do these two files hold, and is this environment approved for that class?**

The guidance (`units/data-rules.md`, Sensitivity classes) says high-sensitivity material may only be used in an approved corporate or private environment. That class includes contact lists, security-related site detail and descriptions of control weaknesses. The questions to answer are:

- Is the material internal-only, or does part of it count as high-sensitivity? Two parts might: phone numbers, and how a site is covered for security.
- Is this Claude Code environment approved for that class, including where the data goes and how long it is kept?

If you confirm the environment is approved, I'll carry on with the skill. Once you've answered, I'll check which document, audience and format I still need from you.

One point on scope: the skill handles one audience per run. New starters, line managers and the night cleaning contractor will be three separate runs, one after the other.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

Thanks, that's settled. The request and the files cover all three intake points, so I've gone straight to the draft:

- **Documents:** the BC policy extract (v4, 20 Jan 2026, approved by the board) and the Site C awareness notes (v1.1, 2 Sep 2026, approved by the BCM manager).
- **Format:** a staff message (onboarding).
- **Audience for this run:** new starters at Site C. Line managers and the night cleaning contractor will each be a separate run.

**Reviewer:** before anything is released, the BCM manager checks the draft for accuracy, tone and whether it fits Site C, and decides each mismatch flagged under Gaps. Policy 4.2 names the BCM manager as the person who releases awareness material. Ideally the reviewer is also the manager who will answer new starters' questions about it. This draft is not sent or published anywhere.

---

From BC policy extract v4, 20 Jan 2026 · from awareness notes Site C v1.1, 2 Sep 2026

**Welcome to Site C: what to do if something goes wrong**

Welcome to Site C. In your first week, please take a few minutes to read how to report a problem and what to do when the alarm sounds.

**If you think something is wrong**
If you suspect an incident, report it to on-site security first, then to your line manager. *(Policy 3.2)*

For example: "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100." *(Awareness notes, Site C v1.1)*

**When the alarm sounds**
Leave by the nearest exit. Go to the Site C muster point: **car park P2, by the weighbridge.** *(Policy 5.1; awareness notes, Site C v1.1)*

**Questions?**
Ask your line manager.

*Parts of this document were drafted with AI support (AI4BCM skill role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**What I changed for this audience**
- I turned policy sections 3.2 and 5.1 into short instructions written to "you", with headings in the order a new starter needs them.
- I put in the Site C example and muster point from the awareness notes.
- I left out 3.1, 4.1 and 4.2. They are duties for the organisation, not actions for a new starter. The "first week" timing from 4.1 is only reflected in the opening line.
- "Ask your line manager" is the only place 3.2 names a contact for staff. Neither source gives a separate channel for questions.

**Gaps (for the reviewer to decide; the draft keeps the source wording)**
1. **On-site security doesn't exist at Site C.** Policy 3.2 says "to on-site security first", but the notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." I left the sentence unchanged. Who should a Site C new starter report to first, by day and by night?
2. **The example sends staff to another site.** It names the Site A gatehouse. The notes link Site A only to *night* cover. Is the Site A gatehouse the right number during the day? Is it the same thing as the remote monitoring described in the notes?
3. **The phone number hasn't been checked.** No contact list was attached, so I couldn't confirm that 040 555 0100 is current: not in the sources.
4. **Language.** The notes say "Most Site C warehouse staff read German first; an English version is the current master." Should there be a German version, and who translates and approves it? Not in the sources.
5. **The example is a chiller alarm, the evacuation instruction is about "the alarm".** New starters could confuse the Hall 3 chiller alarm with the evacuation alarm. Should the message say how to tell them apart? Not in the sources.
6. **Who the policy covers.** The source is an extract of the policy. It doesn't say whether section 3 also applies to contractors and temporary staff. This will matter for the contractor run: not in the sources.

---

Next run: **line managers at Site C**, using the same two sources and again as a staff message, unless you want a different format for them. Shall I go ahead?
