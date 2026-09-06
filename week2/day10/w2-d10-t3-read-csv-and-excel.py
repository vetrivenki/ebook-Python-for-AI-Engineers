from pathlib import Path

import pandas as pd

folder = Path(__file__).parent
df = pd.DataFrame({"product": ["Laptop", "Mouse"], "sales": [1800, 500]})
df.to_csv(folder / "sample-sales.csv", index=False)
df.to_excel(folder / "sample-sales.xlsx", index=False)
print(pd.read_csv(folder / "sample-sales.csv"))
print(pd.read_excel(folder / "sample-sales.xlsx"))
