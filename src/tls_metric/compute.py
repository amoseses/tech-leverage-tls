"""
TLS computation utilities.

Compute Technology Leverage Score (TLS) according to:
    tls_raw = (n_tools * p_auto) / labor_hours_month
    tls = tls_raw * scale

Where:
- n_tools: integer count of distinct tools
- p_auto: proportion automated (0.0 - 1.0)
- labor_hours_month: total paid labor hours per month (must be > 0)
- scale: multiplier to make numbers human-readable (default 1000.0)
"""

from typing import Union
import pandas as pd


def compute_tls(n_tools: int, p_auto: float, labor_hours_month: float, scale: float = 1000.0) -> float:
    if labor_hours_month <= 0:
        raise ValueError("labor_hours_month must be > 0")
    if not (0.0 <= p_auto <= 1.0):
        raise ValueError("p_auto must be between 0.0 and 1.0")
    tls_raw = (n_tools * p_auto) / labor_hours_month
    tls = tls_raw * scale
    return float(tls)


def compute_tls_df(df: pd.DataFrame,
                   tools_col: str = 'n_tools',
                   p_auto_col: str = 'p_auto',
                   hours_col: str = 'labor_hours_month',
                   out_col: str = 'tls',
                   scale: float = 1000.0) -> pd.DataFrame:
    """
    Add a TLS column to a DataFrame using specified column names.
    Returns a *copy* of the DataFrame with the new column.
    """
    df = df.copy()
    if (df[hours_col] <= 0).any():
        raise ValueError("All labor_hours_month values must be > 0")
    df[out_col] = (df[tools_col] * df[p_auto_col]) / df[hours_col]
    df[out_col] = df[out_col] * scale
    return df


if __name__ == "__main__":
    # Quick interactive example
    example = compute_tls(n_tools=6, p_auto=0.35, labor_hours_month=800)
    print("Example TLS (n_tools=6, p_auto=0.35, labor_hours_month=800):", example)
