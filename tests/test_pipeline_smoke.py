import pandas as pd
from pathlib import Path
from src.io_helpers import ensure_dirs

def test_pipeline_creates_output(tmp_path):
    # Setup minimal raw CSV in tmp_path
    csv = tmp_path / "raw.csv"
    csv.write_text("firm_name,employees_fte,tech_tools_list,monthly_labor_hours_2025_total,monthly_revenue_2025_01\nMoes,2,Shopify,960,12000\n")
    ensure_dirs()
    # Import and run pipeline functions directly
    from src.data_loader import load_raw_csv, sanitize_and_standardize, save_processed
    from src.tls_calculator import compute_tls_df
    raw = load_raw_csv(str(csv))
    processed = sanitize_and_standardize(raw)
    processed = compute_tls_df(processed)
    assert 'tls' in processed.columns
