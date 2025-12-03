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
# PREPROCESS
# ========================
def preprocess_image(image):
    image = np.array(image)

    # Normalize channel format
    if len(image.shape) == 2:  # grayscale
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (150, 150))
    image = image / 255.0
    return np.expand_dims(image, axis=0)


# ========================
# REKOMENDASI EMOSI
# ========================
def get_recommendation(emotion):
    emotion = emotion.lower()

    data = {
        "sad": {
            "emoji": "😢",
            "title": "Kamu terlihat sedang sedih",
            "desc": "Tidak apa-apa merasa sedih. Coba beberapa hal berikut:",
            "recs": [
                "🎧 Dengarkan musik menenangkan",
                "✍️ Journaling ringan",
                "👣 Jalan santai 3–5 menit",
                "📹 Tonton video motivasi ringan"
            ],
            "spotify": "https://open.spotify.com/embed/playlist/2EGmGCvE9Wb38EB9Yt2aYB"
        },
        "happy": {
            "emoji": "😀",
            "title": "Kamu sedang merasa senang!",
            "desc": "Pertahankan mood positifmu!",
            "recs": [
                "🎧 Putar playlist happy vibe",
                "🎉 Bagikan kabar baik ke teman",
                "✨ Catat hal baik hari ini",
                "🚀 Lanjutkan aktivitas produktif"
            ],
            "spotify": "https://open.spotify.com/embed/playlist/37i9dQZF1DX9XIFQuFvzM4"
        },
        "angry": {
            "emoji": "😡",
            "title": "Sepertinya kamu sedang marah",
            "desc": "Marah itu manusiawi. Coba beberapa cara berikut:",
            "recs": [
                "🌬️ Deep breathing 4-7-8",
                "✍️ Tulis penyebab kemarahanmu",
                "🎧 Musik relaksasi",
                "🧘 Meditasi singkat 2 menit"
            ],
            "youtube": "https://www.youtube.com/embed/acUZdGd_3Dg?si=iEsJx9HIXCVHjGYR"
        },
        "fear": {
            "emoji": "😨",
            "title": "Kamu terlihat takut",
            "desc": "Tidak apa-apa, mari tenangkan pikiranmu:",
            "recs": [
                "🔍 Identifikasi apa yang membuatmu takut",
                "🌬️ Teknik grounding 5-4-3-2-1",
                "💬 Hubungi orang yang kamu percaya",
                "🎧 Musik relaksasi"
            ],
            "spotify": "https://open.spotify.com/embed/playlist/7AZuDiVAVNfBQCI1cnUfMX"
        },
        "surprise": {
            "emoji": "😮",
            "title": "Kamu terlihat terkejut",
            "desc": "Ambil napas, dan coba hal ini:",
            "recs": [
                "🌬️ Tarik napas dalam 3 kali",
                "🧠 Identifikasi apa yang mengejutkanmu",
                "👣 Jalan sebentar"
            ]
        }
    }
    return data.get(emotion)


# ========================
# MAIN FUNCTION
# ========================
def show():

    # STYLE CARD
    st.markdown("""
    <style>
        .emotion-card {
            padding: 25px;
            border-radius: 18px;
            background-color: #ffffff;
            box-shadow: 0 4px 18px rgba(0,0,0,0.08);
            margin-top: 20px;
            color: #0AA063 !important;
        }

        .emotion-title {
            font-size: 26px;
            font-weight: 700;
            display: flex;
            align-items: center;
            color: #0AA063 !important;
        }

        .emoji {
            font-size: 40px;
            margin-right: 10px;
        }

        .recommendation-item {
            font-size: 18px;
            margin-bottom: 6px;
            color: #0AA063 !important;
        }

        .emotion-card p,
        .emotion-card li,
        .emotion-card b,
        .emotion-card span,
        .emotion-card div {
            color: #0AA063 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='font-size:45px; font-weight:900;'>Deteksi Emosi Wajah</h1>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader("Upload Foto", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            st.session_state.uploaded_image = uploaded_file

    with col2:
        cam = st.camera_input("Ambil Foto")
        if cam:
            st.session_state.uploaded_image = cam

    # PREVIEW IMAGE
    if "uploaded_image" in st.session_state:
        img = Image.open(st.session_state.uploaded_image)
        st.image(img, use_container_width=True)
    else:
        st.info("Belum ada gambar.")

    # DETEKSI TOMBOL
    if st.button("🔍 Analisis Emosi", use_container_width=True):

        if "uploaded_image" not in st.session_state:
            st.warning("Upload atau ambil foto terlebih dahulu!")
            return

        if "model" not in st.session_state:
            st.error("Model belum dimuat ke session_state.model")
            return

        model = st.session_state.model
        img = Image.open(st.session_state.uploaded_image)

        processed = preprocess_image(img)
        preds = model.predict(processed, verbose=0)

        labels = ['Angry', 'Fear', 'Happy', 'Sad', 'Surprise']

        st.session_state.detection_result = {
            labels[i]: float(preds[0][i]) * 100 for i in range(5)
        }

        st.rerun()

    # SHOW RECOMMENDATION
    if "detection_result" in st.session_state:

        emotion = max(
            st.session_state.detection_result,
            key=st.session_state.detection_result.get
        ).lower()

        rec = get_recommendation(emotion)

        if rec:
            st.markdown("<h3>🎯 Rekomendasi untuk Kondisimu</h3>",
                        unsafe_allow_html=True)

            html = f"""
            <div class="emotion-card">

            <div class="emotion-title">
                <span class="emoji">{rec['emoji']}</span>
                {rec['title']}
            </div>

            <p>{rec['desc']}</p>

            <ul>
            """

            for item in rec["recs"]:
                html += f"<li class='recommendation-item'>{item}</li>"

            html += "</ul>"

            # MEDIA HANDLER
            if "spotify" in rec:
                html += f"""
                <b>🎵 Playlist rekomendasi:</b><br>
                <iframe src="{rec['spotify']}"
                    width="100%" height="380" style="border-radius:12px;"
                    frameborder="0" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture">
                </iframe>
                """

            elif "youtube" in rec:
                html += f"""
                <b>📺 Video rekomendasi:</b><br>
                <iframe width="100%" height="315"
                    src="{rec['youtube']}"
                    frameborder="0" allowfullscreen
                    style="border-radius:12px;">
                </iframe>
                """

            html += "</div>"

            st.markdown(html, unsafe_allow_html=True)
