from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

folder = Path(__file__).parent
df = pd.DataFrame(
    {
        "sales": [10, 20, 15, 30, 25, 35],
        "profit": [2, 5, 3, 8, 6, 9],
        "region": ["East", "West", "East", "West", "North", "North"],
    }
)
sns.heatmap(df[["sales", "profit"]].corr(), annot=True)
plt.savefig(folder / "heatmap.png")
plt.close()
sns.pairplot(df[["sales", "profit"]]).savefig(folder / "pairplot.png")
plt.close("all")
sns.countplot(data=df, x="region")
plt.savefig(folder / "countplot.png")
print("Saved three charts")
