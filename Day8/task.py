import streamlit as st
import time

st.title("Admin Dashboard")

col1, col2 = st.columns(2)

col1.metric("Users", 1500, "+10%")
col2.metric("Revenue", "$10,000", "+3%")

if st.button("Process Data"):
    with st.spinner("Processing..."):
        time.sleep(2)
    st.success("Data processed!")