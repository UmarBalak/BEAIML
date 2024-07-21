import streamlit as st
import os
import json

SUBJECT_DIR = 'practicals'

@st.cache_data
def read_code(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return ""
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        return ""

def get_subjects(subject_dir):
    """List all subjects from the specified directory."""
    try:
        return [d for d in os.listdir(subject_dir) if os.path.isdir(os.path.join(subject_dir, d))]
    except FileNotFoundError:
        st.error(f"Directory not found: {subject_dir}")
        return []
    except Exception as e:
        st.error(f"An error occurred while listing subjects: {e}")
        return []

def read_subject_info(subject_name):
    """Read subject information from the info.json file."""
    info_file = os.path.join(SUBJECT_DIR, subject_name, 'info.json')
    if os.path.exists(info_file):
        try:
            with open(info_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            st.error(f"Error decoding JSON from file: {info_file}")
            return None
        except Exception as e:
            st.error(f"An error occurred while reading the JSON file: {e}")
            return None
    else:
        st.warning(f"No info.json file found for subject: {subject_name}")
        return None

def list_files(directory, extension='.py'):
    """List all files in a directory with a specific extension."""
    return sorted([f for f in os.listdir(directory) if f.endswith(extension)], key=lambda x: (x != 'main.py', x))

def display_practical_code(practical_dir, practical_info):
    """Display code files for a practical."""
    files_sorted = list_files(practical_dir)

    # st.subheader("Aim")
    st.markdown("""
    <style>
    .subheader {
        color: #00a67e; 
        font-size: 24px;
        margin-top: 0;
        margin-bottom: 0; 
        padding: 0;
    }
    .aim-content {
        margin-top: 0;
        padding: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h2 class="subheader">Aim</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="aim-content">{practical_info.get("aim", "No aim has been provided for this practical yet. We will update it soon.")}</div>', unsafe_allow_html=True)

    st.markdown("---")  

    if files_sorted:
        files_found = False
        for file in files_sorted:
            file_path = os.path.join(practical_dir, file)
            if os.path.isfile(file_path):
                code = read_code(file_path)
                st.markdown(
                    f"""
                    <div style="padding: 3px; padding-left: 15px; border-radius: 7px 7px 7px 7px; background-color: #2f2f2f;">
                        <span style="color: #A9A9A9;">{file}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.code(code, language='python', line_numbers=True)
                st.download_button(label=f"Download", data=code, file_name=file, mime="text/x-python")
                st.markdown("---")
                files_found = True

        if not files_found:
            st.warning("Currently, no code files are available for this practical. We are working on updating this soon.")
    else:
        st.warning("Currently, no code files are available for this practical. We are working on updating this soon.")

    st.markdown("""
    <style>
    .subheader {
        color: #00a67e; 
        font-size: 24px;
        margin-top: 0;
        margin-bottom: 0; 
        padding: 0;
    }
    .aim-content {
        margin-top: 0;
        padding: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<h2 class="subheader">Conclusion</h2>', unsafe_allow_html=True)
    st.markdown(f'<div class="aim-content">{practical_info.get("con", "No conclusion has been provided for this practical yet. We will update it soon.")}</div>', unsafe_allow_html=True)
