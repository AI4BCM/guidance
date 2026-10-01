# /learn-bcm case 4b, run1: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `51d620d0-c233-42cc-af4b-26efa6ed7f12`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# Business Impact Analysis (BIA)

A BIA answers one question: **if this business activity stopped, how bad would it get, how fast, and what would we need to get it running again?**

It does not ask *why* the activity stopped. Fire, ransomware and a supplier going bust are all treated the same way. Looking at causes and likelihood is the job of the **risk assessment**, which is a separate exercise. A BIA looks only at the consequences of a disruption.

## What a BIA asks for

**1. Processes and activities**
- What does this team or department do?
- Who owns each activity?
- Which products or services does it support?

**2. Impact over time**
For each activity, you ask what happens if it is down for 1 hour, 4 hours, 1 day, 3 days, 1 week and so on. You rate the impact in several categories:
- Financial (lost revenue, penalties, extra costs)
- Operational
- Legal and regulatory (breaching a contract or a law)
- Reputational
- Customer impact
- Health and safety

The point of using time buckets is that impacts usually get worse the longer the outage lasts. The BIA finds the moment when the damage becomes unacceptable.

**3. Recovery time metrics**

| Term | Question it answers |
|---|---|
| **MTPD / MAO** (Maximum Tolerable Period of Disruption / Maximum Acceptable Outage) | After how long does the damage become unacceptable or permanent? |
| **RTO** (Recovery Time Objective) | By when must the activity be running again? It must be **shorter than the MTPD** so there is a safety margin. |
| **RPO** (Recovery Point Objective) | How much data can we afford to lose, measured in time? An RPO of 4 hours means backups must be no more than 4 hours old. |
| **MBCO** (Minimum Business Continuity Objective) | What is the minimum level of service that is acceptable while we recover? For example, 50% of normal volume. |

Some frameworks also use **WRT (Work Recovery Time)**, which is the time needed after systems come back to verify data and catch up on backlog. In that model, **MTD = RTO + WRT**.

**4. Dependencies and resources**
What the activity needs in order to run:
- **People:** how many staff, which key skills, and any single points of failure (one person nobody else can cover for)
- **IT:** applications, systems and data
- **Facilities and equipment**
- **Third parties:** suppliers and outsourced services
- **Vital records:** critical documents and files
- **Internal dependencies:** which activities feed into this one (upstream) and which rely on it (downstream)

**5. Context**
- Peak periods, such as month-end or seasonal spikes
- Manual workarounds, and how long they can be kept up
- Resources needed over time, for example 2 staff on day 1 and 10 by day 5

## What comes out of it
- A **prioritized list of critical activities**, ranked by their RTOs
- **Recovery requirements** for each activity (RTO, RPO, resources, dependencies)
- The input to **continuity strategy and plan design**. The BIA tells you *what* to protect and *how fast* to restore it. The strategy then decides *how*.

---

# Quiz time

I'll ask one question at a time, check your answer, then move on. There are 8 questions, ranging from basic to scenario-based.

**Question 1:** What's the key difference between a BIA and a risk assessment?

**Tool calls (stream-json):**

- none
