# Used when a task takes time.
import streamlit as st
import time
progress = st.progress(0) # creates a progress bar starting at 0%
# It returns a progress bar object and stores it in variable progress.
for i in range(100): # for loop runs 100 times from 0 to 99.
    time.sleep(0.02) # Pauses the program for 0.02 seconds (20 milliseconds). why this beacuse we need to see that progress bar move slowly not at a time thats why we gave delay.
    progress.progress(i+1)
    

# i starts from 0

# But progress bar should start from 1

# So:

# First loop → progress.progress(1)

# Last loop → progress.progress(100)

# Finally progress bar reaches 100%.



# Real Use:

# Model training

# File upload

# Data processing