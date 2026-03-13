# 🩺 Medical Recommendation System using Machine Learning

This project builds a **Medical Recommendation System** using **Machine Learning (Clustering)** and **FastAPI**.
It analyzes patient symptoms and health indicators to recommend possible diseases and outcomes.

---

# 🚀 Project Overview

The system groups patients using **KMeans Clustering** based on symptoms and medical indicators.
When a new patient profile is submitted, the system:

1. Processes the patient data
2. Finds the closest cluster of similar patients
3. Recommends the most common disease in that cluster
4. Predicts the possible outcome

---

# 🧠 Machine Learning Approach

Algorithm used:

* **KMeans Clustering**
* **Nearest Neighbors Similarity**
* **Feature Scaling (StandardScaler)**
* **Label Encoding for categorical data**

---

# 📊 Dataset

Dataset used:
**Disease Symptoms and Patient Profile Dataset**

Features include:

* Disease
* Fever
* Cough
* Fatigue
* Difficulty Breathing
* Age
* Gender
* Blood Pressure
* Cholesterol Level
* Outcome Variable

---

# 🏗 Project Structure

```
medical-recommendation-system
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── preprocessing.py
│   ├── clustering.py
│   └── recommendation.py
│
├── data
│   └── Disease_symptom_and_patient_profile_dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/medical-recommendation-system.git
```

Move into project folder:

```
cd medical-recommendation-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Running the API

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📘 API Documentation

FastAPI automatically generates API documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

You will see **Swagger UI** where you can test the recommendation API.

---

# 📥 Example API Request

POST `/recommend`

```
{
 "Disease": "Influenza",
 "Fever": "Yes",
 "Cough": "No",
 "Fatigue": "Yes",
 "Difficulty_Breathing": "Yes",
 "Age": 19,
 "Gender": "Female",
 "Blood_Pressure": "Low",
 "Cholesterol_Level": "Normal"
}
```

---

# 📤 Example API Response

```
{
 "Cluster": 1,
 "Recommended Disease": "Influenza",
 "Outcome Prediction": "Positive"
}
```

---

# 🛠 Technologies Used

* Python
* FastAPI
* Scikit-learn
* Pandas
* Uvicorn
* Pydantic

---

# 📈 Future Improvements

* Drug recommendation system
* Cluster visualization using PCA
* Streamlit Web Interface
* Model performance evaluation
* Deployment to cloud (Render / AWS / Docker)

---

