import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def preprocess_data(path):

    data = pd.read_csv(path)

    binary_cols = [
        "Fever",
        "Cough",
        "Fatigue",
        "Difficulty Breathing",
        "Outcome Variable",
    ]

    for col in binary_cols:
        data[col] = data[col].map(
            {"Yes": 1, "No": 0, "Positive": 1, "Negative": 0}
        )

    categorical_cols = [
        "Gender",
        "Blood Pressure",
        "Cholesterol Level",
        "Disease",
    ]

    le_dict = {}

    for col in categorical_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        le_dict[col] = le

    features = data.drop(["Outcome Variable"], axis=1)

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(features)

    return data, X_scaled, le_dict, scaler