def get_recommendation(new_df, data, kmeans, nn, scaler, le_dict):

    # Scale input
    X_new = scaler.transform(new_df)

    # Find similar patients
    distances, indices = nn.kneighbors(X_new)

    # Predict cluster
    cluster_id = kmeans.predict(X_new)[0]

    # Get most common disease in cluster
    recommended_disease = data[data["Cluster"] == cluster_id]["Disease"].mode()[0]

    # Get most common outcome
    recommended_outcome = data[data["Cluster"] == cluster_id]["Outcome Variable"].mode()[0]

    # Convert disease back to text
    disease_name = le_dict["Disease"].inverse_transform([recommended_disease])[0]

    return {
        "Cluster": int(cluster_id),
        "Recommended Disease": disease_name,
        "Outcome Prediction": "Positive" if recommended_outcome == 1 else "Negative"
    }