import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 27, Task 1: complete train and validation loop."""
import torch
from torch import nn
from week4_common import TinyCNN, best_device, image_loaders, run_epoch

train, valid = image_loaders(samples=192)
device = best_device()
model = TinyCNN().to(device)
opt = torch.optim.Adam(model.parameters(), lr=0.003)
for epoch in range(1, 3):
    train_metrics = run_epoch(model, train, nn.CrossEntropyLoss(), opt, device)
    valid_metrics = run_epoch(model, valid, nn.CrossEntropyLoss(), device=device)
    print(f"epoch={epoch} train={train_metrics} valid={valid_metrics}")
