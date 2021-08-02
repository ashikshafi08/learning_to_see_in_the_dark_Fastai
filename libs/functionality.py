import matplotlib.pyplot as plt
import fastbook
from fastai import *
from fastai.vision.all import *
import os
import streamlit as st
import gdown
import urllib
from PIL import Image

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


def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/someshfengde/learning_to_see_in_dark-/main/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")


def predict(img, cho):
    image = Image.open(img).convert('RGB')
    image_array = np.array(image)
    if cho == 0:
        mod_name = './first_model.pkl'
    elif cho == 1:
        mod_name = './four_hr_model.pkl'
    model = load_learner(mod_name)
    prediction = model.predict(image_array)
    p_image = prediction[0].numpy()
    return np.transpose(p_image, (1, 2, 0))


def run_the_app():
    choice = st.radio(label='select model', options=['MODEL_S', 'MODEL_E'])
    if choice:
        if choice == 'MODEL_E':
            cho = 0
            download_file('first_model.pkl')
        elif choice == 'MODEL_S':
            cho = 1
            download_file('four_hr_model.pkl')
        img = st.file_uploader(label='upload image to convert it to daytime here', type=['jpg', 'png', 'jpeg'])

        if cho == 0 or cho == 1 and img:
            reshaped_image = Image.open(img).convert('RGB').reshape(224, 224, 3)
            st.image(reshaped_image, use_column_width=True, caption='your image')
            predicted_image = predict(img, cho)
            st.image(predicted_image, use_column_width=True, caption='converted image')
        else:
            st.write('upload the image first')
    else:
        st.write('select the file first')
