"""Week 4, Day 23, Task 3: compare common activations."""

import torch
from torch import nn

x = torch.tensor([-2.0, 0.0, 2.0])
print("ReLU:", nn.ReLU()(x))
print("Sigmoid:", nn.Sigmoid()(x))
print("Tanh:", nn.Tanh()(x))
print("Softmax:", nn.Softmax(dim=0)(x), "sum =", nn.Softmax(dim=0)(x).sum())
