import pandas as pd
from src.tls_metric.tls_calculator import compute_tls

def test_tls_computation():
    df = pd.DataFrame({
        'automation_level': [0.6],
        'ai_tools': [2],
        'capital_intensity': [0.4]
    })
    result = compute_tls(df)
    expected = 2*0.6 + 2 - 0.5*0.4  # = 2.8
    assert abs(result['tls_score'].iloc[0] - expected) < 1e-6


