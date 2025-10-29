import pandas as pd
from pathlib import Path
from src.utils import map_frequency_to_numeric

def load_raw_csv(path: str) -> pd.DataFrame:
    """Load raw CSV exported from Google Sheets or your intake form"""
    df = pd.read_csv(path, dtype=str)
    return df

def sanitize_and_standardize(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Flexible sanitizer that works with unordered Google Sheet columns (2025 schema)."""
    df = raw_df.copy()
    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("__", "_")

    # Ensure essential columns exist
    required = ['firm_name', 'employees_fte', 'monthly_labor_hours_2025_total', 'tech_tools_list']
    missing = [r for r in required if r not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {missing}")

    # Build tools_count if missing
    if 'tools_count' not in df.columns:
        df['tools_count'] = df.get('tech_tools_list', '').fillna('').astype(str).apply(
            lambda s: 0 if s.strip()=='' else len([x for x in s.split(',') if x.strip()])
        )
    else:
        df['tools_count'] = pd.to_numeric(df['tools_count'], errors='coerce').fillna(0)

    # Map frequency to numeric
    if 'tools_frequency_of_use' in df.columns:
        df['tools_frequency_of_use_numeric'] = df['tools_frequency_of_use'].apply(map_frequency_to_numeric)
    else:
        df['tools_frequency_of_use_numeric'] = 0.0

    # Collect revenue columns dynamically; coerce to numeric
    revenue_cols = [c for c in df.columns if c.startswith('monthly_revenue_2025_')]
    if revenue_cols:
        df[revenue_cols] = df[revenue_cols].apply(lambda col: pd.to_numeric(col, errors='coerce'))

    # Other numerics
    numeric_cols = ['employees_fte', 'annual_tech_spend', 'capital_invested',
                    'profit_margin_percent', 'online_revenue_share_percent', 'monthly_labor_hours_2025_total']
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    # Revenue total (convenience)
    if revenue_cols:
        df['revenue_2025_total'] = df[revenue_cols].sum(axis=1, skipna=True)

    # Add a firm_id if missing
    if 'firm_id' not in df.columns:
        df.insert(0, 'firm_id', range(1, len(df)+1))

    return df

def save_processed(df: pd.DataFrame, out_path: str):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    return out_path
