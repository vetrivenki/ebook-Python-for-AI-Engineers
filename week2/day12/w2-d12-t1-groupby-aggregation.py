import pandas as pd
df=pd.DataFrame({"region":["East","East","West","West"],"revenue":[1000,1500,900,1300]})
print(df.groupby("region").agg(total=("revenue","sum"),average=("revenue","mean"),orders=("revenue","size")))
