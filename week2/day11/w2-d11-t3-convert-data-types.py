import pandas as pd

df = pd.DataFrame(
    {
        "date": ["2026-01-01", "2026-01-02"],
        "units": ["5", "8"],
        "price": ["99.50", "120.00"],
    }
)
df["date"] = pd.to_datetime(df["date"])
df["units"] = pd.to_numeric(df["units"])
df["price"] = df["price"].astype(float)
print(df)
print(df.dtypes)
