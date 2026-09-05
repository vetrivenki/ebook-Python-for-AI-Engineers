"""Week 4, Day 25, Task 3: compare max and average pooling."""
import torch
from torch import nn
x = torch.tensor([[[[1., 2., 3., 4.], [5., 6., 7., 8.], [9., 10., 11., 12.], [13., 14., 15., 16.]]]])
print("Max pool:\n", nn.MaxPool2d(2)(x).squeeze())
print("Average pool:\n", nn.AvgPool2d(2)(x).squeeze())

