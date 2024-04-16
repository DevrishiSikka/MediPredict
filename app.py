from flask import Flask, render_template, request
import pickle
from forms import ParkinsonsForm
import numpy as np


app = Flask(__name__)
app.config['SECRET_KEY'] = '354tr12yu14u1#$dgsx887'

#FLASK CODE START
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/precautions')
def precautions():
  return render_template('precautions.html')


@app.route('/multiple-disease-predict')
def mdp():
  return "<h1>Multiple dissease Predict</h1>"

@app.route('/parkinsons-disease-predict', methods=['GET', 'POST'])
def pdp():
    parkinson = False
    form = ParkinsonsForm(request.form)
    filename = './models/parkinsons_model.sav'
    model = pickle.load(open(filename, 'rb'))
    if request.method == 'POST' and form.validate():
        input_data = [form.data[field] for field in form.data if field != 'csrf_token']
        input_data = input_data[:len(input_data)-1]
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction = model.predict(input_data_reshaped)
        print(prediction)
        if (prediction[0] == 0):
          parkinson = False
        else:
          parkinson = True
          
    return render_template('parkinsonsPredict.html', form=form, parkinson = parkinson)

if __name__ == "__main__":
  app.run()