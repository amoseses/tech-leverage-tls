import pandas as pd
from src.tls_calculator.tls_calculator import compute_tls


def test_compute_tls_math():
    df = pd.DataFrame({
        "annual_tech_spend": [12000],
        "capital_invested": [60000],
        "total_quarterly_labor_hours": [300],
    })

    out = compute_tls(df)

    assert out["tls_raw"].iloc[0] > 0
    assert out["tls_scaled"].iloc[0] == out["tls_raw"].iloc[0] * 1000
