### PyCon Ghana 2022 Google Cloud Workshop

This repo is the UI of the workshop that @sohailazangeneh and @ckim328 are running in October 2022.

### Running instructions

**NOTE** 

__This repository assumes that you have already trained and deployed a <i>Vertex AI AutoML Image Classification model </i> by following the instructions in this Qwiklab (add the link).__

#### Run on your local machine
1. Create and activate a virtual environment.

	This step is not required but it's recommended.<br>
	Create a python virtual environment called `pycon-venv` using the following command:<br>
	
		python3 -m venv pycon-venv
	
	Activate your virtual environment<br>
	
		source pycon-venv/bin/activate


2. Install the requirements. <br>
		Run the following command to install the requirements:<br>
		
		pip install -r requirements.txt
		
3. Copy the `endpoint id` of the Vertex AI endpoint that the model is deployed on and paste it in the `app/.env` file:<br>

		ENDPOINT_ID = ""
		
	For example, if the endpoint id is `1111222233334444555`, your `.env` file should look like:
	
		ENDPOINT_ID = "1111222233334444555"
		
4. Run the app using streamlit command:
		
		streamlit run app/main.py

