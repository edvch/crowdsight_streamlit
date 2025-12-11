import streamlit as st
import requests
import pandas as pd
import numpy as np
import tempfile
import cv2

from io import StringIO

def draw_points(img_path, coords, radius=5):
    img_loaded = cv2.imread(img_path)
    img = img_loaded.copy()
    for x, y in coords:
        cv2.circle(img, (int(x), int(y)), radius, (0, 0, 255), -1)
    return img

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: black;'>Crowdsight &#128065;</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'><i>Insert project description</i></h3>", unsafe_allow_html=True)

st.divider()

uploaded_file = st.file_uploader("Choose an image", type=["jpg"], width=700)
if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

st.space(size="small")

# Prediction type
option = st.selectbox(
        "Which methode do you want to use?",
        ("Human count", "Human localisation"),
        index=None,
        placeholder="Select method...",
        width=700)

if option:
    st.badge(f"You selected: {option}", color="green")
    if option == 'Human count':
        url = 'https://crowdsightlive-846239375882.europe-west9.run.app/human_count_pred'
    elif option == 'Human localisation':
        url = 'https://crowdsightlive-846239375882.europe-west9.run.app/vgg_pred'

st.space(size="small")

if uploaded_file:
    params = {'filepath':tmp_path}

if st.button("Let's compute"):
    if url:
        response = requests.get(url, params=params)
        st.write(f'RESPONSE = {response.text}')

    else:
        st.markdown("<p style='text-align: left; color: red;'><i>I'm doing nothing for the moment, \
        please code some actions</i></p>", unsafe_allow_html=True)

    if uploaded_file:
        st.divider()  # Draws a horizontal line

        st.markdown("<h3 style='text-align: center; color: black;'>Compute results</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        col1.markdown("<p style='text-align: center;'><i>Image you selected</i></p>", unsafe_allow_html=True)
        col1.image(tmp_path)

        if option == 'Human count':
            col2.markdown("<p style='text-align: center;'><i>Result</i></p>", unsafe_allow_html=True)
            predicted_count = round(float(response.json()['predict_human_count']),2)
            col2.write(f"<p style='text-align: center; color: black;'>\
                    The number of people in this image is: <br>{predicted_count}\
                        </br></p>",unsafe_allow_html=True)

        elif option == 'Human localisation':
            col2.markdown("<p style='text-align: center;'><i>Result</i></p>", unsafe_allow_html=True)
            col2.image(response.json()['img_to_draw'])
