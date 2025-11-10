# Data Dictionary – Technology Leverage Score (TLS) Project

| Variable | Description | Type | Example |
|-----------|--------------|------|----------|
| firm_LLC_id | Unique firm identifier | string | ABC123 |
| firm_name | Company name (anonymized if needed) | string | HiveTech |
| sector | Industry or business type | string | Retail |
| founded_year | Year company was founded | integer | 2019 |
| employees_fte | Number of full-time equivalent employees | float | 4.5 |
| monthly_revenue_2025_X | Monthly revenue in USD for month X | float | 24000 |
| monthly_labor_hours_2025_total | Total paid labor hours for 2025 | float | 800 |
| annual_tech_spend | Total annual spend on tech tools/subscriptions | float | 12000 |
| tech_tools_list | List of digital tools used | string | "Shopify, ChatGPT, QuickBooks" |
| tools_frequency_of_use | How often tools are used (Daily, Weekly, etc.) | string | Daily |
| capital_invested | Total invested capital ($) | float | 50000 |
| profit_margin_percent | Profit margin (%) | float | 22 |
| online_revenue_share_percent | % of revenue from online sources | float | 65 |
| narrative_notes_for_tech | Short description of major wins or challenges | text | "Automation reduced manual billing time by 40%" |
| TLS_raw | Computed (N_tools * P_auto / H_month) | float | 0.0021 |
| TLS_scaled | Scaled TLS (TLS_raw * 1000) | float | 2.1 |
