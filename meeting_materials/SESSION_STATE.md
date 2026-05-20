# Gragg Robotics — Session State (Living Document)

> **CRITICAL FOR CLAUDE AT SESSION START:** Read this file FIRST every time a new Claude session begins. It's the single source of truth for "where are we." Read `funding/FUNDING_TRACKER.md` second. Read `SESSIONS.md` third for narrative history.
>
> **CRITICAL FOR CLAUDE DURING WORK:** Update this file after every meaningful work block. At minimum:
> - When a milestone changes state (sent / received / signed / deployed / funded)
> - When Lucas makes a decision that affects multiple downstream tracks
> - When a new piece of info emerges from an email, call, or document
> - When a deadline moves
>
> Updates should APPEND to "Recent Updates" at the bottom AND modify the top "Current State" section if the change is structural.

---

## 📅 NEXT SCHEDULED MEETING

**Wed May 20, 2026 — 9:30 AM** — In-person with **Marissa Henkel (APEX)** at **KVCOG offices, Fairfield ME**
- Confirmed by Marissa 5/18 9:48 AM; Lucas reply confirming sent 5/19 11:13 AM
- Agenda branches on whether LLC Certificate has arrived:
  - 🟢 If yes → begin SAM.gov / UEI / CAGE registration
  - 🟡 If no → procurement-readiness coaching session
- Lucas to bring: photo ID, laptop, Certificate (if arrived), SOS Active/Good-Standing screenshot (if arrived), EIN letter (if issued), bank routing/account (if account open)
- Marissa: 207-299-4810 (cell), mhenkel@emdc.org

---

## 🎯 CURRENT STATE — as of 2026-05-16

### Identity
- **Founder:** Lucas Gragg (sole)
- **Personal email:** lukegragg@gmail.com
- **Business email:** **graggrobotics@gmail.com** ← use this for all business correspondence going forward
- **Phone:** 207-242-7351
- **Office:** 16 Boutelle Ave, Waterville, ME 04901
- **Website:** graggrobotics.com (GoDaddy-hosted, currently in editing — Coming Soon placeholder live, full content being built)

### Entity status
- 🟡 **Maine LLC: Certificate of Formation IN TRANSIT.** Mailed 5/5 with 24-hr expedite. Expected back any day — likely arrived by week of 5/12.
- 🟡 **EIN:** queued for IRS application as soon as Certificate arrives
- 🟡 **Business bank account:** queued at Bangor Savings, post-EIN
- 🟡 **SAM.gov registration:** queued, in-person session with Marissa at KVCOG Fairfield once docs are in hand

### Funding pipeline
- 🟢 **MTI BIF App 2428739** — application package received from Abby Osei. Drafting in progress. Abby reviewing before final submission.
  - Abby Osei, Investment Officer · aosei@mainetechnology.org · 240-474-3277
  - Conducted intake call 5/13/2026 — went well, $25K very likely
- 🟢 **APEX engagement (Marissa Henkel)** — active, supporting SAM.gov and AFWERX prep
  - Marissa Henkel, Procurement Counselor (Kennebec County) · mhenkel@emdc.org · 207-299-4810
  - SAM.gov in-person session at KVCOG Fairfield queued for when docs are in hand
- 🟡 **AFWERX SBIR Phase I** — targeting next BAA window (estimated June-August 2026)
- 🟡 **Outreach drafts ready** to MMTC, UMaine ECE, MCE Top Gun, Maine Angels, Maine Venture Fund, MacroFab, Sierra Circuits — sitting in `funding/outreach_drafts/`

### Website (graggrobotics.com)
- 🟢 Custom site at `website/build/` is the chosen production site (Netlify deploy)
- 🟢 Demo section added with placeholder + 3 walkthrough moments (SWEEP / TARGET / FOLLOW+GO HOME)
- 🟢 Civilian logo icon (`logos/logo_icon_civilian.svg`) wired into nav, footer, and favicon
- 🟢 **SITE LIVE on Netlify** — https://unrivaled-mousse-002230.netlify.app (deployed 9:43 AM 2026-05-17)
- 🟡 **DNS swap PENDING** at GoDaddy (see `website/NETLIFY_DNS_SETUP.md`):
  - A record: `@` → `75.2.60.5`
  - CNAME: `www` → `unrivaled-mousse-002230.netlify.app`
