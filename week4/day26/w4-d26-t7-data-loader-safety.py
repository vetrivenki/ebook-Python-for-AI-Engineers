from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 26, Task 7: verify batches and value ranges."""
from week4_common import image_loaders
train, valid = image_loaders(samples=100, batch_size=16)
x, y = next(iter(train))
assert x.ndim == 4 and x.shape[1:] == (3, 32, 32)
assert x.min() >= 0 and x.max() <= 1
assert not train.dataset is valid.dataset
print("Batch and split checks passed:", x.shape, y.shape)

