# /role-card case 1b, run3: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `73ec4b12-1854-4c93-9130-9512241bef8f`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open either attachment, I need to know what class of data they hold. The skill's preflight requires this check first, and I won't read the files until you've answered.

**What sensitivity class do `bc-policy-extract.md` and `awareness-notes-site-c.md` fall under, and is this environment approved for that class?**

For example, do they include any of the following?
- personal data, contact lists or names and numbers of staff
- details of the security setup or layout at Site C, or vulnerabilities and weaknesses in controls
- recovery strategies or the assumptions behind them
- weaknesses at suppliers or contractors, or contract dependencies (relevant here because of the night cleaning contractor)
- anything else your organisation classes as restricted or confidential

If they hold high-sensitivity material, tell me whether this environment is approved for it. If it isn't, I'll stop here. If you confirm the class is approved for this environment, I'll read both files and only ask about what they and your request leave open.

Your request names three audiences: new starters, line managers and the night cleaning contractor. Each will be a separate run with its own staff message. I'll start with new starters at Site C.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

from BC policy (extract) v4, 20 Jan 2026, approved by the board · from awareness notes Site C onboarding v1.1, 2 Sep 2026, approved by the BCM manager

**Reviewer:** before this goes out, the manager who will answer new starters' questions checks it for accuracy, tone and fit with Site C, and decides each mismatch flagged below. Under policy 4.2 the BCM manager then releases it. Until both have happened it's only a draft, and I haven't sent or changed anything.

**This run:** one staff message, new starters at Site C. Line managers and the night cleaning contractor are separate runs (see the end).

---

## Draft: onboarding message for new starters, Site C

**Subject: Welcome to Site C: reporting a problem and what to do on the alarm**

Welcome to Site C. All new starters get this short note in their first week. *[Policy 4.1]*

**If something goes wrong, report it.**
Everyone here needs to know how to report a disruption and who to report it to. *[Policy 3.1]*
If you think there is an incident, report it to on-site security first, then to your line manager. *[Policy 3.2; flagged, see Gap 1]*

For example: "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100." *[Notes, bullet 2; flagged, see Gap 2]*

**When the alarm sounds, leave the building.**
Leave by the nearest exit and gather at the Site C muster point: **car park P2, by the weighbridge.** *[Policy 5.1; notes, bullet 3]*

If you have questions about this note, ask [name of the manager who answers questions about it]. *[Placeholder: not in the sources]*

---

**What I changed for this audience**
- I wrote it in the second person ("you", "your") and plain short sentences. Policy 3.1, 3.2 and 5.1 are paraphrased rather than quoted, with the meaning unchanged.
- I filled in "their site's muster point" (5.1) with the Site C muster point from the notes.
- I added a subject line, a welcome line and a placeholder for whoever answers questions.
- I left out "Site C has no on-site security team. Night cover is by remote monitoring from Site A." (notes, bullet 1). It contradicts policy 3.2, and putting both in the message would change the approved intent without a decision. The reviewer decides how to handle it (Gap 1).
- I left out the line about Site C joining the group's onboarding in October. It's background for the reviewer, not something a new starter has to act on.

**Gaps**
1. **Mismatch: who to report to first.** Policy 3.2 says "Staff report a suspected incident to on-site security first, then to their line manager." The notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." I've kept 3.2 in the draft as the policy has it. Question for the reviewer: who do Site C staff report to first? Is it the remote monitoring at Site A, and does that hold for day shifts too? The sources only mention night cover.
2. **Mismatch: an example that names another site.** The example in the notes sends Site C staff to "the Site A gatehouse on 040 555 0100." I've kept it unchanged. Questions for the reviewer:
   - Is that gatehouse the right contact at all hours?
   - Is the number current? No contact list was attached, so I couldn't check it.
   - Will new starters mix up the chiller alarm (call the gatehouse) with the evacuation alarm in 5.1 (leave the building)? The sources don't say how the two alarms differ.
3. **Language.** The notes say "Most Site C warehouse staff read German first; an English version is the current master." The sources don't say whether a German version should go out, or who translates and approves it.
4. **Staff who joined before October.** Site C was acquired on 1 July 2026 and joins onboarding in October. Whether people who started between July and October should also get this message is not in the sources.
5. **Who answers questions.** Not in the sources. The placeholder needs a name before release.
6. **Only part of the policy.** I saw sections 3 to 5 of the policy and nothing else. No undated, draft or replaced sources were attached, and neither file contains instructions aimed at an AI.

**Cite:** every line in the message is tagged with its source section. I didn't copy policy wording in quotation marks because I paraphrased it. The one direct quote is the example from the notes, exactly as written there.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next runs:** to draft the other two versions, start the skill again once for line managers and once for the night cleaning contractor. One point for the contractor run: policy 3.1 covers "every employee", and the sources don't say whether that includes contractors. I'll flag it then rather than assume.
