# Container :
# A conatiner is used to group multiple elements together and control where and when they appears on the page.
# Think of it like a box or section in your layout

# Basic example:

import streamlit as st
with st.container():
    st.header("Profile")
    st.write("Name: Thraun")
    st.write("Role: Student")

# Everything inside appears together in one block.