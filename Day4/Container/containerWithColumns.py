import streamlit as st
with st.container():
    col1,col2=st.columns(2)
    col1.metric("Users",100)
    col2.metric("Sales",1500)