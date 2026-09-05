"""Week 3 | Day 19 | Task 3: Compare boosting libraries conceptually.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

from importlib.util import find_spec

libraries = {
    "xgboost": "Tree boosting with regularization; this week's runnable main implementation.",
    "lightgbm": "Histogram-based boosting, usually leaf-wise growth; control leaf complexity.",
    "catboost": "Boosting with built-in categorical handling and ordered techniques.",
}
for package, purpose in libraries.items():
    print(package, "| installed:", find_spec(package) is not None)
    print(" ", purpose)
print("LightGBM and CatBoost are optional overview topics; neither is required here.")
print("Do not claim one is always best: compare suitable pipelines on the same folds.")
