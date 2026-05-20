# MTI Intake Call — Word-for-Word Script

**Meeting:** Wednesday May 13, 2026 · 10:00 AM Eastern · Virtual (link will arrive in your inbox)
**With:** Abigail "Abby" Naana Osei, Investment Officer, Maine Technology Institute
**App ID:** 2428739 — Business Innovation Funding (BIF), Gragg Robotics
**Format:** 1 hour, structured around 8 BIF growth/success areas

**Mental model:** This is a MONEY conversation. Abby decides if you advance toward a BIF award ($10K–$250K range). She's not adversarial — she's looking for reasons to YES — but she also has a duty to filter out projects that aren't ready. Your job is to come across as **competent, calibrated, and coachable**.

> **Three things she's secretly evaluating:** (1) Do you understand your own market? (2) Can you execute? (3) Are you the kind of founder who follows through? She'll never ask these directly. She'll infer them from how you answer the 8 areas.

---

## Pre-call — what to do TODAY (Tue 5/12) before you go offline

- [ ] Confirm Abby gets the deck via email (you committed to "Tuesday" in your reply — Claude will send it for you)
- [ ] Read this script through ONCE this evening
- [ ] Read `04_terms_cheatsheet.md` once — pay attention to sections 1, 2, and 8 (likely-questions answers)
- [ ] Charge laptop, headphones, phone

## Pre-call — what to do tomorrow morning (Wed 5/13)

- [ ] **9:00 AM** — laptop online, this script open in one window, deck open in another, Gmail open in a third
- [ ] **9:30 AM** — restroom, water bottle full, snack
- [ ] **9:45 AM** — Teams/Zoom link should be in your inbox by now. If not, email Abby: `aosei@mainetechnology.org` — "Standing by for the meeting link"
- [ ] **9:55 AM** — click the link, allow camera + mic, test audio one more time
- [ ] **9:58 AM** — deep breath. You've done your homework. You're ready.
- [ ] **10:00 AM** — live

---

## OPENING — first 60 seconds (when she joins)

> **"Hi Abby, thanks for the time. Quick warning, first-time founder here so feel free to slow me down on any MTI-side terms I haven't seen before. I'm Lucas Gragg with Gragg Robotics — universal multi-drone control software plus a hardware sensor pod that retrofits onto any drone. Quick status update before we dive in: Maine LLC was mailed last week with expedited processing, Certificate is back / arriving any day now, and APEX has me lined up for SAM.gov registration in person once the docs are in hand. Happy to walk through the deck if you want a 5-minute overview, or jump straight into the 8 areas — what works best for you?"**

That last sentence matters. **Let her drive the format.** Most counselors will say "let's hit the 8 areas, you can reference the deck as we go." Some say "give me the 5-min walkthrough first." Match her preference.

> **If your LLC Certificate already arrived:** swap "is back / arriving any day" → "came back yesterday and the EIN is queued for today"
> **If she opens with general MTI program overview:** listen, take notes, don't interrupt. She does this in every intake. It usually takes 5-10 minutes.

---

## THE 8 AREAS — your prepared answers

She'll cover these in roughly this order. **Each answer is 30-60 seconds.** Don't ramble. End with a hook ("happy to go deeper if useful") so she can probe where she wants.

---

### 1. TEAM — what are your team's skills and experiences?

> **"It's me, sole founder, full-time committed. My background is operations and logistics — I've spent the last several years running route logistics for a regional package-delivery contractor, which means I know how to keep a fleet of moving assets coordinated across geography under time pressure. Different domain, same problem.**
>
> **On the technical side, I've built the entire software stack you'll see in the deck — Python control system, MAVLink integration, the operator UI, the simulation environment. Working prototype runs four drones today.**
>
> **I'm not pretending to be a hardware engineer — for the physical pod build I plan to bring on a contract hardware engineer for the integration phase. That's specifically what some of the BIF money would go toward."**

**If she asks "why are you the right person to lead this":**
> **"I've been around drone hobbyist communities since high school, but more importantly I have the operations background to know what an OPERATOR actually wants out of this software. Most drone-autonomy startups are built by hardware people who underestimate the UI side. I'm building it from the operator-out, not the firmware-up."**

**Key:** be honest about being solo. Don't oversell. Solo with a clear plan to bring in specific contract help is normal at this stage.

---

### 2. PROBLEM and VISION — what are you solving?

> **"Two specific problems.**
>
> **First, multi-drone operations today are stuck in single-pilot, single-vendor mode. Every drone manufacturer ships its own ground station and they don't talk to each other. So if a Maine utility wants to inspect 50 miles of powerline with four drones, they need four pilots and probably four pieces of software. The labor cost kills the ROI of multi-drone work.**
>
> **Second, mission re-tasking mid-flight is brittle. Search and rescue teams pick up a new lead while drones are airborne — current systems require landing and restarting. That's catastrophic when minutes matter.**
>
> **My vision: one operator commanding any drone — not the brand-specific ones, ANY MAVLink-compatible drone — through a single RTS-style interface. Plus a bolt-on sensor pod that retrofits onto existing drones so customers don't have to replace their fleet. Same stack scales from inspection to SAR to defense."**

