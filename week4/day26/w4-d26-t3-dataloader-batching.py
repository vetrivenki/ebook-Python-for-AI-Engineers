"""Week 4, Day 26, Task 3: batch and shuffle data."""
import torch
from torch.utils.data import DataLoader, TensorDataset
data = TensorDataset(torch.randn(25, 4), torch.randint(0, 2, (25,)))
loader = DataLoader(data, batch_size=8, shuffle=True, num_workers=0)
for batch, (x, y) in enumerate(loader, start=1): print(f"batch={batch} x={tuple(x.shape)} y={tuple(y.shape)}")

