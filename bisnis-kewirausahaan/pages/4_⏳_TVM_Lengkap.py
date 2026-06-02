import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Nilai Waktu Uang", page_icon="⏳", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 15px;
    line-height: 1.65;
}

.stApp { background: linear-gradient(150deg, #0d0f1e 0%, #141830 60%, #0f1222 100%); }

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
div[data-baseweb="select"] > div { background: #f5f7fa !important; color: #1c2333 !important; border-radius: 7px !important; }
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

.page-title { font-size: 1.55rem; font-weight: 700; color: #c4d4e4 !important; margin: 0 0 0.3rem 0; }
.page-sub   { color: #566880 !important; font-size: 0.86rem; }

.section-title {
    font-size: 0.95rem;
    font-weight: 600;
    color: #a0b4c8 !important;
    margin: 1.4rem 0 0.7rem 0;
    padding-bottom: 0.4rem;
    border-bottom: 1px solid rgba(140,170,210,0.15);
}

.formula-box {
    background: rgba(40,70,120,0.12);
    border: 1px solid rgba(80,130,200,0.2);
    border-left: 3px solid rgba(80,130,200,0.45);
    border-radius: 0 8px 8px 0;
    padding: 0.7rem 1rem;
    margin: 0.4rem 0 0.75rem 0;
    font-family: 'Courier New', monospace;
    font-size: 0.88rem;
    color: #80a8cc !important;
    line-height: 1.6;
}

.result-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.5rem;
    text-align: center;
}
.result-val   { font-size: 1.4rem; font-weight: 700; color: #90b8d8 !important; }
.result-label { font-size: 0.75rem; color: #4a6080 !important; margin-top: 0.2rem; }

.concept-box {
    background: rgba(40,65,110,0.1);
    border: 1px solid rgba(60,100,180,0.15);
    border-radius: 9px;
    padding: 0.8rem 1rem;
    margin: 0.4rem 0 0.7rem 0;
}
.concept-text { font-size: 0.86rem; color: #6882a0 !important; margin: 0; line-height: 1.65; }

.info-row  { font-size: 0.86rem; color: #7a90a8 !important; margin: 0; padding: 0.2rem 0; }
.info-val  { font-size: 0.86rem; color: #a0b8cc !important; font-weight: 600; margin: 0; padding: 0.2rem 0; }

.amort-header { font-size: 0.72rem; font-weight: 600; color: #44607a !important; text-transform: uppercase; letter-spacing: 0.4px; margin: 0; }
.amort-row    { font-size: 0.83rem; color: #8090a8 !important; margin: 0; padding: 0.18rem 0; }
.amort-row-hl { font-size: 0.83rem; color: #90a8c0 !important; font-weight: 500; margin: 0; padding: 0.18rem 0; }
.divider      { border-top: 1px solid rgba(255,255,255,0.06); margin: 0.2rem 0; }

.tip-box {
    background: rgba(60,110,80,0.08);
    border: 1px solid rgba(60,150,90,0.18);
    border-radius: 9px;
    padding: 0.7rem 1rem;
    margin: 0.6rem 0;
}
.tip-text { font-size: 0.84rem; color: #5a8a6a !important; margin: 0; }

.warn-box {
    background: rgba(180,130,40,0.07);
    border: 1px solid rgba(200,160,60,0.18);
    border-radius: 9px;
    padding: 0.7rem 1rem;
    margin: 0.6rem 0;
}
.warn-text { font-size: 0.84rem; color: #8a7040 !important; margin: 0; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════
st.markdown('<p class="page-title">⏳ Nilai Waktu Uang — Kalkulator Lengkap</p>', unsafe_allow_html=True)
st.markdown('<p class="page-sub">Konsep dasar keuangan: uang hari ini lebih bernilai dari uang yang sama di masa depan, karena potensi investasinya.</p>', unsafe_allow_html=True)
st.markdown("---")

# ══════════════════════════════════════════════════════════════════
# 4 TABS
# ══════════════════════════════════════════════════════════════════
tabs = st.tabs([
    "📌 FV & PV",
    "💳 Anuitas & Cicilan",
    "∞ Perpetuitas",
    "🏦 Amortisasi Pinjaman",
])

# ══════════════════════════════════════════════════════════════════
# TAB 1 — FV & PV
# ══════════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown('<div class="section-title">📌 Future Value (FV) dan Present Value (PV)</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="concept-box"><p class="concept-text">'
        '<strong style="color:#8090b0">Konsep inti:</strong> Karena uang bisa diinvestasikan dan menghasilkan bunga, '
        'Rp 1.000.000 hari ini bernilai lebih dari Rp 1.000.000 yang diterima 5 tahun lagi. '
        'FV menjawab "berapa nilai uang ini di masa depan?", PV menjawab "berapa nilai sekarang dari uang yang '
        'akan diterima di masa depan?"'
        '</p></div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📈 Future Value — Nilai Masa Depan**")
        st.markdown('<div class="formula-box">FV = PV × (1 + r) ⁿ<br>r = tingkat bunga per periode<br>n = jumlah periode</div>', unsafe_allow_html=True)
        pv_input = st.number_input("Nilai Sekarang / Modal Awal (PV)", min_value=0, value=10_000_000, step=500_000, format="%d", key="pv_fv")
        r_fv     = st.slider("Tingkat Bunga per Tahun (%)", 1, 30, 10, key="r_fv")
        n_fv     = st.slider("Jangka Waktu (tahun)", 1, 30, 5, key="n_fv")

        fv = pv_input * (1 + r_fv / 100) ** n_fv
        bunga_total = fv - pv_input

        st.markdown(f"""
        <div class="result-card" style="margin-top:0.8rem">
            <div class="result-val">Rp {fv:,.0f}</div>
            <div class="result-label">Future Value setelah {n_fv} tahun</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:0.82rem;color:#4a6080 !important;text-align:center">Bunga yang diperoleh: <strong style="color:#5eaa7a">Rp {bunga_total:,.0f}</strong></p>', unsafe_allow_html=True)

    with col2:
        st.markdown("**📉 Present Value — Nilai Sekarang**")
        st.markdown('<div class="formula-box">PV = FV / (1 + r) ⁿ<br>r = discount rate per periode<br>n = jumlah periode</div>', unsafe_allow_html=True)
        fv_input = st.number_input("Nilai di Masa Depan (FV)", min_value=0, value=15_000_000, step=500_000, format="%d", key="fv_pv")
        r_pv     = st.slider("Discount Rate per Tahun (%)", 1, 30, 10, key="r_pv")
        n_pv     = st.slider("Jangka Waktu (tahun)", 1, 30, 5, key="n_pv")

        pv = fv_input / (1 + r_pv / 100) ** n_pv
        diskon = fv_input - pv

        st.markdown(f"""
        <div class="result-card" style="margin-top:0.8rem">
            <div class="result-val">Rp {pv:,.0f}</div>
            <div class="result-label">Present Value dari uang {n_pv} tahun ke depan</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f'<p style="font-size:0.82rem;color:#4a6080 !important;text-align:center">Selisih waktu: <strong style="color:#c05858">Rp {diskon:,.0f}</strong> nilai yang "hilang"</p>', unsafe_allow_html=True)

    # Tabel pertumbuhan FV
    st.markdown('<div class="section-title">📋 Tabel Pertumbuhan Nilai Modal (Compound Interest)</div>', unsafe_allow_html=True)
    tvm_rows = []
    for y in range(1, 11):
        fv_y  = pv_input * (1 + r_fv / 100) ** y
        pv_y  = fv_input / (1 + r_pv / 100) ** y
        tvm_rows.append({
            "Tahun ke-":                    y,
            "FV Modal Awal (Rp)":           f"{fv_y:,.0f}",
            "Faktor (1+r)ⁿ":               f"{(1 + r_fv/100)**y:.4f}",
            "PV dari FV Target (Rp)":       f"{pv_y:,.0f}",
        })
    st.dataframe(pd.DataFrame(tvm_rows), use_container_width=True, hide_index=True)

    st.markdown(
        '<div class="tip-box"><p class="tip-text">'
        '💡 <strong>Kekuatan Bunga Majemuk:</strong> Semakin lama jangka waktu dan semakin tinggi tingkat bunga, '
        'FV tumbuh secara eksponensial — bukan linier. Ini yang disebut "keajaiban bunga majemuk". '
        'Investasi Rp 10 juta pada bunga 12% selama 20 tahun akan menjadi sekitar Rp 96 juta.'
        '</p></div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════════════════════
# TAB 2 — ANUITAS & CICILAN
# ══════════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown('<div class="section-title">💳 Anuitas — Aliran Pembayaran Berkala</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="concept-box"><p class="concept-text">'
        '<strong style="color:#8090b0">Anuitas</strong> adalah serangkaian pembayaran atau penerimaan yang sama '
        'jumlahnya, dalam interval waktu yang sama (biasanya bulanan atau tahunan). '
        'Contoh nyata: cicilan KUR, tabungan pensiun rutin, sewa bulanan.'
        '</p></div>',
        unsafe_allow_html=True
    )

    mode_an = st.radio("Hitung apa?", ["PV Anuitas — nilai sekarang dari penerimaan rutin", "FV Anuitas — nilai akhir dari tabungan rutin"], key="an_mode")
    
    col1, col2 = st.columns(2)
    with col1:
        pmt_an = st.number_input("Jumlah Pembayaran per Periode (PMT)", min_value=0, value=2_000_000, step=100_000, format="%d", key="pmt_an")
        r_an   = st.slider("Bunga per Tahun (%)", 1, 30, 10, key="r_an")
    with col2:
        n_an   = st.slider("Jumlah Periode (bulan)", 6, 120, 36, key="n_an")
        freq_an = st.selectbox("Frekuensi", ["Bulanan", "Tahunan"], key="freq_an")

    r_period = (r_an / 100 / 12) if freq_an == "Bulanan" else (r_an / 100)

    if "PV" in mode_an:
        st.markdown('<div class="formula-box">PVA = PMT × [ 1 − (1 + r)⁻ⁿ ] / r<br>PMT = pembayaran per periode | r = bunga per periode | n = jumlah periode</div>', unsafe_allow_html=True)
        if r_period > 0:
            pva = pmt_an * (1 - (1 + r_period) ** (-n_an)) / r_period
        else:
            pva = pmt_an * n_an
        total_terima = pmt_an * n_an
        st.markdown(f"""
        <div style="display:flex;gap:0.8rem;margin-top:0.8rem">
            <div class="result-card" style="flex:1">
                <div class="result-val">Rp {pva:,.0f}</div>
                <div class="result-label">Present Value Anuitas</div>
            </div>
            <div class="result-card" style="flex:1">
                <div class="result-val">Rp {total_terima:,.0f}</div>
                <div class="result-label">Total Nominal Diterima</div>
            </div>
            <div class="result-card" style="flex:1">
                <div class="result-val">Rp {total_terima - pva:,.0f}</div>
                <div class="result-label">Selisih Waktu (Time Premium)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            '<div class="tip-box"><p class="tip-text">'
            '💡 Artinya: menerima Rp {0:,.0f} per {1} selama {2} {1} setara dengan menerima <strong>Rp {3:,.0f} hari ini</strong>. '
            'Selisih Rp {4:,.0f} adalah biaya waktu (time value of money).</p></div>'.format(
                pmt_an, "bulan" if freq_an == "Bulanan" else "tahun",
                n_an, pva, total_terima - pva
            ),
            unsafe_allow_html=True
        )
    else:
        st.markdown('<div class="formula-box">FVA = PMT × [ (1 + r)ⁿ − 1 ] / r<br>PMT = tabungan per periode | r = bunga per periode | n = jumlah periode</div>', unsafe_allow_html=True)
        if r_period > 0:
            fva = pmt_an * ((1 + r_period) ** n_an - 1) / r_period
        else:
            fva = pmt_an * n_an
        modal_total = pmt_an * n_an
        bunga_didapat = fva - modal_total
        st.markdown(f"""
        <div style="display:flex;gap:0.8rem;margin-top:0.8rem">
            <div class="result-card" style="flex:1">
                <div class="result-val">Rp {fva:,.0f}</div>
                <div class="result-label">Nilai Akhir Tabungan</div>
            </div>
            <div class="result-card" style="flex:1">
                <div class="result-val">Rp {modal_total:,.0f}</div>
                <div class="result-label">Total Uang Ditabung</div>
            </div>
            <div class="result-card" style="flex:1">
                <div class="result-val" style="color:#5eaa7a !important">Rp {bunga_didapat:,.0f}</div>
                <div class="result-label">Bunga yang Diperoleh</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            '<div class="tip-box"><p class="tip-text">'
            f'💡 Menabung Rp {pmt_an:,.0f} per {"bulan" if freq_an == "Bulanan" else "tahun"} selama {n_an} '
            f'{"bulan" if freq_an == "Bulanan" else "tahun"} menghasilkan <strong>Rp {fva:,.0f}</strong>. '
            f'Bunga majemuk menambahkan Rp {bunga_didapat:,.0f} di atas modal yang Anda tabung.</p></div>',
            unsafe_allow_html=True
        )

    # Grafik pertumbuhan anuitas
    st.markdown('<div class="section-title">📊 Grafik Pertumbuhan</div>', unsafe_allow_html=True)
    if "FV" in mode_an:
        cum_pmt, cum_fv = [], []
        for i in range(1, n_an + 1):
            cum_pmt.append(pmt_an * i)
            if r_period > 0:
                fv_i = pmt_an * ((1 + r_period) ** i - 1) / r_period
            else:
                fv_i = pmt_an * i
            cum_fv.append(fv_i)

        fig_an = go.Figure()
        fig_an.add_trace(go.Scatter(
            x=list(range(1, n_an + 1)), y=cum_pmt,
            name="Total Ditabung", fill="tozeroy",
            line=dict(color="#3d6090", width=1.5),
            fillcolor="rgba(61,96,144,0.18)"
        ))
        fig_an.add_trace(go.Scatter(
            x=list(range(1, n_an + 1)), y=cum_fv,
            name="Nilai Akhir (dgn bunga)", fill="tonexty",
            line=dict(color="#4a9a6a", width=1.8),
            fillcolor="rgba(74,154,106,0.14)"
        ))
        fig_an.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)", height=280,
            margin=dict(l=10, r=10, t=20, b=30),
            legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
            xaxis=dict(title="Periode", tickfont=dict(size=9, color="#5a6880"),
                       gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(tickfont=dict(size=9, color="#5a6880"),
                       gridcolor="rgba(255,255,255,0.05)", zeroline=False),
        )
        st.plotly_chart(fig_an, use_container_width=True)

# ══════════════════════════════════════════════════════════════════
# TAB 3 — PERPETUITAS
# ══════════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown('<div class="section-title">∞ Perpetuitas — Arus Kas Tanpa Batas Waktu</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="concept-box"><p class="concept-text">'
        '<strong style="color:#8090b0">Perpetuitas</strong> adalah anuitas yang berlangsung selamanya — '
        'tidak ada tanggal berakhir. Karena arus kas terus mengalir tanpa henti, '
        'nilai sekarangnya dihitung dengan membagi arus kas tahunan dengan discount rate. '
        '<br><br>'
        'Contoh nyata: saham preferen yang membayar dividen tetap selamanya, '
        'tanah yang disewakan terus-menerus, aset warisan yang menghasilkan pendapatan rutin.'
        '</p></div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Perpetuitas Biasa** *(arus kas tetap selamanya)*")
        st.markdown('<div class="formula-box">PV = C / r<br>C = arus kas per periode<br>r = discount rate / tingkat imbal hasil</div>', unsafe_allow_html=True)

        c_perp = st.number_input("Arus Kas per Tahun (C)", min_value=0, value=5_000_000, step=500_000, format="%d", key="c_perp")
        r_perp = st.slider("Discount Rate per Tahun (%)", 1, 30, 10, key="r_perp")

        if r_perp > 0:
            pv_perp = c_perp / (r_perp / 100)
        else:
            pv_perp = 0

        st.markdown(f"""
        <div class="result-card" style="margin-top:0.8rem">
            <div class="result-val">Rp {pv_perp:,.0f}</div>
            <div class="result-label">Nilai Sekarang Perpetuitas</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(
            f'<p style="font-size:0.82rem;color:#44607a !important;margin-top:0.4rem">'
            f'Artinya: aset yang menghasilkan <strong style="color:#7a90b0">Rp {c_perp:,.0f}/tahun selamanya</strong> '
            f'bernilai setara <strong style="color:#90b8d8">Rp {pv_perp:,.0f}</strong> hari ini '
            f'jika discount rate-nya {r_perp}%.'
            f'</p>',
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("**Perpetuitas Bertumbuh** *(arus kas tumbuh tiap tahun)*")
        st.markdown('<div class="formula-box">PV = C / (r − g)<br>C = arus kas tahun pertama<br>r = discount rate  |  g = tingkat pertumbuhan<br>Syarat: r harus lebih besar dari g</div>', unsafe_allow_html=True)

        c_grow  = st.number_input("Arus Kas Tahun Pertama (C₁)", min_value=0, value=5_000_000, step=500_000, format="%d", key="c_grow")
        r_grow  = st.slider("Discount Rate (%)", 1, 30, 12, key="r_grow")
        g_grow  = st.slider("Tingkat Pertumbuhan g (%)", 0, 20, 5, key="g_grow")

        if r_grow > g_grow:
            pv_grow = c_grow / ((r_grow - g_grow) / 100)
            valid = True
        else:
            pv_grow = 0
            valid = False

        if valid:
            st.markdown(f"""
            <div class="result-card" style="margin-top:0.8rem">
                <div class="result-val">Rp {pv_grow:,.0f}</div>
                <div class="result-label">Nilai Sekarang (Gordon Growth Model)</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(
                f'<p style="font-size:0.82rem;color:#44607a !important;margin-top:0.4rem">'
                f'Arus kas tumbuh {g_grow}%/tahun, sehingga nilainya lebih tinggi '
                f'dibanding perpetuitas biasa (Rp {c_perp:,.0f} / {r_perp}% = Rp {c_perp/(r_perp/100):,.0f}).'
                f'</p>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="warn-box"><p class="warn-text">⚠️ Discount rate harus lebih besar dari g. '
                'Jika g ≥ r, nilai perpetuitas menjadi tak terhingga secara matematis — '
                'tidak berlaku dalam praktik bisnis nyata.</p></div>',
                unsafe_allow_html=True
            )

    # Aplikasi: Valuasi Saham Sederhana
    st.markdown('<div class="section-title">📌 Aplikasi: Valuasi Saham Preferen (DDM — Dividend Discount Model)</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="concept-box"><p class="concept-text">'
        'Saham preferen membayar dividen tetap setiap tahun. Harga wajar saham = PV dari semua dividen masa depan. '
        'Karena saham bisa dianggap hidup "selamanya", kita gunakan rumus perpetuitas: <strong style="color:#8090b0">P = D / r</strong>.'
        '</p></div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        dividen  = st.number_input("Dividen per Lembar Saham / Tahun (Rp)", min_value=0, value=500, step=50, format="%d")
    with col2:
        req_ret  = st.slider("Required Rate of Return (%)", 5, 30, 12, key="req_ret")
    with col3:
        harga_pasar = st.number_input("Harga Pasar Saham Saat Ini (Rp)", min_value=0, value=3_800, step=100, format="%d")

    harga_wajar = dividen / (req_ret / 100) if req_ret > 0 else 0
    selisih = harga_pasar - harga_wajar

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="result-card"><div class="result-val">Rp {harga_wajar:,.0f}</div><div class="result-label">Harga Wajar (Fair Value)</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="result-card"><div class="result-val">Rp {harga_pasar:,.0f}</div><div class="result-label">Harga Pasar Saat Ini</div></div>', unsafe_allow_html=True)
    with col3:
        if selisih < -harga_wajar * 0.05:
            verdict = ("🟢 Undervalued — Layak Beli", "#5eaa7a")
        elif selisih > harga_wajar * 0.05:
            verdict = ("🔴 Overvalued — Pertimbangkan Jual", "#c05858")
        else:
            verdict = ("🟡 Harga Wajar — Hold", "#b89438")
        st.markdown(f'<div class="result-card"><div class="result-val" style="font-size:1rem;color:{verdict[1]} !important">{verdict[0]}</div><div class="result-label">Keputusan Investasi (estimasi)</div></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="warn-box"><p class="warn-text">'
        '⚠️ Valuasi saham di atas bersifat edukatif dan sangat disederhanakan. '
        'Keputusan investasi nyata membutuhkan analisis lebih mendalam dan konsultasi dengan penasihat keuangan profesional.'
        '</p></div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════════════════════
# TAB 4 — AMORTISASI PINJAMAN
# ══════════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown('<div class="section-title">🏦 Kalkulator Amortisasi Pinjaman</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="concept-box"><p class="concept-text">'
        '<strong style="color:#8090b0">Amortisasi</strong> adalah proses pelunasan pinjaman secara bertahap '
        'melalui cicilan berkala. Setiap cicilan terdiri dari dua komponen: '
        '<strong style="color:#7a9ab8">pokok pinjaman</strong> dan <strong style="color:#7a9ab8">bunga</strong>. '
        'Di awal tenor, porsi bunga lebih besar; di akhir, porsi pokok yang lebih besar.'
        '</p></div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="formula-box">PMT = P × r(1 + r)ⁿ / [(1 + r)ⁿ − 1]<br>PMT = cicilan per bulan  |  P = pokok pinjaman<br>r = bunga per bulan  |  n = jumlah bulan</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        pokok   = st.number_input("Pokok Pinjaman (Rp)", min_value=0, value=50_000_000, step=5_000_000, format="%d")
    with col2:
        bunga_t = st.slider("Suku Bunga per Tahun (%)", 1, 30, 6,
                            help="KUR biasanya 6%/tahun. Pinjaman bank umum 10–18%. P2P Lending 12–24%.")
    with col3:
        tenor   = st.slider("Tenor Pinjaman (bulan)", 6, 120, 36)

    r_m  = bunga_t / 100 / 12
    if r_m > 0:
        pmt = pokok * r_m * (1 + r_m) ** tenor / ((1 + r_m) ** tenor - 1)
    else:
        pmt = pokok / tenor

    total_bayar  = pmt * tenor
    total_bunga  = total_bayar - pokok
    bunga_per_pct = total_bunga / pokok * 100

    # Ringkasan
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f'<div class="result-card"><div class="result-val">Rp {pmt:,.0f}</div><div class="result-label">Cicilan per Bulan</div></div>', unsafe_allow_html=True)
    col2.markdown(f'<div class="result-card"><div class="result-val">Rp {total_bayar:,.0f}</div><div class="result-label">Total yang Dibayar</div></div>', unsafe_allow_html=True)
    col3.markdown(f'<div class="result-card"><div class="result-val" style="color:#c05858 !important">Rp {total_bunga:,.0f}</div><div class="result-label">Total Bunga Dibayar</div></div>', unsafe_allow_html=True)
    col4.markdown(f'<div class="result-card"><div class="result-val">{bunga_per_pct:.1f}%</div><div class="result-label">Bunga / Pokok Pinjaman</div></div>', unsafe_allow_html=True)

    # Bangun tabel amortisasi
    rows_amort = []
    sisa = pokok
    for m in range(1, tenor + 1):
        bunga_m = sisa * r_m
        pokok_m = pmt - bunga_m
        sisa    = max(0, sisa - pokok_m)
        rows_amort.append({
            "Bulan": m,
            "Cicilan (Rp)":      round(pmt),
            "Pokok (Rp)":        round(pokok_m),
            "Bunga (Rp)":        round(bunga_m),
            "Sisa Pinjaman (Rp)":round(sisa),
        })

    df_amort = pd.DataFrame(rows_amort)

    # Grafik pokok vs bunga
    st.markdown('<div class="section-title">📊 Grafik Komposisi Cicilan</div>', unsafe_allow_html=True)
    fig_am = go.Figure()
    fig_am.add_trace(go.Bar(
        name="Pokok", x=df_amort["Bulan"], y=df_amort["Pokok (Rp)"],
        marker_color="#3d6090", opacity=0.80
    ))
    fig_am.add_trace(go.Bar(
        name="Bunga", x=df_amort["Bulan"], y=df_amort["Bunga (Rp)"],
        marker_color="#a04040", opacity=0.70
    ))
    fig_am.add_trace(go.Scatter(
        name="Sisa Pinjaman", x=df_amort["Bulan"], y=df_amort["Sisa Pinjaman (Rp)"],
        mode="lines", yaxis="y2",
        line=dict(color="#7a9ab8", width=1.5, dash="dot")
    ))
    fig_am.update_layout(
        barmode="stack", template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=310, margin=dict(l=10, r=10, t=20, b=30),
        legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(title="Bulan ke-", tickfont=dict(size=9, color="#5a6880"),
                   gridcolor="rgba(255,255,255,0.04)"),
        yaxis=dict(title="Nilai Cicilan (Rp)", tickfont=dict(size=9, color="#5a6880"),
                   gridcolor="rgba(255,255,255,0.04)", zeroline=False),
        yaxis2=dict(title="Sisa Pinjaman (Rp)", overlaying="y", side="right",
                    tickfont=dict(size=9, color="#7a9ab8"), gridcolor="rgba(0,0,0,0)"),
    )
    st.plotly_chart(fig_am, use_container_width=True)
    st.markdown(
        '<p style="font-size:0.78rem;color:#3a5060 !important;font-style:italic;margin-top:-0.5rem">'
        'Batang biru = porsi pokok; batang merah = porsi bunga. Perhatikan bunga mengecil dan pokok membesar seiring waktu.</p>',
        unsafe_allow_html=True
    )

    # Tabel amortisasi — tampilkan dengan format Rp
    st.markdown('<div class="section-title">📋 Tabel Amortisasi Lengkap</div>', unsafe_allow_html=True)

    MAX_ROWS = 36
    tampil = min(len(df_amort), MAX_ROWS)

    hc = st.columns([1, 2, 2, 2, 2.5])
    for col, hdr in zip(hc, ["Bulan", "Cicilan (Rp)", "Pokok (Rp)", "Bunga (Rp)", "Sisa Pinjaman (Rp)"]):
        col.markdown(f'<p class="amort-header">{hdr}</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    for _, row in df_amort.head(tampil).iterrows():
        rc = st.columns([1, 2, 2, 2, 2.5])
        rc[0].markdown(f'<p class="amort-row">{int(row["Bulan"])}</p>', unsafe_allow_html=True)
        rc[1].markdown(f'<p class="amort-row-hl">{row["Cicilan (Rp)"]:,.0f}</p>', unsafe_allow_html=True)
        rc[2].markdown(f'<p class="amort-row" style="color:#5a7a90 !important">{row["Pokok (Rp)"]:,.0f}</p>', unsafe_allow_html=True)
        rc[3].markdown(f'<p class="amort-row" style="color:#8a5050 !important">{row["Bunga (Rp)"]:,.0f}</p>', unsafe_allow_html=True)
        rc[4].markdown(f'<p class="amort-row">{row["Sisa Pinjaman (Rp)"]:,.0f}</p>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if len(df_amort) > MAX_ROWS:
        st.markdown(
            f'<p style="font-size:0.78rem;color:#3a5060 !important;text-align:center;margin-top:0.3rem">'
            f'Tabel menampilkan {MAX_ROWS} dari {tenor} bulan. Download CSV untuk data lengkap.</p>',
            unsafe_allow_html=True
        )

    # Download
    df_dl = df_amort.copy()
    for c in ["Cicilan (Rp)", "Pokok (Rp)", "Bunga (Rp)", "Sisa Pinjaman (Rp)"]:
        df_dl[c] = df_dl[c].apply(lambda x: f"Rp {x:,.0f}")
    csv = df_dl.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Unduh Tabel Amortisasi (.csv)", data=csv, file_name="amortisasi_pinjaman.csv", mime="text/csv")

    # Informasi KUR
    st.markdown('<div class="section-title">📌 Referensi: Program Pinjaman untuk UMKM</div>', unsafe_allow_html=True)
    kur_data = [
        ("🏦 KUR Mikro",     "s.d. Rp 100 juta",   "6% / tahun",  "Maks. 36 bulan", "BRI, BNI, Mandiri, BSI — tanpa agunan"),
        ("🏦 KUR Kecil",     "Rp 100jt – Rp 500jt","6% / tahun",  "Maks. 60 bulan", "Dengan agunan, untuk usaha berkembang"),
        ("💻 P2P Lending",   "Rp 5jt – Rp 2 miliar","12–24% / tahun","6–36 bulan",  "Modalku, Investree, Akseleran — proses digital"),
        ("🏛️ Hibah UMKM",   "Bervariasi",           "0% (hibah)",  "Tidak ada",      "Kemenkop UKM, BUMN — berbasis kompetisi"),
    ]
    hc2 = st.columns([1.5, 1.8, 1.4, 1.4, 2.8])
    for col, hdr in zip(hc2, ["Program", "Plafon", "Bunga", "Tenor", "Keterangan"]):
        col.markdown(f'<p class="amort-header">{hdr}</p>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    for nm, plafon, bunga, tnr, ket in kur_data:
        rc2 = st.columns([1.5, 1.8, 1.4, 1.4, 2.8])
        rc2[0].markdown(f'<p class="amort-row-hl" style="font-size:0.82rem">{nm}</p>', unsafe_allow_html=True)
        rc2[1].markdown(f'<p class="amort-row">{plafon}</p>', unsafe_allow_html=True)
        rc2[2].markdown(f'<p class="amort-row">{bunga}</p>', unsafe_allow_html=True)
        rc2[3].markdown(f'<p class="amort-row">{tnr}</p>', unsafe_allow_html=True)
        rc2[4].markdown(f'<p class="amort-row" style="color:#445060 !important;font-size:0.8rem">{ket}</p>', unsafe_allow_html=True)
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="warn-box"><p class="warn-text">'
        '⚠️ Suku bunga dan plafon KUR dapat berubah sewaktu-waktu mengikuti kebijakan pemerintah. '
        'Verifikasi informasi terkini langsung ke bank penyalur atau situs Kemenkop UKM.'
        '</p></div>',
        unsafe_allow_html=True
    )
