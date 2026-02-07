import streamlit as st
course=st.selectbox("Choose one",["python","java","c++"])
st.write(course)

gender = st.selectbox("Select",["select One","Male","Female"])
if gender == "select One":
    st.warning("Please select gender")
else:
    st.success(f"you selected: {gender}")