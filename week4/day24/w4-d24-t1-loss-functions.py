"""Week 4, Day 24, Task 1: compare classification and regression losses."""
import torch
from torch import nn
logits = torch.tensor([[2.0, 0.5], [0.2, 1.8]])
labels = torch.tensor([0, 1])
print("Cross entropy:", nn.CrossEntropyLoss()(logits, labels).item())
print("MSE:", nn.MSELoss()(torch.tensor([2.5, 3.0]), torch.tensor([3.0, 2.0])).item())

