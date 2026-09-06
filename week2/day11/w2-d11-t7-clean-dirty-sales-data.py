import pandas as pd

df = pd.DataFrame(
    {
        "order_id": [1, 2, 2, 3, 4],
        "product": [" laptop ", "MOUSE", "MOUSE", None, "Monitor"],
        "units": ["2", "5", "5", "3", "1000"],
        "price": [900, 25, 25, None, 250],
    }
)
df = df.drop_duplicates().copy()
df["product"] = df["product"].fillna("Unknown").str.strip().str.title()
df["units"] = pd.to_numeric(df["units"], errors="coerce")
df["price"] = df["price"].fillna(df["price"].median())
df = df[df["units"] < 100]
df["revenue"] = df["units"] * df["price"]
print(df)
