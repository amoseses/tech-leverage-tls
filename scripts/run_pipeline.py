"""
Usage:
    python scripts/run_pipeline.py data/raw/intake_2025_sample.csv
"""
import sys
from src.io_helpers import ensure_dirs
from src.data_loader import load_raw_csv, sanitize_and_standardize, save_processed
from src.tls_calculator import compute_tls_df
from pathlib import Path

def run(input_csv):
    ensure_dirs()
    print("Loading", input_csv)
    raw = load_raw_csv(input_csv)
    print("Sanitizing...")
    processed = sanitize_and_standardize(raw)
    print("Computing TLS...")
    processed = compute_tls_df(processed)
    out = Path("data/processed/with_tls.csv")
    save_processed(processed, str(out))
    print("Saved processed to", out)
    print(processed[['firm_id', 'firm_name', 'tls']].head())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("Usage: python scripts/run_pipeline.py path/to/raw.csv")
