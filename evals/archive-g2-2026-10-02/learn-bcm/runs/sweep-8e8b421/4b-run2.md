# /learn-bcm case 4b, run2: Claude Code, guidance at 8e8b421

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `3a8f52b2-a191-4842-a582-9c8fd0d0c162`.

Files in the working folder: none.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# Business Impact Analysis (BIA)

A BIA works out **which activities matter most, how fast their disruption starts to hurt, and what it would take to get them running again.** It does not look at causes like fire, ransomware or flood. That's the risk assessment's job. The BIA asks: "If this stopped, for any reason, what happens?"

Its results set the recovery priorities and targets that continuity and disaster recovery (DR) plans are built on. Two standards cover it: ISO 22301 / ISO 22317 and NIST SP 800-34.

---

## The questions a BIA asks for each process

### 1. What do you do?
- Which **products and services** do you deliver, and which **processes or activities** support them?
- Who **owns** each process?
- Is the work **time-sensitive or seasonal**? Examples: payroll on the 25th, month-end close, peak retail season.

### 2. What happens if it stops? (Impact over time)
Impact is scored at **time intervals**, such as 1 hour, 4 hours, 1 day, 3 days, 1 week and 1 month, across several categories:

| Category | Example question |
|---|---|
| **Financial** | Lost revenue, penalties, extra costs? |
| **Legal / regulatory** | Missed obligations, fines, breach of contract? |
| **Reputational** | Media attention, loss of customer trust? |
| **Operational** | Knock-on effects on other processes? |
| **Health & safety / customer harm** | Can anyone be hurt? |

The idea is to watch impact **build up over time**. Then you look for the point where it becomes unacceptable.

### 3. How long can you survive? (The key metrics)
- **MTPD**, maximum tolerable period of disruption (also called **MAO**, maximum acceptable outage): how long before the damage becomes unacceptable or the organization can't survive it.
- **RTO**, recovery time objective: the target time to restore the activity. **It must be shorter than the MTPD** to leave a safety margin.
- **RPO**, recovery point objective: how much **data loss** you can tolerate, measured back in time. For example, "we can lose up to 15 minutes of transactions."
- **MBCO**, minimum business continuity objective: the **reduced level of service** that's acceptable during disruption. For example, "process 60% of orders" or "only priority customers."

### 4. What do you depend on? (Dependencies and resources)
- **People:** how many staff, which key skills, and is there a single point of failure, like "only Priya knows how to run this"?
- **IT systems and applications**, plus their data
- **Facilities and equipment**
- **Suppliers and third parties.** Do they have adequate continuity themselves?
- **Upstream and downstream processes:** who feeds you, and who relies on you?
- **Vital records:** documents and data needed to operate

### 5. What could you do in the meantime?
- Are there **workarounds or manual procedures**? How long can they last?
- How big a **backlog** builds up, and how long would it take to clear?

---

## What comes out of a BIA
- A **ranked list of prioritized activities**
- **MTPD, RTO, RPO and MBCO** for each one
- The **resource requirements** for recovery, over time
- A **dependency map**
- **Sign-off by senior management.** Leadership owns the risk appetite, not the analyst.

It's then **reviewed on a regular basis**, usually once a year, and after any major change.

---

## Quiz time 🎯

I'll ask one question at a time and give you feedback after each answer. There are 8 questions, mixing recall and scenarios.

**Question 1:**
How does a BIA differ from a risk assessment? In a sentence or two, what does each one focus on?

**Tool calls (stream-json):**

- none
