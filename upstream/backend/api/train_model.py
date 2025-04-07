# backend/api/train_model.py

import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine
from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV,
    StratifiedKFold
)
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler
)
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
    f1_score,
    RocCurveDisplay
)

# ─── 0) Database Connection ───────────────────────────────────────────────────
DB_USER     = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST     = os.getenv('DB_HOST', 'postgres')
DB_PORT     = os.getenv('DB_PORT', '5432')
DB_NAME     = os.getenv('DB_NAME', 'churn_db')

ENGINE = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ─── 1) Load & Feature–Engineer ───────────────────────────────────────────────
def load_and_engineer() -> pd.DataFrame:
    df = pd.read_sql("SELECT * FROM customers", ENGINE)

    # Binary target
    df['churn'] = df['churn'].str.lower().map({'yes':1, 'no':0})
    # Ensure numeric
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

    # Keep base features
    base = [
        'tenure','monthly_charges','total_charges',
        'contract','gender','senior_citizen','partner','dependents',
        'internet_service','multiple_lines','online_security','online_backup',
        'device_protection','tech_support','streaming_tv','streaming_movies',
        'paperless_billing','payment_method'
    ]
    df = df[base + ['churn']].dropna()

    # Engineered features
    df['avg_charge_per_month'] = df['total_charges'] / (df['tenure'] + 1e-3)
    svc_cols = [
        'multiple_lines','online_security','online_backup',
        'device_protection','tech_support',
        'streaming_tv','streaming_movies'
    ]
    df['services_count'] = df[svc_cols].apply(
        lambda row: sum(str(x).lower()=='yes' for x in row),
        axis=1
    )
    df['tenure_bucket'] = pd.cut(
        df['tenure'],
        bins=[-1,12,24,48,np.inf],
        labels=['0-12','12-24','24-48','48+']
    )
    return df

# ─── 2) Split & Preprocess ────────────────────────────────────────────────────
def build_preprocessor():
    # Numeric pipeline
    num_feats = [
        'tenure','monthly_charges','total_charges',
        'avg_charge_per_month','services_count'
    ]
    num_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    # Categorical pipeline
    cat_feats = [
        'contract','gender','senior_citizen','partner','dependents',
        'internet_service','paperless_billing','payment_method',
        'tenure_bucket'
    ]
    cat_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    return ColumnTransformer([
        ('num', num_pipe, num_feats),
        ('cat', cat_pipe, cat_feats)
    ])

# ─── 3) Train + Hyperparameter Tuning ─────────────────────────────────────────
def train_and_tune(X_train, y_train):
    preprocessor = build_preprocessor()

    # Full pipeline
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('model', GradientBoostingClassifier(random_state=42))
    ])

    # Hyperparameter space (20 random draws)
    param_dist = {
        'model__n_estimators':     [100, 200, 300, 500],
        'model__learning_rate':    [0.01, 0.03, 0.05, 0.1],
