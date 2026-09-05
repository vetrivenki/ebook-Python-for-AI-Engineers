"""Week 3 | Day 20 | Task 4: Plot performance versus training-set size.

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

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=40, max_depth=5, random_state=42, n_jobs=1)
sizes, train_scores, valid_scores = learning_curve(
    model, X_train, y_train, train_sizes=[0.3, 0.6, 1.0], scoring="roc_auc",
    cv=StratifiedKFold(3, shuffle=True, random_state=42), n_jobs=1,
)
fig, ax = plt.subplots()
ax.plot(sizes, train_scores.mean(axis=1), marker="o", label="Training")
ax.plot(sizes, valid_scores.mean(axis=1), marker="o", label="Cross-validation")
ax.set(xlabel="Training rows per fold", ylabel="ROC-AUC", title="Learning curve")
ax.legend()
output = Path(__file__).parent / "output"
output.mkdir(exist_ok=True)
fig.savefig(output / "learning-curve.png", bbox_inches="tight")
plt.close(fig)
print("Training sizes:", sizes)
print("Validation AUC:", valid_scores.mean(axis=1).round(3))
print("Saved:", output / "learning-curve.png")
