import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Simulasi Keuangan", page_icon="📊", layout="wide")

st.markdown("""
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
.mcard { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09);
         border-radius: 10px; padding: 1rem 1.1rem; text-align: center; margin-bottom: 0.5rem; }
.mval  { font-size: 1.25rem; font-weight: 700; color: #90b8d8 !important; }
.mlbl  { font-size: 0.73rem; color: #3a5870 !important; margin-top: 0.15rem; }
.rcard { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09);
         border-radius: 10px; padding: 0.9rem 1rem; margin-bottom: 0.45rem; }
.rval  { font-size: 1.2rem; font-weight: 700; }
.rlbl  { font-size: 0.74rem; color: #3a5870 !important; }
.rst   { font-size: 0.74rem; margin-top: 0.15rem; }
.ok-box  { background: rgba(60,160,100,0.07); border: 1px solid rgba(60,160,100,0.2);  border-radius: 9px; padding: 0.75rem 1rem; margin: 0.4rem 0; }
.wn-box  { background: rgba(200,140,40,0.07); border: 1px solid rgba(200,140,40,0.2);  border-radius: 9px; padding: 0.75rem 1rem; margin: 0.4rem 0; }
.er-box  { background: rgba(190,60,60,0.07);  border: 1px solid rgba(190,60,60,0.2);   border-radius: 9px; padding: 0.75rem 1rem; margin: 0.4rem 0; }
.concept { background: rgba(40,70,120,0.1); border: 1px solid rgba(80,130,200,0.18);
           border-radius: 9px; padding: 0.7rem 1rem; margin: 0.35rem 0 0.7rem 0; }
.concept p { font-size: 0.86rem; color: #6882a0 !important; margin: 0; }
.formula { background: rgba(40,70,120,0.12); border: 1px solid rgba(80,130,200,0.2);
           border-left: 3px solid rgba(80,130,200,0.45); border-radius: 0 8px 8px 0;
           padding: 0.6rem 0.9rem; margin: 0.3rem 0 0.6rem 0;
           font-family: 'Courier New', monospace; font-size: 0.87rem; color: #80a8cc !important; line-height: 1.7; }
.col-h { font-size: 0.71rem; font-weight: 600; color: #3a5870 !important;
         text-transform: uppercase; letter-spacing: 0.4px; margin: 0; }
.rw0  { font-size: 0.85rem; color: #8898ac !important; margin: 0; padding: 0.2rem 0; }
.rw1  { font-size: 0.87rem; color: #a0b8cc !important; font-weight: 600; margin: 0; padding: 0.2rem 0; }
.rw2  { font-size: 0.84rem; color: #6878a0 !important; margin: 0; padding: 0.2rem 0; }
.divl { border-top: 1px solid rgba(255,255,255,0.06); margin: 0.18rem 0; }
.sub-h { font-size: 0.82rem; font-weight: 600; color: #5a7888 !important; margin: 0.9rem 0 0.4rem 0; }
.note  { font-size: 0.76rem; color: #3a5060 !important; font-style: italic; margin-top: 0.35rem; }
.pill-g { display:inline-block; background:rgba(74,200,120,0.11); color:#5eaa7a !important;
          border:1px solid rgba(74,200,120,0.22); border-radius:10px; padding:0.1rem 0.55rem;
          font-size:0.71rem; font-weight:600; }
.pill-a { display:inline-block; background:rgba(210,165,55,0.11); color:#b89438 !important;
          border:1px solid rgba(210,165,55,0.22); border-radius:10px; padding:0.1rem 0.55rem;
          font-size:0.71rem; font-weight:600; }
.pill-r { display:inline-block; background:rgba(200,75,75,0.11); color:#c05858 !important;
          border:1px solid rgba(200,75,75,0.22); border-radius:10px; padding:0.1rem 0.55rem;
          font-size:0.71rem; font-weight:600; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-size:1.55rem;font-weight:700;color:#c4d4e4;margin:0">📊 Simulasi Keuangan Bisnis</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#566880;font-size:0.86rem;margin:0.3rem 0 0 0">BEP · Cashflow · HPP · Rasio Keuangan · NPV · IRR · Capital Budgeting · Modal Kerja · CAPM · dan lebih banyak lagi.</p>', unsafe_allow_html=True)
st.markdown("---")

# ══════════════════════════════════════════════════════════════════
# SECTION 1 — INFORMASI DASAR
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="sec">1️⃣ Informasi Dasar Bisnis</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    nama_bisnis  = st.text_input("Nama Bisnis", placeholder="Contoh: Warung Kopi Nusantara")
    jenis_bisnis = st.selectbox("Jenis Bisnis", ["Kuliner/F&B","Fashion/Pakaian","Jasa/Servis","Teknologi/Digital","Pendidikan","Retail/Toko","Lainnya"])
with col2:
    modal_awal = st.number_input("Modal Awal / Investasi (Rp)", min_value=0, value=50_000_000, step=1_000_000, format="%d")
    periode    = st.selectbox("Periode Proyeksi", ["6 Bulan","12 Bulan","24 Bulan","60 Bulan (5 Tahun)"])

# ══════════════════════════════════════════════════════════════════
# SECTION 2 — HPP
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="sec">2️⃣ HPP — Harga Pokok Produksi</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.82rem;color:#3a5870 !important;margin:0 0 0.4rem 0">Rincian biaya untuk membuat satu unit produk/jasa</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    bahan_baku              = st.number_input("Bahan Baku per Unit (Rp)",            min_value=0, value=8_000,  step=500,  format="%d")
    tenaga_kerja_langsung   = st.number_input("Tenaga Kerja Langsung per Unit (Rp)", min_value=0, value=2_000,  step=500,  format="%d")
with col2:
    overhead_pabrik         = st.number_input("Overhead Pabrik per Unit (Rp)",       min_value=0, value=1_500,  step=500,  format="%d")
    biaya_packing           = st.number_input("Packing / Distribusi per Unit (Rp)",  min_value=0, value=500,   step=100,  format="%d")
with col3:
    hpp_total = bahan_baku + tenaga_kerja_langsung + overhead_pabrik + biaya_packing
    st.markdown(f'<div class="mcard" style="margin-top:1.8rem"><div class="mval">Rp {hpp_total:,.0f}</div><div class="mlbl">Total HPP per Unit</div></div>', unsafe_allow_html=True)
    harga_jual = st.number_input("Harga Jual per Unit (Rp)", min_value=0, value=25_000, step=1_000, format="%d")

# ══════════════════════════════════════════════════════════════════
# SECTION 3 — BIAYA TETAP
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="sec">3️⃣ Biaya Tetap Bulanan</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    sewa              = st.number_input("Sewa Tempat (Rp/bln)",     min_value=0, value=1_500_000, step=100_000, format="%d")
    gaji              = st.number_input("Gaji Karyawan (Rp/bln)",   min_value=0, value=3_000_000, step=100_000, format="%d")
with col2:
    listrik           = st.number_input("Listrik & Air (Rp/bln)",   min_value=0, value=400_000,   step=50_000,  format="%d")
    internet          = st.number_input("Internet/Telepon (Rp/bln)",min_value=0, value=200_000,   step=50_000,  format="%d")
with col3:
    depresiasi        = st.number_input("Depresiasi Aset (Rp/bln)", min_value=0, value=500_000,   step=100_000, format="%d")
    biaya_tetap_lain  = st.number_input("Biaya Tetap Lain (Rp/bln)",min_value=0, value=400_000,   step=100_000, format="%d")
total_biaya_tetap = sewa + gaji + listrik + internet + depresiasi + biaya_tetap_lain

# ══════════════════════════════════════════════════════════════════
# SECTION 4 — VOLUME PENJUALAN
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="sec">4️⃣ Volume Penjualan & Pertumbuhan</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    estimasi_penjualan = st.number_input("Estimasi Penjualan/Bulan (unit)", min_value=1, value=400, step=10, format="%d")
with col2:
    pertumbuhan   = st.slider("Pertumbuhan Penjualan (%/bulan)", 0, 20, 5)
with col3:
    discount_rate = st.slider("Discount Rate / WACC (%/tahun)", 1, 30, 12,
                              help="Digunakan untuk menghitung NPV. Umumnya 10-15% untuk UMKM.")

# ══════════════════════════════════════════════════════════════════
# SECTION 5 — NERACA & MODAL KERJA  (+hutang_usaha untuk CCC)
# ══════════════════════════════════════════════════════════════════
st.markdown('<div class="sec">5️⃣ Data Neraca & Modal Kerja</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    kas              = st.number_input("Kas & Setara Kas (Rp)",    min_value=0, value=10_000_000, step=500_000,   format="%d")
    piutang          = st.number_input("Piutang Usaha (Rp)",       min_value=0, value=5_000_000,  step=500_000,   format="%d")
    persediaan       = st.number_input("Persediaan/Stok (Rp)",     min_value=0, value=8_000_000,  step=500_000,   format="%d")
    hutang_usaha     = st.number_input("Hutang Usaha / AP (Rp)",   min_value=0, value=3_000_000,  step=500_000,   format="%d",
                                       help="Accounts Payable — hutang kepada pemasok/supplier. Digunakan untuk menghitung DPO & Cash Conversion Cycle.")
with col2:
    aktiva_tetap          = st.number_input("Aktiva Tetap Bersih (Rp)",      min_value=0, value=30_000_000, step=1_000_000, format="%d")
    hutang_lancar         = st.number_input("Hutang Lancar (Rp)",             min_value=0, value=6_000_000,  step=500_000,   format="%d")
    hutang_jangka_panjang = st.number_input("Hutang Jangka Panjang (Rp)",    min_value=0, value=15_000_000, step=1_000_000, format="%d")
with col3:
    ekuitas           = st.number_input("Modal / Ekuitas (Rp)",   min_value=1, value=modal_awal,  step=1_000_000, format="%d")
    suku_bunga_hutang = st.slider("Suku Bunga Hutang (%/tahun)", 0, 30, 10,
                                  help="Bunga pinjaman bank atau kreditur")

# ══════════════════════════════════════════════════════════════════
# EXPANDER A — PARAMETER CAPM (BARU)
# ══════════════════════════════════════════════════════════════════
with st.expander("📊 Parameter CAPM — Analisis Risiko & Return Pasar (opsional, untuk Tab Risiko)"):
    st.markdown('<p style="font-size:0.83rem;color:#4a6a80 !important;margin:0 0 0.6rem 0">Isi parameter ini untuk mendapatkan analisis CAPM dan diversifikasi portofolio di Tab Risiko.</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        rf   = st.slider("Risk-Free Rate / BI Rate (%/thn)", 1, 15, 6,
                         help="Tingkat bunga bebas risiko, umumnya mengacu pada BI Rate atau imbal hasil SBN (Surat Berharga Negara).")
    with col2:
        rm   = st.slider("Expected Market Return (%/thn)", 5, 30, 15,
                         help="Estimasi return pasar (IHSG). Secara historis rata-rata sekitar 12–18% per tahun.")
    with col3:
        beta = st.slider("Beta (β) Bisnis", 0.1, 3.0, 1.0, step=0.1,
                         help="β = 1.0 → risiko sama dengan pasar. β < 1 → lebih stabil. β > 1 → lebih berisiko/volatil.")

# ══════════════════════════════════════════════════════════════════
# EXPANDER B — DATA PERIODE SEBELUMNYA (BARU)
# ══════════════════════════════════════════════════════════════════
prev_data_on = False
prev_rev = prev_cogs = prev_net_inc = 0
prev_cash = prev_ar = prev_inv = prev_fixed = 0
prev_cl = prev_ltd = prev_equity = 1

with st.expander("📅 Data Periode Sebelumnya — Perbandingan Rasio Multi-Periode (opsional, untuk Tab Rasio)"):
    st.markdown('<p style="font-size:0.83rem;color:#4a6a80 !important;margin:0 0 0.6rem 0">Isi data keuangan periode lalu untuk menampilkan perbandingan tren rasio di Tab Analisis Rasio.</p>', unsafe_allow_html=True)
    prev_data_on = st.checkbox("Aktifkan perbandingan dengan periode sebelumnya", value=False)
    if prev_data_on:
        prev_label = st.text_input("Label Periode Sebelumnya", value="Tahun Lalu", key="prev_lbl")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<p class="sub-h">📋 Laporan Laba Rugi</p>', unsafe_allow_html=True)
            prev_rev     = st.number_input("Pendapatan (prev)",     min_value=0, value=80_000_000,  step=1_000_000, format="%d", key="prev_rev")
            prev_cogs    = st.number_input("HPP (prev)",            min_value=0, value=48_000_000,  step=1_000_000, format="%d", key="prev_cogs")
            prev_net_inc = st.number_input("Laba Bersih (prev)",    min_value=0, value=8_000_000,   step=500_000,   format="%d", key="prev_ni")
        with col2:
            st.markdown('<p class="sub-h">📋 Neraca</p>', unsafe_allow_html=True)
            prev_cash    = st.number_input("Kas (prev)",            min_value=0, value=8_000_000,   step=500_000,   format="%d", key="prev_cash")
            prev_ar      = st.number_input("Piutang (prev)",        min_value=0, value=3_000_000,   step=500_000,   format="%d", key="prev_ar")
            prev_inv     = st.number_input("Persediaan (prev)",     min_value=0, value=5_000_000,   step=500_000,   format="%d", key="prev_inv")
            prev_fixed   = st.number_input("Aktiva Tetap (prev)",   min_value=0, value=28_000_000,  step=1_000_000, format="%d", key="prev_fix")
            prev_cl      = st.number_input("Hutang Lancar (prev)",  min_value=1, value=5_000_000,   step=500_000,   format="%d", key="prev_cl")
            prev_ltd     = st.number_input("Hutang JP (prev)",      min_value=0, value=12_000_000,  step=1_000_000, format="%d", key="prev_ltd")
            prev_equity  = st.number_input("Ekuitas (prev)",        min_value=1, value=22_000_000,  step=1_000_000, format="%d", key="prev_eq")

# ══════════════════════════════════════════════════════════════════
# TOMBOL UTAMA
# ══════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Hitung Analisis Lengkap!"):

    # ── KALKULASI DASAR ──────────────────────────────────────────
    margin_per_unit      = harga_jual - hpp_total
    pendapatan_bulan1    = harga_jual * estimasi_penjualan
    biaya_variabel_total = hpp_total  * estimasi_penjualan
    laba_kotor           = pendapatan_bulan1 - biaya_variabel_total
    laba_bersih          = laba_kotor - total_biaya_tetap
    gross_margin_pct     = laba_kotor / pendapatan_bulan1 * 100 if pendapatan_bulan1 > 0 else 0

    if harga_jual <= hpp_total:
        st.markdown('<div class="er-box"><p style="margin:0;font-size:0.87rem;color:#c05858 !important">🚨 <strong>Peringatan:</strong> Harga jual lebih rendah dari HPP — setiap unit yang dijual merugi!</p></div>', unsafe_allow_html=True)

    bep_unit   = total_biaya_tetap / margin_per_unit if margin_per_unit > 0 else 0
    bep_rupiah = bep_unit * harga_jual
    roi        = laba_bersih / modal_awal * 100 if modal_awal > 0 else 0
    payback    = modal_awal / laba_bersih   if laba_bersih > 0 else 999

    # ── CASHFLOW & NPV ───────────────────────────────────────────
    bulan_map = {"6 Bulan":6,"12 Bulan":12,"24 Bulan":24,"60 Bulan (5 Tahun)":60}
    n_bulan   = bulan_map[periode]
    r_monthly = discount_rate / 100 / 12

    bulan_list, pend_list, biaya_list, laba_list, kumul_list, dcf_list = [], [], [], [], [], []
    kumulatif  = -modal_awal
    npv        = -modal_awal
    cashflows  = [-modal_awal]

    for i in range(1, n_bulan + 1):
        faktor   = (1 + pertumbuhan / 100) ** (i - 1)
        unit_i   = estimasi_penjualan * faktor
        pend_i   = harga_jual  * unit_i
        var_i    = hpp_total   * unit_i
        laba_i   = pend_i - var_i - total_biaya_tetap
        kumulatif += laba_i
        pv_cf    = laba_i / (1 + r_monthly) ** i
        npv      += pv_cf
        bulan_list.append(f"Bln {i}"); pend_list.append(round(pend_i))
        biaya_list.append(round(var_i + total_biaya_tetap)); laba_list.append(round(laba_i))
        kumul_list.append(round(kumulatif)); dcf_list.append(round(pv_cf))
        cashflows.append(laba_i)

    df = pd.DataFrame({"Bulan":bulan_list,"Pendapatan":pend_list,"Total Biaya":biaya_list,
                        "Laba Bersih":laba_list,"Kumulatif":kumul_list,"PV CashFlow":dcf_list})

    def hitung_irr(cfs, guess=0.01):
        r = guess
        for _ in range(1000):
            npv_r = sum(cf/(1+r)**t for t,cf in enumerate(cfs))
            dnpv  = sum(-t*cf/(1+r)**(t+1) for t,cf in enumerate(cfs))
            if dnpv == 0: break
            r_new = r - npv_r/dnpv
            if abs(r_new-r) < 1e-7: return r_new
            r = r_new
        return r
    try:
        irr_monthly = hitung_irr(cashflows)
        irr_annual  = ((1+irr_monthly)**12 - 1) * 100
    except:
        irr_annual = 0

    # ── PROFITABILITY INDEX (BARU) ────────────────────────────────
    pv_future_cf = npv + modal_awal     # total PV semua arus kas masa depan
    pi           = pv_future_cf / modal_awal if modal_awal > 0 else 0

    # ── RASIO KEUANGAN ───────────────────────────────────────────
    aktiva_lancar     = kas + piutang + persediaan
    total_aktiva      = aktiva_lancar + aktiva_tetap
    total_hutang      = hutang_lancar + hutang_jangka_panjang
    current_ratio     = aktiva_lancar / hutang_lancar if hutang_lancar > 0 else 999
    quick_ratio       = (aktiva_lancar - persediaan) / hutang_lancar if hutang_lancar > 0 else 999
    debt_to_equity    = total_hutang / ekuitas if ekuitas > 0 else 0
    debt_ratio        = total_hutang / total_aktiva if total_aktiva > 0 else 0
    pendapatan_tahunan     = pendapatan_bulan1 * 12
    laba_bersih_tahunan    = laba_bersih * 12
    net_profit_margin      = laba_bersih / pendapatan_bulan1 * 100 if pendapatan_bulan1 > 0 else 0
    roa                    = laba_bersih_tahunan / total_aktiva * 100 if total_aktiva > 0 else 0
    roe                    = laba_bersih_tahunan / ekuitas * 100 if ekuitas > 0 else 0
    asset_turnover         = pendapatan_tahunan / total_aktiva if total_aktiva > 0 else 0
    cogs_tahunan           = biaya_variabel_total * 12
    inventory_turnover     = cogs_tahunan / persediaan if persediaan > 0 else 0
    dso                    = piutang / (pendapatan_tahunan / 365) if pendapatan_tahunan > 0 else 0

    # ── CASH CONVERSION CYCLE (BARU) ─────────────────────────────
    dio = persediaan   / (cogs_tahunan / 365)        if cogs_tahunan > 0 else 0
    dpo = hutang_usaha / (cogs_tahunan / 365)        if cogs_tahunan > 0 else 0
    ccc = dio + dso - dpo

    # ── TVM ──────────────────────────────────────────────────────
    r_tahunan  = discount_rate / 100
    fv_5yr     = modal_awal * (1 + r_tahunan) ** 5
    pv_val     = modal_awal / (1 + r_tahunan) ** 5
    laba_tahunan = laba_bersih * 12
    if r_tahunan > 0 and n_bulan >= 12:
        n_tahun  = n_bulan // 12
        pvifa    = (1 - (1 + r_tahunan) ** (-n_tahun)) / r_tahunan
        pv_anuitas = laba_tahunan * pvifa
    else:
        pv_anuitas = laba_tahunan * (n_bulan / 12)

    # ── MODAL KERJA ──────────────────────────────────────────────
    modal_kerja_bersih = aktiva_lancar - hutang_lancar
    kas_minimum        = total_biaya_tetap * 2
    kas_surplus        = kas - kas_minimum

    # ── SUMBER PEMBIAYAAN ────────────────────────────────────────
    beban_bunga_tahunan  = hutang_jangka_panjang * suku_bunga_hutang / 100
    interest_coverage    = laba_bersih_tahunan / beban_bunga_tahunan if beban_bunga_tahunan > 0 else 999
    total_pendanaan      = ekuitas + total_hutang
    wacc_approx = ((ekuitas / total_pendanaan) * discount_rate +
                   (total_hutang / total_pendanaan) * suku_bunga_hutang * 0.8) if total_pendanaan > 0 else 0

    # ── RISIKO & LEVERAGE ─────────────────────────────────────────
    operating_leverage    = laba_kotor / laba_bersih if laba_bersih > 0 else 0
    margin_of_safety_unit = estimasi_penjualan - bep_unit
    margin_of_safety_pct  = margin_of_safety_unit / estimasi_penjualan * 100 if estimasi_penjualan > 0 else 0
    skenario = {
        "Pesimis (-20%)": laba_bersih * 0.8 - total_biaya_tetap * 0.05,
        "Normal":         laba_bersih,
        "Optimis (+20%)": laba_bersih * 1.2 + total_biaya_tetap * 0.05,
    }

    # ── CAPM (BARU) ───────────────────────────────────────────────
    market_risk_premium = (rm - rf) / 100
    capm_required       = rf/100 + beta * market_risk_premium   # required return per tahun
    capm_pct            = capm_required * 100
    actual_return       = roe / 100                             # gunakan ROE sebagai proxy
    alpha_jensen        = actual_return - capm_required         # Jensen's alpha

    # ── PREVIOUS PERIOD RATIOS (BARU) ─────────────────────────────
    if prev_data_on:
        prev_al    = prev_cash + prev_ar + prev_inv
        prev_ta    = prev_al + prev_fixed
        prev_th    = prev_cl + prev_ltd
        prev_cr    = prev_al / prev_cl            if prev_cl    > 0 else 0
        prev_qr    = (prev_al-prev_inv) / prev_cl if prev_cl    > 0 else 0
        prev_npm   = prev_net_inc / prev_rev * 100 if prev_rev   > 0 else 0
        prev_gm    = (prev_rev-prev_cogs)/prev_rev*100 if prev_rev > 0 else 0
        prev_roa_v = prev_net_inc / prev_ta * 100 if prev_ta    > 0 else 0
        prev_roe_v = prev_net_inc / prev_equity * 100 if prev_equity > 0 else 0
        prev_der_v = prev_th / prev_equity        if prev_equity > 0 else 0
        prev_at    = prev_rev / prev_ta            if prev_ta    > 0 else 0

    # ═══════════════════════════════════════════════════════════════
    # TAMPILKAN HASIL
    # ═══════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown(f'<p style="font-size:1.25rem;font-weight:700;color:#b8cce0;margin-bottom:0.3rem">📈 Hasil Analisis — {nama_bisnis or "Bisnis Anda"}</p>', unsafe_allow_html=True)

    tabs = st.tabs(["🏠 Ringkasan","📊 Cashflow","📐 Rasio Keuangan",
                    "⏳ Time Value of Money","💼 Capital Budgeting",
                    "🏦 Modal Kerja & Kas","💳 Sumber Pembiayaan","⚠️ Risiko & Return"])

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 1 — RINGKASAN                                    ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[0]:
        c1,c2,c3,c4 = st.columns(4)
        cards = [(f"Rp {laba_bersih:,.0f}","Laba Bersih/Bulan"),
                 (f"{bep_unit:,.0f} unit","BEP per Bulan"),
                 (f"{roi:.1f}%","ROI per Bulan"),
                 (f"{payback:.1f} bln" if payback<200 else "N/A","Payback Period")]
        for col,(val,lbl) in zip([c1,c2,c3,c4],cards):
            col.markdown(f'<div class="mcard"><div class="mval">{val}</div><div class="mlbl">{lbl}</div></div>', unsafe_allow_html=True)
        c1,c2,c3,c4 = st.columns(4)
        cards2 = [(f"Rp {hpp_total:,.0f}","HPP per Unit"),
                  (f"{gross_margin_pct:.1f}%","Gross Margin"),
                  (f"Rp {npv:,.0f}",f"NPV ({periode})"),
                  (f"{irr_annual:.1f}%/thn","IRR")]
        for col,(val,lbl) in zip([c1,c2,c3,c4],cards2):
            col.markdown(f'<div class="mcard"><div class="mval">{val}</div><div class="mlbl">{lbl}</div></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        layak = npv>0 and irr_annual>discount_rate and laba_bersih>0
        if layak:
            st.markdown(f'<div class="ok-box"><p style="margin:0;font-size:0.87rem;color:#4a9060 !important">✅ <strong>Bisnis {nama_bisnis or "Anda"} dinilai LAYAK secara finansial.</strong> NPV positif, IRR ({irr_annual:.1f}%) > Discount Rate ({discount_rate}%), laba bersih positif.</p></div>', unsafe_allow_html=True)
        elif laba_bersih>0:
            st.markdown(f'<div class="wn-box"><p style="margin:0;font-size:0.87rem;color:#9a7830 !important">🟡 <strong>Bisnis menghasilkan laba, namun perlu evaluasi lebih lanjut.</strong> Periksa NPV dan IRR.</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="er-box"><p style="margin:0;font-size:0.87rem;color:#c05858 !important">❌ <strong>Bisnis saat ini tidak layak.</strong> Tinjau kembali struktur biaya dan harga jual.</p></div>', unsafe_allow_html=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 2 — CASHFLOW & GRAFIK                            ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[1]:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(name="Pendapatan",x=df["Bulan"],y=df["Pendapatan"],marker_color="#3d6090",opacity=0.80))
        fig1.add_trace(go.Bar(name="Total Biaya",x=df["Bulan"],y=df["Total Biaya"],marker_color="#8a4040",opacity=0.75))
        fig1.add_trace(go.Scatter(name="Laba Bersih",x=df["Bulan"],y=df["Laba Bersih"],
                                  mode="lines+markers",line=dict(color="#5eaa7a",width=2)))
        fig1.update_layout(barmode="group",template="plotly_dark",paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",title=dict(text="Proyeksi Pendapatan vs Biaya",font=dict(color="#8090a8",size=12)),
            legend=dict(font=dict(color="#6878a0",size=11),bgcolor="rgba(0,0,0,0)"),
            margin=dict(l=10,r=10,t=40,b=30),height=300,
            xaxis=dict(tickfont=dict(size=9,color="#5a6880")),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)",tickfont=dict(size=9,color="#5a6880")))
        st.plotly_chart(fig1, use_container_width=True)
        colors = ["#c05858" if v<0 else "#4a9a6a" for v in df["Kumulatif"]]
        fig2 = go.Figure()
        fig2.add_hline(y=0,line_dash="dot",line_color="rgba(255,255,255,0.2)")
        fig2.add_trace(go.Scatter(x=df["Bulan"],y=df["Kumulatif"],fill="tozeroy",mode="lines+markers",
            line=dict(color="#6a9ad8",width=2),fillcolor="rgba(106,154,216,0.1)",
            marker=dict(size=5,color=colors)))
        fig2.update_layout(template="plotly_dark",paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
            title=dict(text="Kumulatif Keuntungan vs Modal Awal",font=dict(color="#8090a8",size=12)),
            margin=dict(l=10,r=10,t=40,b=30),height=280,
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)",tickfont=dict(size=9,color="#5a6880")))
        st.plotly_chart(fig2, use_container_width=True)
        df_disp = df.copy()
        for c in ["Pendapatan","Total Biaya","Laba Bersih","Kumulatif","PV CashFlow"]:
            df_disp[c] = df_disp[c].apply(lambda x: f"Rp {x:,.0f}")
        st.dataframe(df_disp, use_container_width=True, hide_index=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 3 — ANALISIS RASIO + MULTI-PERIODE (BARU)        ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[2]:
        def rc(label, value, satuan, status_text, color):
            return f"""<div class="rcard">
                <div class="rval" style="color:{color}">{value} {satuan}</div>
                <div class="rlbl">{label}</div>
                <div class="rst" style="color:{color}">{'✅' if color=='#5eaa7a' else '⚠️' if color=='#b89438' else '❌'} {status_text}</div>
            </div>"""

        st.markdown('<div class="sec">🔵 Likuiditas</div>', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        cr_c = "#5eaa7a" if current_ratio>=2 else "#b89438" if current_ratio>=1 else "#c05858"
        qr_c = "#5eaa7a" if quick_ratio>=1  else "#b89438" if quick_ratio>=0.7 else "#c05858"
        with c1: st.markdown(rc("Current Ratio",f"{current_ratio:.2f}x","","Sangat Baik"if current_ratio>=2 else"Cukup"if current_ratio>=1 else"Kurang",cr_c),unsafe_allow_html=True)
        with c2: st.markdown(rc("Quick Ratio",f"{quick_ratio:.2f}x","","Baik (≥1)"if quick_ratio>=1 else"Cukup"if quick_ratio>=0.7 else"Perhatian",qr_c),unsafe_allow_html=True)
        with c3: st.markdown(rc("Modal Kerja Bersih",f"Rp {modal_kerja_bersih:,.0f}","","Aktiva Lancar − Hutang Lancar","#7a9ab8"),unsafe_allow_html=True)

        st.markdown('<div class="sec">🟡 Profitabilitas</div>', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        npm_c = "#5eaa7a" if net_profit_margin>=15 else "#b89438" if net_profit_margin>=5 else "#c05858"
        roa_c = "#5eaa7a" if roa>=10 else "#b89438" if roa>=5 else "#c05858"
        roe_c = "#5eaa7a" if roe>=15 else "#b89438" if roe>=8 else "#c05858"
        with c1: st.markdown(rc("Net Profit Margin",f"{net_profit_margin:.1f}%","","Baik ≥15%"if net_profit_margin>=15 else"Sedang"if net_profit_margin>=5 else"Rendah",npm_c),unsafe_allow_html=True)
        with c2: st.markdown(rc("ROA",f"{roa:.1f}%","/thn","Baik ≥10%"if roa>=10 else"Sedang"if roa>=5 else"Rendah",roa_c),unsafe_allow_html=True)
        with c3: st.markdown(rc("ROE",f"{roe:.1f}%","/thn","Baik ≥15%"if roe>=15 else"Sedang"if roe>=8 else"Rendah",roe_c),unsafe_allow_html=True)

        st.markdown('<div class="sec">🔴 Solvabilitas & Aktivitas</div>', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        dte_c = "#5eaa7a" if debt_to_equity<=1 else "#b89438" if debt_to_equity<=2 else "#c05858"
        dr_c  = "#5eaa7a" if debt_ratio<=0.5 else "#b89438" if debt_ratio<=0.7 else "#c05858"
        at_c  = "#5eaa7a" if asset_turnover>=1 else "#b89438" if asset_turnover>=0.5 else "#c05858"
        with c1: st.markdown(rc("Debt to Equity",f"{debt_to_equity:.2f}x","","Sehat ≤1"if debt_to_equity<=1 else"Perhatian"if debt_to_equity<=2 else"Berisiko",dte_c),unsafe_allow_html=True)
        with c2: st.markdown(rc("Asset Turnover",f"{asset_turnover:.2f}x","/thn","Efisien ≥1"if asset_turnover>=1 else"Cukup"if asset_turnover>=0.5 else"Rendah",at_c),unsafe_allow_html=True)
        with c3:
            dso_c = "#5eaa7a" if dso<=30 else "#b89438" if dso<=60 else "#c05858"
            st.markdown(rc("DSO",f"{dso:.0f}","hari","Ideal ≤30 hr"if dso<=30 else"Cukup"if dso<=60 else"Tinggi",dso_c),unsafe_allow_html=True)

        # ── PERBANDINGAN MULTI-PERIODE (BARU) ─────────────────────
        if prev_data_on:
            st.markdown('<div class="sec">📅 Perbandingan Rasio Multi-Periode (BARU)</div>', unsafe_allow_html=True)

            curr_rasio = {
                "Gross Margin (%)":        gross_margin_pct,
                "Net Profit Margin (%)":   net_profit_margin,
                "ROA (%)":                 roa,
                "ROE (%)":                 roe,
                "Current Ratio (x)":       current_ratio,
                "Quick Ratio (x)":         quick_ratio,
                "Debt to Equity (x)":      debt_to_equity,
                "Debt Ratio":              debt_ratio,
                "Asset Turnover (x)":      asset_turnover,
            }
            prev_rasio = {
                "Gross Margin (%)":        prev_gm,
                "Net Profit Margin (%)":   prev_npm,
                "ROA (%)":                 prev_roa_v,
                "ROE (%)":                 prev_roe_v,
                "Current Ratio (x)":       prev_cr,
                "Quick Ratio (x)":         prev_qr,
                "Debt to Equity (x)":      prev_der_v,
                "Debt Ratio":              prev_th/prev_ta if prev_ta>0 else 0,
                "Asset Turnover (x)":      prev_at,
            }
            lo_better = {"Debt to Equity (x)", "Debt Ratio"}

            hc = st.columns([3,1.8,1.8,1.6,1.8])
            for col,hdr in zip(hc,[f"Rasio",prev_label,"Periode Ini","Δ %","Tren"]):
                col.markdown(f'<p class="col-h">{hdr}</p>', unsafe_allow_html=True)
            st.markdown('<div class="divl"></div>', unsafe_allow_html=True)

            for name in curr_rasio:
                v_prev = prev_rasio[name]
                v_curr = curr_rasio[name]
                delta  = v_curr - v_prev
                dpct   = delta/abs(v_prev)*100 if v_prev!=0 else 0
                lower  = name in lo_better
                good   = (delta<0) if lower else (delta>0)
                arc    = "#5eaa7a" if good else "#c05858"
                sym    = "▲" if delta>0 else "▼"
                fmt    = ".1f" if "%" in name or "x)" in name else ".2f"
                rc2    = st.columns([3,1.8,1.8,1.6,1.8])
                rc2[0].markdown(f'<p class="rw0">{name}</p>', unsafe_allow_html=True)
                rc2[1].markdown(f'<p class="rw2" style="color:#6878a0 !important">{v_prev:{fmt}}</p>', unsafe_allow_html=True)
                rc2[2].markdown(f'<p class="rw1">{v_curr:{fmt}}</p>', unsafe_allow_html=True)
                rc2[3].markdown(f'<p style="font-size:0.83rem;color:{arc};font-weight:600;margin:0;padding:0.2rem 0">{sym} {abs(dpct):.1f}%</p>', unsafe_allow_html=True)
                pill_cls = "pill-g" if good else "pill-r"
                pill_lbl = "Membaik" if good else "Turun"
                rc2[4].markdown(f'<span class="{pill_cls}">{pill_lbl}</span>', unsafe_allow_html=True)
                st.markdown('<div class="divl"></div>', unsafe_allow_html=True)

            # Bar chart perbandingan
            keys_chart = ["Gross Margin (%)","Net Profit Margin (%)","ROA (%)","ROE (%)"]
            fig_mp = go.Figure()
            fig_mp.add_trace(go.Bar(name=prev_label,x=keys_chart,
                y=[prev_rasio[k] for k in keys_chart],marker_color="#3d6090",opacity=0.75))
            fig_mp.add_trace(go.Bar(name="Periode Ini",x=keys_chart,
                y=[curr_rasio[k] for k in keys_chart],marker_color="#4a9a6a",opacity=0.82))
            fig_mp.update_layout(barmode="group",template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",height=270,
                margin=dict(l=10,r=10,t=20,b=30),
                legend=dict(font=dict(color="#6878a0",size=11),bgcolor="rgba(0,0,0,0)"),
                yaxis=dict(ticksuffix="%",gridcolor="rgba(255,255,255,0.05)",tickfont=dict(size=9,color="#5a6880")))
            st.plotly_chart(fig_mp, use_container_width=True)
        else:
            st.markdown('<div class="concept" style="margin-top:1rem"><p>💡 Aktifkan <strong style="color:#8090b0">Data Periode Sebelumnya</strong> di expander atas untuk menampilkan perbandingan rasio tren antar periode.</p></div>', unsafe_allow_html=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 4 — TIME VALUE OF MONEY + PERPETUITAS + CICILAN  ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[3]:
        st.markdown('<div class="sec">⏳ Future Value & Present Value</div>', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="rcard"><div style="color:#6a8aaa;font-size:0.8rem;font-weight:600;text-transform:uppercase;letter-spacing:0.5px">Future Value (FV)</div><div style="color:#90b8d8;font-size:1.25rem;font-weight:700;margin:0.4rem 0">Rp {fv_5yr:,.0f}</div><div style="color:#3a5060;font-size:0.8rem">Modal awal Rp {modal_awal:,.0f} dalam 5 tahun<br>tingkat bunga {discount_rate}%/tahun<br><em>FV = PV × (1 + r)ⁿ</em></div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="rcard"><div style="color:#6a8aaa;font-size:0.8rem;font-weight:600;text-transform:uppercase;letter-spacing:0.5px">Present Value (PV)</div><div style="color:#90b8d8;font-size:1.25rem;font-weight:700;margin:0.4rem 0">Rp {pv_val:,.0f}</div><div style="color:#3a5060;font-size:0.8rem">Nilai kini dari Rp {modal_awal:,.0f} yang diterima 5 thn lagi<br>discount rate {discount_rate}%/tahun<br><em>PV = FV / (1 + r)ⁿ</em></div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="rcard"><div style="color:#6a8aaa;font-size:0.8rem;font-weight:600;text-transform:uppercase;letter-spacing:0.5px">PV Anuitas — Nilai Sekarang Aliran Laba</div><div style="color:#90b8d8;font-size:1.25rem;font-weight:700;margin:0.4rem 0">Rp {pv_anuitas:,.0f}</div><div style="color:#3a5060;font-size:0.8rem">Nilai sekarang dari laba bersih Rp {laba_tahunan:,.0f}/thn selama {n_bulan//12 if n_bulan>=12 else 1} tahun | rate {discount_rate}%/thn<br><em>PVA = PMT × [(1−(1+r)⁻ⁿ)/r]</em></div></div>', unsafe_allow_html=True)

        # Tabel compound interest
        tvm_data = []
        for y in range(1,11):
            fv_y = modal_awal*(1+r_tahunan)**y
            pv_y = modal_awal/(1+r_tahunan)**y
            tvm_data.append({"Tahun ke-":y,"Future Value (Rp)":f"Rp {fv_y:,.0f}","Present Value (Rp)":f"Rp {pv_y:,.0f}","Faktor (1+r)ⁿ":f"{(1+r_tahunan)**y:.4f}"})
        st.dataframe(pd.DataFrame(tvm_data), use_container_width=True, hide_index=True)

        # ── PERPETUITAS (BARU) ────────────────────────────────────
        st.markdown('<div class="sec">∞ Kalkulator Perpetuitas (BARU)</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">Perpetuitas</strong> adalah arus kas yang berlangsung selamanya tanpa batas waktu. Rumus: <strong>PV = C / r</strong>. Contoh: saham preferen, tanah sewaan abadi.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">Perpetuitas Biasa  : PV = C / r<br>Perpetuitas Tumbuh : PV = C / (r − g)  ← Gordon Growth Model<br>C = arus kas per tahun | r = discount rate | g = tingkat pertumbuhan (g &lt; r)</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Perpetuitas Biasa** *(arus kas tetap)*")
            c_p   = st.number_input("Arus Kas Tahunan (C)", min_value=0, value=5_000_000, step=500_000, format="%d", key="c_perp")
            r_p   = st.slider("Discount Rate (%)", 1, 30, discount_rate, key="r_perp")
            pv_p  = c_p / (r_p/100) if r_p > 0 else 0
            st.markdown(f'<div class="mcard"><div class="mval">Rp {pv_p:,.0f}</div><div class="mlbl">Present Value Perpetuitas</div></div>', unsafe_allow_html=True)
            st.markdown(f'<p class="note">Aset yang menghasilkan Rp {c_p:,.0f}/tahun selamanya bernilai Rp {pv_p:,.0f} hari ini.</p>', unsafe_allow_html=True)

        with c2:
            st.markdown("**Perpetuitas Bertumbuh** *(Gordon Growth Model)*")
            c_g   = st.number_input("Arus Kas Tahun Pertama (C₁)", min_value=0, value=5_000_000, step=500_000, format="%d", key="c_grow")
            r_g   = st.slider("Discount Rate r (%)", 1, 30, discount_rate, key="r_grow")
            g_g   = st.slider("Pertumbuhan g (%)", 0, 20, 5, key="g_grow")
            if r_g > g_g:
                pv_g = c_g / ((r_g - g_g)/100)
                st.markdown(f'<div class="mcard"><div class="mval">Rp {pv_g:,.0f}</div><div class="mlbl">PV Perpetuitas Bertumbuh</div></div>', unsafe_allow_html=True)
                st.markdown(f'<p class="note">Tumbuh {g_g}%/thn → nilai lebih tinggi dari perpetuitas biasa.</p>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="er-box"><p style="margin:0;font-size:0.83rem;color:#c05858 !important">⚠️ r harus lebih besar dari g. Jika g ≥ r, nilai menjadi tak terhingga.</p></div>', unsafe_allow_html=True)

        # ── KALKULATOR CICILAN PINJAMAN (BARU) ─────────────────────
        st.markdown('<div class="sec">🏦 Kalkulator Cicilan & Amortisasi Pinjaman (BARU)</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">PMT = P × r(1+r)ⁿ / [(1+r)ⁿ − 1]<br>PMT = cicilan per bulan | P = pokok pinjaman | r = bunga/bulan | n = jumlah bulan</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1: pokok_p   = st.number_input("Pokok Pinjaman (Rp)", min_value=0, value=50_000_000, step=5_000_000, format="%d", key="pok_p")
        with c2: bunga_kur = st.slider("Bunga per Tahun (%)", 1, 30, 6, help="KUR=6%, bank umum 10-18%", key="bng_kur")
        with c3: tenor_p   = st.slider("Tenor (bulan)", 6, 120, 36, key="tnr_p")

        r_cicil = bunga_kur/100/12
        if r_cicil > 0:
            pmt_cicil = pokok_p * r_cicil * (1+r_cicil)**tenor_p / ((1+r_cicil)**tenor_p - 1)
        else:
            pmt_cicil = pokok_p / tenor_p if tenor_p > 0 else 0
        total_bayar   = pmt_cicil * tenor_p
        total_bunga_c = total_bayar - pokok_p

        c1,c2,c3,c4 = st.columns(4)
        c1.markdown(f'<div class="mcard"><div class="mval">Rp {pmt_cicil:,.0f}</div><div class="mlbl">Cicilan/Bulan</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="mcard"><div class="mval">Rp {total_bayar:,.0f}</div><div class="mlbl">Total Dibayar</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="mcard"><div class="mval" style="color:#c05858 !important">Rp {total_bunga_c:,.0f}</div><div class="mlbl">Total Bunga</div></div>', unsafe_allow_html=True)
        c4.markdown(f'<div class="mcard"><div class="mval">{total_bunga_c/pokok_p*100:.1f}%</div><div class="mlbl">Bunga / Pokok</div></div>', unsafe_allow_html=True)

        # Tabel amortisasi (20 baris pertama)
        amort_rows = []
        sisa_p = pokok_p
        for m in range(1, tenor_p+1):
            bng_m  = sisa_p * r_cicil
            pok_m  = pmt_cicil - bng_m
            sisa_p = max(0, sisa_p - pok_m)
            amort_rows.append({"Bulan":m, "Cicilan (Rp)":round(pmt_cicil),
                                "Pokok (Rp)":round(pok_m), "Bunga (Rp)":round(bng_m),
                                "Sisa (Rp)":round(sisa_p)})
        df_am = pd.DataFrame(amort_rows)
        show = min(20, len(df_am))
        df_show = df_am.head(show).copy()
        for col in ["Cicilan (Rp)","Pokok (Rp)","Bunga (Rp)","Sisa (Rp)"]:
            df_show[col] = df_show[col].apply(lambda x: f"Rp {x:,.0f}")
        st.dataframe(df_show, use_container_width=True, hide_index=True)
        if len(df_am) > show:
            csv_am = df_am.to_csv(index=False).encode("utf-8")
            st.download_button("⬇ Unduh Tabel Lengkap (.csv)", data=csv_am,
                               file_name="amortisasi.csv", mime="text/csv")

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 5 — CAPITAL BUDGETING + PROFITABILITY INDEX      ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[4]:
        st.markdown('<div class="sec">💼 Penilaian Investasi</div>', unsafe_allow_html=True)
        npv_c = "#5eaa7a" if npv>0 else "#c05858"
        irr_c = "#5eaa7a" if irr_annual>discount_rate else "#c05858"
        pb_c  = "#5eaa7a" if payback<=24 else "#b89438" if payback<=48 else "#c05858"
        pi_c  = "#5eaa7a" if pi>1 else "#b89438" if pi>0.9 else "#c05858"

        c1,c2,c3,c4 = st.columns(4)
        with c1:
            st.markdown(f"""<div class="rcard">
                <div style="color:#6a8aaa;font-size:0.75rem;font-weight:600;letter-spacing:0.5px">NET PRESENT VALUE</div>
                <div style="color:{npv_c};font-size:1.2rem;font-weight:700;margin:0.3rem 0">Rp {npv:,.0f}</div>
                <div style="color:#3a5060;font-size:0.78rem">Rate: {discount_rate}% | {periode}<br>
                <strong style="color:{npv_c}">{"✅ TERIMA" if npv>0 else "❌ TOLAK"}</strong><br>
                <em>Σ[CFₜ/(1+r)ᵗ] − Investasi</em></div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""<div class="rcard">
                <div style="color:#6a8aaa;font-size:0.75rem;font-weight:600;letter-spacing:0.5px">IRR</div>
                <div style="color:{irr_c};font-size:1.2rem;font-weight:700;margin:0.3rem 0">{irr_annual:.2f}%/thn</div>
                <div style="color:#3a5060;font-size:0.78rem">Hurdle Rate: {discount_rate}%<br>
                <strong style="color:{irr_c}">{"✅ IRR > Hurdle" if irr_annual>discount_rate else "❌ IRR < Hurdle"}</strong><br>
                <em>r ketika NPV = 0</em></div>
            </div>""", unsafe_allow_html=True)
        with c3:
            st.markdown(f"""<div class="rcard">
                <div style="color:#6a8aaa;font-size:0.75rem;font-weight:600;letter-spacing:0.5px">PAYBACK PERIOD</div>
                <div style="color:{pb_c};font-size:1.2rem;font-weight:700;margin:0.3rem 0">{payback:.1f} bulan</div>
                <div style="color:#3a5060;font-size:0.78rem">≤24 bln: Cepat ✅<br>24-48: Normal ⚡<br>&gt;48: Lambat ❌<br>
                <em>Investasi / Laba/bln</em></div>
            </div>""", unsafe_allow_html=True)
        with c4:
            pi_status = "✅ TERIMA — PI > 1" if pi>1 else "⚡ Batas — PI ≈ 1" if pi>0.9 else "❌ TOLAK — PI < 1"
            st.markdown(f"""<div class="rcard" style="border-color:rgba({','.join(['74,200,120' if pi>1 else '200,165,55' if pi>0.9 else '200,75,75'])},0.3)">
                <div style="color:#6a8aaa;font-size:0.75rem;font-weight:600;letter-spacing:0.5px">PROFITABILITY INDEX ✨ BARU</div>
                <div style="color:{pi_c};font-size:1.2rem;font-weight:700;margin:0.3rem 0">{pi:.3f}</div>
                <div style="color:#3a5060;font-size:0.78rem">PV Arus Kas: Rp {pv_future_cf:,.0f}<br>
                <strong style="color:{pi_c}">{pi_status}</strong><br>
                <em>PI = 1 + NPV / Investasi</em></div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="concept" style="margin-top:0.5rem"><p><strong style="color:#8090b0">Profitability Index (PI)</strong> mengukur nilai yang diciptakan per Rupiah investasi. PI = 1.000 berarti impas; PI > 1 berarti setiap Rp 1 yang diinvestasikan menghasilkan lebih dari Rp 1 nilai kini. Berguna saat membandingkan beberapa proyek dengan modal terbatas — pilih yang PI-nya paling tinggi.</p></div>', unsafe_allow_html=True)

        # Tabel sensitivitas NPV
        st.markdown('<div class="sec">📋 Sensitivitas NPV terhadap Discount Rate</div>', unsafe_allow_html=True)
        sens = []
        for r_test in [5,8,10,12,15,18,20,25]:
            r_m = r_test/100/12
            npv_t = -modal_awal
            for i,cf in enumerate(cashflows[1:],1):
                npv_t += cf/(1+r_m)**i
            pi_t = (npv_t + modal_awal)/modal_awal if modal_awal>0 else 0
            sens.append({"Discount Rate":f"{r_test}%","NPV":f"Rp {npv_t:,.0f}",
                         "PI":f"{pi_t:.3f}","Keputusan":"✅ TERIMA" if npv_t>0 else "❌ TOLAK"})
        st.dataframe(pd.DataFrame(sens), use_container_width=True, hide_index=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 6 — MODAL KERJA + CASH CONVERSION CYCLE          ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[5]:
        c1,c2 = st.columns(2)
        with c1:
            kas_c = "#5eaa7a" if kas_surplus>0 else "#c05858"
            st.markdown(f"""<div class="rcard">
                <div style="color:#5a7888;font-size:0.82rem;font-weight:600;margin-bottom:0.5rem">💵 Posisi Kas</div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Kas Tersedia</span>
                    <span style="color:#90b8d8;font-weight:600;font-size:0.87rem">Rp {kas:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Kas Minimum (2× biaya tetap)</span>
                    <span style="color:#b89438;font-weight:600;font-size:0.87rem">Rp {kas_minimum:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;border-top:1px solid rgba(255,255,255,0.07);padding-top:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Surplus / Defisit</span>
                    <span style="color:{kas_c};font-weight:700;font-size:0.9rem">Rp {kas_surplus:,.0f}</span>
                </div>
                <div style="font-size:0.78rem;color:{kas_c};margin-top:0.4rem">
                {"✅ Kas mencukupi operasional" if kas_surplus>0 else "❌ Kas di bawah minimum — perlu tambahan modal"}
                </div>
            </div>""", unsafe_allow_html=True)
        with c2:
            nwc_c = "#5eaa7a" if modal_kerja_bersih>0 else "#c05858"
            st.markdown(f"""<div class="rcard">
                <div style="color:#5a7888;font-size:0.82rem;font-weight:600;margin-bottom:0.5rem">📦 Modal Kerja & Piutang</div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Modal Kerja Bersih (NWC)</span>
                    <span style="color:{nwc_c};font-weight:600;font-size:0.87rem">Rp {modal_kerja_bersih:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">DSO (Hari Piutang)</span>
                    <span style="color:{'#5eaa7a' if dso<=30 else '#b89438' if dso<=60 else '#c05858'};font-weight:600;font-size:0.87rem">{dso:.0f} hari</span>
                </div>
                <div style="display:flex;justify-content:space-between">
                    <span style="color:#3a5870;font-size:0.83rem">Inventory Turnover</span>
                    <span style="color:#7a9ab8;font-weight:600;font-size:0.87rem">{inventory_turnover:.1f}x/thn</span>
                </div>
            </div>""", unsafe_allow_html=True)

        # ── CASH CONVERSION CYCLE (BARU) ───────────────────────────
        st.markdown('<div class="sec">🔄 Cash Conversion Cycle (CCC) — BARU</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">CCC</strong> mengukur berapa hari siklus konversi kas bisnis — dari membayar supplier hingga menerima pembayaran dari pelanggan. Makin kecil (bahkan negatif) makin baik, karena berarti bisnis bisa menggunakan uang supplier sebelum harus membayar kembali.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">CCC = DIO + DSO − DPO<br>DIO = Days Inventory Outstanding = (Persediaan / HPP) × 365  → lama stok tersimpan<br>DSO = Days Sales Outstanding    = (Piutang / Pendapatan) × 365  → lama piutang tertagih<br>DPO = Days Payable Outstanding  = (Hutang Usaha / HPP) × 365  → lama membayar supplier</div>', unsafe_allow_html=True)

        ccc_c = "#5eaa7a" if ccc<=30 else "#b89438" if ccc<=60 else "#c05858"
        c1,c2,c3,c4 = st.columns(4)
        c1.markdown(f'<div class="mcard"><div class="mval" style="color:#7a9ab8 !important">{dio:.0f} hari</div><div class="mlbl">DIO — Lama Stok</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="mcard"><div class="mval" style="color:#7a9ab8 !important">{dso:.0f} hari</div><div class="mlbl">DSO — Lama Piutang</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="mcard"><div class="mval" style="color:#5eaa7a !important">{dpo:.0f} hari</div><div class="mlbl">DPO — Tunda Bayar Supplier</div></div>', unsafe_allow_html=True)
        c4.markdown(f'<div class="mcard"><div class="mval" style="color:{ccc_c} !important">{ccc:.0f} hari</div><div class="mlbl">CCC — Siklus Konversi Kas</div></div>', unsafe_allow_html=True)

        if ccc <= 0:
            st.markdown(f'<div class="ok-box"><p style="margin:0;font-size:0.87rem;color:#4a9060 !important">✅ <strong>CCC negatif ({ccc:.0f} hari) — Excellent!</strong> Bisnis menerima pembayaran dari pelanggan sebelum harus membayar supplier. Model ini sangat sehat dari sisi arus kas (seperti supermarket atau e-commerce besar).</p></div>', unsafe_allow_html=True)
        elif ccc <= 30:
            st.markdown(f'<div class="ok-box"><p style="margin:0;font-size:0.87rem;color:#4a9060 !important">✅ <strong>CCC {ccc:.0f} hari — Baik.</strong> Siklus kas tergolong pendek. Uang tidak terkunci lama di stok atau piutang.</p></div>', unsafe_allow_html=True)
        elif ccc <= 60:
            st.markdown(f'<div class="wn-box"><p style="margin:0;font-size:0.87rem;color:#9a7830 !important">⚡ <strong>CCC {ccc:.0f} hari — Perlu perhatian.</strong> Pertimbangkan mempercepat penagihan piutang (DSO) atau menegosiasikan pembayaran lebih lambat ke supplier (DPO).</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="er-box"><p style="margin:0;font-size:0.87rem;color:#c05858 !important">❌ <strong>CCC {ccc:.0f} hari — Tinggi.</strong> Butuh modal kerja besar untuk mendanai siklus operasional. Prioritaskan: (1) turunkan DIO dengan manajemen stok lebih baik, (2) turunkan DSO dengan kebijakan kredit lebih ketat, (3) naikkan DPO dengan negosiasi supplier.</p></div>', unsafe_allow_html=True)

        # Waterfall CCC
        fig_ccc = go.Figure(go.Waterfall(
            x=["DIO (Stok)", "DSO (Piutang)", "DPO (Supplier)", "CCC Total"],
            y=[dio, dso, -dpo, None],
            measure=["relative","relative","relative","total"],
            connector={"line":{"color":"rgba(255,255,255,0.15)"}},
            increasing={"marker":{"color":"rgba(190,80,80,0.65)"}},
            decreasing={"marker":{"color":"rgba(74,180,120,0.65)"}},
            totals={"marker":{"color":("rgba(74,180,120,0.7)" if ccc<=30 else "rgba(200,160,50,0.7)" if ccc<=60 else "rgba(190,80,80,0.7)")}},
            text=[f"{dio:.0f} hr",f"{dso:.0f} hr",f"−{dpo:.0f} hr",f"{ccc:.0f} hr"],
            textposition="outside"
        ))
        fig_ccc.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            height=280, margin=dict(l=10,r=10,t=20,b=30),
            yaxis=dict(title="Hari",tickfont=dict(size=9,color="#5a6880"),gridcolor="rgba(255,255,255,0.05)"),
            xaxis=dict(tickfont=dict(size=10,color="#6878a0"))
        )
        st.plotly_chart(fig_ccc, use_container_width=True)
        st.markdown('<p class="note">DPO mengurangi CCC karena menunda pengeluaran kas. Naikkan DPO dengan negosiasi term pembayaran ke supplier (misal dari net-7 ke net-30).</p>', unsafe_allow_html=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 7 — SUMBER PEMBIAYAAN                            ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[6]:
        st.markdown('<div class="sec">💳 Struktur Permodalan</div>', unsafe_allow_html=True)
        pct_e = ekuitas/total_pendanaan*100 if total_pendanaan>0 else 0
        pct_h = total_hutang/total_pendanaan*100 if total_pendanaan>0 else 0
        c1,c2 = st.columns(2)
        with c1:
            st.markdown(f"""<div class="rcard">
                <div style="color:#b89438;font-weight:600;margin-bottom:0.6rem;font-size:0.87rem">🏗️ Struktur Modal</div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Ekuitas ({pct_e:.1f}%)</span>
                    <span style="color:#5eaa7a;font-weight:600">Rp {ekuitas:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Hutang Lancar</span>
                    <span style="color:#b89438;font-weight:600">Rp {hutang_lancar:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Hutang JP ({pct_h:.1f}%)</span>
                    <span style="color:#c07040;font-weight:600">Rp {hutang_jangka_panjang:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;border-top:1px solid rgba(255,255,255,0.07);padding-top:0.35rem">
                    <span style="color:#7a9ab0;font-weight:600;font-size:0.83rem">Total Pendanaan</span>
                    <span style="color:#90b8d8;font-weight:700">Rp {total_pendanaan:,.0f}</span>
                </div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown(f"""<div class="rcard">
                <div style="color:#7a9ab8;font-weight:600;margin-bottom:0.6rem;font-size:0.87rem">⚙️ Biaya Modal (WACC Estimasi)</div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Biaya Ekuitas (discount rate)</span>
                    <span style="color:#5eaa7a;font-weight:600">{discount_rate}%/thn</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Biaya Hutang (after tax ~20%)</span>
                    <span style="color:#b89438;font-weight:600">{suku_bunga_hutang*0.8:.1f}%/thn</span>
                </div>
                <div style="display:flex;justify-content:space-between;margin-bottom:0.35rem">
                    <span style="color:#3a5870;font-size:0.83rem">Beban Bunga Tahunan</span>
                    <span style="color:#c07040;font-weight:600">Rp {beban_bunga_tahunan:,.0f}</span>
                </div>
                <div style="display:flex;justify-content:space-between;border-top:1px solid rgba(255,255,255,0.07);padding-top:0.35rem">
                    <span style="color:#7a9ab0;font-weight:600;font-size:0.83rem">WACC Estimasi</span>
                    <span style="color:#90b8d8;font-weight:700">{wacc_approx:.2f}%/thn</span>
                </div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="sec">📚 Panduan Sumber Pembiayaan UMKM</div>', unsafe_allow_html=True)
        pem = [
            ("🏦 KUR Mikro / KUR Kecil", "Bunga 6%/thn, plafon s.d. Rp 500 jt, tanpa agunan s.d. Rp 100 jt. BRI, BNI, Mandiri, BSI.", "#5eaa7a"),
            ("👼 Angel Investor", "Cocok untuk startup inovatif. Investor memberi modal dengan imbalan saham/equity bisnis.", "#b89438"),
            ("🌐 Crowdfunding", "Kitabisa, Indiegogo — cocok untuk produk inovatif dengan dukungan komunitas.", "#7a9ab8"),
            ("🎓 Program Inkubator", "UM Metro memiliki program pendampingan dan pendanaan untuk mahasiswa wirausaha.", "#9a78c0"),
            ("📱 P2P Lending", "Modalku, Investree — pinjaman usaha digital, proses cepat.", "#c07040"),
            ("🏛️ Hibah Pemerintah", "Kemenkop UKM, Kemenparekraf, BUMN — umumnya berbasis kompetisi.", "#5eaa7a"),
        ]
        for title, desc, col in pem:
            st.markdown(f'<div class="rcard" style="border-left:3px solid {col}"><div style="color:{col};font-weight:600;font-size:0.87rem">{title}</div><div style="color:#3a5060;font-size:0.8rem;margin-top:0.25rem">{desc}</div></div>', unsafe_allow_html=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ TAB 8 — RISIKO + CAPM + DIVERSIFIKASI                ║
    # ╚═══════════════════════════════════════════════════════╝
    with tabs[7]:
        st.markdown('<div class="sec">📊 Leverage & Margin of Safety</div>', unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            ol_c = "#5eaa7a" if operating_leverage<2 else "#b89438" if operating_leverage<4 else "#c05858"
            st.markdown(f"""<div class="rcard">
                <div style="color:#6a8aaa;font-size:0.8rem;font-weight:600">Operating Leverage (DOL)</div>
                <div style="color:{ol_c};font-size:1.3rem;font-weight:700;margin:0.35rem 0">{operating_leverage:.2f}x</div>
                <div style="color:#3a5060;font-size:0.78rem">Kenaikan penjualan 10% → laba naik {operating_leverage*10:.0f}%<br>
                <strong style="color:{ol_c}">{"✅ Rendah (Aman)" if operating_leverage<2 else "⚡ Sedang" if operating_leverage<4 else "❌ Tinggi (Berisiko)"}</strong></div>
            </div>""", unsafe_allow_html=True)
        with c2:
            mos_c = "#5eaa7a" if margin_of_safety_pct>=30 else "#b89438" if margin_of_safety_pct>=15 else "#c05858"
            st.markdown(f"""<div class="rcard">
                <div style="color:#6a8aaa;font-size:0.8rem;font-weight:600">Margin of Safety</div>
                <div style="color:{mos_c};font-size:1.3rem;font-weight:700;margin:0.35rem 0">{margin_of_safety_pct:.1f}%</div>
                <div style="color:#3a5060;font-size:0.78rem">Penjualan {estimasi_penjualan} unit vs BEP {bep_unit:.0f} unit<br>
                Selisih: {margin_of_safety_unit:.0f} unit di atas BEP<br>
                <strong style="color:{mos_c}">{"✅ Sangat Aman (≥30%)" if margin_of_safety_pct>=30 else "⚡ Cukup (15-30%)" if margin_of_safety_pct>=15 else "❌ Mendekati BEP"}</strong></div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<div class="sec">🎯 Skenario Analisis</div>', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        sk_colors = ["#c05858","#b89438","#5eaa7a"]
        sk_icons  = ["📉","📊","📈"]
        for col,(sk,val),clr,ico in zip([c1,c2,c3],skenario.items(),sk_colors,sk_icons):
            col.markdown(f'<div class="mcard"><div style="font-size:1.4rem">{ico}</div><div style="color:#5a7088;font-size:0.78rem;margin:0.25rem 0">{sk}</div><div style="color:{clr};font-size:1.1rem;font-weight:700">Rp {val:,.0f}</div><div style="color:#3a5060;font-size:0.72rem">Laba Bersih/Bulan</div></div>', unsafe_allow_html=True)

        # ── CAPM (BARU) ───────────────────────────────────────────
        st.markdown('<div class="sec">📈 CAPM — Capital Asset Pricing Model (BARU)</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">CAPM</strong> menghitung berapa <em>minimum return</em> yang seharusnya dihasilkan sebuah investasi, berdasarkan risikonya relatif terhadap pasar. Jika return aktual bisnis &gt; CAPM, berarti bisnis menciptakan nilai lebih dari yang dipersyaratkan.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">E(R) = Rf + β × (Rm − Rf)<br>Rf = Risk-free rate (BI Rate / SBN)  |  β = Beta bisnis terhadap pasar<br>Rm − Rf = Market Risk Premium (imbal hasil ekstra pasar vs bebas risiko)</div>', unsafe_allow_html=True)

        c1,c2,c3,c4 = st.columns(4)
        c1.markdown(f'<div class="mcard"><div class="mval" style="color:#6a8aaa !important">{rf}%</div><div class="mlbl">Risk-Free Rate (Rf)</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="mcard"><div class="mval" style="color:#6a8aaa !important">{beta:.1f}x</div><div class="mlbl">Beta (β)</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="mcard"><div class="mval">{capm_pct:.2f}%</div><div class="mlbl">Required Return (CAPM)</div></div>', unsafe_allow_html=True)

        alpha_c = "#5eaa7a" if alpha_jensen>0 else "#c05858"
        alpha_lbl = f"{'✅ Outperform' if alpha_jensen>0 else '❌ Underperform'} vs CAPM"
        c4.markdown(f'<div class="mcard"><div class="mval" style="color:{alpha_c} !important">{alpha_jensen*100:+.2f}%</div><div class="mlbl">Alpha (α) — Excess Return</div></div>', unsafe_allow_html=True)

        if alpha_jensen > 0:
            st.markdown(f'<div class="ok-box"><p style="margin:0;font-size:0.87rem;color:#4a9060 !important">✅ <strong>Alpha positif (+{alpha_jensen*100:.2f}%)</strong> — ROE bisnis ({roe:.1f}%) melebihi return minimum CAPM ({capm_pct:.2f}%). Bisnis menciptakan nilai lebih dari yang dipersyaratkan oleh risikonya.</p></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="er-box"><p style="margin:0;font-size:0.87rem;color:#c05858 !important">❌ <strong>Alpha negatif ({alpha_jensen*100:.2f}%)</strong> — ROE bisnis ({roe:.1f}%) di bawah return minimum CAPM ({capm_pct:.2f}%). Pertimbangkan menaikkan profitabilitas atau menurunkan risiko bisnis.</p></div>', unsafe_allow_html=True)

        st.markdown(f'<p class="note">Parameter CAPM: Rf={rf}%, Rm={rm}%, β={beta:.1f}, Market Risk Premium={(rm-rf):.0f}%. Actual Return proxy = ROE={roe:.1f}%/tahun. Alpha = Actual − CAPM Required.</p>', unsafe_allow_html=True)

        # ── DIVERSIFIKASI PORTOFOLIO (BARU) ───────────────────────
        st.markdown('<div class="sec">🌐 Diversifikasi Portofolio (BARU)</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p><strong style="color:#8090b0">Diversifikasi</strong> mengurangi risiko tidak sistematis (unsystematic risk) dengan menambah jumlah aset/investasi yang berbeda-beda. Namun, <strong style="color:#8090b0">risiko sistematis (market risk)</strong> tidak bisa dihilangkan — inilah yang diukur oleh Beta (β) dalam CAPM.</p></div>', unsafe_allow_html=True)

        n_range = np.arange(1, 31)
        # Estimasi risiko: systematic (30%) + unsystematic yang bisa dikurangi
        sys_frac = max(0.15, min(0.50, beta**2 * 0.25))  # aproximasi berbasis beta
        port_risk = (sys_frac + (1-sys_frac)/n_range) * 100

        fig_div = go.Figure()
        fig_div.add_trace(go.Scatter(
            x=n_range, y=port_risk, mode="lines",
            line=dict(color="#6a9ad8", width=2.5), name="Risiko Portofolio",
            fill="tozeroy", fillcolor="rgba(106,154,216,0.08)"
        ))
        fig_div.add_hline(y=sys_frac*100, line_dash="dot", line_color="rgba(190,80,80,0.5)",
                          annotation_text=f"Risiko Sistematis (~{sys_frac*100:.0f}%)",
                          annotation_font_color="#c05858", annotation_position="right")
        fig_div.add_vline(x=1, line_dash="dot", line_color="rgba(255,255,255,0.15)")
        fig_div.add_annotation(x=15, y=(sys_frac + (1-sys_frac)/15)*100 + 8,
            text=f"β={beta:.1f} → Risiko Sistematis ≈{sys_frac*100:.0f}%",
            font=dict(color="#6878a0",size=10), showarrow=False)
        fig_div.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            height=300, margin=dict(l=10,r=10,t=20,b=30),
            xaxis=dict(title="Jumlah Saham/Investasi dalam Portofolio",
                       tickfont=dict(size=9,color="#5a6880"), gridcolor="rgba(255,255,255,0.04)"),
            yaxis=dict(title="Risiko Portofolio (% dari risiko 1 aset)",
                       ticksuffix="%", tickfont=dict(size=9,color="#5a6880"),
                       gridcolor="rgba(255,255,255,0.04)"),
            legend=dict(font=dict(color="#6878a0",size=11),bgcolor="rgba(0,0,0,0)"),
        )
        st.plotly_chart(fig_div, use_container_width=True)

        st.markdown(f"""
        <div style="display:flex;gap:0.7rem;margin-top:0.5rem">
            <div class="mcard" style="flex:1">
                <div class="mval" style="color:#c05858 !important">{sys_frac*100:.0f}%</div>
                <div class="mlbl">Risiko Sistematis<br>(Market Risk — tidak bisa dihilangkan)</div>
            </div>
            <div class="mcard" style="flex:1">
                <div class="mval" style="color:#5eaa7a !important">{(1-sys_frac)*100:.0f}%</div>
                <div class="mlbl">Risiko Tidak Sistematis<br>(bisa dikurangi dengan diversifikasi)</div>
            </div>
            <div class="mcard" style="flex:1">
                <div class="mval">{beta:.1f}x</div>
                <div class="mlbl">Beta — Sensitivitas<br>terhadap Pasar Keseluruhan</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        impl_div = [
            ("Diversifikasi Produk", f"Jangan mengandalkan satu produk saja. Bisnis {nama_bisnis or 'Anda'} bisa menambah lini produk/jasa komplementer."),
            ("Diversifikasi Segmen Pasar", "Layani beberapa segmen pelanggan berbeda agar tidak bergantung pada satu kelompok pelanggan."),
            ("Diversifikasi Sumber Pendapatan", "Tambahkan pendapatan dari channel berbeda: offline, online, B2B, B2C."),
            ("Diversifikasi Supplier", "Jangan bergantung pada satu supplier agar tidak rentan gangguan rantai pasokan."),
        ]
        st.markdown('<div class="sec">💡 Strategi Diversifikasi Risiko untuk UMKM</div>', unsafe_allow_html=True)
        for judul, penj in impl_div:
            st.markdown(f'<p style="font-size:0.85rem;color:#5a6a80 !important;margin:0.25rem 0"><span style="color:#7a90a4;font-weight:600">→ {judul}:</span> {penj}</p>', unsafe_allow_html=True)

        # ── RISK PROFILE SUMMARY ──────────────────────────────────
        risk_score = 0
        risk_factors = []
        if debt_to_equity>2:         risk_score+=2; risk_factors.append("❌ D/E Ratio tinggi (>2x)")
        if margin_of_safety_pct<15:  risk_score+=2; risk_factors.append("❌ Margin of safety rendah (<15%)")
        if operating_leverage>4:     risk_score+=2; risk_factors.append("❌ Operating leverage tinggi (>4x)")
        if kas_surplus<0:            risk_score+=2; risk_factors.append("❌ Kas di bawah minimum")
        if npv<0:                    risk_score+=2; risk_factors.append("❌ NPV negatif")
        if alpha_jensen>0:           risk_factors.append(f"✅ Outperform CAPM (+{alpha_jensen*100:.1f}%)")
        if irr_annual>discount_rate: risk_factors.append("✅ IRR melebihi hurdle rate")
        if margin_of_safety_pct>=30: risk_factors.append("✅ Margin of safety kuat")
        if current_ratio>=2:         risk_factors.append("✅ Likuiditas sangat baik")
        if pi>1:                     risk_factors.append(f"✅ Profitability Index positif ({pi:.2f})")

        risk_lbl = "🟢 Risiko Rendah" if risk_score<=2 else "🟡 Risiko Sedang" if risk_score<=6 else "🔴 Risiko Tinggi"
        rl_c     = "#5eaa7a" if risk_score<=2 else "#b89438" if risk_score<=6 else "#c05858"
        st.markdown('<div class="sec">📋 Risk-Return Profile</div>', unsafe_allow_html=True)
        st.markdown(f"""<div class="rcard">
            <div style="color:#90b8d8;font-size:1rem;font-weight:700;margin-bottom:0.6rem">
                Profil Risiko: <span style="color:{rl_c}">{risk_lbl}</span>
            </div>
            {"".join(f'<div style="font-size:0.84rem;color:#5a6880;margin-bottom:0.22rem">{f}</div>' for f in risk_factors)}
        </div>""", unsafe_allow_html=True)

    # ╔═══════════════════════════════════════════════════════╗
    # ║ PDF EXPORT                                           ║
    # ╚═══════════════════════════════════════════════════════╝
    st.markdown("---")
    st.markdown('<p style="font-size:0.82rem;color:#3a5870 !important;margin-bottom:0.5rem">📄 Unduh laporan analisis keuangan lengkap dalam format PDF.</p>', unsafe_allow_html=True)

    def _buat_pdf_simulasi():
        import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from utils import BisnisKuPDF
        import datetime
        pdf = BisnisKuPDF(f"Simulasi Keuangan — {nama_bisnis or 'Bisnis'}")
        pdf.add_page()

        # Info dasar
        pdf.section("Informasi Bisnis")
        pdf.kv("Nama Bisnis",      nama_bisnis or "—")
        pdf.kv("Jenis Bisnis",     jenis_bisnis)
        pdf.kv("Modal Awal",       f"Rp {modal_awal:,.0f}")
        pdf.kv("Harga Jual/Unit",  f"Rp {harga_jual:,.0f}")
        pdf.kv("HPP/Unit",         f"Rp {hpp_total:,.0f}")
        pdf.kv("Periode Proyeksi", periode)

        # Ringkasan utama
        pdf.section("Ringkasan Keuangan Utama")
        pdf.th(["Indikator", "Nilai", "Keterangan"], [70, 55, 57])
        rows_sum = [
            ("BEP (unit/bln)",  f"{bep_unit:,.0f} unit",   "Titik impas penjualan"),
            ("BEP (Rupiah)",    f"Rp {bep_rupiah:,.0f}",   "Titik impas pendapatan"),
            ("Laba Bersih/Bln", f"Rp {laba_bersih:,.0f}",  "Estimasi laba bulanan"),
            ("Gross Margin",    f"{gross_margin_pct:.1f}%", "Margin kotor"),
            ("ROI/Bulan",       f"{roi:.2f}%",              "Return on Investment"),
            ("Payback Period",  f"{payback:.1f} bulan",     "Modal kembali"),
        ]
        for i,(a,b,c) in enumerate(rows_sum):
            pdf.tr([a,b,c],[70,55,57],even=i%2==0)

        # Capital Budgeting
        pdf.section("Analisis Capital Budgeting")
        pdf.th(["Metode","Nilai","Keputusan"], [55,65,62])
        npv_dec = "TERIMA (NPV > 0)" if npv>0 else "TOLAK (NPV < 0)"
        irr_dec = f"TERIMA (IRR {irr_annual:.1f}% > {discount_rate}%)" if irr_annual>discount_rate else f"TOLAK (IRR < {discount_rate}%)"
        pi_dec  = "TERIMA (PI > 1)" if pi>1 else "TOLAK (PI <= 1)"
        pb_dec  = "Cepat (<24 bln)" if payback<24 else "Normal" if payback<48 else "Lambat"
        for i,(a,b,c) in enumerate([
            ("NPV", f"Rp {npv:,.0f}", npv_dec),
            ("IRR", f"{irr_annual:.2f}%/tahun", irr_dec),
            ("Payback Period", f"{payback:.1f} bulan", pb_dec),
            ("Profitability Index (PI)", f"{pi:.3f}", pi_dec),
        ]):
            pdf.tr([a,b,c],[55,65,62],even=i%2==0)
        pdf.note("PI = 1 + NPV / Modal Awal. PI > 1 menunjukkan nilai lebih dari yang diinvestasikan.")

        # Rasio Keuangan
        pdf.section("Analisis Rasio Keuangan")
        pdf.th(["Rasio","Nilai","Benchmark","Status"], [52,38,42,50])
        def st_rasio(val, lo, hi):
            return "Baik" if val >= hi else "Cukup" if val >= lo else "Perlu Perbaikan"
        def st_inv(val, lo, hi):
            return "Baik" if val <= lo else "Cukup" if val <= hi else "Perlu Perbaikan"
        rows_r = [
            ("Current Ratio",    f"{current_ratio:.2f}x",       ">=2x",    st_rasio(current_ratio,1,2)),
            ("Quick Ratio",      f"{quick_ratio:.2f}x",          ">=1x",    st_rasio(quick_ratio,0.7,1)),
            ("Net Profit Margin",f"{net_profit_margin:.1f}%",    ">=15%",   st_rasio(net_profit_margin,5,15)),
            ("ROA",              f"{roa:.1f}%/thn",              ">=10%",   st_rasio(roa,5,10)),
            ("ROE",              f"{roe:.1f}%/thn",              ">=15%",   st_rasio(roe,8,15)),
            ("Debt to Equity",   f"{debt_to_equity:.2f}x",       "<=1x",    st_inv(debt_to_equity,1,2)),
            ("Debt Ratio",       f"{debt_ratio:.2f}",            "<=0.5",   st_inv(debt_ratio,0.5,0.7)),
            ("Asset Turnover",   f"{asset_turnover:.2f}x/thn",   ">=1x",    st_rasio(asset_turnover,0.5,1)),
            ("DSO",              f"{dso:.0f} hari",              "<=30 hr", st_inv(dso,30,60)),
        ]
        for i,(a,b,c,d) in enumerate(rows_r):
            pdf.tr([a,b,c,d],[52,38,42,50],even=i%2==0)

        # CCC
        pdf.section("Cash Conversion Cycle (CCC)")
        pdf.th(["Komponen","Nilai","Keterangan"], [50,45,87])
        ccc_rows = [
            ("DIO",f"{dio:.0f} hari","Rata-rata hari stok tersimpan"),
            ("DSO",f"{dso:.0f} hari","Rata-rata hari piutang tertagih"),
            ("DPO",f"{dpo:.0f} hari","Rata-rata hari pembayaran ke supplier"),
            ("CCC = DIO+DSO-DPO",f"{ccc:.0f} hari","Siklus konversi kas total"),
        ]
        for i,(a,b,c) in enumerate(ccc_rows):
            pdf.tr([a,b,c],[50,45,87],even=i%2==0,bold=(i==3))
        ccc_interp = "Baik — siklus kas pendek." if ccc<=30 else "Perlu perhatian — pertimbangkan percepat piutang & tunda bayar supplier." if ccc<=60 else "Tinggi — butuh modal kerja besar. Optimalkan DIO, DSO, dan DPO."
        pdf.note(f"Interpretasi: {ccc_interp}")

        # CAPM
        pdf.section("Analisis CAPM & Risiko")
        pdf.th(["Parameter","Nilai","Keterangan"],[55,40,87])
        capm_rows = [
            ("Risk-Free Rate (Rf)",     f"{rf}%",          "BI Rate / SBN"),
            ("Market Return (Rm)",      f"{rm}%",          "Expected market return (IHSG)"),
            ("Beta (Bisnis)",           f"{beta:.1f}x",    "Sensitivitas thd pasar"),
            ("CAPM Required Return",    f"{capm_pct:.2f}%","Minimum return yg dipersyaratkan"),
            ("Actual Return (ROE)",     f"{roe:.1f}%",     "Return aktual bisnis"),
            ("Alpha (Jensen's Alpha)",  f"{alpha_jensen*100:+.2f}%","Excess return thd CAPM"),
        ]
        for i,(a,b,c) in enumerate(capm_rows):
            pdf.tr([a,b,c],[55,40,87],even=i%2==0)
        alpha_msg = f"Outperform: ROE ({roe:.1f}%) > CAPM ({capm_pct:.2f}%). Bisnis menciptakan nilai lebih dari yg dipersyaratkan." if alpha_jensen>0 else f"Underperform: ROE ({roe:.1f}%) < CAPM ({capm_pct:.2f}%). Tingkatkan profitabilitas atau turunkan risiko."
        pdf.alert(alpha_msg, ok=alpha_jensen>0)

        # Profil Risiko
        pdf.section("Profil Risiko Keseluruhan")
        pdf.kv("Risk Level",     risk_lbl.replace("🟢","[RENDAH]").replace("🟡","[SEDANG]").replace("🔴","[TINGGI]"))
        pdf.kv("Risk Score",     f"{risk_score} / 10")
        pdf.ln(2)
        for f in risk_factors:
            f_clean = f.replace("✅","[OK]").replace("❌","[!]")
            pdf.set_font("Helvetica","",8.5)
            pdf.set_text_color(55,70,90)
            pdf.cell(0,5,f"  {f_clean}",ln=True)
        pdf.set_text_color(0,0,0)

        return pdf.build()

    import datetime as _dt
    fname = f"BisnisKu_{(nama_bisnis or 'bisnis').replace(' ','_')}_{_dt.date.today()}.pdf"
    st.download_button(
        label="📄 Unduh Laporan PDF Lengkap",
        data=_buat_pdf_simulasi(),
        file_name=fname,
        mime="application/pdf",
        use_container_width=False,
    )
