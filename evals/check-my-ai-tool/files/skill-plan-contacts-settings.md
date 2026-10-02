# Skill: plan-contacts-check

Exported from the skill folder and the tool's admin page by the BCM team, 22 September 2026.

- **Name:** plan-contacts-check
- **Description (as set in the tool):** Reads the business continuity plans in the "BC Plans" library and lists every
  contact line whose person is not in the current organisation chart. Lists only; changes no plan.
- **Version:** 1.3, 10 September 2026. Changes: 1.3 reads the organisation chart export instead of the old phone
  list; 1.2 (2 July 2026) added the plan version to each line; 1.0 (5 May 2026) first version.
- **Runs in:** the organisation's approved enterprise AI workspace, AI tools list entry T-07, approved for high-sensitivity
  data.
- **Sensitivity class:** high (plans name people, phone numbers and recovery sites).
- **Permissions as set in the tool:** read: "BC Plans" library, read-only; read: "HR exports/org-chart" folder,
  read-only. Write: none. Send: none. Web search: off. Other connectors: none.
- **Sources and their dates:** business continuity plans in "BC Plans" (each carries its own version and date);
  organisation chart export, 1 September 2026.
- **Not for:** deciding who replaces a contact; changing any plan.
