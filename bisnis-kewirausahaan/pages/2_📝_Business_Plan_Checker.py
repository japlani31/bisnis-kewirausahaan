import streamlit as st

st.set_page_config(page_title="Business Plan Checker", page_icon="📝", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap');
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
section[data-testid="stSidebar"] { background: rgba(255,255,255,0.04) !important; border-right: 1px solid rgba(255,255,255,0.08); }
section[data-testid="stSidebar"] * { color: #e0e0e0 !important; }
h1,h2,h3 { color: white !important; }
p, li, label { color: rgba(255,255,255,0.8) !important; }
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background: #ffffff !important;
    color: #111111 !important;
    border: 1.5px solid rgba(255,255,255,0.35) !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder { color: #888 !important; }
div[data-baseweb="select"] > div { background: #ffffff !important; color: #111111 !important; border-radius: 8px !important; }
div[data-baseweb="select"] span { color: #111111 !important; }
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    color: white;
    margin: 1.5rem 0 0.75rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(249,199,79,0.4);
}
.score-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
}
.score-val { font-size: 2rem; font-weight: 800; }
.score-lbl { font-size: 0.78rem; color: rgba(255,255,255,0.5); margin-top:0.25rem; }
.swot-box {
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
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
.result-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="font-family:Syne,sans-serif;font-size:2rem;font-weight:800;background:linear-gradient(90deg,#f9c74f,#90e0ef);-webkit-background-clip:text;-webkit-text-fill-color:transparent">📝 Business Plan Checker</p>', unsafe_allow_html=True)
st.markdown('<p style="color:rgba(255,255,255,0.6)">Isi formulir di bawah ini, sistem akan menganalisis kelayakan ide bisnis Anda secara otomatis.</p>', unsafe_allow_html=True)

st.markdown("---")

# ─── FORM INPUT ──────────────────────────────────────────────────
st.markdown('<div class="section-title">1️⃣ Deskripsi Ide Bisnis</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    nama_bisnis = st.text_input("Nama Bisnis / Brand", placeholder="Contoh: EcoBox Packaging")
    kategori = st.selectbox("Kategori Bisnis", [
        "Kuliner/F&B", "Fashion & Aksesoris", "Jasa Digital/Tech",
        "Pendidikan & Pelatihan", "Kesehatan & Kecantikan",
        "Lingkungan/Sustainability", "Retail & E-commerce", "Lainnya"
    ])
with col2:
    target_pasar = st.text_input("Target Pasar", placeholder="Contoh: Mahasiswa usia 18-25 tahun")
    lokasi = st.text_input("Lokasi Bisnis", placeholder="Contoh: Metro, Lampung")

deskripsi = st.text_area("Deskripsi Singkat Bisnis Anda", 
    placeholder="Jelaskan produk/jasa yang ditawarkan, bagaimana cara kerjanya, dan nilai uniknya...",
    height=120)

# ─── ANALISIS SWOT ───────────────────────────────────────────────
st.markdown('<div class="section-title">2️⃣ Analisis SWOT</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Isi sebanyak mungkin — semakin detail, semakin akurat analisisnya.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    kekuatan = st.text_area("💪 STRENGTHS (Kekuatan)",
        placeholder="Apa keunggulan bisnis Anda?\nContoh:\n- Produk unik dan inovatif\n- Harga lebih terjangkau\n- Tim berpengalaman",
        height=140)
    peluang = st.text_area("🚀 OPPORTUNITIES (Peluang)",
        placeholder="Peluang apa yang ada di pasar?\nContoh:\n- Tren gaya hidup sehat meningkat\n- Belum banyak kompetitor\n- Dukungan pemerintah untuk UMKM",
        height=140)
with col2:
    kelemahan = st.text_area("⚠️ WEAKNESSES (Kelemahan)",
        placeholder="Apa kelemahan bisnis Anda?\nContoh:\n- Modal terbatas\n- Brand belum dikenal\n- Ketergantungan pada satu supplier",
        height=140)
    ancaman = st.text_area("🔴 THREATS (Ancaman)",
        placeholder="Ancaman apa yang mungkin dihadapi?\nContoh:\n- Kompetitor besar yang sudah mapan\n- Perubahan regulasi\n- Fluktuasi harga bahan baku",
        height=140)

# ─── KELAYAKAN PASAR ─────────────────────────────────────────────
st.markdown('<div class="section-title">3️⃣ Penilaian Mandiri</div>', unsafe_allow_html=True)
st.markdown('<p style="font-size:0.85rem;color:rgba(255,255,255,0.5)">Jawab jujur — ini untuk membantu penilaian yang akurat.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    riset_pasar = st.radio("Sudah melakukan riset pasar?",
        ["Belum sama sekali", "Sedikit (tanya teman/keluarga)", "Cukup (survei kecil)", "Mendalam (survei, observasi)"])
    kompetitor = st.radio("Kondisi kompetitor?",
        ["Belum ada kompetitor", "Ada sedikit kompetitor", "Kompetitor cukup banyak", "Sangat kompetitif"])
with col2:
    keunikan = st.radio("Keunikan produk/jasa Anda?",
        ["Sama seperti yang lain", "Sedikit berbeda", "Cukup unik", "Sangat unik/inovatif"])
    pengalaman = st.radio("Pengalaman di bidang ini?",
        ["Tidak ada pengalaman", "Sedikit tertarik", "Pernah coba/belajar", "Sudah punya pengalaman nyata"])

modal_tersedia = st.selectbox("Berapa % modal yang sudah tersedia?",
    ["< 25%", "25% - 50%", "50% - 75%", "> 75% (hampir siap)"])

# ─── HITUNG SCORE ────────────────────────────────────────────────
if st.button("🔍 Analisis Business Plan Saya!"):

    if not nama_bisnis or not deskripsi:
        st.warning("⚠️ Mohon isi minimal Nama Bisnis dan Deskripsi terlebih dahulu.")
    else:
        # Scoring system
        score = 0
        feedback = []

        # Riset pasar (0-25)
        riset_score = {"Belum sama sekali": 0, "Sedikit (tanya teman/keluarga)": 8,
                       "Cukup (survei kecil)": 16, "Mendalam (survei, observasi)": 25}
        score += riset_score[riset_pasar]

        # Kompetitor (0-20)
        komp_score = {"Belum ada kompetitor": 20, "Ada sedikit kompetitor": 15,
                      "Kompetitor cukup banyak": 8, "Sangat kompetitif": 3}
        score += komp_score[kompetitor]

        # Keunikan (0-25)
        unik_score = {"Sama seperti yang lain": 0, "Sedikit berbeda": 8,
                      "Cukup unik": 16, "Sangat unik/inovatif": 25}
        score += unik_score[keunikan]

        # Pengalaman (0-15)
        exp_score = {"Tidak ada pengalaman": 0, "Sedikit tertarik": 5,
                     "Pernah coba/belajar": 10, "Sudah punya pengalaman nyata": 15}
        score += exp_score[pengalaman]

        # Modal (0-15)
        modal_score = {"< 25%": 0, "25% - 50%": 5, "50% - 75%": 10, "> 75% (hampir siap)": 15}
        score += modal_score[modal_tersedia]

        # SWOT completeness bonus
        swot_filled = sum([1 for x in [kekuatan, kelemahan, peluang, ancaman] if len(x.strip()) > 20])
        score += swot_filled * 2  # max +8, tapi kita cap di 100

        score = min(score, 100)

        # ─── HASIL ───────────────────────────────────────────────
        st.markdown("---")
        st.markdown('<div class="section-title">📊 Hasil Analisis</div>', unsafe_allow_html=True)

        # Score breakdown
        col1, col2, col3, col4 = st.columns(4)
        if score >= 75:
            grade, grade_color, grade_label = "A", "#48c78e", "Sangat Layak"
        elif score >= 60:
            grade, grade_color, grade_label = "B", "#f9c74f", "Layak dengan Perbaikan"
        elif score >= 40:
            grade, grade_color, grade_label = "C", "#f3722c", "Perlu Perbaikan Signifikan"
        else:
            grade, grade_color, grade_label = "D", "#f94144", "Perlu Rethinking"

        with col1:
            st.markdown(f"""<div class="score-card">
                <div class="score-val" style="color:{grade_color}">{score}/100</div>
                <div class="score-lbl">Total Score</div>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class="score-card">
                <div class="score-val" style="color:{grade_color}">{grade}</div>
                <div class="score-lbl">Grade</div>
            </div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""<div class="score-card">
                <div class="score-val" style="color:{grade_color}" style="font-size:1.1rem">{grade_label}</div>
                <div class="score-lbl">Status Kelayakan</div>
            </div>""", unsafe_allow_html=True)
        with col4:
            st.markdown(f"""<div class="score-card">
                <div class="score-val" style="color:#90e0ef">{kategori.split('/')[0]}</div>
                <div class="score-lbl">Kategori Bisnis</div>
            </div>""", unsafe_allow_html=True)

        # Progress bar
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<p style="color:rgba(255,255,255,0.6);font-size:0.9rem">Score Kelayakan: <strong style="color:{grade_color}">{score}%</strong></p>', unsafe_allow_html=True)
        st.progress(score / 100)

        # ─── SWOT DISPLAY ────────────────────────────────────────
        st.markdown('<div class="section-title">🔄 Ringkasan SWOT Anda</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        def swot_card(title, content, bg_color, icon):
            items = [f"<li>{line.strip().lstrip('-•').strip()}</li>"
                     for line in content.strip().split('\n') if line.strip()] if content.strip() else ["<li><em>Belum diisi</em></li>"]
            return f"""<div class="swot-box" style="background:{bg_color};border:1px solid rgba(255,255,255,0.1)">
                <strong style="color:white">{icon} {title}</strong>
                <ul style="margin:0.5rem 0 0 0;padding-left:1.2rem">{"".join(items)}</ul>
            </div>"""

        with col1:
            st.markdown(swot_card("Strengths", kekuatan, "rgba(72,199,142,0.15)", "💪"), unsafe_allow_html=True)
            st.markdown(swot_card("Opportunities", peluang, "rgba(144,224,239,0.15)", "🚀"), unsafe_allow_html=True)
        with col2:
            st.markdown(swot_card("Weaknesses", kelemahan, "rgba(249,199,79,0.15)", "⚠️"), unsafe_allow_html=True)
            st.markdown(swot_card("Threats", ancaman, "rgba(249,65,68,0.15)", "🔴"), unsafe_allow_html=True)

        # ─── REKOMENDASI ─────────────────────────────────────────
        st.markdown('<div class="section-title">💡 Rekomendasi untuk Anda</div>', unsafe_allow_html=True)

        rekomendasi = []

        if riset_pasar in ["Belum sama sekali", "Sedikit (tanya teman/keluarga)"]:
            rekomendasi.append("📋 **Lakukan riset pasar lebih mendalam** — buat survei online (Google Form) dan bagikan ke calon pelanggan target Anda minimal 30 responden.")

        if kompetitor in ["Kompetitor cukup banyak", "Sangat kompetitif"]:
            rekomendasi.append("🎯 **Perkuat diferensiasi** — karena kompetitor banyak, pastikan ada 1-2 hal yang benar-benar membedakan bisnis Anda dari yang lain.")

        if keunikan in ["Sama seperti yang lain", "Sedikit berbeda"]:
            rekomendasi.append("💡 **Tingkatkan inovasi produk/jasa** — pertimbangkan menambahkan fitur unik, layanan tambahan, atau model bisnis yang berbeda.")

        if pengalaman in ["Tidak ada pengalaman", "Sedikit tertarik"]:
            rekomendasi.append("📚 **Bangun pengalaman dulu** — ikuti pelatihan, magang, atau mulai dari skala sangat kecil untuk belajar sambil praktik.")

        if modal_tersedia in ["< 25%", "25% - 50%"]:
            rekomendasi.append("💰 **Siapkan sumber pendanaan** — eksplorasi KUR (Kredit Usaha Rakyat), investor, crowdfunding, atau program inkubator kampus.")

        if not kekuatan.strip():
            rekomendasi.append("✍️ **Lengkapi analisis SWOT Anda** — terutama bagian Strengths agar lebih mudah dipresentasikan ke investor atau dosen.")

        if not rekomendasi:
            rekomendasi.append("🌟 Business plan Anda sudah cukup kuat! Langkah selanjutnya: buat pitch deck dan mulai uji coba skala kecil (MVP).")

        for i, rek in enumerate(rekomendasi, 1):
            st.markdown(f"""<div class="result-card">
                <p style="margin:0"><strong style="color:#f9c74f">#{i}</strong> {rek}</p>
            </div>""", unsafe_allow_html=True)

        # CTA
        st.markdown("""<div style="background:rgba(249,199,79,0.08);border:1px solid rgba(249,199,79,0.25);
        border-radius:12px;padding:1rem 1.5rem;margin-top:1rem">
            <p style="margin:0;color:rgba(255,255,255,0.85)">
                📊 <strong style="color:#f9c74f">Langkah berikutnya:</strong> 
                Gunakan fitur <strong>Simulasi Keuangan</strong> di menu sidebar untuk menghitung proyeksi finansial bisnis Anda!
            </p>
        </div>""", unsafe_allow_html=True)

        # ── PDF EXPORT ─────────────────────────────────────────────
        st.markdown("---")

        def _buat_pdf_bp():
            import sys, os
            sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
            from utils import BisnisKuPDF
            import datetime
            pdf = BisnisKuPDF(f"Business Plan Checker — {nama_bisnis}")
            pdf.add_page()

            pdf.section("Informasi Bisnis")
            pdf.kv("Nama Bisnis",  nama_bisnis)
            pdf.kv("Kategori",     kategori)
            pdf.kv("Target Pasar", target_pasar)
            pdf.kv("Lokasi",       lokasi)
            pdf.kv("Tanggal",      datetime.datetime.now().strftime("%d %B %Y %H:%M"))

            pdf.section("Hasil Penilaian")
            pdf.kv("Total Score",      f"{score} / 100")
            pdf.kv("Grade",            grade)
            pdf.kv("Status Kelayakan", grade_label)
            pdf.alert(
                f"Grade {grade} — {grade_label}: Skor {score}/100",
                ok=score >= 60
            )

            pdf.section("Deskripsi Bisnis")
            pdf.set_font("Helvetica", "", 9)
            pdf.set_text_color(60, 80, 110)
            pdf.multi_cell(0, 5, f"  {deskripsi[:400]}{'...' if len(deskripsi)>400 else ''}")
            pdf.set_text_color(0, 0, 0)
            pdf.ln(2)

            pdf.section("Analisis SWOT")
            swot_items = [
                ("Strengths (Kekuatan)",  kekuatan),
                ("Weaknesses (Kelemahan)",kelemahan),
                ("Opportunities (Peluang)",peluang),
                ("Threats (Ancaman)",     ancaman),
            ]
            for title, content in swot_items:
                pdf.sub(title)
                lines = [l.strip().lstrip("-•").strip() for l in (content or "Belum diisi").split("\n") if l.strip()]
                for ln in lines[:5]:
                    pdf.set_font("Helvetica", "", 8.5)
                    pdf.set_text_color(60, 80, 110)
                    pdf.cell(0, 5, f"  • {ln[:90]}", ln=True)
                pdf.set_text_color(0, 0, 0)
                pdf.ln(1)

            pdf.section("Rincian Penilaian Mandiri")
            pdf.th(["Kriteria","Jawaban","Skor Kontribusi"],[65,70,47])
            penilaian_rows = [
                ("Riset Pasar",   riset_pasar,     str(riset_score[riset_pasar])),
                ("Kompetitor",    kompetitor,      str(komp_score[kompetitor])),
                ("Keunikan",      keunikan,        str(unik_score[keunikan])),
                ("Pengalaman",    pengalaman,      str(exp_score[pengalaman])),
                ("Modal",         modal_tersedia,  str(modal_score[modal_tersedia])),
                ("Kelengkapan SWOT",f"{swot_filled}/4 terisi",f"+{swot_filled*2}"),
            ]
            for i,(a,b,c) in enumerate(penilaian_rows):
                pdf.tr([a,b,c],[65,70,47],even=i%2==0)

            pdf.section("Rekomendasi Pengembangan")
            for i, rek in enumerate(rekomendasi, 1):
                rek_clean = rek.replace("**","").replace("📋","").replace("🎯","").replace("💡","").replace("📚","").replace("💰","").replace("✍️","").replace("🌟","").strip()
                pdf.set_font("Helvetica", "B", 8.5)
                pdf.set_text_color(24, 50, 88)
                pdf.cell(0, 5, f"  {i}. Rekomendasi", ln=True)
                pdf.set_font("Helvetica", "", 8.5)
                pdf.set_text_color(60, 80, 110)
                pdf.multi_cell(0, 4.5, f"     {rek_clean[:200]}")
                pdf.set_text_color(0, 0, 0)
                pdf.ln(1)

            pdf.note("Laporan ini dibuat otomatis oleh sistem BisnisKu berdasarkan input pengguna. Tidak menggantikan konsultasi bisnis profesional.")
            return pdf.build()

        import datetime as _dt_bp
        fname_bp = f"BisnisKu_BusinessPlan_{nama_bisnis.replace(' ','_')}_{_dt_bp.date.today()}.pdf"
        col1, col2 = st.columns([2,3])
        with col1:
            st.download_button(
                label="📄 Unduh Laporan Business Plan (PDF)",
                data=_buat_pdf_bp(),
                file_name=fname_bp,
                mime="application/pdf",
            )
