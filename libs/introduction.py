import streamlit as st
from libs.functionality import *


def show_introduction():
    readme_text = st.markdown(get_file_content_as_string("README.md"))

    # expander =  st.beta_expander(label='sample images',expanded=True)

    col1, col2 = st.beta_columns(2)
    c1 = col1.markdown(
        "<h2 style='text-align: center; color: gray;'>Dark image input</h1>",
        unsafe_allow_html=True,
    )
    c2 = col2.markdown(
        "<h2 style='text-align: center; color: gray;'>Enhanced image</h1>",
        unsafe_allow_html=True,
    )
    i1 = col1.image(
        "https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/input1.png",
        use_column_width=True,
    )
    i2 = col2.image(
        "https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/output1.png",
        use_column_width=True,
    )
    col3, col4 = st.beta_columns(2)
    i3 = col3.image(
        "https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/input2.png",
        use_column_width=True,
    )
    i4 = col4.image(
        "https://github.com/someshfengde/learning_to_see_in_dark/raw/main/images/output2.png",
        use_column_width=True,
    )

    st.sidebar.title("What to do")

    return
