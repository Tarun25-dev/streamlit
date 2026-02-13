import streamlit as st
tab1,tab2,tab3=st.tabs(["overview","Data","settings"])
with tab1:
    st.header("Overview")
    st.write("Overview section")
with tab2:
    st.header("Data")
    st.write("Data section")
with tab3:
    st.header("Settings")
    st.write("Settings is here.")