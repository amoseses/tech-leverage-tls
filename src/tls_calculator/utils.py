"""
Utility helpers for TLS loading and sanitization.
"""

def map_frequency_to_numeric(value):
    """
    Convert textual frequency to a numeric proxy in range 0..1.
    Accepts numeric strings (1-10 or 0-1), percents '50%' or words.
    """
    if value is None:
        return 0.0
    v = str(value).strip().lower()
    if v == '':
        return 0.0
    # handle percent strings like '35%'
    if v.endswith('%'):
        try:
            num = float(v.replace('%', ''))
            return max(0.0, min(1.0, num / 100.0))
        except Exception:
            return 0.0
    # common words
    mapping = {
        'daily': 1.0,
        'everyday': 1.0,
        'always': 1.0,
        'weekly': 1.0/7.0,
        'monthly': 1.0/30.0,
        'rarely': 0.01,
        'occasionally': 0.05,
        'sometimes': 0.1
    }
    if v in mapping:
        return mapping[v]
    # try numeric
    try:
        num = float(v)
        # if user supplied a 1-10 scale, convert to 0-1 by dividing by 10
        if num > 1 and num <= 10:
            return max(0.0, min(1.0, num / 10.0))
        # if it's already 0..1, return as-is, else if between 1 and 100 treat as percent
        if 0 <= num <= 1:
            return num
        if 1 < num <= 100:
            return max(0.0, min(1.0, num / 100.0))
    except Exception:
        pass
    return 0.0

def normalize_tools_list(s):
    """
    Given a string like "Shopify, QuickBooks, Zapier", return the count of distinct non-empty tools.
    Also standardize separators and strip whitespace.
    """
    if s is None:
        return 0
    try:
        items = [it.strip().lower() for it in str(s).split(',') if it.strip() != '']
        # deduplicate
        uniq = sorted(set(items))
        return len(uniq)
    except Exception:
        return 0
