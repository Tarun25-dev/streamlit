import streamlit as st
placeholder=st.container()
if st.button("ShowData"): # when click it returns True and then it links to with placeholder.
    with placeholder:
        st.success("Data loaded successfully")