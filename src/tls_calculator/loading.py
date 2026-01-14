import pandas as pd

REQUIRED_COLUMNS = [
    "firm_llc_id",
    "sector",
    "founded_year",
    "employees_fte",
    "annual_tech_spend",
    "capital_invested",
    "profit_margin_percent",
    "online_revenue_share_percent",
    "total_quarterly_labor_hours",
    "tech_tools_list",
    "tools_frequency_of_use",
]

def load_csv(path: str) -> pd.DataFrame:
    print(f"Loading raw CSV: {path}")
    return pd.read_csv(path)

def sanitize_and_standardize(df: pd.DataFrame) -> pd.DataFrame:
    print("Sanitizing and standardizing...")

    # Strip whitespace from column names
    df.columns = [c.strip() for c in df.columns]

    # Enforce required columns
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Convert obvious numeric columns safely
    numeric_cols = [
        "founded_year",
        "employees_fte",
        "annual_tech_spend",
        "capital_invested",
        "profit_margin_percent",
        "online_revenue_share_percent",
        "total_quarterly_labor_hours",
    ]

    # Add quarterly revenue columns dynamically
    revenue_cols = [c for c in df.columns if c.startswith("quarterly_revenue_")]
    numeric_cols.extend(revenue_cols)

    for col in numeric_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("%", "", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows that cannot be computed
    df = df.dropna(subset=["total_quarterly_labor_hours"])

    return df

def save_processed(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
    print(f"Saved processed file to: {path}")
