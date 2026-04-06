# Technology Leverage Score (TLS)

A quantitative framework for measuring how efficiently firms 
convert technology investment into productive capacity.

> **TLS = 1000 × (Annual Tech Spend / Total Labor Hours)**

Built on the paper: *"Technology Leverage Score: A Quantitative 
Framework for Measuring Technology Investment Efficiency in Modern 
Firms"* — cross-sectional study of 46 technology-sector firms 
showing larger firms consistently achieve lower technology leverage 
per labor hour (β = −0.0731, p < 0.001).

---

## Repository Map

| Folder | What it is |
|---|---|
| `src/` | Original TLS v1 calculator — preserved for paper reproducibility |
| `scripts/` | Full analysis pipeline (ingest → clean → TLS → regression → output) |
| `data/` | Firm-level CSV inputs |
| `results/` | Pipeline outputs: charts, regression tables, TLS rankings |
| `notebooks/` | Exploratory analysis and figures from the paper |
| `docs/` | Paper PDF and supplementary materials |
| `templates/` | Input CSV schema for data collection |
| `tests/` | Automated test suite |
| `tools/java/` | Standalone TLS scoring tool (Java, no dependencies) |

---

## Quickstart — Run the Analysis Pipeline
```bash
# create virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run tests
pytest -q

# run the full pipeline
# (put your firm CSV in /data first — see /templates for schema)
python scripts/tls_pipeline.py
```

Results land in `/results/`.

---

## Quickstart — Java Scoring Tool
```bash
cd tools/java
javac Startup.java TLSPlatform.java
java TLSPlatform
```

Scores and ranks 50 technology-sector firms. No dependencies. 
Requires Java 17+. See `tools/java/README.md` for details.

---

## The Core Finding

Larger firms show diminishing returns on technology leverage. 
The ratio of tech spend to labor — not absolute spend — is what 
drives operational efficiency.

A firm doubling headcount without scaling its tech budget will 
see TLS decline over time. This is confirmed by both the 
full OLS model (β = −0.0749, p < 0.001) and the employees-only 
robustness check (β = −0.0731, p < 0.001) free of mechanical 
confounding.

---

## TLS v2 (Extended Formula)

Building on v1, TLS v2 incorporates three additional signals:
