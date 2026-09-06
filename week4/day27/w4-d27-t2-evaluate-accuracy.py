import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 27, Task 2: calculate classification accuracy."""
import torch
from week4_common import TinyCNN, image_loaders

_, valid = image_loaders(samples=100)
model = TinyCNN()
correct = total = 0
model.eval()
with torch.inference_mode():
    for x, y in valid:
        correct += (model(x).argmax(1) == y).sum().item()
        total += y.numel()
print(f"Accuracy: {correct / total:.1%} ({correct}/{total})")
