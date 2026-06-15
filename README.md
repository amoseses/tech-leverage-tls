# Technology Leverage Score (TLS)

Technology Leverage Score (TLS) measures how effectively a company converts technology investment into productive labor capacity.

**Formula**

TLS = 1000 × (Technology Spend ÷ Annual Labor Hours)

## What's Included

- Full Python research and analytics pipeline
- Expanded validation dataset pipline - Log-log
- Original study replication (46 firms)
- Regression and benchmarking tools
- Sector analysis and reporting
- Lightweight Java implementation for quick TLS calculations

## Implementations

### Python (Recommended)
The primary and most complete implementation, including:

- Data ingestion and cleaning
- TLS calculation
- Statistical analysis
- Log-log regression models
- Sector benchmarking
- Validation testing

### Java
A lightweight version intended for:

- Quick TLS scoring
- Demonstrations
- Educational use
- Fast local execution

## Key Findings

The expanded validation confirms the original TLS research:

- Technology spend is positively associated with TLS
- Larger firms generally exhibit lower technology leverage when controlling for spend
- Sector-level TLS rankings align with industry expectations
- Original study findings were successfully replicated

## Validation

The pipeline has been validated through:

- Data ingestion testing
- TLS formula verification
- Regression testing
- Outlier analysis
- Sector benchmarking
- Original-study replication

## Future Development

As additional companies are added, TLS benchmarking becomes more robust and useful for:

- Cross-company comparisons
- Industry benchmarking
- Enterprise analytics
- Organizational technology strategy

## Run
Import company data into docs/raw
```bash
pip install -r requirements.txt
python scripts/run_pipeline.py
