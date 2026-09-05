import pandas as pd
df=pd.DataFrame({"region":["East","East","West","West","East"],"category":["Computer","Accessory","Computer","Accessory","Computer"],"revenue":[2000,500,1800,650,2200]})
print(df.groupby(["region","category"]).agg(total_revenue=("revenue","sum"),average_order_value=("revenue","mean"),order_count=("revenue","size")))
