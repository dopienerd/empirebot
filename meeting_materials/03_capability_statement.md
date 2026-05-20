# Capability Statement — Gragg Robotics

> **Note:** This is the standard 1-page document every federal contractor maintains. Marissa will almost certainly ask for one — having it ready tells her you're prepared. Format is industry-standard: company info top, core competencies + differentiators + experience as side-by-side blocks, contact at the bottom. PDF version recommended (use Word/LibreOffice → export PDF).
>
> **Status of fields:**
> - **TBD** = not yet established (e.g., UEI before SAM.gov registration)
> - **DRAFT** = my best guess, Lucas should confirm/replace
>
> Once SAM.gov registration is done and the LLC is formed, regenerate this with real values.

---

## GRAGG ROBOTICS

**Universal Multi-Drone Control Systems**

> *One UI. Any drone. Any mission.*

---

### Company Profile

| Field | Value |
|---|---|
| Legal Name | Gragg Robotics, LLC *(Maine LLC, formation in progress May 2026)* |
| DBA | Gragg Robotics |
| Founder / CEO | Lucas Gragg |
| Address | 16 Boutelle Ave, Waterville, ME 04901 |
| Phone | (207) 242-7351 |
| Email | lukegragg@gmail.com |
| Website | TBD |
| **UEI** (SAM.gov) | **TBD — registering 2026** |
| **CAGE Code** | **TBD — pending SAM.gov** |
| **NAICS** (primary) | **541715** — Research & Development in the Physical, Engineering, and Life Sciences |
| NAICS (secondary) | 336411 (Aircraft Mfg) · 541330 (Engineering Services) · 541512 (Computer Systems Design) |
| Small Business | Yes (sole proprietor / Maine LLC, < 500 employees) |
| Set-Aside Categories | None claimed |
| Cage Code | TBD |
| Year Established | 2026 |

---

### Core Competencies

- **Multi-drone autonomy software** — RTS-style operator interface for fleets of 4–12 drones, MAVLink-native, vendor-agnostic
- **Universal hardware integration** — bolt-on sensor + control pods compatible with any Pixhawk / PX4 / ArduPilot airframe
- **Mission-level control primitives** — TARGET, FOLLOW, SWEEP, WAYPOINT, GO HOME, ENGAGE — abstracted from low-level flight control
- **Ground-station systems** — Flask + WebSocket real-time telemetry dashboards, sub-second command latency
- **Simulation-to-hardware pipeline** — same control software runs in PX4 SITL simulation and on production hardware

### Differentiators

- **Vendor-agnostic by design** — works with any MAVLink-compatible flight controller, not locked to a single drone manufacturer
- **Solo-operator economics** — designed for one operator commanding 4–12 drones simultaneously, ~10× labor leverage vs single-pilot models
- **Defense + civilian dual-use** — same platform serves DoD/AFWERX use cases and commercial verticals (utility inspection, SAR, agriculture)
- **Maine-based with rural test environment** — natural fit for BVLOS development, low-cost ops, no urban-airspace constraints
- **Open-stack foundation** — built on PX4, MAVSDK, MAVLink — no proprietary protocol lock-in, future-proof against vendor changes

### Technical Stack

- **Flight control**: PX4 / ArduPilot / Pixhawk-compatible (any MAVLink controller)
- **Companion compute**: Raspberry Pi 5 (POC tier) · NVIDIA Jetson Orin Nano/NX (production tier)
- **Comms**: RFD900x long-range telemetry · Doodle Labs Helix mesh radio (production)
- **Sensors**: Sony IMX477 visible · FLIR Lepton 3.5 thermal · Livox Mid-360 LiDAR
- **Software**: Python · MAVSDK · Flask · WebSocket telemetry · Leaflet mapping · ESRI satellite imagery
- **Simulation**: PX4 SITL multi-vehicle in WSL2 / Linux containers

### Target Use Cases

- **Rural infrastructure inspection** (powerlines, towers, pipelines) — replacing $1,500/hr helicopter ops
- **Search & Rescue** — multi-drone area coverage 5× faster than ground teams in first hour
- **Precision agriculture** — crop scanning, livestock count, irrigation diagnostics
- **Critical infrastructure perimeter security** (substations, ports, dams)
- **Wildfire monitoring** — thermal sweep + hot-spot mapping + ground-crew handoff
- **Survey & mapping** — photogrammetry + LiDAR over construction sites, forest plots, coastlines
- **Defense / dual-use** — AFWERX SBIR-aligned: contested-environment ops, multi-drone coordination, rapid re-tasking

### Past Performance

> *Pre-revenue, pre-formal-customer stage. To be expanded as customer pilots and SBIR awards accrue.*

- Working software prototype operational in PX4 SITL multi-vehicle simulation (TRL 4)
- 6-command operator UI with real-time telemetry, group selection, and per-drone POV cameras
- Maine Technology Institute Business Innovation Funding self-assessment submitted 2026-04 (response: "may be a fit")
- Funding-strategy roadmap completed: Stage 1 ($115k–475k, 6–9 months) · Stage 2 ($1.85M–4M, 12–18 months)

### Certifications & Compliance

- Small Business Concern (self-certified, < 500 employees)
- US-citizen owned and operated
- ITAR awareness — drone-autonomy stack may fall under USML Category VIII; pre-emptive DDTC registration under evaluation
- TAA-compliant supply chain — no DJI / covered-country components in BOM
- Section 889 / NDAA-compliant — no Huawei / DJI / Hikvision / Hytera dependencies
- FAA Part 107 license — in progress (Q3 2026)

### Federal Engagement Status

| Agency / Program | Status |
|---|---|
| Maine APEX (EMDC) | Intake meeting scheduled with Procurement Counselor Marissa Henkel |
| Maine Technology Institute | Business Innovation Funding self-assessment submitted, awaiting response |
| AFWERX SBIR Phase I | Targeting next BAA window (estimated June–August 2026) |
| SAM.gov | Registration pending (Q2 2026) |
| DoD STTR | Under evaluation as alternative track |

### Contact

**Lucas Gragg**, Founder & CEO
Gragg Robotics, LLC (Maine)
16 Boutelle Ave, Waterville, ME 04901
(207) 242-7351 · lukegragg@gmail.com

---

> **Document version:** Draft v1, dated 2026-05-01
> **Replaces:** N/A (first version)
> **Update triggers:** SAM.gov registration complete · LLC formation complete · first SBIR award · first paying customer
