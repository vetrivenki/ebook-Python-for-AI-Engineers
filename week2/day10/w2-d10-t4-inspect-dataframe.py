import pandas as pd
df=pd.DataFrame({"region":["East","West","North","South"],"revenue":[1200,1500,1100,1750]})
print(df.head(2))
print(df.tail(2))
print("shape",df.shape)
print("columns",df.columns.tolist())
print(df.dtypes)
print(df.describe(include="all"))
df.info()
