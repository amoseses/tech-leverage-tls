"""
Loading and sanitization utilities for raw intake CSVs.
"""

import pandas as pd
from pathlib import Path
from src.tls_calculator.utils import map_frequency_to_numeric, normalize_tools_list

def load_raw_csv(path: str) -> pd.DataFrame:
    """
    Read a raw CSV (exported from Google Sheets). Read as strings first to avoid dtype issues.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Raw CSV not found: {path}")
    # use low_memory False to ensure consistent dtype handling
    df = pd.read_csv(p, dtype=str, low_memory=False)
    return df

def sanitize_and_standardize(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize headers and basic types, create consistent columns expected by TLS calculator.
    - Lowercases headers and replaces spaces with underscores
    - Builds tools_count if missing
    - Converts frequency words (daily, weekly) to numeric proxy
    """
    df = raw_df.copy()

    # Normalize column names
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

    # Ensure basic columns exist but do not fail hard; user should confirm later
    # If firm_id missing, create one
    if 'firm_id' not in df.columns:
        df.insert(0, 'firm_id', range(1, len(df) + 1))

    # tools list normalization
    if 'tech_tools_list' in df.columns:
        df['tech_tools_list'] = df['tech_tools_list'].fillna('').astype(str)
        df['tools_count'] = df['tech_tools_list'].apply(normalize_tools_list)
    elif 'tools_list' in df.columns:
        df['tools_list'] = df['tools_list'].fillna('').astype(str)
        df['tools_count'] = df['tools_list'].apply(normalize_tools_list)
    else:
        # if no tools list provided, ensure tools_count exists (set to 0)
        if 'tools_count' not in df.columns:
            df['tools_count'] = 0

    # Map textual frequency to numeric proxy
    if 'tools_frequency_of_use' in df.columns:
        df['tools_frequency_of_use_numeric'] = df['tools_frequency_of_use'].apply(map_frequency_to_numeric)
    else:
        df['tools_frequency_of_use_numeric'] = 0.0

    # Coerce numeric fields where appropriate (best-effort)
    numeric_fields = [
        'employees_fte', 'annual_tech_spend', 'capital_invested',
        'profit_margin_percent', 'online_revenue_share_percent', 'monthly_labor_hours_2025_total'
    ]
    for nf in numeric_fields:
        if nf in df.columns:
            df[nf] = pd.to_numeric(df[nf], errors='coerce')

    # Coerce p_auto if present (assume supplied as decimal or percent)
    if 'p_auto' in df.columns:
        df['p_auto'] = pd.to_numeric(df['p_auto'], errors='coerce')
        # convert percents >1 to decimal
        df.loc[df['p_auto'] > 1, 'p_auto'] = df.loc[df['p_auto'] > 1, 'p_auto'] / 100.0

    # Identify revenue columns and coerce to numeric
    rev_cols = [c for c in df.columns if c.startswith('monthly_revenue_2025_')]
    for rc in rev_cols:
        df[rc] = pd.to_numeric(df[rc], errors='coerce')

    # convenience: total revenue in observed months
    if rev_cols:
        df['revenue_2025_total'] = df[rev_cols].sum(axis=1, skipna=True)

    return df

def save_processed(df: pd.DataFrame, out_path: str):
    p = Path(out_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    return str(p)
