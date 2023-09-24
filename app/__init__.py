from flask import Flask
from config import Config
import pickle
import requests


# Construct core Flask application.
def init_app():
    app = Flask(__name__)
    # import configuration
    app.config.from_object(Config)
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)

        return app




import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.

# load machine learning models
rf_model = pickle.load(open('app/data/rf_model.pkl', 'rb'))
API_KEY = "kAo8wfLY-SFjfIb9nsvm35oCkCxfxx_LYpFg4m08n61j"
# Define the URL for the IBM Watson Machine Learning service
WML_URL = 'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/diabetesapp/predictions?version=2021-05-01'
        # Obtain an access token for IBM Watson Machine Learning
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + mltoken}