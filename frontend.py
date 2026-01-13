import streamlit as st
import requests
import os

st.title("Enterprise Incident Intelligence Agent")

tenant_id = st.text_input("Tenant ID", value="tenant-1")
incident = st.text_area("Describe the incident")

# Get API key from env or default to "secret123" if not set, matching backend default
api_key = os.getenv("SERVICE_API_KEY", "secret123")

if st.button("Analyze"):
    try:
        response = requests.post(
            "http://localhost:8000/analyze",
            headers={"x-api-key": api_key, "X-Tenant-ID": tenant_id},
            json={"incident": incident},
        )
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Error: Could not connect to backend. Is it running on http://localhost:8000?")
