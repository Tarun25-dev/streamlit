import streamlit as st
with st.sidebar:
    st.title("Settings")
    st.radio("Theme",["Dark","Light"])
    # radio() is used to slected only one option from the following list.
    notify = st.checkbox("Enable notifications")
    
if notify:
    st.success("Enabled",icon="🔔")