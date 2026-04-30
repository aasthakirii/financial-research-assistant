import yfinance as yf


def fetch_company_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    if not info or info.get("longName") is None:
        return {
            "error": "Invalid ticker symbol. Please enter a valid stock ticker like AAPL or AMZN."
        }

    return {
        "name": info.get("longName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "summary": info.get("longBusinessSummary"),
        "marketCap": info.get("marketCap")
    }