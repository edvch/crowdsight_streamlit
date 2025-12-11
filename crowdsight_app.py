import streamlit as st
import requests
import pandas as pd
import numpy as np
import tempfile

from io import StringIO

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: black;'>Crowdsight &#128065;</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'><i>Insert project description</i></h3>", unsafe_allow_html=True)

st.divider()

uploaded_file = st.file_uploader("Choose an image", type=["jpg"], width=700)
if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

st.write(tmp_path)
st.space(size="small")

# Prediction type
option = st.selectbox(
        "Which methode do you want to use?",
        ("Human count", "Human localisation"),
        index=None,
        placeholder="Select method...",
        width=700)

st.space(size="small")

if st.button("Let's compute"):
        st.markdown("<p style='text-align: left; color: red;'><i>I'm doing nothing for the moment, \
        please code some actions</i></p>", unsafe_allow_html=True)

        st.divider()  # Draws a horizontal line

        st.markdown("<h3 style='text-align: center; color: black;'>Compute results</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        col1.markdown("<p style='text-align: center;'><i>Image you selected</i></p>", unsafe_allow_html=True)

        if option == 'Human count':
            col1.image(tmp_path)
            col2.markdown("<p style='text-align: center;'><i>Result</i></p>", unsafe_allow_html=True)
            col2.write(f"<p style='text-align: center; color: black;'>\
                    The predicted number of people in this image is: <br> 321\
                        </br></p>",unsafe_allow_html=True)

            col2.write(f"<p style='text-align: center; color: black;'>\
                    The real number of people in this image is: <br> 578\
                        </br></p>",unsafe_allow_html=True)

        elif option == 'Human localisation':
            col1.image(tmp_path)
            col2.markdown("<p style='text-align: center;'><i>Result</i></p>", unsafe_allow_html=True)
            col2.image('/Users/edvch/Desktop/tennis_court_pred.jpg')
