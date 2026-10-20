import json
from fastapi import FastAPI, HTTPException
from app.config import config
from app.logging_config import setup_logging
from app.model_service import model, predict
from app.schemas import Customer

setup_logging()
app = FastAPI(title="Bank Churn Prediction API")

@app.get("/health")
def health():
    return {"status": "healthy" if model is not None else "not_ready"}

@app.get("/model/info")
def model_info():
    if not config.metrics_path.exists():
        raise HTTPException(status_code=503, detail="Train the model first")
    with open(config.metrics_path, encoding="utf-8") as file:
        return json.load(file)

@app.post("/predict")
def predict_one(customer: Customer):
    if model is None:
        raise HTTPException(status_code=503, detail="Train the model first")
    return predict([customer.model_dump()])[0]

@app.post("/predict/batch")
def predict_batch(customers: list[Customer]):
    if model is None:
        raise HTTPException(status_code=503, detail="Train the model first")
    if not 1 <= len(customers) <= 50:
        raise HTTPException(status_code=422, detail="Send 1 to 50 customers")
    results = predict([customer.model_dump() for customer in customers])
    return {"count": len(results), "results": results}

