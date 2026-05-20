# APEX Intake — Terms & Acronyms Cheat Sheet

**For:** Lucas Gragg, intake meeting with Marissa Henkel (Procurement Counselor, Maine APEX), tentative Tue May 6 2026 9 AM
**Purpose:** Fast lookup so you don't blank when Marissa drops jargon. Read once before the call. Skim during the call if needed.

**Standard caveat:** this is a quick-reference. Numbers and program details change yearly. If Marissa says "the current threshold is X," trust her — she lives in this world.

---

## 1. SBIR / STTR — the core program

| Term | What it is | What to say if asked |
|---|---|---|
| **SBIR** | Small Business Innovation Research. Federal program funding small companies (<500 employees) doing R&D the gov't wants. ~$4B/yr across ~13 agencies. | "Yes, AFWERX SBIR Phase I is our primary near-term target." |
| **STTR** | Small Business Tech Transfer. Same as SBIR but **requires a research-institution partner** (university or federal lab). ~$1B/yr. | "Open to STTR if we can partner with UMaine — would need APEX's read on whether that strengthens the application." |
| **Phase I** | Feasibility study. **6-12 mo, ~$50k-$300k** depending on agency. AFWERX Phase I is typically **$75k-$150k**. | "Phase I demonstrates feasibility — for us that's hardware-in-loop integration of the universal pod with three different airframes." |
| **Phase II** | Prototype + R&D. **~12-24 mo, ~$750k-$1.5M+**. Only Phase I winners are eligible. AFWERX runs ~$1M typical. | "Phase II is the production fleet — 12 drones operational with one paying customer pilot." |
| **Phase III** | Commercialization. **No SBIR funds** but unlocks sole-source contracts and follow-on work. | "Phase III is the commercial deployment — paying customers without further SBIR money." |
| **D2P2** / **Direct-to-Phase II** | Skip Phase I if you can prove feasibility was already done with non-SBIR funds. AFWERX uses this. | "Worth discussing — we have a working simulation prototype. Could that count as feasibility evidence for D2P2?" |
| **Topic** | A specific R&D problem an agency is funding. Each SBIR cycle has 100s of topics. | "We're tracking AFWERX topics around drone-swarm autonomy and contested-environment ops." |
| **Open Topic** | AFWERX's catch-all — "any innovative idea relevant to USAF/USSF." Lower bar than topic-specific calls. | "Open Topic is our backup if no specific topic matches in the next cycle." |
| **BAA** | Broad Agency Announcement. The actual call-for-proposals doc. Topics live inside the BAA. | "We're watching for the next AFWERX BAA — estimated June-Aug 2026." |
| **WOSB / SDVOSB / HUBZone / 8(a)** | Set-aside categories for women-owned, service-disabled-vet-owned, etc. **You're none of these.** | "I'm not a set-aside-eligible business. Standard small-business pool only." |

---

## 2. Federal registrations (you'll need ALL of these)

| Term | What it is | Status |
|---|---|---|
| **SAM.gov** | System for Award Management. THE federal contractor registry. **Must be registered before submitting any SBIR.** Free. ~2-3 weeks first time. | **Not yet registered** — this is the #1 thing APEX can help with. |
| **UEI** | Unique Entity Identifier. 12-char alphanumeric. **Replaced DUNS in April 2022.** Auto-generated when you register on SAM.gov. | "Will be assigned via SAM.gov once registered." |
| **DUNS** | Dun & Bradstreet number. **DEPRECATED — don't say you have one.** If Marissa mentions it she's testing or older. | "I understand UEI replaced DUNS in 2022 — I'll get one via SAM.gov." |
| **CAGE Code** | Commercial and Government Entity. 5-char ID. Auto-issued during SAM.gov registration. Identifies you to DoD specifically. | "Will come with the SAM.gov registration." |
| **NAICS Code** | North American Industry Classification System. 6-digit business category. You pick one or more. **For Gragg Robotics:** likely **541715** (R&D in Physical/Engineering/Life Sciences) or **336411** (Aircraft Mfg) or **541330** (Engineering Services). | "Probably 541715 — R&D in physical/engineering sciences. Open to your input." |
| **SBC** | Small Business Concern. Self-cert at <500 employees + US-owned. You qualify. | "Yes, sole proprietor under SBC threshold." |
| **GSA Schedule** | Pre-negotiated price list for selling to gov't. Not relevant for SBIR. | Don't bring up — out of scope. |

---

## 3. AFWERX-specific

