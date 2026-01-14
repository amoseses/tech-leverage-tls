from src.tls_metric.compute import compute_tls
import math
import pytest

def test_compute_tls_example():
    expected = 2.625  # 6 * 0.35 = 2.1; 2.1 / 800 = 0.002625; *1000 = 2.625
    result = compute_tls(6, 0.35, 800)
    assert math.isclose(result, expected, rel_tol=1e-9)

def test_bad_hours_raises():
    with pytest.raises(ValueError):
        compute_tls(3, 0.2, 0)

def test_p_auto_bounds():
    with pytest.raises(ValueError):
        compute_tls(3, -0.1, 100)
    with pytest.raises(ValueError):
        compute_tls(3, 1.1, 100)
