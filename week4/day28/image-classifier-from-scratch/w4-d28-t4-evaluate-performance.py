from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 4: evaluate accuracy and confusion matrix."""
import csv, torch
from project_common import OUTPUT, load_model, test_loader
model, classes = load_model(); valid = test_loader(); matrix = torch.zeros(len(classes), len(classes), dtype=torch.int64)
with torch.inference_mode():
    for images, labels in valid:
        for truth, prediction in zip(labels, model(images).argmax(1)): matrix[truth, prediction] += 1
accuracy = matrix.diag().sum().item() / matrix.sum().item(); path = OUTPUT/"confusion-matrix.csv"; OUTPUT.mkdir(exist_ok=True)
with path.open("w", newline="") as file: csv.writer(file).writerows([["actual/predicted", *classes], *[[classes[i], *row.tolist()] for i, row in enumerate(matrix)]])
print(f"Accuracy: {accuracy:.1%}"); print("Saved:", path)
