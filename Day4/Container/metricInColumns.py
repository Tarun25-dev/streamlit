import streamlit as st
col1,col2,col3=st.columns(3)
col1.metric("Users","10000","+50")
col2.metric("Orders","1050","+23")
col3.metric("Errors","10","-2")