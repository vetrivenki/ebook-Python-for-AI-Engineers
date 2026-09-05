"""Week 3 | Day 16 | Task 2: Use the right categorical encoder.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder

# Unordered features: a separate indicator for each known category.
one_hot = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
one_hot.fit([["monthly"], ["annual"]])
print("One-hot names:", one_hot.get_feature_names_out())
print("Unseen category:", one_hot.transform([["weekly"]]))

# Ordered features: specify the meaningful ordering explicitly.
ordinal = OrdinalEncoder(categories=[["low", "medium", "high"]])
print("Ordered priorities:", ordinal.fit_transform([["high"], ["low"], ["medium"]]))

# LabelEncoder is for the target y, not ordinary input-feature columns.
target_encoder = LabelEncoder()
print("Encoded targets:", target_encoder.fit_transform(["stay", "churn", "stay"]))
print("Class mapping:", target_encoder.classes_)
