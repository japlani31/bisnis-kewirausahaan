import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Simulasi Keuangan", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.04) !important; border-right: 1px solid rgba(255,255,255,0.08); }
section[data-testid="stSidebar"] * { color: #e0e0e0 !important; }
h1, h2, h3 { color: white !important; }
p, li, label { color: rgba(255,255,255,0.8) !important; }
.stTextInput input, .stNumberInput input, .stSelectbox select {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 8px !important;
}
.metric-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
}
.metric-value { font-size: 1.6rem; font-weight: 800; color: #f9c74f; }
.metric-label { font-size: 0.8rem; color: rgba(255,255,255,0.55); margin-top: 0.25rem; }
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: white;
    margin: 1.5rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(249,199,79,0.4);
}
.info-box {
    background: rgba(72,199,142,0.1);
    border: 1px solid rgba(72,199,142,0.3);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 0.5rem 0;
}
.warning-box {
    background: rgba(249,115,22,0.1);
    border: 1px solid rgba(249,115,22,0.3);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 0.5rem 0;
}
.stButton button {
    background: linear-gradient(90deg, #f9c74f, #f3722c) !important;
    color: #1a1a2e !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 2rem !important;
    font-size: 1rem !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-family:Syne,sans-serif;font-size:2rem;font-weight:800;background:linear-gradient(90deg,#f9c74f,#f3722c);-webkit-background-clip:text;-webkit-text-fill-color:transparent">📊 Simulasi Keuangan Bisnis</p>', unsafe_allow_html=True)
st.markdown('<p style="color:rgba(255,255,255,0.6)">Isi data bisnis Anda, dan sistem akan menghitung otomatis: BEP, Cashflow, ROI, dan kelayakan usaha.</p>', unsafe_allow_html=True)

st.markdown("---")

# ─── INPUT SECTION ───────────────────────────────────────────────
st.markdown('<div class="section-title">1️⃣ Informasi Dasar Bisnis</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    nama_bisnis = st.text_input("Nama Bisnis", placeholder="Contoh: Warung Kopi Nusantara")
    jenis_bisnis = st.selectbox("Jenis Bisnis", ["Kuliner/F&B", "Fashion/Pakaian", "Jasa/Servis", "Teknologi/Digital", "Pendidikan", "Retail/Toko", "Lainnya"])
with col2:
    modal_awal = st.number_input("Modal Awal (Rp)", min_value=0, value=10000000, step=500000, format="%d")
    periode = st.selectbox("Periode Proyeksi", ["6 Bulan", "12 Bulan", "24 Bulan"])

st.markdown('<div class="section-title">2️⃣ Biaya Tetap (Per Bulan)</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Biaya yang selalu ada meski tidak berjualan (sewa, gaji, listrik, dll)</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    sewa = st.number_input("Sewa Tempat (Rp/bulan)", min_value=0, value=1000000, step=100000, format="%d")
    gaji = st.number_input("Gaji Karyawan (Rp/bulan)", min_value=0, value=2000000, step=100000, format="%d")
with col2:
    listrik = st.number_input("Listrik & Air (Rp/bulan)", min_value=0, value=300000, step=50000, format="%d")
    internet = st.number_input("Internet/Telepon (Rp/bulan)", min_value=0, value=200000, step=50000, format="%d")
with col3:
    biaya_tetap_lain = st.number_input("Biaya Tetap Lainnya (Rp/bulan)", min_value=0, value=500000, step=100000, format="%d")

total_biaya_tetap = sewa + gaji + listrik + internet + biaya_tetap_lain

st.markdown('<div class="section-title">3️⃣ Biaya Variabel & Pendapatan</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Biaya yang berubah sesuai jumlah produksi/penjualan</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    harga_jual = st.number_input("Harga Jual per Unit (Rp)", min_value=0, value=25000, step=1000, format="%d")
    hpp = st.number_input("Harga Pokok Produksi per Unit (Rp)", min_value=0, value=12000, step=1000, format="%d")
with col2:
    estimasi_penjualan = st.number_input("Estimasi Penjualan per Bulan (unit)", min_value=0, value=300, step=10, format="%d")
    biaya_variabel_lain = st.number_input("Biaya Variabel Lain per Unit (Rp)", min_value=0, value=2000, step=500, format="%d")
with col3:
    pertumbuhan = st.slider("Estimasi Pertumbuhan Penjualan (%/bulan)", 0, 20, 5)

# ─── KALKULASI ───────────────────────────────────────────────────
if st.button("🚀 Hitung Simulasi Sekarang!"):

    # Validasi
    if harga_jual <= (hpp + biaya_variabel_lain):
        st.markdown('<div class="warning-box">⚠️ <strong>Peringatan:</strong> Harga jual Anda lebih rendah atau sama dengan biaya produksi! Bisnis akan merugi.</div>', unsafe_allow_html=True)

    margin_per_unit = harga_jual - hpp - biaya_variabel_lain
    pendapatan_bulan1 = harga_jual * estimasi_penjualan
    biaya_variabel_total = (hpp + biaya_variabel_lain) * estimasi_penjualan
    laba_kotor = pendapatan_bulan1 - biaya_variabel_total
    laba_bersih = laba_kotor - total_biaya_tetap

    # BEP Unit
    if margin_per_unit > 0:
        bep_unit = total_biaya_tetap / margin_per_unit
        bep_rupiah = bep_unit * harga_jual
    else:
        bep_unit = 0
        bep_rupiah = 0

    # ROI
    roi = (laba_bersih / modal_awal * 100) if modal_awal > 0 else 0

    # Payback Period
    payback = (modal_awal / laba_bersih) if laba_bersih > 0 else 999

    st.markdown("---")
    st.markdown('<div class="section-title">📈 Hasil Simulasi</div>', unsafe_allow_html=True)

    # Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">Rp {laba_bersih:,.0f}</div>
            <div class="metric-label">Laba Bersih/Bulan</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{bep_unit:,.0f} unit</div>
            <div class="metric-label">BEP (Break Even Point)</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{roi:.1f}%</div>
            <div class="metric-label">ROI per Bulan</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        pb_text = f"{payback:.1f} bulan" if payback < 100 else "Belum balik modal"
        st.markdown(f"""<div class="metric-card">
            <div class="metric-value">{pb_text}</div>
            <div class="metric-label">Payback Period</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ─── PROYEKSI CASHFLOW ───────────────────────────────────────
    bulan_map = {"6 Bulan": 6, "12 Bulan": 12, "24 Bulan": 24}
    n_bulan = bulan_map[periode]

    bulan_list, pendapatan_list, biaya_list, laba_list, kumulatif_list = [], [], [], [], []
    kumulatif = -modal_awal

    for i in range(1, n_bulan + 1):
        faktor = (1 + pertumbuhan / 100) ** (i - 1)
        unit_bulan = estimasi_penjualan * faktor
        pend = harga_jual * unit_bulan
        biaya_var = (hpp + biaya_variabel_lain) * unit_bulan
        laba = pend - biaya_var - total_biaya_tetap
        kumulatif += laba

        bulan_list.append(f"Bulan {i}")
        pendapatan_list.append(round(pend))
        biaya_list.append(round(biaya_var + total_biaya_tetap))
        laba_list.append(round(laba))
        kumulatif_list.append(round(kumulatif))

    df = pd.DataFrame({
        "Bulan": bulan_list,
        "Pendapatan": pendapatan_list,
        "Total Biaya": biaya_list,
        "Laba Bersih": laba_list,
        "Kumulatif": kumulatif_list
    })

    # Chart 1: Pendapatan vs Biaya
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(name="Pendapatan", x=df["Bulan"], y=df["Pendapatan"],
                          marker_color="#f9c74f", opacity=0.85))
    fig1.add_trace(go.Bar(name="Total Biaya", x=df["Bulan"], y=df["Total Biaya"],
                          marker_color="#f94144", opacity=0.85))
    fig1.add_trace(go.Scatter(name="Laba Bersih", x=df["Bulan"], y=df["Laba Bersih"],
                              mode="lines+markers", line=dict(color="#90e0ef", width=2.5),
                              marker=dict(size=6)))
    fig1.update_layout(
        barmode="group", template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        title=dict(text="📊 Proyeksi Pendapatan vs Biaya", font=dict(color="white", size=15)),
        legend=dict(font=dict(color="white")),
        font=dict(color="rgba(255,255,255,0.7)")
    )
    st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Kumulatif
    colors = ["#f94144" if v < 0 else "#90be6d" for v in df["Kumulatif"]]
    fig2 = go.Figure()
    fig2.add_hline(y=0, line_dash="dot", line_color="rgba(255,255,255,0.3)")
    fig2.add_trace(go.Scatter(
        x=df["Bulan"], y=df["Kumulatif"],
        fill="tozeroy", mode="lines+markers",
        line=dict(color="#f9c74f", width=2.5),
        fillcolor="rgba(249,199,79,0.15)",
        marker=dict(size=7, color=colors)
    ))
    fig2.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        title=dict(text="💰 Kumulatif Keuntungan (termasuk modal awal)", font=dict(color="white", size=15)),
        font=dict(color="rgba(255,255,255,0.7)")
    )
    st.plotly_chart(fig2, use_container_width=True)

    # Tabel ringkasan
    st.markdown('<div class="section-title">📋 Tabel Proyeksi Lengkap</div>', unsafe_allow_html=True)
    df_display = df.copy()
    for col in ["Pendapatan", "Total Biaya", "Laba Bersih", "Kumulatif"]:
        df_display[col] = df_display[col].apply(lambda x: f"Rp {x:,.0f}")
    st.dataframe(df_display, use_container_width=True, hide_index=True)

    # Kesimpulan
    st.markdown('<div class="section-title">💡 Kesimpulan & Rekomendasi</div>', unsafe_allow_html=True)

    if laba_bersih > 0 and payback <= 12:
        st.markdown(f"""<div class="info-box">
        ✅ <strong>Bisnis {nama_bisnis if nama_bisnis else 'Anda'} terlihat LAYAK!</strong><br>
        • Laba bersih bulan pertama: <strong>Rp {laba_bersih:,.0f}</strong><br>
        • Modal diperkirakan kembali dalam: <strong>{payback:.1f} bulan</strong><br>
        • BEP tercapai saat menjual <strong>{bep_unit:,.0f} unit/bulan</strong>
        </div>""", unsafe_allow_html=True)
    elif laba_bersih > 0:
        st.markdown(f"""<div class="info-box">
        🟡 <strong>Bisnis berpotensi, tapi payback period cukup panjang ({payback:.1f} bulan).</strong><br>
        • Pertimbangkan mengurangi biaya tetap atau meningkatkan harga jual.<br>
        • BEP: <strong>{bep_unit:,.0f} unit/bulan</strong>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div class="warning-box">
        ❌ <strong>Bisnis saat ini MERUGI Rp {abs(laba_bersih):,.0f}/bulan.</strong><br>
        • Tinjau kembali harga jual, kurangi biaya tetap, atau tingkatkan volume penjualan.<br>
        • BEP membutuhkan setidaknya <strong>{bep_unit:,.0f} unit/bulan</strong> agar impas.
        </div>""", unsafe_allow_html=True)
