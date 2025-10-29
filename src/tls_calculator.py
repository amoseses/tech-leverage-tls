import pandas as pd

def compute_tls_row(n_tools, p_auto, labor_hours_month, frequency_proxy=1.0, scale=1000.0):
    """Compute TLS per row. frequency_proxy expected 0..1 or relative numeric."""
    if labor_hours_month is None or labor_hours_month <= 0:
        raise ValueError("labor_hours_month must be > 0")
    # default p_auto to frequency proxy if p_auto missing
    if p_auto is None or p_auto == "" or (isinstance(p_auto, float) and pd.isna(p_auto)):
        p_auto = frequency_proxy
    # enforce bounds
    try:
        p_auto = float(p_auto)
    except Exception:
        p_auto = float(frequency_proxy)
    if p_auto < 0:
        p_auto = 0.0
    tls_raw = (float(n_tools) * float(p_auto)) / float(labor_hours_month)
    return float(tls_raw * scale)

def compute_tls_df(df, tools_col='tools_count', p_auto_col='p_auto', freq_col='tools_frequency_of_use_numeric',
                   hours_col='monthly_labor_hours_2025_total', out_col='tls'):
    df = df.copy()
    # coerce
    df[tools_col] = pd.to_numeric(df.get(tools_col, 0), errors='coerce').fillna(0)
    df[freq_col] = pd.to_numeric(df.get(freq_col, 0), errors='coerce').fillna(0)
    df[hours_col] = pd.to_numeric(df.get(hours_col, 1), errors='coerce').fillna(1)
    # if p_auto column exists, coerce, else fill NaNs with 0
    if p_auto_col in df.columns:
        df[p_auto_col] = pd.to_numeric(df.get(p_auto_col), errors='coerce')
    else:
        df[p_auto_col] = pd.Series([float('nan')]*len(df))

    # normalize frequency if necessary (if >1 assume it's scale up to 10)
    freq_max = df[freq_col].replace(0, pd.NA).max()
    if pd.notna(freq_max) and freq_max > 1:
        df[freq_col] = df[freq_col] / freq_max

    # compute TLS
    tls_vals = []
    for _, row in df.iterrows():
        n_tools = row[tools_col]
        p_auto = row[p_auto_col] if not pd.isna(row[p_auto_col]) else row[freq_col]
        freq = row[freq_col]
        hours = row[hours_col]
        tls_val = compute_tls_row(n_tools=n_tools, p_auto=p_auto, labor_hours_month=hours, frequency_proxy=freq, scale=1000.0)
        tls_vals.append(tls_val)
    df[out_col] = tls_vals
    return df