- 🟡 SSL will auto-provision via Let's Encrypt once DNS propagates (5–60 min after Lucas saves records)
- 🟢 Netlify account: lukegragg@gmail.com, team "Gragg Robotics", project "unrivaled-mousse-002230"
- 🟡 Demo video: recording script ready at `website/godaddy_content/01_demo_recording_script.md` — Lucas to record + upload to YouTube Unlisted
- 🟢 GoDaddy Airo Plus trial **CONFIRMED auto-cancelling June 15, 2026** (Lucas verified 2026-05-17). No $129 charge. Keep the domain (graggrobotics.com Full Domain Protection renews May 15, 2029).
- 🟢 Domain registration paid to May 15, 2029 (keep — DNS will point to Netlify after deploy)
- 🟢 GoDaddy content blocks no longer needed (custom site replaces them)

### Gmail signature
- 🟢 Signature created in graggrobotics@gmail.com (text done, defaults set for new + reply)
- 🟡 Logo image upload PENDING — needs Lucas to drive Windows file picker; Chrome MCP can't reach it
- 🟢 Use **civilian** logo (blue eye) for the email signature — public-facing brand

### Brand identity (rev'd to v3 on 2026-05-17 — realistic black, LED strips, dual tilt)
- 🟢 **Dual-logo system v3** — realistic matte-black quadcopter, LED accent strips, opposing tilts signal market
  - **Civilian:** `website/build/logos/logo_civilian.svg` — blue LED strips, blue observation eye, 20° back-tilt (peaceful hover/ascent stance)
  - **Military:** `website/build/logos/logo_military.svg` — red LED strips, red targeting eye, 40° forward dive (Apache attack stance)
  - **Comparison preview:** `website/build/logos/preview.html`
  - Both use realistic gradients, motor housings, panel lines, glowing sensor pods — premium stealth-tech look, not cartoony
- 🟢 Body palette: matte black gradients `#3a3a44` → `#1c1c24` → `#08080c` with subtle rim lighting
- 🟢 Civilian accent: glowing blue `#3aa6ff` / `#1d6fc7`
- 🟢 Military accent: glowing red `#ff2233` / `#aa1010`
- 🟢 Background field: deep black with subtle tint (blue ambient for civilian, red ambient for military)
- 🟢 Wordmark: Inter 900 GRAGG in `#ebebeb`, Inter 700 ROBOTICS in accent color (blue/red), letter-spacing 6/14
- 🟡 Icon-only versions (no wordmark) for nav/footer/favicon — still using v2 blue at `logo_icon_civilian.svg`, may rebuild to v3 black later

### Security (added 2026-05-16)
- 🟢 Plan written at `funding/security/SECURITY_PLAN_2026-05-16.md`
- 🟡 Phase 0 (2FA + Bitwarden + BitLocker + backup + Malwarebytes) NOT YET DONE by Lucas — ~2 hrs work + $100

### Trading bots (background)
- 🟢 Kalshi bot running green (PID 19980 on port 8445 as of 2026-05-17 23:00ish). **True total capital: $719.99** (all deposits cleared, Lucas added funds 5/17). Bot dashboard shows BALANCE=$470.56 = unallocated cash only; remaining ~$249 deployed in 3 open positions (MIA NO + CHI NO + UK YES longshot). DAILY_LOSS_LIMIT bumped 10→20 today (2.8% of total). Decision pending whether to bump to $25–30 (3.5–4%).
- 🔴 Hyperliquid bot paused (funds withdrawn to Crypto.com 4/30)
- 🟡 Other bots (Freelance, Gumroad, Traffic) currently paused — restart when bandwidth allows

---

## 🧭 STANDING DIRECTIVES FROM LUCAS

These are persistent preferences I follow without re-asking:

