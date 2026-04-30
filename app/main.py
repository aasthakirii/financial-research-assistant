from fastapi import FastAPI
from pydantic import BaseModel

from app.data import fetch_company_data
from app.llm import generate_summary

app = FastAPI()


class Request(BaseModel):
    ticker: str


@app.post("/analyze")
def analyze(req: Request):
    ticker = req.ticker.upper()

    data = fetch_company_data(ticker)

    if "error" in data:
        return {
            "summary": data["error"]
        }

    summary = generate_summary(data)

    return {
        "ticker": ticker,
        "summary": summary
    }