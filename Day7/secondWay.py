# using st.cpmponents.v1.html()
# This is streamlit offical component for embedding HTML/CSS/JS.
# You can render bigger HTML blocks, include CSS styling, and even JS snippets

import streamlit as st
import  streamlit.components.v1 as components

html_code = """
<div style='background-color:lightyellow; padding:20px; border-radius:10px;'>
  <h2 style='color:green;'>Custom HTML Block</h2>
  <p>This is HTML + CSS inside Streamlit.</p>
</div>
"""
components.html(html_code,height=200) # emdedding html, height represents we need to give how much space(height) they max taken. 

# height defines the space for the block.

# Can include HTML, CSS, and limited JS.

# Good for embedding custom widgets or interactive visuals.
