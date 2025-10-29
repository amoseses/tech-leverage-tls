"""
Optional: fetch a Google Sheet CSV programmatically using gspread.
Requires a service account JSON credentials file and the sheet id/link.
Use at your own discretion; otherwise download CSV via Sheets UI.

Example usage:
python scripts/fetch_google_sheet.py <google_sheet_csv_export_url> data/raw/intake_2025_sample.csv
"""
import sys
import requests

def fetch(url, outpath):
    r = requests.get(url)
    r.raise_for_status()
    with open(outpath, "wb") as f:
        f.write(r.content)
    print("Wrote", outpath)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scripts/fetch_google_sheet.py <csv_url> <outpath>")
    else:
        fetch(sys.argv[1], sys.argv[2])
