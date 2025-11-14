#!/usr/bin/env python3
"""
Run the end-to-end TLS pipeline for a single CSV file.

Usage:
    PYTHONPATH=. python scripts/run_pipeline.py data/raw/sample_intake_2025.csv
"""

import sys
import os
from pathlib import Path

# ensure repo root is on path when running directly
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_pipeline.py path/to/raw.csv")
        sys.exit(1)

    raw_csv = Path(sys.argv[1])
    if not raw_csv.exists():
        print(f"ERROR: Input file not found: {raw_csv}")
        sys.exit(1)

    # import pipeline pieces (inside repo)
    from src.tls_calculator.loading import load_raw_csv, sanitize_and_standardize, save_processed
    from src.tls_calculator.tls_calculator import compute_tls_df
    from src.io_helpers import ensure_dirs

    ensure_dirs()

    print("Loading raw CSV:", raw_csv)
    raw_df = load_raw_csv(str(raw_csv))

    print("Sanitizing and standardizing...")
    processed_df = sanitize_and_standardize(raw_df)

    print("Computing TLS...")
    processed_df = compute_tls_df(processed_df)

    outpath = Path("data/processed/with_tls.csv")
    save_processed(processed_df, str(outpath))
    print("Saved processed file to:", outpath)
    print(processed_df[['firm_id','firm_name'] + [c for c in processed_df.columns if 'tls' in c.lower()]].head())

if __name__ == "__main__":
    main()
