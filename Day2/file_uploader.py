import streamlit as st
resume = st.file_uploader("Uplaod file") # limit 200mb

# if we want file name also then 
if resume:
    st.write("File name:",resume.name)

# if you want only desired type then use type property in file_uploader()
photo = st.file_uploader("Upload an image",type=["jpg","png","jpeg"])