---

### 3. VALUE PROP — what's your value proposition?

> **"Three pillars.**
>
> **One — vendor-agnostic. We work with any MAVLink flight controller — Pixhawk, PX4, ArduPilot — so customers aren't locked into one drone manufacturer. That alone saves them six figures over a fleet refresh cycle.**
>
> **Two — solo-operator economics. One operator commanding 4 to 12 drones means roughly 10x labor leverage compared to single-pilot models. That's the ROI lever that makes drone fleets actually pencil out for utilities and SAR teams.**
>
> **Three — defense-plus-civilian dual-use. The same platform serves AFWERX defense topics AND commercial verticals. AFWERX explicitly favors dual-use because it shows market beyond government. We're built that way from day one."**

---

### 4. PRODUCT — how will you prototype, test, commercialize?

> **"Three stages.**
>
> **Stage 1, the prototype, is largely complete on the software side. I have a working multi-drone control UI running in PX4 SITL simulation today — four drones, full command stack, real-time telemetry. What I don't have yet is the hardware pod, which is where the BIF funding plays.**
>
> **Stage 2 is the hardware build. POC tier is around $660 per drone — Raspberry Pi 5, visible camera, RFD900 long-range radio. Production tier is around $4,200 per drone, adding thermal imaging and LiDAR. Total for a 4-drone POC is roughly $2,600 in hardware plus contractor time for integration.**
>
> **Stage 3 is commercialization. I want to land one paying customer pilot — most likely a Maine utility doing powerline or substation inspection — within six months of having flying hardware. Revenue model is SaaS on the UI plus hardware lease or sale on the pod, with optional service contract."**

---

### 5. MARKET — what do you know about the market?

> **"Three verticals where I've done initial research, ranked by addressability.**
>
> **First, rural infrastructure inspection. Maine has hundreds of miles of rural transmission line. Utilities like CMP and Versant currently spend $1,500 an hour for helicopter inspection. A 4-drone fleet replaces 70-80% of that work at maybe $200 an hour all-in. The TAM in Maine alone is in the millions per year just for utilities.**
>
> **Second, search and rescue. Maine has thousands of square miles of woodland. Game Wardens, K9 SAR, Civil Air Patrol all operate manually today. Multi-drone area coverage is roughly 5x faster than ground search in the first hour, which is the golden hour for survival outcomes.**
>
> **Third, defense via AFWERX. Air Force is funding swarm autonomy at hundreds of millions a year. Phase I awards are $75K to $150K, Phase II is $750K to $1.5 million. Six- to twelve-month windows.**
>
> **I'm civilian-first by deliberate choice — defense is a track but not the lead. AFWERX scoring favors dual-use applicants over pure-defense ones."**

---

### 6. BUSINESS MODEL — revenue, financials, organization?

> **"Revenue model is three-stream.**
>
> **One, SaaS subscription on the operator UI — call it $200 to $500 per month per fleet, recurring.**
>
> **Two, hardware sale or lease on the pod — $4K to $12K per drone for the production tier, one-time or amortized.**
>
> **Three, service contracts — installation, training, mission planning support, recurring annual.**
>
> **Stage 1 financial target: one paying customer pilot at $10K to $30K, plus the BIF grant, plus AFWERX Phase I when the window opens. Total runway needed for stage 1 is roughly $115K to $475K depending on which mix of grants land.**
>
> **Organizationally — Maine LLC, sole owner, member-managed. Will likely add a hardware contractor under a 1099 arrangement for the build phase, no employees yet. If we get to Stage 2 funding I'd convert one of those contractors to a full hire."**

**If she asks "what's your match for the BIF":**
> **"Cash match: $5K of personal capital already committed, plus whatever the AFWERX Phase I award contributes if it lands. Sweat equity: my full-time labor on the project at fair market rates. I understand cash match is weighted higher — happy to follow your guidance on the right mix for our specific request."**
>
> *(IMPORTANT: This is also where you ASK her to clarify what Marissa told you. See "Questions to Ask Abby" below — question 1.)*

---

### 7. SCALE — how do you grow?

> **"Stage 1, six to nine months: 4-drone POC working end-to-end, Maine LLC formed, Part 107 license, one paying customer pilot. Realistic raise $115K to $475K mixing MTI BIF, AFWERX Phase I, and customer pilot revenue.**
>
> **Stage 2, twelve to eighteen months from now: 12-drone production fleet, BVLOS waiver, three to five paying customers, AFWERX Phase II submission, and a small seed round. Realistic raise $1.85M to $4M total mixing SBIR Phase II, customer revenue, and equity.**
>
> **Stage 3 is multi-domain expansion — same UI, same pod design, scales to ground rovers and surface vessels. That's a 24-36 month horizon, not what we're talking about today.**
>
> **Scaling bottlenecks I can see: hardware supply chain on Pixhawk-compatible boards, regulatory pace on BVLOS waivers in Maine, and finding contract hardware engineers who want startup risk in Maine specifically."**

