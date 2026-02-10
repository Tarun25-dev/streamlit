# Sidebar is the laft panel used for navigation, filters, settings, user inputs.
# Everything inside the sidebar is written using st.sidebar().
import streamlit as st
st.sidebar.title("MENU")
st.sidebar.write("Choose an option")
option = st.sidebar.selectbox("Select page",["Home","Dashboard","About"])
st.write("Selected page is ",option)

# It is a built in widget and it provides hide and show option also