import pandas as pd
df=pd.DataFrame({"product":["Laptop","Mouse","Monitor"],"units":[5,20,8],"revenue":[4500,500,2000]},index=["A","B","C"])
print(df["product"])
print(df[["product","revenue"]])
print(df.loc["A":"B",["product","units"]])
print(df.iloc[:2,:2])
