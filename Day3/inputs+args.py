import streamlit as st

# Initialize state FIRST
if "role" not in st.session_state:
    st.session_state.role = None

def set_role(role):
    st.session_state.role = role

st.button("Admin", on_click=set_role, args=("Admin",))
st.button("User", on_click=set_role, args=("User",))

st.write("Role:", st.session_state.role)
