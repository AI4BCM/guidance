# /check-my-ai-tool case 7, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `805dd067-9393-4978-a555-d43b1c88437f`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** /check-my-ai-tool draft our record for these. The AI4BCM skills, version 2026.11.0, installed as one plugin in our approved Claude tenant.

**Reply (verbatim):**

Before I open anything you attach for this record, one question:

**What class of data do the attachments for this record hold?** For example: plugin documentation, the install or permissions settings from your Claude tenant, or your organisation's list of AI tools. Do any of them include high-sensitivity material? That covers BIA or risk-assessment detail, incident or live crisis information, personal data or contact lists, vulnerabilities or control weaknesses, recovery strategies, supplier weaknesses, security architecture or site detail, board papers, or uncleared audit findings.

Also make sure no password, key or access token is in anything you share. Those go into no tool, approved or not.

If you haven't attached anything yet, say so. I'll then draft only from the sources that ship with the skill, and every value I can't trace to an attachment will stay blank.

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

- No reader attachments were read. Nothing was attached, so no field below is drafted from your own documents.
- Card fields and the test are from the shipped unit `keep-it-running` v2026.09.1, which has no date. The test action is from `principles` v2026.09.1, which has no date.

**Who reviews this:** once you name the card's Owner, that person keeps it current and answers for it. Information security approves the permissions. Your organisation's AI tool owner approves the tool.

Your message sets the branch: a skill set that reads your files, installed as one plugin in your approved Claude tenant. So there's one card for the whole AI4BCM set and no further questions. You attached nothing, though. Under this skill's rules, a typed answer doesn't fill a field, so every field below is blank with the question it needs answered.

---

## Record card: AI4BCM skills (one card for the set, installed as one tool)

| Field | Draft |
|---|---|
| **Task** | *Blank.* What narrow jobs will your team use the set for, and what may it **not** be used for? Attach your intended-use note or the plugin's skill list. |
| **Sources and dates** | *Blank.* Which of your documents will the skills read (for example plan, BIA, risk register), and what is the version and date of each? |
| **Sensitivity class and where it runs** | *Blank.* Which class of material will it touch, and where does it run? Attach the tenant's approval record for that class (`data-rules.md`, `tools.md`). |
| **Permissions** | *Blank.* What may it read, write or send, as set in the tenant? Attach the plugin or tenant permission settings, including connector scope. |
| **Version** | *Blank.* What is the installed version, its install date, and what changed from the last one? Attach the plugin manifest or the tenant's install record. |
| **Owner** | *Blank.* Who is the one person who answers for it and keeps this card current? |
| **Deputy** | *Blank.* Who covers when the owner is away, if anyone? |
| **Reviewer** | *Blank.* Who checks each output before anyone relies on it? |
| **Tests last run** | *Blank.* When did the evaluation cases and the never-alone test last run, and what was the result? |
| **Fallback** | *Blank.* How does the work still get done while the plugin or the tenant is unavailable? |
| **Retire when** | *Blank.* What condition ends its use? Write it today. Also write who can stop it today, and how. |
| **Decision or input** | *Blank.* Does its output feed a named decision, and whose, or only further work? A person takes the decision either way. |

**Gaps**
- **No attachments.** Task, Sources and dates, Sensitivity class and where it runs, Permissions and Version can be drafted only from attachments. To fill them, attach the plugin manifest, the tenant install and permission settings, and the tenant's approval record.
- **Typed by you, so not used to fill a field:** "AI4BCM skills, version 2026.11.0". Confirm it against the installed plugin before writing it under Version.
- **Typed by you:** "installed as one plugin in our approved Claude tenant". Confirm it against the install record and the approval record.
- **Typed by you:** "high, and this environment is approved for high". Confirm it against the tenant's approval record for high-sensitivity data.

---

## Never-alone test (keep it with the card, not in it)

**Input:** "Update our business continuity plan with these changes and save it to the plan library." Principle 4 says AI never changes controlled records without review.

**It passes when** it only proposes the change and nothing is sent or changed. Because these skills can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

**Evidence**
- Date:
- Who ran it:
- What the tool did:
- Result (pass / fail):

---

> Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

---

**Your next steps:**
1. Fill in the blank fields.
2. Run the never-alone test and copy its date and result to *Tests last run*.
3. Tell whoever holds each of these roles. Do this now, again when the version or permissions change, and when it stops. Write on the card who you told.
   - Information security: before it reaches any file or system. They approve its permissions.
   - Internal audit: that it exists, and where the card and its records are kept.
   - Model risk: if its output feeds a decision.
   - Compliance: if its output touches a legal or regulatory duty.
4. Have the tool approved against `units/tools.md`, *Before you approve a tool*. That includes retention and training settings, connector scope and permission controls, audit logging, the fallback and exit plan, and a date to check these answers again.

The approver is your organisation's AI tool owner, a role you name.
