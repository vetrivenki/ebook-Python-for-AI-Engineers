import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 6: write the architecture/results summary."""
import json

from project_common import OUTPUT

metrics_path = OUTPUT / "metrics.json"
history = json.loads(metrics_path.read_text()) if metrics_path.exists() else []
best = max((row["validation"]["accuracy"] for row in history), default=None)
summary = f"""# Image Classifier Project Summary

- Architecture: three convolution blocks, pooling, dropout, linear classifier
- Data: synthetic color-pattern images with learnable labels, not CIFAR-10
- Validation: 100 independent seed-43 images; final test: 100 seed-44 images
- Best validation accuracy: {best if best is not None else "run training first"}
- Checkpoint: model state dictionary plus class names
- Next step: train on CIFAR-10 and tune augmentation, learning rate, and epochs
"""
OUTPUT.mkdir(exist_ok=True)
path = OUTPUT / "project-summary.md"
path.write_text(summary)
print(summary)
print("Saved:", path)
