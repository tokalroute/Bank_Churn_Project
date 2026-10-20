from app.model_service import predict


def test_predict_single_customer(sample_valid_customer):
    results = predict([sample_valid_customer])
    assert len(results) == 1
    result = results[0]
    assert "prediction" in result
    assert "churn_probability" in result
    assert "risk_level" in result
    assert result["prediction"] in (0, 1)
    assert 0.0 <= result["churn_probability"] <= 1.0
    assert result["risk_level"] in ("Low", "Medium", "High")


def test_predict_multiple_customers(sample_valid_customer, sample_german_customer):
    results = predict([sample_valid_customer, sample_german_customer])
    assert len(results) == 2
    for res in results:
        assert res["risk_level"] in ("Low", "Medium", "High")
