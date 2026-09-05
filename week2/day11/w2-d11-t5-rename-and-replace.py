import pandas as pd
df=pd.DataFrame({"Prod Name":["Laptop","Mouse"],"Region":["E","W"]})
df=df.rename(columns={"Prod Name":"product","Region":"region"})
df["region"]=df["region"].replace({"E":"East","W":"West"})
print(df)
