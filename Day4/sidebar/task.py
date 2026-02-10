import streamlit as st
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to",["HOME","STATS","CONTACT"])
    
def Home():
    st.write("Home page Function")

def Stats():
    st.write("stats page Function")
    
def Contact():
    st.write("contact page Function")
    
if page == "HOME":
    st.header("Home Page")
    st.title("Welcome to the Stream")  
    Home()
    
if page == "STATS":
    st.header("Stats Page")
    st.title("Welcome to the Stats")  
    Stats()

if page == "CONTACT":
    st.header("Contacts Page")
    st.title("Welcome to the Contacts")  
    Contact()

