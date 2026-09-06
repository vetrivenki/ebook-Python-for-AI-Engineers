from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = np.random.default_rng(42).integers(10, 100, 10)
fig, a = plt.subplots(2, 3, figsize=(12, 7))
a[0, 0].plot(x, y)
a[0, 1].bar(x, y)
a[0, 2].hist(y)
a[1, 0].scatter(x, y)
a[1, 1].boxplot(y)
a[1, 2].axis("off")
fig.tight_layout()
out = Path(__file__).with_name("common-plots.png")
fig.savefig(out, dpi=150)
print("Saved", out.name)
