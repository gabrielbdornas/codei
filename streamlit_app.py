from st_pages import (
    add_page_title,
    Page,
    Section,
    show_pages,
)
import streamlit as st

# st.set_page_config(
#     page_title = 'Codei',
#     page_icon = ':snake:',
#     )

show_pages(
    [
        Page('streamlit_app.py', 'Home', '🏠'),
        Page('pages/about.py', 'About', ':books:'),
        Section('Python', '🐍'),
        Page('pages/python/001_basics.py'),
        Page('pages/python/002_functions.py'),
        Page('pages/python/003_built_in_functions.py'),
    ]
)

add_page_title()
