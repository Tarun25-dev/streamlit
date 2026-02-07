import streamlit as st
age=st.number_input("Enter Age",min_value=0,max_value=10)
st.write(age)
# output: int

age=st.number_input("Enter Age")
st.write(age)
# output: float
# it takes only inputs from 0 to 10 only remainly doesnt accept as input.
# also this widget has feature to increment the value or descriment the value using symbols of "+" "-" upto maxvalue
# if you dont use min and max then it accepts anynumber but it takes as float.