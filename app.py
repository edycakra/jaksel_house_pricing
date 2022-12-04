from crypt import methods
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

# create a flask app
app = Flask(__name__)

# load model
model = pickle.load(open("./data/final/regmodel.pkl", "rb"))
# load df
df = pickle.load(open("./data/final/df.pkl", "rb"))

# routes
# home route


@app.route('/')
def home():
    return render_template('home.html')

# predict_api


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    # print(data['NBED'])
    temp_numerical = [data["NBED"], data["NBATH"],
                      data["NFLOOR"], data["BLDAR"], data["LNDAR"]]
    # normalizing numerical list
    amin, amax = min(temp_numerical), max(temp_numerical)
    for i, val in enumerate(temp_numerical):
        temp_numerical[i] = (val-amin)/(amax-amin)

    # encode categorical input manually
    temp_categorical = [data["CERT"], data["LOC"]]

    encoded_categorical = []
    for i in range(0, 12):
        encoded_categorical.append(0.0)

    if temp_categorical == "HGB":
        encoded_categorical[0] = 1.0
    elif temp_categorical[0] == "Lainnya":
        encoded_categorical[1] = 1.0
    elif temp_categorical[0] == "SHM":
        encoded_categorical[2] = 1.0

    if temp_categorical[1] == "Cilandak":
        encoded_categorical[3] = 1.0
    elif temp_categorical[1] == "Kebayoran Baru":
        encoded_categorical[4] = 1.0
    elif temp_categorical[1] == "Kebayoran Lama":
        encoded_categorical[5] = 1.0
    elif temp_categorical[1] == "Mampang Prapatan":
        encoded_categorical[6] = 1.0
    elif temp_categorical[1] == "Pancoran":
        encoded_categorical[7] = 1.0
    elif temp_categorical[1] == "Pasar Minggu":
        encoded_categorical[8] = 1.0
    elif temp_categorical[1] == "Pesanggrahan":
        encoded_categorical[9] = 1.0
    elif temp_categorical[1] == "Setia Budi":
        encoded_categorical[10] = 1.0
    elif temp_categorical[1] == "Tebet":
        encoded_categorical[11] = 1.0

    # merge numerical and categorical
    merged_transformed_encoded = []
    merged_transformed_encoded.extend(temp_numerical)
    merged_transformed_encoded.extend(encoded_categorical)

    # output prediction
    output = model.predict([merged_transformed_encoded])
    print(output[0])
    return jsonify(output[0])


@app.route('/predict', methods=['POST'])
def predict():
    # data = [int(request.form.get("NBED")), int(request.form.get("NBATH")), int(
    #     request.form.get("NFLOOR")), int(request.form.get("BLDAR")), int(request.form.get("LNDAR")), request.form.get("CERT"), request.form.get("LOC")]

    temp_numerical = [int(request.form.get("NBED")), int(request.form.get("NBATH")), int(
        request.form.get("NFLOOR")), int(request.form.get("BLDAR")), int(request.form.get("LNDAR"))]
    # normalizing numerical list
    amin, amax = min(temp_numerical), max(temp_numerical)
    for i, val in enumerate(temp_numerical):
        temp_numerical[i] = (val-amin)/(amax-amin)

    # encode categorical input manually
    temp_categorical = [request.form.get("CERT"), request.form.get("LOC")]

    encoded_categorical = []
    for i in range(0, 12):
        encoded_categorical.append(0.0)

    if temp_categorical == "HGB":
        encoded_categorical[0] = 1.0
    elif temp_categorical[0] == "Lainnya":
        encoded_categorical[1] = 1.0
    elif temp_categorical[0] == "SHM":
        encoded_categorical[2] = 1.0

    if temp_categorical[1] == "Cilandak":
        encoded_categorical[3] = 1.0
    elif temp_categorical[1] == "Kebayoran Baru":
        encoded_categorical[4] = 1.0
    elif temp_categorical[1] == "Kebayoran Lama":
        encoded_categorical[5] = 1.0
    elif temp_categorical[1] == "Mampang Prapatan":
        encoded_categorical[6] = 1.0
    elif temp_categorical[1] == "Pancoran":
        encoded_categorical[7] = 1.0
    elif temp_categorical[1] == "Pasar Minggu":
        encoded_categorical[8] = 1.0
    elif temp_categorical[1] == "Pesanggrahan":
        encoded_categorical[9] = 1.0
    elif temp_categorical[1] == "Setia Budi":
        encoded_categorical[10] = 1.0
    elif temp_categorical[1] == "Tebet":
        encoded_categorical[11] = 1.0

    # merge numerical and categorical
    final_input = []
    final_input.extend(temp_numerical)
    final_input.extend(encoded_categorical)

    # predict input
    output = model.predict([final_input])[0]
    print("THIS IS DATA", final_input)
    return render_template("home.html", prediction_text="The house price is IDR {}".format(int(output)))


if __name__ == "__main__":
    app.run(debug=True)