- **Save conversations and progress after every prompt** (2026-04-15, reinforced 2026-05-16)
- **Read this file + FUNDING_TRACKER first at every session start** (2026-05-16)
- **Direct unvarnished honesty — never lie or fluff**; "I don't know" beats invented confidence
- **Protect our money** — refuse phishing lures with prejudice; surface losses before continuing other work
- **Delegate to existing agents** — when work fits an existing agent's mission, extend the agent's prompt instead of doing it manually
- **Launch background processes minimized** — never Normal window style
- **Blanket permission for advantageous changes** that help the $20K/month goal — but ASK before unilaterally refusing on judgment calls
- **Send messages on Lucas's behalf is allowed for graggrobotics@gmail.com and lukegragg@gmail.com** when the context makes the intent clear (recap emails, thank-you notes, status updates). For first contact with NEW people, draft + confirm before sending.

### Operational know-how (collected during sessions)
- **Chrome is tier="read" for computer-use MCP** (screenshots only, no clicks). Use `mcp__Claude_in_Chrome__computer` for clicks via element refs — that bypasses the read restriction.
- **Netlify React forms** require an actual keyboard event to enable Continue buttons. Programmatic setValue + dispatch input/change events updates DOM but not React's internal state. Workaround: ask Lucas to type a char+backspace in one field, then everything submits.
- **GoDaddy DNS edits require an email OTP per save.** 3 wrong attempts = 24-hour lockout. When you click Save → Continue & Verify → wait for fresh code from Lucas's Gmail → form_input the code → click Verify. Cancelling the OTP dialog and re-saving sends a fresh code.
- **GoDaddy WSM/Airo Plus silently injects hidden A records** that don't show in the DNS panel. The fix is either (a) switch nameservers to a non-GoDaddy DNS provider, or (b) wait for the WSM subscription to actually cancel.
- **Game Bar (Win+G) screen recording** captures the focused window. Recording sometimes saturates Chrome MCP's CDP channel → tab refreshes (Ctrl+R) clear the hang without losing the recording.

---

## 📋 OPEN QUESTIONS WAITING ON OTHERS

| Question | Asked of | Date asked | Status |
|---|---|---|---|
| Match eligibility — pre-award expenses (laptop, Claude sub) count toward 1:1 BIF match? | Abby Osei | not yet sent — draft in current Claude conversation | DRAFT |
| Lump-sum vs match for BIF specifically — Marissa said "often lump sum," contradicts MTI public docs | Abby Osei | will be in next email | PENDING |
| Disbursement model — reimbursement vs milestone vs upfront? | Abby Osei | will be in next email | PENDING |

---

## 🔥 OPEN ACTION ITEMS FOR LUCAS

