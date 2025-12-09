import streamlit as st
import requests
import pandas as pd

from io import StringIO

st.markdown("<h1 style='text-align: left; color: black;'>Crowdsight &#128065;</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; color: black;'><i>Insert project description</i></h3>", unsafe_allow_html=True)

st.divider()  # Draws a horizontal line

with st.container(horizontal=False):
    # Image browser
    uploaded_file = st.file_uploader("Choose an image")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

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
