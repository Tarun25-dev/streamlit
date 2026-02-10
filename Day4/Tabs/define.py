# Tabs - Tabs let you split the content into multiple sections on the same page and users can switch between them without reloading anything.
# Think of browser tabs, but inside your app.

# Basic Example:
import streamlit as st
tab1,tab2=st.tabs(["Home","Profile"])
with tab1:
    st.header("🏡 Home")
    st.write("Welcome to Home Tab")
with tab2:
    st.header("👨‍🏫 Profile")
    st.write("User details here")