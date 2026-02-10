# | Feature   | `radio()`       | `selectbox()` |
# | --------- | --------------- | ------------- |
# | UI        | Visible buttons | Dropdown      |
# | Options   | Few options     | Many options  |
# | Best for  | Clear choice    | Save space    |
# | Selection | One only        | One only      |

# 3–6 options → radio()

# Many options → selectbox()
import streamlit as st
with st.sidebar:
    page = st.radio(
        "Navigation",
        ["Home", "Projects", "Contact"]
    )

# also we can choose how radio button orientation using horizontal keyword it accepts true or false
st.radio("Select Plan",["Free","Pro","Enterprise"],horizontal=True) # default value is False
