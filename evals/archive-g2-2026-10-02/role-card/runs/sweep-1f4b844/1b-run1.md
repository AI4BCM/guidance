# /role-card case 1b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `5dcd8af4-5818-42ed-b8f9-62102e4b0cac`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open either file, I need to check one thing.

**What kind of data do `bc-policy-extract.md` and `awareness-notes-site-c.md` hold, and is this environment approved for it?**

Under the guidance, these kinds of data may only go into an approved corporate or private environment:
- personal data, contact lists or personnel records (for example names and phone numbers in a call tree)
- recovery strategies and design assumptions
- vulnerabilities and control weaknesses
- security-related architecture or site detail (for example Site C access arrangements or alarm handling)
- supplier weaknesses and contractual dependencies (which could include the cleaning contract)
- BIA data, risk assessment detail, incident records or live crisis information
- board papers, or audit findings the audit owner hasn't cleared yet

Reply with one of these:
1. **No high-sensitivity content:** both files are, for example, a published policy extract and general awareness notes.
2. **High-sensitivity content, but this environment is approved for it.**
3. **High-sensitivity content, and you're not sure this environment is approved.** In that case I'll stop here, and you can ask your information security team before we go on.

If either file holds passwords, keys or access tokens, remove them first. They don't go into any tool.

**What happens after you answer:**
- I'll read the two files. Then I'll ask only what they leave open, such as the approved document's version and date.
- **One version per audience:** you've named new starters, line managers and the night cleaning contractor. Each audience is drafted as its own version, so that's three in total, starting with new starters.
- **Reviewer:** each staff message is checked and released by the person or team named in the awareness prompt's Task and Review lines. I'll name them once I've loaded that prompt.
- **What you get:** each version is a draft in this chat. I won't send, publish or change anything.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

I've drafted the new starters message below. The line manager and night cleaning contractor versions are separate runs, one audience each, so I haven't started them.

**Reviewer:** the manager who will answer staff questions about this message checks it for accuracy, tone and local fit, and decides each mismatch flagged under Gaps. Policy 4.2 also says the BCM manager releases awareness material before anyone receives it. I haven't sent, published or changed anything.

---

From BC policy v4, 20 Jan 2026 (approved by the board)
From Site C onboarding awareness notes v1.1, 2 Sep 2026 (approved by the BCM manager)

**Subject: Welcome to Site C: what to do when something goes wrong**

Welcome to Site C. Please read this in your first week. It tells you what to do if something disrupts work here.

**Report it straight away**
- Report a suspected incident to on-site security first, then to your line manager.
- For example: "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100."

**If the alarm sounds, get out**
- Leave by the nearest exit.
- Go to the Site C muster point: **car park P2, by the weighbridge.**

**Questions?** Ask [manager who answers questions about this message; reviewer to fill in].

*Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].*

---

**Cite**
- Reporting: policy §3.1 and §3.2.
- Chiller alarm example: awareness notes, bullet 2, quoted exactly.
- Leaving and muster point: policy §5.1, plus awareness notes bullet 3 for the Site C location.
- First-week timing: policy §4.1.

**What I changed for this audience**
- I wrote it as a short welcome addressed to "you", with two headings, so it can be read in two minutes.
- I put the Site C muster point in place of "their site's muster point" (§5.1), using the notes.
- I combined §3.1 (know how and to whom to report) into the reporting section instead of giving it its own line.

**Left out, with reasons**
- **No on-site security at Site C; night cover by remote monitoring from Site A (notes, bullet 1):** this is security-related site detail, which the guidance treats as high sensitivity. Whether staff should be told is for the reviewer to decide. This also means the files may hold more than the medium class you gave them, so please confirm that with information security.
- **Acquired on 1 July 2026; joins group onboarding in October (notes):** this is background for whoever plans the rollout, not something a new starter needs to do.

**Gaps (for the reviewer)**
1. **The reporting route doesn't fit Site C.** §3.2 says to report "to on-site security first", but the notes say Site C has no on-site security team. I kept the policy wording as written. Who should a Site C starter report to first, in the day and at night? The sources don't say.
2. **The example uses another site's contact.** It sends Site C staff to the Site A gatehouse. I kept it as the notes have it. No contact list was attached, so I can't confirm the number is current or staffed at all hours. Does it apply only at night (notes, bullet 1), or around the clock?
3. **It isn't clear whether the chiller alarm means evacuate.** §5.1 says to leave "on the alarm". The chiller example says to call. Should staff leave, call, or do both when the Hall 3 chiller alarm sounds? The sources don't say.
4. **Language.** Most Site C warehouse staff read German first, and the English version is the current master. Who produces and approves a German version, and is it released under §4.2 as well? The sources don't say.
5. **No named contact for questions.** The sources name no manager who answers questions about this message, so I left a placeholder.

---

**Next runs:** the line manager version and the night cleaning contractor version. Before the contractor version I'll need to ask one thing. The policy speaks of "every employee" and "staff", so does it cover contractor staff, and who at the contractor receives and releases the message? Say which audience to do next.
