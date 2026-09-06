"""Week 4, Day 26, Task 5: make reproducible train/validation subsets."""

import torch
from torch.utils.data import TensorDataset, random_split

data = TensorDataset(torch.randn(100, 4), torch.randint(0, 2, (100,)))
generator = torch.Generator().manual_seed(42)
train, valid = random_split(data, [80, 20], generator=generator)
print("Train:", len(train), "Validation:", len(valid))
