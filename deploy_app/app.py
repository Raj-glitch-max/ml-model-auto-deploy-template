from flask import Flask, jsonify, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # This will load index.html

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get the input data as JSON

    # Ensure the data contains exactly 13 features
    if len(data['data']) != 13:
        return jsonify({"error": "Invalid input. Expected 13 features."}), 400

    prediction_input = np.array(data['data']).reshape(1, -1)  # Reshape input for model prediction
    prediction = model.predict(prediction_input)  # Get the model prediction

    return jsonify({"prediction": prediction[0]})
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

