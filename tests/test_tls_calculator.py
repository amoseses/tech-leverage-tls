import pandas as pd
from src.tls_calculator import compute_tls_df

def test_compute_tls_df_basic():
    df = pd.DataFrame({
        'firm_id':[1],
        'firm_name':['A'],
        'tools_count':[6],
        'tools_frequency_of_use_numeric':[1.0],
        'monthly_labor_hours_2025_total':[800],
    })
    out = compute_tls_df(df)
    assert 'tls' in out.columns
    assert round(out['tls'].iloc[0], 6) == round((6*1.0)/800*1000.0, 6)


