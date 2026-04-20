"""
MedFlow AI — Site officiel
medflowai-landing.streamlit.app
Dr. Mamadou Lamine TALL · PhD Bioinformatique
"""

import streamlit as st
import streamlit.components.v1 as components
import os

# ── Chargement des assets base64
def _b64(path):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except:
        return ""

_LOGO_B64  = _b64("assets/logo_b64.txt")
_PHOTO_B64 = _b64("assets/photo_b64.txt")
LOGO_IMG   = f'<img src="data:image/png;base64,{_LOGO_B64}" style="height:38px;border-radius:6px;vertical-align:middle">' if _LOGO_B64 else '<span style="font-size:1.5rem">🩺</span>'
PHOTO_HTML = f'<img src="data:image/jpeg;base64,{_PHOTO_B64}" style="width:100%;border-radius:18px 18px 0 0;display:block">' if _PHOTO_B64 else ""

st.set_page_config(
    page_title="MedFlow AI — L'IA pour les Médecins & Chercheurs",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }
[data-testid="stAppViewContainer"] {
    background: #020c1e;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% 0%, rgba(16,185,129,0.05) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 100%, rgba(59,130,246,0.04) 0%, transparent 60%);
}
[data-testid="stSidebar"], [data-testid="collapsedControl"] { display:none; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── BASE ── */
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
h1,h2,h3 { color: #f1f5f9; }
p, li { color: #94a3b8; }
a { text-decoration: none; }

/* ── NAV ── */
html { scroll-behavior: smooth; }
.nav {
    position: sticky; top: 0; z-index: 999;
    background: rgba(4,10,22,0.78);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border-bottom: 1px solid rgba(255,255,255,0.07);
    box-shadow: 0 2px 40px rgba(0,0,0,0.5), 0 1px 0 rgba(16,185,129,0.12);
    padding: 0 48px;
    display: flex; align-items: center;
    justify-content: space-between;
    height: 64px;
    position: relative;
}
.nav::after {
    content: "";
    position: absolute; bottom: 0; left: 0;
    width: 100%; height: 2px;
    background: linear-gradient(90deg,
        transparent 0%,
        rgba(16,185,129,0.6) 25%,
        rgba(59,130,246,0.5) 55%,
        rgba(139,92,246,0.4) 80%,
        transparent 100%);
    box-shadow: 0 0 12px rgba(16,185,129,0.25);
}
.nav-logo {
    display: flex; align-items: center; gap: 10px;
    padding-right: 20px;
    border-right: 1px solid rgba(255,255,255,0.08);
}
.nav-badge {
    font-size: 0.58rem; font-weight: 700; letter-spacing: 1.5px;
    color: #10b981; background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.25);
    border-radius: 5px; padding: 2px 7px; text-transform: uppercase;
}
.nav-links {
    display: flex; gap: 2px;
    position: absolute; left: 50%; transform: translateX(-50%);
}
.nav-item { position: relative; }
.nav-item > a {
    color: #8ba3c1;
    font-size: 0.82rem; font-weight: 500; letter-spacing: 0.3px;
    padding: 7px 14px; border-radius: 8px;
    transition: all 0.18s; position: relative;
    text-decoration: none; display: flex; align-items: center; gap: 5px;
    white-space: nowrap; cursor: pointer;
}
.nav-item > a:hover { color: #f1f5f9; background: rgba(255,255,255,0.07); }
.nav-item > a.active {
    color: #f1f5f9; background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.22);
}
.nav-chevron {
    font-size: 0.6rem; opacity: 0.55; transition: transform 0.2s;
    display: inline-block;
}
.nav-item.open > a .nav-chevron { transform: rotate(180deg); }
.nav-item.open > a { color: #f1f5f9; background: rgba(255,255,255,0.07); }
.nav-dropdown {
    display: none;
    position: absolute; top: calc(100% + 10px); left: 50%;
    transform: translateX(-50%);
    min-width: 210px;
    background: rgba(4,10,24,0.97);
    backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 14px; padding: 8px;
    box-shadow: 0 24px 64px rgba(0,0,0,0.6), 0 1px 0 rgba(255,255,255,0.05) inset;
    z-index: 99999;
    animation: dropFade 0.15s ease;
}
@keyframes dropFade {
    from { opacity:0; transform: translateX(-50%) translateY(-6px); }
    to   { opacity:1; transform: translateX(-50%) translateY(0); }
}
.nav-item.open .nav-dropdown { display: block; }
.nav-dropdown-item {
    display: flex; align-items: center; gap: 10px;
    padding: 9px 12px; border-radius: 9px;
    color: #8ba3c1; font-size: 0.8rem; font-weight: 500;
    text-decoration: none; cursor: pointer;
    transition: all 0.15s;
}
.nav-dropdown-item:hover {
    background: rgba(255,255,255,0.07); color: #f1f5f9;
}
.nav-dropdown-icon {
    width: 30px; height: 30px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.9rem; flex-shrink: 0;
}
.nav-dropdown-divider {
    height: 1px; background: rgba(255,255,255,0.07); margin: 6px 4px;
}

/* ── HERO ── */
.hero {
    background: linear-gradient(160deg, #03080f 0%, #071628 50%, #03080f 100%);
    padding: 100px 80px 80px;
    position: relative; overflow: hidden;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.hero::before {
    content: "";
    position: absolute; top: -150px; left: 0; right: 0; height: 500px;
    background: radial-gradient(ellipse 70% 60% at 30% 50%, rgba(16,185,129,0.07), transparent 70%);
    pointer-events: none;
}
.hero-eyebrow {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(16,185,129,0.08);
    border: 1px solid rgba(16,185,129,0.2);
    color: #10b981; border-radius: 100px;
    padding: 6px 18px; font-size: 0.72rem; font-weight: 700;
    letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 32px;
}
.hero-title {
    font-size: clamp(2.6rem, 5.5vw, 4.4rem); font-weight: 900;
    color: #f8fafc; line-height: 1.05; margin-bottom: 24px;
    letter-spacing: -2px;
}
.hero-title .accent {
    background: linear-gradient(135deg, #10b981, #34d399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-title .accent2 {
    background: linear-gradient(135deg, #3b82f6, #60a5fa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1.1rem; color: #64748b; line-height: 1.85;
    max-width: 560px; margin-bottom: 40px; font-weight: 400;
}
.hero-tags { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 48px; }
.hero-tag {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    color: #64748b; border-radius: 100px;
    padding: 6px 16px; font-size: 0.8rem; font-weight: 500;
    backdrop-filter: blur(8px);
}
.hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
.btn-hero-primary {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    color: white; padding: 15px 38px; border-radius: 14px;
    font-weight: 800; font-size: 0.95rem;
    box-shadow: 0 8px 32px rgba(16,185,129,0.35), inset 0 1px 0 rgba(255,255,255,0.15);
    transition: transform 0.2s, box-shadow 0.2s;
}
.btn-hero-secondary {
    border: 1px solid rgba(255,255,255,0.1);
    background: rgba(255,255,255,0.03);
    color: #94a3b8; padding: 14px 34px; border-radius: 14px;
    font-weight: 600; font-size: 0.9rem;
    backdrop-filter: blur(8px);
}

/* ── LOGO BOX ── */
.logo-box {
    background: linear-gradient(145deg, #071628 0%, #050e1d 100%);
    border: 1px solid rgba(16,185,129,0.15);
    border-radius: 28px; padding: 48px 36px;
    text-align: center;
    box-shadow: 0 32px 80px rgba(0,0,0,0.6),
                inset 0 1px 0 rgba(255,255,255,0.04),
                0 0 0 1px rgba(16,185,129,0.05);
}
.logo-title-big {
    font-size: 2.4rem; font-weight: 900; letter-spacing: -1.5px;
    color: #f1f5f9; margin-bottom: 6px;
}
.logo-title-big span {
    background: linear-gradient(135deg, #10b981, #34d399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.logo-tagline { font-size: 0.85rem; color: #475569; margin-bottom: 28px; font-style: italic; }
.logo-tools-row { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }
.logo-tool-icon {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px; padding: 12px 14px;
    text-align: center; min-width: 76px;
    backdrop-filter: blur(8px);
}
.logo-tool-icon .icon { font-size: 1.5rem; margin-bottom: 4px; }
.logo-tool-icon .lbl { font-size: 0.66rem; color: #475569; font-weight: 600; }
.logo-banner {
    background: linear-gradient(90deg, #0891b2, #10b981);
    border-radius: 100px; padding: 8px 24px;
    font-size: 0.76rem; font-weight: 700; color: white;
    letter-spacing: 2.5px; text-transform: uppercase;
    display: inline-block;
    box-shadow: 0 4px 16px rgba(16,185,129,0.2);
}

/* ── SECTION ── */
.section { padding: 96px 80px; }
.section-alt {
    background: #040c1c;
    border-top: 1px solid rgba(59,130,246,0.08);
    border-bottom: 1px solid rgba(59,130,246,0.08);
    box-shadow: inset 0 1px 0 rgba(59,130,246,0.04), inset 0 -1px 0 rgba(59,130,246,0.04);
}
.section-eyebrow {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 3.5px;
    text-transform: uppercase; margin-bottom: 14px;
}
.section-h2 {
    font-size: 2.6rem; font-weight: 900; color: #f1f5f9;
    letter-spacing: -1px; line-height: 1.15; margin-bottom: 18px;
}
.section-lead { color: #475569; font-size: 1rem; line-height: 1.8; max-width: 580px; }
.divider-line { border: none; border-top: 1px solid rgba(255,255,255,0.04); }

/* ── SÉPARATION BLOCS — glow visible ── */
[data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"] {
    border: none !important;
}
.block-sep {
    width: 100%; height: 3px;
    background: linear-gradient(90deg,
        transparent 0%,
        rgba(16,185,129,0.5) 20%,
        rgba(59,130,246,0.45) 50%,
        rgba(139,92,246,0.45) 80%,
        transparent 100%);
    box-shadow: 0 0 20px rgba(16,185,129,0.15), 0 0 40px rgba(59,130,246,0.08);
    margin: 0;
}
.section-wrap {
    border-top: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 -1px 0 rgba(255,255,255,0.02), inset 0 1px 0 rgba(255,255,255,0.02);
}

/* ── ABOUT STATS ── */
.about-stat-num { font-size: 2.2rem; font-weight: 900; line-height: 1; }
.about-stat-lbl { font-size: 0.78rem; color: #475569; margin-top: 5px; letter-spacing: 0.3px; }

/* ── PHOTO MODERNE ── */
.photo-modern-wrap {
    position: relative; display: inline-block; width: 100%;
}
.photo-modern-glow {
    position: absolute; inset: -3px;
    background: linear-gradient(135deg, #10b981 0%, #3b82f6 50%, #8b5cf6 100%);
    border-radius: 26px; z-index: 0;
    opacity: 0.7; filter: blur(0px);
}
.photo-modern-inner {
    position: relative; z-index: 1;
    border-radius: 24px; overflow: hidden;
    background: #0d1829;
}
.photo-modern-inner img {
    width: 100%; display: block;
    border-radius: 24px 24px 0 0;
}
.photo-modern-caption {
    background: linear-gradient(135deg, #071628, #0d1829);
    padding: 20px 22px; border-radius: 0 0 24px 24px;
    border-top: 1px solid rgba(16,185,129,0.1);
}
.photo-floating-badge {
    position: absolute; top: 16px; right: 16px; z-index: 2;
    background: rgba(16,185,129,0.15);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(16,185,129,0.3);
    color: #10b981; border-radius: 100px;
    padding: 5px 14px; font-size: 0.72rem; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase;
}

/* ── CARDS GLASSMORPHISM ── */
.glass-card {
    background: rgba(13,24,41,0.7);
    backdrop-filter: blur(16px) saturate(150%);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px; padding: 28px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3),
                inset 0 1px 0 rgba(255,255,255,0.04);
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
}
.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(16,185,129,0.2);
    box-shadow: 0 16px 48px rgba(0,0,0,0.4), 0 0 0 1px rgba(16,185,129,0.1);
}

/* ── ROADMAP CARDS ── */
.rm-card {
    background: rgba(13,24,41,0.8);
    backdrop-filter: blur(12px);
    border-radius: 18px; padding: 24px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
    box-shadow: 0 4px 24px rgba(0,0,0,0.2);
}
.rm-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.35);
}
.rm-icon-wrap {
    width: 50px; height: 50px; border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem; margin-bottom: 14px;
}
.rm-card-title { font-size: 0.92rem; font-weight: 700; color: #f1f5f9; margin-bottom: 6px; }
.rm-card-desc { font-size: 0.78rem; color: #475569; line-height: 1.65; margin-bottom: 14px; }
.rm-badge { display: inline-block; font-size: 0.68rem; font-weight: 700; border-radius: 6px; padding: 3px 10px; }
.rm-link { display: block; margin-top: 14px; font-size: 0.76rem; font-weight: 600; }
.rm-category-label {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 2.5px;
    text-transform: uppercase; margin-bottom: 24px;
    padding: 7px 16px; border-radius: 100px; display: inline-block;
}

/* ── PUBLICATIONS ── */
.pub-card {
    background: #0d1829; border-radius: 14px; padding: 24px 28px;
    border: 1px solid rgba(255,255,255,0.06);
    border-left: 4px solid;
    margin-bottom: 16px;
}
.pub-type {
    font-size: 0.7rem; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 8px;
}
.pub-title { font-size: 0.97rem; font-weight: 700; color: #f1f5f9; line-height: 1.5; margin-bottom: 6px; }
.pub-meta { font-size: 0.8rem; color: #475569; margin-bottom: 10px; }
.pub-abstract { font-size: 0.83rem; color: #64748b; line-height: 1.65; margin-bottom: 12px; }
.pub-link {
    font-size: 0.8rem; font-weight: 600;
    padding: 5px 14px; border-radius: 6px;
    border: 1px solid;
}

/* ── TEAM ── */
.team-card {
    background: linear-gradient(135deg, #0d1f3c, #0a1628);
    border-radius: 24px; padding: 40px;
    border: 1px solid rgba(16,185,129,0.2);
    text-align: center;
}
.team-name { font-size: 1.6rem; font-weight: 900; color: #f1f5f9; margin-bottom: 6px; }
.team-role { color: #10b981; font-size: 0.95rem; margin-bottom: 16px; }
.team-bio { color: #64748b; font-size: 0.9rem; line-height: 1.75; margin-bottom: 24px; }
.team-links { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
.team-link {
    border: 1px solid rgba(255,255,255,0.1); color: #94a3b8;
    border-radius: 8px; padding: 8px 20px;
    font-size: 0.83rem; font-weight: 600;
    transition: all 0.2s;
}

/* ── CONTACT ── */
.contact-box {
    background: #0d1829; border-radius: 16px; padding: 28px 32px;
    border: 1px solid rgba(255,255,255,0.07);
    display: flex; align-items: flex-start; gap: 18px;
}
.contact-icon {
    width: 44px; height: 44px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem; flex-shrink: 0;
}
.contact-label { font-size: 0.75rem; font-weight: 700; letter-spacing: 1.5px;
    text-transform: uppercase; color: #475569; margin-bottom: 4px; }
.contact-value { font-size: 0.95rem; font-weight: 600; color: #f1f5f9; }
.contact-sub { font-size: 0.8rem; color: #64748b; margin-top: 2px; }

/* ── LEGAL ── */
.legal-section { background: #020609; padding: 64px 80px;
    border-top: 1px solid rgba(255,255,255,0.05); }
.legal-card {
    background: #080f1e; border-radius: 14px; padding: 28px 32px;
    border: 1px solid rgba(255,255,255,0.05); height: 100%;
}
.legal-title { font-size: 0.9rem; font-weight: 700; color: #94a3b8; margin-bottom: 12px; }
.legal-text { font-size: 0.82rem; color: #475569; line-height: 1.7; }

/* ── FOOTER ── */
.footer {
    background: #020609;
    border-top: 1px solid rgba(16,185,129,0.12);
    padding: 40px 80px;
    display: flex; align-items: center;
    justify-content: space-between; flex-wrap: wrap; gap: 16px;
}
.footer-brand {
    font-size: 1.1rem; font-weight: 900;
    background: linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.footer-brand span {
    background: linear-gradient(135deg, #10b981, #34d399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.footer-copy { font-size: 0.78rem; color: #4b5e78; margin-top: 4px; }
.footer-links { display: flex; gap: 20px; flex-wrap: wrap; }
.footer-links a { font-size: 0.78rem; color: #4b5e78; transition: color 0.2s; }
.footer-links a:hover { color: #10b981; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# NAV
# ─────────────────────────────────────────────────────────────────
_nd = (
    "display:none;position:absolute;top:calc(100% + 10px);left:50%;"
    "transform:translateX(-50%);min-width:200px;"
    "background:rgba(4,10,24,0.97);backdrop-filter:blur(24px);"
    "border:1px solid rgba(255,255,255,0.1);border-radius:14px;padding:8px;"
    "box-shadow:0 24px 64px rgba(0,0,0,0.6);z-index:99999;"
)
_da = (
    "display:block;padding:9px 14px;border-radius:9px;color:#8ba3c1;"
    "font-size:0.8rem;font-weight:500;text-decoration:none;cursor:pointer;white-space:nowrap;"
)
_hover_on  = "this.style.background='rgba(255,255,255,0.07)';this.style.color='#f1f5f9';"
_hover_off = "this.style.background='transparent';this.style.color='#8ba3c1';"
_div_sep   = '<div style="height:1px;background:rgba(255,255,255,0.07);margin:4px 6px"></div>'
st.markdown(
    '<div class="nav">'
    f'<div class="nav-logo">{LOGO_IMG}<span class="nav-badge">v2.0</span></div>'
    '<div class="nav-links">'

    '<div class="nav-item">'
    '<a class="nav-link" href="#about" onclick="navTo(\'about\');return false;">&#192;&nbsp;propos</a>'
    '</div>'

    '<div class="nav-item" id="ni-projets">'
    '<a class="nav-link" href="#" onclick="tDrop(\'nd-projets\');return false;">'
    'Projets &#9660;</a>'
    f'<div id="nd-projets" style="{_nd}">'
    f'<a style="{_da}" onmouseover="{_hover_on}" onmouseout="{_hover_off}"'
    ' onclick="navTo(\'roadmap\');closeDrops();return false;">'
    '&#127758; Ecosyst&egrave;me &mdash; Roadmap &amp; outils</a>'
    '</div></div>'

    '<div class="nav-item" id="ni-publications">'
    '<a class="nav-link" href="#" onclick="tDrop(\'nd-publications\');return false;">'
    'Publications &#9660;</a>'
    f'<div id="nd-publications" style="{_nd}">'
    f'<a style="{_da}" onmouseover="{_hover_on}" onmouseout="{_hover_off}"'
    ' onclick="navTo(\'publications\');closeDrops();return false;">'
    '&#128196; Travaux scientifiques</a>'
    + _div_sep +
    f'<a style="{_da}" onmouseover="{_hover_on}" onmouseout="{_hover_off}"'
    ' onclick="navTo(\'equipe\');closeDrops();return false;">'
    '&#127963; Peer-Reviewed &mdash; IHU M&eacute;diterran&eacute;e</a>'
    '</div></div>'

    '<div class="nav-item" id="ni-equipe">'
    '<a class="nav-link" href="#" onclick="tDrop(\'nd-equipe\');return false;">'
    '&Eacute;quipe &#9660;</a>'
    f'<div id="nd-equipe" style="{_nd}">'
    f'<a style="{_da}" onmouseover="{_hover_on}" onmouseout="{_hover_off}"'
    ' onclick="navTo(\'equipe\');closeDrops();return false;">'
    '&#128105; Fondateur &mdash; Dr. M.L. TALL</a>'
    + _div_sep +
    f'<a style="{_da}" onmouseover="{_hover_on}" onmouseout="{_hover_off}"'
    ' onclick="navTo(\'contact\');closeDrops();return false;">'
    '&#9993; Contact &mdash; Nous &eacute;crire</a>'
    '</div></div>'

    '<div class="nav-item">'
    '<a class="nav-link" href="#contact" onclick="navTo(\'contact\');return false;">Contact</a>'
    '</div>'

    '<div class="nav-item">'
    '<a class="nav-link" href="#legal" onclick="navTo(\'legal\');return false;">Mentions l&eacute;gales</a>'
    '</div>'

    '</div></div>',
    unsafe_allow_html=True
)
components.html("""
<script>
(function(){
  var p = window.parent.document;
  var _drops = ["nd-projets","nd-publications","nd-equipe"];
  function navTo(id){
    var el = p.getElementById(id);
    if(el) el.scrollIntoView({behavior:"smooth", block:"start"});
    p.querySelectorAll(".nav-link").forEach(function(a){
      a.style.background=""; a.style.color="#8ba3c1";
    });
    var hit = p.querySelector(".nav-link[href='#"+id+"']");
    if(hit){ hit.style.background="rgba(16,185,129,0.12)"; hit.style.color="#f1f5f9"; }
  }
  function tDrop(id){
    _drops.forEach(function(d){
      var el=p.getElementById(d); if(el && d!==id) el.style.display="none";
    });
    var drop = p.getElementById(id);
    if(drop) drop.style.display = (drop.style.display==="block" ? "none" : "block");
  }
  function closeDrops(){
    _drops.forEach(function(d){ var el=p.getElementById(d); if(el) el.style.display="none"; });
  }
  p.querySelectorAll(".nav-link").forEach(function(a){
    a.addEventListener("click", function(e){
      var href = this.getAttribute("href");
      var id = href && href.startsWith("#") ? href.slice(1) : null;
      if(id) { e.preventDefault(); navTo(id); }
    });
  });
  p.querySelectorAll("[onclick]").forEach(function(el){
    var oc = el.getAttribute("onclick")||"";
    if(oc.includes("tDrop")){
      var m = oc.match(/tDrop\\('([^']+)'\\)/);
      if(m){ el.addEventListener("click", function(e){ e.preventDefault(); tDrop(m[1]); }); }
    }
    if(oc.includes("navTo") && !oc.includes("tDrop")){
      var m2 = oc.match(/navTo\\('([^']+)'\\)/);
      if(m2){ el.addEventListener("click", function(e){ e.preventDefault(); navTo(m2[1]); closeDrops(); }); }
    }
  });
  p.addEventListener("click", function(e){
    if(!e.target.closest(".nav-item")) closeDrops();
  });
})();
</script>
""", height=0)

# ─────────────────────────────────────────────────────────────────
# HERO — full-width centered + stats bar
# ─────────────────────────────────────────────────────────────────
_logo_big = LOGO_IMG.replace('height:38px', 'height:80px').replace('border-radius:6px', 'border-radius:14px') if _LOGO_B64 else '<span style="font-size:4rem">🩺</span>'

_hero_html = (
    '<div style="background:linear-gradient(170deg,#020c1e 0%,#031525 45%,#020b18 100%);'
    'padding:100px 80px 0;position:relative;overflow:hidden;">'
    '<div style="position:absolute;top:-120px;left:-60px;width:600px;height:600px;'
    'background:radial-gradient(ellipse,rgba(16,185,129,0.07) 0%,transparent 65%);'
    'pointer-events:none"></div>'
    '<div style="position:absolute;top:-80px;right:-80px;width:500px;height:500px;'
    'background:radial-gradient(ellipse,rgba(59,130,246,0.06) 0%,transparent 65%);'
    'pointer-events:none"></div>'
    '<div style="max-width:860px;margin:0 auto;text-align:center;position:relative;z-index:1">'
    f'<div style="margin-bottom:28px">{_logo_big}</div>'
    '<div style="display:inline-flex;align-items:center;gap:8px;'
    'background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.22);'
    'color:#10b981;border-radius:100px;padding:7px 20px;'
    'font-size:0.72rem;font-weight:700;letter-spacing:2.5px;'
    'text-transform:uppercase;margin-bottom:32px">'
    '&#128302; Recherche &amp; Clinique &middot; Open Source'
    '</div>'
    '<div style="font-size:clamp(2.8rem,6vw,4.8rem);font-weight:900;color:#f8fafc;'
    'line-height:1.04;letter-spacing:-2.5px;margin-bottom:24px">'
    "L'IA au service des<br>"
    '<span style="background:linear-gradient(135deg,#10b981 0%,#34d399 50%,#3b82f6 100%);'
    '-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">'
    'M&eacute;decins &amp; Chercheurs'
    '</span></div>'
    '<div style="font-size:1.1rem;color:#64748b;line-height:1.8;max-width:640px;margin:0 auto 40px">'
    'Des outils IA con&ccedil;us par un chercheur en bioinformatique m&eacute;dicale &mdash; '
    'pour la d&eacute;cision clinique, l&rsquo;analyse multi-omique et la recherche translationnelle. '
    '<strong style="color:#94a3b8">Enti&egrave;rement en fran&ccedil;ais.</strong>'
    '</div>'
    '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-bottom:44px">'
    '<span class="hero-tag">&#129302; Claude AI</span>'
    '<span class="hero-tag">&#129516; Multi-omique</span>'
    '<span class="hero-tag">&#128202; 9 outils d&eacute;ploy&eacute;s</span>'
    '<span class="hero-tag">&#128218; 5 Preprints soumis 2026</span>'
    '<span class="hero-tag">&#127467;&#127479; 100&nbsp;% fran&ccedil;ais</span>'
    '<span class="hero-tag">&#128275; Open Source</span>'
    '</div>'
    '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:72px">'
    '<a href="https://buy.stripe.com/9B63cvb3G8kZ5cGfHwb3q01" target="_blank" class="btn-hero-primary">'
    'Commencer &mdash; 9&euro;/mois'
    '</a>'
    '<a href="https://cardiac-qol-ai.streamlit.app" target="_blank" class="btn-hero-secondary">'
    'Essayer gratuitement &rarr;'
    '</a>'
    '</div>'
    '</div>'
    '<div style="border-top:1px solid rgba(255,255,255,0.06);'
    'background:rgba(2,8,16,0.6);backdrop-filter:blur(12px);'
    'padding:28px 80px;display:flex;justify-content:center;flex-wrap:wrap">'
    '<div style="display:flex;align-items:center;gap:32px;flex-wrap:wrap;justify-content:center">'
    '<div style="text-align:center;padding:0 32px">'
    '<div style="font-size:2rem;font-weight:900;color:#10b981;line-height:1">9</div>'
    '<div style="font-size:0.72rem;color:#475569;margin-top:4px">Outils d&eacute;ploy&eacute;s</div>'
    '</div>'
    '<div style="width:1px;height:40px;background:rgba(255,255,255,0.06)"></div>'
    '<div style="text-align:center;padding:0 32px">'
    '<div style="font-size:2rem;font-weight:900;color:#3b82f6;line-height:1">31+</div>'
    '<div style="font-size:0.72rem;color:#475569;margin-top:4px">Publications index&eacute;es</div>'
    '</div>'
    '<div style="width:1px;height:40px;background:rgba(255,255,255,0.06)"></div>'
    '<div style="text-align:center;padding:0 32px">'
    '<div style="font-size:2rem;font-weight:900;color:#8b5cf6;line-height:1">5&nbsp;800+</div>'
    '<div style="font-size:0.72rem;color:#475569;margin-top:4px">&Eacute;chantillons analys&eacute;s</div>'
    '</div>'
    '<div style="width:1px;height:40px;background:rgba(255,255,255,0.06)"></div>'
    '<div style="text-align:center;padding:0 32px">'
    '<div style="font-size:2rem;font-weight:900;color:#f59e0b;line-height:1">248+</div>'
    '<div style="font-size:0.72rem;color:#475569;margin-top:4px">Citations Google Scholar</div>'
    '</div>'
    '</div>'
    '</div>'
    '</div>'
)
st.markdown(_hero_html, unsafe_allow_html=True)

st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# ABOUT — Mission + Photo fondateur
# ─────────────────────────────────────────────────────────────────
st.markdown("<div id='about'></div>", unsafe_allow_html=True)

# ── PHOTO src inline — blocs pré-construits pour éviter les conditionnels dans f-string ──
_photo_src = f"data:image/jpeg;base64,{_PHOTO_B64}" if _PHOTO_B64 else ""

if _photo_src:
    _photo_card_about = (
        '<div style="text-align:center">'
        '<div style="position:relative;display:inline-block">'
        '<div style="border-radius:999px;'
        'background:linear-gradient(160deg,#10b981 0%,#3b82f6 50%,#8b5cf6 100%);'
        'padding:3px;box-shadow:0 0 48px rgba(16,185,129,0.18),0 24px 64px rgba(0,0,0,0.55)">'
        '<div style="border-radius:999px;overflow:hidden;background:#03080f">'
        f'<img src="{_photo_src}" style="width:260px;display:block;'
        'height:340px;object-fit:cover;object-position:50% 18%">'
        '</div></div>'
        '<div style="position:absolute;top:18px;left:50%;transform:translateX(-50%);'
        'background:rgba(3,8,15,0.88);backdrop-filter:blur(16px);'
        'border:1px solid rgba(16,185,129,0.45);color:#10b981;'
        'border-radius:100px;padding:5px 16px;white-space:nowrap;'
        'font-size:0.67rem;font-weight:700;letter-spacing:2px;text-transform:uppercase">'
        '&#9679; Fondateur &amp; CEO'
        '</div></div>'
        '<div style="margin-top:18px">'
        '<div style="font-size:1rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.3px">'
        'Dr. Mamadou Lamine TALL'
        '</div>'
        '<div style="font-size:0.76rem;font-weight:600;color:#34d399;margin-top:5px">'
        'PhD Bioinformatique &middot; Aix-Marseille 2020'
        '</div></div></div>'
    )
    _photo_card_team = (
        '<div style="text-align:center">'
        '<div style="position:relative;display:inline-block">'
        '<div style="border-radius:999px;'
        'background:linear-gradient(160deg,#f59e0b 0%,#ef4444 50%,#8b5cf6 100%);'
        'padding:3px;box-shadow:0 0 40px rgba(245,158,11,0.15),0 20px 60px rgba(0,0,0,0.5)">'
        '<div style="border-radius:999px;overflow:hidden;background:#03080f">'
        f'<img src="{_photo_src}" style="width:240px;display:block;'
        'height:316px;object-fit:cover;object-position:50% 18%">'
        '</div></div></div>'
        '<div style="margin-top:16px">'
        '<div style="font-size:0.95rem;font-weight:800;color:#f1f5f9">Dr. Mamadou Lamine TALL</div>'
        '<div style="font-size:0.72rem;color:#f59e0b;margin-top:4px;font-weight:700;letter-spacing:0.8px">'
        'PhD &middot; Aix-Marseille &middot; 2020'
        '</div></div></div>'
    )
else:
    _fallback = '<div style="height:380px;background:linear-gradient(135deg,#071628,#0d1829);display:flex;align-items:center;justify-content:center;font-size:5rem">👤</div>'
    _photo_card_about = _fallback
    _photo_card_team  = _fallback

st.markdown("""
<div style="background:#050e1d;padding:56px 0 0;
     border-bottom:1px solid rgba(255,255,255,0.04)">
</div>
""", unsafe_allow_html=True)

col_about_photo, col_about_text = st.columns([1, 2], gap="large")

with col_about_photo:
    st.markdown(f"""
    <div style="padding:0 0 56px 40px;background:#050e1d">
      {_photo_card_about}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px">
        <div style="background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.12);
             border-radius:14px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#10b981;line-height:1">9</div>
          <div style="font-size:0.7rem;color:#475569;margin-top:3px">Outils déployés</div>
        </div>
        <div style="background:rgba(59,130,246,0.06);border:1px solid rgba(59,130,246,0.12);
             border-radius:14px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#3b82f6;line-height:1">31+</div>
          <div style="font-size:0.7rem;color:#475569;margin-top:3px">Publications</div>
        </div>
        <div style="background:rgba(139,92,246,0.06);border:1px solid rgba(139,92,246,0.12);
             border-radius:14px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#8b5cf6;line-height:1">5 800+</div>
          <div style="font-size:0.7rem;color:#475569;margin-top:3px">Échantillons</div>
        </div>
        <div style="background:rgba(245,158,11,0.06);border:1px solid rgba(245,158,11,0.12);
             border-radius:14px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#f59e0b;line-height:1">248+</div>
          <div style="font-size:0.7rem;color:#475569;margin-top:3px">Citations</div>
        </div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:14px">
        <a href="https://github.com/mamadoulaminetall" target="_blank"
           style="flex:1;text-align:center;background:rgba(255,255,255,0.04);
           border:1px solid rgba(255,255,255,0.07);color:#64748b;
           border-radius:10px;padding:8px 12px;font-size:0.76rem;font-weight:600">GitHub ↗</a>
        <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank"
           style="flex:1;text-align:center;background:rgba(255,255,255,0.04);
           border:1px solid rgba(255,255,255,0.07);color:#64748b;
           border-radius:10px;padding:8px 12px;font-size:0.76rem;font-weight:600">Scholar ↗</a>
        <a href="https://theses.fr/2020AIXM0426" target="_blank"
           style="flex:1;text-align:center;background:rgba(255,255,255,0.04);
           border:1px solid rgba(255,255,255,0.07);color:#64748b;
           border-radius:10px;padding:8px 12px;font-size:0.76rem;font-weight:600">Thèse ↗</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_about_text:
    st.markdown("""
    <div style="padding:0 40px 56px 0;background:#050e1d">
      <div style="font-size:0.7rem;font-weight:700;letter-spacing:3.5px;
           text-transform:uppercase;color:#10b981;margin-bottom:14px">
        À propos · Mission
      </div>
      <div style="font-size:2.8rem;font-weight:900;color:#f1f5f9;
           letter-spacing:-1.2px;line-height:1.1;margin-bottom:24px">
        Pourquoi<br>
        <span style="background:linear-gradient(135deg,#10b981,#34d399);
              -webkit-background-clip:text;-webkit-text-fill-color:transparent">
          MedFlow AI ?
        </span>
      </div>
      <div style="color:#64748b;font-size:1rem;line-height:1.85;margin-bottom:36px">
        MedFlow AI est né d'un constat simple :
        <strong style="color:#cbd5e1">les cliniciens manquent d'outils IA accessibles, validés et en français</strong>
        — des outils qui s'intègrent directement dans leur pratique, sans barrière technique,
        sans jargon informatique, directement au chevet du patient.
        <br><br>
        Fondé par un chercheur en bioinformatique médicale, MedFlow AI réunit deux convictions :
        les données cliniques et biologiques contiennent une richesse sous-exploitée,
        et l'IA peut aider les cliniciens à en extraire la valeur — en moins de 5 minutes,
        en open source, et toujours en français.
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:36px">
        <div style="background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.12);
             border-radius:16px;padding:20px">
          <div style="width:36px;height:36px;background:rgba(16,185,129,0.12);border-radius:10px;
               display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:12px">🎯</div>
          <div style="font-weight:700;color:#e2e8f0;font-size:0.88rem;margin-bottom:6px">Aide à la décision</div>
          <div style="color:#475569;font-size:0.78rem;line-height:1.6">Calcul, analyse et alerte au chevet du patient.</div>
        </div>
        <div style="background:rgba(59,130,246,0.05);border:1px solid rgba(59,130,246,0.12);
             border-radius:16px;padding:20px">
          <div style="width:36px;height:36px;background:rgba(59,130,246,0.12);border-radius:10px;
               display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:12px">📊</div>
          <div style="font-weight:700;color:#e2e8f0;font-size:0.88rem;margin-bottom:6px">Evidence-based</div>
          <div style="color:#475569;font-size:0.78rem;line-height:1.6">Méta-analyses PRISMA et cohortes validées.</div>
        </div>
        <div style="background:rgba(139,92,246,0.05);border:1px solid rgba(139,92,246,0.12);
             border-radius:16px;padding:20px">
          <div style="width:36px;height:36px;background:rgba(139,92,246,0.12);border-radius:10px;
               display:flex;align-items:center;justify-content:center;font-size:1.1rem;margin-bottom:12px">🔓</div>
          <div style="font-weight:700;color:#e2e8f0;font-size:0.88rem;margin-bottom:6px">Open Source</div>
          <div style="color:#475569;font-size:0.78rem;line-height:1.6">Code public GitHub. Gratuit ou 9€/mois.</div>
        </div>
      </div>
      <div style="background:rgba(245,158,11,0.04);border:1px solid rgba(245,158,11,0.12);
           border-radius:16px;padding:22px 24px">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
          <div style="width:32px;height:32px;background:rgba(245,158,11,0.1);border-radius:8px;
               display:flex;align-items:center;justify-content:center;font-size:1rem">🎓</div>
          <div style="font-weight:700;color:#f59e0b;font-size:0.82rem;letter-spacing:0.5px">Thèse de Doctorat · 2020</div>
        </div>
        <div style="font-style:italic;color:#cbd5e1;font-size:0.9rem;line-height:1.6;margin-bottom:8px">
          "Études bioinformatiques et biostatistiques des structures mosaïques des génomes microbiens"
        </div>
        <div style="color:#475569;font-size:0.8rem">
          Aix-Marseille Université · Directeur : Pr. Anthony Levasseur
          · Mots-clés : mosaïcisme génomique, taxonogénomique, phylogénomique
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# ÉCOSYSTÈME — Roadmap + Outils en vue "planètes"
# ─────────────────────────────────────────────────────────────────
st.markdown("<div id='roadmap'></div>", unsafe_allow_html=True)

# ── Données outils cliniques
_eco_tools = [
    {"icon": "🫀", "color": "#ef4444", "title": "QoL Cardiac",
     "desc": "4 questionnaires · percentiles · 600 patients",
     "badge": "Gratuit", "bc": "rgba(16,185,129,0.15)", "bt": "#10b981",
     "url": "https://cardiac-qol-ai.streamlit.app"},
    {"icon": "📊", "color": "#3b82f6", "title": "Scores Cliniques",
     "desc": "15 scores : CHA₂DS₂-VASc, HEART, qSOFA, Glasgow…",
     "badge": "Gratuit", "bc": "rgba(16,185,129,0.15)", "bt": "#10b981",
     "url": "https://clinia-scores.streamlit.app"},
    {"icon": "💓", "color": "#60a5fa", "title": "Réinnervation IA",
     "desc": "VFC/HRV prédictif post-transplantation · AUC 0.961",
     "badge": "Gratuit", "bc": "rgba(16,185,129,0.15)", "bt": "#10b981",
     "url": "https://reinnervationaiapp.streamlit.app"},
    {"icon": "📈", "color": "#10b981", "title": "Biostatistiques",
     "desc": "CSV → t-test, ANOVA, Kaplan-Meier · graphiques publi.",
     "badge": "9€/mois", "bc": "rgba(59,130,246,0.12)", "bt": "#60a5fa",
     "url": "https://clinia-biostat.streamlit.app"},
    {"icon": "📝", "color": "#06b6d4", "title": "Générateur CR IA",
     "desc": "Données cliniques → CR structuré → Export PDF",
     "badge": "9€/mois", "bc": "rgba(59,130,246,0.12)", "bt": "#60a5fa",
     "url": "https://clinia-cr.streamlit.app"},
    {"icon": "📚", "color": "#8b5cf6", "title": "Revue Littérature IA",
     "desc": "PubMed + Claude → synthèse evidence-based",
     "badge": "9€/mois", "bc": "rgba(59,130,246,0.12)", "bt": "#60a5fa",
     "url": "https://clinia-review.streamlit.app"},
    {"icon": "🧬", "color": "#a78bfa", "title": "MYOomics",
     "desc": "RNA-seq · scRNA-seq · ML · myopathies",
     "badge": "Gratuit", "bc": "rgba(16,185,129,0.15)", "bt": "#10b981",
     "url": "https://myoomics.streamlit.app"},
    {"icon": "🫀", "color": "#f43f5e", "title": "CardioSurg AI",
     "desc": "EuroSCORE II + ML · complications post-op · timing valvulaire · CR opératoire",
     "badge": "Nouveau", "bc": "rgba(244,63,94,0.15)", "bt": "#f43f5e",
     "url": "https://cardiosurg-ai.streamlit.app"},
]

_left_eco  = _eco_tools[:4]   # QoL, Scores, Réinnervation, Biostat
_right_eco = _eco_tools[4:]   # Générateur CR, Revue, MYOomics, CardioSurg AI

def _eco_card(t, side):
    """Compact planet card — left cards face right, right cards face left."""
    icon_order = "row-reverse" if side == "left" else "row"
    txt_align  = "right" if side == "left" else "left"
    acc_border = (
        f"border-right:2px solid {t['color']}55" if side == "left"
        else f"border-left:2px solid {t['color']}55"
    )
    return (
        f'<div style="background:#060e1e;border:1px solid rgba(255,255,255,0.07);'
        f'border-radius:14px;padding:14px 16px;{acc_border};'
        'transition:transform 0.2s,box-shadow 0.2s">'
        f'<div style="display:flex;align-items:center;gap:10px;flex-direction:{icon_order}">'
        f'<div style="width:40px;height:40px;border-radius:11px;flex-shrink:0;'
        f'background:{t["color"]}18;display:flex;align-items:center;'
        f'justify-content:center;font-size:1.3rem">{t["icon"]}</div>'
        f'<div style="flex:1;text-align:{txt_align}">'
        f'<div style="font-size:0.86rem;font-weight:800;color:#f1f5f9;margin-bottom:2px">{t["title"]}</div>'
        f'<div style="font-size:0.71rem;color:#4b6280;line-height:1.4;margin-bottom:6px">{t["desc"]}</div>'
        f'<div style="display:flex;gap:6px;justify-content:{"flex-end" if side=="left" else "flex-start"};'
        'flex-wrap:wrap;align-items:center">'
        f'<span style="background:{t["bc"]};color:{t["bt"]};border-radius:5px;'
        f'padding:2px 8px;font-size:0.67rem;font-weight:700">{t["badge"]}</span>'
        f'<a href="{t["url"]}" target="_blank" style="color:{t["color"]};font-size:0.71rem;'
        'font-weight:700;text-decoration:none">Ouvrir ↗</a>'
        '</div>'
        '</div>'
        '</div>'
        '</div>'
    )

_left_cards_html  = "".join(_eco_card(t, "left")  for t in _left_eco)
_right_cards_html = "".join(_eco_card(t, "right") for t in _right_eco)

# ── Centre : timeline solaire
_timeline_steps = [
    ("#f59e0b", "🎓", "Thèse 2020",      "Bioinformatique · AMU"),
    ("#10b981", "🦠", "Recherche",        "Microbiome · Génomique"),
    ("#3b82f6", "💓", "Cardiologie 2025", "Réinnervation · QoL"),
    ("#10b981", "🚀", "MedFlow AI",       "7 outils SaaS déployés"),
    ("#8b5cf6", "🌟", "Vision 2026+",     "PhyMedExp · MYOccitanie"),
]

_tl_html = ""
for idx, (col, ico, lbl, sub) in enumerate(_timeline_steps):
    is_sun = "🚀" in ico
    sz     = "60px" if is_sun else "46px"
    fsz    = "1.5rem" if is_sun else "1.1rem"
    glow   = (f"box-shadow:0 0 28px {col}88,0 0 56px {col}44;"
              if is_sun else f"box-shadow:0 0 10px {col}55;")
    bw     = "3px" if is_sun else "2px"
    conn   = (
        f'<div style="width:2px;height:28px;background:linear-gradient({col}55,transparent);'
        'margin:2px auto"></div>'
        if idx < len(_timeline_steps) - 1 else ""
    )
    _tl_html += (
        '<div style="display:flex;flex-direction:column;align-items:center">'
        f'<div style="width:{sz};height:{sz};border-radius:50%;'
        f'background:{col}15;border:{bw} solid {col};{glow}'
        f'display:flex;align-items:center;justify-content:center;font-size:{fsz}">'
        f'{ico}</div>'
        '<div style="text-align:center;margin-top:5px;margin-bottom:2px">'
        f'<div style="font-size:{"0.88rem" if is_sun else "0.76rem"};'
        f'font-weight:{"900" if is_sun else "700"};'
        f'color:{"#f1f5f9" if is_sun else "#cbd5e1"}">{lbl}</div>'
        f'<div style="font-size:0.67rem;color:#4b6280">{sub}</div>'
        '</div>'
        + conn +
        '</div>'
    )

_center_col = (
    '<div style="display:flex;flex-direction:column;align-items:center;padding:20px 18px;'
    'background:linear-gradient(180deg,rgba(16,185,129,0.04) 0%,'
    'rgba(59,130,246,0.06) 50%,rgba(139,92,246,0.04) 100%);'
    'border:1px solid rgba(255,255,255,0.07);border-radius:24px;'
    'box-shadow:0 0 60px rgba(16,185,129,0.06),0 0 120px rgba(59,130,246,0.04)">'
    + _tl_html +
    '</div>'
)

# ── Ellipses SVG déco (fond)
_svg_orbits = (
    '<svg style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);'
    'width:95%;height:95%;pointer-events:none;z-index:0;opacity:0.6" '
    'viewBox="0 0 1000 500" preserveAspectRatio="xMidYMid meet">'
    '<ellipse cx="500" cy="250" rx="470" ry="210" '
    'stroke="rgba(16,185,129,0.07)" stroke-width="1" stroke-dasharray="10,6" fill="none"/>'
    '<ellipse cx="500" cy="250" rx="340" ry="150" '
    'stroke="rgba(59,130,246,0.07)" stroke-width="1" stroke-dasharray="7,5" fill="none"/>'
    '</svg>'
)

# ── Section complète
_galaxy_html = (
    '<div class="section section-alt" style="padding-bottom:64px">'

    # Header
    '<div style="text-align:center;margin-bottom:52px">'
    '<div class="section-eyebrow" style="color:#3b82f6;text-align:center">'
    'Roadmap &middot; Outils &middot; GitHub</div>'
    '<div class="section-h2" style="text-align:center">'
    '&Eacute;cosyst&egrave;me MedFlow AI</div>'
    '<div style="color:#475569;font-size:0.95rem;max-width:560px;'
    'margin:0 auto;line-height:1.7">'
    'De la recherche fondamentale aux outils cliniques d&eacute;ploy&eacute;s &mdash; '
    'chaque projet est interconnect&eacute; dans l&rsquo;&eacute;cosyst&egrave;me MedFlow AI.'
    '</div>'
    '</div>'

    # Galaxy grid
    '<div style="position:relative">'
    + _svg_orbits +
    '<div style="display:grid;grid-template-columns:1fr 260px 1fr;gap:20px;'
    'align-items:center;position:relative;z-index:1">'

    # Left planets
    f'<div style="display:flex;flex-direction:column;gap:13px">{_left_cards_html}</div>'

    # Center sun/timeline
    f'<div>{_center_col}</div>'

    # Right planets
    f'<div style="display:flex;flex-direction:column;gap:13px">{_right_cards_html}</div>'

    '</div>'
    '</div>'

    '</div>'
)

st.markdown(_galaxy_html, unsafe_allow_html=True)
st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# PUBLICATIONS
# ─────────────────────────────────────────────────────────────────
st.markdown("<div id='publications'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="section" style="background:#030810">
  <div class="section-eyebrow" style="color:#8b5cf6">Publications · Preprints · Recherche</div>
  <div class="section-h2">Travaux scientifiques</div>
  <div class="section-lead" style="margin-bottom:48px">
    Preprints, méta-analyses et revues systématiques publiées dans le cadre des projets MedFlow AI.
  </div>
""", unsafe_allow_html=True)

publications = [
    {
        "color": "#f59e0b",
        "type": "Thèse de Doctorat · Bioinformatique · Aix-Marseille Université",
        "title": "Études bioinformatiques et biostatistiques des structures mosaïques des génomes microbiens",
        "meta": "Dr. Mamadou Lamine TALL · Aix-Marseille Université · Soutenu le 27 novembre 2020 · Directeur : Pr. Anthony Levasseur",
        "abstract": (
            "Ce travail de thèse examine les structures mosaïques des génomes microbiens à l'aide "
            "d'approches bioinformatiques et biostatistiques. Il évalue l'impact des transferts de séquences "
            "sur la classification phylogénétique des micro-organismes et explore les corrélations statistiques "
            "entre échanges de séquences et communautés microbiennes. Plusieurs génomes bactériens "
            "nouvellement séquencés ont été analysés, démontrant la complexité de l'assignation taxonomique "
            "à l'ère de la génomique comparative. Mots-clés : bioinformatique, mosaïcisme génomique, "
            "taxonogénomique, biostatistiques."
        ),
        "tags": ["Mosaïcisme génomique", "Taxonogénomique", "Génomique comparative", "Biostatistiques", "Aix-Marseille", "2020"],
        "url": "https://theses.fr/2020AIXM0426",
        "url_label": "Theses.fr →",
        "github": "https://github.com/mamadoulaminetall",
    },
    {
        "color": "#3b82f6",
        "type": "Preprint · Méta-analyse · Revue systématique · IA prédictive · 2026",
        "title": "Autonomic Reinnervation after Cardiac Transplantation: A Systematic Review and Meta-Analysis of Heart Rate Variability Recovery Patterns across 23 Studies",
        "meta": "Dr. Mamadou Lamine TALL · medRxiv · En modération · 23 études · N=1 247 patients",
        "abstract": (
            "Méta-analyse random-effects (DerSimonian-Laird) portant sur 23 études (N=1 247 transplantés cardiaques, 1995–2022). "
            "Taux de réinnervation poolé global : 56,1 % [95%CI 51,9–60,3 %, I²=51 %]. "
            "Évolution temporelle : précoce (≤18 mois) 37,3 %, intermédiaire (18–36 mois) 53,9 %, "
            "tardif (>36 mois) 65,9 %. Le seuil 50 % est franchi entre 18 et 24 mois post-greffe. "
            "SDNN à 12 mois : meilleur prédicteur précoce (OR=3,14, p<0,001). "
            "Plateforme IA prédictive : Random Forest AUC=0,961. PRISMA 2020."
        ),
        "tags": ["VFC / HRV", "Transplantation cardiaque", "DL meta-analysis · 56,1 %", "PRISMA 2020", "SDNN · LF/HF", "Random Forest AUC=0.961"],
        "url": "https://reinnervationaiapp.streamlit.app",
        "url_label": "Plateforme IA →",
        "github": "https://github.com/mamadoulaminetall/reinnervation_ai_app",
    },
    {
        "color": "#8b5cf6",
        "type": "Preprint · Méta-analyse multi-omique · PRISMA 2026",
        "title": "Multi-Omics Profiling in Inherited Muscular Dystrophies: A Systematic Review and Meta-Analysis of Transcriptomic, Epigenomic, and Proteomic Studies across Four Major Disease Subtypes",
        "meta": "Dr. Mamadou Lamine TALL · medRxiv · En modération · 22 études · N=651 échantillons",
        "abstract": (
            "Méta-analyse random-effects (DerSimonian-Laird) sur 22 études (N=651 échantillons) "
            "portant sur 25 gènes musculaires de référence (DMD, UTRN, CAPN3, DYSF, DMPK…). "
            "Taux de dérégulation poolé : DMD 76,4 % [69,6–82,0 %], DM1 74,1 %, FSHD 66,3 %, LGMD 64,7 %. "
            "RNA-seq : meilleure sensibilité (79,4 %). 15 voies enrichies dans >70 % des études. "
            "Signature 25-gènes validée comme référence diagnostique multi-plateforme. PRISMA 2020."
        ),
        "tags": ["RNA-seq · RNA-seq", "DMD · LGMD · DM1 · FSHD", "DL meta-analysis · 76,4 %", "25-gene signature", "PRISMA 2020", "22 études · 651 samples"],
        "url": "https://github.com/mamadoulaminetall/MYOomics_Project",
        "url_label": "GitHub →",
        "github": "https://github.com/mamadoulaminetall/MYOomics_Project",
    },
    {
        "color": "#ef4444",
        "type": "Méta-analyse · Cardiologie · PRISMA 2026",
        "title": "Qualité de Vie chez le Patient Cardiaque en liste d'attente, sous LVAD et post-transplantation : Méta-analyse PRISMA",
        "meta": "Dr. Mamadou Lamine TALL · medRxiv MEDRXIV/2026/351204 · En screening · 15 études · N=600 patients",
        "abstract": (
            "Méta-analyse systématique de la qualité de vie (QdV) mesurée par KCCQ, SF-36 (PCS/MCS), "
            "Minnesota Living with Heart Failure Questionnaire et EQ-5D chez trois populations : "
            "patients en liste d'attente de greffe cardiaque (études : Grady 2004, Dew 2005, Kugler 2010/2013…), "
            "sous assistance ventriculaire gauche LVAD (Slaughter NEJM 2009, Cowger JACC HF 2017, Rogers 2010…) "
            "et post-transplantation (Evangelista Heart 2014…). Analyse des trajectoires temporelles T0–T5, "
            "percentiles de référence et alerte si dégradation > 10 points. Base de l'outil QoL Cardiac."
        ),
        "tags": ["KCCQ", "SF-36 PCS/MCS", "LVAD", "Greffe cardiaque", "EQ-5D · Mn.LHFQ", "15 études · 600 patients"],
        "url": "https://cardiac-qol-ai.streamlit.app",
        "url_label": "Outil QoL Cardiac →",
        "github": "https://github.com/mamadoulaminetall/cardiac-qol-ai",
    },
    {
        "color": "#10b981",
        "type": "Preprint · Méta-analyse · Microbiome · Oncologie · 2026",
        "title": "Gut Microbiome Signatures as Early Diagnostic Biomarkers in Colorectal, Pancreatic, Gastric, Hepatocellular and Lung Cancers: A Systematic Review and Meta-Analysis of 18 Studies",
        "meta": "Dr. Mamadou Lamine TALL · bioRxiv BIORXIV/2026/719461 · En screening · 18 études · N=2 587 patients",
        "abstract": (
            "Méta-analyse random-effects (DerSimonian-Laird) portant sur 18 études (N=2 587 patients, 5 cancers). "
            "Sensibilité diagnostique poolée : cancer colorectal 74,1 % [68,2–79,3 %], pancréatique 71,8 %, "
            "gastrique 69,4 %, hépatocellulaire 67,2 %, pulmonaire 65,9 %. "
            "I²=62 % expliqué par le type de cancer et la méthode de séquençage. "
            "Biomarqueurs clés : Fusobacterium nucleatum, Bacteroides fragilis, Clostridiales spp. "
            "Modèles ML (RF AUC=0,91). PRISMA 2020."
        ),
        "tags": ["Microbiome", "5 cancers · DL meta-analysis", "16S rRNA · métagénomique", "RF AUC=0.91", "PRISMA 2020", "18 études · 2 587 patients"],
        "url": "https://github.com/mamadoulaminetall/microbiome_diagnostic_cancer_precoce",
        "url_label": "GitHub →",
        "github": "https://github.com/mamadoulaminetall/microbiome_diagnostic_cancer_precoce",
    },
    {
        "color": "#06b6d4",
        "type": "Preprint · Méta-analyse · Génétique · CMA · 2026",
        "title": "Chromosomal Microarray Analysis in Neurodevelopmental Disorders: A Systematic Review and Meta-Analysis of Diagnostic Yield across Six Clinical Indications in 79,417 Patients",
        "meta": "Dr. Mamadou Lamine TALL · medRxiv MEDRXIV/2026/351221 · En screening · 25 études · N=79 417 patients",
        "abstract": (
            "Méta-analyse random-effects (DerSimonian-Laird) portant sur 25 études (N=79 417 patients). "
            "Rendement diagnostique poolé global : 15,4 % [13,8–17,1 %, I²=89 %]. "
            "Par indication : déficience intellectuelle 16,2 %, TSA 11,8 %, anomalies congénitales multiples 22,4 %, "
            "prénatal 7,3 %, épilepsie 10,5 %, troubles psychiatriques 8,9 %. "
            "Classification ACMG des CNVs (Pathogène / Probablement pathogène / VUS). "
            "Plateforme Streamlit de diagnostic CNV déployée. PRISMA 2020."
        ),
        "tags": ["CNV · CMA", "6 indications · DL meta-analysis", "ACMG classification", "25 études · 79 417 patients", "PRISMA 2020", "Streamlit platform"],
        "url": "https://cnv-diagnostic-platform.streamlit.app",
        "url_label": "Plateforme CNV →",
        "github": "https://github.com/mamadoulaminetall/cnv-diagnostic-platform",
    },
]

# ── Grille de boxes verticales ──
_pub_cards_html = (
    '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-bottom:8px">'
)
for pub in publications:
    tags_html = "".join(
        '<span style="background:#0a1628;color:#475569;border-radius:5px;'
        'padding:2px 9px;font-size:0.68rem;margin:2px 2px 0 0;display:inline-block;'
        'border:1px solid rgba(255,255,255,0.05)">' + t + '</span>'
        for t in pub["tags"]
    )
    _pub_cards_html += (
        '<div style="display:flex;flex-direction:column;background:#060e1e;'
        'border:1px solid rgba(255,255,255,0.06);border-radius:16px;overflow:hidden;'
        'transition:transform 0.2s,box-shadow 0.2s">'

        # Bande colorée en haut
        f'<div style="height:4px;background:{pub["color"]};flex-shrink:0"></div>'

        # Corps
        '<div style="padding:24px 22px;display:flex;flex-direction:column;flex:1;gap:12px">'

        # Type badge
        f'<span style="display:inline-block;background:{pub["color"]}18;color:{pub["color"]};'
        'border-radius:6px;padding:4px 12px;font-size:0.68rem;font-weight:700;'
        f'letter-spacing:1.5px;text-transform:uppercase;align-self:flex-start">{pub["type"]}</span>'

        # Titre
        f'<div style="font-size:0.95rem;font-weight:800;color:#f1f5f9;line-height:1.45">{pub["title"]}</div>'

        # Méta
        f'<div style="font-size:0.73rem;color:#4b6280;line-height:1.5">{pub["meta"]}</div>'

        # Abstract (tronqué)
        f'<div style="font-size:0.78rem;color:#64748b;line-height:1.6;flex:1">{pub["abstract"][:260]}…</div>'

        # Tags
        f'<div style="margin-top:auto;padding-top:10px">{tags_html}</div>'

        # Boutons
        '<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px">'
        f'<a href="{pub["url"]}" target="_blank" style="display:inline-block;'
        f'border:1px solid {pub["color"]}55;color:{pub["color"]};'
        'border-radius:7px;padding:6px 16px;font-size:0.75rem;font-weight:700;'
        f'text-decoration:none">{pub["url_label"]}</a>'
        f'<a href="{pub["github"]}" target="_blank" style="display:inline-block;'
        'border:1px solid rgba(255,255,255,0.08);color:#475569;'
        'border-radius:7px;padding:6px 16px;font-size:0.75rem;font-weight:600;'
        'text-decoration:none">GitHub ↗</a>'
        '</div>'

        '</div>'  # fin corps
        '</div>'  # fin card
    )
_pub_cards_html += '</div>'
st.markdown(_pub_cards_html, unsafe_allow_html=True)

peer_reviewed = [
    # ─ Tri par citations décroissantes ─
    ("119", "#10b981", "Optimization and standardization of the culturomics technique for human microbiome exploration",
     "A Diakite, G Dubourg, N Dione, P Afouda, S Bellali, II Ngom, C Valles, ML Tall et al.",
     "Scientific Reports 10(1):9674", "2020",
     "https://www.nature.com/articles/s41598-020-66509-3"),
    ("31", "#3b82f6", "Adenovirus infections in African humans and wild non-human primates: great diversity and cross-species transmission",
     "H Medkour, I Amona, J Akiana, B Davoust, I Bitam, A Levasseur, ML Tall et al.",
     "Viruses 12(6):657", "2020",
     "https://www.mdpi.com/1999-4915/12/6/657"),
    ("15", "#3b82f6", "Enteroviruses from humans and great apes in the Republic of Congo: recombination within enterovirus C serotypes",
     "I Amona, H Medkour, J Akiana, B Davoust, ML Tall, C Grimaldier, C Gazin et al.",
     "Microorganisms 8(11):1779", "2020",
     "https://www.mdpi.com/2076-2607/8/11/1779"),
    ("13", "#8b5cf6", "Taxonogenomics description of Bacillus dakarensis sp. nov., Bacillus sinesaloumensis sp. nov. and Bacillus massiliogabonensis sp. nov.",
     "M Sarr, CI Lo, ML Tall, A Fadlane, B Senghor, C Sokhna, D Raoult et al.",
     "New Microbes and New Infections 37:100718", "2020",
     "https://www.sciencedirect.com/science/article/pii/S2052297520300706"),
    ("10", "#10b981", "Gut microbiota influences Plasmodium falciparum malaria susceptibility",
     "A Kodio, D Coulibaly, S Doumbo, S Konaté, AK Koné, S Dama, ML Tall et al.",
     "New Microbes and New Infections 65:101586", "2025",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("10", "#8b5cf6", "Parabacteroides bouchesdurhonensis sp. nov., a new bacterium isolated from the stool of a healthy adult",
     "EK Yimagou, N Dione, II Ngom, ML Tall, JP Baudoin, D Raoult, JYB Khalil",
     "New Microbes and New Infections 34:100639", "2020",
     "https://www.sciencedirect.com/science/article/pii/S2052297520300123"),
    ("9", "#06b6d4", "Anaerococcus urinimassiliensis sp. nov., a new bacterium isolated from human urine",
     "A Morand, ML Tall, E Kuete Yimagou, II Ngom, CI Lo, F Cornu et al.",
     "Scientific Reports 11(1):2684", "2021",
     "https://www.nature.com/articles/s41598-021-82173-1"),
    ("9", "#8b5cf6", "Prevotella marseillensis sp. nov., a new bacterium isolated from a patient with recurrent Clostridium difficile infection",
     "EK Yimagou, F Mekhalif, ML Tall, JP Baudoin, D Raoult, JYB Khalil",
     "New Microbes and New Infections 32:100606", "2019",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("9", "#8b5cf6", "Noncontiguous finished genome sequence and description of Raoultibacter massiliensis gen. nov., sp. nov. and Raoultibacter timonensis sp. nov",
     "SI Traore, M Bilen, M Beye, A Diop, MDM Fonkou, ML Tall, C Michelle et al.",
     "MicrobiologyOpen 8(6):e00758", "2019",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("8", "#f59e0b", "Bartonella gabonensis sp. nov., a new bartonella species from savannah rodent Lophuromys sp. in Franceville, Gabon",
     "JB Mangombi, N N'Dilimabaka, H Medkour, OL Banga, ML Tall et al.",
     "New Microbes and New Infections 38:100796", "2020",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("7", "#ef4444", "★ Anaerococcus marasmi sp. nov., a new bacterium isolated from human gut microbiota",
     "ML Tall, TPT Pham, S Bellali, II Ngom, J Delerce, CI Lo, D Raoult et al.",
     "New Microbes and New Infections 35:100655", "2020",
     "https://www.sciencedirect.com/science/article/pii/S2052297520300391"),
    ("7", "#8b5cf6", "Clostridium transplantifaecale sp. nov., a new bacterium isolated from patient with recurrent Clostridium difficile infection",
     "EK Yimagou, ML Tall, JP Baudoin, D Raoult, JYB Khalil",
     "New Microbes and New Infections 32:100598", "2019",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("6", "#ef4444", "★ Description of Clostridium cagae sp. nov., Clostridium rectalis sp. nov. and Hathewaya massiliensis sp. nov.",
     "ML Tall, CI Lo, EK Yimagou, S Ndongo, TPT Pham, D Raoult, PE Fournier et al.",
     "New Microbes and New Infections 37:100719", "2020",
     "https://www.sciencedirect.com/science/article/pii/S2052297520300718"),
    ("6", "#ef4444", "★ Massilistercora timonensis gen. nov., sp. nov., a new bacterium isolated from the human microbiota",
     "ML Tall, S Ndongo, II Ngom, J Delerce, S Khelaifia, D Raoult, PE Fournier et al.",
     "New Microbes and New Infections 35:100664", "2020",
     "https://www.sciencedirect.com/science/article/pii/S2052297520300482"),
    ("6", "#8b5cf6", "Olsenella timonensis sp. nov., a new bacteria species isolated from the human gut microbiota",
     "S Ndongo, ML Tall, II Ngom, J Delerce, A Levasseur, D Raoult et al.",
     "New Microbes and New Infections 32:100610", "2019",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("5", "#8b5cf6", "Fenollaria timonensis sp. nov., a New Bacterium Isolated from Healthy Human Fresh Stool",
     "CI Lo, EHA Niang, M Sarr, G Durand, ML Tall, A Caputo, D Raoult et al.",
     "Current Microbiology 77(11):3780-3786", "2020",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("4", "#ef4444", "★ Massilimicrobiota timonensis gen. nov., sp. nov., a new bacterium isolated from the human gut microbiota",
     "ML Tall, S Ndongo, II Ngom, J Delerce, S Khelaifia, D Raoult, PE Fournier et al.",
     "New Microbes and New Infections 31:100574", "2019",
     "https://www.sciencedirect.com/science/article/pii/S2052297519300642"),
    ("3", "#f59e0b", "Resuscitating sleeping beauties: reviving a six-hundred-year-old amoeba and endosymbiont",
     "H Issam, ML Tall, ML Bailly, P Colson, A Levasseur, D Raoult, BL Scola et al.",
     "bioRxiv 2023.09.22.558946", "2023",
     "https://www.biorxiv.org/content/10.1101/2023.09.22.558946"),
    ("3", "#8b5cf6", "Konateibacter massiliensis gen. nov. sp. nov. and Paenibacillus faecalis sp. nov., Two New Species Isolated from the Stool Samples of Infants",
     "M Sarr, ML Tall, M Ben Khedher, TPT Pham, B Mbaye, A Camara et al.",
     "Current Microbiology 79(2):68", "2022",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("2", "#ef4444", "★ Genome sequence and description of Urinicoccus timonensis gen. nov., sp. nov.",
     "ML Tall, CI Lo, EK Yimagou, A Fontanini, J Delerce, PE Fournier, D Raoult et al.",
     "New Microbes and New Infections 37:100720", "2020",
     "https://www.sciencedirect.com/science/article/pii/S2052297520300731"),
    ("2", "#8b5cf6", "Draft genome and description of Negativicoccus massiliensis strain Marseille-P2082",
     "AH Togo, A Diop, ML Tall, M Million, S Khelaifia, M Maraninchi, D Raoult et al.",
     "Antonie van Leeuwenhoek 113(7):997-1008", "2020",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("2", "#8b5cf6", "Massilicoli timonensis sp. nov., a new bacterium isolated from the human microbiota",
     "S Ndongo, ML Tall, II Ngom, PE Fournier, A Levasseur, D Raoult et al.",
     "New Microbes and New Infections 32:100592", "2019",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("2", "#8b5cf6", "Genome sequence and description of Bacteroides bouchesdurhonensis sp. nov.",
     "S Ndongo, ML Tall, II Ngom, PE Fournier, A Levasseur, D Raoult et al.",
     "New Microbes and New Infections 31:100571", "2019",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
    ("1", "#ef4444", "★ Detection of horizontal sequence transfer in microorganisms in the genomic era",
     "ML Tall, MD Mbogning, E Kuete Yimagou, D Raoult, A Levasseur",
     "bioRxiv 2022.12.21.521446", "2022",
     "https://www.biorxiv.org/content/10.1101/2022.12.21.521446"),
    ("1", "#06b6d4", "Epidemiology and genomic characterisation of travel-associated and locally-acquired influenza, Marseille, France",
     "TL Dao, A Levasseur, ML Tall, VT Hoang, P Colson, A Caputo, TDA Ly et al.",
     "Travel Medicine and Infectious Disease 45:102236", "2022",
     "https://www.sciencedirect.com/science/article/pii/S1477893921002052"),
    ("1", "#10b981", "Spatiotemporal dynamic of the RTS, S/AS01 malaria vaccine target antigens in Senegal",
     "MA Diallo, C L'Ollivier, K Diongue, AS Badiane, A Kodio, ML Tall et al.",
     "American Journal of Tropical Medicine and Hygiene 105(6):1738", "2021",
     "https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr"),
]

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# ÉQUIPE — Fondateur + photo
# ─────────────────────────────────────────────────────────────────
st.markdown("<div id='equipe'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="section section-alt" style="text-align:center;background:#040c1c">
  <div class="section-eyebrow" style="color:#f59e0b;text-align:center">Équipe</div>
  <div class="section-h2" style="text-align:center">Le fondateur</div>
  <div style="color:#475569;font-size:0.95rem;margin:0 auto 48px;max-width:500px;line-height:1.7">
    MedFlow AI est un projet solo porté par un chercheur passionné, à l'intersection de la bioinformatique, de la médecine de précision et de l'intelligence artificielle.
  </div>
""", unsafe_allow_html=True)

col_team_photo, col_team_info = st.columns([1, 2], gap="large")

with col_team_photo:
    st.markdown(f"""
    {_photo_card_team}
    """, unsafe_allow_html=True)

with col_team_info:
    st.markdown("""
    <div class="team-card" style="text-align:left">
      <div style="display:inline-block;background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.25);
           color:#f59e0b;border-radius:8px;padding:4px 14px;font-size:0.75rem;font-weight:700;
           letter-spacing:2px;text-transform:uppercase;margin-bottom:20px">
        Fondateur &amp; Développeur principal
      </div>
      <div class="team-name">Dr. Mamadou Lamine TALL</div>
      <div class="team-role">PhD Bioinformatique · Aix-Marseille Université · Montpellier, France</div>
      <div class="team-bio">
        Chercheur spécialisé en <strong style="color:#f1f5f9">bioinformatique médicale</strong>,
        <strong style="color:#f1f5f9">analyse multi-omique</strong> et
        <strong style="color:#f1f5f9">intelligence artificielle appliquée à la médecine</strong>.
        <br><br>
        <strong style="color:#f59e0b">Thèse de doctorat (2020)</strong> —
        <em>Études bioinformatiques et biostatistiques des structures mosaïques des génomes microbiens</em>,
        Aix-Marseille Université, sous la direction du Pr. Anthony Levasseur.
        Travaux portant sur le mosaïcisme génomique, la taxonogénomique et la phylogénomique comparative.
        <br><br>
        Fondateur de <strong style="color:#f1f5f9">MedFlow AI</strong> — plateforme open source d'aide
        à la décision clinique entièrement en français. Auteur de 5 preprints soumis (2026),
        développeur de 9 outils déployés sur Streamlit Cloud, et porteur de projets de recherche
        translationelle en cardiologie, génomique musculaire et onco-microbiome.
        <br><br>
        <strong style="color:#f1f5f9">Domaines d'expertise :</strong>
        génomique comparative · transcriptomique (bulk + single-cell) ·
        variabilité de la fréquence cardiaque · méta-analyses PRISMA ·
        Machine Learning clinique · biomarqueurs diagnostiques.
      </div>
      <div class="team-links">
        <a href="https://github.com/mamadoulaminetall" target="_blank" class="team-link">GitHub ↗</a>
        <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank" class="team-link">Google Scholar ↗</a>
        <a href="https://theses.fr/2020AIXM0426" target="_blank" class="team-link">Thèse 2020 ↗</a>
        <a href="https://www.linkedin.com/in/medflow-ia-350531401/" target="_blank" class="team-link">LinkedIn ↗</a>
        <a href="mailto:mamadoulaminetallgithub@gmail.com" class="team-link">Email ↗</a>
      </div>
      <div style="margin-top:24px;padding-top:24px;border-top:1px solid rgba(255,255,255,0.06)">
        <div style="display:flex;gap:32px;flex-wrap:wrap">
          <div>
            <div style="font-size:1.6rem;font-weight:900;color:#10b981">7</div>
            <div style="font-size:0.78rem;color:#475569">Outils déployés</div>
          </div>
          <div>
            <div style="font-size:1.6rem;font-weight:900;color:#3b82f6">6</div>
            <div style="font-size:0.78rem;color:#475569">Publications / Preprints</div>
          </div>
          <div>
            <div style="font-size:1.6rem;font-weight:900;color:#8b5cf6">11</div>
            <div style="font-size:0.78rem;color:#475569">Repos GitHub</div>
          </div>
          <div>
            <div style="font-size:1.6rem;font-weight:900;color:#f59e0b">5 800+</div>
            <div style="font-size:0.78rem;color:#475569">Échantillons analysés</div>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# PUBLICATIONS PEER-REVIEWED (après Fondateur)
# ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section" style="background:#030810">
  <div class="section-eyebrow" style="color:#3b82f6">IHU M&eacute;diterran&eacute;e Infection &middot; Aix-Marseille</div>
  <div class="section-h2">Publications Peer-Reviewed</div>
  <div style="display:flex;align-items:center;gap:16px;margin-bottom:32px;flex-wrap:wrap">
    <span style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.25);
          color:#60a5fa;border-radius:8px;padding:5px 16px;font-size:0.75rem;font-weight:700;
          letter-spacing:2px;text-transform:uppercase">
      📄 29+ publications index&eacute;es · G&eacute;nomique &middot; M&eacute;tagenomique &middot; Microbiome
    </span>
    <span style="color:#475569;font-size:0.82rem">Google Scholar · ID : qJaCV7MAAAAJ</span>
  </div>
""", unsafe_allow_html=True)

# Grille 2 colonnes
_pr_grid = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px">'
for cit, color, title, authors, journal, year, url in peer_reviewed:
    first_auth = "★ " in title
    clean_title = title.replace("★ ", "")
    fa_badge = ('<span style="background:rgba(239,68,68,0.12);color:#f87171;border-radius:4px;'
                'padding:1px 8px;font-size:0.68rem;font-weight:700;margin-right:6px">1er auteur</span>'
                if first_auth else "")
    _pr_grid += (
        f'<div style="background:#080f1e;border:1px solid rgba(255,255,255,0.05);'
        f'border-left:3px solid {color};border-radius:10px;padding:16px 18px">'
        '<div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px">'
        f'<div style="flex:1">{fa_badge}'
        f'<span style="font-size:0.88rem;font-weight:700;color:#e2e8f0;line-height:1.4">{clean_title}</span>'
        '</div>'
        f'<span style="background:{color}22;color:{color};border-radius:6px;'
        'padding:3px 10px;font-size:0.75rem;font-weight:800;margin-left:12px;white-space:nowrap">'
        f'{cit} cit.</span>'
        '</div>'
        f'<div style="font-size:0.75rem;color:#475569;margin-bottom:4px">{authors}</div>'
        '<div style="display:flex;justify-content:space-between;align-items:center">'
        f'<span style="font-size:0.75rem;color:#475569;font-style:italic">{journal} · {year}</span>'
        f'<a href="{url}" target="_blank" style="color:{color};font-size:0.72rem;'
        f'font-weight:600;white-space:nowrap;margin-left:8px">Voir →</a>'
        '</div>'
        '</div>'
    )
_pr_grid += '</div>'
st.markdown(_pr_grid, unsafe_allow_html=True)

# Stats globales
_total_cit = sum(int(c) for c, *_ in peer_reviewed)
st.markdown(f"""
<div style="margin-top:24px;background:#0d1829;border-radius:12px;padding:20px 28px;
     border:1px solid rgba(255,255,255,0.06);display:flex;gap:40px;flex-wrap:wrap;align-items:center">
  <div>
    <span style="font-size:1.8rem;font-weight:900;color:#3b82f6">{len(peer_reviewed) + 5}</span>
    <span style="color:#475569;font-size:0.82rem;margin-left:8px">Publications totales</span>
  </div>
  <div>
    <span style="font-size:1.8rem;font-weight:900;color:#10b981">{_total_cit}+</span>
    <span style="color:#475569;font-size:0.82rem;margin-left:8px">Citations totales</span>
  </div>
  <div>
    <span style="font-size:1.8rem;font-weight:900;color:#8b5cf6">8</span>
    <span style="color:#475569;font-size:0.82rem;margin-left:8px">Publications 1er auteur</span>
  </div>
  <div>
    <span style="font-size:1.8rem;font-weight:900;color:#f59e0b">2019–2026</span>
    <span style="color:#475569;font-size:0.82rem;margin-left:8px">P&eacute;riode d'activit&eacute;</span>
  </div>
  <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank"
     style="background:#1e3a5f;color:#60a5fa;padding:10px 22px;border-radius:8px;
     font-weight:700;font-size:0.85rem;margin-left:auto">
     Voir sur Google Scholar ↗
  </a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# CONTACT
# ─────────────────────────────────────────────────────────────────
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="section" style="background:#030c18">
  <div class="section-eyebrow" style="color:#06b6d4">Contact · Collaboration</div>
  <div class="section-h2">Nous contacter</div>
  <div class="section-lead" style="margin-bottom:48px">
    Collaboration de recherche, déploiement hospitalier, développement sur mesure,
    ou simplement pour en savoir plus sur MedFlow AI.
  </div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""
    <div class="contact-box">
      <div class="contact-icon" style="background:rgba(6,182,212,0.12)">📧</div>
      <div>
        <div class="contact-label">Email GitHub / Dev</div>
        <div class="contact-value">
          <a href="mailto:mamadoulaminetallgithub@gmail.com"
             style="color:#f1f5f9;font-size:0.85rem">
            mamadoulaminetallgithub@gmail.com
          </a>
        </div>
        <div class="contact-sub">Projets open source · GitHub</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="contact-box">
      <div class="contact-icon" style="background:rgba(16,185,129,0.12)">✉️</div>
      <div>
        <div class="contact-label">Email Personnel / Recherche</div>
        <div class="contact-value">
          <a href="mailto:laminetall30@gmail.com"
             style="color:#f1f5f9;font-size:0.85rem">
            laminetall30@gmail.com
          </a>
        </div>
        <div class="contact-sub">Collaboration · Recherche · Clinique</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="contact-box">
      <div class="contact-icon" style="background:rgba(245,158,11,0.12)">📍</div>
      <div>
        <div class="contact-label">Localisation</div>
        <div class="contact-value">Montpellier, France</div>
        <div class="contact-sub">Occitanie · Disponible en présentiel &amp; distanciel</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

c4, c5, c6 = st.columns(3, gap="medium")
with c4:
    st.markdown("""
    <div class="contact-box">
      <div class="contact-icon" style="background:rgba(59,130,246,0.12)">💼</div>
      <div>
        <div class="contact-label">LinkedIn</div>
        <div class="contact-value">
          <a href="https://www.linkedin.com/in/medflow-ia-350531401/" target="_blank"
             style="color:#60a5fa;font-size:0.85rem">MedFlow IA ↗</a>
        </div>
        <div class="contact-sub">Actualités · Projets · Réseau pro</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="contact-box">
      <div class="contact-icon" style="background:rgba(255,255,255,0.05)">🐙</div>
      <div>
        <div class="contact-label">GitHub</div>
        <div class="contact-value">
          <a href="https://github.com/mamadoulaminetall" target="_blank"
             style="color:#94a3b8;font-size:0.85rem">mamadoulaminetall ↗</a>
        </div>
        <div class="contact-sub">11 repositories publics</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="contact-box">
      <div class="contact-icon" style="background:rgba(139,92,246,0.12)">🎓</div>
      <div>
        <div class="contact-label">Google Scholar</div>
        <div class="contact-value">
          <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank"
             style="color:#a78bfa;font-size:0.85rem">Mamadou Lamine TALL ↗</a>
        </div>
        <div class="contact-sub">Publications · Citations · Preprints</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='block-sep'></div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# MENTIONS LÉGALES
# ─────────────────────────────────────────────────────────────────
st.markdown("<div id='legal'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="legal-section">
  <div style="text-align:center;margin-bottom:48px">
    <div style="font-size:0.75rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;
                color:#475569;margin-bottom:12px">Informations légales</div>
    <div style="font-size:1.8rem;font-weight:800;color:#64748b">Mentions légales</div>
  </div>
""", unsafe_allow_html=True)

leg1, leg2, leg3 = st.columns(3, gap="medium")

with leg1:
    st.markdown("""
    <div class="legal-card">
      <div class="legal-title">🏢 Éditeur du site</div>
      <div class="legal-text">
        <strong style="color:#64748b">MedFlow AI</strong><br>
        Projet indépendant de recherche et développement<br><br>
        <strong style="color:#64748b">Responsable de publication :</strong><br>
        Dr. Mamadou Lamine TALL<br>
        PhD Bioinformatique<br><br>
        <strong style="color:#64748b">Localisation :</strong><br>
        Montpellier, Occitanie, France<br><br>
        <strong style="color:#64748b">Contact :</strong><br>
        mamadoulaminetallgithub@gmail.com<br>
        laminetall30@gmail.com
      </div>
    </div>
    """, unsafe_allow_html=True)

with leg2:
    st.markdown("""
    <div class="legal-card">
      <div class="legal-title">⚕️ Avertissement médical</div>
      <div class="legal-text">
        Les outils proposés par MedFlow AI sont des <strong style="color:#64748b">aides à la décision clinique</strong>
        et ne constituent en aucun cas un avis médical, un diagnostic ou une prescription médicale.<br><br>
        Ces outils sont destinés exclusivement aux <strong style="color:#64748b">professionnels de santé qualifiés</strong>
        et ne remplacent pas le jugement clinique du médecin.<br><br>
        Les résultats fournis doivent être interprétés par un professionnel de santé
        dans le contexte clinique global du patient.<br><br>
        MedFlow AI décline toute responsabilité en cas d'utilisation
        en dehors du cadre médical professionnel.
      </div>
    </div>
    """, unsafe_allow_html=True)

with leg3:
    st.markdown("""
    <div class="legal-card">
      <div class="legal-title">🔒 Données & Hébergement</div>
      <div class="legal-text">
        <strong style="color:#64748b">Hébergement :</strong><br>
        Streamlit Cloud (Snowflake Inc.)<br>
        650 Castro St, Mountain View, CA, USA<br><br>
        <strong style="color:#64748b">Données personnelles :</strong><br>
        Aucune donnée personnelle ou médicale n'est stockée ou transmise
        par les outils MedFlow AI. Les calculs sont effectués localement
        dans votre navigateur.<br><br>
        <strong style="color:#64748b">Propriété intellectuelle :</strong><br>
        Le code source est publié sous licence MIT (open source).
        Le contenu et les marques MedFlow AI sont la propriété de Dr. M.L. TALL.<br><br>
        <strong style="color:#64748b">Paiements :</strong><br>
        Traitement sécurisé via Stripe. Aucune donnée bancaire stockée.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  <div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
      {LOGO_IMG}
      <div class="footer-brand">MedFlow <span>AI</span></div>
    </div>
    <div class="footer-copy">© 2026 Dr. Mamadou Lamine TALL · PhD Bioinformatique · Montpellier, France</div>
    <div style="display:flex;gap:16px;margin-top:10px">
      <a href="https://github.com/mamadoulaminetall" target="_blank"
         style="color:#4b5e78;font-size:0.75rem;transition:color 0.2s">GitHub ↗</a>
      <a href="https://scholar.google.com/citations?user=qJaCV7MAAAAJ&hl=fr" target="_blank"
         style="color:#4b5e78;font-size:0.75rem;transition:color 0.2s">Scholar ↗</a>
      <a href="https://www.linkedin.com/in/medflow-ia-350531401/" target="_blank"
         style="color:#4b5e78;font-size:0.75rem;transition:color 0.2s">LinkedIn ↗</a>
    </div>
  </div>
  <div>
    <div style="font-size:0.7rem;color:#4b5e78;text-transform:uppercase;letter-spacing:2px;
         font-weight:700;margin-bottom:12px">Outils</div>
    <div class="footer-links">
      <a href="https://cardiac-qol-ai.streamlit.app">QoL Cardiac</a>
      <a href="https://clinia-scores.streamlit.app">Scores Cliniques</a>
      <a href="https://clinia-cr.streamlit.app">Générateur CR</a>
    </div>
    <div class="footer-links" style="margin-top:8px">
      <a href="https://reinnervationaiapp.streamlit.app">Réinnervation IA</a>
      <a href="https://myoomics.streamlit.app">MYOomics</a>
      <a href="https://buy.stripe.com/9B63cvb3G8kZ5cGfHwb3q01" target="_blank"
         style="color:#10b981;font-size:0.78rem;font-weight:700">Accès complet ↗</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
