import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

infile = Path("data/processed/with_tls.csv")
if not infile.exists():
    raise FileNotFoundError("Processed file not found. Run scripts/run_pipeline.py first.")

df = pd.read_csv(infile)
print("Loaded", len(df), "rows")
print(df[['firm_id','firm_name','tls']].head())

# Summary stats
summary = df['tls'].describe()
print(summary)
Path("results").mkdir(parents=True, exist_ok=True)
Path("results/figures").mkdir(parents=True, exist_ok=True)
figpath = Path("results/figures/tls_hist.png")
plt.hist(df['tls'].dropna(), bins=10)
plt.title("TLS distribution")
plt.xlabel("TLS")
plt.ylabel("Count")
plt.savefig(figpath)
print("Saved histogram to", figpath)
# Save summary
summary.to_csv("results/summary_stats.csv")
print("Saved summary to results/summary_stats.csv")
