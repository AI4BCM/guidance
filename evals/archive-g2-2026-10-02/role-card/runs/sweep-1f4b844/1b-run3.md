# /role-card case 1b, run3: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `e6ea7509-8ddc-4085-959a-0ee14ee55fa5`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open `bc-policy-extract.md` or `awareness-notes-site-c.md`, I need to know what kind of data they contain. Onboarding drafts adapted for each audience need at least an approved enterprise environment (medium sensitivity). Some content is high-sensitivity and may only be handled in an approved corporate or private environment. That includes:

- personal data, contact lists or personnel records (named people, phone numbers, call-out lists)
- security-related site detail (access codes, alarm or entry procedures, building layout)
- vulnerabilities, control weaknesses, recovery strategies or supplier and contractor dependencies
- incident records or live crisis information

**What class of data do these two files hold, and is this environment approved for that class?** If there's anything sensitive in them, tell me where it is, for example a contact list in the awareness notes. If this environment isn't approved for that class, I'll stop here and won't read the files.

Passwords, keys and access tokens can't go into any tool, so check the files for those whatever the answer.

Once you've answered, I'll read the files. Then I'll ask only what they leave open, such as the policy's version and date. I'll treat new starters, line managers and the night cleaning contractor as three separate runs with one draft each. Each draft goes to the reviewer named in the awareness prompt for checking and release. I won't send or publish anything.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

From BC policy (extract) v4, 20 January 2026 (approved by the board)
From awareness notes: Site C onboarding v1.1, 2 September 2026 (approved by the BCM manager)

## Draft: onboarding message for new starters at Site C

> **Welcome to Site C: what to do when something goes wrong**
>
> Welcome to Site C. This week we want you to know three things: how to report a disruption, who to report it to, and where to go when the alarm sounds.
>
> **1. Report it straight away.** If something disrupts work, or you think an incident may be starting, report it. Tell on-site security first, then your line manager.
>
> **2. Example.** "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100."
>
> **3. If the alarm sounds, get out.** Leave by the nearest exit. Go to the Site C muster point: **car park P2, by the weighbridge**.
>
> Questions about this message: [contact, for the reviewer to fill in]

**What I changed for this audience**
- I turned policy 3.1, 3.2 and 5.1 into "you" instructions in plain language. I didn't change the order: security first, then line manager.
- I put in the Site C muster point from the notes in place of "their site's muster point".
- I used the example exactly as the notes give it.
- I left out policy 4.1 (first-week timing) and 4.2 (release by the BCM manager). They're about how the message is sent, not what new starters do.

**Gaps**
1. **Mismatch, left unchanged:** Point 1 tells staff to report "to on-site security first", as policy 3.2 says. The notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." **For the reviewer:** who do Site C staff report to first? Is that the same by day and at night?
2. **Question:** The notes cover only night cover from Site A. Who covers by day is not in the sources.
3. **Question:** No contact list was attached, so I couldn't confirm that 040 555 0100 is current or answered at all hours. I also couldn't confirm that Hall 3 is a Site C hall; the notes don't say.
4. **Question:** The point 2 example tells staff to call the gatehouse, and point 1 tells them to report to security first. Do the two read as one instruction to a new starter?
5. **Language:** "Most Site C warehouse staff read German first; an English version is the current master." This draft is English only. Whether a German version is made, by whom, and how it's reviewed is not in the sources.
6. **Contact for questions:** Not in the sources. I left a placeholder.
7. **Approver:** Policy 4.2 says the BCM manager releases awareness material before anyone receives it.
8. No undated, replaced or draft sources. No passages addressed to an AI.

**Cite**
- Point 1: policy §3.1, §3.2 ("to on-site security first, then to their line manager")
- Point 2: awareness notes, bullet 2
- Point 3: policy §5.1; awareness notes, bullet 3 ("car park P2, by the weighbridge")

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Reviewer:** The BCM manager releases the message (policy 4.2). The manager who will answer staff questions about it checks it before that. They check accuracy, tone and local fit, decide each flagged mismatch (Gaps 1–6), and confirm the organisation stays the author. I haven't sent, published or saved anything.

**Line managers and the night cleaning contractor** are two separate runs, one draft each, from the same two sources. For the contractor, policy §3 and §4.1 speak of "employee", "staff" and "new starter". Whether they cover contractors is not in the sources, so that will go to the reviewer as a question. Shall I start with line managers?
