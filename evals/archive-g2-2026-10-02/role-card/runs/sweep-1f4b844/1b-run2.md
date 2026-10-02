# /role-card case 1b, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6640e4bb-bdab-4607-b415-31baedbac45b`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open either attachment, I need to know how sensitive they are.

**What class of data do `bc-policy-extract.md` and `awareness-notes-site-c.md` hold, and is this environment approved for that class?**

- **High** (approved corporate or private environment only) means: personal data, contact lists or personnel records (including named contacts or phone numbers); security-related site detail; vulnerabilities or control weaknesses; incident records; recovery strategies; supplier weaknesses or contract dependencies (which could include the cleaning contractor arrangement); unreleased audit findings or board material.
- **Medium** means internal policy and awareness content with none of the above. Awareness and onboarding drafting is usually medium and still needs an approved enterprise environment.

Please confirm the class and whether this tool and environment are approved for it. If they aren't, I'll stop here.

After that I'll read the files. Two things to know up front:
- **One audience per run.** New starters, line managers and the night cleaning contractor become three separate drafts, done one at a time.
- **Drafts only.** I won't send, publish or edit anything. Each staff message goes to whoever checks and releases awareness messages before it goes out.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

**Reviewer:** the BCM manager. Policy 4.2 makes them the one who releases awareness material. Before release, they (or the manager who will answer staff questions) check accuracy, tone and local fit, and decide each flagged item below. Nothing has been sent or published.

**This run covers one audience: new starters at Site C.** Line managers and the night cleaning contractor each need a separate run (see the end).

---

from BC policy (extract) v4, 20 Jan 2026, approved by the board
from Awareness notes: Site C onboarding v1.1, 2 Sep 2026, approved by the BCM manager

**Subject: Welcome to Site C: what to do if something goes wrong**

Welcome to Site C. As part of your first week, here is what to do if something disrupts work on site.

**1. Report it straight away**
If you think something is wrong, report it to on-site security first, then to your line manager.
For example: "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100."

**2. If the evacuation alarm sounds**
Leave by the nearest exit and go to the Site C muster point: **car park P2, by the weighbridge**.

*Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**What I changed for this audience**
- Turned the policy clauses into short "you" instructions with a subject line and two numbered steps.
- Changed "a suspected incident" to "you think something is wrong". Please check this keeps the meaning of 3.2.
- Filled in "their site's muster point" (5.1) with the Site C muster point from the notes.
- Took the framing "first week" from 4.1.
- Left out policy 3.1 as a separate line. The message is how new starters learn how to report and to whom, so it carries out 3.1 rather than repeating it.
- Left out policy 4.2, because it is an instruction for the BCM manager, not for staff.
- Left out the note that Site C has no on-site security team and is monitored remotely from Site A at night. Putting it in the message would contradict step 1 before you've decided who Site C staff should report to first (see Gap 1).
- Left out the German-language point, which is Gap 3.

**Gaps (for the reviewer to decide)**
1. **Mismatch: policy 3.2 doesn't fit Site C.** The policy says staff report "to on-site security first", but the notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." I've kept the policy wording in step 1. Questions for you:
   - Who do Site C staff report to first, by day and at night?
   - Is the Site A gatehouse the right first call?
   - Does this need a policy change or only local guidance?
2. **The example may not fit, and I can't check it.**
   - The notes don't say whether Hall 3 is at Site C.
   - The notes don't say whether the Site A gatehouse number works by day, or only during night cover.
   - No contact list was attached, so I couldn't check 040 555 0100. I've kept the example exactly as the notes give it.
3. **Language: not settled by the sources.** The notes say "Most Site C warehouse staff read German first; an English version is the current master." Neither source says whether a German version is needed, who translates it, or who releases it. This draft is the English master only.
4. **Who answers questions: not in the sources.** Neither source names a contact for new starters' questions about this message.

**Cite**
- Step 1: policy §3.2; example quoted from the Awareness notes v1.1.
- Step 2: policy §5.1; muster point from the Awareness notes v1.1.
- Timing: policy §4.1.
- Release: policy §4.2.

---

**Next runs (one audience each):**
- **Line managers.** Policy 3.2 makes them the second point of report. The sources say nothing else about their role, so that draft may come out short, with gaps listed.
- **Night cleaning contractor.** Expect a scope gap: the policy covers "every employee" and "staff", and nothing in the sources says whether it applies to contractors. The night cover by remote monitoring from Site A also bears directly on that audience.

Should I go ahead with line managers next?
