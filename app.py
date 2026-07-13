import streamlit as st
import base64
import io
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Peridot Apartment | Welcome",
    page_icon=Image.new("RGBA", (1, 1), (0, 0, 0, 0)),
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, header, footer { visibility: hidden !important; display: none !important; }
[data-testid="stFooter"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }
.viewerBadge_container__r5tak { display: none !important; }
.viewerBadge_link__qRIco { display: none !important; }
.stDeployButton { display: none !important; }
div[class*="viewerBadge"] { display: none !important; }
div[class*="streamlit-footer"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

ASSETS = Path(__file__).parent / "assets"
ROOT = Path(__file__).parent


def b64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def b64_video(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def b64_compressed(path: Path, max_w: int = 800, quality: int = 78) -> str:
    img = Image.open(path).convert("RGB")
    if img.width > max_w:
        h = int(img.height * max_w / img.width)
        img = img.resize((max_w, h), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality, optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def img_tag(path: Path, alt: str = "", style: str = "") -> str:
    ext = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png"}.get(ext, "png")
    return f'<img src="data:image/{mime};base64,{b64(path)}" alt="{alt}" style="{style}">'


def img_tag_sm(path: Path, alt: str = "", style: str = "", max_w: int = 800, quality: int = 78) -> str:
    return f'<img src="data:image/jpeg;base64,{b64_compressed(path, max_w=max_w, quality=quality)}" alt="{alt}" style="{style}">'


# ── Load assets ──────────────────────────────────────────────────────────────
logo       = ASSETS / "cropped-F5A33662-9B21-4B86-BD7E-F1D7F4CC3726.png"
building   = ASSETS / "Vila Mojca 2.png"
key_safe   = ASSETS / "key safe.png"
garage_img = ASSETS / "garage.png"
terrace    = ASSETS / "Terasa.jpg"
checkout   = ASSETS / "checkout.png"
here4u     = ASSETS / "here for you.png"
bicycle    = ASSETS / "bycicle storage .png"
garage_plan= ASSETS / "Garage Layout.png"
key_box_loc= ASSETS / "Location key box.png"
id_photo   = ASSETS / "ID.png"
enjoy      = ASSETS / "Enjoy.png"
wishing_you= ASSETS / "Thank you.png"
evac_plan  = ASSETS / "Evacuation .png"
blinds_img = ASSETS / "blinds.png"
air_recup_img = ASSETS / "Air Recuperation.png"

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Streamlit resets ── */
#MainMenu { display: none !important; }
header { display: none !important; }
footer { display: none !important; visibility: hidden !important; height: 0 !important; }
footer * { display: none !important; }
[data-testid="stFooter"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
.viewerBadge_container__r5tak { display: none !important; }
.stDeployButton { display: none !important; }
.st-emotion-cache-15ecox0 { display: none !important; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
[data-testid="stAppViewContainer"] { background: #ffffff; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* ── Global ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --green:  #148A46;
    --dark:   #222222;
    --muted:  #666666;
    --light:  #F1F8F4;
    --border: #DCEBE2;
    --white:  #FFFFFF;
}

body { font-family: 'Inter', sans-serif; color: var(--dark); }
html { scroll-padding-top: 80px; }

/* ── NAV ── */
.pa-nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 9999;
    background: rgba(255,255,255,0.97);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 64px;
    height: 72px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.06);
}
.pa-nav img { height: 46px; object-fit: contain; }
.pa-nav-links { display: flex; gap: 40px; align-items: center; }
.pa-nav-links a {
    text-decoration: none;
    font-family: 'Inter', sans-serif;
    font-size: 12.5px;
    font-weight: 600;
    color: var(--dark);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding-bottom: 3px;
    border-bottom: 2px solid transparent;
    transition: color .2s, border-color .2s;
}
.pa-nav-links a:hover { color: var(--green); border-bottom-color: var(--green); }
.pa-nav-links a.active { color: var(--green); border-bottom-color: var(--green); }

/* ── NAV SPACER ── */
.nav-spacer { height: 72px; }

/* ── HERO ── */
.pa-hero {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: calc(100vh - 72px);
    align-items: center;
    padding: 72px 80px 60px 80px;
    gap: 56px;
    background: #fff;
}
.pa-hero-left { display: flex; flex-direction: column; gap: 22px; }
.hero-eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--green);
}
.hero-dear {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 400;
    color: var(--muted);
    font-style: italic;
    line-height: 1.3;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(38px, 4.2vw, 62px);
    font-weight: 700;
    color: var(--dark);
    line-height: 1.12;
}
.hero-title span { color: var(--green); }
.hero-text {
    font-family: 'Inter', sans-serif;
    font-size: 15.5px;
    color: var(--muted);
    line-height: 1.75;
    max-width: 460px;
}
.hero-btns { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 6px; }
.btn-primary {
    display: inline-block;
    background: var(--green);
    color: #fff !important;
    padding: 14px 30px;
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-decoration: none !important;
    transition: background .2s, transform .15s;
}
.btn-primary:hover { background: #0f6e38; color:#fff !important; transform: translateY(-1px); }
.btn-outline {
    display: inline-block;
    background: transparent;
    color: var(--dark) !important;
    border: 2px solid var(--dark);
    padding: 12px 30px;
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    text-decoration: none !important;
    transition: background .2s, color .2s, border-color .2s;
}
.btn-outline:hover { background: var(--light); color: var(--dark) !important; }
.hero-addr {
    font-family: 'Inter', sans-serif;
    font-size: 19px;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
}
.hero-addr svg { color: var(--green); flex-shrink: 0; }
.hero-addr a {
    color: var(--green);
    font-weight: 600;
    font-size: 14.5px;
    text-decoration: underline;
    text-underline-offset: 3px;
}
.pa-hero-right {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 8px 48px rgba(0,0,0,0.14);
    max-height: 580px;
}
.pa-hero-right img {
    width: 100%;
    height: 580px;
    object-fit: cover;
    display: block;
}
.hero-img-overlay {
    position: absolute;
    inset: 0 auto 0 0;
    width: 38%;
    background: linear-gradient(to right, rgba(255,255,255,0.55), transparent);
    pointer-events: none;
}

/* ── INFO STRIP ── */
.pa-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    background: var(--light);
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
}
.strip-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 38px 28px;
    text-align: center;
    gap: 14px;
    border-right: 1px solid var(--border);
}
.strip-card:last-child { border-right: none; }
.strip-icon svg { display: block; }
.strip-title {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--dark);
}
.strip-desc {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    color: var(--muted);
    line-height: 1.55;
}

