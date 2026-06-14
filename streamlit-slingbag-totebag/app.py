import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image

# =========================
# Load Model
# =========================

MODEL_PATH = "mobilenetv2_best.keras"

model = tf.keras.models.load_model(
    MODEL_PATH
)

# =========================
# Konfigurasi Halaman
# =========================

st.set_page_config(
    page_title="Klasifikasi Slingbag dan Totebag",
    page_icon="👜",
    layout="centered"
)

st.title(
    "Klasifikasi Slingbag dan Totebag"
)

st.write(
    "Upload gambar tas untuk melakukan prediksi menggunakan model MobileNetV2."
)

# =========================
# Upload File
# =========================

uploaded_file = st.file_uploader(
    "Upload gambar",
    type=["jpg", "jpeg", "png"]
)

# =========================
# Prediksi
# =========================

if uploaded_file is not None:

    img = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        img,
        caption="Gambar yang diupload",
        use_container_width=True
    )

    # Sama persis dengan notebook
    IMG_SIZE = (256, 256)

    img_resized = img.resize(
        IMG_SIZE
    )

    img_array = np.array(
        img_resized
    )

    img_batch = np.expand_dims(
        img_array,
        axis=0
    )

    img_batch = (
        tf.keras.applications
        .mobilenet_v2
        .preprocess_input(img_batch)
    )

    prediction = model.predict(
        img_batch,
        verbose=0
    )

    score = prediction[0][0]

    st.write(
        f"Raw Prediction: {score:.6f}"
    )

    if score < 0.5:

        label = "Slingbag"

        confidence = (
            1 - score
        ) * 100

    else:

        label = "Totebag"

        confidence = (
            score
        ) * 100

    st.success(
        f"Prediksi: {label}"
    )

    st.write(
        f"Confidence: {confidence:.2f}%"
    )