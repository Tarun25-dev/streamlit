# Small popup message.
import streamlit as st
if st.button("save"):
    st.toast("successfully saved")

# properties of toast 
# 1. duration which defines how much time it appears on screen after that it disappears.and we give an integer as value in seconds.
if st.checkbox("enable notifications"):
    st.toast("enabled notifications",duration=4)

# real use of code like 
if "notifications_prev" not in st.session_state:
    st.session_state.notifications_prev = None
notifications = st.checkbox("Enable Notifications")

# this if statement doent run at first page load when ever user clicks check box then that returns value stored at last line of code and then it runs aauto and updates as per state 
if st.session_state.notifications_prev is not None: # it prevernts first page load and no notification when opening a page thats are actually none when ever the checkbox chaanged from none then this condition goes.
    if notifications != st.session_state.notifications_prev: # Check if Value Changed
        # Current value vs Previous value
        
        if notifications: # If checkbox is checked → show enabled toast.
            st.toast("Notifications Enabled",duration=3)
        else:
            st.toast("Notifications Disabled",duration=3)
# Update Previous State  
st.session_state.notifications_prev = notifications

# Very important line.
# After everything runs:
# We update the stored previous value.
# So next time user clicks:
# We can compare properly.
            
    