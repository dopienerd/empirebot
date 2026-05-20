#!/usr/bin/env python3
"""
Gragg Robotics — Meeting Command Center
All meeting materials in one browser window.
Includes teleprompter mode for the call script.

Usage: python3 meeting_dashboard.py
Then open http://localhost:5050
"""

import os
import re
import sys
from pathlib import Path
from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory

app = Flask(__name__)

MATERIALS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meeting_materials')
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024


def md_to_html(text):
    text = re.sub(r'^#{3}\s+(.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^#{2}\s+(.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^#{1}\s+(.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)

    lines = text.split('\n')
    result = []
    in_table = False
    in_blockquote = False
    in_list = False
    table_header_done = False

    for line in lines:
        stripped = line.strip()

        # Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                result.append('<table>')
                in_table = True
                table_header_done = False
            if re.match(r'^\|[\s\-\|]+\|$', stripped):
                table_header_done = True
                continue
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            tag = 'th' if not table_header_done else 'td'
            result.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
            continue
        elif in_table:
            result.append('</table>')
            in_table = False
            table_header_done = False

        # Blockquotes
        if stripped.startswith('>'):
            content = stripped.lstrip('> ').strip()
            if not in_blockquote:
                result.append('<blockquote>')
                in_blockquote = True
            result.append(f'<p>{content}</p>')
            continue
        elif in_blockquote and stripped == '':
            result.append('</blockquote>')
            in_blockquote = False

        # Checkboxes
        if stripped.startswith('- [ ]'):
            if not in_list:
                result.append('<ul class="checklist">')
                in_list = True
            result.append(f'<li class="unchecked">{stripped[5:].strip()}</li>')
            continue
        elif stripped.startswith('- [x]') or stripped.startswith('- [X]'):
            if not in_list:
                result.append('<ul class="checklist">')
                in_list = True
            result.append(f'<li class="checked">{stripped[5:].strip()}</li>')
            continue
        elif stripped.startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{stripped[2:]}</li>')
            continue
        elif stripped.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
            if not in_list:
                result.append('<ol>')
                in_list = True
            content = re.sub(r'^\d+\.\s*', '', stripped)
            result.append(f'<li>{content}</li>')
            continue
        elif in_list and stripped == '':
            if in_list:
                result.append('</ul>' if '</ol>' not in ''.join(result[-5:]) else '</ol>')
                in_list = False

        # Horizontal rule
        if stripped == '---':
            result.append('<hr>')
            continue

        # Regular paragraph
        if stripped:
            result.append(f'<p>{stripped}</p>')
        else:
            result.append('')

    if in_table:
        result.append('</table>')
    if in_blockquote:
        result.append('</blockquote>')
    if in_list:
        result.append('</ul>')

    return '\n'.join(result)


def load_materials():
    materials = {}
    for fname in sorted(os.listdir(MATERIALS_DIR)):
        if fname.endswith('.md'):
            with open(os.path.join(MATERIALS_DIR, fname), 'r') as f:
                materials[fname] = f.read()
    return materials


DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Gragg Robotics — Meeting Command Center</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0a0a1a; color: #e0e0e0; }

/* Nav */
.topnav {
    background: #111;
    border-bottom: 2px solid #e94560;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
}
.topnav .brand { font-size: 16px; font-weight: bold; color: #e94560; }
.topnav .brand span { color: #aaa; font-weight: normal; font-size: 13px; margin-left: 10px; }
.nav-tabs { display: flex; gap: 4px; }
.nav-tabs button {
    background: #1a1a2e;
    border: 1px solid #333;
    color: #aaa;
    padding: 8px 16px;
    border-radius: 4px 4px 0 0;
    cursor: pointer;
    font-size: 13px;
    transition: all 0.2s;
}
.nav-tabs button:hover { background: #2a2a4e; color: #fff; }
.nav-tabs button.active { background: #e94560; color: #fff; border-color: #e94560; }
.nav-actions { display: flex; gap: 8px; }
.nav-actions button {
    background: #0f3460;
    border: 1px solid #533483;
    color: #e0e0ff;
    padding: 8px 14px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 12px;
}
.nav-actions button:hover { background: #533483; }
.nav-actions button.danger { background: #e94560; border-color: #e94560; }

/* Content panels */
.panel { display: none; padding: 30px 60px; max-width: 1000px; margin: 0 auto; }
.panel.active { display: block; }

/* Dashboard home */
.dashboard-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 20px;
}
.card {
    background: #16213e;
    border: 1px solid #0f3460;
    border-radius: 8px;
    padding: 20px;
    cursor: pointer;
    transition: all 0.2s;
}
.card:hover { border-color: #e94560; transform: translateY(-2px); }
.card h3 { color: #e94560; margin-bottom: 8px; font-size: 16px; }
.card p { color: #a0a0c0; font-size: 13px; line-height: 1.5; }
.card .badge {
    display: inline-block;
    background: #e94560;
    color: #fff;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 11px;
    margin-top: 8px;
}
.card .badge.green { background: #27ae60; }
.card .badge.yellow { background: #f39c12; }

.hero {
    background: linear-gradient(135deg, #16213e, #0f3460);
    border: 1px solid #533483;
    border-radius: 12px;
    padding: 30px;
    margin-bottom: 20px;
    text-align: center;
}
.hero h1 { color: #e94560; font-size: 24px; margin-bottom: 6px; }
.hero h2 { color: #a0a0c0; font-size: 15px; font-weight: normal; }
.hero .meeting-info {
    margin-top: 15px;
    font-size: 14px;
    color: #e0e0e0;
}
.hero .meeting-info strong { color: #e94560; }

/* Markdown content */
.md-content { line-height: 1.7; font-size: 15px; }
.md-content h1 { color: #e94560; font-size: 24px; margin: 30px 0 15px; border-bottom: 1px solid #333; padding-bottom: 8px; }
.md-content h2 { color: #e94560; font-size: 20px; margin: 25px 0 12px; }
.md-content h3 { color: #f0a0b0; font-size: 17px; margin: 20px 0 10px; }
.md-content p { margin: 8px 0; }
.md-content strong { color: #fff; }
.md-content code { background: #1a1a3e; padding: 2px 6px; border-radius: 3px; color: #e94560; font-size: 13px; }
.md-content blockquote {
    border-left: 3px solid #e94560;
    background: #111;
    padding: 12px 20px;
    margin: 12px 0;
    border-radius: 0 6px 6px 0;
    font-size: 15px;
    color: #d0d0e0;
}
.md-content blockquote p { margin: 4px 0; }
.md-content table { width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; }
.md-content th { background: #1a1a3e; padding: 8px 12px; text-align: left; color: #e94560; border: 1px solid #333; }
.md-content td { padding: 8px 12px; border: 1px solid #333; }
.md-content tr:nth-child(even) td { background: rgba(255,255,255,0.02); }
.md-content ul, .md-content ol { margin: 8px 0 8px 24px; }
.md-content li { margin: 4px 0; }
.md-content .checklist { list-style: none; margin-left: 0; }
.md-content .checklist li { padding: 4px 0 4px 28px; position: relative; }
.md-content .checklist li.unchecked::before { content: '☐'; position: absolute; left: 0; color: #e94560; font-size: 16px; }
.md-content .checklist li.checked::before { content: '☑'; position: absolute; left: 0; color: #27ae60; font-size: 16px; }
.md-content hr { border: none; border-top: 1px solid #333; margin: 20px 0; }

/* Teleprompter mode */
.teleprompter {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: #000;
    z-index: 200;
    overflow-y: auto;
    padding: 60px 15%;
}
.teleprompter.active { display: block; }
.teleprompter .md-content { font-size: 22px; line-height: 1.8; }
.teleprompter .md-content blockquote { font-size: 24px; background: #0a0a2a; border-left-width: 5px; padding: 20px 30px; }
.teleprompter .md-content blockquote strong { color: #4fc3f7; }
.teleprompter .close-btn {
    position: fixed;
    top: 15px;
    right: 20px;
    background: #e94560;
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    z-index: 210;
}
.teleprompter .scroll-hint {
    position: fixed;
    bottom: 15px;
    right: 20px;
    color: #666;
    font-size: 12px;
}

/* Deck upload */
.deck-upload {
    background: #16213e;
    border: 2px dashed #533483;
    border-radius: 12px;
    padding: 40px;
    text-align: center;
    margin: 20px 0;
}
.deck-upload h3 { color: #e94560; margin-bottom: 10px; }
.deck-upload input { display: none; }
.deck-upload button {
    background: #e94560;
    color: #fff;
    border: none;
    padding: 12px 28px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 15px;
}

/* Key phrases */
.key-phrases {
    background: #16213e;
    border: 1px solid #0f3460;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}
.key-phrases h3 { color: #e94560; margin-bottom: 12px; }
.key-phrases .phrase {
    background: #111;
    border-left: 3px solid #e94560;
    padding: 10px 16px;
    margin: 8px 0;
    border-radius: 0 4px 4px 0;
    font-size: 15px;
}
.key-phrases .phrase em { color: #888; font-size: 12px; display: block; margin-top: 4px; }

/* Print */
@media print {
    .topnav { display: none; }
    body { background: #fff; color: #000; }
    .panel { max-width: 100%; padding: 20px; }
    .md-content blockquote { background: #f5f5f5; }
}
</style>
</head>
<body>

<div class="topnav">
    <div class="brand">GRAGG ROBOTICS <span>Meeting Command Center</span></div>
    <div class="nav-tabs">
        <button class="active" onclick="showPanel('home')">Home</button>
        <button onclick="showPanel('script')">Call Script</button>
        <button onclick="showPanel('terms')">Terms Cheatsheet</button>
        <button onclick="showPanel('capability')">Capability Statement</button>
        <button onclick="showPanel('sbir')">AFWERX SBIR Draft</button>
        <button onclick="showPanel('deck')">Deck</button>
    </div>
    <div class="nav-actions">
        <button onclick="openTeleprompter()">TELEPROMPTER MODE</button>
    </div>
</div>

<!-- HOME -->
<div class="panel active" id="panel-home">
    <div class="hero">
        <h1>Gragg Robotics — APEX Meeting Day</h1>
        <h2>Universal Multi-Drone Control Systems</h2>
        <div class="meeting-info">
            <strong>TODAY 9:30 AM</strong> — In-person with <strong>Marissa Henkel</strong> (APEX Accelerator)<br>
            <strong>Location:</strong> KVCOG offices, Fairfield ME &nbsp;|&nbsp; <strong>Topic:</strong> Procurement Readiness Coaching<br>
            <strong>Marissa:</strong> 207-299-4810 &nbsp;|&nbsp; mhenkel@emdc.org
        </div>
    </div>

    <div class="key-phrases">
        <h3>Questions to Ask Marissa Today</h3>
        <div class="phrase">1. <strong>AFWERX BAA timing</strong> — when does the next Phase I window open, where do I monitor? <em>Critical for SBIR</em></div>
        <div class="phrase">2. <strong>End-user letters of support</strong> — does APEX have intros to AFRL / 711 HPW / AFSOC for letter of interest? <em>SBIR strength</em></div>
        <div class="phrase">3. <strong>NDA template</strong> — Maine-friendly NDA for customers and partners? <em>Practical need</em></div>
        <div class="phrase">4. <strong>SAM.gov session reschedule</strong> — once Certificate + EIN + bank in hand, next available slot? <em>Logistics</em></div>
        <div class="phrase">5. <strong>NAICS codes</strong> — which primary NAICS for drone autonomy + dual-use? <em>Registration</em></div>
        <div class="phrase">6. <strong>Pre-award match eligibility</strong> — can grant funds match pre-award expenses (laptop, subs)? <em>Budget</em></div>
    </div>

    <div class="key-phrases" style="margin-top:12px;">
        <h3>Status Update for Marissa</h3>
        <div class="phrase"><strong>LLC:</strong> Certificate in transit (mailed 5/5, USPS Priority Express + 24-hr expedite — overdue)</div>
        <div class="phrase"><strong>MTI BIF:</strong> Intake call 5/13 with Abby Osei went well. $25K likely. Drafting application now.</div>
        <div class="phrase"><strong>AFWERX SBIR:</strong> Full 15-section Phase I draft ready. Waiting for BAA window (Jun-Aug 2026).</div>
        <div class="phrase"><strong>Website:</strong> Live at graggrobotics.com (Netlify). Demo recorded, upload pending.</div>
        <div class="phrase"><strong>Prototype:</strong> Working 4-drone swarm UI in PX4 SITL. Live demo at http://192.168.18.47:8500</div>
    </div>

    <div class="dashboard-grid">
        <div class="card" onclick="showPanel('deck')">
            <h3>Presentation Deck</h3>
            <p>10-slide Gragg Robotics overview deck. Walk Marissa through if she wants to see it.</p>
            <span class="badge danger">HAVE READY</span>
        </div>
        <div class="card" onclick="showPanel('capability')">
            <h3>Capability Statement</h3>
            <p>1-page company profile. Federal-contractor standard format. Show Marissa if she asks.</p>
            <span class="badge danger">HAVE READY</span>
        </div>
        <div class="card" onclick="showPanel('terms')">
            <h3>Terms Cheatsheet</h3>
            <p>Federal contracting + drone-tech vocabulary. SBIR, SAM.gov, AFWERX, ITAR, MAVLink, NAICS.</p>
            <span class="badge yellow">Quick lookup</span>
        </div>
        <div class="card" onclick="showPanel('script')">
            <h3>MTI Call Script</h3>
            <p>Word-for-word script from Abby call — 8 BIF areas. Reference for talking points with Marissa.</p>
            <span class="badge green">Reference</span>
        </div>
        <div class="card" onclick="showPanel('sbir')">
            <h3>AFWERX SBIR Phase I Draft</h3>
            <p>Full 15-section draft. Show Marissa for review — she should see it before submission.</p>
            <span class="badge yellow">Marissa review</span>
        </div>
        <div class="card" onclick="openTeleprompter()">
            <h3>TELEPROMPTER MODE</h3>
            <p>Full-screen dark mode view of the call script. Quick reference during meeting.</p>
            <span class="badge green">Optional</span>
        </div>
    </div>
</div>

<!-- SCRIPT -->
<div class="panel" id="panel-script">
    <div class="md-content">{{ script_html|safe }}</div>
</div>

<!-- TERMS -->
<div class="panel" id="panel-terms">
    <div class="md-content">{{ terms_html|safe }}</div>
</div>

<!-- CAPABILITY -->
<div class="panel" id="panel-capability">
    <div class="md-content">{{ capability_html|safe }}</div>
</div>

<!-- SBIR -->
<div class="panel" id="panel-sbir">
    <div class="md-content">{{ sbir_html|safe }}</div>
</div>

<!-- DECK -->
<div class="panel" id="panel-deck">
    <h1 style="color:#e94560;margin-bottom:20px;">Presentation Deck</h1>
    {% if has_deck %}
    <p style="margin-bottom:15px;">Deck loaded. Once LibreOffice is installed, you can also open the .pptx directly.</p>
    <iframe src="/deck_view" style="width:100%;height:80vh;border:1px solid #333;border-radius:8px;"></iframe>
    {% else %}
    <div class="deck-upload">
        <h3>Upload gragg_robotics_deck_v1.pptx</h3>
        <p style="color:#a0a0c0;margin-bottom:15px;">Drop your .pptx file here to view it in the browser</p>
        <form method="POST" action="/upload_deck" enctype="multipart/form-data" id="deckForm">
            <input type="file" name="deck" id="deckInput" accept=".pptx" onchange="document.getElementById('deckForm').submit()">
            <button type="button" onclick="document.getElementById('deckInput').click()">Choose .pptx File</button>
        </form>
    </div>
    <p style="color:#888;margin-top:15px;">Or open it directly in LibreOffice Impress once installed.</p>
    {% endif %}
</div>

<!-- TELEPROMPTER -->
<div class="teleprompter" id="teleprompter">
    <button class="close-btn" onclick="closeTeleprompter()">Exit Teleprompter (Esc)</button>
    <div class="md-content">{{ script_html|safe }}</div>
    <div class="scroll-hint">Arrow keys or scroll to navigate | Esc to exit</div>
</div>

<script>
function showPanel(name) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-tabs button').forEach(b => b.classList.remove('active'));
    document.getElementById('panel-' + name).classList.add('active');
    const tabs = document.querySelectorAll('.nav-tabs button');
    const tabMap = {'home':0,'script':1,'terms':2,'capability':3,'sbir':4,'deck':5};
    if (tabMap[name] !== undefined) tabs[tabMap[name]].classList.add('active');
    window.scrollTo(0, 0);
}

function openTeleprompter() {
    document.getElementById('teleprompter').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeTeleprompter() {
    document.getElementById('teleprompter').classList.remove('active');
    document.body.style.overflow = '';
}

document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeTeleprompter();
});

// Drag and drop for deck
const deckPanel = document.getElementById('panel-deck');
if (deckPanel) {
    deckPanel.addEventListener('dragover', e => e.preventDefault());
    deckPanel.addEventListener('drop', e => {
        e.preventDefault();
        const input = document.getElementById('deckInput');
        if (input && e.dataTransfer.files.length) {
            input.files = e.dataTransfer.files;
            document.getElementById('deckForm').submit();
        }
    });
}
</script>
</body>
</html>
"""


@app.route('/')
def index():
    materials = load_materials()

    script_md = materials.get('01_MTI_intake_script.md', 'Script not found.')
    terms_md = materials.get('02_terms_cheatsheet.md', 'Cheatsheet not found.')
    capability_md = materials.get('03_capability_statement.md', 'Capability statement not found.')
    sbir_md = materials.get('04_AFWERX_SBIR_PHASE_I_DRAFT.md', 'SBIR draft not found.')

    has_deck = any(f.endswith('.pptx') for f in os.listdir(UPLOAD_DIR)) or any(f.endswith('.pptx') for f in os.listdir(MATERIALS_DIR))

    return render_template_string(
        DASHBOARD_HTML,
        script_html=md_to_html(script_md),
        terms_html=md_to_html(terms_md),
        capability_html=md_to_html(capability_md),
        sbir_html=md_to_html(sbir_md),
        has_deck=has_deck,
    )


@app.route('/upload_deck', methods=['POST'])
def upload_deck():
    if 'deck' in request.files:
        f = request.files['deck']
        if f.filename.endswith('.pptx'):
            f.save(os.path.join(UPLOAD_DIR, f.filename))
    return redirect('/')


@app.route('/deck_view')
def deck_view():
    for d in [UPLOAD_DIR, MATERIALS_DIR]:
        for fname in os.listdir(d):
            if fname.endswith('.pptx'):
                return _render_deck(os.path.join(d, fname))
    return "No deck uploaded.", 404


def _render_deck(pptx_path):
    import base64
    import json
    from pptx import Presentation
    from pptx.enum.text import PP_ALIGN

    prs = Presentation(pptx_path)
    slide_width = prs.slide_width
    slide_height = prs.slide_height
    w_px = 960
    h_px = int(w_px * slide_height / slide_width)
    scale = w_px / slide_width

    slides_data = []
    for slide_num, slide in enumerate(prs.slides, 1):
        slide_info = {"number": slide_num, "elements": [], "background": "#FFFFFF", "width": w_px, "height": h_px}
        try:
            bg = slide.background
            if bg.fill.type is not None and bg.fill.type == 1:
                c = bg.fill.fore_color.rgb
                slide_info["background"] = f"rgb({c[0]},{c[1]},{c[2]})"
        except:
            pass

        for shape in slide.shapes:
            elem = {
                "left": int(shape.left * scale) if shape.left else 0,
                "top": int(shape.top * scale) if shape.top else 0,
                "width": int(shape.width * scale) if shape.width else 0,
                "height": int(shape.height * scale) if shape.height else 0,
            }
            if shape.shape_type == 13:
                try:
                    img = shape.image
                    b64 = base64.b64encode(img.blob).decode()
                    elem["type"] = "image"
                    elem["src"] = f"data:{img.content_type};base64,{b64}"
                    slides_data.append({"slide": slide_num, "elem": elem})
                except:
                    pass
                continue
            if shape.has_text_frame:
                texts = []
                for para in shape.text_frame.paragraphs:
                    for run in para.runs:
                        if run.text.strip():
                            rd = {"text": run.text}
                            if run.font.size:
                                rd["size"] = int(run.font.size.pt * scale * 1.1)
                            if run.font.bold:
                                rd["bold"] = True
                            if run.font.color and run.font.color.rgb:
                                c = run.font.color.rgb
                                rd["color"] = f"rgb({c[0]},{c[1]},{c[2]})"
                            texts.append(rd)
                if texts:
                    elem["type"] = "text"
                    elem["texts"] = texts
            if "type" in elem:
                if len(slides_data) == 0 or slides_data[-1].get("_slide_num") != slide_num:
                    slides_data.append({"_slide_num": slide_num, "info": slide_info, "elems": []})
                slides_data[-1]["elems"].append(elem)

    # Simple rendering
    deck_html = f"""<!DOCTYPE html><html><head><style>
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{background:#000;color:#fff;font-family:sans-serif;overflow:hidden;height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center}}
    .slide{{position:relative;box-shadow:0 4px 20px rgba(0,0,0,0.5);border-radius:4px;overflow:hidden}}
    .nav{{position:fixed;bottom:10px;display:flex;gap:10px;z-index:10}}
    .nav button{{background:#333;border:1px solid #555;color:#fff;padding:8px 20px;border-radius:4px;cursor:pointer}}
    .counter{{color:#888;font-size:13px;margin:0 10px;line-height:36px}}
    </style></head><body>
    <div id="slideContainer"></div>
    <div class="nav"><button onclick="prev()">Prev</button><span class="counter" id="counter">1/{len(prs.slides)}</span><button onclick="next()">Next</button></div>
    <script>
    let current=0,total={len(prs.slides)};
    const slides={json.dumps([{{"bg": s.get("info",{{}}).get("background","#fff"), "w": w_px, "h": h_px}} for s in slides_data if "_slide_num" in s])};
    function show(n){{current=n;document.getElementById('counter').textContent=(n+1)+'/'+total;}}
    function next(){{if(current<total-1)show(current+1)}}
    function prev(){{if(current>0)show(current-1)}}
    document.addEventListener('keydown',e=>{{if(e.key==='ArrowRight')next();if(e.key==='ArrowLeft')prev();}});
    </script></body></html>"""
    return deck_html


if __name__ == '__main__':
    print("\n  Gragg Robotics — Meeting Command Center")
    print("  ========================================")
    print("  Open http://localhost:5050 in your browser")
    print("  Press Ctrl+C to stop\n")
    print("  Features:")
    print("    - All meeting materials in tabbed view")
    print("    - Teleprompter mode for the call script")
    print("    - Upload .pptx deck to view in browser")
    print("    - Terms cheatsheet + capability statement\n")

    app.run(host='0.0.0.0', port=5050, debug=False)
