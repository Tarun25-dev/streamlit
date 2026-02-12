import streamlit as st
if "role" not in st.session_state:
    st.session_state.role = None

# role selection
st.sidebar.title("Select role")
if st.sidebar.button("Admin"):
    st.session_state.role = "Admin"
elif st.sidebar.button("User"):
    st.session_state.role = "User"

# page navigation
pages = ["Home","Profile","Settings"]
page = st.sidebar.radio("Go to",pages)

if st.session_state.role == "Admin":
    st.write("Welcome Admin..!")
elif st.session_state.role == "User":
    st.write("Welcome User..!")
    
st.write(f"current page {page}")

# Overview:
#     Multi-page apps in Streamlit allow developers to split content into multiple screens. Navigation can be done via st.sidebar.radio or Streamlit’s built-in multipage feature. Session state is used to remember which page or role the user is on.