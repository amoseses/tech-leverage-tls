import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load data
df = pd.read_csv("data/processed/with_tls.csv")

# Keep only rows with valid TLS
df = df.dropna(subset=["tls_scaled"])

# Convert key numeric columns
numeric_cols = [
    "employees_fte",
    "annual_tech_spend",
    "capital_invested",
    "profit_margin_percent",
    "online_revenue_share_percent",
    "total_quarterly_labor_hours",
]

for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows missing regression vars
reg_df = df.dropna(subset=["tls_scaled", "employees_fte", "annual_tech_spend"])

# -------------------------
# 1. Distribution of TLS
# -------------------------
plt.figure()
plt.hist(reg_df["tls_scaled"], bins=15)
plt.title("Distribution of Technology Leverage Score (TLS)")
plt.xlabel("TLS (scaled)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("results/tls_distribution.png")
plt.close()

# -------------------------
# 2. TLS vs Firm Size
# -------------------------
plt.figure()
plt.scatter(reg_df["employees_fte"], reg_df["tls_scaled"])
plt.xlabel("Employees (FTE)")
plt.ylabel("TLS (scaled)")
plt.title("TLS vs Firm Size")
plt.tight_layout()
plt.savefig("results/tls_vs_employees.png")
plt.close()

# -------------------------
# 3. Regression
# TLS ~ employees + tech spend
# -------------------------
X = reg_df[["employees_fte", "annual_tech_spend"]]
X = sm.add_constant(X)
y = reg_df["tls_scaled"]

model = sm.OLS(y, X).fit()

# Save regression summary
with open("results/tls_regression.txt", "w") as f:
    f.write(model.summary().as_text())

print("Phase 4 analysis complete.")
print("Outputs saved to /results")
