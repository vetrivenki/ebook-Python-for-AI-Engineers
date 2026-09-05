"""Week 4, Day 26, Task 2: create a custom in-memory image Dataset."""
import torch
from torch.utils.data import Dataset
class ColorImages(Dataset):
    def __init__(self, samples=20): self.images = torch.rand(samples, 3, 32, 32); self.labels = torch.arange(samples) % 4
    def __len__(self): return len(self.labels)
    def __getitem__(self, index): return self.images[index], self.labels[index]
image, label = ColorImages()[0]; print("Image:", image.shape, "label:", label.item())

