from pathlib import Path
import streamlit as st
from pathlib import Path
import yaml

file_name = Path(__file__).name
file_parent_dir = Path(__file__)

file_name_title = file_name[4:-3].capitalize()
file_dir_title = file_parent_dir.parts[-2].capitalize()

st.set_page_config(
    page_title = f'{file_name_title} - {file_dir_title}',
    )

with open(f'pages/python/cheatsheet/003_built_in_functions.md', 'r') as f:
    st.markdown(f.read())
