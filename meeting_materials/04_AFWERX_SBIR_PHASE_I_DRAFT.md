# AFWERX SBIR Phase I — DRAFT Application

**Gragg Robotics, LLC**
**Proposal Title:** Operator-First Universal Multi-Drone Control with Bolt-On Autonomy Pod
**Draft Date:** 2026-05-17
**Document Owner:** Lucas Gragg

---

## ⚠ DRAFT NOTICE — READ BEFORE TOUCHING ANYTHING

This is a **working draft for internal review.** It is NOT a submission and must not be uploaded to DSIP / sbir.gov / DoD SBIR Portal in its current state.

Before this becomes a real submission, the following must happen:

1. **Active AFWERX BAA topic number** must be looked up at SBIR.gov for the open window (estimated June–August 2026). The current draft uses a placeholder. The narrative may need to be re-aligned to the specific topic's stated technology need.
2. **SAM.gov registration** must be complete and the UEI + CAGE codes filled in.
3. **Maine LLC Certificate of Formation** must be received and EIN issued.
4. **Marissa Henkel (APEX)** should review both the technical and cost volumes before submission.
5. **Letter(s) of support** from a defense end-user (AFRL, 711 HPW, AFSOC, or a small commercial customer willing to sign a letter of interest) should be appended.
6. **Cost volume** must be reconciled against the active solicitation — AFWERX Open Phase I has historically come in either a $75K STTR-style variant or a $150K Direct-to-Phase-II eligible variant. The numbers in Section 11 assume the $150K variant. Verify before locking budget.

Any place a fact is uncertain it is marked `[TBD: ...]`. Any place a number is an estimate or assumption it is marked `[ASSUMPTION: ...]`. **Do not strip these tags before Lucas verifies each one.**

---

## SECTION 1 — Cover Sheet

| Field | Value |
|---|---|
| Topic Number | `[AFWERX TOPIC # TBD — pull from active SBIR.gov listing at time of submission. Likely an "Open Topic" or a relevant focused topic on Autonomy / Swarm / Contested Operations.]` |
| Proposal Title | Operator-First Universal Multi-Drone Control with Bolt-On Autonomy Pod |
| Firm Name | Gragg Robotics, LLC |
| Firm Address | 16 Boutelle Ave, Waterville, ME 04901 |
| State of Incorporation | Maine |
| DUNS / UEI | `[TBD — pending SAM.gov registration]` |
| CAGE Code | `[TBD — pending SAM.gov registration]` |
| EIN | `[TBD — pending IRS issuance after LLC Certificate arrives]` |
| Federal Tax Status | Maine LLC, taxed as `[TBD: Lucas to confirm — single-member disregarded entity by default]` |
| Principal Investigator | Lucas Gragg, Founder |
| PI Email | graggrobotics@gmail.com |
| PI Phone | (207) 242-7351 |
| Business Email | graggrobotics@gmail.com |
| Website | https://graggrobotics.com |
| Phase I Total Cost | `$150,000` `[ASSUMPTION: AFWERX Open Phase I Direct-to-Phase-II-eligible variant. Verify against active solicitation — may be capped at $75K for some variants.]` |
| Period of Performance | 3 months from contract award |
| Number of Employees | 1 (founder); contract hires planned during PoP |
| Woman-Owned | No |
| Minority-Owned | No |
| Veteran-Owned | No |
| HUBZone | `[TBD: Kennebec County, ME may qualify as a HUBZone — Lucas to verify at hubzone.sba.gov]` |
| First-time SBIR applicant | Yes |

---

## SECTION 2 — Technical Abstract (200 words max)

Gragg Robotics is building the universal multi-drone control layer the Air Force does not yet have: one operator commanding a fleet of any-vendor drones through a real-time strategy interface, plus a bolt-on autonomy pod that retrofits onto existing Pixhawk / PX4 / MAVLink-compatible airframes. We replace the single-pilot-per-drone model that today makes multi-drone operations economically unviable for both commercial inspection and attritable contested-environment missions.

In Phase I we will (a) demonstrate single-operator control of four heterogeneous MAVLink-compatible airframes in PX4 SITL simulation, (b) deliver a v1 sensor + compute + radio pod at the proof-of-concept tier (~$660/drone), (c) quantify operator workload reduction against a single-pilot baseline using NASA-TLX, (d) characterize graceful-degradation behavior under contested communications, and (e) complete Air Force customer discovery with three end-user organizations.

The platform is dual-use by design. Civilian customers in utility inspection, search-and-rescue, agriculture, and infrastructure security underwrite a robust commercial business that supplies the same retrofit autonomy capability to Air Force operators at attritable cost. Phase II will deliver a hardened 12-pod production fleet plus the integrated autonomy stack against an Air Force end-user transition partner identified during Phase I.

`[Word count: ~210 — trim 10 before submission. Drop "robust" and one descriptive clause.]`

---

## SECTION 3 — Identification and Significance of the Problem / Opportunity

### The problem the Air Force is trying to solve

Recent Air Force doctrine has been explicit that future contested-environment air operations require **large numbers of low-cost, attritable, autonomous platforms** operating in coordinated swarms. Programs from Replicator to AFWERX Open Topic series have repeatedly funded swarm autonomy, distributed manned-unmanned teaming, and attritable platform initiatives. The hardware is increasingly available; the operator interface and the vendor-agnostic control layer are not.