| Term | What it is |
|---|---|
| **AFWERX** | Air Force innovation arm. Runs SBIR/STTR, Pitch Days, and several special vehicles (TACFI, STRATFI). Located at Wright-Patterson AFB. |
| **AFRL** | Air Force Research Laboratory. The AF's R&D org. Some AFWERX topics route through AFRL technical sponsors. |
| **TACFI** | Tactical Funding Increase. Adds ~$1.7M to a Phase II for accelerated commercialization. Requires matching private-investor commitment. |
| **STRATFI** | Strategic Funding Increase. Adds up to $15M to a Phase II for major scale-up. Requires significant private + Air Force matching. |
| **Pitch Day** | AFWERX's "shark tank" — pitch on stage, can win same-day Phase I awards. ~3-5/yr in different cities. |
| **Open Topic Phase I** | AFWERX's standing call for any innovation relevant to the USAF. **This is the most likely entry point for us.** |
| **Customer Discovery** | AFWERX-mandated step where you interview ~15+ potential AF end-users to validate need. They take this seriously. |
| **Dual-Use** | Commercial + defense applicability. AFWERX prefers dual-use because it shows market beyond government. **Our pitch is naturally dual-use** (utility / SAR / agri civilian + AF defense). |

---

## 4. Export controls (real risk for drone autonomy companies)

| Term | What it is | What to say |
|---|---|---|
| **ITAR** | International Traffic in Arms Regulations. Covers items on the **USML** (US Munitions List). Drone autonomy with certain capabilities = **USML Category VIII**. Means: no foreign hires, no foreign sales without State Dept license. | "I'm aware drone-autonomy stacks can fall under USML Cat VIII. Want to make sure we're compliant from day one — interested in your read." |
| **EAR** | Export Administration Regulations. The "lighter" controls — covers dual-use items via the **CCL** (Commerce Control List). | "Understanding ITAR vs EAR is on my homework list." |
| **DDTC** | Directorate of Defense Trade Controls. State Dept body that runs ITAR. Registration is **$2,250/yr minimum**. | "I'd register with DDTC if we go ITAR-controlled." |
| **TAA** | Trade Agreements Act. Restricts where products can be made for federal sale. Made-in-China components are a problem. | "Our hardware BOM avoids covered countries — using Pixhawk variants from Holybro (Vietnam/Taiwan) and US-made compute." |
| **Section 889 / NDAA** | Bans federal use of Huawei/ZTE/DJI/Hikvision/Hytera. Defense agencies extra-strict. **DJI ban specifically affects our market positioning.** | "DJI ban is actually tailwind for us — federal agencies need a non-DJI alternative for fleet ops." |

---

## 5. Maine APEX program details

| Term | What it is |
|---|---|
| **APEX** | Assistance to Procuring Entities & Exchanges. Formerly **PTAC** (Procurement Technical Assistance Centers). DoD-funded, free-to-business. |
| **EMDC** | Eastern Maine Development Corporation. The org that hosts Maine APEX. Bangor-based, 40 Harlow St. |
| **Procurement Counselor** | Marissa's title. Helps small businesses navigate federal contracting — proposal review, registration walk-throughs, agency targeting. |
| **Kennebec County** | Marissa's territory. Includes Augusta + Waterville (you). |
| **APEX Network** | Nationwide — ~95 APEX centers, 600+ counselors. They sometimes refer cases to specialists in other states. |

---

## 6. Drone tech terms (Marissa may know surface-level)

| Term | What it is |
|---|---|
| **BVLOS** | Beyond Visual Line of Sight. Flying drones outside what the operator can see directly. Requires FAA waiver. **Critical for SAR + powerline inspection.** |
| **VLOS** | Visual Line of Sight. Default Part 107 ops — pilot must see the drone. Limits range to ~half-mile. |
| **Part 107** | FAA rule for commercial drone ops. Requires written test ($175). **Status: Not yet — on Lucas's near-term list.** |
| **MAVLink** | The de-facto standard messaging protocol between flight controllers and ground stations. Open-source. **This is what makes our software universal.** |
| **PX4** | Open-source flight controller firmware. Industry standard. Runs on Pixhawk hardware. |
| **ArduPilot** | Older open-source flight stack — competitor to PX4, more conservative. Many existing fleets run ArduPilot. **We support both.** |
| **Pixhawk** | Open-hardware flight controller spec (Holybro, mRobotics, etc. make compatible boards). Industry standard for MAVLink-speaking drones. |
| **Pi 5 / Jetson Orin** | Companion computers — handle mission planning, video processing, ML inference on the drone. Jetson has GPU for CV. |
| **RTK GPS** | Real-Time Kinematic GPS. Centimeter-accurate positioning vs ~3-5m for standard GPS. Needed for precision tasks (survey, agri). |
| **Mesh radio** | Long-range comms (RFD900, Doodle Labs Helix). Used instead of cellular for swarm comms — more reliable, no carrier dependency. |

---

