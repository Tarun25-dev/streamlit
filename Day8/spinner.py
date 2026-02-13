# Shows loading animation.
import streamlit as st
import time
with st.spinner("Loading..."):
    time.sleep(3) # 3 sec
st.success("Loaded successfully")