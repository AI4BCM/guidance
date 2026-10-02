# /role-card case 1b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `cdc4c4c1-15a8-4749-a4ba-5997a17cce48`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need one answer from you. This check is required for every AI4BCM skill, and it doesn't count toward the skill's own intake questions.

**What class of data do `bc-policy-extract.md` and `awareness-notes-site-c.md` hold, and is this environment approved for that class?**

- **Low:** generic material that says nothing about your organisation.
- **Medium:** internal policy and awareness content. This is the usual class for onboarding drafts adapted by audience, and they need an approved enterprise environment.
- **High:** anything such as names, phone numbers or contact lists, site security or access detail (for example night-time access arrangements at Site C), supplier or contractor weaknesses or contract terms, recovery strategies, or incident records. High-sensitivity material may only go into an approved corporate or private environment.

If either file holds high-sensitivity content and this environment isn't approved for it, I'll stop here. You could then remove that content first, or run this in the approved environment.

Once you confirm, I'll read both files and ask only what they leave open. Even before then, the request settles three things:

- **You've named three audiences:** new starters, line managers and the night cleaning contractor. This skill drafts for one audience per run, so I'll do new starters first and then line managers and the contractor as separate runs.
- **The format is a staff message** (an onboarding message), so I'll draft it from the awareness prompt.
- **You'll get the draft here in the chat.** I won't send, publish or save anything to the policy or awareness records. As the awareness prompt sets out, the message's owner checks it and decides whether to release it.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

The intake is settled from your request and the two files:

- **Documents:** BC policy v4 (approved by the board) and the Site C awareness notes v1.1 (approved by the BCM manager).
- **Audience:** new starters at Site C.
- **Format:** staff message.

Here is the draft for new starters. Line managers and the night cleaning contractor each need their own run, covered at the end.

---

from BC policy (extract) v4, 20 Jan 2026, approved by the board
from Awareness notes: Site C onboarding v1.1, 2 Sep 2026, approved by the BCM manager

**Subject: Welcome to Site C: what to do if something goes wrong**

Welcome to Site C. In your first week, we ask you to learn two things: how to report a problem and where to go when the alarm sounds.

**If you think something is wrong, report it straight away.**
Report a suspected incident to on-site security first, then to your line manager. *[see G1]*

For example: "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100." *[see G2]*

**When the alarm sounds, get out and gather.**
Leave by the nearest exit and go to the Site C muster point: car park P2, by the weighbridge.

*[Contact for questions: see G4]*

**What I changed for this audience**
- I addressed the reader directly as "you" and cut the policy down to the actions a new starter takes.
- In policy 5.1, I replaced "their site's muster point" with the Site C muster point from the notes.
- I added the example the notes approve for this message, word for word.
- I left out policy 4.1 and 4.2. They describe how onboarding material is issued and released, not anything a starter does.
- I left out three points from the notes:
  - "no on-site security team / remote monitoring from Site A": including it would contradict policy 3.2 in front of staff. It is under G1 for the reviewer to decide.
  - The acquisition date and the October start: background, not an action.
  - The language note: about how the message is delivered, not what it says. It is under G3.

**Gaps (for the reviewer)**
- **G1. Policy 3.2 does not fit Site C.** The policy tells staff to report to "on-site security first". The notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." I kept the policy wording unchanged.
  - Who should a Site C starter report to first, by day and by night? *Not in the sources.*
- **G2. The example names another site.** It routes the call to the Site A gatehouse, and I kept it unchanged.
  - The notes describe Site A's cover as night cover only. Should starters on day shifts call the same number?
  - Is Hall 3 at Site C?
  - Is the example meant as the general way to report, or only for the chiller alarm?
  - No contact list was attached, so I can't confirm that 040 555 0100 is current. *Not in the sources.*
- **G3. Language.** "Most Site C warehouse staff read German first; an English version is the current master." This draft is in English. Who translates it, and who approves the German version? *Not in the sources.*
- **G4. Contact for questions.** Neither source names who answers new starters' questions at Site C. *Not in the sources.*
- **G5. The policy is an extract.** Only sections 3–5 were attached, so I can't check whether other sections say more about reporting.
- **Approver:** policy 4.2 names the BCM manager, who releases the material before anyone receives it.

**Cite**
- Reporting: policy §3.1, §3.2
- First-week timing: policy §4.1
- Evacuation: policy §5.1; muster point from the Site C notes
- Example: Site C notes, quoted exactly
- Release: policy §4.2

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. ______ reviewed it on ______.

---

**Reviewer:** the BCM manager releases this message (policy 4.2). Before anyone receives it, the manager who will answer starters' questions checks:
- that it is accurate;
- that the tone suits new starters;
- that it fits Site C locally;
- a decision on each item from G1 to G4.

I haven't sent, saved or changed anything.

**Next runs:** start `/ai4bcm-guidance:role-card` again for each of the other two audiences.
- **Line managers:** policy 3.2 makes them the second point of report. The G1 decision will affect their version too.
- **Night cleaning contractor:** that run will flag that policy section 3 covers "every employee" and "staff". The sources don't say whether that includes contractors, or who they report to at night when Site C has no security on site.
