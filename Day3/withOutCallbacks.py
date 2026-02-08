import streamlit as st
if st.button("Submit"):
    st.session_state.submitted = True

# Works, but:
# Logic mixed with UI 
# Hard to scale

