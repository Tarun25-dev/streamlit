import streamlit as st
data = {
    "Names":["a","b","c","d"],
    "Age":[10,20,30,40]
}
st.dataframe(data)