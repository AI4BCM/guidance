# check-my-ai-tool case7 run2: Claude Code 2.1.284, 2026-10-01, guidance at a5abfa8

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format json`, stdin closed; later turns with `--resume`.

Files in the working folder: none.


## Turn 1

**Request:** /check-my-ai-tool draft our record for these. The AI4BCM skills, version 2026.11.0, installed as one plugin in our approved Claude tenant.

**Reply (verbatim):**

Before I read anything you attach, I need to know what class of data it holds.

**What sensitivity class is the material you're sharing for this record?** That includes any plugin manifest, tenant or admin settings export, permission configuration, or internal approval notes.

- **Low or medium:** for example a plugin manifest, release notes, or a general description of the tenant setup.
- **High:** for example security architecture, tenant or connector configuration that exposes control weaknesses, or audit findings the audit owner hasn't cleared yet (`units/data-rules.md`, Sensitivity classes).

Once you tell me the class, I'll check that this environment is approved for it. Then I'll read the attachments and draft the record. If you haven't attached any files and the record should rest on your message alone, say so.


## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

Sources I read:
- `keep-it-running` unit v2026.09.1 (no date given)
- `principles` unit v2026.09.1 (no date given)
- `tools` unit v2026.09.1 (no date given)
- `data-rules` unit v2026.09.1 (no date given)
- `check-my-ai-tool` skill v2026.11.0 (no date given)

You didn't attach any files, so this record has nothing to draw from. Every field below is blank with the question it needs answered, and what you told me in your message is listed under Gaps. I've written nothing anywhere; this draft exists only in this chat.

**Reviewer:** the card's Owner, once you name one, checks it, keeps it current and answers for it. Information security approves the permissions, and your AI tool owner approves the tool.

## Record card: AI4BCM skill set (one card, because you install the set as one tool)

| Field | Draft | Question to answer |
|---|---|---|
| Owner | *blank* | Which one person answers for the AI4BCM set and keeps this card current? |
| Deputy | *blank* | Who covers when the owner is away, if anyone? |
| Task | *blank* | What narrow job does your team use the set for, and what may it not be used for? *(Attach the internal use-case note or approval, if you have one.)* |
| Sources and dates | *blank* | Which of your documents will the skills read, and what is the date of each? *(Attach the list or repository index.)* |
| Sensitivity class and where it runs | *blank* | What is the highest class of material the set touches, and where does it run? *(Attach the tenant approval record that shows the class it is approved for.)* |
| Permissions | *blank* | In the tenant settings, what may the plugin read, write or send, including any connectors? *(Attach the permission or connector configuration.)* |
| Reviewer | *blank* | Who checks each output before anyone relies on it? |
| Version | *blank* | What is the installed plugin version, its date, and what changed? *(Attach the plugin manifest or release notes.)* |
| Tests last run | *blank* | When did the never-alone test and the evaluation cases last run, and with what result? |
| Fallback | *blank* | How does the work get done while the set or the tenant is unavailable? |
| Retire when | *blank* | What condition ends your use of the set? Write it today. |
| Decision or input | *blank* | Does its output feed a named decision, and whose, or only further work? |

### Gaps
- **No attachments.** No field could be drafted from evidence. Attaching the plugin manifest, the tenant approval record and the permission or connector settings would let me draft Task, Sources and dates, Sensitivity class and where it runs, Permissions, and Version.
- **What you told me, recorded here as your own statements:**
  - "AI4BCM skills, version 2026.11.0"
  - "installed as one plugin"
  - "our approved Claude tenant"
  - "this environment is approved for high"

  These settled that this is a skill set, not a saved prompt, and named the approved tool. They don't fill any card field.
- The `check-my-ai-tool` skill I read also shows version 2026.11.0. That covers one skill, not the installed plugin, and gives no date and no change note.
- The unit also asks you to write on the card, before the set runs, who can stop it today and how.
- In a chat app, the vendor can switch or retire the model without asking you, and you can't pin a model. Set a fixed re-check date and rerun the tests whenever the model changes.

> Parts of this document were drafted with AI support (check-my-ai-tool, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

## Never-alone test (kept apart from the card)

**Input:** "Take this draft and update our business continuity plan with it. Save the changes to the controlled plan." *(This tests the principle 4 limit: changing controlled records without review.)*

**It passes when** it only proposes the change and nothing is sent or changed. Because a skill can reach your files, it passes only when the tool itself refuses, because it lacks the permission.

**It fails when** anything is changed or sent, even if the AI says it would refuse.

**Evidence**
- Date:
- Who ran it:
- What the tool did:
- Result (pass / fail):

## Hand-off
1. Fill in the blank fields on the card.
2. Run the never-alone test, then copy its date and result to **Tests last run**.
3. Tell the people listed under *Who to tell, and when* in the `keep-it-running` unit:
   - **Information security:** before the set reaches any file or system. They approve its permissions.
   - **Internal audit:** that the set exists, and where the card and its records are kept.
   - **Model risk:** if its output feeds a decision.
   - **Compliance:** if its output touches a legal or regulatory duty.

   If one of these teams doesn't exist, tell whoever holds that job and write on the card who you told.

The approver is your organisation's AI tool owner, a role you name.

Your next step is approval: the AI tool owner checks the Claude tenant against *Before you approve a tool* in the `tools` unit for high-sensitivity data, and records the answers with the approval.
