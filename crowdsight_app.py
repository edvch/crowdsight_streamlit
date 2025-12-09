import streamlit as st
import requests
import pandas as pd
import tempfile

from io import StringIO

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: black;'>Crowdsight &#128065;</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'><i>Insert project description</i></h3>", unsafe_allow_html=True)

st.divider()  # Draws a horizontal line

uploaded_file = st.file_uploader("Choose an image", type=["jpg"], width=700)
if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

st.space(size="small")

# Prediction type
option = st.selectbox(
        "Which methode do you want to use?",
        ("Human count", "Human localisation", "Both"),
        index=None,
        placeholder="Select method...",
        width=700)

tmp_path = ""
if option:
    st.badge(f"You selected: {option}", color="green")
    # if option == 'Human count':
    #     url = 'https://crowdsight.ai/human_count_pred'
    # elif option == 'Human localisation':
    #     url = 'https://crowdsight.ai/vgg_pred'
    # else:
    #     url = 'https://crowdsight.ai/yolo_pred'

st.space(size="small")

params = {'filepath':tmp_path}
url="" # to be delete, temporary
if st.button("Let's compute"):
    if url:
        response = requests.get(url, params=params)
    else:
        st.markdown("<p style='text-align: left; color: red;'><i>I'm doing nothing for the moment, \
        please code some actions</i></p>", unsafe_allow_html=True)

    if uploaded_file:
        st.divider()  # Draws a horizontal line

        st.markdown("<h3 style='text-align: left; color: black;'>Compute results</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        col1.markdown("<p style='text-align: center;'><i>Image you selected</i></p>", unsafe_allow_html=True)
        col1.image(tmp_path)

            # if option == 'Human count':
            #     st.markdown("<p><i>Result</i></p>", unsafe_allow_html=True)
            #     predicted_count = round(float(response.json()['predict_human_count']), 2)
            #     st.write(f"<p style='text-align: left; color: black;'>\
            #         The number of people in this image is: <br>{predicted_count}\
            #             </br></p>",unsafe_allow_html=True)
