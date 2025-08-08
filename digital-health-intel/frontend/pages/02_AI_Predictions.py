import streamlit as st
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("🤖 AI Predictions")
st.write("Upload a health data file to send it to the backend for predictions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df)

    if st.button("Send to Backend for Prediction"):
        try:
            # Convert DataFrame to JSON and send to FastAPI
            response = requests.post(API_URL, json={"data": df.to_dict(orient="records")})
            
            if response.status_code == 200:
                st.success("Prediction received from backend!")
                st.write(response.json())
            else:
                st.error(f"Backend error: {response.status_code}")
        except Exception as e:
            st.error(f"Request failed: {e}")
