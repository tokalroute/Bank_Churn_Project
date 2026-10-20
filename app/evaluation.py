import logging
from sklearn.metrics import accuracy_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    metrics = {
        "accuracy": round(accuracy_score(y_test, predictions), 3),
        "recall": round(recall_score(y_test, predictions), 3),
        "f1": round(f1_score(y_test, predictions), 3),
    }
    logging.info("Evaluation: %s", metrics)
    return metrics