## 7. Acronym jukebox (alphabetical, for fast lookup)

- **AFRL** — Air Force Research Laboratory
- **AFWERX** — Air Force innovation arm
- **APEX** — Assistance to Procuring Entities & Exchanges (you're talking to one)
- **ArduPilot** — drone flight stack (alt to PX4)
- **BAA** — Broad Agency Announcement (the SBIR call-for-proposals doc)
- **BVLOS** — Beyond Visual Line of Sight
- **CAGE** — DoD vendor ID code
- **CCL** — Commerce Control List (under EAR)
- **CONOPS** — Concept of Operations (how you'd actually use the system)
- **D2P2** — Direct-to-Phase II
- **DDTC** — Directorate of Defense Trade Controls (runs ITAR)
- **DHS** — Dept of Homeland Security (alt agency for SBIR)
- **DoD STTR** — research-institution-partner SBIR variant
- **DUNS** — DEPRECATED, replaced by UEI
- **EAR** — Export Administration Regulations
- **EMDC** — Eastern Maine Development Corp (Marissa's employer)
- **FAA** — Federal Aviation Admin
- **GSA Schedule** — pre-negotiated gov't price list (not relevant)
- **HUBZone** — set-aside category (not relevant for you)
- **ITAR** — defense export controls
- **MAVLink** — drone messaging protocol
- **NAICS** — industry classification code (yours probably 541715)
- **NDAA Section 889** — bans Huawei/DJI/etc from federal use
- **NSF SBIR** — civilian backup track to AFWERX
- **OUSD(R&E)** — Office of Under Secretary of Defense, Research & Engineering
- **Part 107** — FAA commercial drone rule
- **Phase I/II/III** — SBIR funding stages
- **Pixhawk** — flight controller standard
- **PTAC** — old name for APEX
- **PX4** — drone flight stack
- **RTK GPS** — centimeter-accurate GPS
- **SAM.gov** — federal contractor registry
- **SBC** — Small Business Concern (you qualify)
- **SBIR** — Small Business Innovation Research
- **SDVOSB** — Service-Disabled Vet-Owned Small Business
- **STRATFI** — AFWERX big-money Phase II add-on
- **STTR** — research-partner SBIR
- **TAA** — Trade Agreements Act (country-of-origin rules)
- **TACFI** — AFWERX Phase II accelerator
- **TPOC** — Technical Point of Contact (the gov't tech rep on a contract)
- **TRL** — Technology Readiness Level (1-9 scale; we're around TRL 4)
- **UEI** — Unique Entity Identifier (SAM.gov assigns it)
- **USML** — US Munitions List (drones in Cat VIII)
- **VLOS** — Visual Line of Sight
- **WOSB** — Women-Owned Small Business

---

## 8. Common questions Marissa might ask & strong answers

> **"What's your TRL?"**
TRL 4 — components validated in lab/sim environment. Working software prototype in mock simulation, hardware integration starting May.

> **"Have you registered on SAM.gov?"**
Not yet — that's actually one of the top things I'm hoping APEX can help with. I want to do it right the first time.

> **"What's your business structure?"**
Maine LLC, formation in progress this month (May 2026). Sole owner, US citizen.

> **"Have you done customer discovery?"**
Initial conversations with [pick: rural utilities like CMP, Maine SAR teams, Kennebec County Sheriff]. Plan to formalize 15+ interviews as part of any AFWERX submission.

> **"What's your funding to date?"**
$5K self-funded for hardware. Submitted MTI Business Innovation Funding self-assessment ($25K ask) — they replied "may be a fit."

> **"Why drone autonomy?"**
Background: [Lucas — fill in your honest 1-sentence reason — engineering interest, market gap, mission, whatever]. Spent the last [X months] building a working software prototype.

> **"What agencies have you talked to?"**
None directly yet — APEX is my first formal touchpoint. Plan to use your guidance to identify which to approach first.

> **"How will you use APEX services?"**
Three things: SBIR Phase I package review before the next AFWERX window, SAM.gov walkthrough, and your read on whether other agencies (DoD STTR, DHS, DoE for grid inspection, NASA) fit alongside AFWERX.

> **"Do you have a teaming partner?"**
Currently solo. Open to teaming — would value your view on whether a Maine-based research partner (UMaine?) would strengthen our position for STTR.

> **"Are you ITAR-aware?"**
Yes — drone autonomy can fall under USML Category VIII. Want to make sure we're compliant from day one. Interested in your guidance on whether to register with DDTC pre-emptively or wait until needed.

> **"What's your timeline?"**
Maine LLC by mid-May. SAM.gov registration June. Part 107 license July. AFWERX SBIR Phase I submission whenever the next window opens (estimated June-Aug 2026). Hardware build complete summer.
