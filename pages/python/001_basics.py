import streamlit as st

with open(f'pages/python/cheatsheet/001_basic.md', 'r') as f:
    st.markdown(f.read())
