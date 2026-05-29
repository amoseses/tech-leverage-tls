import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tls_calculator.loading import (
    load_csv,
    sanitize_and_standardize,
    save_processed,
)
from src.tls_calculator.tls_calculator import compute_tls

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/run_pipeline.py <csv_path>")
        sys.exit(1)

    csv_path = sys.argv[1]

    df = load_csv(csv_path)
    df = sanitize_and_standardize(df)
    df = compute_tls(df)

    save_processed(df, "data/processed/with_tls.csv")

    tls_cols = [c for c in df.columns if "tls" in c]
    print(df[["firm_llc_id"] + tls_cols].head())

if __name__ == "__main__":
    main()
