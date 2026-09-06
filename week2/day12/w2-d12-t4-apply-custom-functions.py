import pandas as pd

df = pd.DataFrame(
    {"product": ["Laptop", "Mouse", "Monitor"], "revenue": [2500, 600, 1400]}
)


def band(v):
    return "High" if v >= 2000 else "Medium" if v >= 1000 else "Low"


df["band"] = df["revenue"].apply(band)
print(df)
