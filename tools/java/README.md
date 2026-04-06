# TLS Scoring Tool — Java Implementation

A standalone implementation of the TLS v1 and v2 scoring 
framework in Java, built as a CS class project demonstrating 
that the TLS formula is simple enough to reimplement without 
the full Python research stack.

## What it does
- Stores 50 technology-sector firms in an ArrayList<Startup>
- Computes TLS v1, TLS v2, Scale-Adjusted TLS, and ROI Proxy
- Filters by industry, funding stage, TLS range, YC batch
- Sorts and ranks firms by any metric
- Adds, removes, updates, and searches firms

## Run it
```bash
javac Startup.java TLSPlatform.java
java TLSPlatform
```

Requires Java 17+. No external dependencies.

## Relationship to the Python pipeline
The Python pipeline in /scripts/ is the authoritative research 
implementation. This Java tool is a portable scoring calculator 
for practitioners who don't need the full analysis stack.
