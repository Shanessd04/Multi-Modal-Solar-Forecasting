import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# ---- Set Absolute Path to Model ----
model_path = "/Users/shanes/sep/solar_forecasting_model.h5"  # Explicit full path

# ---- Load Model Safely ----
model = None  # Initialize model variable
if st.button("🔄 Load Model"):
    try:
        model = load_model(model_path)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"🔴 Error loading model: {e}")

# ---- Function to Preprocess Image ----
def preprocess_image(img):
    img = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64))
    img = img / 255.0  
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    return img

# ---- Image Upload ----
st.title("🖼️ Image-Based Solar Energy Prediction")
uploaded_image = st.file_uploader("Upload a satellite image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image")

    if model is not None:
        processed_img = preprocess_image(uploaded_image)
        prediction = model.predict(processed_img)[0][0]
        st.success(f" Solar Potential from Image: **{prediction:.2f} kWh/m²**")
    else:
        st.error("⚠️ Model not loaded. Click 'Load Model' first.")

# ---- Navigation back to main page ----
if st.button("🔙 Back to Home"):
    st.switch_page("../main.py")
