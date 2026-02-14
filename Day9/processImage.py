# How to process uploaded images for ML
# we must use python python imaging library
# tensorflow is free library used for building,training, and deep learning models across various platforms.
import streamlit as st
from PIL import Image
import tensorflow as tf
uploaded_file = st.file_uploader("Upload file",type=["jpg","jpeg","png"])
if uploaded_file:
    image =Image.open(uploaded_file)
    st.image(image,caption=uploaded_file.name)
    
    # preprocess for model
    img = image.resize((224,224)) # height and width compressed as our desired size
    img_arrays = tf.keras.utils.img_to_array(img)
    img_arrays = tf.expand_dims(img_arrays,0)
    st.write("Image ready for ML model")