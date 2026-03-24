from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "House Price API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    size = float(data.get('size', 0))
    
    prediction = model.predict([[size]])[0]
    
    return jsonify({
        "house_size": size,
        "predicted_price": round(prediction, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)