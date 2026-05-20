# Full Project Briefing for Laptop Claude — 2026-05-20

> **HOW TO USE THIS FILE (Lucas):**
> 1. Open **claude.ai** in Chrome on the laptop
> 2. Start a **new chat**
> 3. Click the **paperclip / attachment icon** in the message box
> 4. Attach this `.md` file
> 5. Send with the message: **"Read this for full context on my company Gragg Robotics — I'll be asking for help throughout the day."**
>
> That Claude session will then have everything below memorized for the rest of the conversation. You can ask it any question and it will respond with full project context.

---

# Identity

I'm **Lucas Gragg**, sole founder of **Gragg Robotics, LLC**, a Maine-based drone autonomy startup founded 2026.

- **Personal email:** lukegragg@gmail.com
- **Business email:** graggrobotics@gmail.com ← use this for all business correspondence
- **Phone:** 207-242-7351
- **Office:** 16 Boutelle Ave, Waterville, ME 04901
- **Website:** graggrobotics.com (live, served via Netlify)

---

# What we build (one-paragraph product summary)

A **universal multi-drone control software** + **bolt-on autonomy pod** that retrofits onto any Pixhawk / PX4 / MAVLink-compatible drone. One operator commands 4-12 drones simultaneously via six RTS-style command primitives (TARGET / FOLLOW / SWEEP / WAYPOINT / GO HOME / ENGAGE). Vendor-agnostic — works with the drones our customers already own. ~10× labor leverage vs the single-pilot-per-drone model the industry is stuck in. Dual-use: civilian (utility inspection, search & rescue, agriculture, infrastructure security, wildfire monitoring) and military (AFWERX / DoD attritable & contested-environment ops).

**Tech stack:** PX4 SITL simulation, MAVSDK, Flask, Python.

**Hardware tiers:**
- POC ~$660/drone (Raspberry Pi 5 + visible cam + RFD900x radio)
- Production ~$4,200/drone (Jetson Orin + thermal FLIR + Livox LiDAR + mesh radio)

---

# Today (2026-05-20)

**🎯 9:30 AM IN-PERSON MEETING — KVCOG offices, Fairfield ME — with Marissa Henkel (APEX Accelerator)**

