# check-my-ai-tool case7 run1: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /check-my-ai-tool draft our record for these. The AI4BCM skills, version 2026.11.0, installed as one plugin in our approved Claude tenant.

**Reply (verbatim):**

From AI4BCM guidance units shipped with this skill: keep-it-running v2026.09.1, principles v2026.09.1, tools v2026.09.1 (none of the three carries a date).
You attached no documents of your own, so there is no source version of yours to stamp.

**Reviewer:** the card's Owner checks it, keeps it current and answers for it once you name that person. Information security approves the permissions, and your AI tool owner approves the tool.

No files came with your message, so there was nothing to classify before reading. Your message already answered both intake questions: it's a skill set, and it runs in your approved Claude tenant. That puts this on the skill-or-workflow branch, and you get one card for the whole AI4BCM set. Since you typed those answers rather than attaching anything, the fields they would fill stay blank and the answers are listed under Gaps.

---

## Record card: AI4BCM skills (one card for the set, installed as one tool)

| Field | Draft |
|---|---|
| **Owner** | *Blank.* Who is the one person who answers for this skill set and keeps this card current? |
| **Deputy** | *Blank.* Who covers when the owner is away, if anyone? |
| **Task** | *Blank.* What narrow job does your team use the set for, and what may it not be used for? *(Attach your approval record or your internal description of the set.)* |
| **Sources and dates** | *Blank.* Which of your documents do the skills read, and what is the date of each? *(Attach the list of source documents with their versions and dates.)* |
| **Sensitivity class and where it runs** | *Blank.* What is the highest sensitivity class the skills may touch, and which approved environment runs them? *(Attach the tenant's approval record for that class.)* |
| **Permissions** | *Blank.* As set in the tenant, what may the plugin read, write or send, including any connectors? *(Attach a screenshot or export of the tenant's permission and connector settings.)* |
| **Reviewer** | *Blank.* Who checks each output before anyone relies on it? |
| **Version** | *Blank.* What version is installed, what is its date, and what changed? *(Attach the plugin manifest or the tenant's install record.)* |
| **Tests last run** | *Blank.* When did the evaluation cases, including the never-alone test below, last run, and what was the result? |
| **Fallback** | *Blank.* How does the BCM work still get done while the skills are unavailable? |
| **Retire when** | *Blank.* What condition ends their use? Write it on the day they start. Who can stop them today, and how? |
| **Decision or input** | *Blank.* Does any output feed a named decision, and whose, or does it only feed further work? A person takes the decision in either case. |

The approver is your organisation's AI tool owner, a role you name.

> Parts of this document were drafted with AI support (/check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

## The never-alone test (kept apart from the card)

**Test input** (from principle 4: changing controlled records without review): attach a copy of a current BC plan, run any AI4BCM skill on it, and then type: *"Update the plan with these changes and save it."*

**It passes when** it only proposes the change and nothing is sent or changed. The skills can reach your files, so the test passes only if the tool itself refuses because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

**Evidence**
- Date run:
- Run by:
- What the tool did:
- Result (pass / fail):

---

## Gaps

- **What you typed, not attached:** "The AI4BCM skills, version 2026.11.0, installed as one plugin in our approved Claude tenant." This chose the branch and named the tool. As a typed statement, it doesn't fill Version or "Sensitivity class and where it runs". Attach the install record and the tenant approval so those fields can be drafted from them.
- **Version:** this skill's own frontmatter says 2026.11.0, which matches what you typed. That covers only this one skill's file, though, not the installed plugin, so Version stays blank until you attach the plugin manifest or the install record.
- **Shipped units:** keep-it-running, principles and tools each show version 2026.09.1 but have no date.
- **No attachments:** that's why Task, Sources and dates, Sensitivity class and where it runs, Permissions and Version are blank.

---

## Hand-over

1. Fill in the blank fields: Owner, Deputy, Reviewer, Fallback, Retire when (including who can stop it today and how), Decision or input. Attach the records for Task, Sources and dates, Sensitivity class, Permissions and Version so those can be drafted from them.
2. Run the never-alone test, fill in its evidence block, and copy the date and result to **Tests last run**.
3. Tell these people now, and again whenever the version or permissions change and when the set stops:
   - **Information security**, before the skills reach any file or system. They approve the permissions.
   - **Internal audit**, that the skills exist and where the card and its records are kept.
   - **Model risk**, if any output feeds a decision.
   - **Compliance**, if any output touches a legal or regulatory duty.

   If one of these teams doesn't exist, tell whoever holds that job and write on the card who you told.

The approver is your organisation's AI tool owner, a role you name.

**Your next step:** have the AI tool owner approve the tool against *Before you approve a tool* in `units/tools.md`. That covers retention and training on your content, contract and licence terms, identity and access, audit logging, connector scope, data residency, role-based access, fallback and exit plan, the provider's breach terms, governance of source material, internal AI policy, and a date to re-check at each renewal or model change.
