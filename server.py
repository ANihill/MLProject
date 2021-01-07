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
    # speed requires upper and lower limit based on dataset 
    if speed > 0 and speed < 25:
        windspeed = np.array([speed])
        prediction =  model.predict(windspeed)
        return prediction
    else: 
        return 0 


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/power')
def power():
    wind = float(fl.request.args.get("wind", 0.0))
    p = predict_power(wind)
    return {"power output": p}


if __name__ == "__main__":
    app.run(debug=True)