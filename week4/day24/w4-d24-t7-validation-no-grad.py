from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 24, Task 7: evaluate without changing weights."""
import torch
from torch import nn
from week4_common import TinyMLP, classification_loaders, run_epoch
train, valid = classification_loaders(); model = TinyMLP(); opt = torch.optim.Adam(model.parameters(), lr=0.02)
run_epoch(model, train, nn.CrossEntropyLoss(), opt)
loss, accuracy = run_epoch(model, valid, nn.CrossEntropyLoss())
print(f"validation_loss={loss:.4f} validation_accuracy={accuracy:.1%}")

