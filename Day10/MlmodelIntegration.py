import streamlit as st
from PIL import Image
import tensorflow as tf # used to load the trained models and also make predictions.
import numpy as np # converting img to array, mathematical operations and reshaping data

# load model
@st.cache_resource
# it is a decorator from streamlit it only loads the model one time, prevents reloading every time and makes the app faster.
def load_model():
    return tf.keras.models.load_model("model.h5") # this was replace with your model name 

model = load_model() # Now model can be used to predict images.

upload_img = st.file_uploader("upload image",type=["png","jpg","jpeg"])
if upload_img:
    image = Image.open(upload_img) # stored img in image variable
    st.image(image,caption="img",width=260)
 
 # resize image
img = image.resize((224,224)) # in pixels
# convert img to array
img_array = np.array(img)/225.0 
# why 225.0 beacuse pixel values ranges from 0 to 225
# by dividing with 225 which gives values in the range of 0 to 1 
# this is called normalization

img_array = np.expand_dims(img_array, axis=0)
# It adds 1 extra dimension at position 0.
# why beacuse,
# while we training a model it should like model.fit(X_train, y_train, batch_size=32)
# so the model expects the same dimension as input.
# (batch_size, height, width, channels)
# (224,224,3) to (1,224,224,3)

# what is batch = no.of images given to the model at a time.
# (32, 224, 224, 3)

# Means:

# 32 images

# Each image 224x224

# 3 color channels

# which is used for faster training, memory management and also model structure(Neural networks are built to accept data in batches.)
 
# RGB = Red, Green, Blue

# Every color image is made from these 3 colors.
# [R value, G value, B value] and each values ranges from 0 to 255
# Helps model detect color-based patterns