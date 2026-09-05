"""Week 3 | Day 20 | Task 1: Use identical stratified folds.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Each model lesson uses the same data and validation split.
X, y = make_classification(
    n_samples=600, n_features=10, n_informative=6, n_redundant=2,
    weights=[0.7, 0.3], class_sep=0.8, random_state=42,
)
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42,
)

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=folds, scoring="roc_auc", n_jobs=1)
print("Fold AUC:", scores.round(3))
print("Mean and standard deviation:", round(scores.mean(), 3), round(scores.std(), 3))
print("The pipeline refits its scaler within every training fold.")
