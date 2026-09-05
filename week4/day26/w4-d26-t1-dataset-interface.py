"""Week 4, Day 26, Task 1: implement the Dataset interface."""
import torch
from torch.utils.data import Dataset
class Points(Dataset):
    def __init__(self): self.x = torch.randn(12, 3); self.y = (self.x.sum(1) > 0).long()
    def __len__(self): return len(self.y)
    def __getitem__(self, index): return self.x[index], self.y[index]
data = Points(); print("Length:", len(data)); print("First shapes:", data[0][0].shape, data[0][1].shape)

