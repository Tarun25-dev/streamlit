import streamlit as st
from PIL import Image
import random

st.title("Image Classifier")
uploaded_file = st.file_uploader("upload image",type=["jpg","png","jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image,caption="image",width=150)
if st.button("Predict"):
    prediction = random.choice(["Apple","Banana","Orange"])
    st.success(f"prediction: {prediction}")