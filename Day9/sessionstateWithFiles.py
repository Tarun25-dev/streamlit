import streamlit as st 
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

file = st.file_uploader("Upload file")

if file:
    st.session_state.uploaded_file = file

if st.session_state.uploaded_file:
    st.image(st.session_state.uploaded_file,caption="saved in session")
    
# Overview:
# focused on file and image uploads using st.file_uploader(), including type restrictions, multiple uploads, and form integration to make inputs required. We also learned how to process uploaded files (images, PDFs, DOCX) and use session state to persist them across pages for ML or dashboard applications.