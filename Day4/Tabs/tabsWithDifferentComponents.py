import streamlit as st
tab1,tab2,tab3=st.tabs(["Stats","Charts","Settings"])
with tab1:
    st.metric("Users","100")
with tab2:
    st.line_chart([10,20,30])
with tab3:
    st.checkbox("Enable notifications")