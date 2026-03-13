from fastapi import FastAPI
import pandas as pd
from app.models import Patient
from app.preprocessing import preprocess_data
from app.clustering import train_clustering
from app.recommendation import get_recommendation

app = FastAPI(title="Medical Recommendation System API")

# Dataset path (STRING not pandas)
DATA_PATH = "Disease_symptom_and_patient_profile_dataset.csv"

# Load and preprocess dataset
data, X_scaled, le_dict, scaler = preprocess_data(DATA_PATH)

# Train clustering model
kmeans, nn, clusters = train_clustering(X_scaled)

data["Cluster"] = clusters


@app.get("/")
def home():
    return {"message": "Medical Recommendation API Running"}


@app.post("/recommend")
def recommend(patient: Patient):

    new_patient = {
        "Disease": le_dict["Disease"].transform([patient.Disease])[0],
        "Fever": 1 if patient.Fever == "Yes" else 0,
        "Cough": 1 if patient.Cough == "Yes" else 0,
        "Fatigue": 1 if patient.Fatigue == "Yes" else 0,
        "Difficulty Breathing": 1 if patient.Difficulty_Breathing == "Yes" else 0,
        "Age": patient.Age,
        "Gender": le_dict["Gender"].transform([patient.Gender])[0],
        "Blood Pressure": le_dict["Blood Pressure"].transform([patient.Blood_Pressure])[0],
        "Cholesterol Level": le_dict["Cholesterol Level"].transform([patient.Cholesterol_Level])[0]
    }

    new_df = pd.DataFrame([new_patient])

    return get_recommendation(new_df, data, kmeans, nn, scaler, le_dict)