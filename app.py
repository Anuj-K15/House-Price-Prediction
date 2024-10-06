from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    bhk = data['bhk']
    type = data['type']
    area = data['area']
    region = data['region']
    
    input_features = np.array([[bhk, type, area, region]])
    predicted_price = model.predict(input_features)
    
    return jsonify({'price': predicted_price[0]})

@app.route('/result')
def result():
    price = request.args.get('price', type=float)
    return render_template('result.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)
