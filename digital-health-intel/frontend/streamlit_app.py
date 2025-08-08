import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Digital Health Intel", layout="wide")

st.title("🏥 Digital Health Intel Dashboard")
st.write("Welcome to your digital health intelligence platform!")

# 📊 Data Insights Section
st.subheader("📊 Data Insights")

# List all CSV files in data/raw
data_dir = "data/raw"
csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

if csv_files:
    selected_file = st.selectbox("Select a dataset to view", csv_files)
    file_path = os.path.join(data_dir, selected_file)

    df = pd.read_csv(file_path)
    st.write(f"### Preview of `{selected_file}`")
    st.dataframe(df)

    st.write("### Summary Statistics")
    st.write(df.describe())

    if df.select_dtypes(include=["number"]).shape[1] > 1:
        st.line_chart(df.select_dtypes(include=["number"]))
else:
    st.warning("No CSV files found in `data/raw/`. Please upload datasets.")

# 🤖 AI Predictions Section
st.subheader("🤖 AI Predictions")
if st.button("Go to Predictions Page"):
    st.switch_page("pages/02_AI_Predictions.py")

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.info("Use the sidebar to explore the dashboard and AI predictions.")
