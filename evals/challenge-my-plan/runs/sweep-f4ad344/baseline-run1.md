# challenge-my-plan baseline (no skill loaded), run1: Claude Code, guidance at f4ad344

`claude -p --setting-sources project --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `9abb6a34-a223-4b89-aec6-3200cdfd7a36`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Baseline: the job request without the skill, no AI4BCM package installed, no data-class turn; graded on the hard rows only, as a note for `results.md`.
Attached files after the run: unchanged against the folder as the run started (hashes), nothing created.

## Turn 1

**Request:** Can you ask me the hard questions about this recovery option before the steering group meets tomorrow? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

I read all three files. Here are the questions I'd expect the steering group to ask, roughly in order of how much damage each could do to the paper.

**Before anything else: the paper says the decision is due on 2 Oct 2026. That was yesterday.** Has the meeting moved, or is this an old version? The paper is v1.2 from 14 August. What has changed in the seven weeks since, and why isn't there a newer version?

## 1. Can you actually do it in 8 hours?
1. **Where does the 8 hours go?** Break it down: noticing the problem, the decision to invoke, calling shift leaders, about 2 hours of driving for 140 km, the manual export, setting up Site B, and the first NordFrost collection. Does the total come in under 8 hours with some margin, or does it only work if everything goes right?
2. **Has any part of this been tested?** If not, what makes you confident in the 8 hours, and when would the first exercise be?
3. **What happens at 3 a.m. on a Sunday?** Who has authority to invoke the plan, and how do they reach the shift leaders?

## 2. The stock (I think this is the biggest gap)
4. **If Hall 3 is lost, isn't the chilled stock in it lost too?** The option moves the *dispatch activity*. What does Site B dispatch? Where does replacement stock come from, how does it reach Site B, and how fast?
5. **The cold room holds "two days' volume". Who checked that, and when?** Is the room spare all year, including peak season? Is it reserved anywhere, or could Site B fill it the week before you need it?

## 3. NordFrost: the paper relies on the weakest dependency on record
6. **The BIA already flags NordFrost as a single carrier with no backup.** This option still depends entirely on NordFrost. Why is that acceptable?
7. **The supplier record says there's no recovery SLA and no information on NordFrost's own continuity plan.** What obliges NordFrost to move Site A's volume to Site B pickups at short notice, on top of Site B's normal volume? Have you asked them?
8. **What if the incident also hits NordFrost**, for example a regional event, a fuel problem or a strike? With no second carrier, recovery is zero.

## 4. People
9. **How many shift leaders, and are they obliged to go?** What do their contracts say about working at another site? What's the plan for a recovery lasting several days: accommodation, overtime, rotation?
10. **Who runs what's left of Site A** while its shift leaders are at Site B?
11. **Do the Site A leaders have access, training and system logins at Site B**, or will they arrive and wait?

## 5. The warehouse system
12. **Where does the "manual export" come from?** If Hall 3 is lost, is the Site A system, its server or its network still up? Who runs the export, how long does it take, and has Site B's system ever imported it?
13. **What doesn't carry over in the export?** For example labels, customer references, lot numbers and temperature records.

## 6. Cost: "no additional cost" will get challenged
14. **Can you defend "no additional cost"?** Overtime, travel, accommodation, extra freight over a longer distance, testing, and Site B business pushed aside all cost money. A paper that says zero invites people to doubt everything else in it. Do you have a rough estimate?

## 7. Customers and compliance
15. **Can you still meet customer delivery windows** from 140 km further away?
16. **Is Site B approved and licensed for Site A's products and customers?** That includes food safety, cold chain and any customer audits.

## 8. Scope and alternatives
17. **What scenario does this cover?** It covers "Hall 3 lost". What about all of Site A going down, or an event that affects both sites?
18. **Why only one option?** The group is asked to "choose" without anything to compare it with. What else did you consider, for example a second carrier, a third-party cold store, or mobile refrigerated units, and why did you reject it?
19. **Who owns the plan after approval**, and when is it reviewed? Is the BIA from 4 February still current?

---

**The ones that could sink it at the meeting:** #4 (stock), #6–8 (NordFrost) and #14 (cost). If you can't answer those yet, you could ask for conditional approval: approve the option subject to a confirmation from NordFrost, a Site B capacity check, and a tabletop exercise by a set date. That's easier to defend than asking for an outright choice.

I can draft short answers or a one-page annex covering these gaps if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`

## Turn 2

**Request:** I own this paper; I am the BCM manager at Site A. On the shift leaders driving to Site B: two of the four have agreed to drive; the other two have not been asked. On §4, the cost: finance has not seen the paper.

**Reply (verbatim):**

Those two answers change what the paper can claim. As written, §3 and §4 state things that aren't true yet. Here are the follow-up questions the group is likely to ask.

## Shift leaders: 2 of 4 agreed

1. **Is two enough?** The MTPD is 24 hours and the cold room holds two days' volume, so this could run for several days. How many shift leaders does chilled dispatch need per shift, and how many shifts per day? Two people can't cover round-the-clock work for days, especially after a 2-hour drive.
2. **What exactly did the two agree to?** Was it verbal or in writing? Did they agree to one shift or several days? Daytime only, or out of hours too? Can you reach them at night?
3. **Are the two who agreed on different shifts?** If they're on the same rota, a single bad timing could mean neither is available.
4. **Why haven't the other two been asked?** Can you ask them before the meeting? If one says no, does the option still work?
5. **Does a works council or union need to be involved?** Making staff drive 140 km to another site may need more than personal agreement.
6. **The wording needs to change either way.** "Site A's shift leaders drive to Site B" reads as all of them, confirmed. The accurate version is "2 of 4 confirmed (verbally, [date]); remaining 2 to be asked by [date]."

## Cost: finance hasn't seen it

7. **What is "no additional cost; uses existing capacity" based on?** As the paper stands, it's your claim alone. The first question at the meeting will probably be "has finance seen this?", and the answer is currently no.
8. **Who pays when you invoke the plan?** Overtime, travel, accommodation, extra NordFrost mileage and Site B time all cost money on the day. Who can authorise emergency spending at 3 a.m.?
9. **What does it cost to keep the option ready?** That includes exercises, any internal charge for holding Site B's cold room free, and any change to NordFrost's terms.
10. **Can you get even an informal look from finance before the meeting?** If not, change §4 to "not yet costed; finance review pending" and list the known cost items. That's more credible than zero.

## The pattern behind both
11. **Two of the four §3 assumptions turned out not to be fully confirmed. What about the other two?** Has anyone at Site B confirmed in writing that the cold room is free? Has the export to Site B's system ever been run? Has NordFrost been asked? Expect the group to ask this once one gap comes out.

Separately, the paper still gives 2 Oct as the decision date. Worth correcting before you circulate it again.

**My recommendation:** don't ask the group to "choose this option" tomorrow. Ask for **conditional approval**, with conditions that have dates and owners:
- all four shift leaders asked and confirmed in writing
- finance costing
- written confirmation from Site B on the cold room
- a NordFrost conversation about recovery support
- a tabletop exercise against the 8-hour RTO

That turns weaknesses they'd otherwise find themselves into a plan you're presenting.

I can redraft §3, §4 and §5 in that form if you'd like.

**Tool calls (stream-json):**

- none
