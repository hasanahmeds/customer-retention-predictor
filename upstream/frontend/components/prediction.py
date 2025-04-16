import streamlit as st
import requests
import os

# Try to read from the environment, defaulting to the Compose service name:
API_URL = os.getenv("API_URL", "http://backend:8000")

def prediction_form():
    st.header("🔮 Customer Churn Prediction")
    st.markdown(
        "Fill in the customer’s profile below. "
        "Hover over any input for guidance on how to choose."
    )
    with st.form("prediction_form"):
        # --- Numeric Inputs ---
        tenure = st.number_input(
            "⏳ Tenure (months)",
            min_value=0, max_value=100, value=12,
            help="How many months this customer has been with the company."
        )
        monthly_charges = st.number_input(
            "💰 Monthly Charges ($)",
            min_value=0.0, value=70.0, format="%.2f",
            help="What the customer pays every month, on average."
        )

        # --- Core Categorical Inputs ---
        contract = st.selectbox(
            "📄 Contract Type",
            ["Month-to-month", "One year", "Two year"],
            help=(
                "Month-to-month contracts often see higher churn.\n"
                "One- and two-year contracts generally retain customers longer."
            )
        )
        gender = st.selectbox(
            "👤 Gender",
            ["Female", "Male"],
            help="Select the customer’s reported gender."
        )
