import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

FEATURES = [
    "CreditScore", "Geography", "Age", "Tenure", "Balance",
    "NumOfProducts", "HasCrCard", "IsActiveMember",
]

@dataclass
class Config:
    data_path: Path = ROOT / os.getenv("DATA_PATH", "data/demo_churn.csv")
    model_path: Path = ROOT / os.getenv("MODEL_PATH", "artifacts/churn_model.joblib")
    metrics_path: Path = ROOT / os.getenv("METRICS_PATH", "artifacts/metrics.json")
    api_url: str = os.getenv("API_URL", "http://127.0.0.1:8000")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    test_size: float = 0.2
    random_state: int = 42
    
config = Config()
