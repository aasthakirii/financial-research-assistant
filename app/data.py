import yfinance as yf


def fetch_company_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        if not info:
            return None

        return {
            "company_name": info.get("longName", ticker),
            "sector": info.get("sector", "Unknown"),
            "industry": info.get("industry", "Unknown"),
            "market_cap": info.get("marketCap", "Unknown"),
            "summary": info.get("longBusinessSummary", "No summary available")
        }

    except Exception as e:
        print("Error fetching data:", e)
        return None