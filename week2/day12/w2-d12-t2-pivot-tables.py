import pandas as pd

df = pd.DataFrame(
    {
        "region": ["East", "East", "West", "West"],
        "product": ["Laptop", "Mouse", "Laptop", "Mouse"],
        "revenue": [2000, 500, 1800, 650],
    }
)
print(
    df.pivot_table(
        index="region", columns="product", values="revenue", aggfunc="sum", fill_value=0
    )
)
