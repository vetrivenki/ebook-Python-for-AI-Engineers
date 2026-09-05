from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 25, Task 6: train a CNN on small image data."""
import torch
from torch import nn
from week4_common import TinyCNN, image_loaders, run_epoch
train, valid = image_loaders(samples=160); model = TinyCNN()
optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
train_loss, train_acc = run_epoch(model, train, nn.CrossEntropyLoss(), optimizer)
valid_loss, valid_acc = run_epoch(model, valid, nn.CrossEntropyLoss())
print(f"train={train_acc:.1%} validation={valid_acc:.1%} losses={train_loss:.3f}/{valid_loss:.3f}")

