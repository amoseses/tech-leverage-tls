import pandas as pd

# Load processed TLS data
df = pd.read_csv("data/processed/tls_dataset.csv")

# Generate simple summary stats
summary = {
    "num_firms": len(df),
    "avg_TLS": df["TLS_scaled"].mean(),
    "median_TLS": df["TLS_scaled"].median(),
    "avg_revenue": df.filter(like="monthly_revenue").mean(axis=1).mean(),
}

summary_df = pd.DataFrame([summary])
summary_df.to_csv("results/summary_stats.csv", index=False)

print("✅ Summary statistics generated:")
print(summary_df)
