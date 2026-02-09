# Multi-Column Layout Example:

# 1. Basic multi column layout:
import streamlit as st
# # initialize columns
col1, col2 = st.columns(2) # must equal no.of columns mention in both ends.
# # this divides page into two parts 

col1.write("THARUN")
col2.write("KUMAR")

# 2. Unequal column widths:

col3,col4,col5=st.columns([1,2,1]) # here first and third column each has half width compared to second column width.
col3.button("PLAY")
col4.button("PAUSE")
col5.button("REPLAY")

# 3. Adding different elements in columns:
col6, col7 = st.columns(2)
with col6: # with is a keyword used to add multiple elements in a column
    st.title("RGM")
    st.write("Rajiv Gandhi Memorial")
    st.button("Visit Official Page",key="first") # why key? beacuse not button label as same as another buttton label if it is same we must differentiate with key.
with col7:
    st.title("SREC")
    st.write("Santhiram Engineering College")
    st.button("Visit Official Page",key="sec")
    
# 4. columns with images
col8,col9 = st.columns(2)
with col8:
    st.image("./img1.jpg",caption="Sample Img")
with col9:
    st.image("./img2.jpg",caption="Sample Img")

# we also used for charts also 

# 5. Nested columns:
col10,col11 = st.columns(2)
with col10:
    con1,con2 = st.columns(2)
    con1.write("NESTED")
    con2.write("COLUMNS")
with col11:
    con3,con4=st.columns(2)
    con3.write("PYTHON")
    con4.write("WEBSITE")