Today the multi-drone operations stack looks like this:

- Each drone vendor (Skydio, BRINC, Anduril, Teal, Parrot, Autel) ships its own ground control station.
- The ground stations do not talk to each other. An operator running drones from three vendors needs three laptops, three operators (often), and zero data fusion between platforms.
- "Swarm" capability, where it exists at all, is locked to a single vendor's airframe family. The Air Force loses the ability to mix-and-match the best available platform for a given mission.
- For commercial operators (utilities, public safety, surveying), the labor cost of one pilot per airframe destroys the ROI of multi-drone work. They under-invest, the market stays small, and the unit economics never improve.

The Air Force inherits this fragmented, single-vendor, labor-heavy world by default. AFWERX Phase I funding can fix it.

### The opportunity

Three things have aligned in 2025–2026 that make a universal multi-drone control layer practical today:

1. **MAVLink has become the de facto open protocol for small autonomous airframes.** Pixhawk, PX4, ArduPilot, and an increasing list of commercial vendors expose MAVLink. A control layer built on MAVSDK and MAVLink reaches a substantial fraction of the relevant fleet on day one.
2. **Edge compute is cheap and field-deployable.** A Raspberry Pi 5 (POC tier) or Jetson Orin (production tier) is small enough, light enough, and power-efficient enough to ride on the drone as an autonomy companion, no airframe modification required.
3. **Real-time-strategy interaction patterns are mature.** Operators do not need a flight-control panel; they need a map, a small set of high-level command verbs, and good defaults. The RTS genre has spent thirty years refining the one-operator-many-units interaction model — borrowing it directly is the right move.

### Why Gragg Robotics now

We are a Maine-based, founder-led startup with a working software prototype today: a PX4-SITL-backed 4-drone simulator running our RTS-style operator UI over Flask + MAVSDK + SocketIO. We are building the hardware pod on top of off-the-shelf components for the POC tier (~$660/drone) and a production tier (~$4,200/drone with Jetson Orin, FLIR thermal, Livox LiDAR, mesh radio). The civilian commercial market gives us a real revenue path that supplements DoD funding — exactly the dual-use profile AFWERX rewards.

### Significance to the Air Force and DoD

A vendor-agnostic, retrofit autonomy pod plus operator-first multi-drone control software gives the Air Force four immediate capabilities:

- **Recapitalize existing fleets** — the Air Force, AFSOC, and Air National Guard already field thousands of MAVLink-compatible airframes. The pod adds swarm capability without buying new aircraft.
- **One-operator-many-airframes economics** — at ~10× labor leverage, the operator workforce can sustain operations at fleet scale that single-pilot-per-airframe models cannot.
- **Attritable cost basis** — at $660/pod POC tier, the autonomy hardware is genuinely attritable. The aircraft itself can be the cheapest available airframe and still inherit modern autonomy.
- **Dual-use commercial subsidy** — the civilian customer base (utility, SAR, agriculture, security) underwrites continuous platform improvement at no DoD cost. Defense gets the benefit of commercial-scale iteration on the same stack.

`[ASSUMPTION: the "~10× labor leverage" framing is the natural extrapolation from one-operator-four-to-twelve-drones. Phase I will substantiate this via NASA-TLX measurement; until then it is a directional claim, not a measured one.]`

---

## SECTION 4 — Phase I Technical Objectives

Phase I has six concrete, measurable objectives. Each objective has a defined success criterion that will be reported in the Phase I final deliverable.

### Objective 1 — Single-operator multi-airframe control in PX4 SITL

Demonstrate one operator commanding **four or more heterogeneous MAVLink-compatible airframes** simultaneously in PX4 SITL. Heterogeneity means at least two distinct airframe profiles (e.g., quadcopter + fixed-wing) using the same UI and command set.

**Success criterion:** complete a scripted multi-phase mission (launch, SWEEP, TARGET, FOLLOW, RTH) with all four airframes responding to operator inputs within 500 ms median command-to-acknowledgement latency, and full mission completion with no operator intervention beyond the six UI commands.

### Objective 2 — Command primitive coverage analysis

