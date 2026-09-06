from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

folder = Path(__file__).parent
fig, ax = plt.subplots()
ax.bar(["Laptop", "Mouse", "Monitor"], [5000, 1200, 2800])
for ext in ("png", "pdf", "svg"):
    fig.savefig(folder / ("product-revenue." + ext), dpi=150)
print("Saved PNG PDF SVG")
