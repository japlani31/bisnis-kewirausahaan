import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Studi Kasus Rasio", page_icon="📐", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    line-height: 1.65;
}

.stApp {
    background: linear-gradient(150deg, #0d0f1e 0%, #141830 60%, #0f1222 100%);
}

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.03) !important;
    border-right: 1px solid rgba(255,255,255,0.07);
}
section[data-testid="stSidebar"] * { color: #8a9ab0 !important; }

h1, h2, h3 { color: #d0dcea !important; }
p, li { color: #8896a8 !important; font-size: 0.9rem; line-height: 1.65; }
label { color: #7a8ea4 !important; font-size: 0.88rem; }

.stTextInput input, .stNumberInput input {
    background: #f5f7fa !important;
    color: #1c2333 !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    border-radius: 7px !important;
    font-size: 0.9rem !important;
}
div[data-baseweb="select"] > div {
    background: #f5f7fa !important;
    color: #1c2333 !important;
    border-radius: 7px !important;
}
div[data-baseweb="select"] span { color: #1c2333 !important; }

.stButton button {
    background: #1e3a5f !important;
    color: #b8cce0 !important;
    font-weight: 600 !important;
    border: 1px solid rgba(80,130,200,0.25) !important;
    border-radius: 8px !important;
    padding: 0.55rem 2rem !important;
    font-size: 0.9rem !important;
}

.page-title {
    font-size: 1.55rem;
    font-weight: 700;
    color: #c4d4e4 !important;
    margin: 0 0 0.3rem 0;
    letter-spacing: -0.2px;
}
.page-sub { color: #566880 !important; font-size: 0.86rem; margin-bottom: 0; }

.section-title {
    font-size: 0.95rem;
    font-weight: 600;
    color: #a0b4c8 !important;
    margin: 1.4rem 0 0.7rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid rgba(140,170,210,0.15);
    letter-spacing: 0.2px;
}

.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 10px;
    padding: 0.95rem 1.1rem;
    margin-bottom: 0.5rem;
}

.info-box {
    background: rgba(60,100,170,0.07);
    border: 1px solid rgba(60,100,170,0.18);
    border-radius: 9px;
    padding: 0.75rem 1rem;
    margin: 0.4rem 0 0.8rem 0;
}

.pill-g {
    display: inline-block;
    background: rgba(74,200,120,0.11);
    color: #5eaa7a !important;
    border: 1px solid rgba(74,200,120,0.22);
    border-radius: 10px;
    padding: 0.1rem 0.55rem;
    font-size: 0.71rem;
    font-weight: 600;
}
.pill-a {
    display: inline-block;
    background: rgba(210,165,55,0.11);
    color: #b89438 !important;
    border: 1px solid rgba(210,165,55,0.22);
    border-radius: 10px;
    padding: 0.1rem 0.55rem;
    font-size: 0.71rem;
    font-weight: 600;
}
.pill-r {
    display: inline-block;
    background: rgba(200,75,75,0.11);
    color: #c05858 !important;
    border: 1px solid rgba(200,75,75,0.22);
    border-radius: 10px;
    padding: 0.1rem 0.55rem;
    font-size: 0.71rem;
    font-weight: 600;
}

.col-head {
    font-size: 0.72rem;
    font-weight: 600;
    color: #44607a !important;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin: 0;
}
.row-label { font-size: 0.87rem; color: #8898ac !important; margin: 0; padding: 0.22rem 0; }
.row-val1  { font-size: 0.87rem; color: #6878a0 !important; margin: 0; padding: 0.22rem 0; }
.row-val2  { font-size: 0.9rem;  color: #aac0d8 !important; font-weight: 600; margin: 0; padding: 0.22rem 0; }
.divider   { border-top: 1px solid rgba(255,255,255,0.06); margin: 0.25rem 0; }

.bench-row-name  { font-size: 0.85rem; color: #7a8aa0 !important; margin: 0; padding: 0.2rem 0; }
.bench-row-good  { font-size: 0.82rem; color: #5eaa7a !important; margin: 0; padding: 0.2rem 0; }
.bench-row-ok    { font-size: 0.82rem; color: #b89438 !important; margin: 0; padding: 0.2rem 0; }
.bench-row-bad   { font-size: 0.82rem; color: #c05858 !important; margin: 0; padding: 0.2rem 0; }
.bench-row-note  { font-size: 0.78rem; color: #506070 !important; margin: 0; padding: 0.2rem 0; font-style: italic; }

.insight-pos {
    background: rgba(74,200,120,0.05);
    border: 1px solid rgba(74,200,120,0.14);
    border-left: 3px solid #4a7a5a;
    border-radius: 0 8px 8px 0;
    padding: 0.5rem 0.8rem;
    margin-bottom: 0.4rem;
}
.insight-neg {
    background: rgba(200,75,75,0.05);
    border: 1px solid rgba(200,75,75,0.14);
    border-left: 3px solid #8a4848;
    border-radius: 0 8px 8px 0;
    padding: 0.5rem 0.8rem;
    margin-bottom: 0.4rem;
}
.insight-text { font-size: 0.84rem; color: #7a8890 !important; margin: 0; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════
st.markdown('<p class="page-title">📐 Studi Kasus &amp; Perbandingan Rasio Keuangan</p>', unsafe_allow_html=True)
st.markdown('<p class="page-sub">Bandingkan kinerja keuangan dua periode atau gunakan studi kasus UMKM untuk memahami tren rasio secara nyata.</p>', unsafe_allow_html=True)
st.markdown("---")

# ══════════════════════════════════════════════════════════════════
# DATA STUDI KASUS
# ══════════════════════════════════════════════════════════════════
KASUS = {
    "☕  Warung Kopi Nusantara — Kuliner / F&B": {
        "deskripsi": (
            "Kedai kopi lokal di Metro, Lampung. Berdiri 2022 dengan modal KUR Rp 30 juta. "
            "Di tahun kedua menambah menu makanan ringan dan minuman seasonal."
        ),
        "label1": "Tahun 2023 — Tahun Pertama",
        "label2": "Tahun 2024 — Setelah Berkembang",
        "p1": dict(rev=120_000_000, cogs=72_000_000, net_inc=13_000_000,
                   cash=15_000_000, ar=2_000_000, inv=8_000_000, fixed=45_000_000,
                   cl=12_000_000, ltd=20_000_000, equity=38_000_000),
        "p2": dict(rev=185_000_000, cogs=102_000_000, net_inc=35_000_000,
                   cash=28_000_000, ar=5_000_000, inv=10_000_000, fixed=55_000_000,
                   cl=8_000_000, ltd=15_000_000, equity=75_000_000),
    },
    "🧵  Batik Lampung Heritage — Fashion / Kerajinan": {
        "deskripsi": (
            "Usaha batik khas Lampung yang melayani pesanan custom dan retail. "
            "Di tahun kedua berhasil menurunkan piutang macet dan mengurangi stok berlebih."
        ),
        "label1": "Tahun 2023 — Sebelum Pembenahan",
        "label2": "Tahun 2024 — Sesudah Pembenahan",
        "p1": dict(rev=250_000_000, cogs=165_000_000, net_inc=22_000_000,
                   cash=10_000_000, ar=40_000_000, inv=80_000_000, fixed=100_000_000,
                   cl=55_000_000, ltd=80_000_000, equity=95_000_000),
        "p2": dict(rev=320_000_000, cogs=195_000_000, net_inc=46_000_000,
                   cash=25_000_000, ar=32_000_000, inv=62_000_000, fixed=115_000_000,
                   cl=40_000_000, ltd=65_000_000, equity=135_000_000),
    },
    "💻  DigiMarketing Pro — Jasa Digital / Tech": {
        "deskripsi": (
            "Agensi pemasaran digital yang membantu UMKM lokal. Layanan meliputi kelola "
            "media sosial, iklan digital, dan pembuatan website. Tidak butuh stok besar."
        ),
        "label1": "Tahun 2023 — Fase Rintisan",
        "label2": "Tahun 2024 — Skala Naik",
        "p1": dict(rev=80_000_000, cogs=22_000_000, net_inc=25_000_000,
                   cash=20_000_000, ar=15_000_000, inv=1_500_000, fixed=28_000_000,
                   cl=8_000_000, ltd=10_000_000, equity=46_500_000),
        "p2": dict(rev=148_000_000, cogs=35_000_000, net_inc=60_000_000,
                   cash=50_000_000, ar=18_000_000, inv=800_000, fixed=32_000_000,
                   cl=10_000_000, ltd=8_000_000, equity=82_800_000),
    },
}

# ══════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════
def hitung_rasio(d, lbl):
    al  = d["cash"] + d["ar"] + d["inv"]
    ta  = al + d["fixed"]
    th  = d["cl"]  + d["ltd"]
    r   = d["rev"]
    return {
        "label":                  lbl,
        "Gross Margin (%)":       round((r - d["cogs"]) / r * 100, 2) if r > 0 else 0,
        "Net Profit Margin (%)":  round(d["net_inc"] / r * 100, 2)    if r > 0 else 0,
        "ROA (%)":                round(d["net_inc"] / ta * 100, 2)   if ta > 0 else 0,
        "ROE (%)":                round(d["net_inc"] / d["equity"] * 100, 2) if d["equity"] > 0 else 0,
        "Current Ratio (x)":      round(al / d["cl"], 2)              if d["cl"] > 0 else 0,
        "Quick Ratio (x)":        round((al - d["inv"]) / d["cl"], 2) if d["cl"] > 0 else 0,
        "Debt to Equity (x)":     round(th / d["equity"], 2)          if d["equity"] > 0 else 0,
        "Debt Ratio":             round(th / ta, 2)                   if ta > 0 else 0,
        "Asset Turnover (x)":     round(r / ta, 2)                    if ta > 0 else 0,
        "Inventory Turnover (x)": round(d["cogs"] / d["inv"], 1)      if d["inv"] > 0 else 0,
        "DSO (hari)":             round(d["ar"] / (r / 365), 1)       if r > 0 else 0,
    }

def warna(name, val):
    rules = {
        "Gross Margin (%)":       ("hi", 20,  10),
        "Net Profit Margin (%)":  ("hi", 15,   5),
        "ROA (%)":                ("hi", 10,   5),
        "ROE (%)":                ("hi", 15,   8),
        "Current Ratio (x)":      ("hi",  2,   1),
        "Quick Ratio (x)":        ("hi",  1, 0.7),
        "Debt to Equity (x)":     ("lo",  1,   2),
        "Debt Ratio":             ("lo", 0.5, 0.7),
        "Asset Turnover (x)":     ("hi",  1, 0.5),
        "Inventory Turnover (x)": ("hi",  6,   3),
        "DSO (hari)":             ("lo", 30,  60),
    }
    if name not in rules:
        return "amber"
    d, good, ok = rules[name]
    if d == "hi":
        return "green" if val >= good else "amber" if val >= ok else "red"
    else:
        return "green" if val <= good else "amber" if val <= ok else "red"

def pill(w):
    lbl = {"green": "✓ Baik", "amber": "⚡ Cukup", "red": "⚠ Waspada"}
    cls = {"green": "pill-g",  "amber": "pill-a",   "red": "pill-r"}
    return f'<span class="{cls[w]}">{lbl[w]}</span>'

def arah(name, v1, v2):
    if v1 == 0:
        return "—", "#44607a"
    delta = v2 - v1
    pct   = abs(delta) / abs(v1) * 100
    lo_better = name in ("Debt to Equity (x)", "Debt Ratio", "DSO (hari)")
    baik = (delta < 0) if lo_better else (delta > 0)
    sym  = "▲" if delta > 0 else "▼"
    col  = "#5eaa7a" if baik else "#c05858"
    return f"{sym} {pct:.1f}%", col

# ══════════════════════════════════════════════════════════════════
# MODE SELECTION
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">1️⃣ Mode Analisis</div>', unsafe_allow_html=True)
mode = st.radio(
    "",
    ["📅  Perbandingan Dua Periode (Bisnis Saya)", "📚  Gunakan Studi Kasus UMKM"],
    horizontal=True,
    label_visibility="collapsed"
)

# ══════════════════════════════════════════════════════════════════
# DATA INPUT
# ══════════════════════════════════════════════════════════════════
p1_d, p2_d = {}, {}
label1, label2, biz_name = "Periode 1", "Periode 2", "Bisnis"

if mode == "📚  Gunakan Studi Kasus UMKM":
    st.markdown('<div class="section-title">2️⃣ Pilih Studi Kasus</div>', unsafe_allow_html=True)
    sel = st.selectbox("", list(KASUS.keys()), label_visibility="collapsed")
    kasus = KASUS[sel]
    st.markdown(
        f'<div class="info-box"><p style="margin:0;font-size:0.84rem;color:#607a94 !important">'
        f'📋 <strong style="color:#7a9ab8">Latar Belakang Bisnis:</strong> {kasus["deskripsi"]}</p></div>',
        unsafe_allow_html=True
    )
    p1_d, p2_d = kasus["p1"], kasus["p2"]
    label1, label2 = kasus["label1"], kasus["label2"]
    biz_name = sel.split("—")[0].strip()

else:
    col_a, col_b = st.columns(2)
    with col_a:
        biz_name = st.text_input("Nama Bisnis", placeholder="Contoh: Toko Pakaian Anugrah")
        label1   = st.text_input("Nama Periode 1", value="Tahun Lalu")
    with col_b:
        st.markdown("<br>", unsafe_allow_html=True)
        label2 = st.text_input("Nama Periode 2", value="Tahun Ini")

    st.markdown('<div class="section-title">2️⃣ Laporan Laba Rugi &nbsp;<span style="font-weight:400;color:#44607a;font-size:0.78rem">(dalam Rupiah)</span></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<p style="font-size:0.8rem;font-weight:600;color:#6a8cb0;margin-bottom:0.3rem">📅 {label1}</p>', unsafe_allow_html=True)
        p1_d["rev"]     = st.number_input("Pendapatan (P1)",    min_value=0, value=120_000_000, step=1_000_000, format="%d", key="rev1")
        p1_d["cogs"]    = st.number_input("HPP (P1)",           min_value=0, value=72_000_000,  step=1_000_000, format="%d", key="cogs1")
        p1_d["net_inc"] = st.number_input("Laba Bersih (P1)",   min_value=0, value=13_000_000,  step=500_000,   format="%d", key="ni1")
    with col2:
        st.markdown(f'<p style="font-size:0.8rem;font-weight:600;color:#6a8cb0;margin-bottom:0.3rem">📅 {label2}</p>', unsafe_allow_html=True)
        p2_d["rev"]     = st.number_input("Pendapatan (P2)",    min_value=0, value=185_000_000, step=1_000_000, format="%d", key="rev2")
        p2_d["cogs"]    = st.number_input("HPP (P2)",           min_value=0, value=102_000_000, step=1_000_000, format="%d", key="cogs2")
        p2_d["net_inc"] = st.number_input("Laba Bersih (P2)",   min_value=0, value=35_000_000,  step=500_000,   format="%d", key="ni2")

    st.markdown('<div class="section-title">3️⃣ Neraca / Balance Sheet &nbsp;<span style="font-weight:400;color:#44607a;font-size:0.78rem">(dalam Rupiah)</span></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<p style="font-size:0.8rem;font-weight:600;color:#6a8cb0;margin-bottom:0.3rem">📅 {label1}</p>', unsafe_allow_html=True)
        p1_d["cash"]   = st.number_input("Kas (P1)",                 min_value=0, value=15_000_000, step=500_000,   format="%d", key="cash1")
        p1_d["ar"]     = st.number_input("Piutang Usaha (P1)",       min_value=0, value=2_000_000,  step=500_000,   format="%d", key="ar1")
        p1_d["inv"]    = st.number_input("Persediaan (P1)",          min_value=0, value=8_000_000,  step=500_000,   format="%d", key="inv1")
        p1_d["fixed"]  = st.number_input("Aktiva Tetap Bersih (P1)", min_value=0, value=45_000_000, step=1_000_000, format="%d", key="fa1")
        p1_d["cl"]     = st.number_input("Hutang Lancar (P1)",       min_value=1, value=12_000_000, step=500_000,   format="%d", key="cl1")
        p1_d["ltd"]    = st.number_input("Hutang Jangka Panjang (P1)",min_value=0, value=20_000_000,step=1_000_000, format="%d", key="ltd1")
        p1_d["equity"] = st.number_input("Modal / Ekuitas (P1)",     min_value=1, value=38_000_000, step=1_000_000, format="%d", key="eq1")
    with col2:
        st.markdown(f'<p style="font-size:0.8rem;font-weight:600;color:#6a8cb0;margin-bottom:0.3rem">📅 {label2}</p>', unsafe_allow_html=True)
        p2_d["cash"]   = st.number_input("Kas (P2)",                 min_value=0, value=28_000_000, step=500_000,   format="%d", key="cash2")
        p2_d["ar"]     = st.number_input("Piutang Usaha (P2)",       min_value=0, value=5_000_000,  step=500_000,   format="%d", key="ar2")
        p2_d["inv"]    = st.number_input("Persediaan (P2)",          min_value=0, value=10_000_000, step=500_000,   format="%d", key="inv2")
        p2_d["fixed"]  = st.number_input("Aktiva Tetap Bersih (P2)", min_value=0, value=55_000_000, step=1_000_000, format="%d", key="fa2")
        p2_d["cl"]     = st.number_input("Hutang Lancar (P2)",       min_value=1, value=8_000_000,  step=500_000,   format="%d", key="cl2")
        p2_d["ltd"]    = st.number_input("Hutang Jangka Panjang (P2)",min_value=0, value=15_000_000,step=1_000_000, format="%d", key="ltd2")
        p2_d["equity"] = st.number_input("Modal / Ekuitas (P2)",     min_value=1, value=75_000_000, step=1_000_000, format="%d", key="eq2")

# ══════════════════════════════════════════════════════════════════
# TOMBOL ANALISIS
# ══════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔍  Analisis Perbandingan Rasio"):

    r1 = hitung_rasio(p1_d, label1)
    r2 = hitung_rasio(p2_d, label2)
    RASIO_KEYS = [k for k in r1 if k != "label"]

    st.markdown("---")
    st.markdown(
        f'<p style="font-size:1.25rem;font-weight:700;color:#b8cce0;margin-bottom:0.4rem">'
        f'📊 Hasil Analisis — {biz_name}</p>',
        unsafe_allow_html=True
    )

    tabs = st.tabs(["📋  Tabel Perbandingan", "📈  Grafik Rasio", "🔎  Interpretasi & Rekomendasi"])

    # ══════════════════════════════════════════════════════════
    # TAB 1 — TABEL PERBANDINGAN
    # ══════════════════════════════════════════════════════════
    with tabs[0]:
        KATEGORI = {
            "💰 Profitabilitas": ["Gross Margin (%)", "Net Profit Margin (%)", "ROA (%)", "ROE (%)"],
            "🏦 Likuiditas":     ["Current Ratio (x)", "Quick Ratio (x)"],
            "⚖️ Solvabilitas":   ["Debt to Equity (x)", "Debt Ratio"],
            "⚙️ Aktivitas":      ["Asset Turnover (x)", "Inventory Turnover (x)", "DSO (hari)"],
        }

        for kat, keys in KATEGORI.items():
            st.markdown(f'<div class="section-title">{kat}</div>', unsafe_allow_html=True)

            hc = st.columns([3, 1.8, 1.8, 1.6, 1.6])
            for col, hdr in zip(hc, ["Nama Rasio", label1, label2, "Perubahan", "Status"]):
                col.markdown(f'<p class="col-head">{hdr}</p>', unsafe_allow_html=True)
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            for k in keys:
                v1  = r1.get(k, 0)
                v2  = r2.get(k, 0)
                w   = warna(k, v2)
                arr, arc = arah(k, v1, v2)
                fmt = ".1f" if "%" in k or "x)" in k or "hari" in k else ".2f"
                rc  = st.columns([3, 1.8, 1.8, 1.6, 1.6])
                rc[0].markdown(f'<p class="row-label">{k}</p>', unsafe_allow_html=True)
                rc[1].markdown(f'<p class="row-val1">{v1:{fmt}}</p>', unsafe_allow_html=True)
                rc[2].markdown(f'<p class="row-val2">{v2:{fmt}}</p>', unsafe_allow_html=True)
                rc[3].markdown(f'<p style="font-size:0.82rem;color:{arc};font-weight:600;margin:0;padding:0.22rem 0">{arr}</p>', unsafe_allow_html=True)
                rc[4].markdown(pill(w), unsafe_allow_html=True)
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════
    # TAB 2 — GRAFIK PERBANDINGAN
    # ══════════════════════════════════════════════════════════
    with tabs[1]:
        chart_groups = [
            ("Profitabilitas (%)",  ["Gross Margin (%)", "Net Profit Margin (%)", "ROA (%)", "ROE (%)"]),
            ("Likuiditas & Solvabilitas", ["Current Ratio (x)", "Quick Ratio (x)", "Debt to Equity (x)"]),
            ("Aktivitas",           ["Asset Turnover (x)", "Inventory Turnover (x)"]),
        ]

        COLOR1 = "#3d6090"
        COLOR2 = "#4a9a6a"

        for title, keys in chart_groups:
            v1s = [r1.get(k, 0) for k in keys]
            v2s = [r2.get(k, 0) for k in keys]
            lbs = [k.replace(" (%)", "").replace(" (x)", "").replace(" (hari)", "") for k in keys]

            fig = go.Figure()
            fig.add_trace(go.Bar(
                name=label1, x=lbs, y=v1s,
                marker_color=COLOR1, opacity=0.72,
                text=[f"{v:.1f}" for v in v1s], textposition="outside",
                textfont=dict(size=10, color="#6070a0")
            ))
            fig.add_trace(go.Bar(
                name=label2, x=lbs, y=v2s,
                marker_color=COLOR2, opacity=0.82,
                text=[f"{v:.1f}" for v in v2s], textposition="outside",
                textfont=dict(size=10, color="#5a9060")
            ))
            fig.update_layout(
                barmode="group",
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                title=dict(text=title, font=dict(color="#8090a8", size=12)),
                legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
                font=dict(color="#5a6880"),
                margin=dict(l=10, r=10, t=44, b=30),
                height=300,
                bargap=0.18,
                bargroupgap=0.06,
                xaxis=dict(tickfont=dict(size=10, color="#5a6880"), gridcolor="rgba(0,0,0,0)"),
                yaxis=dict(tickfont=dict(size=9, color="#5a6880"), gridcolor="rgba(255,255,255,0.05)", zeroline=False),
            )
            st.plotly_chart(fig, use_container_width=True)

        # DSO barchart — terpisah karena satuannya hari bukan rasio
        dso_fig = go.Figure()
        dso_fig.add_trace(go.Bar(
            name=label1, x=["DSO (hari)"], y=[r1.get("DSO (hari)", 0)],
            marker_color=COLOR1, opacity=0.72,
            text=[f"{r1.get('DSO (hari)', 0):.0f} hari"], textposition="outside",
            textfont=dict(size=10, color="#6070a0")
        ))
        dso_fig.add_trace(go.Bar(
            name=label2, x=["DSO (hari)"], y=[r2.get("DSO (hari)", 0)],
            marker_color=COLOR2, opacity=0.82,
            text=[f"{r2.get('DSO (hari)', 0):.0f} hari"], textposition="outside",
            textfont=dict(size=10, color="#5a9060")
        ))
        dso_fig.update_layout(
            barmode="group", template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Days Sales Outstanding — Rata-rata Hari Piutang Tertagih (lebih rendah lebih baik)",
                       font=dict(color="#8090a8", size=12)),
            legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
            font=dict(color="#5a6880"), margin=dict(l=10, r=10, t=44, b=30),
            height=250,
            xaxis=dict(gridcolor="rgba(0,0,0,0)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)", zeroline=False,
                       ticksuffix=" hr", tickfont=dict(size=9, color="#5a6880")),
        )
        st.plotly_chart(dso_fig, use_container_width=True)

    # ══════════════════════════════════════════════════════════
    # TAB 3 — INTERPRETASI
    # ══════════════════════════════════════════════════════════
    with tabs[2]:
        st.markdown('<div class="section-title">📝 Ringkasan Temuan</div>', unsafe_allow_html=True)

        positif, perhatian = [], []
        for k in RASIO_KEYS:
            v1, v2 = r1.get(k, 0), r2.get(k, 0)
            w      = warna(k, v2)
            _, arc = arah(k, v1, v2)
            if w == "green" and arc == "#5eaa7a":
                positif.append(f"{k} membaik menjadi <strong>{v2:.2f}</strong> — sudah dalam kondisi baik.")
            elif w == "red":
                perhatian.append(f"{k} di angka <strong>{v2:.2f}</strong> — perlu tindakan perbaikan segera.")
            elif w == "amber":
                perhatian.append(f"{k} di angka <strong>{v2:.2f}</strong> — masih bisa dipertahankan, pantau terus.")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<p style="font-size:0.82rem;font-weight:600;color:#4a8a60;margin-bottom:0.5rem">✅ Poin Positif</p>', unsafe_allow_html=True)
            if positif:
                for p in positif:
                    st.markdown(f'<div class="insight-pos"><p class="insight-text">{p}</p></div>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="font-size:0.82rem;color:#3a5040 !important">Belum ada rasio yang berada di zona optimal.</p>', unsafe_allow_html=True)

        with col2:
            st.markdown('<p style="font-size:0.82rem;font-weight:600;color:#9a4848;margin-bottom:0.5rem">⚠️ Perlu Perhatian</p>', unsafe_allow_html=True)
            if perhatian:
                for p in perhatian:
                    st.markdown(f'<div class="insight-neg"><p class="insight-text">{p}</p></div>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="font-size:0.82rem;color:#3a3050 !important">Semua rasio dalam kondisi baik.</p>', unsafe_allow_html=True)

        # ── BENCHMARK TABLE ──────────────────────────────────
        st.markdown('<div class="section-title">📚 Acuan Benchmark Rasio untuk UMKM</div>', unsafe_allow_html=True)
        st.markdown(
            '<p style="font-size:0.78rem;color:#3a5060 !important;font-style:italic;margin-bottom:0.75rem">'
            'Angka berikut adalah acuan umum. Kondisi ideal dapat berbeda tergantung jenis industri dan skala bisnis.</p>',
            unsafe_allow_html=True
        )

        bench = [
            ("Gross Margin",        "≥ 20%",  "10–20%",  "< 10%",   "Efisiensi biaya produksi dari tiap Rp penjualan"),
            ("Net Profit Margin",   "≥ 15%",  "5–15%",   "< 5%",    "Laba bersih yang tersisa setelah semua biaya"),
            ("ROA",                 "≥ 10%",  "5–10%",   "< 5%",    "Seberapa produktif aset menghasilkan laba"),
            ("ROE",                 "≥ 15%",  "8–15%",   "< 8%",    "Return atas modal yang diinvestasikan pemilik"),
            ("Current Ratio",       "≥ 2x",   "1–2x",    "< 1x",    "Kemampuan membayar hutang jangka pendek"),
            ("Quick Ratio",         "≥ 1x",   "0.7–1x",  "< 0.7x",  "Likuiditas tanpa menghitung persediaan"),
            ("Debt to Equity",      "≤ 1x",   "1–2x",    "> 2x",    "Lebih rendah = struktur modal lebih sehat"),
            ("Debt Ratio",          "≤ 0.5",  "0.5–0.7", "> 0.7",   "Proporsi aset yang dibiayai dengan hutang"),
            ("Asset Turnover",      "≥ 1x",   "0.5–1x",  "< 0.5x",  "Efisiensi penggunaan aset menghasilkan pendapatan"),
            ("Inventory Turnover",  "≥ 6x/th","3–6x/th", "< 3x/th", "Seberapa cepat stok terjual — makin cepat makin baik"),
            ("DSO",                 "≤ 30 hr","30–60 hr", "> 60 hr", "Rata-rata hari piutang tertagih — makin singkat lebih baik"),
        ]

        hc = st.columns([2.2, 1.2, 1.3, 1.2, 3.2])
        for col, hdr in zip(hc, ["Rasio", "✅ Baik", "⚡ Cukup", "❌ Waspada", "Arti Praktis"]):
            col.markdown(f'<p class="col-head">{hdr}</p>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        for name, good, ok, bad, meaning in bench:
            bc = st.columns([2.2, 1.2, 1.3, 1.2, 3.2])
            bc[0].markdown(f'<p class="bench-row-name">{name}</p>', unsafe_allow_html=True)
            bc[1].markdown(f'<p class="bench-row-good">{good}</p>', unsafe_allow_html=True)
            bc[2].markdown(f'<p class="bench-row-ok">{ok}</p>', unsafe_allow_html=True)
            bc[3].markdown(f'<p class="bench-row-bad">{bad}</p>', unsafe_allow_html=True)
            bc[4].markdown(f'<p class="bench-row-note">{meaning}</p>', unsafe_allow_html=True)
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── PDF EXPORT ────────────────────────────────────────────────
    st.markdown("---")
    st.markdown('<p style="font-size:0.82rem;color:#3a5870 !important;margin-bottom:0.5rem">📄 Unduh laporan perbandingan rasio dalam format PDF.</p>', unsafe_allow_html=True)

    def _buat_pdf_rasio():
        import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from utils import BisnisKuPDF
        import datetime
        pdf = BisnisKuPDF(f"Perbandingan Rasio Keuangan — {biz_name}")
        pdf.add_page()

        pdf.section("Informasi Analisis")
        pdf.kv("Nama Bisnis / Studi Kasus", biz_name)
        pdf.kv("Periode 1", str(label1))
        pdf.kv("Periode 2", str(label2))
        pdf.kv("Tanggal Cetak", datetime.datetime.now().strftime("%d %B %Y %H:%M"))

        RASIO_KEYS = [k for k in r1 if k != "label"]
        KATEGORI = {
            "Profitabilitas": ["Gross Margin (%)", "Net Profit Margin (%)", "ROA (%)", "ROE (%)"],
            "Likuiditas":     ["Current Ratio (x)", "Quick Ratio (x)"],
            "Solvabilitas":   ["Debt to Equity (x)", "Debt Ratio"],
            "Aktivitas":      ["Asset Turnover (x)", "Inventory Turnover (x)", "DSO (hari)"],
        }
        lo_better = {"Debt to Equity (x)", "Debt Ratio", "DSO (hari)"}

        for kat, keys in KATEGORI.items():
            pdf.section(kat)
            pdf.th([f"Rasio", str(label1), str(label2), "Delta %", "Tren"], [60, 32, 32, 24, 34])
            for i, k in enumerate(keys):
                v1, v2 = r1.get(k, 0), r2.get(k, 0)
                delta = v2 - v1
                dpct  = delta / abs(v1) * 100 if v1 != 0 else 0
                lower = k in lo_better
                good  = (delta < 0) if lower else (delta >= 0)
                sym   = "+" if delta >= 0 else ""
                trend = "Membaik" if good else "Menurun"
                fmt   = ".1f" if "%" in k or "x)" in k else ".2f"
                pdf.tr([k, f"{v1:{fmt}}", f"{v2:{fmt}}", f"{sym}{dpct:.1f}%", trend],
                        [60, 32, 32, 24, 34], even=i%2==0)

        pdf.section("Acuan Benchmark UMKM (Kisaran Umum)")
        pdf.th(["Rasio","Baik","Cukup","Waspada"],[60,40,40,42])
        bench_data = [
            ("Gross Margin",      ">=20%","10-20%","<10%"),
            ("Net Profit Margin", ">=15%","5-15%","<5%"),
            ("ROA",               ">=10%","5-10%","<5%"),
            ("ROE",               ">=15%","8-15%","<8%"),
            ("Current Ratio",     ">=2x","1-2x","<1x"),
            ("Quick Ratio",       ">=1x","0.7-1x","<0.7x"),
            ("Debt to Equity",    "<=1x","1-2x",">2x"),
            ("Debt Ratio",        "<=0.5","0.5-0.7",">0.7"),
            ("DSO",               "<=30 hr","30-60 hr",">60 hr"),
        ]
        for i,(a,b,c,d) in enumerate(bench_data):
            pdf.tr([a,b,c,d],[60,40,40,42],even=i%2==0)
        pdf.note("Benchmark adalah kisaran umum UMKM. Nilai ideal bervariasi per industri dan skala bisnis.")
        return pdf.build()

    import datetime as _dt
    fname_r = f"BisnisKu_Rasio_{biz_name.replace(' ','_')}_{_dt.date.today()}.pdf"
    st.download_button(
        label="📄 Unduh Laporan Perbandingan Rasio (PDF)",
        data=_buat_pdf_rasio(),
        file_name=fname_r,
        mime="application/pdf",
    )
