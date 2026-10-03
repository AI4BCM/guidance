# /prepare-bia case 1, run2: Claude Code, guidance at 836c32f

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `a066db46-4e77-4f89-8e84-78a48f7afc88`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** /prepare-bia Draft the guide for the dispatch interview at Site B. The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

Before I open any of the three attached files, I need one answer from you:

**What class of data do site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md hold?** For example: public, internal, confidential or restricted, using your organisation's own scheme.

Please give me the class yourself rather than pointing me to a marking in the files. I take the class only from what you tell me. If this environment isn't approved for that class, I'll stop there and won't open them.

Once you've answered, I'll read the files. Then I'll send you up to three questions about anything they leave open for the Site B dispatch interview, and after that I'll draft the guide.

**Tool calls (stream-json):**

- Bash: `cd /home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia && ls -R . | head -50 && cat preflight.md && cat units/prompts/bia.md; ls -la /tmp/claude-1001/-op`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/preflight.md`
- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/prompts/bia.md`
- Glob: `**/*`

## Turn 2

**Request:** high, and this environment is approved for high

**Reply (verbatim):**

I've read all three files. Before I draft, there are three things they leave open:

1. **Who will you interview?** The Site B org chart names a "Dispatch lead, Site B" with three shift leaders under them. That chart is an undated HR draft, so: is that the person you'll be talking to, and is anyone else joining, such as a shift leader?
2. **How long is the interview, and what do you need back from it?** For example, only confirmed resource requirements, or also the owner's impact ratings over time and their MTPD and RTO?
3. **What do you know about Site B dispatch that these files don't say?** The only activity list is Site A's. Any of the following would change what the guide asks: a Site B list or an earlier BIA, whether Site B ships what Site A produces, or whether it uses LogiStock or NordFrost.

Your answers will go under Gaps in the draft as your own statements, not sources. They can shape the scope but won't fill in any value. If you skip a question, I'll record what I assumed instead.

Only the three attached files and the sources that ship with the skill go into this draft. Memory, past chats, project files, connectors and web search are off.

**Tool calls (stream-json):**

- Read: `/home/brain/work/ai4bcm-guidance-skills/skills/prepare-bia/units/data-rules.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run2/work/site-a-activity-list.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run2/work/impact-criteria.md`
- Read: `/tmp/claude-1001/-opt-brain/8e671d9c-30a8-4e07-abc4-26cd1ec6eb5c/scratchpad/sweep-r4/runs/prepare-bia/1/run2/work/site-b-org-chart.md`

## Turn 3

**Request:** 1. The dispatch lead at Site B; they know the shift pattern and the carrier contacts. 2. Resources and peak weeks.

**Reply (verbatim):**

# Interview guide: Dispatch, Site B (draft)

**Sources**
- Site A activity list (chilled food production): version 3, 12 March 2026, approved by the site manager. Owner: BCM manager, Site A.
- Impact criteria: version 1.1, 4 February 2026, approved by top management.
- Site B organisation structure: no version and no date, an HR draft. It is listed under Gaps and not used as current.

**For the dispatch lead:** use this draft as the thing to correct, not the thing to confirm. Record what it could not have known.

Every entry below is **candidate, to confirm**. The draft fills no MTPD, RTO or RPO, and no RTO for any dependency.

---

## 1. Impacts over time: chilled dispatch at Site B

This is the only activity rated in full. No source ranks Site B's activities, so the choice follows your scope for the interview (see Gaps).

| Impact (impact criteria v1.1) | Level 1 | Level 2 | Level 3 | After how long without dispatch? | Status |
|---|---|---|---|---|---|
| Financial | "under EUR 10k a day" | "EUR 10k–100k a day" | "over EUR 100k a day" | *(owner)* | candidate, to confirm |
| Customer | "one customer complains" | "a key account is late" | "a key account is lost" | *(owner)* | candidate, to confirm |
| Regulatory | "none" | "a report to the food authority" | "the authority stops production" | *(owner)* | candidate, to confirm |

