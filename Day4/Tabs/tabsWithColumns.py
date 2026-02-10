import streamlit as st
tab1,tab2=st.tabs(["Overview","Details"])
with tab1:
    col1,col2=st.columns(2)
    col1.metric("Sales","10000")
    col2.metric("Profit","1500")
with tab2:
    st.dataframe({
        "Year":[2025,2026],
         "Revenue":[400,500]         
        })
    
# Tabs inside sidebar is not recommended.
