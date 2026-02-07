import streamlit as st
skills = st.multiselect("Select one or more:",["Python","Java","Sql","ML"])

# also you can add must skills default selected using default property

jobReq = st.multiselect("select",["python","java","english"],default=["english"])
# must keep default values also in main list other wise you get error and also if you dont want default remove option also available
# if you dont want to remove then we keep condition like this
if "english" not in jobReq:
    st.warning("English skill is mandatory!")