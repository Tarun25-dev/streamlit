import streamlit as st
with st.form("file upload form"):
    file = st.file_uploader("Upload Resume",type=["docx","pdf","doc","html"])
    button = st.form_submit_button("Submit",icon="✔")
if button:
    if file is None:
        st.error("Please upload file")
    else:
        st.success("file submitted")