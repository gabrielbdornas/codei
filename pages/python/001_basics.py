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

with open(f'pages/python/cheatsheet/001_basics.md', 'r') as f:
    st.markdown(f.read())

st.header('Exercises')

with open('pages/python/cheatsheet/quiz.yaml', 'r') as file:
    yaml_content = file.read()
yaml_data = yaml.safe_load(yaml_content)
current_file = Path(__file__)
questions = yaml_data['questions'][current_file.stem]

for question in questions:
    for number, info in question.items():

        with st.form(f'{number}° Question:'):
            question = st.markdown(info['question'])
            answer = st.radio('A opção correta é:',
                              options=info['options'],
                              index=None)
            submitted = st.form_submit_button('Enviar')
            if submitted:
                if answer == info['answer']:
                    st.write('Teste')

                # import ipdb; ipdb.set_trace(context=10)