/* ── SECTION ── */
.pa-section {
    padding: 88px 80px;
    background: #fff;
}
.pa-section-alt { background: var(--light); }
.section-tag {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 10px;
}
.section-h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(28px, 3vw, 42px);
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 10px;
    line-height: 1.2;
}
.section-sub {
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 52px;
    max-width: 540px;
}
.section-divider {
    width: 52px; height: 3px;
    background: var(--green);
    border-radius: 2px;
    margin-bottom: 20px;
}

/* ── CHECK-IN GRID ── */
.checkin-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: start;
}

/* ── TIMELINE ── */
.timeline { display: flex; flex-direction: column; }
.tl-item { display: flex; gap: 20px; }
.tl-spine { display: flex; flex-direction: column; align-items: center; flex-shrink: 0; }
.tl-circle {
    width: 42px; height: 42px;
    border-radius: 50%;
    background: var(--green);
    color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 15px;
    flex-shrink: 0;
    box-shadow: 0 2px 12px rgba(20,138,70,0.3);
}
.tl-line {
    width: 2px;
    flex: 1;
    min-height: 28px;
    background: var(--border);
    margin: 6px 0;
}
.tl-body { padding-bottom: 36px; flex: 1; padding-top: 8px; }
.tl-step {
    font-family: 'Inter', sans-serif;
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 3px;
}
.tl-title {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    font-weight: 600;
    color: var(--dark);
    margin-bottom: 6px;
}
.tl-desc {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    color: var(--muted);
    line-height: 1.65;
}
.tl-item:last-child .tl-line { display: none; }

/* ── PHOTO GRID ── */
.photo-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    align-content: start;
}
.photo-card {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--border);
    box-shadow: 0 2px 16px rgba(0,0,0,0.06);
    background: #fff;
}
.photo-card img {
    width: 100%;
    height: 190px;
    object-fit: cover;
    display: block;
}
.photo-cap {
    padding: 10px 14px 12px;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    font-weight: 500;
    color: var(--muted);
    text-align: center;
    letter-spacing: 0.04em;
}

/* ── GARAGE PLAN CARD ── */
.garage-plan-wrap {
    padding: 0 80px 64px 80px;
}
.garage-plan-card {
    border: 2px solid var(--green);
    border-radius: 18px;
    overflow: hidden;
    background: #fff;
    display: grid;
    grid-template-columns: 1fr 1fr;
    box-shadow: 0 6px 32px rgba(20,138,70,0.12);
}
.garage-plan-text {
    padding: 44px 52px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 16px;
}
.garage-plan-text h3 {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-weight: 700;
    color: var(--dark);
    line-height: 1.25;
}
.garage-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--light);
    border: 1px solid var(--border);
    border-radius: 40px;
    padding: 8px 18px;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 600;
    color: var(--green);
    width: fit-content;
}
.garage-plan-text p {
    font-family: 'Inter', sans-serif;
    font-size: 14.5px;
    color: var(--muted);
    line-height: 1.65;
}
.garage-plan-img img {
    width: 100%;
    height: 320px;
    object-fit: cover;
    display: block;
}

/* ── CHECKIN HEADER (2-col: title + important notice) ── */
.checkin-header {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 56px;
    align-items: center;
    margin-bottom: 52px;
}

/* ── IMPORTANT NOTICE — filled green ── */
.important-notice {
    background: var(--green);
    border-radius: 16px;
    padding: 28px 30px;
}
.important-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255,255,255,0.18);
    color: #fff;
    font-family: 'Inter', sans-serif;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 14px;
}
.important-notice h4 {
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: #fff;
    margin-bottom: 10px;
}
.important-notice p {
    font-family: 'Inter', sans-serif;
    font-size: 13.5px;
    color: rgba(255,255,255,0.88);
    line-height: 1.7;
    margin: 0;
    text-align: justify;
}

/* ── INFO BLOCK ── */
.info-block {
    margin: 0 80px 56px 80px;
    background: var(--light);
    border: 1px solid var(--border);
    border-left: 4px solid var(--green);
    border-radius: 14px;
    padding: 36px 44px;
    display: flex;
    gap: 20px;
    align-items: flex-start;
}
.info-block-icon svg { flex-shrink: 0; margin-top: 3px; }
.info-block-body h4 {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 8px;
}
.info-block-body p {
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    color: #444;
    line-height: 1.7;
}

