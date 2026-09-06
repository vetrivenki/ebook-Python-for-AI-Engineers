import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 8: run fast project smoke tests."""
import torch
from project_common import ImageCNN, loaders, seed_all

seed_all()
model = ImageCNN()
train, valid = loaders(samples=50, batch_size=10)
images, labels = next(iter(train))
logits = model(images)
assert logits.shape == (10, 10)
assert labels.min() >= 0 and labels.max() < 10
assert len(train.dataset) == 40 and len(valid.dataset) == 100
loss = torch.nn.CrossEntropyLoss()(logits, labels)
loss.backward()
assert any(p.grad is not None for p in model.parameters())
print("All smoke tests passed.")
