"""Week 3 | Day 16 | Task 4: Route different columns through different steps.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(42)
data = pd.DataFrame({
    "tenure": rng.integers(1, 60, 120).astype(float),
    "monthly_fee": rng.uniform(20, 100, 120),
    "contract": rng.choice(["monthly", "annual"], 120),
})
risk = -1 + 1.4 * (data["contract"] == "monthly") - data["tenure"] / 40
target = (rng.random(120) < 1 / (1 + np.exp(-risk))).astype(int)
data.loc[::11, "tenure"] = np.nan
X_train, X_valid, y_train, y_valid = train_test_split(
    data, target, stratify=target, test_size=0.25, random_state=42,
)

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

numeric_steps = Pipeline([
    ("fill_missing", SimpleImputer(strategy="median")),
    ("scale", StandardScaler()),
])
category_steps = Pipeline([
    ("fill_missing", SimpleImputer(strategy="most_frequent")),
    ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
])
preprocessor = ColumnTransformer([
    ("numeric", numeric_steps, ["tenure", "monthly_fee"]),
    ("category", category_steps, ["contract"]),
])

prepared_train = preprocessor.fit_transform(X_train)
prepared_valid = preprocessor.transform(X_valid)
print("Train shape:", prepared_train.shape)
print("Validation shape:", prepared_valid.shape)
print("Feature names:", preprocessor.get_feature_names_out())
assert np.isfinite(prepared_valid).all()
