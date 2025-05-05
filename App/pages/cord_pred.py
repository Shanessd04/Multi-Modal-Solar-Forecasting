import streamlit as st
import folium
from streamlit_folium import st_folium
import numpy as np
import pandas as pd
import plotly.express as px

# ---- Streamlit App Title ----
st.set_page_config(layout="wide")
st.title("Solar Energy Potential Predictor")

# ---- Layout: Map (Left) | Prediction (Center) | Insights (Right) ----
col1, col2, col3 = st.columns([3, 1.5, 1.5])

with col1:
    st.write("### Interactive Map (Click to Select Location)")
    
    # ---- Folium Map for Clicks ----
    folium_map = folium.Map(location=[20, 78], zoom_start=5)
    clicked_location = st_folium(folium_map, height=500, width=700)

    # ---- Get Clicked Coordinates ----
    lat, lon = None, None
    if clicked_location and clicked_location["last_clicked"]:
        lat = clicked_location["last_clicked"]["lat"]
        lon = clicked_location["last_clicked"]["lng"]

solar_potential = None  # Initialize before use

with col2:
    st.write("### 📌 Selected Coordinates")
    if lat and lon:
        st.write(f"**Latitude:** `{lat}`")
        st.write(f"**Longitude:** `{lon}`")
        st.success("✔️ Click 'Predict Solar Potential' below to proceed.")
    else:
        st.warning("⚠️ Click on the map to select a location.")

    # ---- Prediction Button ----
    if lat and lon:
        if st.button("🔍 Predict Solar Potential"):
            solar_potential = np.round(np.random.uniform(3, 6), 2)  # Mock Prediction
            st.success(f"Predicted Solar Potential: **{solar_potential} kWh/m²**")

            # ---- ✅ Solar Panel Suitability Suggestions ----
            if solar_potential >= 4.5:
                st.success("✅ Highly suitable for solar panels!")
            else:
                st.error("❌ May not be ideal for solar panels.")

with col3:
    st.write("### 📊 Insights")
    
    if solar_potential is not None:  # Ensure the variable is defined
        # ---- 📈 Historical Solar Potential Trends ----
        years = list(range(2015, 2025))
        solar_trend = np.random.uniform(3, 6, len(years))  # Mock data

        df_trend = pd.DataFrame({"Year": years, "Solar Potential (kWh/m²)": solar_trend})
        fig_trend = px.line(df_trend, x="Year", y="Solar Potential (kWh/m²)", 
                            title="Historical Trends", markers=True)
        st.plotly_chart(fig_trend, use_container_width=True)

        # ---- 📊 Comparison with Nearby Locations ----
        locations = ["Selected Location", "Nearby 1", "Nearby 2", "Nearby 3"]
        potentials = [solar_potential] + list(np.random.uniform(3, 6, 3))  # Mock data

        df_comparison = pd.DataFrame({"Location": locations, "Solar Potential": potentials})
        fig_bar = px.bar(df_comparison, x="Location", y="Solar Potential",
                         title="Nearby Solar Potential",
                         color="Solar Potential", color_continuous_scale="YlOrRd")
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("⚠️ Click 'Predict Solar Potential' first to view insights.")

# ---- Add Some Styling ----
st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        font-size: 18px;
        font-weight: bold;
        background-color: #FFA500;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)