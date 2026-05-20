# Briefing for Laptop Claude — APEX Meeting Day (2026-05-20)

**INSTRUCTIONS FOR LUCAS:** Copy everything below the `---` line into a new Claude.ai chat on your laptop. That session will then have full context for today's meeting.

---

I'm Lucas Gragg, founder of **Gragg Robotics, LLC**, a Maine-based drone autonomy startup. Today is **2026-05-20**. In ~2 hours I have an **in-person meeting at 9:30 AM at the KVCOG offices in Fairfield, Maine** with **Marissa Henkel** (Procurement Counselor at Maine APEX Accelerator, hosted by EMDC).

## Meeting context

Marissa is my APEX advisor — federal-funded help (free) for small businesses navigating government contracting (SAM.gov, AFWERX SBIR, DoD procurement). She's specifically going to coach me on procurement readiness today because **my LLC Certificate of Formation has not arrived in the mail yet** (mailed 5/5 with USPS Priority Express + 24-hr expedite — overdue, possibly today). Without the Certificate we can't do the planned SAM.gov / UEI / CAGE registration walkthrough, so today is general procurement-readiness coaching.

## Company state — current as of 2026-05-20

**Entity:**
- Maine LLC formation: **Certificate in transit** (mailed 5/5)
- EIN: queued (after Certificate)
- Business bank account: queued (Bangor Savings, after EIN)
- SAM.gov registration: queued (in-person session with Marissa, after the above three)

**Product:**
- **Universal multi-drone control software + bolt-on autonomy pod** that retrofits onto any Pixhawk / PX4 / MAVLink-compatible drone
- Tech stack: PX4 SITL simulation, MAVSDK, Flask, Python
- 6 RTS-style command primitives: TARGET / FOLLOW / SWEEP / WAYPOINT / GO HOME / ENGAGE
- One operator commands 4-12 drones simultaneously (~10× labor leverage vs single-pilot model)
- Hardware tiers: POC ~$660/drone (Pi 5 + camera + RFD900x radio), Production ~$4,200/drone (Jetson Orin + thermal + LiDAR + mesh radio)

**Website:**
- Live at **https://unrivaled-mousse-002230.netlify.app** (will eventually move to graggrobotics.com once DNS swap completes — currently graggrobotics.com is partially routing to a GoDaddy parking page due to a WSM hijack issue, fixable via nameserver switch to Netlify DNS)
- Custom-built HTML/CSS/JS site at `website/build/` in the project
- v3 dual-logo system: realistic black quadcopter with blue LED strips (civilian) or red LED strips (military), opposing tilt angles

**Funding pipeline:**
- 🟢 **MTI Business Innovation Funding** application 2428739 in flight (~$25K likely). Working with **Abby Osei, Investment Officer** (aosei@mainetechnology.org · 240-474-3277). Intake call 5/13 went well. Drafting the application now.
- 🟢 **AFWERX SBIR Phase I draft** complete at `funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md`. Full 15-section ~9-page application. Not for submission until next AFWERX BAA opens (estimated June–August 2026).
- 🟡 Outreach drafts ready (MMTC, UMaine ECE, MCE Top Gun, Maine Angels, Maine Venture Fund, MacroFab, Sierra Circuits) — not yet sent
- 🟡 Maine Venture Fund + Maine Angels: queued for Stage 2

**Target customers:**
- Civilian: Central Maine Power (CMP), Versant Power (utility inspection), Maine SAR / Game Wardens / Civil Air Patrol, Kennebec County sheriffs, Maine agriculture
- Defense: AFWERX, AFRL, 711 HPW, AFSOC (via SBIR Phase I → Phase II → Phase III sole-source pipeline)

## Open questions to ask Marissa today

1. **AFWERX BAA timing** — when does the next Phase I window open, and where exactly do I monitor for it?
2. **End-user letters of support** — does APEX have introductions to AFRL / 711 HPW / AFSOC end-users who could sign a letter of interest for my SBIR proposal?
3. **NDA template** — does APEX have a Maine-friendly NDA template I can use with potential customers and partners?
4. **Pre-award match eligibility** — can MTI BIF match expenses cover pre-award purchases (laptop, Claude subscription)? (Need to ask Abby too)
5. **SAM.gov session reschedule** — once Certificate arrives + EIN issued + bank statement in hand, what's the next available in-person slot?

## What Marissa might want from me

- A clear, brief status update (LLC, site, MTI, SBIR)
- An honest view of my Year-1 customer targets
- Any blocker she can help unstick

## Files I have on the laptop (or accessible via local network)

- **Pitch deck:** `gragg_robotics_deck_v1.pptx` (downloaded from desktop file server)
- **Capability statement:** `03_capability_statement.md` (also on file server)
- **Live website:** open in Chrome tab
- **Swarm UI (live demo):** http://192.168.18.47:8500/ — runs on my desktop, accessible from laptop on same WiFi

## What I want from THIS Claude session on the laptop

Help me during/after the meeting with:
- Quick lookups Marissa asks about (e.g., "what's a CAGE code", "what's NAICS code XYZ")
- Drafting follow-up emails after the meeting
- Capturing meeting notes into a clean summary
- Researching any names/programs Marissa mentions

I don't need you to control the laptop directly — just be ready to answer questions and help draft text quickly.

---

End of briefing. Paste this whole block (above the `---`) into a new Claude.ai chat on the laptop and that Claude will be up to speed.
