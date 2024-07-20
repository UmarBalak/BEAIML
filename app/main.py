import streamlit as st
import os

# Cache the function to read the content of a file
@st.cache_data
def read_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_subjects(subject_dir):
    return [d for d in os.listdir(subject_dir) if os.path.isdir(os.path.join(subject_dir, d))]

def get_practicals(practicals_dir):
    practicals = {}
    for folder in os.listdir(practicals_dir):
        folder_path = os.path.join(practicals_dir, folder)
        if os.path.isdir(folder_path):
            files = sorted([f for f in os.listdir(folder_path) if f.endswith('.py')])
            practicals[folder] = files
    return practicals


# Main function to build the Streamlit app
def main():
    st.title("BE AIML Practicals Repository")

    SUBJECT_DIR = 'practicals'

    # Fetch the list of subjects
    subjects = get_subjects(SUBJECT_DIR)
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #151515;
        }
    </style>
    """, unsafe_allow_html=True)
    st.sidebar.header("Code Repository")
    
    if subjects:
        # Select subject
        selected_subject = st.sidebar.selectbox("Select Subject", subjects)
        
        # Display subject header
        st.header(f"Subject: {selected_subject.upper()}")
        
        # Get practicals for the selected subject
        practicals_dir = os.path.join(SUBJECT_DIR, selected_subject)
        practicals = get_practicals(practicals_dir)

        if practicals:
            # Select practical
            selected_practical = st.sidebar.radio("Select Practical", list(practicals.keys()))

            # Get files for the selected practical
            files = practicals[selected_practical]
            files.sort(key=lambda x: (x != 'main.py', x))  # Ensure 'main.py' is at the top

            for file in files:
                file_path = os.path.join(practicals_dir, selected_practical, file)
                code = read_code(file_path)
                # st.subheader(f"{file.replace('.py', '').replace('_', ' ').title()}")
                st.markdown(f" `{file}` ")
                st.code(code, language='python', line_numbers=True)
                st.markdown("---")
        else:
            st.write("No practicals available for the selected subject.")
    else:
        st.write("No subjects available in the repository.")

if __name__ == "__main__":
    main()

