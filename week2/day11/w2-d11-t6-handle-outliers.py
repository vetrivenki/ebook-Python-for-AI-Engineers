import pandas as pd
s=pd.Series([100,110,115,120,125,130,1000])
q1,q3=s.quantile([.25,.75]); iqr=q3-q1
low,high=q1-1.5*iqr,q3+1.5*iqr
print("outliers",s[~s.between(low,high)].tolist())
print("clean",s[s.between(low,high)].tolist())
