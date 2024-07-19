import streamlit as st
import os

def read_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

st.title("BE AIML Practicals Repository")

SUBJECT_DIR = 'practicals'
subjects = [d for d in os.listdir(SUBJECT_DIR) if os.path.isdir(os.path.join(SUBJECT_DIR, d))]

selected_subject = st.sidebar.selectbox("Select Subject", subjects)

st.header(f"Subject: {selected_subject.upper()}")

practicals = [f for f in os.listdir(os.path.join(SUBJECT_DIR, selected_subject)) if f.endswith('.py')]

for practical in practicals:
    practical_path = os.path.join(SUBJECT_DIR, selected_subject, practical)
    code = read_code(practical_path)

    st.subheader(f"{practical.replace('.py', '').replace('_', ' ').title()}")
    st.code(code, language='python')
    # st.button(f"Copy", on_click=lambda code=code: st.code(code, language='python'))

