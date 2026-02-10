# Table - st.table():
# Table is used to display static tabular data in a simple non interactive table.
import streamlit as st

data = {
    "Name": ["Tharun", "Kumar", "Kodiganti"],
    "Score": [90, 95, 99]
}

st.table(data)

# When should you use st.table()?

# ✔ Small datasets
# ✔ Summary tables
# ✔ Read-only data
# ✔ Quick demos / learning

# Limitations

# ❌ Not editable
# ❌ No filters
# ❌ No pagination
# ❌ Not suitable for large datasets