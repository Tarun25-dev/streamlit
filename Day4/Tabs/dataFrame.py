# DataFrame - DataFrame is used to display tabular data in a clean and interactive table.
# most commonly it works with python library pandas.
# Basic Example:

import streamlit as st
import pandas as pd
data = {
    "Name":["Tharun","Kumar","Kodiganti"],
    "Score":[90,95,99]
}
df = pd.DataFrame(data) # converting to dataframe
st.dataframe(df)
