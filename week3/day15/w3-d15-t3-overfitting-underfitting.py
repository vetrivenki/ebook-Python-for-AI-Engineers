"""Week 3 | Day 15 | Task 3: Compare tree complexity.

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

from sklearn.tree import DecisionTreeClassifier

for depth in [1, 4, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    print("Depth:", depth,
          "train accuracy:", round(model.score(X_train, y_train), 3),
          "validation accuracy:", round(model.score(X_valid, y_valid), 3))
print("A large train/validation gap suggests overfitting; one split is not proof.")
