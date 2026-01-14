import pandas as pd

def compute_tls(df: pd.DataFrame) -> pd.DataFrame:
    print("Computing TLS...")

    df = df.copy()

    # number of tools proxy
    df["n_tools"] = df["tech_tools_list"].fillna("").apply(
        lambda x: len([t for t in str(x).split(",") if t.strip()])
    )

    # TLS definition
    df["tls_raw"] = (
        df["n_tools"] * df["annual_tech_spend"]
    ) / df["total_quarterly_labor_hours"].replace(0, 1)

    df["tls_scaled"] = df["tls_raw"] * 1000

    return df
