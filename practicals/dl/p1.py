import streamlit as st
import os

st.title("BE AIML Practicals Repository")

SUBJECT_DIR = 'practicals'
subjects = [d for d in os.listdir(SUBJECT_DIR) if os.path.isdir(os.path.join(SUBJECT_DIR, d))]

selected_subject = st.sidebar.selectbox("Select Subject", subjects)

st.header(f"Subject: {selected_subject.upper()}")
st.write("Select a practical to view its code.")