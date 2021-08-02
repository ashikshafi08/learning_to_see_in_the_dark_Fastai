# %%
import streamlit as st
import os
import urllib
import gdown

EXTERNAL_DEPENDENCIES = {
    "first_model.pkl": {
        "url": "https://drive.google.com/uc?id=1--SFRPTTBImeD4qzWlY2TAKNlREchOv_",
        "size": 299015189

    },
    "four_hr_model.pkl": {
        "url": "https://drive.google.com/uc?id=1QKoF3I-qZC8zLqlMBb3NB5g0ibskrN8-",
        "size": 355994005
    }
}


def download_file(file_path):
    # Don't download the file twice. (If possible, verify the download using the file length.)
    if os.path.exists(file_path):
        print(os.path.getsize('./' + file_path) == EXTERNAL_DEPENDENCIES[file_path]["size"])
        print(os.path.getsize(file_path), EXTERNAL_DEPENDENCIES[file_path]["size"])
        if os.path.getsize(file_path) == EXTERNAL_DEPENDENCIES[file_path]["size"]:
            st.warning('model already there haha')
            return

    # These are handles to two visual elements to animate.
    weights_warning, progress_bar = None, None
    try:
        weights_warning = st.warning("Downloading %s..." % file_path)
        gdown.download(EXTERNAL_DEPENDENCIES[file_path]['url'], output=file_path)
        st.warning('download finished')
    finally:
        st.write('thanks for the patience')


# %%
download_file('four_hr_model.pkl')
# %%

image = st.file_uploader('upload image ', type=['jpg', 'png', 'jpeg'])
# %%
image.shape
# %%
