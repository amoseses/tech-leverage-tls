import pandas as pd

def compute_tls(df):
    """
    Compute Technology Leverage Score (TLS)
    TLS = 2*(automation_level) + 1*(ai_tools) - 0.5*(capital_intensity)
    """
    df['tls_score'] = 2*df['automation_level'] + df['ai_tools'] - 0.5*df['capital_intensity']
    return df

if __name__ == "__main__":
    # Example dataset for testing
    data = pd.DataFrame({
        'automation_level': [0.6, 0.8, 0.3],
        'ai_tools': [2, 5, 0],
        'capital_intensity': [0.4, 0.3, 1.2]
    })
    result = compute_tls(data)
    print(result)


