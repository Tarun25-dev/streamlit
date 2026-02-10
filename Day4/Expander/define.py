# Expander:
#     An expander lets you hide and show content when the user clicks on it.
#     Think of it like a dropdown section for extra details.
#     We can do this by using st.expander()
import streamlit as st
with st.expander("Click to see more details"):
    st.write("This content is hidden")
    st.write("More information here")