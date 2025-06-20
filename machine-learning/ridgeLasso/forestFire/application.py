from flask import Flask,request,render_template,jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__) # Create a Flask application instance, act as the WSGI application
app = application

# import ridge model and standard scaler pickle file
try:
    with open(r'C:\Users\Aaditya Khanal\OneDrive\Desktop\python_practice\machine-learning\ridgeLasso\ENDtoEND\models\ridge.pkl', 'rb') as f:
        ridge_model = pickle.load(f)
    print("Pickle loaded successfully for ridge model !")
    with open(r'C:\Users\Aaditya Khanal\OneDrive\Desktop\python_practice\machine-learning\ridgeLasso\ENDtoEND\models\scaler.pkl', 'rb') as f:
        standard_scaler = pickle.load(f)
    print("Pickle loaded successfully for standard scaler !")

except (pickle.UnpicklingError, EOFError, FileNotFoundError) as e:
    print(f"Oops, failed to load pickle: {e}")
    data = None
@app.route('/') # Define a route for the root URL

def index():
    return render_template('index.html') # Render the index.html template

@app.route('/predictdata',methods=['GET','POST'])

def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True) # host and port are default
    