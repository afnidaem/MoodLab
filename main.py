import streamlit as st
from PIL import Image
from pages import beranda, deteksi_emosi, tentang
import tensorflow as tf
from tensorflow import keras
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)  # Hilangkan TF1 warning

st.set_page_config(
    page_title="Mood Lab",
    page_icon="🔍",  # Emoji kaca pembesar
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD MODEL (HANYA SEKALI)
# =========================
@st.cache_resource
def load_model():
    try:
        model = keras.models.load_model("model.h5")   # Ganti jika nama file berbeda
        print("Model berhasil dimuat!")
        return model
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None

# Inisialisasi session_state.model
if "model" not in st.session_state:
    st.session_state.model = load_model()

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* Terapkan font ke seluruh elemen HTML */
html, body, div, p, h1, h2, h3, h4, h5, h6, button, label {
    font-family: 'Poppins', sans-serif !important;
}

/* Hilangkan teks internal seperti “keycl” yang bocor */
[data-testid="stDecoration"],
div[style*="pointer-events"] {
    color: transparent !important;
    font-size: 0 !important;
}
                        
/* Sembunyikan default navigation Streamlit */
[data-testid="stSidebarNav"] {
    display: none;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
    padding: 5px 20px 25px 20px;
}

/* Logo Box */
.logo-box {
    width: 45px;
    height: 45px;
    background-color: #0aa06e;
    border-radius: 8px;
    margin-bottom: 10px;
}

/* Logo Text */
.logo-text {
    font-family: 'Poppins', sans-serif !important;        
    font-size: 22px;
    font-weight: 700;
    margin-left: 5px;
    color: #0aa06e;
}

/* Styling untuk button Streamlit di sidebar */
.stSidebar button {
    width: 100%;
    background-color: #ffffff;
    color: #4c4c4c;
    border: none;
    border-radius: 10px;
    padding: 12px 15px;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 4px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex !important;
    justify-content: flex-start !important;
    align-items: center !important;
}

/* Gradasi hover: #10b981 100% opacity (0%) → #44bb88 65% opacity (100%) */
.stSidebar button:hover {
    background: linear-gradient(to right, rgba(16, 185, 129, 1) 0%, rgba(68, 187, 136, 0.65) 100%) !important;
    color: #000000 !important;
}

/* Button active/focus/visited state - HILANGKAN WARNA MERAH */
.stSidebar button:focus,
.stSidebar button:active,
.stSidebar button:focus-visible {
    background-color: #ffffff !important;
    color: #4c4c4c !important;
    box-shadow: none !important;
    border: none !important;
    outline: none !important;
}

/* Button active state berdasarkan halaman */
.stSidebar button[data-active="true"] {
    background: linear-gradient(to right, rgba(16, 185, 129, 1) 0%, rgba(68, 187, 136, 0.65) 100%) !important;
    color: #000000 !important;
}

/* Paksa text di dalam button tetap warna yang sama */
.stSidebar button p {
    margin: 0;
    text-align: left !important;
    width: 100%;
    color: inherit !important;
}

.stSidebar button div {
    justify-content: flex-start !important;
    text-align: left !important;
}

/* Hilangkan efek link/visited */
.stSidebar button:visited,
.stSidebar button:link {
    color: #4c4c4c !important;
}

/* ===== GRADASI LATAR BELAKANG HALAMAN (ATAS KE BAWAH) ===== */
.stMain {
    background: linear-gradient(to bottom, 
        rgba(248, 250, 252, 0) 0%, 
        rgba(209, 250, 229, 0.5) 50%, 
        rgba(204, 251, 241, 1) 100%) !important;
}

/* Alternative: jika ingin full page termasuk header */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, 
        rgba(248, 250, 252, 0) 0%, 
        rgba(209, 250, 229, 0.5) 50%, 
        rgba(204, 251, 241, 1) 100%) !important;
}

/* Styling untuk button Mulai Deteksi di content area */
.stMain div[data-testid="stButton"] button {
    background: linear-gradient(135deg, #14B8A6 0%, #0d9488 100%) !important;
    color: white !important;
    font-size: 9px !important;
    font-weight: 700 !important;
    padding: 18px 60px !important;
    border-radius: 8px !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(20, 184, 166, 0.4) !important;
    transition: all 0.3s ease !important;
    letter-spacing: 0.5px !important;
    width: 100% !important;  /* Full width dalam kolom */
}

.stMain div[data-testid="stButton"] button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 6px 20px rgba(20, 184, 166, 0.5) !important;
    background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%) !important;
}

.stMain div[data-testid="stButton"] button:active {
    transform: translateY(-1px) !important;
}

/* Responsive */
@media (max-width: 768px) {
    .features-grid {
        grid-template-columns: 1fr;
    }
    .steps-grid {
        grid-template-columns: 1fr;
    }
    .hero-title {
        font-size: 32px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR LAYOUT
# =========================
with st.sidebar:
    # Logo + Judul
    col1, col2 = st.columns([0.3, 1])
    with col1:
        logo = Image.open("moodlabb.png")
        st.image(logo, width=60)
    with col2:
        st.markdown('<div class="logo-text">Mood Lab</div>', unsafe_allow_html=True)

    st.write("")  # spasi

    # Navigation state
    if "page" not in st.session_state:
        st.session_state.page = "Beranda"

    # Menu Items dengan st.button
    if st.button("🏠 Beranda", key="nav_beranda", use_container_width=True):
        st.session_state.page = "Beranda"
        st.rerun()
    
    if st.button("😃 Deteksi Emosi", key="nav_deteksi", use_container_width=True):
        st.session_state.page = "Deteksi Emosi"
        st.rerun()
    
    if st.button("💬 Tentang", key="nav_tentang", use_container_width=True):
        st.session_state.page = "Tentang"
        st.rerun()

    st.markdown("---")
    st.markdown("**Mata Kuliah:** Pembelajaran Mesin")
    st.markdown("**Program Studi:** Teknik Informatika ITERA")

# =========================
# ROUTING HALAMAN
# =========================
page = st.session_state.page

if page == "Beranda":
    beranda.show()
elif page == "Deteksi Emosi":
    deteksi_emosi.show()
elif page == "Tentang":
    tentang.show()

# =========================
# FOOTER GLOBAL
# =========================
st.markdown("""
<style>
.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    padding: 18px 0;
    text-align: center;
    color: #6b7280;
    font-size: 14px;
    margin-top: 50px;
}
</style>

<div class="footer">
    © 2025 Mood Lab — Built for Machine Learning Project · Teknik Informatika ITERA
</div>
""", unsafe_allow_html=True)