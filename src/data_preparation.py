import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Función para la carga de datos

def load_data(path: str) -> pd.DataFrame:
    """
    Carga de la data original
    """
    return pd.read_csv(path)


# Limpieza de datos

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reemplazar data inválida (cero) con la mediana
    """
    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    for col in cols:
        df[col] = df[col].replace(0, df[col].median())

    return df

# División en Train y Test

def split_data(df: pd.DataFrame):
    """
    Dividir la data en train y test.
    """
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    return train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

# Guardar dataset

def save_data(X_train, X_test, y_train, y_test):
    """
    Guardar dataset procesada en un directorio estructurado
    """
    os.makedirs("data/training", exist_ok=True)

    X_train.to_csv("data/training/X_train.csv", index=False)
    X_test.to_csv("data/training/X_test.csv", index=False)
    y_train.to_csv("data/training/y_train.csv", index=False)
    y_test.to_csv("data/training/y_test.csv", index=False)


# ejecución principal

def main():

    raw_path = "data/raw/diabetes.csv"

    df = load_data(raw_path)
    df = clean_data(df)

    X_train, X_test, y_train, y_test = split_data(df)

    save_data(X_train, X_test, y_train, y_test)

    print("Data preparation completed successfully.")


if __name__ == "__main__":
    main()