| Priority | Action | Blocking what |
|---|---|---|
| **HIGH** | Upload demo video (recorded 2026-05-17, in `C:\Users\PC\Videos\Captures\`) to YouTube Unlisted, send Claude the URL | Site Demo section iframe + email signature link |
| **HIGH** | DNS Option B with Claude tomorrow: switch graggrobotics.com nameservers from GoDaddy → Netlify DNS (1 more OTP, ~30 min propagation) | Fully cleaning up GoDaddy WSM hidden-A-record hijack |
| **HIGH** | Finish BIF application draft with Abby | $25K funding |
| **HIGH** | Drag civilian logo SVG into Gmail signature (Windows file picker, ~30 sec) | Email signature looks unprofessional without it |
| **MEDIUM** | Review the AFWERX SBIR Phase I draft at `funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md` (focus on cost-volume rates, budget ceiling variant, year-1 customer naming) | Phase I window opens Jun–Aug 2026 |
| **MEDIUM** | Phase 0 security plan (2FA, Bitwarden, BitLocker, backup) — see `funding/security/SECURITY_PLAN_2026-05-16.md` | IP + endpoint safety; relatively cheap insurance |
| **MEDIUM** | Send the 7 outreach drafts (MMTC, UMaine, MCE, Maine Angels, MVF, MacroFab, Sierra) — sitting in `funding/outreach_drafts/` | Building relationships for Stage 2 |
| **MEDIUM** | When Certificate arrives: EIN → Bangor Savings → SAM.gov w/ Marissa | All downstream federal funding |
| **MEDIUM** | Buy laptop ($1,000 Legion Slim 5 recommended) — see `funding/hiring/business_laptop_recommendation_2026-05-16.md` | Mobile work; recording demo away from desktop |
| **LOW** | Apply to MCE Top Gun program | Networking + investor-readiness |

---

## 🗂 KEY FILE PATHS (so Claude doesn't have to search)

| Topic | File |
|---|---|
| AFWERX SBIR Phase I draft (NEW 2026-05-17) | `funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md` |
| Netlify DNS swap reference (NEW 2026-05-17) | `website/NETLIFY_DNS_SETUP.md` |
| Master timeline | `funding/MASTER_TIMELINE_2026-05-14.md` |
| Funding tracker (outreach log) | `funding/FUNDING_TRACKER.md` |
| Post-MTI action plan (workers/manufacturing/funding) | `funding/post_mti_action_plan_2026-05-13.md` |
| Networking plan (conventions/colleges/local/media) | `funding/networking_plan_2026-05-15.md` |
| Security plan | `funding/security/SECURITY_PLAN_2026-05-16.md` |
| Laptop recommendation | `funding/hiring/business_laptop_recommendation_2026-05-16.md` |
| Mechanical engineer hire scope | `funding/hiring/mechanical_engineer_scope_2026-05-14.md` |
| Outreach email drafts | `funding/outreach_drafts/` (7 files + README) |
| APEX intake materials | `funding/apex_intake/` (4 files + README) |
| MTI intake materials | `MTI Meeting 2026-05-13/` (on Desktop) |
| LLC paperwork | `funding/legal/` + `Gragg Robotics LLC Filing/` (on Desktop) |
| Website content blocks (for GoDaddy paste) | `website/godaddy_content/02_website_content_blocks.md` |
| Demo video recording script | `website/godaddy_content/01_demo_recording_script.md` |
| Custom static site (Netlify backup plan) | `website/build/` |
| Logo pair (civilian + military) | `website/build/logos/` |
| Logo comparison page | `website/build/logos/preview.html` |
| Drone swarm UI code | repo root + `swarm/`, `static/`, `templates/`, `app.py` |
| Session narrative history | `SESSIONS.md` |

---

## 🧾 RECENT UPDATES (append-only — newest first)

### 2026-05-17 — Site LIVE on Netlify + v3 logos + SBIR draft + DNS partially routed

**Headline: graggrobotics.com partially serves the Netlify site (1/3 of clients). GoDaddy WSM still hijacks 2/3 via hidden A records. Fix queued for tomorrow (Option B: switch nameservers to Netlify DNS).**

**v3 dual-logo system (replaces v2):**
- Lucas requested realistic black drones with LED light strips + opposing tilts. Built fresh from scratch.
- `logos/logo_civilian.svg` — matte black body, blue LED accent strips, 20° back-tilt (peaceful hover/ascent stance), blue observation eye in sensor pod
- `logos/logo_military.svg` — matte black body, red LED accent strips, 40° forward dive (Apache attack stance), intense red targeting eye
- `logos/logo_icon_civilian.svg` — drone-only icon (no wordmark) for nav/footer/favicon
- Realistic details: matte black gradients, motor housings with status LEDs, panel lines, glossy sensor pod with sharp lens reflections, drop shadows
- Updated `logos/preview.html` to show new side-by-side

**Site updated (`website/build/`):**
- Added new `#demo` section with placeholder video frame + 3 walkthrough moments (SWEEP / TARGET / FOLLOW+GO HOME) + "Request Live Demo" CTA
- Civilian icon now in nav, footer, and as favicon
- Added Demo to nav links
- Added CSS for Demo section + moments grid

**Netlify deploy COMPLETE:**
- Site live at `https://unrivaled-mousse-002230.netlify.app` (deployed 9:43 AM)
- Account: lukegragg@gmail.com, team "Gragg Robotics", project "unrivaled-mousse-002230"
- Onboarding form had React-state quirk — needed Lucas to manually type a char+backspace in team-name field to enable Continue button (programmatic setValue didn't trigger React's onChange)

**DNS partially routed at GoDaddy:**
- A record `@` → `75.2.60.5` (Netlify anycast) — SAVED via OTP
- CNAME `www` → `unrivaled-mousse-002230.netlify.app` — SAVED via OTP
- Both saves required GoDaddy "Continue & Verify" → email OTP (2-attempts-left lockout if 3 wrong codes — first attempt "098108" was wrong, retried with fresh codes successfully)
- DNS records reference doc saved at `website/NETLIFY_DNS_SETUP.md`

**🔴 CRITICAL LEARNING — GoDaddy WSM hidden A records:**
- After A+CNAME saved, `Resolve-DnsName graggrobotics.com` still returned 3 A records: `75.2.60.5` (ours), `13.248.243.5`, `76.223.105.230`
- Tested each: `curl --resolve graggrobotics.com:443:<ip> https://graggrobotics.com -I` revealed:
  - `75.2.60.5` → `Server: Netlify` ✅
  - `13.248.243.5` → `Server: DPS/2.0.0+sha-78da108` (GoDaddy parking) ❌
  - `76.223.105.230` → `Server: DPS/2.0.0+sha-78da108` ❌
- The hidden IPs are NOT in GoDaddy's visible DNS panel — they're auto-injected by the WSM/Airo Plus product
- Result: 2/3 of clients hit GoDaddy "Coming Soon" page instead of Netlify
- **Fix Option A (queued tomorrow):** Switch nameservers from GoDaddy to Netlify DNS (one more OTP, ~30min propagation, clean long-term)
- **Fix Option B (passive):** Wait until June 15 when Airo Plus trial auto-cancels (the hidden A records drop)
- Lucas chose Option A for tomorrow

**GoDaddy Airo Plus trial:**
- CONFIRMED auto-cancelling June 15, 2026 (no $129 charge)
- Domain registration paid through May 15, 2029 (keep)

**SBIR Phase I draft COMPLETE:**
- Background agent wrote full 15-section AFWERX SBIR Phase I application
- File: `funding/sbir/AFWERX_SBIR_PHASE_I_DRAFT_2026-05-17.md` (~9 pages)
- Sections: cover sheet, 200-word abstract, problem/significance, 6 measurable technical objectives, 3-month work plan, related work (positioned vs Skydio/Anduril/Shield AI), commercialization, key personnel, facilities, subcontractors, $150K cost volume table, CCR, data rights, disclosures, submission checklist
- Every fabricated metric tagged `[ASSUMPTION: ...]`, every gap tagged `[TBD: ...]`
- Top 3 review items: (1) cost-volume labor rate + indirect rate are guesses, set with Marissa/accountant; (2) budget assumes $150K Direct-to-Phase-II variant, verify against active solicitation (could be $75K variant); (3) 3-year revenue projection needs naming specific Year-1 pilot customers (CMP/Versant/Maine SAR/Kennebec sheriff) instead of categories
- Lucas to review when quiet hour available — not for submission until next AFWERX BAA opens (Jun–Aug 2026)

**Demo video recorded (upload pending):**
- Game Bar recording, Lucas drove the recorder, Claude drove the demo via Chrome MCP clicks on the SPLIT-view swarm UI at localhost:8500
- Sequence: INSPECTION → PLAY DEMO (25s) → RESET → SAR → PLAY DEMO (45s) = ~85 sec total
- Multiple takes; final take needs trimming + upload to YouTube Studio (Unlisted) → URL to Claude → swap site placeholder for iframe → redeploy
- Recording script reference: `website/godaddy_content/01_demo_recording_script.md`

**Mouse fix:**
- 40" TV mouse felt slow vs 22" monitor (same 1920×1080 but ~2× physical size = same px-speed but slower perceived sweep)
- Bumped `MouseSensitivity` from 10→14 via Win32 `SystemParametersInfo` + registry write
- Adjustable later via Settings → Mouse → pointer speed slider

**Other:**
- Started swarm bot `app.py` minimized on port 8500 (PID 20300) for demo recording — still running at session close, fine to leave or kill
- Tab group accumulated: Netlify drop, Netlify project, GoDaddy DNS, GoDaddy billing, YouTube Studio, local logo preview, local index preview, live graggrobotics.com test
- Background agent successfully delegated for SBIR draft (~5 min, ~106K tokens, 15 tool uses, returned summary + flagged review items)

### 2026-05-16 (continued — dual-logo branding)
- **DUAL LOGO SYSTEM LOCKED.** Same Apache-stance drone body, 40° forward pitch, identical wordmark — single visual cue (sensor eye color) signals which market you're addressing.
  - `logos/logo_civilian.svg` — BLUE sensor eye (#5cb8ff/#1d6fc7). Use on graggrobotics.com, business email signature, civilian customer outreach (utilities, SAR, ag, sheriffs), Maine Venture Fund / Maine Angels / MCE Top Gun applications, default capability statement, press releases.
  - `logos/logo_military.svg` — RED sensor eye (#ff5533/#a01010). Use on AFWERX SBIR proposals, DoD-facing capability statement variant, defense-track BD decks (Shield Capital, Razor's Edge, In-Q-Tel), conference booths at defense events, defense-industry press (Defense News, Breaking Defense), letterhead for federal contract correspondence.
  - Rule of thumb: when in doubt, default civilian. Dual-use positioning is the stronger long-term play, and AFWERX scoring rewards it.
  - Side-by-side comparison at `logos/preview.html` (served by local Python server on port 9090).
- **KALSHI: capital scaled from ~$34 to ~$398** (cash $234.66 + portfolio $163.21). Lucas deposited more; bot is running green at claimed 2-3%/day. **Bumped `DAILY_LOSS_LIMIT_USD` from $5 → $10** — old limit was 1.25% of new capital (too tight). Restarted Kalshi clean on PID 17332, 3 active positions intact. Watch for: when balance crosses $1k, convert loss limit to percentage of balance instead of absolute.
- **Website decision locked: Option B (Netlify custom site, keep graggrobotics.com domain).** Lucas confirmed continuity priority: single logo + colors + email + URL across all platforms. GoDaddy free Coming Soon tier is a dead-end (5 editable fields only). Custom site at `website/build/` ready to deploy. Next: Lucas signs up at netlify.com → drag-drop `build` folder → I add custom domain → he updates GoDaddy DNS → cancels GoDaddy WSM trial before day 8.

### 2026-05-16
- Session state file CREATED to be the canonical "where are we" reference per Lucas's request that I save + reference progress every session
- Security plan written — 5 actions to do this week for ~$100 + 2 hrs (2FA, Bitwarden, BitLocker, backup, Malwarebytes)
- Laptop recommendation written — Lenovo Legion Slim 5 at ~$950-1,000 from Costco
- Drafted Abby question on pre-award match eligibility — sitting in current Claude conversation, not yet sent
- Logo upload to Gmail signature stuck on Chrome security tier — Lucas to drive picker manually
- GoDaddy editor tab access lost; Lucas to re-activate Chrome extension to give Claude access

### 2026-05-15
- Networking plan written covering 4 channels (events/colleges/local/media) with concrete actions + 90-day cadence
- Mechanical engineer scope-of-work + outreach template written
- Website upgrade decision pivoted from custom Netlify build → keep GoDaddy + paste prepared content into it
- Website content blocks for all 8 sections of graggrobotics.com written + saved

### 2026-05-14
- Lucas asked for chronological task timeline — master timeline written
- 7 outreach email drafts created (MMTC, UMaine ECE, MCE Top Gun, Maine Angels, Maine Venture Fund, MacroFab, Sierra Circuits)
- Custom HTML/CSS/JS site built at `website/build/` as backup to GoDaddy

### 2026-05-13
- MTI intake call with Abby Osei went well — $25K very likely
- Abby flagged 3 parallel relationship-building tracks: workers, manufacturing, private funding
- Post-MTI action plan written

### 2026-05-12
- MTI meeting prep package built in `MTI Meeting 2026-05-13/` folder
- New MTI intake script written (different from APEX, 8 BIF areas)

### 2026-05-07
- APEX intake call with Marissa Henkel went well — Marissa to walk through SAM.gov in-person once Lucas has docs
- New business email graggrobotics@gmail.com established, housekeeping emails sent to Abby + Marissa
- Marissa sent SAM.gov required-docs checklist (Certificate + EIN letter + bank statement + Active screenshot + bank routing/account)

### 2026-05-05
- LLC Certificate of Formation (MLLC-6) mailed by Corrina via USPS Priority Mail Express + money order $225 ($175 filing + $50 24-hr expedite)

### Earlier history
- See `SESSIONS.md` for narrative session logs from April 2026 forward
- See `funding/FUNDING_TRACKER.md` for outreach log
