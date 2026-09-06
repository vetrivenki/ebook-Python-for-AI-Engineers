import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 1: inspect the offline CIFAR-shaped dataset."""
from project_common import loaders

train, valid = loaders(samples=100, batch_size=16)
images, labels = next(iter(train))
print(
    "Training samples:", len(train.dataset), "validation samples:", len(valid.dataset)
)
print("Image batch:", images.shape, "label batch:", labels.shape)
