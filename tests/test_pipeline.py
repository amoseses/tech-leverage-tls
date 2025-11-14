import pandas as pd
from pathlib import Path
from src.tls_calculator.loading import sanitize_and_standardize
from src.tls_calculator.tls_calculator import compute_tls_df

def test_pipeline_smoke(tmp_path):
    # create a minimal raw CSV content
    raw_csv = tmp_path / "raw.csv"
    raw_csv.write_text(
        "firm_name,tech_tools_list,monthly_labor_hours_2025_total,p_auto,monthly_revenue_2025_11\n"
        "Moes Lawn,Shopify,960,0.2,12000\n"
    )
    df = pd.read_csv(raw_csv)
    sanitized = sanitize_and_standardize(df)
    processed = compute_tls_df(sanitized)
    assert 'tls' in processed.columns
    assert processed['tls'].notnull().any()
