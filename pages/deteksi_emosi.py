import streamlit as st
from PIL import Image
import numpy as np
import cv2

# ========================
# EMOJI EMOTION
# ========================
EMOTION_EMOJI = {
    'Angry': '😠',
    'Fear': '😨',
    'Happy': '😊',
    'Sad': '😢',
    'Surprise': '😲'
}

# ========================
# FIXED PREPROCESSING (RGB, 150x150, 3 channel)
# ========================
def preprocess_image(image):
    """
    Preprocessing gambar untuk model MobileNetV2
    Input: RGB 150x150
    """
    # Convert Streamlit/PIL ke numpy BGR
    image = np.array(image)
    
    # Jika grayscale, convert ke RGB
    if len(image.shape) == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize sesuai model
    image = cv2.resize(image, (150, 150))

    # Normalisasi
    image = image / 255.0

    # Tambah dimensi → (1,150,150,3)
    image = np.expand_dims(image, axis=0)

    return image


# ========================
# HALAMAN DETEKSI
# ========================
def show():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    /* Terapkan font ke seluruh elemen HTML */
    html, body, div, p, h1, h2, h3, h4, h5, h6, button, label {
        font-family: 'Poppins', sans-serif !important;
    }

        /* Hilangkan teks icon collapse seperti "keyboard_double_arrow_right" */
        button[kind="icon"] svg, 
        button[title="Expand sidebar"] svg,
        button[title="Collapse sidebar"] svg {
        display: block !important;
    }
                
        .result-card {
        background-color: white;
        border-radius: 15px;
        padding: 18px 22px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.08);
        width: 100%;
    }

    .result-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid #e5e7eb;
    }

    .result-item:last-child {
        border-bottom: none;
    }

    .result-name {
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: 'Poppins', sans-serif;
    }

    .result-value {
        font-size: 18px;
        font-weight: 700;
        color: #059669;
        font-family: 'Poppins', sans-serif;
    }


    button[kind="icon"] {
        font-size: 0 !important;
        color: transparent !important;
    }

    .about-container {
        max-width: 1200px;
        width: 100%;
        margin: 0 auto;
        padding: 40px 20px 60px;
    }

    .about-card {
        background: white;
        width: 100%;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }

    .about-title {
        font-size: 32px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 20px;
    }

    .about-text {
        font-size: 15px;
        color: #4b5563;
        line-height: 1.8;
        margin-bottom: 15px;
    }

    .steps-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 25px;
        margin-top: 5px;
    }

    .step-card {
        background: #CCFBF1;
        padding: 22px;
        border-radius: 12px;
        border-left: 4px solid #059669;
    }

    .step-number {
        font-size: 24px;
        font-weight: 700;
        color: #1a1a1a;
        margin-bottom: 8px;
    }

    .step-title {
        font-size: 16px;
        font-weight: 600;
        color: #1a1a1a;
        margin-bottom: 6px;
    }

    .step-desc {
        font-size: 13px;
        color: #6b7280;
        margin-top: 4px;
    }

    .tech-wrapper {
        border: 3px solid #059669;
        border-radius: 18px;
        padding: 25px;
        background: white;
        margin-top: 10px;
    }

    .tech-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .tech-item {
        background: #f3f4f6;
        padding: 14px 16px;
        border-radius: 10px;
        margin-bottom: 12px;
    }

    .tech-item-title {
        font-weight: 700;
        font-size: 15px;
    }

    .tech-item-desc {
        font-size: 13px;
        color: #6b7280;
        margin-top: 4px;
    }

    @media (max-width: 768px) {
        .steps-grid {
            grid-template-columns: 1fr;
        }
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style="font-size: 65px; font-weight: 900; color: #000000; margin-bottom: 5px;">
        Deteksi Emosi Wajah
    </h1>
    <p style="font-size: 25px; color: #6B7280; margin-bottom: 75px;">
        Upload foto wajah Anda untuk mendeteksi emosi secara otomatis
    </p>
    """, unsafe_allow_html=True)

    # =================
    # UPLOAD / CAMERA
    # =================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="section-title">📁 Upload Foto</p>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Pilih File", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file

    with col2:
        st.markdown('<p class="section-title">📷 Ambil Foto</p>', unsafe_allow_html=True)
        cam = st.camera_input("Gunakan Kamera", label_visibility="collapsed")
        if cam:
            st.session_state.uploaded_image = cam

    # =================
    # PREVIEW
    # =================
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<p class="section-title">Preview</p>', unsafe_allow_html=True)
        if "uploaded_image" in st.session_state:
            img = Image.open(st.session_state.uploaded_image)
            st.image(img, use_container_width=True)
        else:
            st.info("Belum ada gambar.")

    # =================
    # HASIL DETEKSI
    # =================
    with col4:
        st.markdown('<p class="section-title">Hasil Deteksi</p>', unsafe_allow_html=True)

        if "detection_result" in st.session_state:
            for em, pct in st.session_state.detection_result.items():
                st.markdown(f"""
                <div class="result-item">
                    <div class="result-name">
                        <span style="font-size: 28px;">{EMOTION_EMOJI[em]}</span>
                        <span style="font-size: 16px; font-weight: 600;">{em}</span>
                    </div>
                    <div class="result-value">{pct:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        else:
            st.info("Hasil deteksi akan tampil di sini.")

    # =================
    # BUTTON
    # =================
    st.markdown("<br>", unsafe_allow_html=True)
    _, col_btn, _ = st.columns([1, 2, 1])

    with col_btn:
        if st.button("🔍 Analisis Emosi", use_container_width=True):

            if "uploaded_image" not in st.session_state:
                st.warning("Upload atau ambil foto terlebih dahulu!")
                return

            if st.session_state.model is None:
                st.error("❌ Model tidak dimuat!")
                return

            try:
                model = st.session_state.model
                img = Image.open(st.session_state.uploaded_image)
                processed = preprocess_image(img)
                preds = model.predict(processed, verbose=0)

                labels = ['Angry', 'Fear', 'Happy', 'Sad', 'Surprise']
                result = {labels[i]: preds[0][i] * 100 for i in range(5)}

                st.session_state.detection_result = result
                st.rerun()

            except Exception as e:
                st.error(f"❌ Error prediksi: {e}")