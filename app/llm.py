def generate_summary(data):
    return f"""
Business Overview:
{data['company_name']} operates in the {data['sector']} sector.

Industry:
{data['industry']}

Market Cap:
{data['market_cap']}

Company Summary:
{data['summary']}
"""