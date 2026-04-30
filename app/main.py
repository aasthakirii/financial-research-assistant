from fastapi import FastAPI
from pydantic import BaseModel

from data import fetch_company_data
from db import init_db, get_cache, save_cache
from llm import generate_summary

app = FastAPI()

init_db()


class TickerRequest(BaseModel):
    ticker: str


@app.get("/")
def home():
    return {"message": "Financial Research Assistant API Running"}


@app.post("/analyze")
def analyze(request: TickerRequest):
    ticker = request.ticker.upper()

    # Check cache first
    cached_data = get_cache(ticker)
    if cached_data:
        return {
            "ticker": ticker,
            "analysis": cached_data
        }

    # Fetch company data
    company_data = fetch_company_data(ticker)

    if not company_data:
        return {
            "error": f"Could not fetch data for {ticker}"
        }

    # Generate summary
    summary = generate_summary(company_data)

    # Save to cache
    save_cache(ticker, summary)

    return {
        "ticker": ticker,
        "analysis": summary
    }