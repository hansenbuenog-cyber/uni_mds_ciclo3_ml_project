# src/serving.py

import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Inicializar aplicación Flask
app = Flask(__name__)

# Cargar modelo entrenado
model = joblib.load("models/random_forest.pkl")

# Endpoint raíz
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Diabetes Prediction API is running"})

# Endpoint de predicción
@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        # Convertir JSON a DataFrame
        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)