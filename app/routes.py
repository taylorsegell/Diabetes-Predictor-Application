from flask import render_template, current_app as app, jsonify
import numpy
import requests
from app.forms import DiagnoseForm


@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", title='Home')


@app.route("/diagnose", methods=['GET'])
def diagnose():
    form = DiagnoseForm()
    return render_template("diagnose.html",
                           form=form,
                           title='Diagnose')





# Define the URL for the IBM Watson Machine Learning service
WML_URL = 'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/diabetesapp/predictions?version=2021-05-01'
API_KEY = "kAo8wfLY-SFjfIb9nsvm35oCkCxfxx_LYpFg4m08n61j"

@app.route('/diagnosis', methods=['POST'])
def diagnosis():
    form = DiagnoseForm()
    if form.validate_on_submit():
        form_dict = form.data
        form_dict.pop('csrf_token')
        form_dict.pop('submit')
        form_dict['gender'] = (form_dict['gender'] == 'True')  # Convert string to boolean

        # Create the payload for scoring
        payload_scoring = {
            "input_data": [
                {
                    "fields": [
                        "Age", "Gender", "Polyuria", "Polydipsia", "Sudden Weight Loss",
                        "Weakness", "Polyphagia", "Genital Thrush", "Visual Blurring", "Itching",
                        "Irritability", "Delayed Healing", "Partial Paresis", "Muscle Stiffness",
                        "Alopecia", "Obesity"
                    ],
                    "values": [list(form_dict.values())]
                }
            ]
        }

        # Obtain an access token for IBM Watson Machine Learning
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        # Define the headers for the request
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + mltoken
        }

        # Make a POST request to the IBM Watson Machine Learning service
        response_scoring = requests.post(WML_URL, json=payload_scoring, headers=header)
        prediction_data = response_scoring.json()

        # Extract the prediction result
        prediction = 'Positive' if prediction_data['predictions'][0]['values'][0][0] == 1 else 'Negative'
        
        accuracy = prediction_data['predictions'][0]['values'][0][1][1]  # Adjust the indices as needed


        results = {
            'prediction': prediction,
            'accuracy': accuracy
        }

        return results

    return jsonify(data=form.errors)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/report")
def report():
    return render_template("report.html", title='Report')


