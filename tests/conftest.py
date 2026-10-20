import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def sample_valid_customer():
    return {
        "credit_score": 650,
        "geography": "France",
        "age": 42,
        "tenure": 5,
        "balance": 75000.0,
        "num_of_products": 2,
        "has_credit_card": True,
        "is_active_member": True,
    }


@pytest.fixture
def sample_german_customer():
    return {
        "credit_score": 720,
        "geography": "Germany",
        "age": 55,
        "tenure": 3,
        "balance": 120000.5,
        "num_of_products": 1,
        "has_credit_card": False,
        "is_active_member": False,
    }
