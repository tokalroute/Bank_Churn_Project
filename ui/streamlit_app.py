"""Session 2: One simple Streamlit form calling FastAPI."""
import sys
from pathlib import Path

import requests
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.config import config

st.title("Bank Churn Predictor")
st.write("Enter customer information to predict churn.")
st.caption("Teaching demo: not for real banking decisions.")

with st.form("customer_form"):
    credit_score = st.number_input("Credit score", 350, 850, 650)
    geography = st.selectbox("Country", ["France", "Germany", "Spain"])
    age = st.number_input("Age", 18, 100, 42)
    tenure = st.number_input("Years with bank", 0, 10, 5)
    balance = st.number_input("Balance", min_value=0.0, value=75000.0)
    num_of_products = st.number_input("Number of products", 1, 4, 2)
    has_credit_card = st.checkbox("Has credit card", value=True)
    is_active_member = st.checkbox("Active member", value=True)
    submitted = st.form_submit_button("Predict")

if submitted:
    customer = {
        "credit_score": credit_score,
        "geography": geography,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "num_of_products": num_of_products,
        "has_credit_card": has_credit_card,
        "is_active_member": is_active_member,
    }
    try:
        response = requests.post(f"{config.api_url}/predict", json=customer, timeout=10)
        if response.ok:
            result = response.json()
            st.metric("Churn probability", f"{result['churn_probability']:.1%}")
            st.write("Risk level:", result["risk_level"])
            st.write("Prediction:", result["prediction"])
        else:
            st.error(f"API error: {response.status_code} - {response.text}")
    except requests.RequestException:
        st.error("Cannot connect to FastAPI. Start the API server first.")

st.caption("To try batch predictions, open FastAPI /docs and use /predict/batch.")
