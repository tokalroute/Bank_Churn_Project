from unittest.mock import MagicMock

import numpy as np

from app.evaluation import evaluate_model


def test_evaluate_model():
    mock_model = MagicMock()
    # 4 predictions: 2 correct positives, 1 false positive, 1 correct negative
    mock_model.predict.return_value = np.array([1, 1, 0, 0])
    y_test = np.array([1, 0, 0, 0])
    X_test = np.array([[1], [2], [3], [4]])

    metrics = evaluate_model(mock_model, X_test, y_test)
    assert "accuracy" in metrics
    assert "recall" in metrics
    assert "f1" in metrics
    assert metrics["accuracy"] == 0.75
    assert metrics["recall"] == 1.0
