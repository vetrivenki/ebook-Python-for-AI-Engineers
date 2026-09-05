import numpy as np
import pandas as pd
df=pd.DataFrame({"product":["Laptop",None,"Mouse"],"sales":[1200,np.nan,500]})
print(df.isna().sum())
print(df.fillna({"product":"Unknown","sales":df["sales"].median()}))
print(df.dropna())
