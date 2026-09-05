from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 27, Task 6: save only the best validation model."""
import torch
from torch import nn
from week4_common import TinyCNN, image_loaders, run_epoch, save_state
train, valid = image_loaders(samples=192); model = TinyCNN(); opt = torch.optim.Adam(model.parameters(), lr=0.003); best = -1.0
path = Path(__file__).with_name("output") / "best-cnn.pt"
for epoch in range(2):
    run_epoch(model, train, nn.CrossEntropyLoss(), opt); _, score = run_epoch(model, valid, nn.CrossEntropyLoss())
    if score > best: best = score; save_state(model, path)
print(f"Best accuracy={best:.1%}; saved={path}")

