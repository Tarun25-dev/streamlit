import streamlit as st
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age",0,100,1)
    submitted = st.form_submit_button("Submit") #is used to submit all the inputs together at once.

if submitted:
    st.write("Name: ",name)
    st.write("Age: ",age)