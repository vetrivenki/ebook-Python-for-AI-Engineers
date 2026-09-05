"""Week 4, Day 23, Task 4: create an nn.Sequential network."""
import torch
from torch import nn
model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 2))
print(model)
print("Batch output shape:", model(torch.randn(5, 4)).shape)

