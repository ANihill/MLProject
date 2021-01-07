from flask import Flask, render_template
# https://pypi.org/project/silence-tensorflow/
import silence_tensorflow.auto
import tensorflow as tf
import tensorflow.keras as kr 
import h5py
import numpy as np

model = kr.models.load_model("model.h5")

def predict_power(speed):
    # speed requires upper and lower limit based on dataset 
    if speed > 0 and speed < 25:
        windspeed = np.array([speed])
        return model.predict(windspeed)
    else: 
        return 0 

test = predict_power(100)

print(test)

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)