import streamlit as st
import requests

st.title("Enterprise Incident Intelligence Agent")

incident = st.text_area("Describe the incident")

if st.button("Analyze"):
    response = requests.post(
        "http://localhost:8000/analyze",
        headers={"x-api-key": "secret123"},
        json={"incident": incident},
    )
    st.json(response.json())
