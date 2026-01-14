import streamlit as st
import numpy as np
import joblib

# Load model dan fitur
model = joblib.load("house_price_model.pkl")
features = joblib.load("feature_columns.pkl")

st.set_page_config(
    page_title="House Price Prediction",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Masukkan data rumah untuk memprediksi harga")

# Input user
gr_liv_area = st.number_input("Luas Bangunan (sqft)", min_value=0)
lot_area = st.number_input("Luas Tanah (sqft)", min_value=0)
total_bsmt = st.number_input("Luas Basement (sqft)", min_value=0)
bedroom = st.number_input("Jumlah Kamar Tidur", min_value=0)
bathroom = st.number_input("Jumlah Kamar Mandi", min_value=0)
total_room = st.number_input("Total Ruangan", min_value=0)
quality = st.slider("Kualitas Rumah (1–10)", 1, 10, 5)

# Tombol prediksi
if st.button("Prediksi Harga"):
    input_data = np.array([[
        gr_liv_area,
        lot_area,
        total_bsmt,
        bedroom,
        bathroom,
        total_room,
        quality
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Perkiraan Harga Rumah: ${prediction:,.2f}")
