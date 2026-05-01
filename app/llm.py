def generate_summary(data):
    company = data.get("company_name", "Unknown")
    sector = data.get("sector", "N/A")
    industry = data.get("industry", "N/A")
    market_cap = data.get("market_cap", 0)
    current_price = data.get("current_price", "N/A")
    pe_ratio = data.get("pe_ratio", "N/A")
    high_52 = data.get("fifty_two_week_high", "N/A")
    low_52 = data.get("fifty_two_week_low", "N/A")
    dividend = data.get("dividend_yield", "N/A")
    summary = data.get("summary", "No summary available.")

    # Recommendation logic
    recommendation = "HOLD"
    recommendation_reason = "Moderate financial outlook."

    if market_cap > 500_000_000_000:
        recommendation = "BUY"
        recommendation_reason = (
            "Large-cap company with strong market dominance and stability."
        )

    elif market_cap < 10_000_000_000:
        recommendation = "RISKY"
        recommendation_reason = (
            "Smaller market cap may indicate higher volatility."
        )

    # Risk logic
    risk_level = "Medium"

    if market_cap > 500_000_000_000:
        risk_level = "Low"

    elif market_cap < 10_000_000_000:
        risk_level = "High"

    dividend_display = (
        f"{round(dividend * 100, 2)}%"
        if isinstance(dividend, (int, float))
        else "N/A"
    )

    return f"""
📌 Company: {company}

🏢 Sector: {sector}

🏭 Industry: {industry}

💰 Market Cap: ${market_cap:,}

💵 Current Price: ${current_price}

📊 P/E Ratio: {pe_ratio}

📈 52 Week High: ${high_52}

📉 52 Week Low: ${low_52}

💸 Dividend Yield: {dividend_display}

⚠️ Risk Level: {risk_level}

📝 Business Summary:
{summary}

🚀 Investment Recommendation: {recommendation}

💡 Why?
{recommendation_reason}
"""