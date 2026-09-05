import pandas as pd
df=pd.DataFrame({"product":[" laptop ","MOUSE","wireless keyboard"]})
df["product"]=df["product"].str.strip().str.title()
df["word_count"]=df["product"].str.split().str.len()
print(df)
