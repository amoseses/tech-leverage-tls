import pandas as pd
import numpy as np
from src.tls_calculator.tls_calculator import compute_tls_row, compute_tls_df

def test_compute_tls_row_basic():
    # simple example: 6 tools, 0.35 p_auto, 800 hours -> raw = (6*0.35)/800 = 0.002625 -> scaled 2.625
    val = compute_tls_row(n_tools=6, p_auto=0.35, labor_hours_month=800, frequency_proxy=0.0, scale=1000.0)
    assert np.isclose(val, 2.625, atol=1e-6)

def test_compute_tls_df_on_frame():
    df = pd.DataFrame({
        'firm_id':[1],
        'firm_name':['A'],
        'tools_count':[6],
        'p_auto':[0.35],
        'monthly_labor_hours_2025_total':[800]
    })
    out = compute_tls_df(df)
    assert 'tls' in out.columns
    assert np.isclose(out['tls'].iloc[0], 2.625, atol=1e-6)
