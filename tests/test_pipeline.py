import pandas as pd
from pathlib import Path
from src.tls_calculator.loading import sanitize_and_standardize
from src.tls_calculator.tls_calculator import compute_tls

def test_pipeline_smoke(tmp_path):
    raw_csv = tmp_path / "raw.csv"
    raw_csv.write_text(
        "firm_llc_id,sector,founded_year,employees_fte,annual_tech_spend,capital_invested,"
        "profit_margin_percent,online_revenue_share_percent,total_quarterly_labor_hours,"
        "tech_tools_list,tools_frequency_of_use\n"
        "moes-lawn,Services,2010,5,12000,60000,10,50,960,Shopify,High\n"
    )
    df = pd.read_csv(raw_csv)
    sanitized = sanitize_and_standardize(df)
    processed = compute_tls(sanitized)
    assert 'tls_raw' in processed.columns
    assert processed['tls_raw'].notnull().any()
