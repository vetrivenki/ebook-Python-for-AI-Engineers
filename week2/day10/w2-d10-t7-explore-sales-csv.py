from pathlib import Path

import pandas as pd

path = Path(__file__).with_name("day10-sales.csv")
df = pd.DataFrame(
    {
        "region": ["East", "West", "North", "South"] * 2,
        "product": ["Laptop", "Mouse", "Monitor", "Keyboard"] * 2,
        "revenue": [1200, 500, 900, 400, 1500, 650, 1100, 550],
    }
)
df.to_csv(path, index=False)
loaded = pd.read_csv(path)
print(loaded.head())
print(loaded.tail())
print(loaded.describe(include="all"))
