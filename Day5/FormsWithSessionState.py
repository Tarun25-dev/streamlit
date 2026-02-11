import streamlit as st
DBname = "tharunkumar"
DBpass = "Tharun@123456789"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

with st.form("Login Form"):
    name = st.text_input("Name",placeholder="Enter name").lower().replace(" ","") # REMOVING ALL Spaces in name and also converted into lower case thats the format only i  stored credentials in database (assume)
    password = st.text_input("Password",placeholder="Enter your password",type="password")
    submitted = st.form_submit_button("Login")
    
if submitted:
    if not name or not password:
        st.warning("Must Enter all details")
    elif DBname == name and DBpass == password:
        st.session_state.logged_in = True
    else:
        st.warning("Enter valid details!")

if st.session_state.logged_in:
    st.success("Welcome to MyApp")
    
    
# Overview:
# st.form() groups multiple inputs and prevents immediate reruns, allowing controlled submission logic similar to traditional web forms.
    
            