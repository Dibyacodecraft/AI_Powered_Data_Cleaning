import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Power Data Cleaning")
st.header("Data Source Selection")

option = st.selectbox("Select Data Source", ["CSV", "Database Query", "API Data"])

if option == "CSV":
    uploaded_file = st.file_uploader("Upload CSV")
    if st.button("Clean Data") and uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
        try:
            response = requests.post(f"{FASTAPI_URL}/clean_data", files=files, timeout=60)
            response.raise_for_status()
        except requests.RequestException as exc:
            st.error(f"Failed to process data: {exc}")
        else:
            st.write(response.json())
