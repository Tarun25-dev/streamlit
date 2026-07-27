import streamlit as st

user_input = st.text_input("input",placeholder="type a word")

if st.button("Check"):
    reverse = "" 
    for ch in user_input:
        reverse = ch + reverse
    if reverse == user_input:
        st.success("Polinrome")
    else:
        st.error("Not a Polindrome")



    