/* ── CONTACT CARD ── */
.contact-section {
    padding: 0 80px 64px 80px;
}
.contact-card {
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 48px 52px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 48px;
    align-items: center;
    box-shadow: 0 4px 28px rgba(0,0,0,0.07);
}
.contact-left h3 {
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 24px;
}
.contact-line {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 14px;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    color: #444;
}
.contact-line svg { color: var(--green); flex-shrink: 0; }
.contact-line a { color: var(--green); text-decoration: none; font-weight: 500; }
.contact-line a:hover { text-decoration: underline; }
.contact-sig {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    text-align: center;
}
.contact-sig img { max-height: 200px; max-width: 280px; object-fit: contain; }
.sig-caption {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    font-style: italic;
    color: var(--muted);
}

/* ── CHECKOUT ── */
.checkout-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: start;
}
.checkout-img {
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 6px 32px rgba(0,0,0,0.12);
    position: sticky;
    top: 90px;
}
.checkout-img img { width: 100%; height: 420px; object-fit: cover; display: block; }
.checkout-intro {
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    font-style: italic;
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 32px;
}
.checklist { display: flex; flex-direction: column; gap: 14px; margin-bottom: 32px; }
.cl-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    color: var(--dark);
    line-height: 1.55;
    padding: 16px 20px;
    background: var(--light);
    border-radius: 10px;
    border: 1px solid var(--border);
}
.cl-item svg { color: var(--green); flex-shrink: 0; margin-top: 2px; }
.direct-note {
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 28px;
    font-family: 'Inter', sans-serif;
    font-size: 14.5px;
    color: var(--muted);
    line-height: 1.7;
    font-style: italic;
    margin-bottom: 24px;
}
.direct-note strong { color: var(--dark); font-style: normal; }

/* ── VIDEO ── */
.video-section {
    background: #fff;
    padding: 8px 0 56px;
}
[data-testid="stVideo"] {
    width: 40%;
    margin: 0 auto;
    display: block;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(0,0,0,0.1);
}
[data-testid="stVideo"] video { width: 100%; display: block; border-radius: 14px; }

