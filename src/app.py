import streamlit as st
from src.agent import investigate_vpn_incident

st.set_page_config(page_title="NVIDIA OpsGuard AI", page_icon="🛡️", layout="wide")
st.title("NVIDIA OpsGuard AI")
st.caption("Governed Agentic AI for Enterprise IT Operations")

st.subheader("Synthetic Incident")
st.write("Employee cannot connect to the corporate VPN after returning from travel.")

if st.button("Investigate incident"):
    result = investigate_vpn_incident()
    st.subheader("Probable root cause")
    st.success(result["probable_cause"])
    st.subheader("Recommended remediation")
    st.write(result["recommendation"])
    st.subheader("Policy decision")
    st.json(result["policy_decision"])
    st.subheader("Execution result")
    st.json(result["execution"])
    st.subheader("Evidence")
    st.json(result["evidence"])
