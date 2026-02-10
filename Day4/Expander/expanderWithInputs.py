import streamlit as st
with st.expander("Filter"):
    age = st.slider("Age",18,80,1) # here slider(label,min value,max value,step)
    city = st.selectbox("City:",["Delhi","Chennai","Hyderabad"])

userAge = age
UserCity = city
st.write("Age:",userAge)
st.write("City:",UserCity)