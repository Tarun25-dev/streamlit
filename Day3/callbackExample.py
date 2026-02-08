import streamlit as st
def increase():
    st.session_state.count += 1
if "count" not in st.session_state:
    st.session_state.count = 0
st.button("Add",on_click=increase)
st.write("Count: ",st.session_state.count)

# Button clicked

# increase() runs

# State updates

# App reruns

# Value persists