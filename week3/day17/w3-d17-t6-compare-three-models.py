"""Week 3 | Day 17 | Task 6: Practice: compare three models on one split.

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

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=80, random_state=42, n_jobs=1),
    "SVM": make_pipeline(StandardScaler(), SVC(probability=True, random_state=42)),
    "KNN": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=9)),
    "Naive Bayes": GaussianNB(),
}

models = {name: model for name, model in models.items() if name in ["Logistic Regression", "Decision Tree", "Random Forest"]}
rows = []
for name, model in models.items():
    model.fit(X_train, y_train)
    labels = model.predict(X_valid)
    probability = model.predict_proba(X_valid)[:, 1]
    rows.append({
        "model": name, "accuracy": accuracy_score(y_valid, labels),
        "f1": f1_score(y_valid, labels), "roc_auc": roc_auc_score(y_valid, probability),
    })
table = pd.DataFrame(rows).sort_values("roc_auc", ascending=False)
print(table.round(3).to_string(index=False))
print("Validation comparison only. Do not call this an untouched final test.")
