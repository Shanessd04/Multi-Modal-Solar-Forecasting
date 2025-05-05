import streamlit as st

# ---- Page Configuration ----
st.set_page_config(page_title="Solar Energy Prediction", layout="wide")

st.image("/Users/shanes/sep/images/Solar.png")

# ---- Home Page Content ----
st.title("Multi-Modal Solar Energy Prediction")
st.markdown("""
### Problem Statement  
Accurate solar energy forecasting is essential for optimizing solar panel installations and energy grid planning.  
This project aims to improve solar energy potential prediction using **multi-modal approaches**:  
- **Location-Based Prediction** using geographical coordinates 🌍  
- **Image-Based Prediction** using satellite images 🖼️  

### Purpose of This Project  
✅ Help decision-makers optimize solar farm locations  
✅ Improve renewable energy forecasting with deep learning  
✅ Compare two different prediction approaches  

### Model Developed  
- **Location-Based Model** → Uses spatial interpolation (cKDTree) for predictions  
- **Image-Based Model** → A **CNN** trained on satellite images for solar energy estimation  
""")

# ---- Navigation Buttons ----
st.markdown("### Choose a Prediction Method:")
col1, col2 = st.columns(2)

with col1:
    if st.button("📍 Location-Based Prediction"):
        st.switch_page("/Users/shanes/sep/pages/cord_pred.py")

with col2:
    if st.button("🖼️ Image-Based Prediction"):
        st.switch_page("/Users/shanes/sep/pages/image_pred.py")