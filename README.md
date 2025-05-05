# ☀️ Multi-Modal Solar Forecasting with Adaptive Attention Networks

A deep learning project to forecast solar energy potential using satellite imagery, weather data, and attention-based models.

---

## 🚀 Project Overview

This project predicts solar energy output by combining:
- Satellite images (GeoTIFF)
- Ground weather measurements
- Adaptive neural network models (CNNs, LSTMs, Vision Transformers)

Deployed using **Flask API** and **Streamlit UI**. Supports both **location-based** and **image-based** predictions.

---

## 📦 Tech Stack

- Python, TensorFlow, Keras, PyTorch
- OpenCV, GDAL, Rasterio (GeoTIFF handling)
- SHAP & LIME (Model Interpretability)
- Flask (API deployment)
- Streamlit (Interactive UI)
- Blender (3D Visualization)
- Docker (optional)

---

## 🧠 Model Architecture

- **Image Processing:** CNNs on satellite patches
- **Multi-modal Fusion:** Adaptive Attention
- **Time-Series Forecasting:** LSTMs
- **Explainability:** SHAP / LIME for model insights

---

## 🗺️ App Features

### 1. 📍 Location-based Prediction
- Enter latitude & longitude or select via map
- View predicted solar potential with insights

### 2. 🖼️ Image-based Prediction
- Upload satellite image patches
- Get spatial predictions using trained CNN

---

## 🌐 Live Demos (Optional)
- Streamlit: `https://your-streamlit-link`
- Flask API: `https://your-api-link`

---

## 🔧 Getting Started

### Clone this repo:
```bash
git clone https://github.com/yourusername/multi-modal-solar-forecasting.git
cd multi-modal-solar-forecasting
