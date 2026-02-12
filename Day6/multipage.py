# Two ways to create a multi page app 
# 1. using st.session_state
import streamlit as st
if "page" not in st.session_state:
    st.session_state.page = "Home" # we are setting home page as default page when open the app.
page = st.sidebar.radio("Go to",["home","profile","settings"])
st.session_state.page=page

if st.session_state.page == "home":
    st.title("Home Page")
elif st.session_state.page == "profile":
    st.title("Profile Page")
elif st.session_state.page == "settings":
    st.title("Settings Page")
    
# Simple

# Uses only session_state

# No extra folder structure needed