import streamlit as st 
import datetime
with st.form("Form"):
    Fname = st.text_input("First Name")
    Lname = st.text_input("Last Name")
    age = st.number_input("Age",18) # starts from 18 and stop value is the max value in number_input as default and also step value default as one.
    defaultDoB = datetime.date.today()
    DoB = st.date_input("DoB",
                        min_value=datetime.date(1990,1,1),
                        max_value=datetime.date.today()
                        )
    gender=st.selectbox("Gender",["Male","Female","Others"])
    submitted = st.form_submit_button("Submit")
    
    # validation
    if submitted:
        if not Fname and not Lname:
            st.warning("Name is required")
        elif not defaultDoB:
            st.warning("Enter Correct DOB")
        else:
            st.success("Successfully Submitted")
