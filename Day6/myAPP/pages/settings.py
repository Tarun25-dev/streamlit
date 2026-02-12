import streamlit as st
st.set_page_config(page_title="Settings Page",page_icon="🎁")
st.title("SETTINGS PAGE")
st.write("This is the settings page of the multi-page app")
if st.button("click"):
    st.success("Button clicked")