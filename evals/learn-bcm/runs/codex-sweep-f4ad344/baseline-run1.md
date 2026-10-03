# learn-bcm baseline (no skill loaded), run1: Codex, guidance at f4ad344

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with no `.agents/skills/` (no AI4BCM package). Every agent message of a turn is kept, in order. One driver. Session `01a1011c-f541-7ec0-a38a-6fe45091f8d3`.

Files in the working folder: none.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Can you teach me what a BIA asks for and then quiz me on it?

**Reply (verbatim):**

A **Business Impact Analysis (BIA)** asks: **If an important business activity stops, what happens, how quickly does that become unacceptable, and what do we need to restore it?**

In business continuity planning, a BIA usually asks for:

- **Activities and outputs:** What does your team do, and who relies on it?
- **Impacts over time:** What would a disruption cause after a few hours, a day, or a week? Consider financial loss, customer harm, legal obligations, safety, and reputation.
- **Maximum tolerable disruption:** How long can the activity be interrupted before the consequences become unacceptable?
- **Recovery requirements:** How quickly should it resume, and what minimum level of service is needed? The target recovery time is called the **Recovery Time Objective (RTO)** and should fall within the tolerable disruption period.
- **Data recovery needs:** How much recent data could you afford to lose? The **Recovery Point Objective (RPO)** expresses this as time—for example, losing at most one hour of records.
- **Dependencies and resources:** Which people, systems, records, premises, suppliers, and other teams are needed to operate or recover?
- **Timing and workarounds:** Are there critical deadlines or peak periods? Could a temporary manual process help, and for how long?

For example, a payroll BIA might find that a disruption becomes serious near payday, payroll needs access to employee records and its banking provider, and a limited manual process could cover urgent payments.

A useful distinction: **a risk assessment asks what might cause a disruption and how likely it is; a BIA asks what the disruption would mean for the business.**

Let’s quiz you one question at a time. I’ll give feedback after each answer.

**Question 1:** A team says, “Our service is critical, so we need it back immediately.” What would you ask them to establish whether that recovery requirement is justified?

**Tool calls (JSON events):**

- none
