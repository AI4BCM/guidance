# /challenge-my-plan on Claude Code: case 1v-internal

Date 2026-10-01. Claude Code 2.1.284, `claude -p --setting-sources project --plugin-dir /home/brain/work/ai4bcm-guidance-skills --permission-mode dontAsk --allowedTools Read,Glob,Grep`, stdin closed, scratch folder with the case files copied in; later turns with `--resume`. One run; no crash.

## Turn 1

**Request:**

> /challenge-my-plan The three files in this folder (option-paper-dispatch.md, bia-extract-dispatch.md, supplier-record-nordfrost.md) are attached. The steering group meets tomorrow.

**Reply** (session 82198c5a-c60a-421a-9388-25124695d95a, is_error False):

Before I open the three files, two things to settle.

**1. What class of data do these files hold, and is this environment approved for it?**

From the file names, they probably contain material the guidance rates as **high sensitivity** (`units/data-rules.md`, Sensitivity classes):
- **BIA extract:** "BIA data and risk assessment detail"
- **Supplier record (Nordfrost):** possibly "supplier weaknesses and contractual dependencies"
- **Option paper:** probably "recovery strategies and design assumptions". If it's going to the steering group, it may also count as board or executive-session material.

The guidance allows high-sensitivity material only in an **enterprise, private or purpose-built BCM environment** (`units/tools.md`, Selection guide, Analyse and Design rows). Please confirm:
- (a) the sensitivity class of each file, and
- (b) that this Claude Code session is an environment your organisation has approved for that class.

If it isn't approved, I'll stop here and won't read the files.

**2. Who reviews the output.** The **owner of the option paper** answers each question. A finding stays a question until they've answered it. Any risk the review turns up goes to the risk owner the files name, and I'll say so if they name none. Are you the owner of the dispatch option paper? If not, who is? If you answer on someone else's behalf, my recommendation on that question waits for the owner.

**What you'll get:** a draft in this chat, delivered in rounds of questions. I won't edit, send or publish anything. With the steering group meeting tomorrow, it's worth answering quickly so we get through at least one or two rounds before then.

## Turn 2

**Request:**

> Internal; this environment is approved for internal material only.

**Reply** (session 82198c5a-c60a-421a-9388-25124695d95a, is_error False):

I'm stopping here and haven't opened any of the three files.

**Why.** The guidance doesn't use an "internal" class; it rates material low, medium or high. "Internal" probably means medium. But the guidance names specific content as **high sensitivity, for an approved corporate or private environment only** (`units/data-rules.md`, Sensitivity classes). Going by their names, each file likely holds some of it:

| File | Matching item on the high list |
|---|---|
| `bia-extract-dispatch.md` | "BIA data and risk assessment detail" (a BIA extract is BIA data by definition) |
| `supplier-record-nordfrost.md` | "supplier weaknesses and contractual dependencies" |
| `option-paper-dispatch.md` | "recovery strategies and design assumptions"; maybe "board papers and executive-session material" if it goes to the steering group |

An environment approved for internal material only isn't approved for that list. And I can't open the files to check, because reading them is the step that puts the data into this environment.

**Ways forward:**

1. **Run the review in an environment approved for high-sensitivity material.** That means enterprise, private or a purpose-built BCM platform (`units/tools.md`, Selection guide, Analyse and Design rows). This is the cleanest option given tomorrow's meeting.
2. **Confirm that a file holds nothing from that list.** For example, a version of the option paper with the BIA figures, supplier detail and recovery design taken out. I'll review only the files you confirm, and the questions will stay within what they contain.
3. **Have your information security or data owner reclassify the files.** If they rate them internal or medium, tell me and I'll go ahead. That decision is theirs, not mine.

You also haven't said who owns the option paper. Whichever way you go, I need to know who answers the review questions.
