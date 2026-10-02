# /role-card case 1b, run3: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `ecb5b9da-1a2f-4e0d-a66f-2b143f4560e4`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open `bc-policy-extract.md` or `awareness-notes-site-c.md`, I need to know what kind of data they contain.

**What is the most sensitive kind of data in either file?** For example:

- **General or internal only**: policy wording, awareness points, nothing personal or security-related.
- **High sensitivity**, which includes any of these:
  - personal data, contact lists or named phone numbers
  - incident records
  - BIA or risk detail
  - control weaknesses, or site security or layout detail
  - supplier weaknesses or contract terms
  - recovery strategies
  - board material
  - audit findings that haven't been cleared

If either file holds high-sensitivity data, also tell me whether this environment is approved for that. If it isn't, I'll stop here. If you aren't sure, a quick description of what's in each file is enough.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

Draft for **Site C new starters**, written as a staff message. Line managers and the night cleaning contractor each need a separate run of this skill. I can do either next.

**Reviewer:** Before anything is released, the manager who will answer new starters' questions checks the message for accuracy, tone and fit with Site C, and decides each mismatch flagged below. The policy (4.2) says the BCM manager must release the message before anyone receives it. Nothing has been sent or saved anywhere.

---

From BC policy v4, 20 Jan 2026 (extract, sections 3–5) · from Awareness notes: Site C onboarding v1.1, 2 Sep 2026

**Welcome to Site C: what to do if something goes wrong**

Welcome to Site C. In your first week, we'd like you to know two things in case something disrupts work here.

**1. Report it straight away.**
If you think something has gone wrong, report it to on-site security first, then tell your line manager.
*For example:* "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100."
*(Policy 3.1, 3.2; example from Awareness notes v1.1)*

**2. If the alarm sounds, get out.**
Leave by the nearest exit and go to the Site C muster point: **car park P2, by the weighbridge.**
*(Policy 5.1; muster point from Awareness notes v1.1)*

**What I changed for this audience**
- I turned policy 3.1 and 3.2 into a single instruction in plain words ("report it… then tell your line manager"). The order is the same.
- I put "their site's muster point" (policy 5.1) together with the Site C location from the notes, so the reader doesn't have to look it up.
- I used the notes' example exactly as written, because the notes say it's meant for this message.
- I left out policy 4.1 and 4.2 (first-week delivery, BCM manager release). They tell the organisation what to do, not new starters.
- I left out "Site C has no on-site security team. Night cover is by remote monitoring from Site A." The reviewer has to decide this first (see Gap 1). It's also detail about how the site is secured, and a general staff message isn't the place for it.

**Gaps**
1. **Mismatch: no on-site security at Site C.** Policy 3.2 says to report "to on-site security first", but the notes say "Site C has no on-site security team." I've left the policy wording unchanged in the message. The reviewer needs to decide who Site C staff report to first, and whether that is different at night.
2. **Mismatch: the example names another site.** The example sends staff to the "Site A gatehouse", not anyone at Site C. I've left it unchanged. Questions for the reviewer:
   - Is Hall 3 at Site C?
   - Does 040 555 0100 reach the Site A remote monitoring team, and is it answered during the day as well as at night?

   No contact list was attached, so I couldn't check whether the number is current.
3. **Language.** The notes say "Most Site C warehouse staff read German first; an English version is the current master." Should there be a German version? If so, who translates it, and does the BCM manager release the translation too (policy 4.2)?
4. **Policy scope.** Policy v4 (20 Jan 2026) was written before Site C was acquired (1 Jul 2026). Do its sections apply to Site C as written, or is there a Site C addendum? Not in the sources.
5. **Partial source.** I only saw sections 3–5 of the policy. The sources don't define "disruption" or "suspected incident" (3.1, 3.2).
6. **Whom new starters ask about this message:** not in the sources.
7. **Channel and timing.** Policy 4.1 requires delivery in the first week, and the notes say Site C joins group onboarding in October. Which channel delivers the message is not in the sources.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next runs:**
- **Line managers:** for this audience, policy 3.2 makes them the second point of contact for reports.
- **Night cleaning contractor:** the policy extract mentions only "employee" and "staff", and nothing in the sources covers contractors. That gap will be flagged in that run, along with how Site A's night remote monitoring applies to the contractor.

Which run would you like next?
