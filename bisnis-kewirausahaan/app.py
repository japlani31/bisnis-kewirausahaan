import streamlit as st

st.set_page_config(
    page_title="BisnisKu — Tools Kewirausahaan",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Syne:wght@700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.04) !important;
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}

/* Cards */
.hero-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
}

.feature-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #f9c74f, #f3722c, #f94144);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.2;
}

.hero-sub {
    color: rgba(255,255,255,0.65);
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

.badge {
    display: inline-block;
    background: rgba(249,199,79,0.15);
    border: 1px solid rgba(249,199,79,0.4);
    color: #f9c74f;
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 1rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}

h1, h2, h3 { color: white !important; }
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    background: #ffffff !important; color: #111111 !important;
    border: 1.5px solid rgba(255,255,255,0.35) !important; border-radius: 8px !important;
}
div[data-baseweb="select"] > div { background: #ffffff !important; color: #111111 !important; border-radius: 8px !important; }
div[data-baseweb="select"] span { color: #111111 !important; }
p, li { color: rgba(255,255,255,0.75) !important; }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-card">
    <div class="badge">🎓 Prodi S1 Kewirausahaan</div>
    <p class="hero-title">BisnisKu Tools</p>
    <p class="hero-sub">Platform simulasi keuangan & analisis business plan untuk mahasiswa kewirausahaan</p>
</div>
""", unsafe_allow_html=True)

# Feature cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:3rem; margin-bottom:0.75rem">📊</div>
        <h3 style="margin:0 0 0.5rem 0">Simulasi Keuangan</h3>
        <p style="font-size:0.9rem">Hitung BEP, proyeksi cashflow, ROI, dan kelayakan finansial bisnis Anda secara otomatis.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:3rem; margin-bottom:0.75rem">📝</div>
        <h3 style="margin:0 0 0.5rem 0">Business Plan Checker</h3>
        <p style="font-size:0.9rem">Validasi ide bisnis Anda dengan analisis SWOT, scoring kelayakan, dan saran pengembangan.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(249,199,79,0.08); border: 1px solid rgba(249,199,79,0.25); 
border-radius: 12px; padding: 1rem 1.5rem;">
    <p style="margin:0; color: rgba(255,255,255,0.8) !important; font-size:0.95rem">
        👈 <strong style="color:#f9c74f">Pilih menu di sidebar kiri</strong> untuk mulai menggunakan fitur yang tersedia.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color: rgba(255,255,255,0.3); font-size:0.8rem; border-top: 1px solid rgba(255,255,255,0.08); padding-top:1rem">
    BisnisKu Tools · Prodi S1 Kewirausahaan · UM Metro
</div>
""", unsafe_allow_html=True)
