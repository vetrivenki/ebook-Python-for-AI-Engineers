"""Week 4, Day 26, Task 4: apply torchvision image transforms."""

import torch
from torchvision.transforms import v2

transform = v2.Compose(
    [v2.RandomHorizontalFlip(p=1.0), v2.Normalize([0.5] * 3, [0.5] * 3)]
)
image = torch.rand(3, 32, 32)
changed = transform(image)
print("Shape:", changed.shape, "range:", (changed.min().item(), changed.max().item()))
