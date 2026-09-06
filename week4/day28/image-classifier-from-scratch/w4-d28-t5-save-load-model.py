import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 5: save and safely reload the model."""
import torch
from project_common import OUTPUT, ImageCNN

model = ImageCNN()
OUTPUT.mkdir(exist_ok=True)
path = OUTPUT / "state-dict-demo.pt"
torch.save(model.state_dict(), path)
restored = ImageCNN()
restored.load_state_dict(torch.load(path, map_location="cpu", weights_only=True))
restored.eval()
print("Saved and restored:", path)
