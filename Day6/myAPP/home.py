import streamlit as st
st.set_page_config(page_title="Home Page",page_icon="🏡")
st.title("HOME PAGE")
st.write("This is the home page of the multi-page app")
if st.button("click"):
    st.success("Button clicked")