# Remembering text input
import streamlit as st
if "name" not in st.session_state:
    st.session_state.name=""
st.session_state.name=st.text_input("Enter your name:")
st.write("Hello",st.session_state.name)