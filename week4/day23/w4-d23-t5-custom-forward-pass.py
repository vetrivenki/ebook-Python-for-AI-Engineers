"""Week 4, Day 23, Task 5: write a custom forward pass."""
import torch
from torch import nn
class ResidualToy(nn.Module):
    def __init__(self):
        super().__init__(); self.layer = nn.Linear(4, 4)
    def forward(self, x):
        return torch.relu(self.layer(x) + x)
print(ResidualToy()(torch.randn(2, 4)))

