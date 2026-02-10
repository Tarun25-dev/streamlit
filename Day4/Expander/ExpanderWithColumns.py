import streamlit as st
col1,col2=st.columns(2)
with col1:
    with st.expander("User info"):
        username = st.text_input("Name:")
        userAge = st.text_input("Age:")
with col2:
    with st.expander("Preferences"):
        userTheme = st.radio("Themes:",["Light","Dark"])

st.write("UserName:",username)
st.write("Age:",userAge)
st.write("Selected Theme:",userTheme)