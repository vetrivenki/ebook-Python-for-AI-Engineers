"""Week 3 | Day 18 | Task 5: Explain algorithm trade-offs.

Run this file with Python after installing week3/requirements.txt.
Uses local sample data; no API key or network dataset is required.
"""

choices = {
    "Logistic Regression": "Strong fast baseline; linear decision boundary; scale features.",
    "Decision Tree": "Readable rules at shallow depth; deep trees can overfit.",
    "Random Forest": "Nonlinear tabular baseline; larger and less transparent.",
    "SVM": "Useful for medium-sized data; scale inputs; prediction can be costly.",
    "KNN": "Simple distance baseline; scale inputs; costly on large training sets.",
    "Naive Bayes": "Fast baseline; independence assumption may be unrealistic.",
}
for name, guidance in choices.items():
    print(name + ":", guidance)
print("Measure validation quality, training time, inference time, and model size.")
print("Use MultinomialNB for suitable count features; this week uses GaussianNB.")
