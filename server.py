from flask import Flask, render_template, jsonify, url_for, request, json
# https://pypi.org/project/silence-tensorflow/
import silence_tensorflow.auto
import tensorflow as tf
import tensorflow.keras as kr 
import h5py
import numpy as np
import flask as fl
import pandas as pd

model = kr.models.load_model("model.h5")

def predict_power(speed):
    speed = float(speed)
    # speed requires upper and lower limit based on dataset 
    if speed >= 1 and speed <= 25:
        windspeed = np.array([speed])
        prediction =  model.predict(windspeed)
        return prediction
    else: 
        return "Invalid Input. Please Enter a Number Between 1 and 25."


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/power', methods=['GET', 'POST'])
def power():
     if request.method == 'POST' and 'speed' in request.form:
            speed = request.form['speed']
            prediction = predict_power(speed)
            if isinstance(prediction, str):
                error = prediction
                return render_template('index.html', msg=error)
            else:
                p = prediction[0][0]
                msg = "The Power Output for Windspeed of %s km/h is equal to %.3f kw." %(speed, p)
                return render_template('index.html', msg=msg)


if __name__ == "__main__":
    app.run(debug=True)