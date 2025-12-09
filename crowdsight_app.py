import streamlit as st
import requests
import pandas as pd
import tempfile

from io import StringIO

st.markdown("<h1 style='text-align: left; color: black;'>Crowdsight &#128065;</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: black;'><i>Insert project description</i></h3>", unsafe_allow_html=True)

st.divider()  # Draws a horizontal line

tmp_path = ""
with st.container(horizontal=False):
    # Image browser and create a tmp path in order to use it in our prediction function
    uploaded_file = st.file_uploader("Choose an image", type=["jpg"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

    st.space(size="small")

    # Prediction type
    option = st.selectbox(
        "Which methode do you want to use?",
        ("Human count", "Human localisation", "Both"),
    )

    st.space(size="small")

    st.badge(f"You selected: {option}", color="green")

    st.space(size="small")

    if st.button("Let's compute"):
        st.markdown("<p style='text-align: left; color: red;'><i>I'm doing nothing for the moment, \
            please code some actions</i></p>", unsafe_allow_html=True)
        # if option == 'Human count':
        #     pass
        # elif option == 'Human localisation':
        #     pass
        # else:
        #     pass

st.divider()  # Draws a horizontal line

st.markdown("<h3 style='text-align: left; color: black;'>Compute results</h3>", unsafe_allow_html=True)

with st.container(horizontal=True):
    st.markdown("<p><i>Image you selected</i></p>", unsafe_allow_html=True)

    if option == 'Human count':
        st.markdown("<p><i>Result</i></p>", unsafe_allow_html=True)
