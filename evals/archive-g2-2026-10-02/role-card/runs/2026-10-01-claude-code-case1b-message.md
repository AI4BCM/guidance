# role-card case1b-message, Claude Code 2.1.284, 2026-10-01

Files in the run folder: bc-policy-extract.md, awareness-notes-site-c.md. Command: `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, later turns with `--resume`.

## Turn 1

Session `17e1cf53-fa2b-42b6-a5bd-25daea9bb43a`. Request:

```text
/role-card write the onboarding message for new starters at Site C. We also need versions for line managers and for the night cleaning contractor. Attached: bc-policy-extract.md, awareness-notes-site-c.md
```

Final text:

````markdown
Before I open either attachment I need a few answers. I'll ask them all at once.

**First, the data class (I need this before I read anything).** What class of data do `bc-policy-extract.md` and `awareness-notes-site-c.md` hold? In particular, do they include any of these: contact lists or personal data, site security detail, recovery strategies, supplier or contractual dependencies, or audit findings not yet cleared? If they do, they're high-sensitivity and can only be used in an approved corporate or private environment. Please confirm this environment is approved for that class. If it isn't, I'll stop here.

**Then three intake questions:**

1. **The source document.** Which approved BC policy is `bc-policy-extract.md` taken from, and what are its version, approval date and status (approved, draft or proposed)? Do the awareness notes for Site C have a version or date? I'll put these as the first line of the message, for example "from BC policy v4, approved 12 Mar". Anything undated or not yet approved will be listed under Gaps and not treated as current.
2. **The format.** I'm treating the "onboarding message" as a staff message under the awareness prompt. Which channel is it for: a welcome email, an intranet page, or a handout in the induction pack? This sets the length and layout.
3. **Who approves it.** Who is the manager at Site C who will answer new starters' questions about this message? They review it before it goes out. If the policy names an approver, I'll use that person.

**Scope.** This run covers one audience: new starters at Site C. The line managers' version and the night cleaning contractor's version will each be a separate run after this one. The contractor isn't staff, so on that run I'll check whether the policy covers contractors at all, and flag it if it doesn't.

**What you get.** You'll get a draft in this chat. I won't send, publish or save anything. Before anything is published, the manager who will answer questions about the message checks its accuracy, tone and fit for Site C. They also decide every mismatch I flag, such as a retired phone number or an example taken from another site. I'll flag those and leave the policy wording as it is.
````

## Turn 2

Session `17e1cf53-fa2b-42b6-a5bd-25daea9bb43a`. Request:

```text
Data class: medium, and this environment is approved for medium. 1. The versions and status are in the files. 2. A staff message, for the onboarding e-mail. 3. Skip.
```

Final text:

````markdown
**Draft: Site C new-starter onboarding e-mail**

---

from BC policy v4, approved by the board 20 Jan 2026 · with Site C awareness notes v1.1, approved by the BCM manager 2 Sep 2026

**Subject: Welcome to Site C: what to do if something goes wrong**

Welcome to Site C. In your first week, we ask everyone to learn three things that help keep the site running and keep people safe when something goes wrong. [policy 4.1]

**1. Know how to report a disruption, and who to report it to**
If something stops work or looks like it could become an incident (a breakdown, an alarm, a power cut), you need to know who to tell. [policy 3.1]
"Staff report a suspected incident to on-site security first, then to their line manager." [policy 3.2]

**2. An example from Site C**
"If the Hall 3 chiller alarm sounds, call the Site A gatehouse on 040 555 0100." [awareness notes, example]

**3. If the alarm sounds, leave the building**
"On the alarm, staff leave by the nearest exit and gather at their site's muster point." [policy 5.1]
At Site C, the muster point is **car park P2, by the weighbridge**. [awareness notes]

If you have questions about any of this, please ask [name of the manager who will answer questions].

---

**What I changed for this audience**
- I gave the e-mail a subject line and a welcome, and put the policy points in the order a new starter needs them.
- I added a short plain-language explanation of "disruption" to point 1. The examples in brackets are illustrations and are not in the sources. The reviewer may remove them.
- I put the Site C muster point next to the policy's evacuation rule.
- I quoted 3.2, 5.1 and the example exactly as the sources have them, because each one has a fit question below.
- I left out policy 4.2 (who releases the material). It is an instruction to the BCM manager, not to new starters.

**Gaps**
1. **Mismatch: no on-site security at Site C.** Policy 3.2 says to report "to on-site security first". The awareness notes say "Site C has no on-site security team. Night cover is by remote monitoring from Site A." I have left 3.2 unchanged in the draft. The reviewer needs to decide who a Site C new starter reports to first, by day and at night.
2. **Mismatch: the example names another site.** The example sends staff to the "Site A gatehouse". The notes only say Site A covers Site C at night, by remote monitoring. They do not say whether Site A also covers the day shift, whether the Site A gatehouse is the remote monitoring point, or whether 040 555 0100 is a current number. The sources have no contact list to check it against. I have left the example unchanged. Question for the reviewer: is this the right first call for a Site C new starter at any hour?
3. **Question: language.** The notes say most Site C warehouse staff read German first and the English version is the master. The policy doesn't say whether a German translation is needed or who approves one ("not in the sources"). Question for the reviewer: should a German version go out alongside this one, and if so, who checks it against the English master?
4. **Line manager.** Point 1 tells new starters to report to their line manager, but the sources don't say how a new starter finds out who that is ("not in the sources"). Question for the reviewer: should the e-mail name the line manager, or leave a placeholder for it?
5. **Who answers questions.** The awareness prompt requires the manager who will answer new starters' questions to check this draft. Neither source names that person, so the closing line has a placeholder.
6. **Timing.** Policy 4.1 requires the material in the first week. Site C "joins the group's onboarding in October". I haven't checked whether anyone has already started without receiving it.

**Review and release.** You asked to skip naming a reviewer. You don't need to name anyone now, but the review step stays in place. Policy 4.2 says "Awareness material is released by the BCM manager before anyone receives it." Before release, the manager who will answer questions checks this e-mail for accuracy, tone and fit for Site C, and decides each mismatch in Gaps 1–4. I haven't sent, published or saved anything.

Parts of this document were drafted with AI support (role-card skill, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Next runs.** The line managers' message and the night cleaning contractor's message are separate runs. Run `/ai4bcm-guidance:role-card` again for each one. For the contractor, the first question will be whether policy v4 covers contractors at all: sections 3 and 5 refer only to "employee" and "staff".
````
