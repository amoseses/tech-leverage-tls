"""
TLS computation functions.
"""

import pandas as pd
import numpy as np

def compute_tls_row(n_tools, p_auto, labor_hours_month, frequency_proxy=0.0, scale=1000.0):
    """
    Compute TLS for a single row.

    - n_tools: number of distinct tools (int or float)
    - p_auto: proportion automated (0..1) or NaN (use frequency_proxy)
    - labor_hours_month: total paid labor hours per month (must be > 0)
    - frequency_proxy: fallback numeric proxy (0..1) derived from usage frequency
    - scale: multiply raw TLS by this to produce readable numbers
    """
    # defensively coerce
    try:
        n_tools = float(n_tools)
    except Exception:
        n_tools = 0.0
    # choose p_auto if valid, else fallback to frequency_proxy
    p = None
    try:
        if p_auto is None or (isinstance(p_auto, float) and np.isnan(p_auto)):
            p = float(frequency_proxy if frequency_proxy is not None else 0.0)
        else:
            p = float(p_auto)
    except Exception:
        p = float(frequency_proxy if frequency_proxy is not None else 0.0)

    try:
        hours = float(labor_hours_month)
        if hours <= 0:
            raise ValueError
    except Exception:
        # avoid division by zero; treat as missing -> return NaN
        return np.nan

    # constrain p to [0,1] for interpretability
    if p < 0:
        p = 0.0
    if p > 1:
        # if frequency_proxy or raw percent > 1, treat as percent -> scale to 0..1 if >1 and <=100
        if p <= 100:
            p = p / 100.0
        else:
            p = 1.0

    raw = (n_tools * p) / hours
    return raw * scale

def compute_tls_df(df: pd.DataFrame,
                   tools_col: str = 'tools_count',
                   p_auto_col: str = 'p_auto',
                   freq_col: str = 'tools_frequency_of_use_numeric',
                   hours_col: str = 'monthly_labor_hours_2025_total',
                   out_col: str = 'tls'):
    """
    Compute TLS for a dataframe and append column `out_col`.
    - Attempts to coerce and normalize columns.
    - If p_auto column missing, uses freq_col as proxy.
    """
    df = df.copy()

    # ensure numeric columns
    df[tools_col] = pd.to_numeric(df.get(tools_col, 0), errors='coerce').fillna(0)
    df[hours_col] = pd.to_numeric(df.get(hours_col, np.nan), errors='coerce')

    # p_auto: if present, coerce; otherwise NaN
    if p_auto_col in df.columns:
        df[p_auto_col] = pd.to_numeric(df.get(p_auto_col), errors='coerce')
    else:
        df[p_auto_col] = np.nan

    # frequency proxy: if present, coerce
    if freq_col in df.columns:
        df[freq_col] = pd.to_numeric(df.get(freq_col, 0), errors='coerce').fillna(0)
    else:
        df[freq_col] = 0.0

    # normalize frequency proxy if values > 1 but <= 10 (assume 1-10 scale)
    maxf = df[freq_col].replace(0, pd.NA).max()
    if pd.notna(maxf) and maxf > 1:
        df[freq_col] = df[freq_col] / maxf  # normalize to 0..1

    # compute tls per row
    out_vals = []
    for idx, row in df.iterrows():
        n_tools = row.get(tools_col, 0)
        p_auto = row.get(p_auto_col, np.nan)
        freq_proxy = row.get(freq_col, 0.0)
        hours = row.get(hours_col, np.nan)
        tls_val = compute_tls_row(n_tools=n_tools, p_auto=p_auto, labor_hours_month=hours, frequency_proxy=freq_proxy, scale=1000.0)
        out_vals.append(tls_val)

    df[out_col] = out_vals

    # also add a raw (unscaled) column for diagnostics
    df['tls_raw'] = df[out_col] / 1000.0

    return df
