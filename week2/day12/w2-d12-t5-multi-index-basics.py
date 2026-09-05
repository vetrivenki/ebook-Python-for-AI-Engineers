import pandas as pd
df=pd.DataFrame({"region":["East","East","West","West"],"product":["Laptop","Mouse","Laptop","Mouse"],"revenue":[2000,500,1800,650]}).set_index(["region","product"])
print(df)
print(df.loc["East"])
print(df.loc[("West","Laptop"),"revenue"])
