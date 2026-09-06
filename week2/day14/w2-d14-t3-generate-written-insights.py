import pandas as pd

df = pd.DataFrame({"region": ["East", "West", "East"], "revenue": [2000, 1800, 2500]})
s = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
total = s.sum()
print("Total revenue:", round(total, 2))
print("Top region:", s.index[0], round(s.iloc[0], 2))
print("Top-region share:", round(s.iloc[0] / total * 100, 1), "%")
