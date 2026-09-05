from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
"""Week 4, Day 28, Task 7: make one prediction with confidence."""
import torch
import argparse
from PIL import Image
from torchvision import transforms
from project_common import load_model
parser = argparse.ArgumentParser()
parser.add_argument("--image", help="Path to an RGB image; omit for a synthetic demo")
args = parser.parse_args()
model, classes = load_model()
if args.image:
    transform = transforms.Compose([transforms.Resize((32, 32)), transforms.ToTensor(),
                                    transforms.Normalize((0.5,)*3, (0.5,)*3)])
    with Image.open(args.image) as source:
        image = transform(source.convert("RGB")).unsqueeze(0)
else:
    from project_common import pattern_data
    image = pattern_data(1, seed=45)[0][0].unsqueeze(0)
print("This model recognizes synthetic color classes, not real-world object names.")
with torch.inference_mode(): probabilities = model(image).softmax(1); confidence, index = probabilities.max(1)
print({"class": classes[index.item()], "confidence": round(confidence.item(), 4)})
