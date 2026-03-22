import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

st.title("House Price Prediction App")
st.write("Predict house price based on **area (sq.ft)** using a Linear Regression model.")

# Input box
area = st.number_input("Enter area (in sq.ft):", min_value=500, max_value=20000, step=100)

# Prediction button
if st.button("Predict Price"):
    # Reshape and predict
    input_data = np.array([[area]])
    predicted_price = model.predict(input_data)[0][0]
    st.success(f"Predicted House Price: ₹{predicted_price:,.2f}")

# Optional: Add model info
st.markdown("---")
st.caption("Model trained using Linear Regression on area vs price data.")
