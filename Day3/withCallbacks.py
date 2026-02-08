import streamlit as st
def submit():
    st.session_state.submitted = True

st.button("submit",on_click=submit) # "submit" is a button name, on_click is an event in streamlit and submit which is a function to happen when click. 

# What means .submitted:
# Its not a built in, its just a custom flag (variable), we create inside st.session_state
# we can take any name

# What do we even need .submitted?
# beacuse,
# streamlit reruns the app every click
# we need a way to remember that an action already happened.
# .submitted is memory flag.

