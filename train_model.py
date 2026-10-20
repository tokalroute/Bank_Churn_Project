# Train model once Load model
import json
import logging
import joblib
from app.config import config
from app.logging_config import setup_logging
from app.data import load_data
from app.training import train_model
from app.evaluation import evaluate_model

setup_logging()

X_train, X_test, y_train, y_test = load_data()
model = train_model(X_train, y_train)
metrics = evaluate_model(model, X_test, y_test)

config.model_path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, config.model_path)
logging.info("Model saved to %s", config.model_path)

with open(config.metrics_path, "w", encoding="utf-8") as file:
    json.dump({"model": "Random Forest", "metrics": metrics}, file, indent=2)
logging.info("Metrics saved to %s", config.metrics_path)
