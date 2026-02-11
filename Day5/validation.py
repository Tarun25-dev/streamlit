import streamlit as st
with st.form("CheckIn Form"):
    name = st.text_input("Name")
    loc = st.text_input("Location")
    submitted = st.form_submit_button("Submit")
    
if submitted:
    if name == "" or loc =="":
        st.error("All fields are required!")
    else:
        st.success("Form submitted successfully")
        st.write("Name:",name)
        st.write("Location:",loc)