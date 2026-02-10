import streamlit as st
st.metric(label="Accuracy",
          value="92%",
          delta="+1.5%",
          help="Model Accuracy compared to last version")
# help is used to describe the delta 
# here according to the code as compared to last version the accuracy is improved by +1.5%.
# help looks like in a question mark thing when we hover it then shows the help info.