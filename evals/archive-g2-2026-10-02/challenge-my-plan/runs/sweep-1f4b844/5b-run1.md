# /challenge-my-plan case 5b, run1: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `289c1b23-d52b-4b56-b4f8-a51edc4e5f39`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you ask me the hard questions about this recovery option before the steering group meets tomorrow? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

Here are the questions I'd expect the steering group to ask tomorrow, roughly in order of how much damage each could do. Each one rests on something the three files say, or don't say.

## 1. The 8-hour claim

1. **Has anyone timed the 8 hours, even on paper?** Walk me through it hour by hour: the incident, the decision to invoke, calling the shift leaders, a 140 km drive (about 2 hours before traffic), the manual export, Site B taking the orders, picking, and the first NordFrost truck leaving. What's left over?
2. **Who decides to invoke, and how quickly?** If that decision takes 2 hours, the plan already misses the RTO.
3. **Has any part of this been tested?** The export, the import at Site B, a shift leader working in Site B's layout? If not, how can you tell the board it meets the RTO? An untested arrangement is a plan, not a recovery capability.

## 2. NordFrost is the weakest point, and the paper doesn't mention it

4. **What makes NordFrost re-route to Site B within 8 hours?** The supplier record says there's no SLA for recovery support. Have you asked them? Is there anything in writing?
5. **NordFrost serves both sites. The paper lists that as a strength. Isn't it a single point of failure?** If NordFrost has a bad day, Site A and the recovery site both stop. The BIA already notes there's no second carrier, and this option leaves that gap open.
6. **We know nothing about NordFrost's own continuity plan.** Why should the steering group approve a recovery option that depends on a supplier whose resilience nobody has checked?

## 3. Site B's capacity

7. **Who says Site B's cold room is "spare", and as of when?** Is it spare in peak season? Has Site B's management agreed in writing to give it up at no notice, or is this an assumption made at Site A?
8. **Two days' volume, then what?** Losing Hall 3 is unlikely to be fixed in 48 hours. What happens on day 3, and on week 3?
9. **What stock gets dispatched?** If Hall 3 is lost, so is the chilled stock in it. How do supplier deliveries get redirected to Site B, and how fast? The paper only covers orders and people, not the product.

## 4. People

10. **How many shift leaders, and who does the actual picking and loading?** Does Site B have spare staff on the shift, or are we assuming Site A's workforce follows?
11. **What if the event that took out Hall 3 also hurts or affects those shift leaders?** Is there a deputy list? Have working-time limits, overnight stays and travel been agreed?

## 5. The manual export

12. **Export from what?** If Site A's warehouse system runs in or depends on Hall 3, or goes down in the same event, there's nothing to export. Where is it hosted?
13. **Who does the export, in what format, and has Site B's system ever accepted one?** How many orders a shift are we talking about, and what's the error rate when it's done by hand under pressure?

## 6. "No additional cost"

14. **Is that number credible?** Extra mileage for NordFrost, overtime, travel and accommodation, displaced Site B business, and food-safety and traceability work all cost money. Who signed off "no additional cost"? Do you want your name on it if Finance looks at it after an incident?
15. **What's the ongoing cost of keeping this option ready?** That means reserving the cold room, testing and training. It's not zero even if nothing goes wrong.

## 7. The decision itself

16. **Why is there only one option?** The steering group is being asked to "choose" with nothing to compare against: no second carrier, no third-party cold store, no do-nothing baseline with its accepted risk. Expect someone to ask what else was considered.
17. **Are customers still served?** Chilled product travelling an extra 140 km: do delivery windows and shelf life still work?
18. **The paper is v1.2, dated 14 Aug, and still marked "draft".** What has changed in the seven weeks since? Is the steering group seeing the current version?
19. **What exactly are we approving?** Is it the option in principle, subject to validation (a NordFrost commitment, a Site B agreement, a timed test), or an arrangement we then report as in place? The first is defensible. The second, on this evidence, is not.

---

**If you only prepare for three:** the NordFrost dependency (4–6), the unproven 8-hour timeline (1–3), and the cost claim (14). The paper says nothing on the first, the second hasn't been tested, and the third is the one most likely to be challenged on the spot.

If you answer any of these here, I'll push back on your answers the way a sceptical steering group member would.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`
