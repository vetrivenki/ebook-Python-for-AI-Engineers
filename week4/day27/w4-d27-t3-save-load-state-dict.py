import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
"""Week 4, Day 27, Task 3: save and load a model state_dict."""
import torch
from week4_common import TinyCNN, save_state

path = Path(__file__).with_name("output") / "cnn-state.pt"
model = TinyCNN()
save_state(model, path)
restored = TinyCNN()
restored.load_state_dict(torch.load(path, map_location="cpu", weights_only=True))
restored.eval()
print("Loaded safely from:", path)
