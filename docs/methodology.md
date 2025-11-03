# Methodology

Describe TLS definitions, alternatives, normalization choices, and scoring decisions here.
firm_id — unique id

firm_name — optional (store separately)

sector — categorical (retail, services,…)

founded_year — numeric

employees_fte — numeric (sum of full-time equivalents)

monthly_revenue_2025_01 ... monthly_revenue_2025_12 — numeric, same units (USD)

monthly_labor_hours_2025_total — numeric (sum paid employee hours per month or monthly average)

tools_list / tech_tools_list — comma-separated text

tools_count — integer (# distinct tools)

tools_frequency_of_use — raw text (daily/weekly/1–10) converted to tools_frequency_of_use_numeric

p_auto — estimated proportion of core processes automated (decimal 0–1). If respondents give percent, convert to decimal.

annual_tech_spend — dollar amount (USD/year)

capital_invested — initial capital invested (USD)

profit_margin_percent — percent

online_revenue_share_percent — percent

narrative_notes_for_tech — text

consent_flag — Yes/No
