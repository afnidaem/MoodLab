import streamlit as st

def show():
    st.markdown("""
    <style>

        /* Import font Poppins dari Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

        /* Terapkan Poppins ke seluruh halaman */
        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif !important;
        }

        .emotion-card {
            background-color: white;
            border: 2px solid #d1fae5;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            cursor: pointer;
            font-family: 'Poppins', sans-serif !important;
        }
        
        .emotion-card:hover {
            transform: translateY(-8px);
            border-color: #10b981;
            box-shadow: 0 8px 20px rgba(16, 185, 129, 0.25);
        }
        
        .emotion-emoji {
            font-size: 40px;
            margin-bottom: 10px;
            transition: transform 0.3s ease;
        }
        
        .emotion-card:hover .emotion-emoji {
            transform: scale(1.2);
        }
        
        .emotion-label {
            font-family: 'Poppins', sans-serif !important;
            font-size: 14px;
            font-weight: 600;
            color: #0aa06e;
        }

        /* Heading & paragraph juga Poppins */
        h1, h2, h3, p, div {
            font-family: 'Poppins', sans-serif !important;
        }
                
        @media (max-width: 600px) {
        .hero-title {
            font-size: 38px !important;
            line-height: 1.2 !important;
        }

        .auto-text {
            font-size: 32px !important;  /* kecilkan hanya ini */
            display: inline-block !important;
            white-space: nowrap !important;  /* cegah turun baris */
        }
    }

    </style>
    """, unsafe_allow_html=True)

    # Container utama
    st.markdown("<br>", unsafe_allow_html=True)

    # Badge
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div style="
                display: inline-block; 
                background-color: rgba(209, 250, 229, 0.8); 
                border: 2px solid #10b981; 
                border-radius: 25px; 
                padding: 8px 20px; 
                font-size: 14px; 
                font-weight: 600; 
                color: #0aa06e;
                font-family: 'Poppins', sans-serif !important;
            ">
                ✨ Powered by MoodLab
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Judul Utama
    st.markdown("""
    <h1 class="hero-title" style="text-align: center; font-family: 'Poppins', sans-serif; font-size: 65px; font-weight: 900; color: #000000; margin: 20px 0 10px 0;">
        Detect Your Emotions<br>
        <span class="auto-text" style="color: #059669;">Automatically</span>
    </h1>
    """, unsafe_allow_html=True)


    # Subtitle
    st.markdown("""
    <p style="text-align: center; font-family: 'Poppins', sans-serif; font-size: 22px; color: #6B7280; margin-bottom: 30px;">
        Upload foto wajah Anda dan dapatkan analisis emosi secara real-time
    </p>
    """, unsafe_allow_html=True)

    # Button mulai deteksi
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mulai Deteksi →", use_container_width=True, key="mulai_deteksi"):
            st.session_state.page = "Deteksi Emosi"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Judul kartu
    st.markdown("""
    <h3 style='text-align: center; font-family: 'Poppins', sans-serif; color: #6b7280; font-size: 18px; margin: 75px 0 20px 0;'>
        Emosi yang dapat dideteksi:
    </h3>
    """, unsafe_allow_html=True)

    # 5 kartu emosi
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("""
        <div class="emotion-card">
            <div class="emotion-emoji">😢</div>
            <div class="emotion-label">Sedih</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="emotion-card">
            <div class="emotion-emoji">😨</div>
            <div class="emotion-label">Takut</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="emotion-card">
            <div class="emotion-emoji">😊</div>
            <div class="emotion-label">Senang</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="emotion-card">
            <div class="emotion-emoji">😠</div>
            <div class="emotion-label">Marah</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="emotion-card">
            <div class="emotion-emoji">😲</div>
            <div class="emotion-label">Kaget</div>
        </div>
        """, unsafe_allow_html=True)