<!-- meta: unit=stages/analysis version=2026.11.1 -->
# Analysis: business impact and risk

Stage 3 of six.

## What this stage covers

This stage covers BCM analysis activities, especially business impact analysis (BIA), risk assessment, and the identification of dependencies, priorities, and recovery requirements. These activities draw on many people and systems, and their inputs have to be compared and checked.

AI shows where impact becomes unacceptable; the activity owner decides where the line sits

EXAMPLE. AI DRAWS THE CURVE FROM THE INTERVIEWS AND MARKS WHERE IMPACT TURNS UNACCEPTABLE.

## Where does AI help, and where are its limits?

AI can structure interviews, summarise workshops, spot inconsistencies and dependencies, and compare data sets. It can also flag records for review when something changes. It can also link information from internal systems, such as HR, application inventories, supplier records, location data and previous incident reports.

This stage involves handling some of the most sensitive information in BCM. The BIA and risk assessment data includes information on financial impacts, staffing dependencies, concentration risks, vulnerabilities, supplier weaknesses and internal operational constraints. Always keep live BIA and risk data in approved corporate or private environments, never in public tools.

**Used today.** Cited public example, source in References, p. 31.

The US Defense Logistics Agency uses AI risk-assessment models to identify unreliable suppliers and those providing counterfeit or non-conforming parts (2025).

## What AI can do, by activity

Gather the approved source material for the analysis. This should include activity lists, organisational structures, system inventories, supplier records, location data, impact criteria, prior incident material and existing risk information (*Data rules*, p. 7).

## Preparing the BIA

- Explaining BIA terms such as maximum tolerable period of disruption (MTPD) and recovery time objective (RTO) in easier language (L1)
- **BIA interview support.** Use an enterprise AI assistant to prepare interview guides and workshop questions, explain definitions, and structure the expected outputs of the discussion. (L2)

## BIA interviews and workshops

- Transcribing and summarising workshops and interviews. The summary includes impacts, dependencies, assumptions, gaps and open questions, rather than just providing a well organised summary. (L2)

## Dependencies and consistency

- **Consistency checking across responses.** Ask the AI to compare BIA outputs from related departments and identify where one team's assumptions or recovery expectations conflict with another's. (L2)
- **Dependency mapping.** Compare activities with systems, people, suppliers, sites and data to identify shared dependencies, single points of failure and areas of concentration risk. (L3)

## Recovery requirements

AI verifies the proposed recovery requirements, but does not set them.

- **Recovery target review support.** Use AI to test whether a proposed RTO is consistent with impact thresholds, dependencies, and comparable activities. The activity owner and management set the target. (L2)

## Risk assessment

- **Risk scenario support.** Search-enabled tools identify current public threat developments. AI then writes a relevance note for each threat, naming the source and the risk record affected. This is followed by questions for the risk owner. The risk owner then decides on the next steps. (L4)
- Clustering risks, issues, and recurring themes (L3)

## Keeping the analysis up to date

Where possible, a connected workflow can detect changes such as application retirement, restructuring, changes to suppliers, or site closure.

- Prompting a review when the organisation or its systems change (L4)
- **Continuous review workflows.** A workflow tool monitors changes in approved source systems and flags any potentially affected BIA or risk assessment records for human review. (L5)

L1 Ad hoc · L2 Repeatable · L3 Defined · L4 Measured · L5 Optimising

## Minimum controls

The one control that matters: **a resource requirement drafted by AI is only a question for the activity owner.** It goes into the register only when the owner confirms it.

- The draft names its source data and that data's date. An out-of-date inventory yields a BIA that looks current and is wrong.
- Recovery fields stay empty in anything AI produces.

**For the auditor.** The requirements register with the source, the interview it came from and the date behind each entry, the date the owner confirmed it, and the recovery times the owner set. For risk, each relevance note with its sources and the risk owner's decision.

## Method

