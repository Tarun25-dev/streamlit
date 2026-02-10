# Metric - st.metric() is used to display Key Numeric Values (KPIs) in a clean, dashboard style format.
# Think of it like a stats card you see in analytics dashboards.

# syntax = st.metric(label,value,delta) # delta refers to increase or decrease shows according to the value.
# Example:

import streamlit as st
st.metric(label="Sales",value="1050",delta="-400",delta_color="red") # default color is green
# also
st.metric("Sales","1000","+430")
# it aslo decides the arrow symbol based on delta sign 
# if sign is positive(+) then it shows up arraw(⬆)
# if sign is negative(-) then it shows up arraw(⬇)

# Important points

# value and delta can be string or number

# Delta color is automatic

# Not meant for long text