import pandas as pd
orders=pd.DataFrame({"order_id":[1,2],"customer_id":[101,102],"sales":[500,750]})
customers=pd.DataFrame({"customer_id":[101,102],"customer":["Asha","Ben"]})
print(orders.merge(customers,on="customer_id"))
print(orders.set_index("customer_id").join(customers.set_index("customer_id")))
print(pd.concat([orders,orders],ignore_index=True))
