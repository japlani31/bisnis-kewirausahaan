import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Simulasi Keuangan", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.04) !important; border-right: 1px solid rgba(255,255,255,0.08); }
section[data-testid="stSidebar"] * { color: #e0e0e0 !important; }
h1,h2,h3 { color: white !important; }
p, li, label { color: rgba(255,255,255,0.8) !important; }

/* INPUT WARNA HITAM */
.stTextInput input,
.stNumberInput input,
.stSelectbox select,
.stTextArea textarea {
    background: #ffffff !important;
    color: #111111 !important;
    border: 1.5px solid rgba(255,255,255,0.35) !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
}
.stTextInput input::placeholder,
.stTextArea textarea::placeholder { color: #888 !important; }
div[data-baseweb="select"] > div { background: #ffffff !important; color: #111111 !important; border-radius: 8px !important; }
div[data-baseweb="select"] span { color: #111111 !important; }

.metric-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
    margin-bottom: 0.5rem;
}
.metric-value { font-size: 1.4rem; font-weight: 800; color: #f9c74f; }
.metric-label { font-size: 0.75rem; color: rgba(255,255,255,0.5); margin-top: 0.25rem; }
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.35rem;
    font-weight: 800;
    color: white;
    margin: 1.5rem 0 0.75rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(249,199,79,0.4);
}
.info-box {
    background: rgba(72,199,142,0.1);
    border: 1px solid rgba(72,199,142,0.3);
    border-radius: 12px; padding: 1rem 1.25rem; margin: 0.5rem 0;
}
.warning-box {
    background: rgba(249,115,22,0.1);
    border: 1px solid rgba(249,115,22,0.3);
    border-radius: 12px; padding: 1rem 1.25rem; margin: 0.5rem 0;
}
.danger-box {
    background: rgba(249,65,68,0.1);
    border: 1px solid rgba(249,65,68,0.3);
    border-radius: 12px; padding: 1rem 1.25rem; margin: 0.5rem 0;
}
.tab-content { padding: 1rem 0; }
.stButton button {
    background: linear-gradient(90deg, #f9c74f, #f3722c) !important;
    color: #1a1a2e !important; font-weight: 700 !important;
    border: none !important; border-radius: 10px !important;
    padding: 0.6rem 2rem !important; font-size: 1rem !important;
}
.rasio-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px; padding: 1rem; margin-bottom: 0.5rem;
}
.rasio-val { font-size: 1.3rem; font-weight: 700; }
.rasio-lbl { font-size: 0.78rem; color: rgba(255,255,255,0.5); }
.rasio-status { font-size: 0.78rem; margin-top: 0.2rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-family:Syne,sans-serif;font-size:2rem;font-weight:800;background:linear-gradient(90deg,#f9c74f,#f3722c);-webkit-background-clip:text;-webkit-text-fill-color:transparent">📊 Simulasi Keuangan Bisnis</p>', unsafe_allow_html=True)
st.markdown('<p style="color:rgba(255,255,255,0.6)">Analisis lengkap: BEP, Cashflow, HPP, Rasio Keuangan, NPV, IRR, Capital Budgeting, Modal Kerja & lebih banyak lagi.</p>', unsafe_allow_html=True)
st.markdown("---")

# ══════════════════════════════════════════════════════════════════
# INPUT DATA
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="section-title">1️⃣ Informasi Dasar Bisnis</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    nama_bisnis = st.text_input("Nama Bisnis", placeholder="Contoh: Warung Kopi Nusantara")
    jenis_bisnis = st.selectbox("Jenis Bisnis", ["Kuliner/F&B","Fashion/Pakaian","Jasa/Servis","Teknologi/Digital","Pendidikan","Retail/Toko","Lainnya"])
with col2:
    modal_awal = st.number_input("Modal Awal / Investasi (Rp)", min_value=0, value=50000000, step=1000000, format="%d")
    periode = st.selectbox("Periode Proyeksi", ["6 Bulan","12 Bulan","24 Bulan","60 Bulan (5 Tahun)"])

st.markdown('<div class="section-title">2️⃣ HPP — Harga Pokok Produksi</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Rincian komponen biaya untuk membuat satu unit produk/jasa</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    bahan_baku = st.number_input("Bahan Baku per Unit (Rp)", min_value=0, value=8000, step=500, format="%d")
    tenaga_kerja_langsung = st.number_input("Tenaga Kerja Langsung per Unit (Rp)", min_value=0, value=2000, step=500, format="%d")
with col2:
    overhead_pabrik = st.number_input("Overhead Pabrik per Unit (Rp)", min_value=0, value=1500, step=500, format="%d")
    biaya_packing = st.number_input("Biaya Packing/Distribusi per Unit (Rp)", min_value=0, value=500, step=100, format="%d")
with col3:
    hpp_total = bahan_baku + tenaga_kerja_langsung + overhead_pabrik + biaya_packing
    st.markdown(f"""<div class="metric-card" style="margin-top:1.8rem">
        <div class="metric-value">Rp {hpp_total:,.0f}</div>
        <div class="metric-label">Total HPP per Unit</div>
    </div>""", unsafe_allow_html=True)
    harga_jual = st.number_input("Harga Jual per Unit (Rp)", min_value=0, value=25000, step=1000, format="%d")

st.markdown('<div class="section-title">3️⃣ Biaya Tetap Bulanan</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    sewa       = st.number_input("Sewa Tempat (Rp/bln)", min_value=0, value=1500000, step=100000, format="%d")
    gaji       = st.number_input("Gaji Karyawan (Rp/bln)", min_value=0, value=3000000, step=100000, format="%d")
with col2:
    listrik    = st.number_input("Listrik & Air (Rp/bln)", min_value=0, value=400000, step=50000, format="%d")
    internet   = st.number_input("Internet/Telepon (Rp/bln)", min_value=0, value=200000, step=50000, format="%d")
with col3:
    depresiasi = st.number_input("Depresiasi Aset (Rp/bln)", min_value=0, value=500000, step=100000, format="%d")
    biaya_tetap_lain = st.number_input("Biaya Tetap Lain (Rp/bln)", min_value=0, value=400000, step=100000, format="%d")

total_biaya_tetap = sewa + gaji + listrik + internet + depresiasi + biaya_tetap_lain

st.markdown('<div class="section-title">4️⃣ Volume Penjualan & Pertumbuhan</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    estimasi_penjualan = st.number_input("Estimasi Penjualan/Bulan (unit)", min_value=1, value=400, step=10, format="%d")
with col2:
    pertumbuhan = st.slider("Pertumbuhan Penjualan (%/bulan)", 0, 20, 5)
with col3:
    discount_rate = st.slider("Discount Rate / WACC (%/tahun)", 1, 30, 12,
        help="Digunakan untuk menghitung NPV. Umumnya 10-15% untuk UMKM.")

st.markdown('<div class="section-title">5️⃣ Data Neraca & Modal Kerja</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    kas          = st.number_input("Kas & Setara Kas (Rp)", min_value=0, value=10000000, step=500000, format="%d")
    piutang      = st.number_input("Piutang Usaha (Rp)", min_value=0, value=5000000, step=500000, format="%d")
    persediaan   = st.number_input("Persediaan/Stok (Rp)", min_value=0, value=8000000, step=500000, format="%d")
with col2:
    aktiva_tetap = st.number_input("Aktiva Tetap Bersih (Rp)", min_value=0, value=30000000, step=1000000, format="%d")
    hutang_lancar= st.number_input("Hutang Lancar (Rp)", min_value=0, value=6000000, step=500000, format="%d")
    hutang_jangka_panjang = st.number_input("Hutang Jangka Panjang (Rp)", min_value=0, value=15000000, step=1000000, format="%d")
with col3:
    ekuitas      = st.number_input("Modal / Ekuitas (Rp)", min_value=1, value=modal_awal, step=1000000, format="%d")
    suku_bunga_hutang = st.slider("Suku Bunga Hutang (%/tahun)", 0, 30, 10,
        help="Bunga pinjaman bank atau kreditur")

# ══════════════════════════════════════════════════════════════════
# TOMBOL HITUNG
# ══════════════════════════════════════════════════════════════════
if st.button("🚀 Hitung Analisis Lengkap!"):

    margin_per_unit = harga_jual - hpp_total
    pendapatan_bulan1 = harga_jual * estimasi_penjualan
    biaya_variabel_total = hpp_total * estimasi_penjualan
    laba_kotor = pendapatan_bulan1 - biaya_variabel_total
    laba_bersih = laba_kotor - total_biaya_tetap
    gross_margin_pct = (laba_kotor / pendapatan_bulan1 * 100) if pendapatan_bulan1 > 0 else 0

    if harga_jual <= hpp_total:
        st.markdown('<div class="danger-box">🚨 <strong>PERINGATAN KRITIS:</strong> Harga jual lebih rendah dari HPP! Setiap unit yang dijual akan merugi.</div>', unsafe_allow_html=True)

    # BEP
    bep_unit   = (total_biaya_tetap / margin_per_unit) if margin_per_unit > 0 else 0
    bep_rupiah = bep_unit * harga_jual

    # ROI & Payback
    roi     = (laba_bersih / modal_awal * 100) if modal_awal > 0 else 0
    payback = (modal_awal / laba_bersih) if laba_bersih > 0 else 999

    # ─── PROYEKSI CASHFLOW ───────────────────────────────────────
    bulan_map = {"6 Bulan":6,"12 Bulan":12,"24 Bulan":24,"60 Bulan (5 Tahun)":60}
    n_bulan = bulan_map[periode]
    r_monthly = discount_rate / 100 / 12

    bulan_list, pend_list, biaya_list, laba_list, kumul_list, dcf_list = [], [], [], [], [], []
    kumulatif = -modal_awal
    npv = -modal_awal
    cashflows = [-modal_awal]

    for i in range(1, n_bulan + 1):
        faktor  = (1 + pertumbuhan / 100) ** (i - 1)
        unit_i  = estimasi_penjualan * faktor
        pend_i  = harga_jual * unit_i
        var_i   = hpp_total * unit_i
        laba_i  = pend_i - var_i - total_biaya_tetap
        kumulatif += laba_i
        pv_cf   = laba_i / ((1 + r_monthly) ** i)
        npv    += pv_cf

        bulan_list.append(f"Bln {i}")
        pend_list.append(round(pend_i))
        biaya_list.append(round(var_i + total_biaya_tetap))
        laba_list.append(round(laba_i))
        kumul_list.append(round(kumulatif))
        dcf_list.append(round(pv_cf))
        cashflows.append(laba_i)

    df = pd.DataFrame({
        "Bulan": bulan_list,
        "Pendapatan": pend_list,
        "Total Biaya": biaya_list,
        "Laba Bersih": laba_list,
        "Kumulatif": kumul_list,
        "PV CashFlow": dcf_list
    })

    # IRR (Newton-Raphson sederhana)
    def hitung_irr(cfs, guess=0.01):
        r = guess
        for _ in range(1000):
            npv_r = sum(cf / (1 + r) ** t for t, cf in enumerate(cfs))
            dnpv  = sum(-t * cf / (1 + r) ** (t + 1) for t, cf in enumerate(cfs))
            if dnpv == 0:
                break
            r_new = r - npv_r / dnpv
            if abs(r_new - r) < 1e-7:
                return r_new
            r = r_new
        return r

    try:
        irr_monthly = hitung_irr(cashflows)
        irr_annual  = ((1 + irr_monthly) ** 12 - 1) * 100
    except:
        irr_annual = 0

    # ─── ANALISIS RASIO ──────────────────────────────────────────
    aktiva_lancar  = kas + piutang + persediaan
    total_aktiva   = aktiva_lancar + aktiva_tetap
    total_hutang   = hutang_lancar + hutang_jangka_panjang
    current_ratio  = (aktiva_lancar / hutang_lancar) if hutang_lancar > 0 else 999
    quick_ratio    = ((aktiva_lancar - persediaan) / hutang_lancar) if hutang_lancar > 0 else 999
    debt_to_equity = (total_hutang / ekuitas) if ekuitas > 0 else 0
    debt_ratio     = (total_hutang / total_aktiva) if total_aktiva > 0 else 0
    pendapatan_tahunan = pendapatan_bulan1 * 12
    laba_bersih_tahunan = laba_bersih * 12
    net_profit_margin = (laba_bersih / pendapatan_bulan1 * 100) if pendapatan_bulan1 > 0 else 0
    roa = (laba_bersih_tahunan / total_aktiva * 100) if total_aktiva > 0 else 0
    roe = (laba_bersih_tahunan / ekuitas * 100) if ekuitas > 0 else 0
    asset_turnover = (pendapatan_tahunan / total_aktiva) if total_aktiva > 0 else 0
    inventory_turnover = (biaya_variabel_total * 12 / persediaan) if persediaan > 0 else 0
    dso = (piutang / (pendapatan_tahunan / 365)) if pendapatan_tahunan > 0 else 0  # Days Sales Outstanding

    # ─── TIME VALUE OF MONEY ─────────────────────────────────────
    r_tahunan = discount_rate / 100
    fv_5yr  = modal_awal * (1 + r_tahunan) ** 5
    pv_val  = modal_awal / (1 + r_tahunan) ** 5
    # Anuitas: laba bersih per tahun selama n tahun
    laba_tahunan = laba_bersih * 12
    if r_tahunan > 0 and n_bulan >= 12:
        n_tahun = n_bulan // 12
        pvifa   = (1 - (1 + r_tahunan) ** (-n_tahun)) / r_tahunan
        pv_anuitas = laba_tahunan * pvifa
    else:
        pv_anuitas = laba_tahunan * (n_bulan / 12)

    # ─── MODAL KERJA ─────────────────────────────────────────────
    modal_kerja_bersih = aktiva_lancar - hutang_lancar
    kas_minimum = total_biaya_tetap * 2  # aturan praktis: 2 bulan biaya tetap
    kas_surplus  = kas - kas_minimum
    piutang_hari = dso

    # ─── SUMBER PEMBIAYAAN ───────────────────────────────────────
    beban_bunga_tahunan = hutang_jangka_panjang * suku_bunga_hutang / 100
    interest_coverage   = (laba_bersih_tahunan / beban_bunga_tahunan) if beban_bunga_tahunan > 0 else 999
    wacc_approx = (ekuitas / (ekuitas + total_hutang)) * discount_rate + \
                  (total_hutang / (ekuitas + total_hutang)) * suku_bunga_hutang * 0.8  # asumsi tax 20%

    # ─── ANALISIS RISIKO ─────────────────────────────────────────
    operating_leverage = (laba_kotor / laba_bersih) if laba_bersih > 0 else 0
    margin_of_safety_unit = estimasi_penjualan - bep_unit
    margin_of_safety_pct  = (margin_of_safety_unit / estimasi_penjualan * 100) if estimasi_penjualan > 0 else 0

    # Skenario analisis
    skenario = {
        "Pesimis (-20%)": laba_bersih * 0.8 - total_biaya_tetap * 0.05,
        "Normal (100%)":  laba_bersih,
        "Optimis (+20%)": laba_bersih * 1.2 + total_biaya_tetap * 0.05,
    }

    # ══════════════════════════════════════════════════════════════
    # TAMPILKAN HASIL
    # ══════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown('<p style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:800;color:white">📈 Hasil Analisis Lengkap</p>', unsafe_allow_html=True)

    tabs = st.tabs(["🏠 Ringkasan","📊 Cashflow & Grafik","📐 Analisis Rasio","⏳ Time Value of Money","💼 Capital Budgeting","🏦 Modal Kerja & Kas","💳 Sumber Pembiayaan","⚠️ Risiko & Return"])

    # ── TAB 1: RINGKASAN ─────────────────────────────────────────
    with tabs[0]:
        col1,col2,col3,col4 = st.columns(4)
        cards = [
            (f"Rp {laba_bersih:,.0f}", "Laba Bersih/Bulan"),
            (f"{bep_unit:,.0f} unit", "BEP per Bulan"),
            (f"{roi:.1f}%", "ROI per Bulan"),
            (f"{payback:.1f} bln" if payback < 200 else "N/A", "Payback Period"),
        ]
        for col, (val, lbl) in zip([col1,col2,col3,col4], cards):
            with col:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{val}</div><div class="metric-label">{lbl}</div></div>', unsafe_allow_html=True)

        col1,col2,col3,col4 = st.columns(4)
        cards2 = [
            (f"Rp {hpp_total:,.0f}", "HPP per Unit"),
            (f"{gross_margin_pct:.1f}%", "Gross Margin"),
            (f"Rp {npv:,.0f}", f"NPV ({periode})"),
            (f"{irr_annual:.1f}%/thn", "IRR"),
        ]
        for col, (val, lbl) in zip([col1,col2,col3,col4], cards2):
            with col:
                st.markdown(f'<div class="metric-card"><div class="metric-value">{val}</div><div class="metric-label">{lbl}</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        # Kesimpulan kelayakan
        layak = npv > 0 and irr_annual > discount_rate and laba_bersih > 0
        if layak:
            st.markdown(f"""<div class="info-box">✅ <strong>Bisnis {nama_bisnis or 'Anda'} dinilai LAYAK secara finansial.</strong><br>
            NPV positif (Rp {npv:,.0f}), IRR ({irr_annual:.1f}%) > Discount Rate ({discount_rate}%), dan laba bersih positif.</div>""", unsafe_allow_html=True)
        elif laba_bersih > 0:
            st.markdown(f"""<div class="warning-box">🟡 <strong>Bisnis menghasilkan laba, namun perlu evaluasi lebih lanjut.</strong><br>
            Periksa NPV dan IRR — pastikan return melebihi biaya modal Anda.</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="danger-box">❌ <strong>Bisnis saat ini tidak layak.</strong> Tinjau kembali struktur biaya dan harga jual.</div>""", unsafe_allow_html=True)

    # ── TAB 2: CASHFLOW & GRAFIK ─────────────────────────────────
    with tabs[1]:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(name="Pendapatan", x=df["Bulan"], y=df["Pendapatan"], marker_color="#f9c74f", opacity=0.85))
        fig1.add_trace(go.Bar(name="Total Biaya", x=df["Bulan"], y=df["Total Biaya"], marker_color="#f94144", opacity=0.85))
        fig1.add_trace(go.Scatter(name="Laba Bersih", x=df["Bulan"], y=df["Laba Bersih"],
                                  mode="lines+markers", line=dict(color="#90e0ef", width=2.5)))
        fig1.update_layout(barmode="group", template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Proyeksi Pendapatan vs Biaya", font=dict(color="white")),
            legend=dict(font=dict(color="white")), font=dict(color="rgba(255,255,255,0.7)"))
        st.plotly_chart(fig1, use_container_width=True)

        colors = ["#f94144" if v < 0 else "#90be6d" for v in df["Kumulatif"]]
        fig2 = go.Figure()
        fig2.add_hline(y=0, line_dash="dot", line_color="rgba(255,255,255,0.3)")
        fig2.add_trace(go.Scatter(x=df["Bulan"], y=df["Kumulatif"], fill="tozeroy",
            mode="lines+markers", line=dict(color="#f9c74f", width=2.5),
            fillcolor="rgba(249,199,79,0.12)", marker=dict(size=6, color=colors)))
        fig2.update_layout(template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Kumulatif Keuntungan (vs Modal Awal)", font=dict(color="white")),
            font=dict(color="rgba(255,255,255,0.7)"))
        st.plotly_chart(fig2, use_container_width=True)

        df_disp = df.copy()
        for c in ["Pendapatan","Total Biaya","Laba Bersih","Kumulatif","PV CashFlow"]:
            df_disp[c] = df_disp[c].apply(lambda x: f"Rp {x:,.0f}")
        st.dataframe(df_disp, use_container_width=True, hide_index=True)

    # ── TAB 3: RASIO KEUANGAN ────────────────────────────────────
    with tabs[2]:
        st.markdown('<div class="section-title">📐 Analisis Rasio Keuangan Standar</div>', unsafe_allow_html=True)

        def rasio_card(label, value, satuan, status_text, color):
            return f"""<div class="rasio-card">
                <div class="rasio-val" style="color:{color}">{value} {satuan}</div>
                <div class="rasio-lbl">{label}</div>
                <div class="rasio-status" style="color:{color}">{'✅' if color=='#48c78e' else '⚠️' if color=='#f9c74f' else '❌'} {status_text}</div>
            </div>"""

        st.markdown("**🔵 Rasio Likuiditas** — kemampuan membayar hutang jangka pendek")
        col1,col2,col3 = st.columns(3)
        with col1:
            cr_color = "#48c78e" if current_ratio >= 2 else "#f9c74f" if current_ratio >= 1 else "#f94144"
            cr_status = "Sangat Baik" if current_ratio >= 2 else "Cukup" if current_ratio >= 1 else "Kurang"
            st.markdown(rasio_card("Current Ratio", f"{current_ratio:.2f}x", "", cr_status, cr_color), unsafe_allow_html=True)
        with col2:
            qr_color = "#48c78e" if quick_ratio >= 1 else "#f9c74f" if quick_ratio >= 0.7 else "#f94144"
            qr_status = "Baik (≥1)" if quick_ratio >= 1 else "Cukup" if quick_ratio >= 0.7 else "Perlu Perhatian"
            st.markdown(rasio_card("Quick Ratio", f"{quick_ratio:.2f}x", "", qr_status, qr_color), unsafe_allow_html=True)
        with col3:
            st.markdown(rasio_card("Modal Kerja Bersih", f"Rp {modal_kerja_bersih:,.0f}", "", "Aktiva Lancar - Hutang Lancar", "#90e0ef"), unsafe_allow_html=True)

        st.markdown("<br>**🟡 Rasio Profitabilitas** — kemampuan menghasilkan laba")
        col1,col2,col3 = st.columns(3)
        with col1:
            npm_color = "#48c78e" if net_profit_margin >= 20 else "#f9c74f" if net_profit_margin >= 10 else "#f94144"
            st.markdown(rasio_card("Net Profit Margin", f"{net_profit_margin:.1f}%", "", "Baik ≥20%" if net_profit_margin>=20 else "Sedang" if net_profit_margin>=10 else "Rendah", npm_color), unsafe_allow_html=True)
        with col2:
            roa_color = "#48c78e" if roa >= 10 else "#f9c74f" if roa >= 5 else "#f94144"
            st.markdown(rasio_card("ROA (Return on Assets)", f"{roa:.1f}%/thn", "", "Baik ≥10%" if roa>=10 else "Sedang" if roa>=5 else "Rendah", roa_color), unsafe_allow_html=True)
        with col3:
            roe_color = "#48c78e" if roe >= 15 else "#f9c74f" if roe >= 8 else "#f94144"
            st.markdown(rasio_card("ROE (Return on Equity)", f"{roe:.1f}%/thn", "", "Baik ≥15%" if roe>=15 else "Sedang" if roe>=8 else "Rendah", roe_color), unsafe_allow_html=True)

        st.markdown("<br>**🔴 Rasio Solvabilitas** — kemampuan membayar semua kewajiban")
        col1,col2,col3 = st.columns(3)
        with col1:
            dte_color = "#48c78e" if debt_to_equity <= 1 else "#f9c74f" if debt_to_equity <= 2 else "#f94144"
            st.markdown(rasio_card("Debt to Equity Ratio", f"{debt_to_equity:.2f}x", "", "Sehat ≤1" if debt_to_equity<=1 else "Perhatian" if debt_to_equity<=2 else "Risiko Tinggi", dte_color), unsafe_allow_html=True)
        with col2:
            dr_color = "#48c78e" if debt_ratio <= 0.5 else "#f9c74f" if debt_ratio <= 0.7 else "#f94144"
            st.markdown(rasio_card("Debt Ratio", f"{debt_ratio:.2f}", "", "Sehat ≤0.5" if debt_ratio<=0.5 else "Perhatian" if debt_ratio<=0.7 else "Berisiko", dr_color), unsafe_allow_html=True)
        with col3:
            ic_color = "#48c78e" if interest_coverage >= 3 else "#f9c74f" if interest_coverage >= 1.5 else "#f94144"
            ic_val = f"{interest_coverage:.1f}x" if interest_coverage < 999 else "∞ (No Debt)"
            st.markdown(rasio_card("Interest Coverage Ratio", ic_val, "", "Aman ≥3x" if interest_coverage>=3 else "Waspada" if interest_coverage>=1.5 else "Kritis", ic_color), unsafe_allow_html=True)

        st.markdown("<br>**🟢 Rasio Aktivitas** — efisiensi penggunaan aset")
        col1,col2,col3 = st.columns(3)
        with col1:
            st.markdown(rasio_card("Asset Turnover", f"{asset_turnover:.2f}x/thn", "", "Efisiensi Penggunaan Aset", "#90e0ef"), unsafe_allow_html=True)
        with col2:
            st.markdown(rasio_card("Inventory Turnover", f"{inventory_turnover:.1f}x/thn", "", "Putaran Stok Barang", "#90e0ef"), unsafe_allow_html=True)
        with col3:
            dso_color = "#48c78e" if dso <= 30 else "#f9c74f" if dso <= 60 else "#f94144"
            st.markdown(rasio_card("Days Sales Outstanding", f"{dso:.0f} hari", "", "Rata-rata Piutang Tertagih", dso_color), unsafe_allow_html=True)

    # ── TAB 4: TIME VALUE OF MONEY ───────────────────────────────
    with tabs[3]:
        st.markdown('<div class="section-title">⏳ Time Value of Money (TVM)</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:rgba(255,255,255,0.6);font-size:0.9rem">Konsep: uang Rp1.000.000 hari ini lebih bernilai dari Rp1.000.000 di masa depan karena potensi investasinya.</p>', unsafe_allow_html=True)

        col1,col2 = st.columns(2)
        with col1:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#f9c74f;font-size:0.85rem;font-weight:700;text-transform:uppercase;letter-spacing:1px">Future Value (FV)</div>
                <div style="color:white;font-size:1.3rem;font-weight:800;margin:0.5rem 0">Rp {fv_5yr:,.0f}</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">Nilai modal awal Rp {modal_awal:,.0f} dalam 5 tahun<br>
                dengan tingkat bunga {discount_rate}%/tahun<br>
                <em>Formula: FV = PV × (1 + r)ⁿ</em></div>
            </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#90e0ef;font-size:0.85rem;font-weight:700;text-transform:uppercase;letter-spacing:1px">Present Value (PV)</div>
                <div style="color:white;font-size:1.3rem;font-weight:800;margin:0.5rem 0">Rp {pv_val:,.0f}</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">Nilai masa kini dari Rp {modal_awal:,.0f} yang diterima 5 tahun lagi<br>
                dengan discount rate {discount_rate}%/tahun<br>
                <em>Formula: PV = FV / (1 + r)ⁿ</em></div>
            </div>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="rasio-card" style="margin-top:1rem">
            <div style="color:#48c78e;font-size:0.85rem;font-weight:700;text-transform:uppercase;letter-spacing:1px">Nilai Sekarang Anuitas (PV Anuitas)</div>
            <div style="color:white;font-size:1.3rem;font-weight:800;margin:0.5rem 0">Rp {pv_anuitas:,.0f}</div>
            <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">
            Nilai sekarang dari aliran laba bersih Rp {laba_tahunan:,.0f}/tahun selama {n_bulan//12 if n_bulan>=12 else 1} tahun<br>
            dengan discount rate {discount_rate}%/tahun<br>
            <em>Formula: PVA = PMT × [(1-(1+r)⁻ⁿ)/r]</em></div>
        </div>""", unsafe_allow_html=True)

        # Tabel FV per tahun
        st.markdown("<br>**📋 Tabel Pertumbuhan Nilai Modal (Compound Interest)**")
        tvm_data = []
        for y in range(1, 11):
            fv_y = modal_awal * (1 + r_tahunan) ** y
            pv_y = modal_awal / (1 + r_tahunan) ** y
            tvm_data.append({"Tahun ke-": y, "Future Value Modal": f"Rp {fv_y:,.0f}",
                             "Present Value (dari masa depan)": f"Rp {pv_y:,.0f}",
                             "Faktor Bunga (1+r)ⁿ": f"{(1+r_tahunan)**y:.4f}"})
        st.dataframe(pd.DataFrame(tvm_data), use_container_width=True, hide_index=True)

    # ── TAB 5: CAPITAL BUDGETING ─────────────────────────────────
    with tabs[4]:
        st.markdown('<div class="section-title">💼 Capital Budgeting & Penilaian Investasi</div>', unsafe_allow_html=True)

        col1,col2,col3 = st.columns(3)
        # NPV
        npv_color = "#48c78e" if npv > 0 else "#f94144"
        npv_status = "TERIMA — Investasi menciptakan nilai" if npv > 0 else "TOLAK — Investasi menghancurkan nilai"
        with col1:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#f9c74f;font-weight:700;font-size:0.85rem;letter-spacing:1px">NET PRESENT VALUE (NPV)</div>
                <div style="color:{npv_color};font-size:1.4rem;font-weight:800;margin:0.5rem 0">Rp {npv:,.0f}</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">Discount Rate: {discount_rate}%/tahun<br>
                Periode: {periode}<br><br>
                <strong style="color:{npv_color}">{"✅" if npv>0 else "❌"} {npv_status}</strong><br><br>
                <em>NPV = Σ[CFₜ/(1+r)ᵗ] - Investasi Awal</em></div>
            </div>""", unsafe_allow_html=True)

        # IRR
        irr_color = "#48c78e" if irr_annual > discount_rate else "#f94144"
        with col2:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#90e0ef;font-weight:700;font-size:0.85rem;letter-spacing:1px">INTERNAL RATE OF RETURN (IRR)</div>
                <div style="color:{irr_color};font-size:1.4rem;font-weight:800;margin:0.5rem 0">{irr_annual:.2f}%/tahun</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">Hurdle Rate (WACC): {discount_rate}%<br><br>
                <strong style="color:{irr_color}">{"✅ TERIMA — IRR > Hurdle Rate" if irr_annual>discount_rate else "❌ TOLAK — IRR < Hurdle Rate"}</strong><br><br>
                <em>IRR adalah r ketika NPV = 0</em></div>
            </div>""", unsafe_allow_html=True)

        # Payback
        pb_color = "#48c78e" if payback <= 24 else "#f9c74f" if payback <= 48 else "#f94144"
        with col3:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#48c78e;font-weight:700;font-size:0.85rem;letter-spacing:1px">PAYBACK PERIOD</div>
                <div style="color:{pb_color};font-size:1.4rem;font-weight:800;margin:0.5rem 0">{payback:.1f} bulan</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">
                ≤24 bln: Sangat Cepat ✅<br>
                24-48 bln: Normal 🟡<br>
                >48 bln: Lambat ❌<br><br>
                <em>PP = Investasi / Laba Bersih/bln</em></div>
            </div>""", unsafe_allow_html=True)

        # Tabel NPV Sensitivity
        st.markdown("<br>**📋 Tabel Sensitivitas NPV terhadap Discount Rate**")
        sensitivity = []
        for r_test in [5, 8, 10, 12, 15, 18, 20, 25]:
            r_m = r_test / 100 / 12
            npv_test = -modal_awal
            for i, cf in enumerate(cashflows[1:], 1):
                npv_test += cf / (1 + r_m) ** i
            sensitivity.append({"Discount Rate": f"{r_test}%", "NPV": f"Rp {npv_test:,.0f}",
                                 "Keputusan": "✅ TERIMA" if npv_test > 0 else "❌ TOLAK"})
        st.dataframe(pd.DataFrame(sensitivity), use_container_width=True, hide_index=True)

    # ── TAB 6: MODAL KERJA & KAS ─────────────────────────────────
    with tabs[5]:
        st.markdown('<div class="section-title">🏦 Manajemen Modal Kerja & Kas</div>', unsafe_allow_html=True)

        col1,col2 = st.columns(2)
        with col1:
            st.markdown("**💵 Posisi Kas**")
            kas_color = "#48c78e" if kas_surplus > 0 else "#f94144"
            st.markdown(f"""<div class="rasio-card">
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem">Kas Tersedia</div>
                <div style="color:white;font-size:1.2rem;font-weight:700">Rp {kas:,.0f}</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.5rem">Kas Minimum (2× biaya tetap)</div>
                <div style="color:#f9c74f;font-size:1.2rem;font-weight:700">Rp {kas_minimum:,.0f}</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.5rem">Surplus / Defisit Kas</div>
                <div style="color:{kas_color};font-size:1.2rem;font-weight:700">Rp {kas_surplus:,.0f}</div>
                <div style="margin-top:0.75rem;font-size:0.8rem;color:{kas_color}">
                {"✅ Kas mencukupi operasional" if kas_surplus > 0 else "❌ Kas di bawah minimum — perlu tambahan modal kerja"}</div>
            </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown("**📦 Manajemen Piutang & Persediaan**")
            st.markdown(f"""<div class="rasio-card">
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem">Days Sales Outstanding (DSO)</div>
                <div style="color:{'#48c78e' if dso<=30 else '#f9c74f' if dso<=60 else '#f94144'};font-size:1.2rem;font-weight:700">{dso:.0f} hari</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.78rem">Rata-rata hari piutang tertagih (ideal ≤30 hari)</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.75rem">Inventory Turnover</div>
                <div style="color:#90e0ef;font-size:1.2rem;font-weight:700">{inventory_turnover:.1f}x per tahun</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.78rem">Perputaran stok (makin tinggi makin efisien)</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.75rem">Modal Kerja Bersih (NWC)</div>
                <div style="color:{'#48c78e' if modal_kerja_bersih>0 else '#f94144'};font-size:1.2rem;font-weight:700">Rp {modal_kerja_bersih:,.0f}</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>**📊 Komposisi Aktiva Lancar**")
        fig_pie = go.Figure(go.Pie(
            labels=["Kas", "Piutang", "Persediaan"],
            values=[kas, piutang, persediaan],
            hole=0.45,
            marker_colors=["#f9c74f","#90e0ef","#48c78e"]
        ))
        fig_pie.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Komposisi Modal Kerja", font=dict(color="white")),
            font=dict(color="white"), height=350)
        st.plotly_chart(fig_pie, use_container_width=True)

    # ── TAB 7: SUMBER PEMBIAYAAN ─────────────────────────────────
    with tabs[6]:
        st.markdown('<div class="section-title">💳 Sumber-Sumber Pembiayaan Bisnis</div>', unsafe_allow_html=True)

        total_pendanaan = ekuitas + total_hutang
        pct_ekuitas = ekuitas / total_pendanaan * 100 if total_pendanaan > 0 else 0
        pct_hutang  = total_hutang / total_pendanaan * 100 if total_pendanaan > 0 else 0

        col1,col2 = st.columns(2)
        with col1:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#f9c74f;font-weight:700;margin-bottom:0.75rem">🏗️ Struktur Permodalan</div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem">
                    <span style="color:rgba(255,255,255,0.6)">Modal Sendiri (Ekuitas)</span>
                    <span style="color:#48c78e;font-weight:700">Rp {ekuitas:,.0f} ({pct_ekuitas:.1f}%)</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem">
                    <span style="color:rgba(255,255,255,0.6)">Hutang Lancar</span>
                    <span style="color:#f9c74f;font-weight:700">Rp {hutang_lancar:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem">
                    <span style="color:rgba(255,255,255,0.6)">Hutang Jangka Panjang</span>
                    <span style="color:#f3722c;font-weight:700">Rp {hutang_jangka_panjang:,.0f} ({pct_hutang:.1f}%)</span>
                </div>
                <div style="display:flex;justify-content:space-between;border-top:1px solid rgba(255,255,255,0.1);padding-top:0.5rem;margin-top:0.5rem">
                    <span style="color:white;font-weight:700">Total Pendanaan</span>
                    <span style="color:white;font-weight:700">Rp {total_pendanaan:,.0f}</span>
                </div>
            </div>""", unsafe_allow_html=True)

        with col2:
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#90e0ef;font-weight:700;margin-bottom:0.75rem">⚙️ Biaya Modal (WACC Estimasi)</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem">Biaya Ekuitas (discount rate)</div>
                <div style="color:#48c78e;font-size:1.1rem;font-weight:700">{discount_rate}%/tahun</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.5rem">Biaya Hutang (after tax ~20%)</div>
                <div style="color:#f9c74f;font-size:1.1rem;font-weight:700">{suku_bunga_hutang * 0.8:.1f}%/tahun</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.5rem">Beban Bunga Tahunan</div>
                <div style="color:#f3722c;font-size:1.1rem;font-weight:700">Rp {beban_bunga_tahunan:,.0f}</div>
                <div style="color:rgba(255,255,255,0.6);font-size:0.85rem;margin-top:0.5rem">WACC (estimasi)</div>
                <div style="color:white;font-size:1.2rem;font-weight:800">{wacc_approx:.2f}%/tahun</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>**📚 Panduan Sumber Pembiayaan UMKM**")
        pembiayaan = [
            ("🏦 KUR (Kredit Usaha Rakyat)", "Bunga 6%/tahun, maks Rp 500jt, tanpa agunan s.d Rp 100jt. Tersedia di BRI, BNI, Mandiri, BSI.", "#48c78e"),
            ("👼 Investor / Angel Investor", "Cocok untuk startup. Investor memberi modal dengan imbalan equity/saham bisnis.", "#f9c74f"),
            ("🌐 Crowdfunding", "Platform seperti Kitabisa, Indiegogo. Cocok untuk produk inovatif dengan community support.", "#90e0ef"),
            ("🎓 Program Inkubator Kampus", "UM Metro memiliki program pendampingan dan pendanaan untuk mahasiswa wirausaha.", "#c77dff"),
            ("📱 P2P Lending", "Platform fintech (Modalku, Investree) untuk pinjaman usaha dengan proses digital.", "#f3722c"),
            ("🏛️ Hibah Pemerintah", "Program Kemenkop UKM, Kemenparekraf, BUMN untuk UMKM — biasanya berbasis kompetisi.", "#48c78e"),
        ]
        for title, desc, color in pembiayaan:
            st.markdown(f"""<div class="rasio-card" style="border-left:3px solid {color}">
                <div style="color:{color};font-weight:700">{title}</div>
                <div style="color:rgba(255,255,255,0.65);font-size:0.85rem;margin-top:0.3rem">{desc}</div>
            </div>""", unsafe_allow_html=True)

    # ── TAB 8: RISIKO & RETURN ───────────────────────────────────
    with tabs[7]:
        st.markdown('<div class="section-title">⚠️ Analisis Risiko & Return Investasi</div>', unsafe_allow_html=True)

        col1,col2 = st.columns(2)
        with col1:
            ol_color = "#48c78e" if operating_leverage < 2 else "#f9c74f" if operating_leverage < 4 else "#f94144"
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#f9c74f;font-weight:700">📊 Operating Leverage (DOL)</div>
                <div style="color:{ol_color};font-size:1.4rem;font-weight:800;margin:0.5rem 0">{operating_leverage:.2f}x</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">
                DOL mengukur sensitivitas laba terhadap perubahan penjualan.<br>
                DOL {operating_leverage:.1f}x artinya kenaikan penjualan 10% = laba naik {operating_leverage*10:.0f}%.<br>
                <span style="color:{ol_color}">{'✅ Leverage Rendah (Aman)' if operating_leverage<2 else '⚠️ Leverage Sedang' if operating_leverage<4 else '❌ Leverage Tinggi (Berisiko)'}</span>
                </div>
            </div>""", unsafe_allow_html=True)

        with col2:
            mos_color = "#48c78e" if margin_of_safety_pct >= 30 else "#f9c74f" if margin_of_safety_pct >= 15 else "#f94144"
            st.markdown(f"""<div class="rasio-card">
                <div style="color:#90e0ef;font-weight:700">🛡️ Margin of Safety</div>
                <div style="color:{mos_color};font-size:1.4rem;font-weight:800;margin:0.5rem 0">{margin_of_safety_pct:.1f}%</div>
                <div style="color:rgba(255,255,255,0.5);font-size:0.8rem">
                Penjualan aktual ({estimasi_penjualan} unit) vs BEP ({bep_unit:.0f} unit)<br>
                Selisih: {margin_of_safety_unit:.0f} unit di atas BEP<br>
                <span style="color:{mos_color}">{'✅ Sangat Aman (≥30%)' if margin_of_safety_pct>=30 else '⚠️ Cukup Aman (15-30%)' if margin_of_safety_pct>=15 else '❌ Mendekati BEP — Waspada'}</span>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>**🎯 Analisis Skenario (Scenario Analysis)**")
        col1,col2,col3 = st.columns(3)
        skenario_items = list(skenario.items())
        colors_s = ["#f94144","#f9c74f","#48c78e"]
        icons_s  = ["📉","📊","📈"]
        for col, (nama_sk, val_sk), color_s, icon_s in zip([col1,col2,col3], skenario_items, colors_s, icons_s):
            with col:
                st.markdown(f"""<div class="rasio-card" style="text-align:center">
                    <div style="font-size:1.5rem">{icon_s}</div>
                    <div style="color:rgba(255,255,255,0.6);font-size:0.8rem;margin:0.3rem 0">{nama_sk}</div>
                    <div style="color:{color_s};font-size:1.2rem;font-weight:800">Rp {val_sk:,.0f}</div>
                    <div style="color:rgba(255,255,255,0.4);font-size:0.75rem">Laba Bersih/Bulan</div>
                </div>""", unsafe_allow_html=True)

        st.markdown("<br>**📋 Ringkasan Risk-Return Profile**")
        risk_score = 0
        risk_factors = []
        if debt_to_equity > 2:  risk_score += 2; risk_factors.append("❌ D/E Ratio tinggi (>2x)")
        if margin_of_safety_pct < 15: risk_score += 2; risk_factors.append("❌ Margin of safety rendah (<15%)")
        if operating_leverage > 4: risk_score += 2; risk_factors.append("❌ Operating leverage tinggi (>4x)")
        if kas_surplus < 0: risk_score += 2; risk_factors.append("❌ Kas di bawah minimum")
        if npv < 0: risk_score += 2; risk_factors.append("❌ NPV negatif")
        if irr_annual > discount_rate: risk_factors.append("✅ IRR melebihi hurdle rate")
        if margin_of_safety_pct >= 30: risk_factors.append("✅ Margin of safety kuat")
        if current_ratio >= 2: risk_factors.append("✅ Likuiditas sangat baik")

        risk_label = "🟢 Risiko Rendah" if risk_score <= 2 else "🟡 Risiko Sedang" if risk_score <= 6 else "🔴 Risiko Tinggi"
        st.markdown(f"""<div class="rasio-card">
            <div style="color:white;font-size:1.1rem;font-weight:700;margin-bottom:0.75rem">
                Profil Risiko: <span style="color:{'#48c78e' if risk_score<=2 else '#f9c74f' if risk_score<=6 else '#f94144'}">{risk_label}</span>
            </div>
            {"".join(f'<div style="color:rgba(255,255,255,0.7);font-size:0.85rem;margin-bottom:0.25rem">{f}</div>' for f in risk_factors)}
        </div>""", unsafe_allow_html=True)

