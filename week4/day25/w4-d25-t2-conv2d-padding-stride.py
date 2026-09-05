"""Week 4, Day 25, Task 2: compare padding and stride."""
import torch
from torch import nn
x = torch.randn(1, 3, 32, 32)
for layer in [nn.Conv2d(3, 8, 3), nn.Conv2d(3, 8, 3, padding=1), nn.Conv2d(3, 8, 3, stride=2, padding=1)]:
    print(layer, "->", tuple(layer(x).shape))

