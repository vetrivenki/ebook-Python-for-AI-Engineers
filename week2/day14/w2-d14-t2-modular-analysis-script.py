import pandas as pd
def load_data():
 return pd.DataFrame({"region":["East","West"],"units":[3,5],"price":[100,80]})
def transform(df):
 result=df.copy(); result["revenue"]=result["units"]*result["price"]; return result
def summarize(df):
 return df.groupby("region",as_index=False)["revenue"].sum()
if __name__=="__main__":
 print(summarize(transform(load_data())))
