# Technology Leverage Score (TLS)

A quantitative framework for measuring how efficiently firms 
convert technology investment into productive capacity.

> **TLS = 1000 × (Annual Tech Spend / Total Labor Hours)**

Built on the paper: *"Technology Leverage Score: A Quantitative 
Framework for Measuring Technology Investment Efficiency in Modern 
Firms"* — cross-sectional study of 46 technology-sector firms showing 
larger firms consistently achieve lower technology leverage per labor 
hour (β = −0.0731, p < 0.001).

## What this repo contains

- **Full analysis pipeline** — put your firm data in `/data`, 
  run the pipeline, get TLS scores, regression output, and charts 
  in `/results`
- **Test suite + CI** — automated tests run on every push
- **Notebooks** — exploratory analysis and figures from the paper
- **Java scoring tool** — standalone TLS calculator for 50 YC 
  companies, no dependencies (`tools/java/`)

## Quickstart
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## The finding

Larger firms show diminishing returns on technology leverage. 
The ratio of tech spend to labor — not absolute spend — is what 
drives operational efficiency. A firm doubling headcount without 
scaling its tech budget will see TLS decline.

## Data

`/data` accepts firm-level CSV with: employees, annual tech spend, 
total labor hours, industry, funding stage. See `/templates` for 
the input schema.

## Status

Year 1 dataset: 46 firms. Expanding to 150+ firms for Year 2 
annual report (Summer 2025).