---

### 8. EXIT / SUSTAINABILITY — what does long-term look like?

> **"Honest answer — too early to plan a hard exit, but I think about it in two paths.**
>
> **Path one is sustainable independence — recurring SaaS plus hardware refresh cycles. A few hundred customers each paying $5K to $20K a year is a real business that doesn't need to exit.**
>
> **Path two is strategic acquisition. The natural acquirers are larger drone-autonomy companies — Skydio, Anduril, Shield AI, BRINC, Easy Aerial — or a defense prime that wants in on swarm autonomy. Five to seven year horizon for that conversation.**
>
> **What I'm NOT planning is a quick flip. I'm building this to operate, not to sell next year. If MTI invests, I want you confident I'll still be running it three years from now."**

---

## QUESTIONS TO ASK HER (have these ready — most counselors ask "any questions for me?")

### #1 — Match clarification (HIGH PRIORITY, do not skip)

> **"Marissa Henkel at APEX mentioned that some of MTI's funding is awarded as lump sum without strict 1:1 match — but the BIF page says 1:1 match required. Can you clarify what's actually expected for a $25K BIF request? Cash match weighted heaviest, sweat equity counts but less, no other Maine-state-grant funds — is that the right read?"**

### #2 — Disbursement model

> **"Is BIF reimbursement-based — I spend, then submit receipts — or milestone-based — you pay tranches as I hit deliverables? That matters for my cashflow planning."**

### #3 — Common rejection reasons

> **"What are the top one or two reasons applicants in my range get sent back for revision? I'd rather hear it now than after I submit."**

### #4 — Timeline

> **"From submitting a full BIF application, what's typical decision turnaround — 30 days, 60, longer?"**

### #5 — Other MTI programs

> **"Beyond BIF, are there other MTI vehicles that fit a Stage 1 hardware-build phase — TechStart, MERC, anything else? I'd rather find out from you than miss something."**

### #6 — AFWERX coordination

> **"Many of your portfolio companies do MTI plus AFWERX. Have you seen patterns where the two grants reinforce each other on timing or scope? Anything I should structure differently in the BIF app to set up a strong AFWERX submission later?"**

---

## CLOSING — last 90 seconds

When she signals wrap-up, take initiative:

> **"Abby, this has been incredibly useful. Three commitments I'm taking away from this call: [list whatever she specifically asked for or recommended]. What's the right next step on my end — submit a full BIF application now, or is there a pre-application conversation or document she'd want to see first?"**

After the call, within two hours:
1. Email her a one-page recap with what you committed to
2. Update `funding/FUNDING_TRACKER.md` with date, agreed next steps, anything she said about timeline
3. If she gave you any homework (financial projections, customer letters of interest, a specific application section), START it that day

---

## What NOT to do

- Don't promise revenue numbers you haven't validated. "We'll do $1M in year one" is a credibility-killer if you can't back it. Use ranges and say "based on what I know today."
- Don't badmouth competitors. Federal world is small. The drone person you trash-talk to Abby might be advising her next month.
- Don't ask for money in the call. The BIF application IS the ask. The intake is the conversation about whether the ask is worth submitting.
- Don't oversell the team. "Just me, plus contractors as needed" is a stronger answer than "we have a robust team" when you're solo.
- Don't promise to apply for things you won't follow through on. Counselors track this.

---

## If something goes wrong

| Problem | What to say |
|---|---|
| Internet drops | Reconnect on phone hotspot. Email Abby: "Lost connection, reconnecting." |
| Abby asks something you don't know | "I don't know — what should I be reading on that?" Calibration > guessing. |
| You realize mid-call your numbers were wrong | "Actually let me correct that — the right number is X." Abby will appreciate the correction more than the error. |
| She seems unimpressed with an answer | Don't double down. "Where would you push me to think harder?" — give her permission to coach you. Counselors love that. |
| She asks if you've talked to other agencies | "APEX is my first formal touchpoint. They're set up to walk me through SAM.gov in person once the docs are in hand. AFWERX is the next agency target." |

---

## Five sentences to remember

1. **"First-time founder, feel free to slow me down on terms."** Sets the bar to honest, not performative.
2. **"Cash match $5K plus full-time sweat equity, happy to follow your guidance on the right mix."** Concrete + coachable.
3. **"Civilian-first by deliberate choice — defense is a track, not the lead."** Differentiates you from the typical AFWERX-only applicant.
4. **"I'm building this to operate, not to sell next year."** Counselors hear "quick flip" pitches all day. This is the antidote.
5. **"Where would you push me to think harder?"** The single best line for getting unfiltered coaching.
