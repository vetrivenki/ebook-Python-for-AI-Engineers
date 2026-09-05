from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE=Path(__file__).parent
DATA=BASE/"sales-data.csv"
OUTPUT=BASE/"output"

def create_data():
 rng=np.random.default_rng(42); rows=240
 df=pd.DataFrame({"date":pd.date_range("2026-01-01",periods=rows,freq="D"),"region":rng.choice(["East","West","North","South"],rows),"product":rng.choice(["Laptop","Mouse","Monitor","Keyboard"],rows),"units":rng.integers(1,10,rows),"unit_price":rng.choice([25.,75.,250.,900.],rows),"unit_cost":rng.choice([12.,40.,170.,700.],rows)})
 df.loc[5,"region"]=None
 pd.concat([df,df.iloc[[0]]],ignore_index=True).to_csv(DATA,index=False)

def load_clean():
 if not DATA.exists(): create_data()
 df=pd.read_csv(DATA,parse_dates=["date"]).drop_duplicates()
 df["region"]=df["region"].fillna("Unknown")
 for c in ["units","unit_price","unit_cost"]:
  df[c]=pd.to_numeric(df[c],errors="coerce").fillna(df[c].median())
 df["revenue"]=df["units"]*df["unit_price"]
 df["profit"]=df["units"]*(df["unit_price"]-df["unit_cost"])
 df["month"]=df["date"].dt.to_period("M").astype(str)
 return df

def dashboard(df):
 OUTPUT.mkdir(exist_ok=True)
 fig,a=plt.subplots(2,2,figsize=(14,9))
 df.groupby("month")["revenue"].sum().plot(ax=a[0,0],marker="o",title="Monthly Revenue")
 df.groupby("product")["revenue"].sum().plot.barh(ax=a[0,1],title="Revenue by Product")
 df.groupby("region")["profit"].sum().plot.bar(ax=a[1,0],title="Profit by Region")
 p=df.pivot_table(index="region",columns="product",values="revenue",aggfunc="sum")
 sns.heatmap(p,annot=True,fmt=".0f",cmap="Blues",ax=a[1,1])
 fig.tight_layout(); target=OUTPUT/"sales-dashboard.png"; fig.savefig(target,dpi=160)
 return target

def main():
 df=load_clean(); target=dashboard(df); df.to_csv(OUTPUT/"cleaned-sales.csv",index=False)
 regions=df.groupby("region")["revenue"].sum().sort_values(ascending=False)
 products=df.groupby("product")["profit"].sum().sort_values(ascending=False)
 print("Total revenue:",round(df["revenue"].sum(),2))
 print("Total profit:",round(df["profit"].sum(),2))
 print("Top region:",regions.index[0],round(regions.iloc[0],2))
 print("Most profitable product:",products.index[0],round(products.iloc[0],2))
 print("Dashboard:",target)

if __name__=="__main__":
 main()