1. Fix the sources you will attach, and their dates. With memory, past chats, project files, connectors and web search switched off, what you do not attach is not in the answer. Where any of them is on, the model may draw on it without saying so. Whether the model filled the gap or left it out, the output looks the same.
2. Draft before interviewing (activities, resource requirements, questions, recovery fields blank). The draft is the organiser's homework and stays with the organiser.
3. Turn the draft into a take-in sheet for the interview: plain spoken questions, conflicts between sources first, fitted to the interview's length, with a rough time per section and a mark on what to drop first. Rate impacts over time in full only for the one or two activities the sources rank highest; for the others, ask only where they differ.
4. Interview from the sheet. The activity owner corrects the questions, not the draft; record what the draft could not have known.
5. Compare registers across sites; put every conflict to the two owners, not to the model.
6. Hand the register on with the confirmed and unconfirmed marks intact, so the next stage can see which entries were drafted and never challenged.

Requirements come in four classes. Once the impacts and the MTPD are settled, the interview covers people, with the skills, authorities and mandates the work needs; then seats and buildings; then IT and applications, each with its RTO and its RPO; then suppliers and other third parties.

Dependencies are a separate item and keep the narrower meaning of up- and downstream relationships with other departments, each recorded with the RTO the relationship carries, so that a relationship one department records appears in the other department's BIA.

The five-stage BIA workflow (identification of scope, structured interview, conversion to the standardised template, listing the requirements, consolidation and handover) is set out in `workflow-design.md`.

## Risk assessment with AI support

The BIA method does not cover risk assessment. Risk assessment with AI support has public and internal aspects. The data rule distinguishes between the two. Public threat, regulatory and incident reporting data can be collected in any approved tool. This is because it contains no information about your organisation. However, once you judge relevance against your own records, the work moves to the highest classification level. It then moves to the approved environment.

| | Risk assessment with AI support |
|---|---|
| Inputs | public threat, regulatory and incident reporting for the sector and the regions you work in; the approved risk register, the requirements register and the BIA output, each with its date |
| Type of tool | for public research, any approved tool; for judging what it means for your own records, only the approved environment (`tools.md`) |
| Output | a relevance note per threat. It states how certain the public evidence is. It links each point to the public source and to the internal record it touches. It ends in questions or themes for the risk owner |
| Review boundary | a person assesses the threat, decides the treatment and accepts the risk. A model proposes relevance. It does not rate a risk, accept it or change a risk record |

## Prompts

The task prompt is `prompts/bia.md`. The first choice in its Task line is the pre-interview draft that the case below uses. Its Review line names who confirms each requirement and who sets the recovery fields. The risk-assessment relevance note uses the same six-element pattern from `prompts/README.md`, with the threat evidence and the risk register as its sources and the table above as its output.

Skill: `/prepare-bia` drafts the interview guide from your material.

## Case example

**Prompt.** Draft the activities, resource requirements and interview questions for the acquired site. Leave recovery times blank.

**Response.** Fourteen candidate activities, drawn from the four existing sites. Resource requirements listed per activity in four classes (people, seats and buildings, IT and applications, and suppliers). Thirty-one interview questions. RTO and MTPD fields left empty as instructed.

**What changed.** The interview guide existed before the first interview. The interviews then found that the site slaughters wild boar, seasonally, and that it matters for cash flow.

## Level

Level 2, Repeatable. The pre-interview draft needs no connector: it works from the sources you attach, so what it takes is agreed tools, a written data rule, a saved prompt, a named reviewer and the normal approval route. Write down the method and the dates of those sources as you go, so a reviewer can see what the draft was built from. BIA support over connected records is Level 3, Defined, where retrieval reaches the live inventory under a written, owned method, the draft can be regenerated when the inventory changes, and all five self-check questions in `levels.md` answer yes with evidence. Threat relevance over connected records is Level 4, Measured, as *Risk assessment* marks risk scenario support.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
