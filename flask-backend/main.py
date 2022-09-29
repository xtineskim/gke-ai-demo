from flask import Flask
from google.cloud import aiplatform

app = Flask(__name__)

aiplatform.init(
    project=ENV.PROJECT_NAME,

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://cloud-ml-tables-data',

)


@app.route("/")
def main():
    return "<p>Hello</p>"