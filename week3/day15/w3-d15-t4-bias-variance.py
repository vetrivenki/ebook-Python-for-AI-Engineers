"""Week 3 | Day 15 | Task 4: Estimate bias and variance with repeated training samples.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

rng = np.random.default_rng(42)
grid = np.linspace(-1, 1, 80).reshape(-1, 1)
truth = np.sin(3 * grid[:, 0])
for degree in [1, 4, 12]:
    predictions = []
    for repeat in range(30):
        X = rng.uniform(-1, 1, (40, 1))
        y = np.sin(3 * X[:, 0]) + rng.normal(0, 0.3, 40)
        model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=0.0001))
        model.fit(X, y)
        predictions.append(model.predict(grid))
    predictions = np.array(predictions)
    bias_squared = np.mean((predictions.mean(axis=0) - truth) ** 2)
    variance = np.mean(predictions.var(axis=0))
    print(
        "Degree:",
        degree,
        "bias squared:",
        round(bias_squared, 4),
        "variance:",
        round(variance, 4),
    )
print("Empirical estimates against a known function, not exact generalization error.")
