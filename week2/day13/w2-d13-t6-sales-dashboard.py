from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.DataFrame({"month":["Jan","Feb","Mar","Apr"]*3,"region":["East"]*4+["West"]*4+["North"]*4,"product":["Laptop","Mouse","Monitor","Keyboard"]*3,"revenue":[2000,500,1200,700,1800,650,1100,750,2100,550,1300,600]})
fig,a=plt.subplots(2,2,figsize=(12,8))
df.groupby("month",sort=False)["revenue"].sum().plot(ax=a[0,0],marker="o")
df.groupby("product")["revenue"].sum().plot.barh(ax=a[0,1])
sns.boxplot(data=df,x="region",y="revenue",ax=a[1,0])
p=df.pivot_table(index="region",columns="product",values="revenue",aggfunc="sum")
sns.heatmap(p,annot=True,fmt=".0f",ax=a[1,1])
fig.tight_layout()
out=Path(__file__).with_name("sales-dashboard.png")
fig.savefig(out,dpi=150)
print("Saved",out.name)
