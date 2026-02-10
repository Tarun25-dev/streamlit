# Default state of Expander is closed if we want that as opened then use expanded proprty and it takes True / False.
import streamlit as st
with st.expander("My Details",expanded=True):
    st.write("Name: Tharun Kumar")
    st.write("College: SREC")
    st.write("Location: Nandyal")