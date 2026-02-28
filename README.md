# MLOps Introduction: Final Project
FInal work description in  the [final_project_description.md](final_project_description.md) file.

Student info:
- Full name: Hansen Wibelsman Bueno Gómez
- e-mail: hansen.bueno.g@uni.pe
- Grupo: 

## Project Name: [Insert Your Project Title Here]

Put here the description, implementation doc, info, results, etc about your work.
You can also use links/reference to other documents/files form this repository or outside resources.

Remarks: feel free to modify this file for documentation 
TODO:
...

################################################################################

## Predicción de diabetes - Proyecto de machine learning

### 1. Definición del probelma

El objetivo del proyecto es desarrollar un modelo de Machine Learning capaz de predecir si una persona tiene diabetes a partir de variables clínicas como:
    * Glucosa
    * BMI
    * Año
    * Presión sanguínea
    * Insulina

Target:
    * Outcome
        0 - No diabetes
        1 - Diabetes


Contexto

La detección temprana de diabetes permite mejorar la prevención y el tratamiento, reduciendo riesgos médicos.

Tipo del problema: Clasificación binaria

Dataset

Se utilizó el dataset Pima Indians Diabetes, almacenado en:

### 2 EDA

    * Evaluación de la calidad de la data
    * Identificación de valores ceros
    * Análisis de la distribución del target
    * Análisis de relación entre el target y los features

### 3. Experimentación

    * Data cleaning

    * Modelos evaluados
        - Regresión Logística
        - Random Forest
        - Support Vector Machine
    
    * Métricas de evaluación
        - Accuracy
        - Precision
        - Recall
        - F1-Score
        - ROC - AUC

    * Mejor modelo
        - Random Forest con AUC-ROC de 0.82

### 4. Desarrollo del modelo de machine learning

* Preparación de la data
    - Data cruta alamcenada en 'data/raw/'
    - Limpieza y transformación en 'src/data_preparation.py'
    - Data procesada en 'data/training/'
    - Se generan los siguientes archivos:
        -- X_train.csv
        -- X_test.csv
        -- y_train.csv
        -- y_test.csv
* Entrenamiento del modelo
    - Lógica del entrenamiento implementado en stc/train.py
        Este script:
        -- Carga data procesada
        -- Entrena el modelo ganador
        -- Evaluación
        -- Serializa el modelo
    - Modelo de entrenamiento guardado en: models/random_forest.pkl

### 5. Model Deploymen and Serving
- Implementación del API REST usando Flask: src/serving.py
- Para correr la API: python src/serving.py
- End Point disponible: POST/predict

    -- Ejemplo Request
    La API necesita un objeto JSON con la siguiente estructura:

{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 85,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 35
}


    -- Ejemplo de Respuesta

{
  "prediction": 1,
  "probability": 0.82
}


### 6. Resultados

* El modelo final logró un mejor performance en términos de:
    - Accuracy
    - ROC-AUC

7. Reproducibilidad 

* Preparación de la data: python src/data_preparation.py

* Entrenamiento del modelo: python src/train.py

* Correo la API: python src/serving.py

8. Conclusiones

* El modelo Random Forest mostró la mejor predicción entre los modelos evaluados
* El modelo es desplegable a traves de una REST API
* El proyecto sigue las prácticas de un ciclo de vida de machine learning