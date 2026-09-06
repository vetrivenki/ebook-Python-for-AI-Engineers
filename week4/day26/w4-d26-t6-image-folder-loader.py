"""Week 4, Day 26, Task 6: show the ImageFolder structure and loader."""

from pathlib import Path

from PIL import Image
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

root = Path(__file__).with_name("sample-images")
for name, color in [("class-a", "red"), ("class-b", "blue")]:
    folder = root / name
    folder.mkdir(parents=True, exist_ok=True)
    for index in range(4):
        target = folder / f"demo-{index}.png"
        if not target.exists():
            Image.new("RGB", (32, 32), color).save(target)
print("Expected folders:", root / "class-a", "and", root / "class-b")
if root.exists():
    data = datasets.ImageFolder(
        root,
        transform=transforms.Compose(
            [transforms.Resize((32, 32)), transforms.ToTensor()]
        ),
    )
    print("Classes:", data.classes, "samples:", len(data))
    images, labels = next(iter(DataLoader(data, batch_size=4, shuffle=True)))
    print("Batch:", images.shape, labels.tolist())
else:
    print("Create class subfolders with images, then run this file again.")
