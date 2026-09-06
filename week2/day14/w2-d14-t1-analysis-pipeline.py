from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

folder = Path(__file__).parent
raw = pd.DataFrame(
    {
        "region": ["East", "West", None, "East"],
        "units": [2, 3, 4, 2],
        "price": [900, 25, 250, 900],
    }
)
path = folder / "pipeline-sales.csv"
raw.to_csv(path, index=False)
df = pd.read_csv(path).drop_duplicates()
df["region"] = df["region"].fillna("Unknown")
df["revenue"] = df["units"] * df["price"]
summary = df.groupby("region", as_index=False)["revenue"].sum()
summary.plot.bar(x="region", y="revenue", legend=False)
plt.tight_layout()
plt.savefig(folder / "pipeline-summary.png")
print(summary)
