import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Penilaian Saham & Obligasi", page_icon="💹", layout="wide")

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
.concept { background: rgba(40,70,120,0.1); border: 1px solid rgba(80,130,200,0.18);
           border-radius: 9px; padding: 0.75rem 1rem; margin: 0.4rem 0 0.75rem 0; }
.concept p { font-size: 0.86rem; color: #6882a0 !important; margin: 0; line-height: 1.65; }
.formula { background: rgba(40,70,120,0.12); border: 1px solid rgba(80,130,200,0.2);
           border-left: 3px solid rgba(80,130,200,0.45); border-radius: 0 8px 8px 0;
           padding: 0.65rem 1rem; margin: 0.35rem 0 0.7rem 0;
           font-family: 'Courier New', monospace; font-size: 0.87rem; color: #80a8cc !important; line-height: 1.7; }
.rcard { background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09);
         border-radius: 10px; padding: 0.9rem 1.1rem; margin-bottom: 0.5rem; text-align: center; }
.rval  { font-size: 1.35rem; font-weight: 700; color: #90b8d8 !important; }
.rlbl  { font-size: 0.73rem; color: #3a5870 !important; margin-top: 0.2rem; }
.tip   { background: rgba(60,110,80,0.07); border: 1px solid rgba(60,150,90,0.18);
         border-radius: 9px; padding: 0.65rem 0.9rem; margin: 0.5rem 0; }
.tip p { font-size: 0.83rem; color: #5a8a6a !important; margin: 0; }
.warn  { background: rgba(180,130,40,0.07); border: 1px solid rgba(200,160,60,0.18);
         border-radius: 9px; padding: 0.65rem 0.9rem; margin: 0.5rem 0; }
.warn p { font-size: 0.83rem; color: #8a7040 !important; margin: 0; }
.col-h { font-size: 0.71rem; font-weight: 600; color: #3a5870 !important;
         text-transform: uppercase; letter-spacing: 0.4px; margin: 0; }
.row0  { font-size: 0.85rem; color: #8898ac !important; margin: 0; padding: 0.2rem 0; }
.row1  { font-size: 0.87rem; color: #a0b8cc !important; font-weight: 600; margin: 0; padding: 0.2rem 0; }
.divl  { border-top: 1px solid rgba(255,255,255,0.06); margin: 0.18rem 0; }
.note  { font-size: 0.76rem; color: #3a5060 !important; font-style: italic; margin-top: 0.4rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-size:1.55rem;font-weight:700;color:#c4d4e4;margin:0">💹 Penilaian Saham &amp; Obligasi</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#566880;font-size:0.86rem;margin:0.3rem 0 0 0">Valuasi intrinsik saham dan obligasi — dasar keputusan investasi yang terukur dan rasional.</p>', unsafe_allow_html=True)
st.markdown("---")

TABS = st.tabs(["📈 Valuasi Saham", "📋 Valuasi Obligasi", "📉 Hubungan Harga & Yield"])

# ╔══════════════════════════════════════════════════════════╗
# ║ TAB 1 — VALUASI SAHAM                                  ║
# ╚══════════════════════════════════════════════════════════╝
with TABS[0]:
    st.markdown('<div class="sec">📈 Penilaian Saham (Stock Valuation)</div>', unsafe_allow_html=True)
    st.markdown('<div class="concept"><p>Harga wajar (intrinsic value) saham dihitung berdasarkan arus kas yang diharapkan investor di masa depan. Ada tiga pendekatan utama: DDM, Gordon Growth Model, dan P/E Method.</p></div>', unsafe_allow_html=True)

    metode = st.radio("Pilih Metode Valuasi:", [
        "1️⃣  DDM — Dividen Konstan (Zero Growth)",
        "2️⃣  Gordon Growth Model — Dividen Bertumbuh",
        "3️⃣  P/E Method — Berbasis Laba",
    ], label_visibility="collapsed")

    # ── METODE 1: DDM ZERO GROWTH ──────────────────────────
    if "1️⃣" in metode:
        st.markdown('<div class="sec">Dividend Discount Model — Pertumbuhan Nol</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">P₀ = D / r<br>D  = dividen per lembar saham (tetap tiap tahun)<br>r  = required rate of return (tingkat imbal hasil yang diharapkan investor)</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="concept"><p>Cocok untuk saham preferen atau perusahaan matang yang membayar dividen tetap tanpa pertumbuhan. '
            'Model ini mengasumsikan dividen dibayar selamanya (perpetuitas).</p></div>', unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns(3)
        with col1: D   = st.number_input("Dividen per Lembar (Rp)", min_value=0, value=500, step=50, format="%d")
        with col2: r   = st.slider("Required Return (%/tahun)", 5, 30, 12, key="r_ddm0")
        with col3: hm  = st.number_input("Harga Pasar Saat Ini (Rp)", min_value=0, value=3_800, step=100, format="%d")

        p0 = D / (r / 100) if r > 0 else 0
        selisih = hm - p0
        if abs(p0) > 0:
            pct_sel = selisih / p0 * 100
            if pct_sel < -5:
                verdict = ("🟢 Undervalued — Harga pasar di bawah nilai wajar, layak dipertimbangkan beli", "#5eaa7a")
            elif pct_sel > 5:
                verdict = ("🔴 Overvalued — Harga pasar di atas nilai wajar, pertimbangkan jual", "#c05858")
            else:
                verdict = ("🟡 Fairly Valued — Harga pasar mendekati nilai wajar", "#b89438")
        else:
            verdict = ("—", "#5a7090")

        c1, c2, c3 = st.columns(3)
        c1.markdown(f'<div class="rcard"><div class="rval">Rp {p0:,.0f}</div><div class="rlbl">Nilai Wajar (Fair Value)</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="rcard"><div class="rval">Rp {hm:,.0f}</div><div class="rlbl">Harga Pasar</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="rcard"><div class="rval" style="font-size:0.95rem;color:{verdict[1]} !important">{verdict[0][:verdict[0].index("—")].strip()}</div><div class="rlbl">Kesimpulan Valuasi</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tip"><p>💡 {verdict[0]}</p></div>', unsafe_allow_html=True)

    # ── METODE 2: GORDON GROWTH ────────────────────────────
    elif "2️⃣" in metode:
        st.markdown('<div class="sec">Gordon Growth Model — Pertumbuhan Dividen Konstan</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">P₀ = D₁ / (r − g)<br>D₁ = D₀ × (1 + g)  →  dividen tahun berikutnya<br>r  = required rate of return  |  g = tingkat pertumbuhan dividen<br><em>Syarat: r harus lebih besar dari g</em></div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p>Paling sering digunakan untuk menilai saham perusahaan yang dividen-nya tumbuh stabil tiap tahun, misalnya perusahaan di sektor konsumen, perbankan, atau BUMN yang rutin bagi dividen.</p></div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            D0   = st.number_input("Dividen Terakhir D₀ (Rp)", min_value=0, value=400, step=50, format="%d")
            r_gg = st.slider("Required Return r (%/tahun)", 5, 30, 14, key="r_gg")
        with col2:
            g_gg = st.slider("Pertumbuhan Dividen g (%/tahun)", 0, 25, 8, key="g_gg")
            hm2  = st.number_input("Harga Pasar Saat Ini (Rp)", min_value=0, value=5_500, step=100, format="%d")

        if r_gg > g_gg:
            D1   = D0 * (1 + g_gg / 100)
            p_gg = D1 / ((r_gg - g_gg) / 100)
            selisih2 = hm2 - p_gg
            pct2 = selisih2 / p_gg * 100 if p_gg > 0 else 0
            if pct2 < -5:
                vrd2 = ("🟢 Undervalued", "#5eaa7a")
            elif pct2 > 5:
                vrd2 = ("🔴 Overvalued", "#c05858")
            else:
                vrd2 = ("🟡 Fairly Valued", "#b89438")

            c1, c2, c3, c4 = st.columns(4)
            c1.markdown(f'<div class="rcard"><div class="rval">Rp {D1:,.0f}</div><div class="rlbl">D₁ (Dividen Tahun Depan)</div></div>', unsafe_allow_html=True)
            c2.markdown(f'<div class="rcard"><div class="rval">Rp {p_gg:,.0f}</div><div class="rlbl">Nilai Wajar (P₀)</div></div>', unsafe_allow_html=True)
            c3.markdown(f'<div class="rcard"><div class="rval">Rp {hm2:,.0f}</div><div class="rlbl">Harga Pasar</div></div>', unsafe_allow_html=True)
            c4.markdown(f'<div class="rcard"><div class="rval" style="color:{vrd2[1]} !important">{vrd2[0]}</div><div class="rlbl">Kesimpulan</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="tip"><p>💡 Dengan asumsi dividen tumbuh {g_gg}%/tahun, harga wajar saham adalah Rp {p_gg:,.0f}. Saat ini saham {"undervalued" if pct2 < -5 else "overvalued" if pct2 > 5 else "fairly valued"} sebesar {abs(pct2):.1f}%.</p></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warn"><p>⚠️ Required return (r) harus lebih besar dari g. Jika g ≥ r, formula Gordon Growth tidak berlaku karena menghasilkan nilai tak terhingga.</p></div>', unsafe_allow_html=True)

    # ── METODE 3: P/E METHOD ───────────────────────────────
    else:
        st.markdown('<div class="sec">Price / Earnings Method — Berbasis Laba Per Saham</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula">P₀ = EPS × P/E Wajar<br>EPS   = Earnings Per Share (laba bersih per lembar saham)<br>P/E   = Price to Earnings Ratio industri sebanding</div>', unsafe_allow_html=True)
        st.markdown('<div class="concept"><p>Metode praktis yang membandingkan laba per saham dengan rasio P/E industri. Berguna ketika perusahaan belum membayar dividen secara rutin, tapi sudah menghasilkan laba stabil.</p></div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            laba_bersih = st.number_input("Laba Bersih Perusahaan (Rp)",  min_value=0, value=10_000_000_000, step=500_000_000, format="%d")
            jml_saham   = st.number_input("Jumlah Saham Beredar (lembar)", min_value=1, value=1_000_000_000, step=10_000_000,  format="%d")
            pe_wajar    = st.slider("P/E Ratio Industri (wajar)", 5, 50, 15, help="P/E 10–15: konservatif. 15–25: rata-rata. >25: growth stock.")
        with col2:
            hm3 = st.number_input("Harga Pasar Saat Ini (Rp/lembar)", min_value=0, value=1_200, step=50, format="%d")
            dps = st.number_input("Dividen per Saham (Rp, jika ada)", min_value=0, value=80, step=10, format="%d")

        eps      = laba_bersih / jml_saham if jml_saham > 0 else 0
        p_pe     = eps * pe_wajar
        pe_aktual = hm3 / eps if eps > 0 else 0
        div_yield = dps / hm3 * 100 if hm3 > 0 else 0

        selisih3 = hm3 - p_pe
        pct3 = selisih3 / p_pe * 100 if p_pe > 0 else 0
        if pct3 < -5:   vrd3 = ("🟢 Undervalued", "#5eaa7a")
        elif pct3 > 5:  vrd3 = ("🔴 Overvalued",  "#c05858")
        else:           vrd3 = ("🟡 Fairly Valued","#b89438")

        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f'<div class="rcard"><div class="rval">Rp {eps:,.2f}</div><div class="rlbl">EPS (Rp/lembar)</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="rcard"><div class="rval">Rp {p_pe:,.0f}</div><div class="rlbl">Nilai Wajar (P₀)</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="rcard"><div class="rval">{pe_aktual:.1f}x</div><div class="rlbl">P/E Aktual Pasar</div></div>', unsafe_allow_html=True)
        c4.markdown(f'<div class="rcard"><div class="rval" style="color:{vrd3[1]} !important">{vrd3[0]}</div><div class="rlbl">Kesimpulan</div></div>', unsafe_allow_html=True)

        c5, c6 = st.columns(2)
        c5.markdown(f'<div class="rcard"><div class="rval">{div_yield:.2f}%</div><div class="rlbl">Dividend Yield (D/P)</div></div>', unsafe_allow_html=True)
        c6.markdown(f'<div class="rcard"><div class="rval">{pe_wajar}x vs {pe_aktual:.1f}x</div><div class="rlbl">P/E Wajar vs P/E Pasar</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="warn" style="margin-top:1rem"><p>⚠️ Valuasi di atas bersifat edukatif. Keputusan investasi saham nyata membutuhkan analisis fundamental mendalam, kondisi makroekonomi, dan konsultasi dengan analis keuangan profesional.</p></div>', unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════╗
# ║ TAB 2 — VALUASI OBLIGASI                               ║
# ╚══════════════════════════════════════════════════════════╝
with TABS[1]:
    st.markdown('<div class="sec">📋 Penilaian Obligasi (Bond Valuation)</div>', unsafe_allow_html=True)
    st.markdown('<div class="concept"><p>Harga wajar obligasi adalah nilai kini (PV) dari semua arus kas masa depan: kupon periodik + pengembalian nilai nominal saat jatuh tempo. Harga bergerak <strong style="color:#8090b0">berlawanan arah</strong> dengan imbal hasil (YTM).</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="formula">Harga = Σ [ C / (1 + r)ᵗ ] + Nominal / (1 + r)ⁿ<br>C        = kupon per periode (= Nominal × tingkat kupon / frekuensi)<br>r        = required yield per periode<br>n        = total periode pembayaran<br>Nominal  = nilai par / nilai muka obligasi</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        nominal   = st.number_input("Nilai Nominal Obligasi (Rp)", min_value=0, value=1_000_000, step=100_000, format="%d")
        kupon_r   = st.slider("Tingkat Kupon (%/tahun)", 1, 20, 8,  help="Tertera di prospektus obligasi")
        n_tahun   = st.slider("Jangka Waktu (tahun)",   1, 30, 5)
    with col2:
        ytm_input = st.slider("Required Yield / YTM (%/tahun)", 1, 25, 10, help="Imbal hasil yang diinginkan investor; bisa dari suku bunga pasar")
        frekuensi = st.selectbox("Frekuensi Pembayaran Kupon", ["Semesteran (2x/tahun)", "Tahunan (1x/tahun)"])
        freq_n    = 2 if "Semesteran" in frekuensi else 1

    C   = nominal * kupon_r / 100 / freq_n   # kupon per periode
    r   = ytm_input / 100 / freq_n           # yield per periode
    n   = n_tahun * freq_n                   # total periode

    pv_kupon   = C * (1 - (1 + r) ** (-n)) / r if r > 0 else C * n
    pv_nominal = nominal / (1 + r) ** n
    harga_obl  = pv_kupon + pv_nominal
    premium    = harga_obl - nominal
    premium_pct = premium / nominal * 100

    if premium_pct > 1:   status_obl = ("📈 Premium — Kupon > YTM, harga di atas nilai nominal", "#5eaa7a")
    elif premium_pct < -1: status_obl = ("📉 Diskon — Kupon < YTM, harga di bawah nilai nominal", "#c05858")
    else:                  status_obl = ("🟡 Par — Kupon ≈ YTM, harga mendekati nilai nominal",   "#b89438")

    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="rcard"><div class="rval">Rp {harga_obl:,.0f}</div><div class="rlbl">Harga Wajar Obligasi</div></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="rcard"><div class="rval">Rp {C:,.0f} / {frekuensi.split(" ")[0].lower()}</div><div class="rlbl">Kupon per Periode</div></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="rcard"><div class="rval" style="color:{status_obl[1]} !important">{premium_pct:+.2f}%</div><div class="rlbl">Premium / Diskon thd Nominal</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="tip"><p>💡 {status_obl[0]}. PV Kupon: Rp {pv_kupon:,.0f} | PV Nominal: Rp {pv_nominal:,.0f}</p></div>', unsafe_allow_html=True)

    # Macaulay Duration
    st.markdown('<div class="sec">⏱️ Durasi Obligasi (Macaulay Duration)</div>', unsafe_allow_html=True)
    st.markdown('<div class="formula">Durasi = Σ [ t × PV(Arus Kas_t) ] / Harga Obligasi<br>Mengukur rata-rata tertimbang jangka waktu penerimaan arus kas. Makin besar durasi, makin sensitif harga terhadap perubahan suku bunga.</div>', unsafe_allow_html=True)

    if r > 0 and harga_obl > 0:
        weighted = sum(t * C / (1 + r) ** t for t in range(1, int(n) + 1))
        weighted += n * nominal / (1 + r) ** n
        mac_dur   = weighted / harga_obl / freq_n       # in years
        mod_dur   = mac_dur / (1 + ytm_input / 100 / freq_n)
        price_chg_1pct = -mod_dur * harga_obl * 0.01

        c1, c2, c3 = st.columns(3)
        c1.markdown(f'<div class="rcard"><div class="rval">{mac_dur:.2f} thn</div><div class="rlbl">Macaulay Duration</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="rcard"><div class="rval">{mod_dur:.2f} thn</div><div class="rlbl">Modified Duration</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="rcard"><div class="rval">Rp {price_chg_1pct:,.0f}</div><div class="rlbl">Perubahan Harga jika YTM naik 1%</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="tip"><p>💡 Jika YTM naik 1% (dari {ytm_input}% ke {ytm_input+1}%), harga obligasi akan turun sekitar Rp {abs(price_chg_1pct):,.0f} (≈ {abs(price_chg_1pct/harga_obl*100):.2f}%). Durasi yang lebih panjang = sensitivitas lebih tinggi.</p></div>', unsafe_allow_html=True)

    # Tabel Arus Kas
    st.markdown('<div class="sec">📋 Rincian Arus Kas Obligasi</div>', unsafe_allow_html=True)
    akrual_rows = []
    for t in range(1, int(n) + 1):
        cf = C + (nominal if t == n else 0)
        pv = cf / (1 + r) ** t
        akrual_rows.append({"Periode": t, "Arus Kas (Rp)": round(cf), "PV Arus Kas (Rp)": round(pv)})
    df_ak = pd.DataFrame(akrual_rows)
    for col in ["Arus Kas (Rp)", "PV Arus Kas (Rp)"]:
        df_ak[col] = df_ak[col].apply(lambda x: f"Rp {x:,.0f}")
    max_show = min(20, len(df_ak))
    st.dataframe(df_ak.head(max_show), use_container_width=True, hide_index=True)
    if len(df_ak) > max_show:
        st.markdown(f'<p class="note">Menampilkan {max_show} dari {len(df_ak)} periode.</p>', unsafe_allow_html=True)

# ╔══════════════════════════════════════════════════════════╗
# ║ TAB 3 — HUBUNGAN HARGA & YIELD                         ║
# ╚══════════════════════════════════════════════════════════╝
with TABS[2]:
    st.markdown('<div class="sec">📉 Hubungan Harga Obligasi dan Yield (YTM)</div>', unsafe_allow_html=True)
    st.markdown('<div class="concept"><p><strong style="color:#8090b0">Prinsip utama:</strong> Harga obligasi dan imbal hasil (YTM) bergerak <strong>berlawanan arah</strong>. Ketika suku bunga pasar naik, harga obligasi lama turun. Ketika suku bunga turun, harga obligasi naik. Ini adalah konsep terpenting dalam investasi obligasi.</p></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1: nom2    = st.number_input("Nilai Nominal (Rp)",     min_value=0, value=1_000_000, step=100_000, format="%d", key="nom2")
    with col2: kpn2    = st.slider("Tingkat Kupon (%)",            1, 20, 8,  key="kpn2")
    with col3: nthn2   = st.slider("Jangka Waktu (tahun)",         1, 30, 5,  key="nthn2")
    freq2 = 2  # semesteran

    # Generate price-yield curve
    ytm_range = np.linspace(1, 25, 100)
    prices    = []
    for ytm_val in ytm_range:
        r_v = ytm_val / 100 / freq2
        n_v = nthn2 * freq2
        C_v = nom2 * kpn2 / 100 / freq2
        pv_c = C_v * (1 - (1 + r_v)**(-n_v)) / r_v if r_v > 0 else C_v * n_v
        pv_n = nom2 / (1 + r_v)**n_v
        prices.append(pv_c + pv_n)

    fig_py = go.Figure()
    fig_py.add_trace(go.Scatter(
        x=ytm_range, y=prices, mode="lines",
        line=dict(color="#6a9ad8", width=2.5),
        name="Harga Obligasi", fill="tozeroy", fillcolor="rgba(106,154,216,0.07)"
    ))
    # Mark current kupon rate
    r_par = kpn2 / 100 / freq2
    n_par = nthn2 * freq2
    C_par = nom2 * kpn2 / 100 / freq2
    pv_c_par = C_par * (1 - (1+r_par)**(-n_par)) / r_par
    pv_n_par = nom2 / (1+r_par)**n_par
    price_at_kupon = pv_c_par + pv_n_par
    fig_py.add_vline(x=kpn2, line_dash="dot", line_color="rgba(180,160,60,0.5)")
    fig_py.add_hline(y=nom2,  line_dash="dot", line_color="rgba(180,160,60,0.3)")
    fig_py.add_trace(go.Scatter(
        x=[kpn2], y=[price_at_kupon], mode="markers",
        marker=dict(size=10, color="#b8a848", symbol="diamond"),
        name=f"Par (YTM={kpn2}%)"
    ))
    fig_py.update_layout(
        template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        title=dict(text=f"Kurva Harga vs YTM — Obligasi {kpn2}% selama {nthn2} tahun",
                   font=dict(color="#8090a8", size=12)),
        xaxis=dict(title="YTM (%)", ticksuffix="%", tickfont=dict(size=10, color="#5a6880"),
                   gridcolor="rgba(255,255,255,0.04)"),
        yaxis=dict(title="Harga Obligasi (Rp)", tickfont=dict(size=10, color="#5a6880"),
                   gridcolor="rgba(255,255,255,0.04)"),
        legend=dict(font=dict(color="#6878a0", size=11), bgcolor="rgba(0,0,0,0)"),
        height=360, margin=dict(l=10, r=10, t=44, b=30),
    )
    st.plotly_chart(fig_py, use_container_width=True)

    # Tabel skenario YTM
    st.markdown('<div class="sec">📋 Tabel Skenario: Harga pada Berbagai Tingkat YTM</div>', unsafe_allow_html=True)
    scenario_ytm = [4, 6, kpn2-2, kpn2, kpn2+2, 12, 16, 20]
    scenario_ytm = sorted(list(set([max(1, y) for y in scenario_ytm])))
    sc_rows = []
    for ytm_sc in scenario_ytm:
        r_sc  = ytm_sc / 100 / freq2
        n_sc  = nthn2 * freq2
        C_sc  = nom2  * kpn2 / 100 / freq2
        pv_c_sc = C_sc * (1-(1+r_sc)**(-n_sc)) / r_sc if r_sc > 0 else C_sc * n_sc
        pv_n_sc = nom2 / (1+r_sc)**n_sc
        hsc  = pv_c_sc + pv_n_sc
        prm  = (hsc - nom2) / nom2 * 100
        cat  = "🟢 Premium" if prm > 1 else "🔴 Diskon" if prm < -1 else "🟡 Par"
        sc_rows.append({
            "YTM (%)": f"{ytm_sc}%",
            "Harga (Rp)": f"Rp {hsc:,.0f}",
            "Premium/Diskon": f"{prm:+.2f}%",
            "Kategori": cat,
        })
    st.dataframe(pd.DataFrame(sc_rows), use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="sec" style="margin-top:1.2rem">📌 Tiga Prinsip Penting Hubungan Harga–Yield</div>
    """, unsafe_allow_html=True)
    prinsip = [
        ("1", "YTM = Kupon Rate → Harga = Nominal (Par)", "Obligasi diperdagangkan tepat di nilai nominalnya."),
        ("2", "YTM < Kupon Rate → Harga > Nominal (Premium)", "Investor bersedia bayar lebih karena kupon lebih menarik dari pasar."),
        ("3", "YTM > Kupon Rate → Harga < Nominal (Diskon)", "Obligasi dijual murah agar imbal hasil kompetitif dengan pasar."),
    ]
    for num, title, desc in prinsip:
        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);
             border-left:3px solid rgba(80,130,200,0.45);border-radius:0 9px 9px 0;
             padding:0.65rem 1rem;margin-bottom:0.4rem">
            <p style="font-size:0.88rem;font-weight:600;color:#7a9ab0 !important;margin:0 0 0.2rem 0">
                {num}. {title}</p>
            <p style="font-size:0.82rem;color:#4a6a80 !important;margin:0">{desc}</p>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="warn"><p>⚠️ Perubahan suku bunga oleh Bank Indonesia (BI Rate) secara langsung mempengaruhi harga obligasi di pasar sekunder. Ini adalah risiko utama investor obligasi — disebut <strong>interest rate risk</strong>.</p></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# PDF EXPORT — PENILAIAN SAHAM & OBLIGASI
# ══════════════════════════════════════════════════════════════════
import datetime as _dt_so

st.markdown("---")
st.markdown('<p style="font-size:0.82rem;color:#3a5870 !important;margin-bottom:0.5rem">📄 Unduh ringkasan valuasi saham dan obligasi saat ini dalam format PDF.</p>', unsafe_allow_html=True)

def _buat_pdf_saham_obligasi():
    import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from utils import BisnisKuPDF
    import datetime
    pdf = BisnisKuPDF("Penilaian Saham & Obligasi")
    pdf.add_page()

    pdf.section("Informasi Laporan")
    pdf.kv("Topik",        "Valuasi Saham dan Obligasi")
    pdf.kv("Tanggal",      datetime.datetime.now().strftime("%d %B %Y %H:%M"))
    pdf.kv("Dibuat oleh",  "BisnisKu — FEB UM Metro")

    # Valuasi Obligasi
    pdf.section("Valuasi Obligasi")
    pdf.kv("Nilai Nominal",       f"Rp {nom2:,.0f}")
    pdf.kv("Tingkat Kupon",       f"{kpn2}%/tahun")
    pdf.kv("Jangka Waktu",        f"{nthn2} tahun")
    pdf.kv("Required Yield (YTM)",f"{ytm_input if 'ytm_input' in dir() else kpn2}%")

    # Hitung ulang untuk PDF
    _freq = freq_n if 'freq_n' in dir() else 2
    _ytm  = ytm_input if 'ytm_input' in dir() else kpn2
    _r    = _ytm/100/_freq
    _n    = nthn2 * _freq
    _C    = nom2 * kpn2/100/_freq
    _pv_c = _C*(1-(1+_r)**(-_n))/_r if _r>0 else _C*_n
    _harga= _pv_c + nom2/(1+_r)**_n
    _prm  = (_harga-nom2)/nom2*100

    pdf.kv("Harga Wajar Obligasi", f"Rp {_harga:,.0f}")
    prm_label = "Premium" if _prm>1 else "Diskon" if _prm<-1 else "Par"
    pdf.kv("Status",              f"{prm_label} ({_prm:+.2f}% dari nominal)")
    pdf.alert(
        f"Obligasi diperdagangkan {prm_label.lower()} — kupon {'>' if _prm>0 else '<'} YTM.",
        ok=True
    )

    # Price-Yield Scenarios
    pdf.section("Skenario Harga pada Berbagai YTM")
    pdf.th(["YTM (%)","Harga Obligasi (Rp)","Premium/Diskon","Status"],[28,55,45,54])
    for i,ytm_sc in enumerate([4,6,8,kpn2,12,16,20]):
        r_sc = ytm_sc/100/_freq; n_sc = nthn2*_freq; C_sc = nom2*kpn2/100/_freq
        pv_c_sc = C_sc*(1-(1+r_sc)**(-n_sc))/r_sc if r_sc>0 else C_sc*n_sc
        h_sc = pv_c_sc + nom2/(1+r_sc)**n_sc
        p_sc = (h_sc-nom2)/nom2*100
        status_sc = "Premium" if p_sc>1 else "Diskon" if p_sc<-1 else "Par"
        pdf.tr([f"{ytm_sc}%", f"Rp {h_sc:,.0f}", f"{p_sc:+.2f}%", status_sc],
               [28,55,45,54], even=i%2==0)

    pdf.section("Prinsip Hubungan Harga & Yield")
    prinsip = [
        ("YTM = Kupon", "Harga = Nominal (Par)"),
        ("YTM < Kupon", "Harga > Nominal (Premium) — kupon lebih menarik dari pasar"),
        ("YTM > Kupon", "Harga < Nominal (Diskon) — harga turun agar kompetitif"),
    ]
    pdf.th(["Kondisi","Implikasi"],[55,127])
    for i,(a,b) in enumerate(prinsip):
        pdf.tr([a,b],[55,127],even=i%2==0)
    pdf.note("Suku bunga BI naik -> harga obligasi turun. Ini adalah interest rate risk utama investor obligasi.")
    return pdf.build()

st.download_button(
    label="📄 Unduh Laporan Penilaian Saham & Obligasi (PDF)",
    data=_buat_pdf_saham_obligasi(),
    file_name=f"BisnisKu_Valuasi_SahamObligasi_{_dt_so.date.today()}.pdf",
    mime="application/pdf",
)
