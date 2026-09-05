"""Week 4, Day 25, Task 1: see a 2D convolution operation."""
import torch
from torch.nn.functional import conv2d
image = torch.arange(25, dtype=torch.float32).reshape(1, 1, 5, 5)
kernel = torch.tensor([[[[1., 0., -1.], [1., 0., -1.], [1., 0., -1.]]]])
print("Edge response:\n", conv2d(image, kernel).squeeze())

