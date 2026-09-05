"""Week 4, Day 25, Task 5: inspect convolution feature maps."""
import torch
from torch import nn
images = torch.randn(2, 3, 32, 32)
features = nn.Sequential(nn.Conv2d(3, 8, 3, padding=1), nn.ReLU())(images)
print("Input:", tuple(images.shape))
print("Eight learned feature maps:", tuple(features.shape))
print("First map range:", features[0, 0].min().item(), features[0, 0].max().item())