- Procurement-readiness coaching mode (LLC Certificate hasn't arrived in mail yet, so no SAM.gov registration today)
- Marissa Henkel — Procurement Counselor, APEX Accelerator (EMDC) — `mhenkel@emdc.org` · 207-299-4810
- Already confirmed via email at 6:50 AM this morning
- Bringing: laptop, photo ID, any docs I have, the pitch deck (`gragg_robotics_deck_v1.pptx`)

---

# Entity status

| Item | Status |
|---|---|
| Maine LLC Certificate of Formation | 🟡 IN TRANSIT (mailed 5/5 USPS Priority Express + 24-hr expedite; overdue) |
| EIN | 🟡 Queued — IRS application after Certificate arrives |
| Maine business bank account | 🟡 Queued — Bangor Savings, post-EIN |
| SAM.gov registration | 🟡 Queued — in-person session with Marissa once Certificate + EIN + bank statement in hand |

---

# Funding pipeline

| Source | Amount target | Status | Contact |
|---|---|---|---|
| **MTI Business Innovation Funding** (App 2428739) | ~$25K | 🟢 ACTIVE — application package received, drafting | **Abby Osei**, Investment Officer · aosei@mainetechnology.org · 240-474-3277 |
| **Maine APEX Accelerator** | $0 (free advice) | 🟢 ACTIVE — coaching + SAM.gov walkthrough | **Marissa Henkel** · mhenkel@emdc.org · 207-299-4810 |
| **AFWERX SBIR Phase I** | $75-150K | 🟡 Draft application ready (see `funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md`); awaiting next BAA window (est. Jun–Aug 2026) | TBD via AFWERX BAA |
| **Maine Venture Fund** | TBD | 🟡 Outreach drafted, not yet sent | TBD |
| **Maine Angels** | TBD | 🟡 Outreach drafted | TBD |
| **MCE Top Gun** | TBD | 🟡 Application pending | TBD |
| **Manufacturing quotes** (MacroFab, Sierra Circuits) | n/a | 🟡 Email drafts in `funding/outreach_drafts/` | TBD |

---

# Website — graggrobotics.com

- ✅ **LIVE** on Netlify at https://unrivaled-mousse-002230.netlify.app (deployed 2026-05-17)
- 🟡 **DNS partially routed** — A record + CNAME saved at GoDaddy, but GoDaddy's WSM/Airo Plus product silently injects 2 hidden parking A records (`13.248.243.5`, `76.223.105.230`) that route 2/3 of traffic to GoDaddy's "Coming Soon" page. Fix is to switch nameservers to Netlify DNS (queued for tonight) OR wait until June 15 when Airo Plus trial auto-cancels.
- Custom site built at `website/build/` — hero, demo placeholder, use cases, contact form, dual-logo brand
- Demo video recorded 5/17, not yet uploaded to YouTube
- GoDaddy Airo Plus trial confirmed auto-cancelling June 15, 2026 (no $129 charge)
- Domain registration paid to May 15, 2029

---

# Brand identity (v3 — locked 2026-05-17)

**Dual-logo system** — realistic matte-black quadcopter, LED accent strips, opposing tilt angles signal market segment.

- **Civilian** (`website/build/logos/logo_civilian.svg`): blue LED strips, blue observation eye, 20° back-tilt (peaceful hover/ascent stance) — public-facing brand, civilian outreach, default
- **Military** (`website/build/logos/logo_military.svg`): red LED strips, red targeting eye, 40° forward dive (Apache attack stance) — AFWERX / DoD / defense materials only

**Palette:**
- Body: matte black gradients `#3a3a44` → `#1c1c24` → `#08080c`
- Civilian accent: `#3aa6ff` / `#1d6fc7` (glowing blue)
- Military accent: `#ff2233` / `#aa1010` (glowing red)
- Wordmark: Inter 900 GRAGG (`#ebebeb`) + Inter 700 ROBOTICS (accent color)

---

# Standing directives (how I want Claude to operate)

- **Direct unvarnished honesty** — never lie or fluff; "I don't know" beats invented confidence
- **Protect our money** — refuse phishing lures with prejudice; surface losses before continuing other work
- **Save progress after every meaningful work block** — append updates to `SESSION_STATE.md`
- **Blanket permission for advantageous changes** that help the $20K/month goal — but ASK before unilaterally refusing on judgment calls
- **Send messages on Lucas's behalf is allowed** for graggrobotics@gmail.com and lukegragg@gmail.com when intent is clear (recap emails, thank-you notes, status updates). For first contact with NEW people, draft + confirm before sending.

---

# Open questions to ask Marissa today

1. **AFWERX BAA timing** — when does the next Phase I window open, and where exactly do I monitor for it?
2. **End-user letters of support** — does APEX have introductions to AFRL / 711 HPW / AFSOC end-users who could sign a letter of interest for my SBIR proposal?
3. **NDA template** — does APEX have a Maine-friendly NDA template I can use with potential customers and partners?
4. **SAM.gov session reschedule** — once Certificate arrives + EIN issued + bank statement in hand, what's the next available in-person slot?
5. **NAICS codes** — which primary NAICS code should I register under for drone autonomy + dual-use?
6. **Pre-award match eligibility** — I'm also asking Abby Osei this for MTI BIF, but: can grant funds match pre-award expenses (laptop, software subs)?

---

# Open questions waiting on Abby Osei (MTI)

1. Match eligibility — pre-award expenses (laptop, Claude sub) count toward 1:1 BIF match?
2. Lump-sum vs match for BIF specifically (Marissa said "often lump sum", contradicts MTI public docs)
3. Disbursement model — reimbursement vs milestone vs upfront?

---

# Target customers (year 1)

**Civilian:**
- Central Maine Power (CMP) — utility inspection
- Versant Power — utility inspection
- Maine Search & Rescue / Maine Game Wardens / K9 SAR / Civil Air Patrol
- Kennebec County Sheriff
- Maine agriculture sector

**Defense (year 2-3):**
- AFWERX, AFRL, 711 HPW, AFSOC — via SBIR Phase I → Phase II → Phase III sole-source pipeline
- Defense VCs: Shield Capital, Razor's Edge Ventures, In-Q-Tel

---

# Key files & their paths (so Claude doesn't have to search)

| Topic | File |
|---|---|
| Pitch deck (today's primary asset) | `MTI Meeting 2026-05-13/gragg_robotics_deck_v1.pptx` |
| Capability statement | `funding/apex_intake/03_capability_statement.md` |
| AFWERX SBIR Phase I draft | `funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md` |
| MTI intake script | `MTI Meeting 2026-05-13/01_MTI_intake_script_2026-05-13.md` |
| Master timeline | `funding/MASTER_TIMELINE_2026-05-14.md` |
| Funding tracker (outreach log) | `funding/FUNDING_TRACKER.md` |
| Networking plan (events, colleges, local, media) | `funding/networking_plan_2026-05-15.md` |
| Security plan | `funding/security/SECURITY_PLAN_2026-05-16.md` |
| Mechanical engineer hire scope | `funding/hiring/mechanical_engineer_scope_2026-05-14.md` |
| 7 outreach email drafts | `funding/outreach_drafts/` |
| Netlify DNS swap reference | `website/NETLIFY_DNS_SETUP.md` |
| Live website code | `website/build/index.html` + `style.css` + `script.js` |
| Logo SVGs | `website/build/logos/` |

---

# Trading bots (background — keep alive but not focus today)

- **Kalshi prediction-market bot** running on desktop at port 8445. Strategy: NEAR_CERTAIN sniper on 24h-window weather contracts at 87-89¢. Yesterday hit a tail-loss event (~$320 on AUS-26MAY19 — Austin only hit 87°F, but bet was for >92.5°F). Current capital ~$449. Bot reconfig'd this morning: 25% max-per-position cap, 4 concurrent NC slots (was 50%/2 = too concentrated).

(Don't help me with the bot unless I ask — focus is Gragg Robotics today.)

---

# What I want from THIS Claude session on the laptop

1. **Live help during the meeting** — quick lookups (NAICS codes, CAGE process, NIST 800-171, etc.)
2. **Note-taking** — I'll dump meeting notes; you organize them
3. **Email drafting** — post-meeting follow-up to Marissa, thank-you notes, any action items
4. **Research** — if Marissa mentions a program/contact/grant I don't know, look it up
5. **Continuity** — anything I worked on before (logos, SBIR draft, MTI app), be ready to help refine

I'm NOT asking you to control the laptop — just be a smart partner I can talk to throughout the day.

---

# Quick URLs

- Live site: https://unrivaled-mousse-002230.netlify.app
- Live swarm UI (LAN, same WiFi as desktop): http://192.168.18.47:8500
- File server (deck + briefing files, while desktop is online): http://192.168.18.47:9999
- Netlify project: https://app.netlify.com/projects/unrivaled-mousse-002230/domain-management

---

**END OF BRIEFING. The Claude session that has read this is now fully briefed on Gragg Robotics.**
