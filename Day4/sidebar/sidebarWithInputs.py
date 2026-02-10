# Sidebar with inputs(filters)
import streamlit as st
st.sidebar.title("MENU",text_alignment="center")
st.sidebar.header("Filters")
age=st.sidebar.slider("Age",18,59,25) # range 18 - 59 slider is nothing but a selecter and used to select values visually using drag.
city=st.sidebar.selectbox("City",["Delhi","Mumbai","Banglore"])
st.write(f"Age:{age}, City:{city}")