"""
Session state:
>> Session state is used to remember data across reruns of a streamlit app.

Why do we need it?
>> Every time the user clicks, types, selects, uploads the entire scripts runs again from stop to bottom.
So normally,
> variables reset
> values are lost
> counters go back to zero
> st.session_state solves this problem

Real-life example:
> Imagine a form:
> Users enters name
> clicks submit
> page reruns
> name disappears with session_state remembered


"""
# initializing session_state: you must initialize before using it.

import streamlit as st
if "count" not in st.session_state:
    st.session_state.count=0
# “If count doesn’t exist, create it and set to 0”

# Update session state
if st.button("increment"): # means if button name called increment exits it returns true
    st.session_state.count +=1
    st.write("Count:",st.session_state.count)

