import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("data/processed/with_tls.csv")

# Example: TLS vs revenue growth (if you have t0 and t1 revenue)
# This is a placeholder — adapt to your available temporal fields
if 'monthly_revenue_2025_01' in df.columns and 'monthly_revenue_2025_12' in df.columns:
    df['revenue_growth_pct'] = (df['monthly_revenue_2025_12'] - df['monthly_revenue_2025_01']) / df['monthly_revenue_2025_01']
    X = df[['tls', 'employees_fte']]
    X = sm.add_constant(X.fillna(0))
    y = df['revenue_growth_pct'].fillna(0)
    model = sm.OLS(y, X).fit()
    print(model.summary())
else:
    print("Revenue columns for growth not present; adjust regression.py to match your data")
