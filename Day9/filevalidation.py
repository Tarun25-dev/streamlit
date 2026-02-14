import streamlit as st
# 1mb = 1024 kb
# validation is file must be less than 2mb
file = st.file_uploader("Upload file")
if file:
    if file.size > 2*1024*1024: # 2mb (must write in kbs and format  should be kb*kb)
        st.error("File too large! Max 2MB")
        
        
# check file if conatins extra redundents or unsupported format 
img = st.file_uploader("Upload image")
if img:
    if img.type not in ["image/png","image/jpg"]:
       st.error("Unsupported file")
    else:
        st.success("uploaded")
        
# we must write image type in mime beacuse it returns that type only for images we use image/file extension name 
# if we want to check for documents like pdf or doc we use application/pdf like that.