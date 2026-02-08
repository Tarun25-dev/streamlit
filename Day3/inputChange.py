# on_change : on_change is an event when ever the input changes then it triggers like first input you entered wrong and you cleard and type another time then it activates, more than one changes triggered.
# key : Key is a uniquely identifies a widget and connects it to st.session_state

# Why key exists?

# Rerun top → bottom
# Widgets need a stable identity
# Without identity → Streamlit gets confused

# key = ID card for widget

# Real-life analogy

# Person name → might duplicate
# Aadhaar number → unique = key

import streamlit as st
def name_changes():
    st.write("Name Updated")
st.text_input("Enter name ",key="name",on_change=name_changes)

