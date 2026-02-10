# Empty container - st.empty():
# Used when content changes dynamically.
import streamlit as st
status = st.empty()
status.info("waiting...")
# later
status.success("Completed!")

# Think of st.empty() as a replaceable container.