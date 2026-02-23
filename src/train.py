# Importar librerías
import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

import mlflow
import mlflow.sklearn



# Carga de datos procesados

def load_training_data():
    X_train = pd.read_csv("data/training/X_train.csv")
    X_test = pd.read_csv("data/training/X_test.csv")
    y_train = pd.read_csv("data/training/y_train.csv")
    y_test = pd.read_csv("data/training/y_test.csv")

    return X_train, X_test, y_train, y_test


# Entrenar modelo campeón

def train_model(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train.values.ravel())

    return model



# Evaluación

def evaluate_model(model, X_test, y_test):

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, preds)
    roc_auc = roc_auc_score(y_test, probs)

    print("Accuracy:", accuracy)
    print("ROC-AUC:", roc_auc)

    return accuracy, roc_auc



# Guardar modelo

def save_model(model):

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/random_forest.pkl")

    print("Modelo guardado exitosamente.")



# Main Execution

def main():

    # Cargar datos
    X_train, X_test, y_train, y_test = load_training_data()

    mlflow.set_experiment("diabetes_training")

    with mlflow.start_run():

        # Entrenar
        model = train_model(X_train, y_train)

        # Evaluar
        accuracy, roc_auc = evaluate_model(model, X_test, y_test)

        # Log métricas
        mlflow.log_param("model", "RandomForest")
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("roc_auc", roc_auc)

        # Log modelo en MLflow
        mlflow.sklearn.log_model(model, name = 'random_forest_model')

        # Guardar modelo local
        save_model(model)


if __name__ == "__main__":
    main()

