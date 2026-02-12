# Using CSS in <style> tags inside st.markdown()
# You can customize Streamlit’s native widgets or app style using CSS.

import streamlit as st
st.markdown("""
            <style>
                h1{
                    color: red;
                }
                p{
                    font-size:18px;
                    color:blue;
                    cursor:pointer;
                }
                button{
                    padding:3px;
                    font-size:25px;
                    background-color:grey;
                    color:black;
                }
                button:hover{
                    background-color:red;
                    font-size:27px;
                }
            </style>
            """,unsafe_allow_html=True)
st.markdown("<h1>MY STREAMLIT APP</h1>",unsafe_allow_html=True)
st.markdown("<p>My name is Tharun Kumar</p>",unsafe_allow_html=True)
st.markdown("<button>Click</button>",unsafe_allow_html=True)