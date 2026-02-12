import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {background-color: lightyellow; font-family: Arial;}
        h1 {color: green;}
        p {color: blue; font-size: 18px;}
        button {padding: 10px; font-size:16px;}
    </style>
</head>
<body>
    <h1>Full HTML, CSS & JS in Streamlit</h1>
    <p>This paragraph is styled with CSS.</p>
    <button onclick="showMessage()">Click Me</button>
    <p id="demo"></p>

    <script>
        function showMessage() {
            document.getElementById('demo').innerText = 'Button Clicked!';
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=300)
