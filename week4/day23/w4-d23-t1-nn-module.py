"""Week 4, Day 23, Task 1: define a model with nn.Module."""
import torch
from torch import nn
class SmallNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.output = nn.Linear(4, 2)
    def forward(self, x):
        return self.output(x)
model = SmallNet()
print(model(torch.randn(3, 4)))

