import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 24, Task 4: train over epochs and mini-batches."""
import torch
from torch import nn
from week4_common import TinyMLP, classification_loaders, run_epoch

train, _ = classification_loaders(batch_size=24)
model = TinyMLP()
optimizer = torch.optim.Adam(model.parameters(), lr=0.02)
for epoch in range(1, 4):
    loss, accuracy = run_epoch(model, train, nn.CrossEntropyLoss(), optimizer)
    print(f"epoch={epoch} loss={loss:.4f} accuracy={accuracy:.1%}")
