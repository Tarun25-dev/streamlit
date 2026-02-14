import streamlit as st
files = st.file_uploader("Upload file",type=["pdf","docx","csv","xlsx"],accept_multiple_files=True)
if files:
    st.toast("file uploaded",duration=4)