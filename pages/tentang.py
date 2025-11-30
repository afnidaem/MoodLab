import streamlit as st

def show():
    # Custom CSS
    st.markdown("""
    <style>
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
        color: #059669 !important;
        font-size: 32px;
        font-weight: 700;
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

    /* ==== Teknologi Card ==== */
    .tech-wrapper {
        border: 3px solid #059669;
        border-radius: 18px;
        padding: 25px;
        background: white;
        margin-top: 10px;
    }

    .tech-title {
        font-size: 20px;
        color: #059669;
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
        color: #059669;
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

    # CARD 1 — Tentang
    st.markdown("""
    <h1 style="font-size: 65px; font-weight: 900; color: #000000; margin-bottom: 6px;">
        Tentang Mood Lab
    </h1>
    <p style="font-size: 25px; color: #6B7280; margin-bottom: 0px;">
        Informasi lengkap tentang cara penggunaan dan teknologi yang digunakan.
    </p>
    """, unsafe_allow_html=True)

    # Buka container utama
    st.markdown("<div class='about-container'>", unsafe_allow_html=True)

    # CARD 2 — Cara Menggunakan
    st.markdown("""
    <div class='about-card'>
        <h2 class='about-title'>🚀 Cara Menggunakan</h2>
        <div class='steps-grid'>
            <div class='step-card'>
                <div class='step-number'>1</div>
                <div class='step-title'>Pilih Menu Deteksi Emosi</div>
                <div class='step-desc'>Klik tombol "Mulai Deteksi" atau menu "Deteksi Emosi" di navigasi</div>
            </div>
            <div class='step-card'>
                <div class='step-number'>2</div>
                <div class='step-title'>Pilih Metode Input</div>
                <div class='step-desc'>Pilih "Upload Photo" untuk mengunggah gambar atau "Take Photo" untuk menggunakan kamera</div>
            </div>
            <div class='step-card'>
                <div class='step-number'>3</div>
                <div class='step-title'>Pilih/Ambil Gambar</div>
                <div class='step-desc'>Unggah file gambar dari perangkat atau ambil foto menggunakan kamera</div>
            </div>
            <div class='step-card'>
                <div class='step-number'>4</div>
                <div class='step-title'>Klik Analisis Emosi</div>
                <div class='step-desc'>Tekan tombol "Analisis Emosi" untuk memulai proses analisis emosi</div>
            </div>
        </div>
    <p class='about-text' style='margin-top: 20px;'>
        <strong>Tips:</strong> Pastikan wajah terlihat jelas dalam foto untuk hasil deteksi yang lebih akurat.
        Hindari foto dengan pencahayaan yang terlalu gelap atau terlalu terang.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # CARD 3 — Teknologi yang Digunakan
    st.markdown("""
        <div class='about-card'>
            <div class='tech-wrapper'>
                <div class='tech-title'>Teknologi yang digunakan</div>
                <div class='tech-item'>
                    <div class='tech-item-title'>TensorFlow & Keras</div>
                    <div class='tech-item-desc'>Framework deep learning untuk membangun model CNN</div>
                </div>
                <div class='tech-item'>
                    <div class='tech-item-title'>Python</div>
                    <div class='tech-item-desc'>Bahasa pemrograman utama</div>
                </div>
                <div class='tech-item'>
                    <div class='tech-item-title'>Streamlit</div>
                    <div class='tech-item-desc'>Framework untuk membuat aplikasi web interaktif</div>
                </div>
                <div class='tech-item'>
                    <div class='tech-item-title'>OpenCV & PIL</div>
                    <div class='tech-item-desc'>Library untuk pemrosesan gambar</div>
                </div>
                <div class='tech-item'>
                    <div class='tech-item-title'>NumPy</div>
                    <div class='tech-item-desc'>Library untuk komputasi numerik</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Tutup container utama
    st.markdown("</div>", unsafe_allow_html=True)