# we can allow only images using type keyword 
import streamlit as st
img_file = st.file_uploader("Image upload",type=["png","jpg","jpeg"])
if img_file:
    st.image(img_file,caption="uploaded image",width=250) # this line shows that images which one you uploaded
    # image resize automatically to fit the width of the column or container where it is displayed.