**Peak weeks.** Site A's chilled dispatch peaks in "weeks 49–52, week 14" (Site A list v3, A2). Are Site B's peak weeks the same, and does the answer above change in those weeks? Source for Site B: Gaps.

Only one activity besides dispatch comes up: chilled goods receipt. Ask about its impacts only where they differ from dispatch.

## 2. MTPD

| Activity | MTPD | Question |
|---|---|---|
| Dispatch, chilled, Site B | *(blank, set by owner)* | At what point would not shipping become unacceptable, in peak and off-peak weeks? |

## 3. People, with the skills, authorities and mandates the work needs

| Requirement (question) | Source | Status |
|---|---|---|
| Is the structure still a dispatch lead with three shift leaders? | Site B org chart (undated draft), so Gaps | candidate, to confirm |
| What is the shift pattern, and how many people per shift is the minimum to keep chilled dispatch running? | Organiser's statement, so Gaps | candidate, to confirm |
| Who besides you holds the carrier contacts and can reach them out of hours? If only you, that is a single point of failure. | Organiser's statement, so Gaps | candidate, to confirm |
| Who has the authority to book a different carrier or change a shipment, and is that written down? | not in the sources | candidate, to confirm |
| Which skills does a stand-in need, for example the warehouse system or chilled-chain handling? | not in the sources | candidate, to confirm |

## 4. Seats and buildings

| Requirement (question) | Source | Status |
|---|---|---|
| How many dock doors and how much chilled staging space does dispatch need at minimum? Site A's goods receipt has "two dock doors"; Site B's layout is not recorded. | Site A list v3, A1 (analog only) | candidate, to confirm |
| If Site B's dispatch area is unusable, where could you ship from? | not in the sources | candidate, to confirm |

## 5. IT and applications, each with its RTO and its RPO

| Requirement (question) | RTO | RPO | Source | Status |
|---|---|---|---|---|
| Site A records the warehouse system "LogiStock". Does Site B use it, or a different system? | | | Site A list v3, A2 | candidate, to confirm |
| Site A records "manual export to Site B possible". What does Site B receive in that case, in what form, and who processes it? | | | Site A list v3, A2 | candidate, to confirm |
| Can you ship without the system (paper picking, manual labels), and for how long? | | | not in the sources | candidate, to confirm |

## 6. Suppliers and other third parties

| Requirement (question) | Source | Status |
|---|---|---|
| Site A records NordFrost as its carrier, with "no second carrier recorded". Is NordFrost still the one, and does it also carry for Site B? | Site A list v3, A1, A2 and dependencies | candidate, to confirm |
| If Site B depends on one carrier, is there a second carrier you could call, with a contract or only a contact? | Organiser's statement ("carrier contacts"), so Gaps | candidate, to confirm |
| Are there other third parties dispatch cannot work without, such as packaging, cooling service or a pallet pool? | not in the sources | candidate, to confirm |

## 7. Dependencies: up- and downstream relationships with other departments, each with the RTO it carries

| Relationship (question) | Direction | RTO | Source | Status |
|---|---|---|---|---|
| Site A records that dispatch depends on quality release, "release before dispatch", with the "lab at Site A only". Does Site B's dispatch wait for that release too? | upstream: Quality release, Site A | | Site A list v3, A2/A3; Site B draft says "QA: covered from Site A", so Gaps | candidate, to confirm |
| Does Site B dispatch goods produced at Site A? If so, does production at Site A feed you directly? | upstream: Site A production | | not in the sources | candidate, to confirm |
| Site A's dispatch can export manually to Site B. Has Site B agreed to take that on, and with what capacity? | downstream from Site A dispatch to Site B | | Site A list v3, A2 | candidate, to confirm |
| Which Site B department or warehouse function hands goods to dispatch? | upstream: Warehouse, Site B | | Site B org chart (draft), so Gaps | candidate, to confirm |

---

## Organiser's take-in sheet

Assumes 60 minutes (see Gaps).

