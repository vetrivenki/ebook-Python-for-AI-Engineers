import pandas as pd

df = pd.DataFrame(
    {"region": ["East", "West", "East", "South"], "revenue": [1200, 900, 1800, 1500]}
)
print(df[df["revenue"] >= 1500])
print(df[(df["region"] == "East") & (df["revenue"] > 1000)])
