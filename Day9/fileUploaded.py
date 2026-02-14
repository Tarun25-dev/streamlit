# st.file_uploaded - is used to take input files from users 
# | Parameter               | Description                                |
# | ----------------------- | ------------------------------------------ |
# | `label`                 | Label for uploader                         |
# | `type`                  | Allowed file types (e.g., `['png','jpg']`) |
# | `accept_multiple_files` | Allow multiple files upload                |
# | `key`                   | Session state key if needed                |

import streamlit as st
uploaded_file = st.file_uploader("Upload file")
if uploaded_file is not None:
    st.write("File name :",uploaded_file.name)