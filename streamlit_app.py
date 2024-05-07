from st_pages import (
    Page,
    show_pages,
)
import streamlit as st

st.set_page_config(
    page_title = 'Codei',
    page_icon = ':snake:',
    )

show_pages(
    [
        Page('streamlit_app.py', 'All we need is Python', '🐍'),
        Page('pages/about.py', 'About', ':books:'),
    ]
)

st.title('🐍 All we need is Python')
