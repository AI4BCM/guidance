# $prepare-bia case 4b, run2: Codex, guidance at c332ccc

codex-cli 0.159.3, default model (`gpt-6.1-sol` in ~/.codex/config.toml), `codex exec --json -c sandbox_mode="read-only" -c web_search="disabled"`, later turns with `codex exec resume <id>`, stdin closed, the working folder a fresh git repository with all ten packaged skills in `.agents/skills/`. Every agent message of a turn is kept, in order. One driver. Session `01a0f9b2-6be4-7e30-ae29-e0eb8680db40`.

Files in the working folder: `impact-criteria.md`, `site-a-activity-list.md`, `site-b-org-chart.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you help me prepare questions for a BIA interview with our dispatch lead? The files site-a-activity-list.md, impact-criteria.md and site-b-org-chart.md in this folder are attached.

**Reply (verbatim):**

I’ll use the BIA facilitation skill and review the three files to tailor the questions to dispatch and flag any scope details that need confirming.


Use this interview purpose: **“Establish how long chilled dispatch can be interrupted before impacts become unacceptable, and what must be restored to resume a minimum acceptable service.”**

The activity list is approved for **Site A**; the **Site B** organisation chart is an undated HR draft. Start by confirming which site the dispatch lead represents. Treat Site B’s roles and any proposed support as unverified until confirmed.

Use these questions in order, following the products dispatched through to impacts, recovery needs and dependencies.

1. **Scope and service:** “Are you answering for Site A, Site B or both? Which products, customers and delivery commitments does your dispatch operation support?”

2. **Validate the activity:** “Does the Site A description of ‘Dispatch, chilled’ still reflect how you work? What has changed since March 2026, and where does dispatch start and finish?”

3. **Peak timing:** “The list identifies weeks 49–52 and week 14 as peaks. What makes those periods different? At what time of day would an interruption cause the greatest impact—for example, just before a carrier collection or customer delivery deadline?”

4. **Impact over time:** “Assume dispatch stops during that peak period while other operations initially remain available. What happens after a missed collection, by the end of the shift, after 24 hours and over subsequent days?” Adjust these time bands to the actual dispatch cycle.

5. **Financial impact:** “At each point, what daily losses would arise from spoilage, penalties, lost sales or other costs? When would these cross the approved bands: under €10k, €10k–€100k and over €100k per day? What records support the estimates?”

6. **Customer impact:** “When would we first see a complaint, a late key-account delivery or the loss of a key account? Which contracts, delivery windows or past incidents support that judgment?”

7. **Regulatory impact:** “Could delayed dispatch create food-safety, temperature-control or traceability issues? Under what circumstances would a report to the food authority or an authority-imposed production stop arise? Which answers need QA confirmation?”

8. **Unacceptable downtime:** “At what point would the interruption become unacceptable, and which impact drives that limit?” Record the reason; the approved impact levels alone do not establish an acceptable downtime limit.

9. **Recovery target and minimum service:** “How much earlier must dispatch resume to avoid that limit? What minimum throughput, customer coverage and operating hours would be needed?” Keep the proposed recovery target inside the maximum tolerable downtime.

10. **Quality release:** “A2 depends on A3, quality release. What happens to dispatch if release is unavailable? Who can authorise release, and what evidence must accompany each shipment?” Site A is the only recorded lab location.

11. **Systems and records:** “What does LogiStock enable? If it is unavailable, which orders, stock, release, temperature and traceability records must remain accessible? How much missing or outdated data could you tolerate?”

12. **Site B support:** “What does ‘manual export to Site B possible’ mean in practice? Has it been tested? What staffing, chilled storage, systems access, QA support and transport capacity would Site B need, and how quickly could it help?”

13. **Carrier dependency:** “NordFrost is the only recorded carrier. What happens if it cannot collect? Are alternatives actually available, qualified and able to meet chilled-chain requirements during peak demand?”

14. **Resources and backlog:** “What minimum people, skills, equipment, loading capacity and chilled storage are needed? Once dispatch resumes, how long would clearing the backlog take, and what could constrain it?”

Close with: **“Which answers are supported by evidence, which need validation, and where do you have reservations?”** Record an owner and due date for each open point. Treat recovery priorities and targets as proposals for management endorsement.

**Tool calls (JSON events):**

- command_execution: `/bin/bash -lc "pwd && rg --files -g 'AGENTS.md' -g 'site-a-activity-list.md' -g 'impact-criteria.md' -g 'site-b-org-chart.md'"`
- command_execution: `/bin/bash -lc 'cat /home/brain/.codex/skills/role-bia-facilitation/SKILL.md'`
- command_execution: `/bin/bash -lc 'cat impact-criteria.md'`
- command_execution: `/bin/bash -lc 'cat site-a-activity-list.md'`
- command_execution: `/bin/bash -lc 'cat site-b-org-chart.md'`