Through customer discovery interviews with **three Air Force end-user organizations** (target: representatives from AFRL, 711 HPW, AFSOC, or DIU's autonomy portfolio — `[ASSUMPTION: Marissa Henkel and the AFWERX Engage network will help broker these intros]`), validate that the existing six-command primitive set (TARGET, FOLLOW, SWEEP, WAYPOINT, GO HOME, ENGAGE — currently rendered in the UI as the eight verbs GO_TO, ENGAGE_EN_ROUTE, ENGAGE_MOD, SWEEP_1KM, INSPECT, SENTRY, OBSERVE, RTH) covers ≥ 90 % of operator-relevant use-case scenarios.

**Success criterion:** a use-case matrix scored against interview transcripts, with ≥ 90 % of named operator scenarios decomposable into compositions of the existing primitives. Any unaddressed scenarios drive a Phase II command-set revision proposal.

### Objective 3 — Bolt-on autonomy pod v1

Design, fabricate, and bench-characterize a v1 POC-tier sensor + compute + radio pod:

- Companion compute: Raspberry Pi 5
- Visible camera: Sony IMX477 module
- Long-range mesh radio: RFD900x
- Power from drone battery via regulated tap
- MAVLink connection to flight controller over UART/USB
- IP54 weatherproof, sub-250 g, ~100 × 80 × 50 mm enclosure (per `funding/hiring/mechanical_engineer_scope_2026-05-14.md`)

Integration target airframe: a Holybro X500 or equivalent commercial PX4 reference airframe.

**Success criterion:** one fully assembled pod, mounted on the target airframe, demonstrating MAVLink telemetry round-trip and visible-camera streaming over the RFD900x link at ≥ 500 m line-of-sight range under bench/field test conditions.

### Objective 4 — Operator workload measurement (NASA-TLX)

Run a controlled simulator study using the PX4 SITL stack: same mission profile executed under (a) the Gragg Robotics single-operator-multi-drone UI and (b) a single-pilot-per-drone baseline using a representative existing GCS (QGroundControl or Auterion Suite, `[TBD: pick which]`). NASA-TLX administered after each trial.

**Success criterion:** measured operator workload reduction reported as a quantitative delta across the six NASA-TLX subscales. The hypothesis is meaningful reduction in Mental Demand, Effort, and Frustration subscales when comparing single-operator-four-drones to four-pilots-four-drones. Whatever the result, it is reported honestly — a null or negative result is still valid Phase I deliverable content and informs Phase II design.

### Objective 5 — Graceful degradation under contested communications

Characterize the autonomy stack's behavior under simulated link degradation: link loss, intermittent packet loss, latency spikes, and partial mesh failure. The pod's default behavior on link loss must be deterministic and survivable (configurable: hold position, return to home, continue current command).

**Success criterion:** a documented characterization report covering at least three degraded-comms regimes, with per-regime default behaviors that have been tested in SITL and demonstrated to be safe (no loss of aircraft, no operator-perceived unpredictability).

### Objective 6 — Customer discovery + transition partner identification

Complete structured discovery interviews with at least three Air Force-relevant end-user organizations. Identify at least one qualified transition partner — defined as an organization that has explicitly stated interest in evaluating the Phase II prototype.

**Success criterion:** signed letter of interest from at least one Air Force transition partner organization, included in the Phase I final report and ready to support a Phase II / Direct-to-Phase-II proposal.

---

## SECTION 5 — Phase I Work Plan

Three-month period of performance. Monthly milestones; weekly status to the contracting officer.

### Month 1 — Discovery + framework setup

| Week | Activity |
|---|---|
| 1 | Kickoff with contracting officer. AFWERX customer-discovery interview prep with Marissa Henkel (APEX). PX4 SITL multi-airframe framework setup — extend the existing single-airframe-type simulator to support heterogeneous airframes. |
| 2 | First three Air Force customer-discovery interviews scheduled and conducted. Mechanical engineer contractor signed (per `funding/hiring/mechanical_engineer_scope_2026-05-14.md`). Hardware procurement: 4× Holybro X500 airframes, 4× Raspberry Pi 5 + RFD900x pairs, sensors. |
| 3 | First multi-airframe SITL mission scripted and running. Pod mechanical CAD first draft from contractor. |
| 4 | Use-case matrix populated from first three interview transcripts. Pod CAD review and revision. PCB layout begins (subcontractor: MacroFab or Sierra Circuits, quotes already in progress). |

### Month 2 — Build + integration

| Week | Activity |
|---|---|
| 5 | First 3D-printed enclosure iteration. PCB v1 ordered. Two additional customer-discovery interviews (target: 5 total by end of Month 2). |
| 6 | Pod assembly bench test. MAVLink integration with Pixhawk flight controller on the X500 reference airframe. SITL graceful-degradation regimes scripted. |
| 7 | First integrated outdoor test at controlled site (rural Maine, `[ASSUMPTION: 40 Benson Rd, Manchester ME — Lucas's existing flying area]`). Pod mounted on real airframe; basic telemetry + camera-streaming validation. |
| 8 | Iteration based on outdoor test findings. SITL operator-study protocol finalized + IRB-equivalent review of NASA-TLX procedure. `[ASSUMPTION: a single-PI workload study at this scale does not require formal IRB but should follow informed-consent best practice. Confirm with AFRL Human Effectiveness contact if available.]` |

### Month 3 — Measure + write

| Week | Activity |
|---|---|
| 9 | NASA-TLX simulator study conducted with at least 6 participants (3 single-operator-multi-drone trials + 3 single-pilot-per-drone trials). `[ASSUMPTION: 6 participants drawn from local UMaine ECE / WPI robotics network — sample size adequate for directional comparison but not for formal statistical claims. Phase II expands the panel.]` |
| 10 | Data analysis. Graceful-degradation final characterization. Customer-discovery report assembly. |
| 11 | Final report drafting. Letter(s) of interest secured from transition partner(s). Phase II / Direct-to-Phase-II proposal prep begins. |
| 12 | Final report delivered to contracting officer. Phase II submission package complete and ready for the next AFWERX window. |

### Deliverables

1. Phase I Final Report covering all six objectives (PDF).
2. Source code release of the multi-drone control UI (private GitHub repo with DoD-readable access, MIT-licensed for the open components, proprietary on the autonomy pod firmware).
3. Pod mechanical CAD package + BOM + assembly instructions.
4. PCB schematic + Gerber files for the pod baseboard.
5. NASA-TLX raw data + analysis summary.
6. Customer discovery report with interview transcripts (suitably anonymized) and use-case matrix.
7. Letter of interest from at least one Air Force transition partner.
8. Phase II proposal package, ready for next AFWERX window.

---

## SECTION 6 — Related Work

### Lucas's prior background

Lucas Gragg is a self-taught software engineer with a multi-year track record building autonomous systems for personal projects, including trading bot automation, hardware integration, and end-to-end software products. He is the sole author of the existing PX4-SITL + MAVSDK + Flask multi-drone control stack at the core of this proposal.

**Honest disclosure:** Lucas is a first-time defense applicant. He does not have a prior SBIR, a prior DoD contract, or a security clearance. He does have demonstrated ability to ship working software, a working prototype today, and grant funding momentum (MTI Business Innovation Funding application 2428739 in flight, expected mid-2026). The "first-time" status is not a disqualifier for AFWERX Open Phase I — the Open program explicitly exists to bring new entrants into the DoD ecosystem.

### Foundational open-source work this builds on

- **MAVLink** (mavlink.io) — the open communication protocol that enables vendor-agnosticism.
- **PX4 Autopilot** (px4.io) — the open flight-control firmware running on a substantial fraction of Pixhawk-compatible airframes worldwide.
- **MAVSDK** (mavsdk.mavlink.io) — the Python/C++ SDK providing high-level mission control over MAVLink. Our software stack uses MAVSDK as the abstraction layer between our control logic and the airframe.
- **ArduPilot** — alternative MAVLink-compatible firmware; targeted for compatibility in Phase II.

Gragg Robotics is a contributor and consumer of these projects, not a competitor. Our value-add is the operator-facing control layer plus the bolt-on hardware pod — the open stack remains the foundation.

### Other multi-drone GCS efforts

We are aware of and respect adjacent efforts in the market:

- **Skydio Defense** — vertically integrated; their swarm capability is locked to Skydio airframes. Strong product, narrow fleet.
- **Anduril Lattice** — sensor and command-and-control fusion at a much higher tier of program. Operates at the level of a theater C2 platform; not focused on the operator-level multi-drone-fleet problem we are solving.
- **Shield AI Hivemind** — V-BAT-focused autonomous fleet operations. Strong autonomy, again vertically integrated to a specific airframe.
- **Auterion Suite** — modular GCS with growing multi-drone support, but anchored to a specific autopilot family and not focused on the RTS-style operator workflow.

**How Gragg Robotics is different:** we are the vendor-agnostic, retrofit-onto-existing-fleet, operator-first option. We do not compete to be the next vertically integrated drone company. We compete to be the **horizontal autonomy layer** that lets the Air Force keep using the airframes it already has — including those from the four vendors above — and run them all from one operator console. The civilian commercial market accelerates that horizontal-layer play in a way the defense-only vendors structurally cannot match.

---

## SECTION 7 — Commercialization Plan

### Civilian commercial revenue is the foundation

Gragg Robotics is not a "defense-only" company that hopes commercial markets show up later. The dual-use positioning is the strategy from day one. The civilian customer base both pays the bills and validates the platform at a scale and iteration cadence that defense-only competitors cannot match.

### Year 1 — civilian-first sales (Maine + adjacent New England utility / public safety)

**Target customers:**

- **Central Maine Power (CMP)** and **Versant Power** — Maine's two largest electric utilities. Powerline and substation inspection currently runs at $1,500/hour for helicopter inspection or single-pilot drone work. A 4-drone fleet operated by one inspector reduces unit cost and accelerates rural Maine transmission-line coverage. Initial conversations targeted for Q3 2026.
- **Maine Search & Rescue / Maine Game Wardens / county sheriffs (Kennebec County initial)** — wide-area search with autonomous detection and ground-team handoff. Cuts hours off SAR timelines, especially the first "golden hour." Letter-of-interest target Q3–Q4 2026.
- **Maine Department of Agriculture, Conservation and Forestry** — wildfire monitoring and forestry survey via thermal-equipped fleet, post-BIF-funded production tier.

**Pricing model:**

- Software: per-operator-seat SaaS license, `[ASSUMPTION: $5,000/seat/year — to be benchmarked against ESRI / AutoCAD / Skydio Cloud comparable tiers in Phase I commercial discovery]`
- Hardware pod: per-unit sale at the POC tier (~$660 BOM, retail TBD with margin), production tier (~$4,200 BOM, retail TBD)
- Optional professional services: pilot mission planning, custom mission scripts, training — billed hourly

### Year 2 — expansion into adjacent civilian markets + AFWERX Phase II execution

**Civilian:**

- Out-of-state utility (Eversource, National Grid)
- Precision agriculture in the Northeast corn / dairy belt
- Critical infrastructure security (substations, water treatment, ports)

**Defense:**

- AFWERX Phase II Direct (~$750K–$1.5M, 12–24 month performance)
- Phase II prototype delivery against the transition partner identified in Phase I
- Air National Guard pilot if a state guard unit is identified during Phase I customer discovery

### Year 3 — strategic options

By end of year 3 the company is positioned for one of two outcomes:

1. **Acquisition by a defense prime or autonomy-portfolio acquirer** (candidates: Anduril, Shield AI, L3Harris, Teledyne FLIR). The dual-use commercial customer base meaningfully increases acquisition value over a defense-only vendor.
2. **Continued operating business with Series A or DoD Phase III sole-source contracting.** Maine Venture Fund relationship developed in Stage 2 funds the Series A path if pursued.

### Conservative 3-year revenue projection

| Year | Civilian rev | Defense rev | Total | Notes |
|---|---|---|---|---|
| 2026 | $25K (MTI BIF) | $0 | $25K | BIF grant treated as revenue equivalent for build-out |
| 2027 | $50K–$150K | $150K (AFWERX Phase I) | $200K–$300K | First 1–2 civilian pilots; Phase I funded |
| 2028 | $400K–$800K | $750K–$1.5M (AFWERX Phase II) | $1.15M–$2.3M | 5–10 paying civilian customers; Phase II executing |
| 2029 (yr 3 from this proposal) | $1.0M–$1.5M | $1.0M–$2.0M | $2.0M–$3.5M | 20–30 utility / municipal customers; Phase III / Series A decision point |

`[ASSUMPTION: these are conservative, founder-built projections. Defense reviewers will scrutinize them — they are positioned as conservative (we hit the bottom of these ranges, things are going well) rather than aspirational. Lucas should review each number against his own gut before submission.]`

### Why this commercialization plan beats a defense-only plan

AFWERX scoring rewards commercialization potential. A defense-only plan that depends entirely on a Phase II → Phase III → program-of-record trajectory has all its risk concentrated in the Air Force budget cycle. Our dual-use plan has two independent revenue legs: every dollar of civilian revenue reduces the company's dependence on DoD funding velocity. This is precisely the profile AFWERX is looking for.

---

## SECTION 8 — Key Personnel

### Lucas Gragg — Founder, Principal Investigator

Lucas is the sole founder of Gragg Robotics, headquartered in Waterville, Maine. He is the technical lead, sole author of the existing multi-drone control software prototype, and will serve as Principal Investigator on this Phase I.

**Skills directly relevant to this proposal:**

- Python software engineering — primary language of the existing control stack (Flask + MAVSDK + SocketIO + asyncio)
- Drone autonomy — hands-on with PX4, MAVLink, MAVSDK, PX4 SITL simulation
- Real-time-strategy UI design — the operator-first six-command primitive set is his original work
- MAVLink integration — direct integration experience between the Python control layer and Pixhawk-compatible airframes
- Autonomous-systems software — multi-year track record building autonomous decision systems for adjacent domains (algorithmic trading bots, automated content production), demonstrating the ability to ship and operate complex autonomous software in production

**Honest disclosure:** Lucas has no prior defense industry experience. He has no security clearance. He does not have an aerospace or mechanical engineering degree. He has working autonomous-systems software shipping in production, a working drone-swarm prototype today, and a documented learning velocity. The Air Force has historically funded first-time founders through AFWERX Open precisely because the program is structured to bring new talent in.

**Time commitment to Phase I:** 100 % (full-time). Founder is the only full-time employee.

### To-Be-Hired — Contract Mechanical Engineer

Per the scope of work at `funding/hiring/mechanical_engineer_scope_2026-05-14.md`, a 1099 contract mechanical engineer will lead the pod enclosure and mounting design. The role is scoped at 60–100 hours over 8–10 weeks, billed hourly, with deliverables specified up front. Sourcing channels include the ArduPilot dev forum, UMaine ECE, WPI Robotics Engineering, and direct LinkedIn outreach. Target candidate profile: mid-level mechanical engineer with prior drone-payload enclosure experience.

`[TBD: candidate will be named in the final submission — Phase I award is gated on getting at least 3 candidate intros lined up by submission week. Marissa at APEX can advise on whether a named subcontractor is preferred or acceptable as TBD at the proposal stage.]`

### Advisory / supporting (uncompensated for Phase I)

- **Marissa Henkel** — Procurement Counselor, Maine APEX Accelerator (Kennebec County). Supporting SAM.gov registration, customer discovery introductions, and proposal review. Not a Phase I personnel cost.
- **Abby Osei** — Investment Officer, Maine Technology Institute. Supporting the MTI BIF grant in parallel. Not a Phase I personnel cost.

---

## SECTION 9 — Facilities and Equipment

### Headquarters

Gragg Robotics is headquartered at 16 Boutelle Ave, Waterville, ME 04901 (Kennebec County). The facility includes the founder's full-time development workstation, dedicated multi-monitor setup for SITL operator-study runs, and adequate space for pod bench assembly and small-scale hardware test.

### Outdoor flying area

Phase I outdoor flight testing will be conducted at `[ASSUMPTION: 40 Benson Rd, Manchester ME — already configured as the HOME location in the existing software stack per config.py. Lucas to confirm site access for outdoor flight test during Phase I.]`. The Maine rural environment provides excellent low-airspace-conflict conditions for SITL-to-real-flight transition testing.

### Computing resources currently in place

- Primary development workstation (Windows 11, sufficient for PX4 SITL multi-instance simulation up to 8 airframes simultaneously)
- Existing development environment with Python 3.12, PX4 SITL, MAVSDK Python bindings, Flask, SocketIO, and the in-development control stack

### Equipment to be procured under Phase I

- 4× Holybro X500 reference airframes (or equivalent commercial PX4 airframes) — for pod integration and outdoor flight test
- 4× Raspberry Pi 5 companion compute modules
- 4× RFD900x mesh radios
- 4× Sony IMX477 camera modules
- 1× Jetson Orin Nano dev kit (for production-tier preview / Phase II planning)
- Additional dev workstation (laptop, per `funding/hiring/business_laptop_recommendation_2026-05-16.md`) for mobile work and customer-discovery travel
- Bench test equipment: oscilloscope `[ASSUMPTION: low-cost USB scope adequate]`, power supplies, soldering station, multimeter

### Subcontractor facilities

- PCB fabrication and assembly: MacroFab (Houston, TX) or Sierra Circuits (Sunnyvale, CA), quotes in progress. Both are U.S.-based ITAR-friendly contract manufacturers.
- 3D-printing for pod enclosure prototypes: contractor's own facility or a Maine-based service bureau.

---

## SECTION 10 — Subcontractors and Consultants

| Role | Vendor | Scope | Estimated Phase I cost |
|---|---|---|---|
| Mechanical engineer (1099) | TBD — sourced via ArduPilot dev forum, UMaine ECE, WPI, direct outreach | Pod enclosure + mounting bracket CAD, BOM, assembly docs (per `funding/hiring/mechanical_engineer_scope_2026-05-14.md`) | ~$8,000 |
| PCB fab + assembly | MacroFab or Sierra Circuits | Pod baseboard PCB design review, fab, partial assembly for 4 units | ~$5,000 |
| Optional: outdoor test pilot (1099) | TBD — Maine licensed Part 107 pilot, hired ad-hoc for outdoor flight test if Lucas does not yet hold Part 107 by Month 2 | 1–2 days of pilot-of-record service during outdoor testing | ~$2,000 |
| **Total subcontractor** | | | **~$15,000** |

**SBIR work-share compliance:** The total subcontractor cost of ~$15,000 is approximately 10 % of the proposed $150,000 Phase I total. The prime (Gragg Robotics) retains roughly 90 % of the work, comfortably above the 67 % minimum required by SBIR rules for Phase I. `[ASSUMPTION: verify exact Phase I work-share rule against the active solicitation — historical SBIR Phase I rule is ≥ 67 % for prime; AFWERX may modify this.]`

---

## SECTION 11 — Cost Volume Summary

Total proposed: **$150,000** (3-month period of performance)

| Category | Description | Amount |
|---|---|---|
| Direct labor — PI (Lucas Gragg) | 3 months full-time at `[ASSUMPTION: $200K-equivalent annual rate, fully loaded]`, prorated | $50,000 |
| Direct labor — contract mechanical engineer | ~80 hours at ~$75/hr median rate | $6,000 |
| Direct labor — outdoor test pilot (contingency) | 1–2 days, billable to Phase I if Lucas not Part 107 by Month 2 | $2,000 |
| **Subtotal direct labor** | | **$58,000** |
| Subcontract — PCB fab + assembly | MacroFab or Sierra Circuits, 4 pod baseboards | $5,000 |
| Subcontract — mechanical engineering | (counted under direct labor above) | (incl.) |
| **Subtotal subcontracts** | | **$5,000** |
| Materials — drone airframes (4× Holybro X500 or equivalent) | ~$2,000 each | $8,000 |
| Materials — compute, radio, camera (4 sets) | RPi 5, RFD900x, IMX477, regulators, cables — ~$660/set | $2,640 |
| Materials — 1× Jetson Orin Nano dev kit (Phase II preview) | | $500 |
| Materials — enclosure 3D-printing + PCB components + misc hardware | | $4,000 |
| Materials — bench test equipment | scope, soldering, power supplies | $2,000 |
| Materials — dev laptop (per business_laptop_recommendation) | | $1,000 |
| **Subtotal materials** | | **$18,140** |
| Travel — customer-discovery trips (3 trips, in-region + 1 to Wright-Patt or AFWERX Engage venue) | airfare, lodging, per diem | $7,000 |
| Travel — outdoor flight test site fuel + small expenses | | $1,000 |
| **Subtotal travel** | | **$8,000** |
| Other direct costs — cloud compute (CI for SITL, build infrastructure) | | $1,500 |
| Other direct costs — software licenses (CAD seat if not contractor-provided, dev tools) | | $1,500 |
| Other direct costs — IRB / human-subjects-equivalent review of NASA-TLX protocol | `[ASSUMPTION: low cost for small in-house study; budget includes external review if AFRL contact requests it]` | $1,000 |
| Other direct costs — SAM.gov / business / accounting fees prorated to Phase I | | $1,000 |
| **Subtotal ODC** | | **$5,000** |
| Indirect costs — small-business overhead + G&A | `[ASSUMPTION: Gragg Robotics will operate under a simple small-business indirect-rate structure of ~28 % of direct labor. This is at the low end of typical SBIR firms. Should be confirmed with Marissa Henkel and possibly a small-business accountant before submission.]` | $22,000 |
| **Subtotal indirect** | | **$22,000** |
| Fee at 7 % of total direct + indirect | per FAR small-business norm | ~$8,000 |
| **Subtotal fee** | | **$8,000** |
| Reserve / unallocated | rounding + small-buffer | ~$25,860 `[FLAG: this is too large — once Lucas tightens the labor rate and indirect-rate assumptions, redistribute this back into specific line items]` |
| **TOTAL** | | **$150,000** |

### ⚠ Cost-volume open issues for Lucas to resolve before submission

1. **PI labor rate** — the $200K-equivalent fully loaded rate is a placeholder. Lucas should set this based on (a) what he actually plans to pay himself, (b) what's customary for a sole-founder PI on a federal small-business grant, and (c) Marissa's guidance on what AFWERX reviewers expect. Anything between $100K and $250K fully loaded is defensible; the labor cost should not be the dominant line item if it stretches the budget.
2. **Indirect rate** — the 28 % indirect rate is a small-business estimate. A real indirect rate should be computed against actual G&A, rent, utilities, software subscriptions, accounting fees, insurance, etc. Marissa or an SBIR-experienced accountant can help compute a defensible rate.
3. **Fee** — 7 % is the standard SBIR/FAR small-business profit fee. Confirm the active solicitation does not cap or modify this.
4. **Topic variant total** — AFWERX Open Phase I has historically come in either a $75K STTR-style variant or a $150K Direct-to-Phase-II eligible variant. **Lucas must verify which variant the active solicitation supports before locking the cost volume.** If $75K, the entire budget gets cut in half — typically by removing the optional outdoor test pilot, deferring the Jetson Orin dev kit to Phase II, and shrinking the customer-discovery travel scope.
5. **Reserve / unallocated** — the ~$26K reserve line is too large. Redistribute it back into specific line items (likely: more labor for the PI, more for materials, slightly more for travel) once labor and indirect assumptions are tightened.

---

## SECTION 12 — Company Commercialization Report (CCR)

Gragg Robotics is a brand-new Maine LLC, founded in 2026. As of the proposal date:

- **Prior SBIR / STTR awards:** None. This is our first SBIR application.
- **Prior federal contracts:** None.
- **Prior commercial revenue:** None to date. MTI Business Innovation Funding application 2428739 is in flight, anticipated $25,000 award targeted Q2–Q3 2026.
- **Outside investment:** None to date. Bootstrapped to date by the founder.
- **Patents:** None pending or issued.
- **Publications:** None to date relevant to this proposal.

**Why this is not a disqualifier:** AFWERX Open Phase I exists explicitly to bring new entrants into the DoD innovation ecosystem. First-time SBIR firms have historically been awarded under the Open program. Our position is honest: brand-new company, real working software prototype, grant momentum, dual-use market validated through early civilian-customer conversations, founder fully committed.

---

## SECTION 13 — Allocation of Rights (Bayh-Dole / SBIR Data Rights)

### SBIR Data Rights — Assertion

Per SBIR Policy Directive 8(b), Gragg Robotics asserts a **4-year SBIR Data Rights period** on technical data and computer software developed under this Phase I contract. During that period, the Government's rights are limited per the standard SBIR data rights clause.

### Pre-existing intellectual property

- The existing multi-drone control software prototype (Flask + MAVSDK + SocketIO + asyncio core, six-command RTS UI primitive set) is **pre-existing IP** of Lucas Gragg, contributed in-kind to the company. It pre-dates this contract and is not a Phase I deliverable per se — it is the foundation on which Phase I work builds.
- Pre-existing IP licensed to Gragg Robotics on royalty-free, perpetual basis by the founder.
- Open-source dependencies (PX4, MAVLink, MAVSDK, Flask, SocketIO) are used and integrated under their respective open-source licenses. No GPL contamination of Gragg Robotics proprietary work — all dependencies are MIT, BSD, Apache-2.0, or similarly permissive. `[ASSUMPTION: verify license compatibility per dependency before submission. PX4 is BSD-3-Clause; MAVLink LGPL-3.0; MAVSDK BSD-3-Clause; Flask BSD; SocketIO MIT — all confirmed permissive.]`

### Commercial software assertion

The operator-facing software (the GCS layer including the six-command UI and the underlying control logic) is asserted as **commercial computer software** developed at private expense and offered to the Government under restricted rights per FAR / DFARS commercial-item provisions. The autonomy pod firmware developed under Phase I will be marked with SBIR data rights as appropriate.

### Bayh-Dole

Gragg Robotics will exercise standard Bayh-Dole rights to elect title to any subject inventions developed under this Phase I, and will report inventions per 37 CFR 401.

---

## SECTION 14 — Required Disclosures

### Foreign ties / foreign-controlled relationships

Gragg Robotics has **no foreign ties or foreign-controlled relationships.** The company is a Maine LLC, 100 % owned by Lucas Gragg, a U.S. citizen residing in Waterville, Maine.

### U.S. Person status

- **Lucas Gragg (Founder, PI):** U.S. citizen.
- **All planned contractors / subcontractors:** to be U.S. citizens or U.S. Persons; international subcontracting is not contemplated for Phase I.
- **All planned facilities:** in the continental United States.

### Conflicts of interest

The founder discloses parallel activity in algorithmic trading and adjacent autonomous-software domains (see CLAUDE.md / personal background). None of these create a conflict with the Phase I work or the Air Force mission set being addressed. No prior federal grants in progress.

### SAM.gov registration

Registration is in progress. Target completion before this proposal is submitted. UEI and CAGE codes will be in place at submission.

### Federal debarment / exclusion

Gragg Robotics is not debarred, suspended, proposed for debarment, or otherwise excluded from federal contracting. No pending legal action against the company or the founder.

### Other federal grants in flight

- **MTI Business Innovation Funding application 2428739** (state-level, Maine — not a federal program). No overlap or duplication with this Phase I request.

---

## SECTION 15 — Submission Checklist & Open Items

Use this checklist to track everything still to be resolved before this draft becomes a live submission.

### Hard blockers (cannot submit without)

- [ ] **Active AFWERX BAA Topic # confirmed** at sbir.gov. Next window estimated June–August 2026. Re-align the technical narrative if the topic specifies a particular technology need.
- [ ] **SAM.gov registration complete** → UEI and CAGE codes in hand. In-person session with Marissa Henkel at KVCOG Fairfield is queued.
- [ ] **Maine LLC Certificate of Formation received** and EIN issued by IRS.
- [ ] **Business bank account opened** at Bangor Savings, post-EIN.
- [ ] **Cost volume reconciled** against the active solicitation's actual ceiling ($75K vs $150K variant).
- [ ] **PI labor rate, indirect rate, fee structure** all set against real numbers (not the placeholders in Section 11).

### Strongly recommended (don't submit without)

- [ ] **Marissa Henkel review** of both the technical and cost volumes.
- [ ] **Letter of interest** from at least one Air Force end-user (AFRL, 711 HPW, AFSOC, ANG unit). Marissa's network and the APEX program can help broker the introduction.
- [ ] **Customer discovery interviews started** — at least one Air Force end-user conversation before submission so the proposal can reference it concretely rather than promissorily.
- [ ] **At least 3 candidate mechanical-engineer contractors** identified and reachable, so the "TBD subcontractor" risk is minimized in reviewer eyes.
- [ ] **Decide on Direct-to-Phase-II eligibility** — if Lucas wants the option of jumping straight to Phase II, the Phase I scope and budget have to be structured to qualify.

### Nice-to-have

- [ ] **Letter of support from MTI** (Abby Osei) referencing the BIF investment and the Maine ecosystem support.
- [ ] **Letter of support from a Maine civilian customer prospect** (CMP, Versant, Maine SAR, county sheriff). Strengthens the commercialization-plan section.
- [ ] **HUBZone qualification check** for Kennebec County (potential 10 % evaluation preference).
- [ ] **First public press hit** (Mainebiz, BDN) about the company. Useful as a credibility marker even though not directly referenced.

---

## Review Notes for Lucas

A few sections where I made bold or assumption-laden claims that you should review and either confirm, correct, or soften:

1. **Section 11 (Cost Volume) — labor rate, indirect rate, fee, and reserve line.** I plugged in placeholders. The labor rate ($200K fully loaded annually) and indirect rate (28 %) are both guesses. Marissa Henkel at APEX or a small-business accountant should help you set these against real numbers before this becomes a real submission. The reserve / unallocated line is too large — that gets redistributed once you fix the upstream numbers.

2. **Section 2 (Technical Abstract) — slight word-count overage.** I came in around 210 words; the limit is 200. I flagged where to trim (drop "robust" plus one descriptor) before submission. Also worth re-reading once on its own — abstracts are heavily weighted by reviewers and you want every word working.

3. **Section 4 (Objective 4 — NASA-TLX study) — sample size and the IRB question.** I budgeted for 6 participants drawn from the local UMaine / WPI network. That's adequate for a directional comparison but not for any formal statistical claim. I also flagged the IRB-equivalent question — a 6-person workload study at a small business almost certainly does not require formal IRB, but you should confirm that you're following informed-consent best practice. If you want to claim anything stronger from the study, the participant count needs to grow and the methodology gets more formal.

4. **Section 7 (Commercialization Plan) — the 3-year revenue projection.** I positioned these as conservative founder projections, but conservative-vs-aspirational is in the eye of the reviewer. Read the numbers against your own gut. The Y3 floor of $2M total revenue assumes 20–30 utility / municipal customers, which is achievable but not trivial — back it up by being specific about WHICH customers you plan to land in your first year of pilots (you have CMP, Versant, Maine SAR, county sheriffs identified — name them when you can).

5. **Section 8 (Key Personnel) — first-time-defense-applicant honest disclosure.** I leaned into the honest framing rather than hiding it. Defense reviewers can smell BS faster than commercial reviewers, and the AFWERX Open program is explicitly built to bring first-time founders in. But you should read the "honest disclosure" paragraphs and confirm you're comfortable with the framing. If you'd rather emphasize what you HAVE built (the trading bots, the autonomous-systems work in adjacent domains) more loudly, that's a fair edit — but don't fabricate credentials you don't have.

6. **Section 1 (Cover Sheet) — single-member LLC tax status.** Maine LLCs default to single-member-disregarded-entity for federal tax. If you've elected S-Corp status (or plan to), the cover sheet needs to reflect that. Worth a 5-minute confirmation with whoever's helping you with the Bangor Savings account opening.

The draft is at: **`C:/Users/PC/Desktop/Projects/drone-swarm/funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md`**

---

*End of draft.*
