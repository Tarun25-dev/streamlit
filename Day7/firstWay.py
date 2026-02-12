import streamlit as st

# You can write HTML directly inside Markdown.
# Works for text formatting, colors, fonts, images, and simple layouts.

st.markdown("<h1 style='color:blue;'>Hello HTML in Streamlit</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:20px;'>This is a paragraph with HTML.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line

# Limited to basic HTML and inline CSS.

# JavaScript usually won’t work here.

