import pandas as pd
df=pd.DataFrame({"order_id":[101,102,102,103],"sales":[500,750,750,900]})
print(df[df.duplicated()])
print(df.drop_duplicates())
