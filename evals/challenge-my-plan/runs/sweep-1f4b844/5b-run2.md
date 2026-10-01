# /challenge-my-plan case 5b, run2: Claude Code, guidance at 1f4b844

`claude -p --setting-sources project --plugin-dir <repo> --permission-mode dontAsk --allowedTools Read,Glob,Grep --output-format stream-json --verbose`, stdin closed, later turns with `--resume`; one driver, at most two runs at once. Session `fd1c4417-3808-43ea-b2fe-f94632b106c0`.

Files in the working folder: `bia-extract-dispatch.md`, `option-paper-dispatch.md`, `supplier-record-nordfrost.md`.
Attached files after the run: unchanged against `files/`.

## Turn 1

**Request:** Can you ask me the hard questions about this recovery option before the steering group meets tomorrow? The files option-paper-dispatch.md, bia-extract-dispatch.md and supplier-record-nordfrost.md in this folder are attached.

**Reply (verbatim):**

I read all three files. The option rests on four assumptions in §3, and none of them is backed by evidence in the pack. The one in the worst shape is the carrier: the BIA and the supplier record both point to NordFrost as a single point of failure, and the paper treats it as a strength. Here are the questions I'd expect the steering group to ask, most damaging first.

## 1. The carrier (likely the deciding question)

- **"NordFrost serves both sites" isn't the same as NordFrost helping you recover. What have they committed to?** The supplier record says there's no SLA for recovery support. Nothing obliges them to move their collections and routes to Site B within 8 hours.
- **What happens if NordFrost is the problem, or is stretched by the same incident?** The BIA records "no second carrier." The supplier record has no information on NordFrost's own continuity plan. The option doesn't remove the single point of failure; it moves it to a second site.
- **Has anyone asked NordFrost whether they could serve Site A's customers from Site B, 140 km away?** Their routes, driver hours and delivery windows were planned around Site A.
- **Why does the paper list as an assumption something the BIA already flags as a known gap?**

## 2. The 8-hour RTO

- **Has anyone timed the full sequence from losing Hall 3 to the first chilled dispatch leaving Site B?** That means the decision to activate, call-out, a roughly 2-hour drive for 140 km, opening the cold room, the manual export, picking, loading and carrier collection. If it hasn't been timed or tested, "within 8 hours" is a hope.
- **Who decides to activate, on what trigger, and at 3 a.m. on a Sunday?** The clock starts at the incident, not when someone makes the decision.
- **Only the shift leaders are named. Who does the picking and loading?** Is Site B staffing the extra volume? If so, is that agreed?

## 3. Site B's cold room

- **Who confirmed that the cold room is "spare," and when?** Is it spare at your seasonal peak? Has Site B's management signed up to this in writing?
- **Does Site B's own continuity plan already count on that room?** If so, the same capacity is promised twice.
- **What stock goes into it?** If Hall 3 is lost, Site A's chilled stock may be lost too. Where does the replacement product come from, and how does it get to Site B?

## 4. What happens after 48 hours

- **The room holds two days of volume. What happens on day three?** The BIA's maximum tolerable period of disruption (MTPD) is 24 hours, so you'd meet it. But rebuilding Hall 3 will take far longer than 48 hours, and the paper is silent on everything after that point.
- **Can Site A's customers accept delivery times from a site 140 km further away?** The option could meet the RTO and still break customer commitments.

## 5. The manual export

- **Will Site A's warehouse system still be running when Hall 3 is lost?** If it runs in or depends on that hall, there may be nothing to export from.
- **Who runs the export? How long does it take at a full day's volume, and what happens to orders that arrive after it?** Has it ever been done end to end?

## 6. Cost

- **"No additional cost" can't be right.** The plan involves overtime, travel and possibly accommodation for the shift leaders. It also means longer routes and possible re-routing charges from NordFrost, and any Site B work that gets displaced. Even a rough figure would be more credible than zero.

## 7. The decision itself

- **What else was considered?** The group is asked to "choose" an option, but the paper presents only one, with no comparison and no "do nothing" baseline.
- **The paper is a v1.2 draft from 14 Aug. Has anything changed in the seven weeks since?**
- **If the group approves it, who owns the option, and when will it first be tested?** The paper names no owner, test date or review date.

## If you only prepare three answers

1. What NordFrost has actually agreed to, or a plan to get a recovery commitment or a second carrier.
2. Evidence for the 8-hour timeline, or a date for a timed walkthrough.
3. Written confirmation from Site B that the cold room is available.

If those aren't settled by tomorrow, you could ask the group for **conditional approval**: they agree the direction now, and final sign-off waits until those three are closed. That's likely to land better than asking for a full decision the paper can't yet support.

I can turn this into a one-page briefing for the steering group if that would help.

**Tool calls (stream-json):**

- Bash: `ls -la && cat option-paper-dispatch.md bia-extract-dispatch.md supplier-record-nordfrost.md`
