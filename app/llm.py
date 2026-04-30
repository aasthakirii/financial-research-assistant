def generate_summary(data):
    company_name = data.get("name", "Unknown Company")
    sector = data.get("sector", "Unknown Sector")
    industry = data.get("industry", "Unknown Industry")

    return f"""
Business Overview:
{company_name} operates in the {sector} sector.

Recent Material Events:
- No recent events available from current data source.

Key Risks:
- Market volatility
- Competitive pressure
- Regulatory risks

Market Position:
Company operates in the {industry} industry.
"""