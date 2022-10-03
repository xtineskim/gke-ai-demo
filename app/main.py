from typing import Dict
import streamlit as st
import base64
from google.cloud import aiplatform
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import seaborn as sns

load_dotenv()

def get_endpoint_id() -> str:
  """This function reads the endpoint ID from the .env file

  Returns:
      str: the endpoint id
  """
  endpoint_id = os.getenv("ENDPOINT_ID")

  if endpoint_id is None or endpoint_id=="":
    raise ValueError("Invalid endpoint: Add the endpoint ID in the app/.env file")
  else:
    return endpoint_id


def send_prediction_request(image_bytes: bytes, endpoint_id: str) -> Dict:
  # get the endpoint instance
  endpoint = aiplatform.Endpoint(endpoint_id)

  # encode image bytes
  encoded_content = base64.b64encode(image_bytes).decode("utf-8")

  # Create test instances
  instances = [
    {
      "content": encoded_content,
      "parameters": {
        "confidenceThreshold": 0.5,
        "maxPredictions": 5
      }
    }
  ]

  response = endpoint.predict(instances=instances)
  return response.predictions


def visualize_prediction(
  dataframe: pd.DataFrame,
  x_label: str,
  y_label: str
  ):
  """This function creates a barplot based on theinput dataframe

  Args:
      dataframe (pd.DataFrame): prediction dataframe

  Returns:
      fig: pyplot figure
  """
  sns.set_context('paper')
  fig, ax = plt.subplots()
  sns.barplot(
    data=dataframe,
    x=x_label,
    y=y_label,
    palette = 'magma'
  )

  plt.xlabel(x_label)
  plt.ylabel(y_label)

  return fig


def run():

  st.title('Damaged Car Application')
  st.write('The goal of the trained model is to predict based on an image uploaded.')

  uploaded_file = st.file_uploader("Choose a file")

  if uploaded_file is not None:

    # display the uploaded image
    st.image(uploaded_file, caption='Uploaded image')

    # Read the image as bytes:
    bytes_data = uploaded_file.getvalue()

    if st.button("Predict"):
      # get the endpoint id
      endpoint_id = get_endpoint_id()
      response = send_prediction_request(
        image_bytes=bytes_data,
        endpoint_id=endpoint_id
        )

      # Save prediction response in a dataframe
      predictions = {}
      labels_col_name = "Label"
      predictions_col_name = "Prediction Confidence"
      for prediction in response:
        predictions = {
          labels_col_name: prediction["displayNames"],
          predictions_col_name: prediction["confidences"]
        }
      prediction_df = pd.DataFrame(data=predictions)
      st.dataframe(prediction_df)

      # Visualize the predictions
      fig = visualize_prediction(
        dataframe=prediction_df,
        x_label=labels_col_name,
        y_label=predictions_col_name
        )
      st.pyplot(fig)

if __name__ == '__main__':
  run()
