import streamlit as st
import base64
from google.cloud import aiplatform
import pandas as pd

endpoint = aiplatform.Endpoint("YOUR_ENDPOINT_HERE")

# The car part



# Encode the image 
def encode_image(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

def run():

  st.title('Damaged Car Application')

  st.write('The goal of the trained model is to predict based on an image uploaded.')
  uploaded_file = st.file_uploader("Choose a file")
  if uploaded_file is not None:
        # # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write("filename:", uploaded_file.name)

        # st.write(bytes_data)
        # prediction = endpoint.predict([dataframe])


        # st.write(prediction)
        if st.button("Predict"):
            prediction = endpoint.predict(bytes_data)

if __name__ == '__main__':
  run()