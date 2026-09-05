from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7,4))
ax.plot(["Jan","Feb","Mar","Apr"],[1200,1500,1350,1800],marker="o")
ax.set(title="Monthly Sales",xlabel="Month",ylabel="Revenue")
fig.tight_layout()
out=Path(__file__).with_name("matplotlib-fundamentals.png")
fig.savefig(out,dpi=150)
print("Saved",out.name)
