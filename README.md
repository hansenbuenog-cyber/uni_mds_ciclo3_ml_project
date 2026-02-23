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

##########

## Predicción de diabetes

### 0.0 Definición del probelma

PEl objetivo del proyecto es desarrollar un modelo de Machine Learning capaz de predecir si una persona tiene diabetes a partir de variables clínicas como:
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

Dataset

Se utilizó el dataset Pima Indians Diabetes, almacenado en:

data/raw/diabetes.csv

### 0.1 EDA

    * Evaluación de la calidad de la data
    * Identificación de valores ceros
    * Análisis de la distribución del target
    * Análisis de relación entre el target y los features

### 0.2 Experimentación

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

### 0.3 Desarrollo de modelos de machine learning
