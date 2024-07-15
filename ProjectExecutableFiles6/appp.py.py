import pickle
from flask import Flask,render_template,request
import pandas as pd
import numpy as np

model=pickle.load(open('fetalhealth.pkl','rb'))
app=Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/details", methods=["GET"])
def predict():
    return render_template('details.html')

@app.route("/output",methods=["POST","GET"])
def submit():
    if request.method == 'POST' :
        print(request.form.keys())
        input_features = [float(x) for x in request.form.values()]
        features_values = [np.array(input_features) ]
        print(features_values)
        
        predict = model.predict(features_values)
        
        print(predict[0])
        rounded_value = round(predict[0],2)
        text="Hence,based on calculation, the predicted FetalHealth Yield is: " + str(rounded_value)
        
        return render_template('output.html', prediction_text=text)
    return render_template('details.html')

if __name__ == "__main__":
    app.run(debug=True)
















































