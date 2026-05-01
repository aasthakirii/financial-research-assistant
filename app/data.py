import yfinance as yf


def fetch_company_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "company_name": info.get("longName", ticker),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "market_cap": info.get("marketCap", 0),
            "current_price": info.get("currentPrice", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "fifty_two_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
            "fifty_two_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A"),
            "summary": info.get("longBusinessSummary", "No summary available."),
        }

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None