import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 24, Task 5: store loss history."""
import torch
from torch import nn
from week4_common import TinyMLP, classification_loaders, run_epoch

train, _ = classification_loaders()
model = TinyMLP()
optimizer = torch.optim.Adam(model.parameters(), lr=0.02)
history = []
for _ in range(5):
    loss, _ = run_epoch(model, train, nn.CrossEntropyLoss(), optimizer)
    history.append(loss)
print("Loss history:", [round(value, 4) for value in history])
