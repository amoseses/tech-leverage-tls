# Utility helpers

def map_frequency_to_numeric(value):
    """
    Convert textual/numeric frequency values to a numeric proxy (0..1 or >0).
    Accepts numeric strings, words like 'daily', 'weekly', 'monthly', or '1-10' scales.
    """
    if value is None:
        return 0.0
    v = str(value).strip().lower()
    mapping = {
        "daily": 1.0,
        "everyday": 1.0,
        "always": 1.0,
        "weekly": 0.25,
        "monthly": 1/30,
        "rarely": 0.01,
        "occasionally": 0.05,
        "sometimes": 0.1
    }
    try:
        # try numeric first
        num = float(v)
        return num
    except Exception:
        return mapping.get(v, 0.0)
