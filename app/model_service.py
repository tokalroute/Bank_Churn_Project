import logging
import joblib
import pandas as pd
from app.config import config, FEATURES

# Load the saved model once when the API starts.
model = joblib.load(config.model_path) if config.model_path.exists() else None

def predict(customers: list[dict]) -> list[dict]:
    if model is None:
        raise FileNotFoundError("Train the model first")

    data = pd.DataFrame(customers).rename(columns={
        "credit_score": "CreditScore",
        "geography": "Geography",
        "age": "Age",
        "tenure": "Tenure",
        "balance": "Balance",
        "num_of_products": "NumOfProducts",
        "has_credit_card": "HasCrCard",
        "is_active_member": "IsActiveMember",
    })

    probabilities = model.predict_proba(data[FEATURES])[:, 1]
    results = []

    for probability in probabilities:
        probability = float(probability)
        if probability >= 0.7:
            risk = "High"
        elif probability >= 0.3:
            risk = "Medium"
        else:
            risk = "Low"

        results.append({
            "prediction": int(probability >= 0.5),
            "churn_probability": round(probability, 4),
            "risk_level": risk,
        })

    logging.info("Predicted %s customers", len(results))
    return results
