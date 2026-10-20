import pytest
from pydantic import ValidationError

from app.schemas import Customer


def test_customer_valid_schema(sample_valid_customer):
    customer = Customer(**sample_valid_customer)
    assert customer.credit_score == 650
    assert customer.geography == "France"
    assert customer.age == 42
    assert customer.tenure == 5
    assert customer.balance == 75000.0
    assert customer.num_of_products == 2
    assert customer.has_credit_card is True
    assert customer.is_active_member is True


def test_customer_invalid_credit_score_too_low(sample_valid_customer):
    sample_valid_customer["credit_score"] = 200
    with pytest.raises(ValidationError):
        Customer(**sample_valid_customer)


def test_customer_invalid_credit_score_too_high(sample_valid_customer):
    sample_valid_customer["credit_score"] = 900
    with pytest.raises(ValidationError):
        Customer(**sample_valid_customer)


def test_customer_invalid_geography(sample_valid_customer):
    sample_valid_customer["geography"] = "Italy"
    with pytest.raises(ValidationError):
        Customer(**sample_valid_customer)


def test_customer_invalid_age(sample_valid_customer):
    sample_valid_customer["age"] = 12
    with pytest.raises(ValidationError):
        Customer(**sample_valid_customer)


def test_customer_invalid_num_of_products(sample_valid_customer):
    sample_valid_customer["num_of_products"] = 5
    with pytest.raises(ValidationError):
        Customer(**sample_valid_customer)


def test_customer_invalid_tenure(sample_valid_customer):
    sample_valid_customer["tenure"] = 15
    with pytest.raises(ValidationError):
        Customer(**sample_valid_customer)
