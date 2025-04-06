# backend/main.py

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint, confloat, constr
import pickle
import pandas as pd

app = FastAPI(title="Customer Churn Prediction API")

# --- Load the Trained Model ---
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    model = None
    print("Error loading the model:", e)

# --- Define Input Schema ---
class CustomerInput(BaseModel):
    tenure:        conint(ge=0)
    monthly_charges: confloat(ge=0.0)
    contract:      constr(strict=True)
    gender:        constr(strict=True)
    senior_citizen: conint(ge=0, le=1)
    partner:       constr(strict=True)
    dependents:    constr(strict=True)

    internet_service:  constr(strict=True)
    paperless_billing: constr(strict=True)
    payment_method:    constr(strict=True)

    # ONE field instead of seven: a list of service names
    services_list:    List[constr(strict=True)] = []

def make_feature_df(data: CustomerInput) -> pd.DataFrame:
    d = data.dict()

    # 1) Derive total_charges & avg_charge_per_month
    d['total_charges'] = d['tenure'] * d['monthly_charges']