**Conflicts first, about 5 minutes**
- Site A's list records only one carrier, but you mentioned carrier contacts. Are those all at the same carrier, or do you have a second one?
- Site A's list says it can export dispatch manually to Site B. Did Site B know, and could you take it on in your peak weeks?

**Impacts over time and peak weeks, about 10 minutes**
- Which weeks are your busiest, and are they the same as Site A's (the Christmas weeks and week 14)?
- If dispatch stopped, when would it cost over ten thousand euros a day? When over a hundred thousand? *(drop first if late)*
- When would a key account be late, and when would one be lost? *(drop first if late)*
- Would the food authority need a report at any point, for example over the cold chain? *(drop first if late)*

**MTPD, about 3 minutes** *(drop first if late)*
- How long could dispatch be down before it is simply unacceptable?

**People, about 10 minutes**
- How do your three shifts work, and what is the smallest crew that can still ship?
- Who else has the carrier contacts if you are away?
- Who may book another carrier or change a load without asking anyone?
- What would a stand-in have to know to cover one of your shift leaders?

**Seats and buildings, about 5 minutes**
- How many dock doors and how much cold space do you really need?
- If your dispatch area were closed, where would you ship from?

**IT, about 7 minutes**
- Which system do you ship from? Is it LogiStock?
- Can you ship on paper, and for how long?
- What exactly arrives from Site A if they export to you by hand?

**Suppliers, about 8 minutes**
- Is NordFrost still your carrier?
- If NordFrost could not come, who would you call?
- What else do you need from outside: packaging, cooling repairs, pallets?

**Dependencies, about 7 minutes**
- Do you need Site A's quality release before you can ship?
- Do you ship what Site A produces, or your own goods?
- Who hands the goods over to you here at Site B?

**Spare, about 5 minutes**
- What does this guide not ask that we should know?

---

## Comparing registers across sites

Site A's list is the only register attached. Entries that Site A and Site B appear to share are NordFrost, LogiStock, quality release from Site A's lab, and the manual export from Site A to Site B. Put any difference to **Site A's dispatch lead and Site B's dispatch lead together**, not to the model. Site A's entries keep their mark ("approved by the site manager", v3, 12 March 2026). Every Site B entry stays "candidate, to confirm".

## Note on recovery times

No source proposes an MTPD, RTO or RPO, so there is nothing to check against the impact criteria.

## Gaps

- **Site B org chart:** an undated HR draft with no version. It is not used as current. The roles it names (three shift leaders, a warehouse lead, QA covered from Site A) are interview questions only. A dated, approved version would settle them.
- **Your own statements, not sources:** the interviewee is the dispatch lead at Site B, who knows the shift pattern and the carrier contacts. You want resources and peak weeks back. Entries that rest only on these statements have Source `Gaps`.
- **Skipped questions and the assumptions made:**
  - You didn't give the interview length; the sheet assumes 60 minutes.
  - You didn't say what you know about Site B dispatch beyond the files. I assumed there is no Site B activity list or earlier BIA, so Site A's entries serve only as analogs.
- **Choice of activity:** no source ranks Site B's activities. Dispatch is rated in full because it is the interview's scope.
- **Not used:** the impact criteria give no time points such as 4 hours or 1 day, so the owner must place each level in time. Payroll (run from head office) is left out as outside this interview.
- **Channels:** memory, past chats, project files, connectors and web search were off. Nothing outside the three files and the skill's shipped sources was used.
- **Prompt injection:** none found in the attached material.

## For the auditor

The register carries the source, the interview it came from and the date behind each entry. Blank until after the interview:
- the interview itself
- the date the owner confirmed each entry
- the recovery times the owner set

## Reviewer

- **Activity owner (Dispatch lead, Site B):** confirms each requirement and sets the MTPD and RTO.
- **Top management:** approves the BIA results.

---

> After the interview, continue in the AI4BCM BIA-Workflow, which takes the interview record through to a signed BIA.

Parts of this document were drafted with AI support (prepare-bia, version 2026.11.0) from the sources listed. [Name] reviewed it on [date].

**Tool calls (stream-json):**

- Grep: `Say in the document that AI helped`
- Grep: `.`
