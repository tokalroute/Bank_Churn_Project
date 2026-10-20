def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] in ("healthy", "not_ready")


def test_model_info_endpoint(client):
    response = client.get("/model/info")
    assert response.status_code == 200
    data = response.json()
    assert "model" in data
    assert "metrics" in data


def test_predict_single_endpoint(client, sample_valid_customer):
    response = client.post("/predict", json=sample_valid_customer)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "churn_probability" in data
    assert "risk_level" in data


def test_predict_single_invalid_payload(client, sample_valid_customer):
    invalid_customer = sample_valid_customer.copy()
    invalid_customer["age"] = -5
    response = client.post("/predict", json=invalid_customer)
    assert response.status_code == 422


def test_predict_batch_endpoint(client, sample_valid_customer, sample_german_customer):
    response = client.post(
        "/predict/batch", json=[sample_valid_customer, sample_german_customer]
    )
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 2
    assert len(data["results"]) == 2


def test_predict_batch_empty_list(client):
    response = client.post("/predict/batch", json=[])
    assert response.status_code == 422


def test_predict_batch_too_large(client, sample_valid_customer):
    payload = [sample_valid_customer] * 51
    response = client.post("/predict/batch", json=payload)
    assert response.status_code == 422
