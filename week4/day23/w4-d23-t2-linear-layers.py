"""Week 4, Day 23, Task 2: understand a linear layer's shapes."""
import torch
from torch import nn
layer = nn.Linear(in_features=3, out_features=2)
x = torch.tensor([[1.0, 2.0, 3.0]])
print("Output:", layer(x))
print("Weight shape:", layer.weight.shape)
print("Bias shape:", layer.bias.shape)