/* ── FOOTER ── */
.pa-footer {
    background: var(--green);
    color: #fff;
    padding: 56px 80px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 40px;
    align-items: center;
}
.footer-left p {
    font-family: 'Inter', sans-serif;
    font-size: 16px;
    margin-bottom: 10px;
    opacity: 0.92;
    line-height: 1.6;
}
.footer-left a { color: #fff; text-decoration: underline; opacity: 0.85; }
.footer-logo { display: flex; align-items: center; }
.footer-logo img {
    height: 52px;
    object-fit: contain;
    filter: brightness(0) invert(1);
    opacity: 0.88;
}
.footer-copy {
    grid-column: 1 / -1;
    border-top: 1px solid rgba(255,255,255,0.2);
    padding-top: 20px;
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    color: rgba(255,255,255,0.55);
    text-align: center;
}

/* ── TABLET (≤900px) ── */
@media (max-width: 900px) {
    .pa-nav { padding: 0 28px; height: 64px; }
    .pa-nav img { height: 40px; }
    .nav-spacer { height: 64px; }
    .pa-nav-links { gap: 20px; }
    .pa-nav-links a { font-size: 11px; }
    .pa-hero { grid-template-columns: 1fr; padding: 44px 28px 52px; gap: 28px; min-height: auto; }
    .pa-hero-right { max-height: 300px; border-radius: 16px; }
    .pa-hero-right img { height: 300px; }
    .pa-strip { grid-template-columns: repeat(2, 1fr); }
    .strip-card { padding: 28px 18px; border-bottom: 1px solid var(--border); }
    .strip-card:nth-child(2) { border-right: none; }
    .strip-card:nth-child(3) { border-bottom: none; }
    .strip-card:nth-child(4) { border-right: none; border-bottom: none; }
    .pa-section { padding: 60px 28px; }
    .checkin-header { grid-template-columns: 1fr; gap: 24px; margin-bottom: 36px; }
    .checkin-grid { grid-template-columns: 1fr; gap: 44px; }
    .photo-grid { grid-template-columns: repeat(2, 1fr); }
    .garage-plan-wrap { padding: 0 28px 56px; }
    .garage-plan-card { grid-template-columns: 1fr; }
    .garage-plan-img { order: -1; }
    .garage-plan-img img { height: 240px; }
    .garage-plan-text { padding: 32px 28px; }
    .info-block { margin: 0 28px 52px; padding: 28px 28px; }
    .contact-section { padding: 0 28px 52px; }
    .contact-card { grid-template-columns: 1fr; gap: 28px; padding: 36px 28px; }
    .contact-sig { align-items: flex-start; text-align: left; }
    .checkout-grid { grid-template-columns: 1fr; gap: 40px; }
    .checkout-img { position: static; }
    .checkout-img img { height: 280px; }
    .pa-footer { grid-template-columns: 1fr; padding: 44px 28px; gap: 24px; }
}

/* ── PHONE (≤600px) ── */
@media (max-width: 600px) {
    .pa-nav { padding: 0 16px; height: 56px; }
    .pa-nav img { height: 34px; }
    .nav-spacer { height: 56px; }
    .pa-nav-links {
        gap: 14px;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
        flex-shrink: 1;
        min-width: 0;
    }
    .pa-nav-links::-webkit-scrollbar { display: none; }
    .pa-nav-links a { font-size: 10px; letter-spacing: 0.07em; white-space: nowrap; }
    .pa-hero { padding: 28px 16px 40px; gap: 22px; }
    .hero-dear { font-size: 17px; }
    .hero-title { font-size: clamp(28px, 8.5vw, 38px); }
    .hero-text { font-size: 14px; line-height: 1.65; }
    .hero-btns { flex-direction: column; gap: 10px; }
    .btn-primary, .btn-outline { text-align: center; padding: 13px 20px; width: 100%; }
    .hero-addr { font-size: 14px; justify-content: center; text-align: center; }
    .pa-hero-right { max-height: 220px; border-radius: 12px; }
    .pa-hero-right img { height: 220px; }
    .pa-strip { grid-template-columns: repeat(2, 1fr); }
    .strip-card { padding: 22px 12px; gap: 10px; }
    .strip-icon svg { width: 28px; height: 28px; }
    .strip-title { font-size: 11px; }
    .strip-desc { font-size: 12px; }
    .pa-section { padding: 48px 16px; }
    .section-h2 { font-size: clamp(22px, 6.5vw, 32px); }
    .section-sub { font-size: 14px; margin-bottom: 36px; }
    .checkin-header { gap: 18px; margin-bottom: 28px; }
    .important-notice { padding: 20px 18px; }
    .important-notice > div[style*="flex"] { flex-direction: column; gap: 14px; }
    .important-notice > div[style*="flex"] > div:last-child img { width: 100% !important; height: 140px !important; object-fit: cover; border-radius: 10px; }
    .tl-circle { width: 36px; height: 36px; font-size: 13px; }
    .tl-title { font-size: 15px; }
    .tl-desc { font-size: 13px; }
    .tl-body { padding-bottom: 28px; }
    .photo-grid { grid-template-columns: 1fr; }
    .photo-card img { height: 200px; }
    .garage-plan-wrap { padding: 0 16px 40px; }
    .garage-plan-text { padding: 24px 18px; }
    .garage-plan-text h3 { font-size: 20px; }
    .garage-plan-text p { font-size: 13.5px; text-align: justify; }
    .garage-plan-img img { height: 200px; }
    .legend-label { font-size: 12px !important; }
    .info-block { margin: 0 16px 40px; padding: 20px 18px; flex-direction: column; gap: 12px; }
    .info-block-body p { font-size: 14px; }
    .contact-section { padding: 0 16px 40px; }
    .contact-card { padding: 24px 18px; }
    .contact-left h3 { font-size: 22px; margin-bottom: 18px; }
    .contact-line { font-size: 14px; gap: 10px; }
    .contact-sig img { max-height: 160px; }
    .checkout-img img { height: 200px; }
    .checkout-intro { font-size: 16px; margin-bottom: 24px; }
    .cl-item { font-size: 14px; padding: 14px 16px; gap: 12px; }
    .direct-note { font-size: 13.5px; padding: 18px 18px; }
    .pa-footer { padding: 36px 16px; gap: 20px; }
    .footer-left p { font-size: 14px; }
    .footer-logo img { height: 40px; }
}

/* ── SMALL PHONE (≤380px) ── */
@media (max-width: 380px) {
    .pa-strip { grid-template-columns: 1fr; }
    .strip-card { border-right: none; border-bottom: 1px solid var(--border); }
    .strip-card:last-child { border-bottom: none; }
    .pa-nav-links a { font-size: 9px; letter-spacing: 0.04em; }
    .pa-nav-links { gap: 10px; }
}
</style>
""", unsafe_allow_html=True)

# ── ROUTING ───────────────────────────────────────────────────────────────────
page = st.query_params.get("page", "home")

# ── NAVIGATION ────────────────────────────────────────────────────────────────
_active_home = "active" if page == "home" else ""
_active_evac = "active" if page == "evacuation" else ""
# Only force a reload back to the home page when we're not already on it —
# otherwise these stay plain in-page anchors so scrolling works instantly.
_home_prefix = "" if page == "home" else "?page=home"
st.markdown(f"""
<nav class="pa-nav">
  <a href="{_home_prefix}#welcome">{img_tag(logo, "Peridot Apartment", "height:46px;object-fit:contain;")}</a>
  <div class="pa-nav-links">
    <a href="{_home_prefix}#welcome" class="{_active_home}">Welcome</a>
    <a href="{_home_prefix}#checkin">Check-in</a>
    <a href="{_home_prefix}#checkout">Check-out</a>
    <a href="{_home_prefix}#temperature">Temperature</a>
    <a href="{_home_prefix}#contact">Contact</a>
    <a href="?page=evacuation" target="_self" class="{_active_evac}">Evacuation Plan</a>
  </div>
</nav>
<div class="nav-spacer"></div>
""", unsafe_allow_html=True)

# ── SHARED FOOTER (routed pages) ──────────────────────────────────────────────
def _render_routed_footer():
    st.markdown(
    f'<div class="pa-footer">'
    f'<div class="footer-left">'
    f'<p><strong>Need anything during your stay?</strong></p>'
    f'<p>Contact Saša anytime — we\'re always happy to help.</p>'
    f'<p><a href="tel:+38631676315">+386 31 676 315</a> &nbsp;·&nbsp; <a href="mailto:sasa.podpeskar@gmail.com">sasa.podpeskar@gmail.com</a></p>'
    f'</div>'
    f'<div class="footer-logo">'
    f'{img_tag(logo, "Peridot Apartment", "height:52px;object-fit:contain;filter:brightness(0) invert(1);opacity:0.88;")}'
    f'</div>'
    f'<div class="footer-copy">© Peridot Apartment · Villa Mojca · Borovška cesta 99b, 4280 Kranjska Gora</div>'
    f'</div>',
    unsafe_allow_html=True)

# ── EVACUATION PLAN PAGE ──────────────────────────────────────────────────────
if page == "evacuation":
    evac_pdf_path = ASSETS / "Evacuation plan.pdf"
    evac_pdf_href = f"data:application/pdf;base64,{b64(evac_pdf_path)}"

    _numbers = [
        ("Emergency", "112"),
        ("Police", "113"),
        ("Road emergency", "1987"),
        ("Owners", "+386 31 676 315 or +386 40 414 141"),
    ]

    def _number_row(label, value, is_last=False):
        tel_links = " or ".join(
            f'<a href="tel:{n.replace(" ", "")}" style="color:var(--green);text-decoration:none;">{n}</a>'
            for n in value.split(" or ")
        )
        border = "" if is_last else "border-bottom:1px solid var(--border);"
        return (
            f'<div style="display:flex;align-items:center;justify-content:space-between;'
            f'padding:18px 0;{border}">'
            f'<span style="font-family:Inter,sans-serif;font-size:15px;font-weight:600;color:var(--dark);">{label}</span>'
            f'<span style="font-family:Inter,sans-serif;font-size:15px;font-weight:700;color:var(--green);">{tel_links}</span>'
            f'</div>'
        )

    st.markdown(f"""
    <section class="pa-section" style="padding-bottom:0;">
      <div class="section-tag">Safety information</div>
      <div class="section-divider"></div>
      <div class="section-h2">Evacuation Plan</div>
    </section>
    <div class="garage-plan-wrap">
      <div class="garage-plan-card">
        <div class="garage-plan-text">
          <div class="section-tag">Evacuation Plan</div>
          <h3>Evacuation Plan</h3>
          <p>The image shows the evacuation routes for the apartment floor. Green markings indicate the escape paths leading to the emergency staircase and exits, while red symbols show fire safety equipment such as extinguishers, alarms, and hydrants. The designated assembly point is marked outside the building.</p>
          <a class="btn-primary" href="{evac_pdf_href}" download="Evacuation Plan.pdf" style="width:fit-content;">Download Evacuation Plan (PDF) &nbsp;<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block;vertical-align:middle;margin-top:-2px;"><path d="M12 3v12"/><polyline points="7 10 12 15 17 10"/><path d="M5 21h14"/></svg></a>
        </div>
        <div class="garage-plan-img">
          {img_tag_sm(evac_plan, "Evacuation plan", "width:100%;height:auto;object-fit:contain;display:block;padding:16px;background:#f9fbf9;")}
        </div>
      </div>
    </div>
    <div class="garage-plan-wrap">
      <div class="garage-plan-card" style="grid-template-columns:1fr;">
        <div class="garage-plan-text" style="padding:44px 52px;">
          <div class="section-tag">Important Numbers</div>
          {"".join(_number_row(label, value, i == len(_numbers) - 1) for i, (label, value) in enumerate(_numbers))}
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    _render_routed_footer()
    st.stop()

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<section id="welcome" class="pa-hero">
  <div class="pa-hero-left">
    <div class="hero-dear">Dear Guest,</div>
    <div class="hero-title">
      welcome to<br>
      <span>Peridot</span> Apartment
    </div>
    <p class="hero-text">
      Thank you for choosing our apartment in Kranjska Gora.<br>
      We wish you a pleasant stay and unforgettable moments in the mountains.
    </p>
    <div class="hero-btns">
      <a class="btn-primary" href="#checkin">Check-in Instructions</a>
      <a class="btn-outline" href="#checkout">Check-out Info</a>
    </div>
    <div class="hero-addr">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>
      </svg>
      Borovška cesta 99b, 4280 Kranjska Gora &nbsp;·&nbsp;
      <a href="https://www.google.com/maps/place/VILA+MOJCA+Kranjska+Gora+-+Peridot+apartment,+Sa%C5%A1a+Podpeskar+s.p./@46.4840309,13.7788626,17z/data=!3m1!4b1!4m6!3m5!1s0x477a7d96a036c899:0xc03b6f12d98b7421!8m2!3d46.4840272!4d13.7814429!16s%2Fg%2F11rgbrfk6w" target="_blank">Open in Google Maps &nbsp;<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block;vertical-align:middle;margin-top:-2px;"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg></a>
    </div>
  </div>
  <div class="pa-hero-right">
    <img src="data:image/jpeg;base64,{b64_compressed(building, max_w=1600, quality=92)}" alt="Villa Mojca" style="width:100%;object-fit:cover;display:block;">
    <div class="hero-img-overlay"></div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── INFO STRIP ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="pa-strip">

  <div class="strip-card">
    <div class="strip-icon">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
      </svg>
    </div>
    <div class="strip-title">Self Check-in</div>
    <div class="strip-desc">Arrive any time after 15:00.<br>Key safe access code sent in advance.</div>
  </div>

  <div class="strip-card">
    <div class="strip-icon">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
      </svg>
    </div>
    <div class="strip-title">Safe &amp; Secure</div>
    <div class="strip-desc">Private garage with remote access.<br>Secure building entrance.</div>
  </div>

  <div class="strip-card">
    <div class="strip-icon">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M2 15V13Q2 12 3 12H5L7.5 9Q9 8.5 12 8.5Q15 8.5 16.5 9L19 12H21Q22 12 22 13V15Q22 16 21 16H3Q2 16 2 15Z"/><line x1="12" y1="8.5" x2="12" y2="12"/><circle cx="7" cy="17.5" r="1.5"/><circle cx="17" cy="17.5" r="1.5"/>
      </svg>
    </div>
    <div class="strip-title">Parking &amp; Garage</div>
    <div class="strip-desc">Dedicated space #5 in covered garage.<br>Bicycle &amp; storage room included.</div>
  </div>

  <div class="strip-card">
    <div class="strip-icon">
      <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>
      </svg>
    </div>
    <div class="strip-title">We Are Here</div>
    <div class="strip-desc">Need anything? We are always<br>just a message away.</div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── CHECK-IN SECTION ──────────────────────────────────────────────────────────
_tl = (
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">1</div><div class="tl-line"></div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 1</div>'
      '<div class="tl-title">Arrive</div>'
      '<div class="tl-desc">Head to <strong>Villa Mojca</strong>, Borovška cesta 99b, Kranjska Gora.</div>'
    '</div>'
  '</div>'
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">2</div><div class="tl-line"></div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 2</div>'
      '<div class="tl-title">Find the Key Safe</div>'
      '<div class="tl-desc">The key safe is on the <strong>wall by the garage door, on the left side</strong>. Your access code will be sent via WhatsApp/SMS before arrival.</div>'
    '</div>'
  '</div>'
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">3</div><div class="tl-line"></div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 3</div>'
      '<div class="tl-title">Open the Safe</div>'
      '<div class="tl-desc">Enter your code, open the safe and take the <strong>apartment keys</strong> and <strong>garage remote</strong>.</div>'
    '</div>'
  '</div>'
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">4</div><div class="tl-line"></div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 4</div>'
      '<div class="tl-title">Garage Access</div>'
      '<div class="tl-desc">Use the remote to open the ramp first, then the garage door.</div>'
    '</div>'
  '</div>'
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">5</div><div class="tl-line"></div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 5</div>'
      '<div class="tl-title">Parking, Storage &amp; Bicycle Room</div>'
      '<div class="tl-desc">Your dedicated parking space is number <span style="color:#148A46;font-weight:700;">5</span> (fourth on the left side). In case you need additional storage or bicycle space, room number <span style="color:#148A46;font-weight:700;">5</span> is located in the garage area.</div>'
    '</div>'
  '</div>'
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">6</div><div class="tl-line"></div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 6</div>'
      '<div class="tl-title">Apartment Location</div>'
      '<div class="tl-desc">From the garage, take the <strong>stairs to the first floor</strong>. From the main entrance, the apartment is on the <strong>first floor to the right</strong>.</div>'
    '</div>'
  '</div>'
  '<div class="tl-item">'
    '<div class="tl-spine"><div class="tl-circle">7</div></div>'
    '<div class="tl-body">'
      '<div class="tl-step">Step 7</div>'
      '<div class="tl-title">Apartment Terrace</div>'
      '<div class="tl-desc">Enjoy <strong>mountain views</strong> from our terrace with a welcome drink prepared only for you.</div>'
    '</div>'
  '</div>'
)

_photos = (
  f'<div style="grid-column:1/-1;border-radius:14px;overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,0.08);">'
    f'<video controls preload="metadata" style="width:100%;display:block;border-radius:14px;">'
      f'<source src="data:video/mp4;base64,{b64_video(ASSETS/"VIDEO.mp4")}" type="video/mp4">'
    f'</video>'
  f'</div>'
  f'<div class="photo-card">'
    f'{img_tag_sm(key_safe, "Key safe", "width:100%;height:190px;object-fit:cover;display:block;")}'
    f'<div class="photo-cap">Key safe</div>'
  f'</div>'
  f'<div class="photo-card">'
    f'{img_tag_sm(garage_img, "Garage &amp; Storage room", "width:100%;height:190px;object-fit:cover;display:block;")}'
    f'<div class="photo-cap">Garage &amp; Storage room</div>'
  f'</div>'
  f'<div class="photo-card">'
    f'{img_tag_sm(terrace, "Terrace", "width:100%;height:190px;object-fit:cover;display:block;")}'
    f'<div class="photo-cap">Apartment terrace</div>'
  f'</div>'
  f'<div class="photo-card">'
    f'{img_tag_sm(bicycle, "Bicycle &amp; storage", "width:100%;height:190px;object-fit:cover;display:block;")}'
    f'<div class="photo-cap">Bicycle room</div>'
  f'</div>'
  f'<div style="grid-column:1/-1;display:flex;justify-content:center;margin-top:72px;">'
    f'{img_tag_sm(enjoy, "Enjoy your stay", "width:55%;height:130px;object-fit:cover;display:block;border-radius:14px;")}'
  f'</div>'
)

_important = (
  f'<div class="important-notice">'
    f'<div class="important-badge">'
      f'<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/><circle cx="12" cy="12" r="10"/></svg>'
      f' Important — Before or Upon Arrival'
    f'</div>'
    f'<div style="display:flex;gap:16px;align-items:center;margin-top:4px;">'
      f'<div style="flex:1;">'
        f'<h4>Guest Registration Required</h4>'
        f'<p>Slovenian law requires all accommodation providers to register guests before or shortly after arrival. Please provide the required registration details (<strong style="color:#fff;">full name, date of birth, nationality, permanent address, and ID/passport number</strong>) for all guests before your arrival, or present your ID/passport upon arrival so we can verify the information and complete the registration. For your privacy and security, your personal data will only be used for the mandatory guest registration and will not be used for any other purpose. Please note that the tourist tax is not included in the accommodation price and is payable separately, and should be settled before check-out.</p>'
      f'</div>'
      f'<div style="flex-shrink:0;">'
        f'{img_tag_sm(id_photo, "ID document", "width:110px;height:80px;object-fit:cover;border-radius:10px;opacity:0.92;")}'
      f'</div>'
    f'</div>'
  f'</div>'
)

st.markdown(
f'<section id="checkin" class="pa-section">'
f'<div class="checkin-header">'
f'<div>'
f'<div class="section-tag">Your arrival guide</div>'
f'<div class="section-divider"></div>'
f'<div class="section-h2">Check-in Instructions</div>'
f'<p class="section-sub" style="margin-bottom:0">Everything you need to know before arriving at Peridot Apartment.</p>'
f'</div>'
f'{_important}'
f'</div>'
f'<div class="checkin-grid">'
f'<div class="timeline">{_tl}</div>'
f'<div class="photo-grid">{_photos}</div>'
f'</div>'
f'</section>',
unsafe_allow_html=True)

# ── KEY BOX LOCATION CARD ─────────────────────────────────────────────────────
st.markdown(
f'<div class="garage-plan-wrap">'
f'<div class="garage-plan-card">'
f'<div class="garage-plan-text">'
f'<div class="section-tag">Key box location &amp; apartment location</div>'
f'<h3>Where to Find the Key Safe and the Apartment?</h3>'
f'<div class="garage-badge">'
f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
f' Key Safe — beside the garage entrance, on the left'
f'</div>'
f'<div class="garage-badge">'
f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
f' Apartment on the first floor'
f'</div>'
f'<p>The apartment keys and garage remote are stored in the key safe beside the garage entrance. Use the access code provided before arrival to open the safe and enter the garage area. The apartment is located on the first floor to the right.</p>'
f'</div>'
f'<div class="garage-plan-img" style="align-self:start;">'
f'{img_tag_sm(key_box_loc, "Key box location", "width:100%;height:320px;object-fit:contain;display:block;padding:16px;background:#f9fbf9;", max_w=1200, quality=95)}'
f'<div style="border-top:1px solid var(--border);padding:16px 24px;display:flex;gap:32px;">'
f'<span style="font-family:Inter,sans-serif;font-size:13px;color:var(--muted);display:flex;align-items:center;gap:10px;">'
f'<span style="width:22px;height:22px;border-radius:50%;background:var(--green);color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;">1</span>'
f'Garage entrance'
f'</span>'
f'<span style="font-family:Inter,sans-serif;font-size:13px;color:var(--muted);display:flex;align-items:center;gap:10px;">'
f'<span style="width:22px;height:22px;border-radius:50%;background:var(--green);color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;">2</span>'
f'Building entrance'
f'</span>'
f'</div>'
f'</div>'
f'</div>'
f'</div>',
unsafe_allow_html=True)

# ── GARAGE PLAN CARD ──────────────────────────────────────────────────────────
if garage_plan.exists():
    plan_html = img_tag_sm(garage_plan, "Garage floor plan", "width:100%;height:320px;object-fit:contain;display:block;padding:16px;background:#f9fbf9;")
else:
    plan_html = '<div style="height:320px;background:#F1F8F4;display:flex;align-items:center;justify-content:center;color:#999;font-family:Inter,sans-serif;font-size:14px;">Floor plan coming soon</div>'

st.markdown(f"""
<div class="garage-plan-wrap">
  <div class="garage-plan-card">
    <div class="garage-plan-text">
      <div class="section-tag">Garage layout</div>
      <h3>Your Parking Space, Storage &amp; Bicycle Room</h3>
      <div class="garage-badge">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
        Parking space number 5 — on the left
      </div>
      <div class="garage-badge">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
        Storage in garage — number 4
      </div>
      <div class="garage-badge">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
        Bicycle room before garage entrance — number 5
      </div>
      <p>Your dedicated parking space is number 5 — the fourth parking space on the left. Storage room number 4 is located inside the garage area through the door on the left side (as marked on the map). Before the garage entrance, you can also access the bicycle room for storing bicycles or additional equipment.</p>
    </div>
    <div class="garage-plan-img">
      {plan_html}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── TEMPERATURE SECTION ───────────────────────────────────────────────────────
st.markdown(f"""
<section id="temperature" class="pa-section" style="padding-bottom:0;">
  <div class="section-tag">Comfort tips</div>
  <div class="section-divider"></div>
  <div class="section-h2">Apartment Temperature Regulation</div>
  <p class="section-sub">During summer days, you can help keep the apartment cool and comfortable by using the blinds and the air recuperation system together.</p>
</section>
<div class="garage-plan-wrap" style="padding-bottom:32px;">
  <div class="garage-plan-card">
    <div class="garage-plan-text">
      <div class="section-tag">Blinds</div>
      <h3>Blinds</h3>
      <p>The apartment blinds can be lowered during the day to reduce direct sunlight and prevent the apartment from overheating. Keeping the blinds closed, especially on sunny windows, will help maintain a cooler indoor temperature.</p>
    </div>
    <div class="garage-plan-img">
      {img_tag_sm(blinds_img, "Blinds", "width:100%;height:220px;object-fit:contain;display:block;padding:16px;background:#f9fbf9;", max_w=1200, quality=95)}
    </div>
  </div>
</div>
<div class="garage-plan-wrap">
  <div class="garage-plan-card">
    <div class="garage-plan-img">
      {img_tag_sm(air_recup_img, "Air recuperation system", "width:100%;height:220px;object-fit:contain;display:block;padding:16px;background:#f9fbf9;", max_w=1200, quality=95)}
    </div>
    <div class="garage-plan-text">
      <div class="section-tag">Air Recuperation System</div>
      <h3>Air Recuperation System</h3>
      <p>The air recuperation system continuously circulates fresh air throughout the apartment and helps maintain a fresh and comfortable indoor climate during summer days. For the best cooling effect, we recommend using the economy/automatic mode and keeping the fan speed on level 1.</p>
    </div>
    <div style="grid-column:1 / -1;border-top:1px solid var(--border);padding:28px 52px 36px;">
      <div class="section-tag" style="margin-bottom:14px;">Air Recuperation System Control Panel</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px 28px;">
        {"".join(
          f'<div style="display:flex;align-items:flex-start;gap:10px;">'
          f'<span style="width:22px;height:22px;border-radius:50%;background:var(--green);color:#fff;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;">{n}</span>'
          f'<span class="legend-label" style="font-family:Inter,sans-serif;font-size:13.5px;color:var(--muted);line-height:1.45;">{label}</span>'
          f'</div>'
          for n, label in [
            (1, "Fan speed indicator"),
            (2, "Increase fan speed"),
            (3, "Automatic mode (AUTO)"),
            (4, "Decrease fan speed / power off"),
            (5, "Economy mode"),
            (6, "Standard ventilation mode"),
            (7, "Sleep / quiet mode"),
            (8, "Filter indicator"),
          ]
        )}
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── CONTACT CARD ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div id="contact" class="contact-section">
  <div class="contact-card">
    <div class="contact-left">
      <h3>Contact Saša</h3>
      <div class="contact-line">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.15 11.9a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.06 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.09 8.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>
        </svg>
        <span>WhatsApp / Viber / GSM: <a href="tel:+38631676315">+386 31 676 315</a></span>
      </div>
      <div class="contact-line">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
          <polyline points="22,6 12,13 2,6"/>
        </svg>
        <span>E-mail: <a href="mailto:sasa.podpeskar@gmail.com">sasa.podpeskar@gmail.com</a></span>
      </div>
      <div class="contact-line">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <line x1="2" y1="12" x2="22" y2="12"/>
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
        </svg>
        <span>Website: <a href="https://www.vila-mojca.com" target="_blank">www.vila-mojca.com</a></span>
      </div>
    </div>
    <div class="contact-sig">
      {img_tag_sm(here4u, "Saša & Rok", "max-height:200px;max-width:280px;object-fit:contain;")}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CHECK-OUT SECTION ─────────────────────────────────────────────────────────
_chk_icon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#148A46" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'

st.markdown(
f'<section id="checkout" class="pa-section pa-section-alt">'
f'<div class="section-tag">End of your stay</div>'
f'<div class="section-divider"></div>'
f'<div class="section-h2">Check-out</div>'
f'<div class="checkout-grid">'
f'<div class="checkout-left">'
f'<p class="checkout-intro">We hope you had a wonderful time in Kranjska Gora.</p>'
f'<div class="checklist">'
f'<div class="cl-item">{_chk_icon}<span><strong>Check-out is by 10:00 a.m.</strong></span></div>'
f'<div class="cl-item">{_chk_icon}<span>Return the keys to the key safe, <strong>lock it and close the lid</strong>. Leave the garage remote with the keys.</span></div>'
f'<div class="cl-item">{_chk_icon}<span>Make sure <strong>all windows and doors are closed</strong> before leaving.</span></div>'
f'<div class="cl-item">{_chk_icon}<span>Please <strong>take out all trash</strong> before leaving.</span></div>'
f'</div>'
f'<div class="direct-note"><strong>Thank you for staying with us.</strong> For your next stay, feel free to contact us directly for possible special offers and returning guest benefits.</div>'
f'<a class="btn-primary" href="https://vila-mojca.com/en/dobrodosli-english/" target="_blank">Book Directly Next Time &nbsp;<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="display:inline-block;vertical-align:middle;margin-top:-2px;"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg></a>'
f'</div>'
f'<div class="checkout-img">'
f'{img_tag_sm(checkout, "Key return", "width:100%;height:420px;object-fit:cover;display:block;")}'
f'</div>'
f'</div>'
f'<div style="display:flex;justify-content:center;margin-top:36px;">'
f'{img_tag(wishing_you, "Wishing you", "width:26%;display:block;")}'
f'</div>'
f'</section>',
unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(
f'<div class="pa-footer">'
f'<div class="footer-left">'
f'<p><strong>Need anything during your stay?</strong></p>'
f'<p>Contact Saša anytime — we\'re always happy to help.</p>'
f'<p><a href="tel:+38631676315">+386 31 676 315</a> &nbsp;·&nbsp; <a href="mailto:sasa.podpeskar@gmail.com">sasa.podpeskar@gmail.com</a></p>'
f'</div>'
f'<div class="footer-logo">'
f'{img_tag(logo, "Peridot Apartment", "height:52px;object-fit:contain;filter:brightness(0) invert(1);opacity:0.88;")}'
f'</div>'
f'<div class="footer-copy">© Peridot Apartment · Villa Mojca · Borovška cesta 99b, 4280 Kranjska Gora</div>'
f'</div>',
unsafe_allow_html=True)
