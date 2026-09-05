from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")
fig,ax=plt.subplots()
ax.plot(["Jan","Feb","Mar"],[1200,1400,1600],marker="o",label="East")
ax.plot(["Jan","Feb","Mar"],[1000,1300,1250],marker="s",label="West")
ax.set(title="Regional Sales",xlabel="Month",ylabel="Revenue")
ax.legend(); fig.tight_layout()
out=Path(__file__).with_name("customized-chart.png")
fig.savefig(out,dpi=150)
print("Saved",out.name)
