
# Coffee Cart Sales Analysis
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA = PROJECT_ROOT / "data" / "raw" / "coffee_sales.csv"
OUTDIR = PROJECT_ROOT / "analysis"
OUTDIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df.head()
df["revenue"] = df["quantity"] * df["unit_price"]
df.head()
# ### Daily revenue
daily = df.groupby("date")["revenue"].sum()
avg_daily = daily.mean()
daily

# Average Daily Revenue
print(f"Average daily revenue: ${avg_daily:.2f}")


# Compare revenue: random 50/50 split of the days
shuffled = df.sample(frac=1, random_state=30)
half = len(shuffled) // 2
group_a = shuffled.iloc[:half]
group_b = shuffled.iloc[half:]
print(f"Group A mean revenue: {group_a['revenue'].mean():.2f}")
print(f"Group B mean revenue: {group_b['revenue'].mean():.2f}")


# Revenue by product
by_product = df.groupby("product")["revenue"].sum()
by_product.plot(kind="bar")
plt.ylabel("Total revenue ($)")
plt.title("Revenue by product")
plt.savefig(OUTDIR/"revenue_by_product.png")
daily.to_csv(OUTDIR / "daily_revenue.csv")
with open(OUTDIR / "daily_revenue.csv", "a") as f:
    f.write(f"Average daily revenue,{avg_daily:.2f}\n")
    f.write(f"Group A mean revenue,{group_a['revenue'].mean():.2f}\n")
    f.write(f"Group B mean revenue,{group_b['revenue'].mean():.2f}\n")

#plt.show()
