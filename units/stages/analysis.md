<!-- meta: unit=stages/analysis version=2026.11 -->
# Analysis: Business Impact and Risk

## Situation

Much of what the analysis team needs has not yet been documented. Before the first interview, a candidate activity list, a set of resource requirements and a set of questions must be produced. AI can draft the initial versions using the information from your other sites. However, it cannot know what only the acquired site's staff know.

Analysis also involves some of the most sensitive material in BCM: live BIA and risk data must be entered into an approved environment.

## Typical AI uses

- drafting candidate activities, their resource requirements and the interview guide from existing site data
- summarising interviews into impacts, resource requirements, assumptions and unresolved points
- comparing requirements registers across sites to surface shared suppliers
- naming where two teams' recovery assumptions contradict
- summarising public threat developments for a person's risk review, and clustering risks, issues and recurring themes
- re-opening affected BIA and risk records when a system, supplier or site changes

The type of tool and the environment for each use are in the selection guide in `tools.md`.

## Minimum controls

The one control that matters: **a resource requirement drafted by AI is only a question for the activity owner.** It goes into the register only when the owner confirms it.

- **AI can test whether a proposed RTO fits the impact criteria. It does not set the RTO.** The same holds for MTPD.
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

## Risk assessment

The BIA method does not cover risk assessment. Risk assessment with AI support has public and internal aspects. The data rule distinguishes between the two. Public threat, regulatory and incident reporting data can be collected in any approved tool. This is because it contains no information about your organisation. However, once you judge relevance against your own records, the work becomes high-sensitivity. It then moves to the approved environment.

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

Level 2, Repeatable. The pre-interview draft needs no connector: it works from the sources you attach, so what it takes is agreed tools, a written data rule, a saved prompt, a named reviewer and the normal approval route. Write down the method and the dates of those sources as you go, so a reviewer can see what the draft was built from. BIA support and threat relevance over connected records are Level 3, Defined, where retrieval reaches the live inventory under a written, owned method, the draft can be regenerated when the inventory changes, and all five self-check questions in `levels.md` answer yes with evidence.

Hoekstra, W., Gerner, K., et al. (2026). AI4BCM: Guideline for using AI by BCM professionals. CC BY 4.0.
