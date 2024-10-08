import streamlit as st
import os
from functions import get_subjects, read_subject_info, list_files, read_code, display_practical_code, SUBJECT_DIR

def main():
    st.set_page_config(
        page_title="AIML Practical Hub",
        page_icon=":open_file_folder:",
        initial_sidebar_state="expanded",
    )
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;} /* Hides the main menu */
    footer {visibility: hidden;} /* Hides the footer */
    header {visibility: hidden;} /* Hides the header */
    .css-1d391kg {visibility: hidden;} /* Hides the status indicator */
    .css-1v3fvcr {visibility: hidden;} /* Hides the Streamlit watermark */
    .css-1v0mbdj {visibility: hidden;} /* Hides the overall container */
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: #171717;
            }
        </style>
        """, unsafe_allow_html=True)
    st.title("AIML Practical Hub")

    # Fetch the list of subjects
    subjects = get_subjects(SUBJECT_DIR)

    st.sidebar.markdown("""
    <style>
    .sidebar-header {
        color: #00a67e;
    }
    </style>
    """, unsafe_allow_html=True)
    st.sidebar.markdown('<h1 class="sidebar-header">Practical Menu</h1>', unsafe_allow_html=True)

    if subjects:
        selected_subject = st.sidebar.selectbox("Select Subject", subjects)
        st.sidebar.markdown("---")

        subject_info = read_subject_info(selected_subject)
        # st.write(f"**{selected_subject}**")
        if subject_info:
            practical_names = [p['name'] for p in subject_info.get("practicals", [])]
            if practical_names:
                selected_practical_name = st.sidebar.radio("Select Practical", practical_names)
                practical_info = next((p for p in subject_info['practicals'] if p['name'] == selected_practical_name), None)

                if practical_info:
                    practicals_dir = os.path.join(SUBJECT_DIR, selected_subject, selected_practical_name)

                    if os.path.isdir(practicals_dir):
                        display_practical_code(practicals_dir, practical_info)
                    else:
                        st.warning(f"Sorry, the practical '{selected_practical_name}' is not yet available. We will upload the details soon.")
                else:
                    st.warning("No details are available for the selected practical at the moment. We are working on it.")
            else:
                st.warning("Currently, there are no practicals available for this subject. Please check back later.")
        else:
            st.warning("Sorry, we don't have information for this subject right now. Please check back later.")
    else:
        st.warning("Currently, there are no subjects available in the repository. We are updating our content and will have more subjects soon.")
    
if __name__ == "__main__":
    main()




