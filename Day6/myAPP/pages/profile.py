import streamlit as st
st.set_page_config(page_title="Profile Page",page_icon="👨‍🏫")
st.title("PROFILE PAGE")
st.write("This is the profile page of the multi-page app")
if st.button("click"):
    st.success("Button clicked")