import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Analisis Laporan Keuangan", page_icon="📊", layout="wide")

BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; line-height: 1.65; }
.stApp { background: linear-gradient(150deg, #0d0f1e 0%, #141830 60%, #0f1222 100%); }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.03) !important; border-right: 1px solid rgba(255,255,255,0.07); }
section[data-testid="stSidebar"] * { color: #8a9ab0 !important; }
h1,h2,h3 { color: #d0dcea !important; }
p, li  { color: #8896a8 !important; font-size: 0.9rem; line-height: 1.65; }
label  { color: #7a8ea4 !important; font-size: 0.88rem; }
.stTextInput input, .stNumberInput input {
    background: #f5f7fa !important; color: #1c2333 !important;
    border: 1px solid rgba(255,255,255,0.18) !important; border-radius: 7px !important; font-size: 0.9rem !important;
}
div[data-baseweb="select"] > div { background: #f5f7fa !important; color: #1c2333 !important; border-radius: 7px !important; }
div[data-baseweb="select"] span { color: #1c2333 !important; }
.stButton button {
    background: #1e3a5f !important; color: #b8cce0 !important; font-weight: 600 !important;
    border: 1px solid rgba(80,130,200,0.25) !important; border-radius: 8px !important;
    padding: 0.55rem 2rem !important; font-size: 0.9rem !important;
}
.sec { font-size: 0.95rem; font-weight: 600; color: #a0b4c8 !important;
       margin: 1.3rem 0 0.65rem 0; padding-bottom: 0.4rem; border-bottom: 1px solid rgba(140,170,210,0.14); }
.concept { background: rgba(40,70,120,0.1); border: 1px solid rgba(80,130,200,0.18);
           border-radius: 9px; padding: 0.75rem 1rem; margin: 0.4rem 0 0.75rem 0; }
.concept p { font-size: 0.86rem; color: #6882a0 !important; margin: 0; line-height: 1.65; }
.info-box { background: rgba(60,100,170,0.07); border: 1px solid rgba(60,100,170,0.18);
            border-radius: 9px; padding: 0.75rem 1rem; margin: 0.4rem 0 0.8rem 0; }
.col-h { font-size: 0.71rem; font-weight: 600; color: #3a5870 !important;
          text-transform: uppercase; letter-spacing: 0.4px; margin: 0; }
.r0  { font-size: 0.85rem; color: #8898ac !important; margin: 0; padding: 0.2rem 0; }
.r1  { font-size: 0.85rem; color: #6a7a9a !important; margin: 0; padding: 0.2rem 0; }
.r2  { font-size: 0.87rem; color: #a0b8cc !important; font-weight: 600; margin: 0; padding: 0.2rem 0; }
.r3  { font-size: 0.87rem; color: #90a8bc !important; font-weight: 600; margin: 0; padding: 0.2rem 0; }
.div { border-top: 1px solid rgba(255,255,255,0.06); margin: 0.18rem 0; }
.sub-head { font-size: 0.8rem; font-weight: 600; color: #5a7888 !important; margin: 0.8rem 0 0.4rem 0; }
.note { font-size: 0.76rem; color: #3a5060 !important; font-style: italic; margin: 0.3rem 0 0 0; }
</style>"""
st.markdown(BASE_CSS, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════
st.markdown('<p style="font-size:1.55rem;font-weight:700;color:#c4d4e4;margin:0">📊 Analisis Laporan Keuangan</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#566880;font-size:0.86rem;margin:0.3rem 0 0 0">Horizontal · Vertikal · Trend · Common Size — empat pendekatan analisis laporan keuangan UMKM.</p>', unsafe_allow_html=True)
st.markdown("---")

# ══════════════════════════════════════════════════════════════════
# DATA STUDI KASUS (3 TAHUN)
# ══════════════════════════════════════════════════════════════════
KASUS = {
    "☕  Warung Kopi Nusantara — Kuliner / F&B": {
        "deskripsi": "Kedai kopi di Metro, Lampung. Berdiri 2022 dengan modal awal Rp 30 juta (KUR). Bertumbuh pesat di tahun ke-2 dan ke-3.",
        "tahun": [2022, 2023, 2024],
        "is": {
            2022: dict(rev=85_000_000, cogs=53_000_000, opex=23_000_000, int_exp=2_000_000, tax=1_000_000),
            2023: dict(rev=120_000_000, cogs=72_000_000, opex=30_000_000, int_exp=1_500_000, tax=3_500_000),
            2024: dict(rev=185_000_000, cogs=102_000_000, opex=40_000_000, int_exp=1_500_000, tax=6_500_000),
        },
        "bs": {
            2022: dict(cash=8_000_000, ar=1_500_000, inv=6_000_000, fixed=42_000_000, cl=15_000_000, ltd=25_000_000, equity=17_500_000),
            2023: dict(cash=15_000_000, ar=2_000_000, inv=8_000_000, fixed=45_000_000, cl=12_000_000, ltd=20_000_000, equity=38_000_000),
            2024: dict(cash=28_000_000, ar=5_000_000, inv=10_000_000, fixed=55_000_000, cl=8_000_000, ltd=15_000_000, equity=75_000_000),
        },
    },
    "🧵  Batik Lampung Heritage — Fashion / Kerajinan": {
        "deskripsi": "UMKM batik khas Lampung. Di tahun ketiga berhasil mengurangi piutang macet dan memperbaiki likuiditas secara signifikan.",
        "tahun": [2022, 2023, 2024],
        "is": {
            2022: dict(rev=180_000_000, cogs=125_000_000, opex=38_000_000, int_exp=5_000_000, tax=3_000_000),
            2023: dict(rev=250_000_000, cogs=165_000_000, opex=55_000_000, int_exp=4_500_000, tax=5_500_000),
            2024: dict(rev=320_000_000, cogs=195_000_000, opex=65_000_000, int_exp=4_000_000, tax=12_000_000),
        },
        "bs": {
            2022: dict(cash=6_000_000, ar=50_000_000, inv=90_000_000, fixed=90_000_000, cl=70_000_000, ltd=90_000_000, equity=76_000_000),
            2023: dict(cash=10_000_000, ar=40_000_000, inv=80_000_000, fixed=100_000_000, cl=55_000_000, ltd=80_000_000, equity=95_000_000),
            2024: dict(cash=25_000_000, ar=32_000_000, inv=62_000_000, fixed=115_000_000, cl=40_000_000, ltd=65_000_000, equity=129_000_000),
        },
    },
}

# ══════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════
def calc_is(d):
    d = dict(d)
    d["gross"]   = d["rev"] - d["cogs"]
    d["ebit"]    = d["gross"] - d["opex"]
    d["ebt"]     = d["ebit"] - d["int_exp"]
    d["net_inc"] = d["ebt"] - d["tax"]
    return d

def calc_bs(d):
    d = dict(d)
    d["curr"]   = d["cash"] + d["ar"] + d["inv"]
    d["ta"]     = d["curr"] + d["fixed"]
    d["td"]     = d["cl"] + d["ltd"]
    d["tp"]     = d["td"] + d["equity"]
    return d

def fmt(v, mode="rp"):
    if mode == "rp":
        return f"Rp {v:,.0f}"
    elif mode == "pct":
        return f"{v:.1f}%"
    elif mode == "idx":
        return f"{v:.1f}"

def delta_color(v):
    return "#5eaa7a" if v >= 0 else "#c05858"

# IS rows: (label, key, is_subtotal)
IS_ROWS = [
    ("Penjualan / Pendapatan",     "rev",     False),
    ("Harga Pokok Penjualan",      "cogs",    False),
    ("Laba Kotor",                 "gross",   True),
    ("Beban Operasional",          "opex",    False),
    ("Laba Operasional (EBIT)",    "ebit",    True),
    ("Beban Bunga",                "int_exp", False),
    ("Laba Sebelum Pajak (EBT)",   "ebt",     True),
    ("Pajak Penghasilan",          "tax",     False),
    ("Laba Bersih",                "net_inc", True),
]

BS_ROWS = [
    ("AKTIVA",                     None,     "header"),
    ("  Kas & Setara Kas",         "cash",   False),
    ("  Piutang Usaha",            "ar",     False),
    ("  Persediaan",               "inv",    False),
    ("  Total Aktiva Lancar",      "curr",   True),
    ("  Aktiva Tetap (Bersih)",    "fixed",  False),
    ("Total Aktiva",               "ta",     True),
    ("PASIVA",                     None,     "header"),
    ("  Hutang Lancar",            "cl",     False),
    ("  Hutang Jangka Panjang",    "ltd",    False),
    ("  Total Hutang",             "td",     True),
    ("  Modal / Ekuitas",          "equity", False),
    ("Total Pasiva",               "tp",     True),
]

# ══════════════════════════════════════════════════════════════════
# MODE SELECTION
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="sec">1️⃣ Mode Input Data</div>', unsafe_allow_html=True)
mode = st.radio("", ["📚  Gunakan Studi Kasus UMKM", "✏️  Input Data Manual (2 Tahun)"],
                horizontal=True, label_visibility="collapsed")

years, is_data, bs_data, biz_name = [], {}, {}, "Bisnis"

if mode == "📚  Gunakan Studi Kasus UMKM":
    sel   = st.selectbox("Pilih studi kasus:", list(KASUS.keys()), label_visibility="collapsed")
    kasus = KASUS[sel]
    st.markdown(f'<div class="info-box"><p style="font-size:0.84rem;color:#607a94 !important;margin:0">📋 <strong style="color:#7a9ab8">Profil:</strong> {kasus["deskripsi"]}</p></div>', unsafe_allow_html=True)
    years    = kasus["tahun"]
    is_data  = {y: calc_is(kasus["is"][y]) for y in years}
    bs_data  = {y: calc_bs(kasus["bs"][y]) for y in years}
    biz_name = sel.split("—")[0].strip()

else:
    col_a, col_b = st.columns(2)
    with col_a: biz_name = st.text_input("Nama Bisnis", placeholder="Contoh: Toko Sembako Barokah")
    y1_lbl = st.text_input("Label Tahun Pertama",  value="Tahun 2023", key="y1l")
    y2_lbl = st.text_input("Label Tahun Kedua",    value="Tahun 2024", key="y2l")
    years = ["T1", "T2"]

    st.markdown('<div class="sec">2️⃣ Laporan Laba Rugi <span style="font-weight:400;color:#3a5870;font-size:0.78rem">(Rupiah)</span></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    is_raw = {}
    for yi, (col, lbl) in enumerate([(c1, y1_lbl), (c2, y2_lbl)]):
        with col:
            st.markdown(f'<p style="font-size:0.8rem;font-weight:600;color:#5a7898;margin-bottom:0.3rem">📅 {lbl}</p>', unsafe_allow_html=True)
            k = years[yi]
            is_raw[k] = dict(
                rev     = st.number_input("Penjualan",         min_value=0, value=120_000_000, step=1_000_000, format="%d", key=f"rev{k}"),
                cogs    = st.number_input("HPP",               min_value=0, value=72_000_000,  step=1_000_000, format="%d", key=f"cogs{k}"),
                opex    = st.number_input("Beban Operasional",  min_value=0, value=30_000_000,  step=500_000,   format="%d", key=f"opex{k}"),
                int_exp = st.number_input("Beban Bunga",        min_value=0, value=1_500_000,   step=100_000,   format="%d", key=f"intx{k}"),
                tax     = st.number_input("Pajak",              min_value=0, value=3_500_000,   step=100_000,   format="%d", key=f"tax{k}"),
            )
            is_data[k] = calc_is(is_raw[k])

    st.markdown('<div class="sec">3️⃣ Neraca / Balance Sheet <span style="font-weight:400;color:#3a5870;font-size:0.78rem">(Rupiah)</span></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    for yi, (col, lbl) in enumerate([(c1, y1_lbl), (c2, y2_lbl)]):
        with col:
            st.markdown(f'<p style="font-size:0.8rem;font-weight:600;color:#5a7898;margin-bottom:0.3rem">📅 {lbl}</p>', unsafe_allow_html=True)
            k = years[yi]
            bs_data[k] = calc_bs(dict(
                cash   = st.number_input("Kas",                 min_value=0, value=15_000_000, step=500_000,   format="%d", key=f"csh{k}"),
                ar     = st.number_input("Piutang Usaha",       min_value=0, value=2_000_000,  step=500_000,   format="%d", key=f"ar{k}"),
                inv    = st.number_input("Persediaan",          min_value=0, value=8_000_000,  step=500_000,   format="%d", key=f"inv{k}"),
                fixed  = st.number_input("Aktiva Tetap Bersih", min_value=0, value=45_000_000, step=1_000_000, format="%d", key=f"fix{k}"),
                cl     = st.number_input("Hutang Lancar",       min_value=1, value=12_000_000, step=500_000,   format="%d", key=f"cl{k}"),
                ltd    = st.number_input("Hutang JP",           min_value=0, value=20_000_000, step=1_000_000, format="%d", key=f"ltd{k}"),
                equity = st.number_input("Modal / Ekuitas",     min_value=1, value=38_000_000, step=1_000_000, format="%d", key=f"eq{k}"),
            ))

# ══════════════════════════════════════════════════════════════════
# TOMBOL
# ══════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔍  Analisis Laporan Keuangan"):
    st.markdown("---")
    st.markdown(f'<p style="font-size:1.25rem;font-weight:700;color:#b8cce0;margin-bottom:0.3rem">📈 Hasil Analisis — {biz_name}</p>', unsafe_allow_html=True)

    TABS = st.tabs(["📊 Horizontal", "📐 Vertikal", "📈 Trend", "🔲 Common Size"])

    # ╔══════════════════════════════════════════════════════╗
    # ║ TAB 1 — ANALISIS HORIZONTAL                         ║
    # ╚══════════════════════════════════════════════════════╝
    with TABS[0]:
        st.markdown('<div class="sec">📊 Analisis Horizontal</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">Definisi:</strong> Membandingkan setiap pos laporan keuangan antar periode untuk melihat besarnya perubahan dalam Rupiah maupun persentase. Positif (+) berarti naik, negatif (−) berarti turun.</p></div>', unsafe_allow_html=True)

        pairs = [(years[i], years[i+1]) for i in range(len(years)-1)]

        for (ya, yb) in pairs:
            isa, isb = is_data[ya], is_data[yb]
            bsa, bsb = bs_data[ya], bs_data[yb]

            # Header judul
            n_cols = 5
            st.markdown(f'<p class="sub-head">📋 Perbandingan {ya} → {yb}</p>', unsafe_allow_html=True)

            # IS Table
            st.markdown('<p style="font-size:0.8rem;font-weight:600;color:#4a6a80;margin-bottom:0.3rem">Laporan Laba Rugi</p>', unsafe_allow_html=True)
            hc = st.columns([3, 2, 2, 1.8, 1.8])
            for col, hdr in zip(hc, ["Pos", str(ya), str(yb), "Δ Rupiah", "Δ %"]):
                col.markdown(f'<p class="col-h">{hdr}</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

            for label, key, is_sub in IS_ROWS:
                if key is None: continue
                v1, v2 = isa[key], isb[key]
                drp = v2 - v1
                dpct = drp / abs(v1) * 100 if v1 != 0 else 0
                style = "r2" if is_sub else "r0"
                rc = st.columns([3, 2, 2, 1.8, 1.8])
                rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
                rc[1].markdown(f'<p class="r1">{fmt(v1)}</p>', unsafe_allow_html=True)
                rc[2].markdown(f'<p class="r2">{fmt(v2)}</p>', unsafe_allow_html=True)
                rc[3].markdown(f'<p style="font-size:0.84rem;color:{delta_color(drp)};margin:0;padding:0.2rem 0">{fmt(drp)}</p>', unsafe_allow_html=True)
                rc[4].markdown(f'<p style="font-size:0.84rem;color:{delta_color(dpct)};font-weight:600;margin:0;padding:0.2rem 0">{dpct:+.1f}%</p>', unsafe_allow_html=True)
                st.markdown('<div class="div"></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # BS Table
            st.markdown('<p style="font-size:0.8rem;font-weight:600;color:#4a6a80;margin-bottom:0.3rem">Neraca</p>', unsafe_allow_html=True)
            hc = st.columns([3, 2, 2, 1.8, 1.8])
            for col, hdr in zip(hc, ["Pos", str(ya), str(yb), "Δ Rupiah", "Δ %"]):
                col.markdown(f'<p class="col-h">{hdr}</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

            for label, key, tp in BS_ROWS:
                if tp == "header":
                    st.markdown(f'<p style="font-size:0.78rem;font-weight:700;color:#3a5870;margin:0.5rem 0 0.2rem 0;text-transform:uppercase">{label}</p>', unsafe_allow_html=True)
                    continue
                v1, v2 = bsa[key], bsb[key]
                drp = v2 - v1
                dpct = drp / abs(v1) * 100 if v1 != 0 else 0
                style = "r2" if tp else "r0"
                rc = st.columns([3, 2, 2, 1.8, 1.8])
                rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
                rc[1].markdown(f'<p class="r1">{fmt(v1)}</p>', unsafe_allow_html=True)
                rc[2].markdown(f'<p class="r2">{fmt(v2)}</p>', unsafe_allow_html=True)
                rc[3].markdown(f'<p style="font-size:0.84rem;color:{delta_color(drp)};margin:0;padding:0.2rem 0">{fmt(drp)}</p>', unsafe_allow_html=True)
                rc[4].markdown(f'<p style="font-size:0.84rem;color:{delta_color(dpct)};font-weight:600;margin:0;padding:0.2rem 0">{dpct:+.1f}%</p>', unsafe_allow_html=True)
                st.markdown('<div class="div"></div>', unsafe_allow_html=True)

    # ╔══════════════════════════════════════════════════════╗
    # ║ TAB 2 — ANALISIS VERTIKAL                           ║
    # ╚══════════════════════════════════════════════════════╝
    with TABS[1]:
        st.markdown('<div class="sec">📐 Analisis Vertikal</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">Definisi:</strong> Menyatakan setiap pos laporan keuangan sebagai persentase dari angka dasar: <strong>Penjualan</strong> untuk Laporan L/R, dan <strong>Total Aktiva</strong> untuk Neraca. Membantu melihat struktur biaya dan komposisi aset.</p></div>', unsafe_allow_html=True)

        # IS Vertikal
        st.markdown('<p class="sub-head">Laporan Laba Rugi — % dari Penjualan</p>', unsafe_allow_html=True)
        hc = st.columns([3] + [1.5]*len(years))
        hc[0].markdown('<p class="col-h">Pos Laporan</p>', unsafe_allow_html=True)
        for i, y in enumerate(years):
            hc[i+1].markdown(f'<p class="col-h">{y} (%)</p>', unsafe_allow_html=True)
        st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        for label, key, is_sub in IS_ROWS:
            style = "r2" if is_sub else "r0"
            rc = st.columns([3] + [1.5]*len(years))
            rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
            for i, y in enumerate(years):
                v   = is_data[y][key]
                rev = is_data[y]["rev"]
                pct = v / rev * 100 if rev > 0 else 0
                rc[i+1].markdown(f'<p class="r2">{pct:.1f}%</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # BS Vertikal
        st.markdown('<p class="sub-head">Neraca — % dari Total Aktiva</p>', unsafe_allow_html=True)
        hc = st.columns([3] + [1.5]*len(years))
        hc[0].markdown('<p class="col-h">Pos Neraca</p>', unsafe_allow_html=True)
        for i, y in enumerate(years):
            hc[i+1].markdown(f'<p class="col-h">{y} (%)</p>', unsafe_allow_html=True)
        st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        for label, key, tp in BS_ROWS:
            if tp == "header":
                st.markdown(f'<p style="font-size:0.78rem;font-weight:700;color:#3a5870;margin:0.5rem 0 0.2rem 0;text-transform:uppercase">{label}</p>', unsafe_allow_html=True)
                continue
            style = "r2" if tp else "r0"
            rc = st.columns([3] + [1.5]*len(years))
            rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
            for i, y in enumerate(years):
                v  = bs_data[y][key]
                ta = bs_data[y]["ta"]
                pct = v / ta * 100 if ta > 0 else 0
                rc[i+1].markdown(f'<p class="r2">{pct:.1f}%</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        # Grafik komposisi IS
        st.markdown('<p class="sub-head" style="margin-top:1.2rem">Grafik Struktur Biaya (% Penjualan)</p>', unsafe_allow_html=True)
        fig_v = go.Figure()
        items_v = [("HPP", "cogs"), ("Beban Operasional", "opex"), ("Bunga + Pajak", "int_exp"), ("Laba Bersih", "net_inc")]
        colors_v = ["#4a6a90", "#6a5a90", "#8a5a70", "#4a9a6a"]
        for (lbl, key), col in zip(items_v, colors_v):
            vals = [is_data[y][key] / is_data[y]["rev"] * 100 for y in years]
            fig_v.add_trace(go.Bar(name=lbl, x=[str(y) for y in years], y=vals, marker_color=col, opacity=0.78))
        fig_v.update_layout(
            barmode="stack", template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            height=300, margin=dict(l=10, r=10, t=20, b=30),
            legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
            yaxis=dict(ticksuffix="%", tickfont=dict(size=9, color="#5a6880"), gridcolor="rgba(255,255,255,0.05)"),
            xaxis=dict(tickfont=dict(size=11, color="#6878a0")),
        )
        st.plotly_chart(fig_v, use_container_width=True)

    # ╔══════════════════════════════════════════════════════╗
    # ║ TAB 3 — ANALISIS TREND                              ║
    # ╚══════════════════════════════════════════════════════╝
    with TABS[2]:
        st.markdown('<div class="sec">📈 Analisis Trend (Angka Indeks)</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="concept"><p><strong style="color:#8090b0">Definisi:</strong> Menggunakan angka indeks untuk melihat perkembangan jangka panjang. Tahun dasar = <strong>{years[0]}</strong> ditetapkan sebagai 100. Indeks > 100 berarti tumbuh, &lt; 100 berarti turun dibanding tahun dasar.</p></div>', unsafe_allow_html=True)

        base_y = years[0]

        # IS Trend
        st.markdown('<p class="sub-head">Laporan Laba Rugi — Indeks (Tahun Dasar = 100)</p>', unsafe_allow_html=True)
        hc = st.columns([3] + [1.5]*len(years))
        hc[0].markdown('<p class="col-h">Pos</p>', unsafe_allow_html=True)
        for i, y in enumerate(years):
            lbl = f"{y} (Dasar)" if y == base_y else str(y)
            hc[i+1].markdown(f'<p class="col-h">{lbl}</p>', unsafe_allow_html=True)
        st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        for label, key, is_sub in IS_ROWS:
            style = "r2" if is_sub else "r0"
            rc = st.columns([3] + [1.5]*len(years))
            rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
            base_v = is_data[base_y][key]
            for i, y in enumerate(years):
                v = is_data[y][key]
                idx = v / base_v * 100 if base_v != 0 else 0
                col_c = "#5a6880" if y == base_y else (delta_color(idx - 100))
                rc[i+1].markdown(f'<p style="font-size:0.87rem;color:{col_c};font-weight:600;margin:0;padding:0.2rem 0">{idx:.0f}</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        # Grafik Trend
        st.markdown('<p class="sub-head" style="margin-top:1.2rem">Grafik Trend Pos Utama</p>', unsafe_allow_html=True)
        trend_keys = [("Penjualan", "rev", "#6a9ad8"), ("Laba Kotor", "gross", "#5eaa7a"), ("Laba Bersih", "net_inc", "#b8a848")]
        fig_t = go.Figure()
        for label, key, col in trend_keys:
            base_v = is_data[base_y][key]
            idxs = [is_data[y][key] / base_v * 100 if base_v != 0 else 0 for y in years]
            fig_t.add_trace(go.Scatter(
                name=label, x=[str(y) for y in years], y=idxs,
                mode="lines+markers", line=dict(color=col, width=2),
                marker=dict(size=7, color=col)
            ))
        fig_t.add_hline(y=100, line_dash="dot", line_color="rgba(255,255,255,0.2)",
                        annotation_text="Dasar (100)", annotation_font_color="#3a5060")
        fig_t.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            height=300, margin=dict(l=10, r=10, t=20, b=30),
            legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
            yaxis=dict(tickfont=dict(size=9, color="#5a6880"), gridcolor="rgba(255,255,255,0.05)"),
            xaxis=dict(tickfont=dict(size=11, color="#6878a0")),
        )
        st.plotly_chart(fig_t, use_container_width=True)
        st.markdown(f'<p class="note">Contoh baca: Indeks Laba Bersih tahun {years[-1]} = {is_data[years[-1]]["net_inc"]/is_data[base_y]["net_inc"]*100:.0f} berarti laba bersih tumbuh {is_data[years[-1]]["net_inc"]/is_data[base_y]["net_inc"]*100-100:.0f}% dibanding tahun {years[0]}.</p>', unsafe_allow_html=True)

    # ╔══════════════════════════════════════════════════════╗
    # ║ TAB 4 — ANALISIS COMMON SIZE                        ║
    # ╚══════════════════════════════════════════════════════╝
    with TABS[3]:
        st.markdown('<div class="sec">🔲 Analisis Common Size</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">Definisi:</strong> Menyajikan laporan keuangan dalam persentase sehingga mudah dibandingkan antar perusahaan berbeda ukuran. Kolom Benchmark menunjukkan kisaran umum UMKM sejenis sebagai acuan perbandingan.</p></div>', unsafe_allow_html=True)

        # Benchmark UMKM (approximate, for educational purposes)
        IS_BENCH = {
            "cogs":    "55–75%",  "gross": "25–45%",  "opex":    "15–30%",
            "ebit":    "8–18%",   "int_exp":"1–5%",   "ebt":     "7–16%",
            "tax":     "1–5%",    "net_inc":"5–15%",
        }
        BS_BENCH = {
            "cash":   "5–15%",  "ar":     "5–20%",  "inv":    "8–25%",
            "curr":   "20–40%", "fixed":  "45–65%", "ta":     "100%",
            "cl":     "15–35%", "ltd":    "15–35%", "td":     "30–55%",
            "equity": "40–65%", "tp":     "100%",
        }

        latest_y = years[-1]
        is_l     = is_data[latest_y]
        bs_l     = bs_data[latest_y]

        # IS Common Size
        st.markdown(f'<p class="sub-head">L/R Common Size — {latest_y} vs Benchmark UMKM (% dari Penjualan)</p>', unsafe_allow_html=True)
        hc = st.columns([3, 1.8, 2.5, 3])
        for col, hdr in zip(hc, ["Pos", f"{latest_y} (%)", "Benchmark UMKM", "Keterangan"]):
            col.markdown(f'<p class="col-h">{hdr}</p>', unsafe_allow_html=True)
        st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        ket_is = {
            "cogs": "Biaya bahan baku + produksi", "gross": "Sisa setelah biaya produksi",
            "opex": "Biaya operasional (gaji, sewa, dll)", "ebit": "Laba sebelum bunga & pajak",
            "int_exp": "Beban pinjaman", "ebt": "Laba sebelum pajak",
            "tax": "Kewajiban pajak penghasilan", "net_inc": "Laba final untuk pemilik",
        }
        for label, key, is_sub in IS_ROWS:
            style = "r2" if is_sub else "r0"
            v = is_l[key]; rev = is_l["rev"]
            pct = v / rev * 100 if rev > 0 else 0
            bench = IS_BENCH.get(key, "—")
            rc = st.columns([3, 1.8, 2.5, 3])
            rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
            rc[1].markdown(f'<p class="r2">{pct:.1f}%</p>', unsafe_allow_html=True)
            rc[2].markdown(f'<p style="font-size:0.82rem;color:#4a6a80 !important;margin:0;padding:0.2rem 0">{bench}</p>', unsafe_allow_html=True)
            rc[3].markdown(f'<p style="font-size:0.78rem;color:#3a5060 !important;margin:0;padding:0.2rem 0;font-style:italic">{ket_is.get(key,"")}</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # BS Common Size
        st.markdown(f'<p class="sub-head">Neraca Common Size — {latest_y} vs Benchmark UMKM (% dari Total Aktiva)</p>', unsafe_allow_html=True)
        hc = st.columns([3, 1.8, 2.5, 3])
        for col, hdr in zip(hc, ["Pos", f"{latest_y} (%)", "Benchmark UMKM", "Keterangan"]):
            col.markdown(f'<p class="col-h">{hdr}</p>', unsafe_allow_html=True)
        st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        ket_bs = {
            "cash": "Likuiditas jangka pendek", "ar": "Piutang dari pelanggan",
            "inv": "Stok barang / bahan baku", "curr": "Aset cair jangka pendek",
            "fixed": "Peralatan, bangunan, kendaraan", "ta": "Keseluruhan aset",
            "cl": "Kewajiban dalam 1 tahun", "ltd": "Pinjaman jangka panjang",
            "td": "Total seluruh kewajiban", "equity": "Hak pemilik atas aset",
            "tp": "Sama dengan total aktiva",
        }
        for label, key, tp in BS_ROWS:
            if tp == "header":
                st.markdown(f'<p style="font-size:0.78rem;font-weight:700;color:#3a5870;margin:0.5rem 0 0.2rem 0;text-transform:uppercase">{label}</p>', unsafe_allow_html=True)
                continue
            style = "r2" if tp else "r0"
            v  = bs_l[key]; ta = bs_l["ta"]
            pct = v / ta * 100 if ta > 0 else 0
            bench = BS_BENCH.get(key, "—")
            rc = st.columns([3, 1.8, 2.5, 3])
            rc[0].markdown(f'<p class="{style}">{label}</p>', unsafe_allow_html=True)
            rc[1].markdown(f'<p class="r2">{pct:.1f}%</p>', unsafe_allow_html=True)
            rc[2].markdown(f'<p style="font-size:0.82rem;color:#4a6a80 !important;margin:0;padding:0.2rem 0">{bench}</p>', unsafe_allow_html=True)
            rc[3].markdown(f'<p style="font-size:0.78rem;color:#3a5060 !important;margin:0;padding:0.2rem 0;font-style:italic">{ket_bs.get(key,"")}</p>', unsafe_allow_html=True)
            st.markdown('<div class="div"></div>', unsafe_allow_html=True)

        st.markdown('<p class="note" style="margin-top:0.6rem">⚠️ Benchmark di atas adalah perkiraan kisaran umum untuk UMKM. Angka ideal bervariasi tergantung jenis industri, skala bisnis, dan kondisi ekonomi. Verifikasi dengan data industri yang relevan.</p>', unsafe_allow_html=True)

    # ── PDF EXPORT ────────────────────────────────────────────────
    st.markdown("---")
    st.markdown('<p style="font-size:0.82rem;color:#3a5870 !important;margin-bottom:0.5rem">📄 Unduh laporan analisis laporan keuangan (Horizontal, Vertikal, Trend, Common Size) dalam format PDF.</p>', unsafe_allow_html=True)

    def _buat_pdf_lk():
        import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from utils import BisnisKuPDF
        import datetime
        pdf = BisnisKuPDF(f"Analisis Laporan Keuangan — {biz_name}")
        pdf.add_page()

        pdf.section("Informasi Bisnis")
        pdf.kv("Nama Bisnis",   biz_name)
        pdf.kv("Periode Data",  " | ".join(str(y) for y in years))
        pdf.kv("Tahun Dasar",   str(years[0]))
        pdf.kv("Tanggal Cetak", datetime.datetime.now().strftime("%d %B %Y %H:%M"))

        # Analisis Horizontal
        base_y = years[0]
        if len(years) >= 2:
            ya, yb = years[0], years[1]
            isa, isb = is_data[ya], is_data[yb]
            pdf.section(f"Analisis Horizontal — L/R: {ya} vs {yb}")
            pdf.th(["Pos Laporan L/R", str(ya), str(yb), "Delta (Rp)", "Delta (%)"],
                   [55, 32, 32, 36, 27])
            for i,(lbl,key,is_sub) in enumerate(IS_ROWS):
                v1, v2 = isa[key], isb[key]
                d  = v2 - v1
                dp = d/abs(v1)*100 if v1!=0 else 0
                sign = "+" if dp>=0 else ""
                pdf.tr([lbl, f"Rp{v1//1000:,}K", f"Rp{v2//1000:,}K",
                        f"Rp{d//1000:,}K", f"{sign}{dp:.1f}%"],
                       [55,32,32,36,27], even=i%2==0, bold=is_sub)

        # Analisis Vertikal
        pdf.section("Analisis Vertikal — L/R (% dari Penjualan)")
        hdr_v = ["Pos L/R"] + [str(y) for y in years]
        wds_v = [65] + [25]*len(years) + [0]
        wds_v = [65] + [int((182-65)/len(years))]*len(years)
        pdf.th(hdr_v, wds_v)
        for i,(lbl,key,is_sub) in enumerate(IS_ROWS):
            row = [lbl]
            for y in years:
                v   = is_data[y][key]
                rev = is_data[y]["rev"]
                pct = v/rev*100 if rev>0 else 0
                row.append(f"{pct:.1f}%")
            pdf.tr(row, wds_v, even=i%2==0, bold=is_sub)

        # Analisis Trend
        pdf.section(f"Analisis Trend — Indeks (Tahun Dasar {years[0]} = 100)")
        pdf.th(["Pos L/R"] + [str(y) for y in years], wds_v)
        for i,(lbl,key,is_sub) in enumerate(IS_ROWS):
            base_v = is_data[years[0]][key]
            row = [lbl]
            for y in years:
                idx = is_data[y][key]/base_v*100 if base_v!=0 else 0
                row.append(f"{idx:.0f}")
            pdf.tr(row, wds_v, even=i%2==0, bold=is_sub)
        pdf.note("Indeks > 100 = tumbuh; < 100 = menurun dibanding tahun dasar.")

        return pdf.build()

    import datetime as _dt
    fname_lk = f"BisnisKu_Analisis_LK_{biz_name.replace(' ','_')}_{_dt.date.today()}.pdf"
    st.download_button(
        label="📄 Unduh Laporan Analisis Laporan Keuangan (PDF)",
        data=_buat_pdf_lk(),
        file_name=fname_lk,
        mime="application/pdf",
    )
