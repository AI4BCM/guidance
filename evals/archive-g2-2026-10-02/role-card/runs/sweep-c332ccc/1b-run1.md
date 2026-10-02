# /role-card case 1b, run1: Claude Code, guidance at c332ccc

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `6d89539e-1683-489e-9b65-509aaf991da4`.

Files in the working folder: `awareness-notes-site-c.md`, `bc-policy-extract.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /role-card Write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. The files bc-policy-extract.md and awareness-notes-site-c.md in this folder are attached.

**Reply (verbatim):**

Before I open `bc-policy-extract.md` or `awareness-notes-site-c.md`, I need one answer from you.

**What class of data do these two files hold, and is this environment approved for it?**

- **Medium sensitivity:** approved policy and awareness content with no personal details. Onboarding and awareness drafting fits here, and it needs an enterprise environment working from approved sources.
- **High sensitivity:** the files include personal data or contact lists (for example named people's phone numbers), security or site layout details, vulnerabilities, supplier weaknesses or contract dependencies, or live incident information. This needs an approved corporate or private environment only.

Please tell me the class and confirm this environment is approved for it. If it isn't, I'll stop here, and the files can be brought into an approved tool instead. If either file contains passwords, keys or access codes (door or alarm codes, for example), take them out first, because they shouldn't go into any tool.

Once you've answered, I'll read both files and ask only about what they leave open. That's likely to be the approved version and date, and the format for each group: a staff message or a role card. I'll handle new starters, line managers and the night cleaning contractor as three separate drafts.

## Turn 2

**Request:** medium, and this environment is approved for medium

**Reply (verbatim):**

From BC policy v4, 20 January 2026 (approved by the board)
From awareness notes: Site C onboarding v1.1, 2 September 2026 (approved by the BCM manager)

**Staff message for new starters at Site C (draft, not released)**

---

**Welcome to Site C: what to do if something goes wrong**

In your first week, take a few minutes to learn three things. *(Policy §4.1)*

**1. Report a disruption: know how, and who to tell.**
If you think something is going wrong, report it to "on-site security first, then to [your] line manager." *(Policy §3.1, §3.2)*

For example: "If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100." *(Awareness notes, Site C, example line)*

**2. If the alarm sounds, get out and gather.**
Leave by the nearest exit and go to the Site C muster point: "car park P2, by the weighbridge." *(Policy §5.1; awareness notes, Site C, muster point)*

**3. Ask if you're unsure.**
Your line manager can tell you more. *(Policy §3.2)*

---

**What I changed for new starters at Site C**
- I turned the policy wording into three short, numbered actions in the second person.
- I put the Site C muster point in place of "their site's muster point" in §5.1, using the approved notes.
- I used the example the notes give for the onboarding message, word for word.
- I left out policy §4.2 (the release rule). It's an instruction for the BCM manager, not for new starters.
- Point 3 adds no new content. It points back to the line manager named in §3.2. Remove it if the reviewer thinks it adds too much.

**Gaps (left unchanged in the draft for the reviewer to decide)**
1. **There's no on-site security team at Site C.** Policy §3.2 says to report "to on-site security first", but the notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." I've kept the policy wording. The reviewer needs to decide who Site C staff report to first, by day and by night. That decision belongs to the policy owner (the BCM manager), not to this draft.
2. **The example names another site.** The example line sends staff to "the Site A gatehouse". The notes only describe Site A as *night* cover. Does that number apply during the day as well?
3. **Is the number current?** I don't have a contact list to check 040 555 0100 against. Does someone answer it now, at all hours?
4. **Which alarm?** The example is about a chiller alarm, while policy §5.1 is about evacuation "on the alarm". Should a Hall 3 chiller alarm mean evacuating, calling Site A, or both? The two lines next to each other could confuse a new starter. Not in the sources.
5. **Language.** "Most Site C warehouse staff read German first; an English version is the current master." This draft is in English, and no German version exists. Is a German version needed, who translates it, and who checks the translation?
6. **Timing.** Site C "joins the group's onboarding in October". The sources don't say whether people who started at Site C between 1 July and October will also receive this message.

**Reviewer:** before this goes out, the manager who will answer new starters' questions at Site C checks it for accuracy, tone and local fit, and decides each gap above. The BCM manager then releases it, because policy §4.2 says awareness material "is released by the BCM manager before anyone receives it." I haven't sent, published or changed anything.

Parts of this document were drafted with AI support (/role-card, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next: line managers and the night cleaning contractor** are two separate runs, one per audience. Before I draft them, I need two things:

1. **Format for each.** A staff message (as above) or a role card? A role card has to be built from an approved *plan*, and I only have the policy extract and the awareness notes. So unless you attach a plan with its version and date, both will be staff messages.
2. **Does the policy cover the contractor?** Policy §3.1 covers "every employee", and neither source mentions contractors. Should I still use the policy for the night cleaning contractor's message, with this listed as a gap for the BCM manager? Or is there a separate approved document, such as a contractor induction or site rules, that you can attach?
