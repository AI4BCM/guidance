# learn-bcm baseline (no skill loaded), run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `c13ec1f6-c64d-42dd-b817-0d08a1f5e958`.

Files in the working folder: none.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

# Business Impact Analysis (BIA): what it asks for

A BIA is a core part of business continuity management (BCM), described in ISO 22301 and ISO/TS 22317. It answers one question: **if this activity stopped, how bad would it get, how fast, and what would we need to bring it back?**

It looks at **impact, not cause**. A BIA doesn't care whether the outage comes from a fire, a cyberattack or a pandemic. Threats and likelihood belong to the **risk assessment**, which is a separate exercise.

## 1. Activities in scope
- The **products and services** the organization delivers.
- The **processes and activities** that produce them, each with an owner.

## 2. Impact over time
For each activity, the BIA asks how bad the impact gets at set points in time, for example at 1 hour, 4 hours, 1 day, 3 days and 1 week. It rates several types of impact:
- **Financial:** lost revenue, penalties, extra costs
- **Operational:** backlog, knock-on effects on other teams
- **Legal / regulatory:** breached obligations, fines
- **Reputational / customer:** lost trust, complaints, customers leaving
- **Health, safety and environmental**

The reason for using time points is that impact usually grows over time. Sometimes it jumps suddenly, for example when a regulatory deadline passes.

## 3. The key time and data targets
| Term | Meaning |
|---|---|
| **MTPD / MAO** (Maximum Tolerable Period of Disruption / Maximum Acceptable Outage) | The point where the impact becomes unacceptable. Beyond it the organization's viability is threatened. |
| **RTO** (Recovery Time Objective) | The target time to resume the activity. It **must be shorter than the MTPD** to leave a safety margin. |
| **RPO** (Recovery Point Objective) | The most data loss you can tolerate, measured as time back to the last good copy. |
| **MBCO** (Minimum Business Continuity Objective) | The minimum level of service that is acceptable during a disruption, for example "50% of orders processed". |

## 4. Dependencies and resources
These are the things the activity needs to recover:
- **People:** minimum staff numbers, key skills, single points of knowledge
- **IT:** applications, systems, **data**
- **Facilities and equipment**
- **Suppliers and third parties**, and their own recovery capabilities
- **Internal dependencies:** which other activities it relies on (upstream) and which rely on it (downstream)

## 5. Context and workarounds
- **Peak periods and seasonality:** for example, payroll is critical at month-end.
- **Manual workarounds**, and how long each one can realistically be kept up.
- **Backlog:** how much work builds up during an outage and how long it takes to clear.

## 6. Outputs
- A **prioritized list of activities** with their RTO, RPO and MBCO.
- The **resource requirements** for recovery.
- These outputs feed the **risk assessment** and the choice of **continuity strategies**.
- Senior management **signs off** the BIA. It is reviewed at least once a year and whenever something significant changes.

---

# Quiz time 🎯

There are 8 questions, asked one at a time. I'll mark each answer and explain it before moving to the next.

**Question 1:** A BIA finds that the order-processing activity has an MTPD of 48 hours. The IT team proposes an RTO of 72 hours because it's cheaper. What's wrong with this proposal, and what would a sensible RTO look like?

**Tool calls (stream-json):**

- none
